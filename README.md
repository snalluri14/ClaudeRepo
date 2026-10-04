# Jarvis: voice planner on your Claude subscription

Jarvis tracks your work and personal tasks in Notion. You talk to it, it updates your tasks, and every morning it plans your day and reads the plan aloud.

Everything Jarvis needs is on this branch. It doesn't need an API key.

| Command | What it does |
|---|---|
| `python jarvis.py dump` | Talk freely about your day. Jarvis marks tasks done, adds new ones, moves dates, and journals it. |
| `python jarvis.py plan` | Jarvis builds today's plan (up to 3 priorities, quick wins, risks), saves it to Notion, and reads it to you. |
| `python jarvis.py ask` | Ask a question, such as "what's overdue?" or "what's left for the Negen launch?" |

Add `--text` to type instead of talking, or `--quiet` for no voice reply.

## Why it's cheap and private

| Step | Runs where | Cost |
|---|---|---|
| Recording + Whisper speech-to-text | Your laptop. Audio never leaves it. | Free |
| Thinking (Claude) | Claude Code CLI signed in with **your Claude subscription**. Only the transcript text is sent. | Included in your plan |
| Task storage | Your Notion workspace, through Notion's official MCP server | Free |
| Voice reply | Your laptop (Piper or the OS voice) | Free |
| Journal of every transcript and reply | `journal/` on your laptop (not committed to git) | Free |

Claude may only use the Notion tools. Shell, file-editing and web tools are blocked.

## Setup (about 15 minutes, one time)

1. **Install Claude Code and sign in with your subscription:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   claude            # choose "Claude account with subscription" and log in, then /exit
   ```
   Make sure `ANTHROPIC_API_KEY` is **not** set in this terminal. Otherwise Claude Code bills the API instead of your subscription.

2. **Connect Notion:**
   ```bash
   claude mcp add --scope user --transport http notion https://mcp.notion.com/mcp
   claude            # type /mcp, pick notion, approve access in the browser, then /exit
   ```

3. **Install the voice packages:**
   ```bash
   git clone -b jarvis-only https://github.com/snalluri14/ClaudeRepo.git jarvis
   cd jarvis
   pip install -r requirements.txt
   ```
   On Linux you may also need `sudo apt install portaudio19-dev espeak-ng`.

4. **Optional: a natural local voice with Piper.** Run `pip install piper-tts`, download a voice such as `en_US-lessac-medium.onnx` and its `.json` file from the [Piper voices list](https://huggingface.co/rhasspy/piper-voices), then:
   ```bash
   export JARVIS_PIPER_VOICE=/path/to/en_US-lessac-medium.onnx
   ```

5. **First run:** `python jarvis.py dump --text` and type a few tasks. Jarvis creates a **Jarvis** page in Notion with a **Jarvis Tasks** database and one page per day.

## Settings

| Variable | Default | Notes |
|---|---|---|
| `JARVIS_MODEL` | `sonnet` | Use `opus` for deeper planning (uses more of your subscription limit) or `haiku` for speed. |
| `JARVIS_WHISPER_MODEL` | `base` | `small` is more accurate, and slower on older laptops. |
| `JARVIS_PIPER_VOICE` | unset | Path to a Piper `.onnx` voice. Without it, the OS voice is used. |

How Jarvis plans and talks is set in `prompts/jarvis.md`. Edit it freely, for example to allow 5 priorities or add a "health" area.

## Automatic morning briefing

macOS or Linux, weekdays at 8:50 (run `crontab -e`):
```
50 8 * * 1-5 cd /path/to/jarvis && /usr/bin/python3 jarvis.py plan >> journal/cron.log 2>&1
```
Windows: in Task Scheduler, create a daily task that runs `python C:\path\to\jarvis\jarvis.py plan`.

## Daily routine

- **Morning:** `plan`, either scheduled or run by hand.
- **During the day:** a quick `dump` whenever something changes.
- **Evening:** a 2-minute `dump` covering what got done, what slipped, and what's new.

You can also see and edit everything in Notion from your phone. Jarvis picks up your edits next time it runs.

## Files

```
jarvis.py            # record → Whisper → Claude Code + Notion → speak
prompts/jarvis.md    # how Jarvis plans and speaks (edit freely)
requirements.txt     # voice packages
journal/             # local log of transcripts and replies (git-ignored)
```
