"""Jarvis: a voice assistant that plans your day from Notion.

    python jarvis.py dump      # talk about your day; Jarvis updates your Notion tasks
    python jarvis.py plan      # Jarvis builds today's plan and reads it to you
    python jarvis.py ask       # ask anything about your tasks ("what's overdue?")
    python jarvis.py review    # where you're falling short, with evidence and drills
    python jarvis.py coach     # a spoken practice session on your weakest area
    python jarvis.py coach "handling pricing objections"   # or pick the topic

Add --text to type instead of speaking, --quiet to skip the voice reply.

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

# Claude may only touch Notion. Everything else is denied for privacy and safety.
ALLOWED_TOOLS = ["mcp__notion"]
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
    "coach": (
        "Start a coaching session. Pick my current focus skill from the growth tracker "
        "(or the topic I name), tell me in one or two sentences what we'll practice and "
        "why, then give me the first exercise or question and wait for my answer."
    ),
}
COACH_WRAP_UP = (
    "End the session now. Give me my score for this session, the one thing I did well, "
    "the one thing to fix, and the drill to practice before next time. Log the session "
    "in the growth tracker."
)
STOP_WORDS = {"q", "quit", "stop", "done", "end", "exit"}


# ---------------------------------------------------------------- voice in --

def record(allow_quit: bool = False):
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


def transcribe(audio) -> str:
    """Transcribe locally with openai-whisper, or faster-whisper if that's what's installed."""
    print("Transcribing on this laptop...")
    try:
        import whisper
        model = whisper.load_model(WHISPER_MODEL)
        return model.transcribe(audio, fp16=False)["text"].strip()
    except ImportError:
        pass
    try:
        from faster_whisper import WhisperModel
        model = WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8")
        segments, _ = model.transcribe(audio)
        return " ".join(s.text.strip() for s in segments)
    except ImportError:
        sys.exit("Whisper isn't installed. Run: pip install openai-whisper")


def get_input(mode: str, typed: bool) -> str:
    if mode in ("plan", "review", "coach"):
        return ""  # nothing to say, Jarvis reads Notion
    return listen(typed) or ""


def listen(typed: bool, allow_quit: bool = False):
    """One turn of input. Returns None when the user asks to finish."""
    if typed:
        hint = " Type q to finish." if allow_quit else ""
        print(f"Type your input. Finish with an empty line.{hint}")
        lines = []
        while (line := input()) != "":
            lines.append(line)
        text = "\n".join(lines)
        return None if allow_quit and text.strip().lower() in STOP_WORDS else text
    audio = record(allow_quit)
    if audio is None:
        return None
    text = transcribe(audio)
    print(f"\nYou said: {text}\n")
    return text


# ------------------------------------------------------------------- brain --

def ask_claude(mode: str, said: str, session: str = None, resume: bool = False) -> str:
    """Send one message. Pass session to start (or, with resume, continue) a conversation."""
    if not shutil.which("claude"):
        sys.exit("Claude Code isn't installed. See README.md.")

    if resume and said == COACH_WRAP_UP:
        message = said
    elif resume:
        message = f"What I said:\n\"\"\"\n{said}\n\"\"\""
    else:
        now = datetime.now()
        message = f"Now: {now:%A %B %d, %Y %H:%M}.\n\n{REQUESTS[mode]}"
        if said:
            label = "Topic I want to practice" if mode == "coach" else "What I said"
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


def coach(topic: str, typed: bool, quiet: bool):
    """A back-and-forth practice session that keeps context between turns."""
    session = str(uuid.uuid4())
    respond("coach", topic, ask_claude("coach", topic, session), quiet)
    while (said := listen(typed, allow_quit=True)) is not None:
        if said.strip():
            respond("coach", said, ask_claude("coach", said, session, resume=True), quiet)
    respond("coach", "(end of session)",
            ask_claude("coach", COACH_WRAP_UP, session, resume=True), quiet)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("mode", choices=list(REQUESTS))
    parser.add_argument("topic", nargs="?", default="", help="coach only: what to practice")
    parser.add_argument("--text", action="store_true", help="type instead of speaking")
    parser.add_argument("--quiet", action="store_true", help="don't speak the reply")
    args = parser.parse_args()

    if args.mode == "coach":
        coach(args.topic, args.text, args.quiet)
        return

    said = get_input(args.mode, args.text)
    if args.mode in ("dump", "ask") and not said.strip():
        sys.exit("I didn't catch anything. Try again.")
    respond(args.mode, said, ask_claude(args.mode, said), args.quiet)


if __name__ == "__main__":
    main()
