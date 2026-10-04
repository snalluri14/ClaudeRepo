"""Jarvis: a voice assistant that plans your day from Notion.

    python jarvis.py dump      # talk about your day; Jarvis updates your Notion tasks
    python jarvis.py plan      # Jarvis builds today's plan and reads it to you
    python jarvis.py ask       # ask anything about your tasks ("what's overdue?")

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
}


# ---------------------------------------------------------------- voice in --

def record() -> "numpy.ndarray":
    """Record from the default microphone until Enter is pressed."""
    import numpy as np
    import sounddevice as sd

    chunks = []
    stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32",
                            callback=lambda data, *_: chunks.append(data.copy()))
    input("Press Enter to start talking...")
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
    if mode == "plan":
        return ""  # nothing to say, Jarvis reads Notion
    if typed:
        print("Type your input. Finish with an empty line.")
        lines = []
        while (line := input()) != "":
            lines.append(line)
        return "\n".join(lines)
    text = transcribe(record())
    print(f"\nYou said: {text}\n")
    return text


# ------------------------------------------------------------------- brain --

def ask_claude(mode: str, said: str) -> str:
    if not shutil.which("claude"):
        sys.exit("Claude Code isn't installed. See README.md.")

    now = datetime.now()
    message = f"Now: {now:%A %B %d, %Y %H:%M}.\n\n{REQUESTS[mode]}"
    if said:
        message += f"\n\nWhat I said:\n\"\"\"\n{said}\n\"\"\""

    cmd = [
        "claude", "-p", message,
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


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("mode", choices=list(REQUESTS))
    parser.add_argument("--text", action="store_true", help="type instead of speaking")
    parser.add_argument("--quiet", action="store_true", help="don't speak the reply")
    args = parser.parse_args()

    said = get_input(args.mode, args.text)
    if args.mode != "plan" and not said.strip():
        sys.exit("I didn't catch anything. Try again.")

    reply = ask_claude(args.mode, said)
    print(f"\nJarvis: {reply}\n")
    log(args.mode, said, reply)
    if not args.quiet:
        speak(reply)


if __name__ == "__main__":
    main()
