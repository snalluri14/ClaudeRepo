"""Jarvis: a voice assistant that plans your day from Notion.

    python jarvis.py talk      # a spoken conversation: plan, update tasks, ask, practice
    python jarvis.py dump      # talk about your day; Jarvis updates your Notion tasks
    python jarvis.py plan      # Jarvis builds today's plan and reads it to you
    python jarvis.py ask       # ask anything about your tasks ("what's overdue?")
    python jarvis.py review    # where you're falling short, with evidence and drills
    python jarvis.py coach     # a spoken practice session on your weakest area
    python jarvis.py coach "handling pricing objections"   # or pick the topic

Jarvis stops listening when you pause. Say "goodbye" (or press Ctrl+C) to end a
conversation. Add --manual to press Enter to start and stop talking instead,
--text to type, and --quiet to skip the voice reply.

Privacy and cost:
  * Your voice is recorded and transcribed on this laptop with Whisper. Audio is never uploaded.
  * Only the transcript text goes to Claude, through the Claude Code CLI signed in with
    your Claude subscription, so there's no API bill.
  * Claude reads and writes your tasks through Notion's official MCP server. It may use
    only the Notion tools; shell, file and web tools are blocked.
  * The reply is spoken by a local voice (Piper if configured, otherwise your OS voice).
  * Every transcript and reply is also saved to journal/ on this laptop.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import uuid
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROMPT_FILE = ROOT / "prompts" / "jarvis.md"
JOURNAL = ROOT / "journal"

SAMPLE_RATE = 16000  # what Whisper expects
WHISPER_MODEL = os.environ.get("JARVIS_WHISPER_MODEL", "base")  # tiny/base/small/medium
CLAUDE_MODEL = os.environ.get("JARVIS_MODEL", "sonnet")
PIPER_VOICE = os.environ.get("JARVIS_PIPER_VOICE")  # path to a Piper .onnx voice file

# Auto-stop: Jarvis stops recording after this many seconds of silence once you've
# started speaking. Raise it if Jarvis cuts you off mid-thought.
SILENCE_SECONDS = float(os.environ.get("JARVIS_SILENCE_SECONDS", "2.0"))
WAIT_FOR_SPEECH_SECONDS = 15  # give up if you say nothing for this long
MAX_TURN_SECONDS = 300        # hard cap on one turn, so a noisy room can't record forever

# Claude may only touch Notion. Everything else is denied for privacy and safety.
# "notion" is the server from `claude mcp add`; "Notion" and "claude_ai_Notion" are the Notion
# connector from your claude.ai account, if you connected it there instead.
ALLOWED_TOOLS = ["mcp__notion", "mcp__Notion", "mcp__claude_ai_Notion"]
BLOCKED_TOOLS = ["Bash", "Edit", "Write", "NotebookEdit", "WebFetch", "WebSearch"]

REQUESTS = {
    "dump": (
        "Here is my brain dump. Update my Notion tasks from it: mark finished tasks Done, "
        "add new tasks, change dates and priorities I mention, and add a short entry to "
        "today's journal page. Then give me the spoken confirmation."
    ),
    "plan": (
        "Plan my day. Read my open tasks, build today's plan, save it as today's plan page "
        "in Notion, and give me the spoken briefing."
    ),
    "ask": "Answer my question using my Notion tasks. Change tasks only if I ask you to.",
    "review": (
        "Run my growth review. Look at my tasks, daily pages and growth tracker from the "
        "last 14 days, find where I'm falling short, update the growth tracker, save the "
        "review page, and give me the spoken review."
    ),
    "talk": (
        "Start a conversation. Check my tasks, greet me in one short sentence with the "
        "single most important thing right now, and ask what I need. Then keep talking "
        "with me: update tasks, plan, answer questions or coach me, whatever I ask."
    ),
    "coach": (
        "Start a coaching session. Pick my current focus skill from the growth tracker "
        "(or the topic I name), tell me in one or two sentences what we'll practice and "
        "why, then give me the first exercise or question and wait for my answer."
    ),
}
TALK_WRAP_UP = "I'm done for now. Say a one-sentence goodbye, and remind me of the next thing to do."
COACH_WRAP_UP = (
    "End the session now. Give me my score for this session, the one thing I did well, "
    "the one thing to fix, and the drill to practice before next time. Log the session "
    "in the growth tracker."
)
STOP_WORDS = {"q", "quit", "stop", "done", "end", "exit"}
# Spoken phrases that end a conversation, when they make up a short utterance.
GOODBYES = ("goodbye", "bye", "that's all", "that is all", "that's it", "we're done",
            "stop", "end session", "end the session", "exit", "quit", "see you")
CONVERSATIONS = ("talk", "coach")


# ---------------------------------------------------------------- voice in --

def record_manual(allow_quit: bool = False):
    """Record from the default microphone until Enter is pressed.

    With allow_quit, typing q (or stop/done) instead of Enter returns None.
    """
    import numpy as np
    import sounddevice as sd

    chunks = []
    stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32",
                            callback=lambda data, *_: chunks.append(data.copy()))
    hint = " (or type q to finish)" if allow_quit else ""
    if input(f"Press Enter to start talking{hint}... ").strip().lower() in STOP_WORDS:
        return None
    with stream:
        input("Listening. Press Enter when you're done.")
    if not chunks:
        return np.zeros(0, dtype="float32")
    return np.concatenate(chunks).flatten()


def record_auto():
    """Record from the default microphone, stopping when you pause.

    The first half second sets the room's noise level. Speech is anything clearly
    louder than that. Returns an empty array if you never start speaking.
    """
    import numpy as np
    import sounddevice as sd

    block = int(SAMPLE_RATE * 0.1)  # 100 ms blocks
    chunks, noise, spoke, quiet_blocks = [], [], False, 0
    silence_blocks = int(SILENCE_SECONDS * 10)
    print("Listening... (just talk, I'll stop when you pause)")
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32") as stream:
        for i in range(MAX_TURN_SECONDS * 10):
            data, _ = stream.read(block)
            level = float(np.sqrt(np.mean(data ** 2)))
            if i < 5:
                noise.append(level)
                continue
            threshold = max(np.mean(noise) * 3, 0.01)
            if level > threshold:
                spoke, quiet_blocks = True, 0
            elif spoke:
                quiet_blocks += 1
            if spoke:
                chunks.append(data.copy())
                if quiet_blocks >= silence_blocks:
                    break
            elif i >= WAIT_FOR_SPEECH_SECONDS * 10:
                break
    if not chunks:
        return np.zeros(0, dtype="float32")
    return np.concatenate(chunks).flatten()


_whisper = None


def transcribe(audio) -> str:
    """Transcribe locally with openai-whisper, or faster-whisper if that's what's installed.

    The model is loaded once and reused, so later turns in a conversation are faster.
    """
    global _whisper
    if len(audio) < SAMPLE_RATE // 2:  # under half a second: nothing worth transcribing
        return ""
    print("Transcribing on this laptop...")
    if _whisper is None:
        try:
            import whisper
            model = whisper.load_model(WHISPER_MODEL)
            _whisper = lambda a: model.transcribe(a, fp16=False)["text"].strip()
        except ImportError:
            try:
                from faster_whisper import WhisperModel
                model = WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8")
                _whisper = lambda a: " ".join(seg.text.strip() for seg in model.transcribe(a)[0])
            except ImportError:
                sys.exit("Whisper isn't installed. Run: pip install openai-whisper")
    return _whisper(audio)


def is_goodbye(text: str) -> bool:
    words = re.findall(r"[a-z']+", text.lower().replace("’", "'"))
    short = f" {' '.join(words)} "
    return len(words) <= 5 and any(f" {phrase} " in short for phrase in GOODBYES)


def get_input(mode: str, input_mode: str) -> str:
    if mode in ("plan", "review"):
        return ""  # nothing to say, Jarvis reads Notion
    return listen(input_mode) or ""


def listen(input_mode: str, allow_quit: bool = False):
    """One turn of input: "auto" (voice, stops on a pause), "manual" (voice, Enter to
    stop) or "text". Returns None when the user asks to finish."""
    typed = input_mode == "text"
    if typed:
        hint = " Type q to finish." if allow_quit else ""
        print(f"Type your input. Finish with an empty line.{hint}")
        lines = []
        while (line := input()) != "":
            lines.append(line)
        text = "\n".join(lines)
        if allow_quit and (text.strip().lower() in STOP_WORDS or is_goodbye(text)):
            return None
        return text
    audio = record_auto() if input_mode == "auto" else record_manual(allow_quit)
    if audio is None:
        return None
    text = transcribe(audio)
    if text:
        print(f"\nYou said: {text}\n")
    if allow_quit and text and is_goodbye(text):
        return None
    return text


# ------------------------------------------------------------------- brain --

def ask_claude(mode: str, said: str, session: str = None, resume: bool = False) -> str:
    """Send one message. Pass session to start (or, with resume, continue) a conversation."""
    if not shutil.which("claude"):
        sys.exit("Claude Code isn't installed. See README.md.")

    if resume and said in (COACH_WRAP_UP, TALK_WRAP_UP):
        message = said
    elif resume:
        message = f"What I said:\n\"\"\"\n{said}\n\"\"\""
    else:
        now = datetime.now()
        message = f"Now: {now:%A %B %d, %Y %H:%M}.\n\n{REQUESTS[mode]}"
        if said:
            label = {"coach": "Topic I want to practice",
                     "talk": "What I want to start with"}.get(mode, "What I said")
            message += f"\n\n{label}:\n\"\"\"\n{said}\n\"\"\""

    cmd = ["claude", "-p", message]
    if session:
        cmd += ["--resume" if resume else "--session-id", session]
    cmd += [
        "--model", CLAUDE_MODEL,
        "--append-system-prompt-file", str(PROMPT_FILE),
        "--allowedTools", *ALLOWED_TOOLS,
        "--disallowedTools", *BLOCKED_TOOLS,
        "--output-format", "text",
    ]
    print("Jarvis is thinking...")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if result.returncode != 0:
        sys.exit(f"Claude Code failed:\n{result.stderr or result.stdout}")
    return result.stdout.strip()


# --------------------------------------------------------------- voice out --

def speak(text: str):
    if PIPER_VOICE and shutil.which("piper"):
        wav = JOURNAL / "last_reply.wav"
        subprocess.run(["piper", "--model", PIPER_VOICE, "--output_file", str(wav)],
                       input=text, text=True, check=True, capture_output=True)
        play(wav)
        return
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate", 185)
        engine.say(text)
        engine.runAndWait()
    except Exception as exc:  # no voice available; the text is already on screen
        print(f"(Couldn't speak: {exc})")


def play(wav: Path):
    import sounddevice as sd
    import soundfile as sf
    data, rate = sf.read(wav)
    sd.play(data, rate)
    sd.wait()


# -------------------------------------------------------------------- main --

def log(mode: str, said: str, reply: str):
    JOURNAL.mkdir(exist_ok=True)
    now = datetime.now()
    with open(JOURNAL / f"{now:%Y-%m-%d}.md", "a", encoding="utf-8") as f:
        f.write(f"\n## {now:%H:%M} {mode}\n\n")
        if said:
            f.write(f"**Me:** {said}\n\n")
        f.write(f"**Jarvis:** {reply}\n")


def respond(mode: str, said: str, reply: str, quiet: bool):
    print(f"\nJarvis: {reply}\n")
    log(mode, said, reply)
    if not quiet:
        speak(reply)


def converse(mode: str, topic: str, input_mode: str, quiet: bool):
    """A back-and-forth conversation that keeps context between turns (talk or coach)."""
    session = str(uuid.uuid4())
    respond(mode, topic, ask_claude(mode, topic, session), quiet)
    misses = 0
    while True:
        try:
            said = listen(input_mode, allow_quit=True)
        except (KeyboardInterrupt, EOFError):
            said = None
        if said is None:
            break
        if not said.strip():
            misses += 1
            if misses >= 2:  # silence twice in a row: assume you've walked away
                print("I didn't hear anything, so I'm wrapping up.")
                break
            print("I didn't catch that. Go ahead whenever you're ready.")
            continue
        misses = 0
        respond(mode, said, ask_claude(mode, said, session, resume=True), quiet)
    wrap_up = COACH_WRAP_UP if mode == "coach" else TALK_WRAP_UP
    respond(mode, "(end of conversation)", ask_claude(mode, wrap_up, session, resume=True), quiet)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("mode", choices=list(REQUESTS))
    parser.add_argument("topic", nargs="?", default="",
                        help="talk/coach: what to start with, such as a skill to practice")
    parser.add_argument("--text", action="store_true", help="type instead of speaking")
    parser.add_argument("--manual", action="store_true",
                        help="press Enter to start and stop talking instead of auto-stop")
    parser.add_argument("--quiet", action="store_true", help="don't speak the reply")
    args = parser.parse_args()

    input_mode = "text" if args.text else "manual" if args.manual else "auto"

    if args.mode in CONVERSATIONS:
        converse(args.mode, args.topic, input_mode, args.quiet)
        return

    said = get_input(args.mode, input_mode)
    if args.mode in ("dump", "ask") and not said.strip():
        sys.exit("I didn't catch anything. Try again.")
    respond(args.mode, said, ask_claude(args.mode, said), args.quiet)


if __name__ == "__main__":
    main()
