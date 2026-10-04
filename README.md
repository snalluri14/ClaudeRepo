# Jarvis: voice planner on your Claude subscription

Jarvis tracks your work and personal tasks in Notion. You talk to it, it updates your tasks, and every morning it plans your day and reads the plan aloud. It also coaches you: it finds where you're falling short using evidence from your own tasks and journal, then trains you on it in spoken practice sessions.

Everything Jarvis needs is on this branch. It doesn't need an API key.

| Command | What it does |
|---|---|
| `python jarvis.py dump` | Talk freely about your day. Jarvis marks tasks done, adds new ones, moves dates, and journals it. |
| `python jarvis.py plan` | Jarvis builds today's plan (up to 3 priorities, quick wins, risks), saves it to Notion, and reads it to you. |
| `python jarvis.py ask` | Ask a question, such as "what's overdue?" or "what's left for the Negen launch?" |
| `python jarvis.py review` | Growth review: your top 3 gaps with evidence ("you moved the pitch deck 4 times"), the likely cause, and a drill for each. Also one thing you're doing well. |
| `python jarvis.py coach` | A spoken practice session on your Focus skill: role-plays, timed challenges, scenarios or quizzes, with feedback after every answer. Type `q` to finish and get your score. |
| `python jarvis.py coach "handling pricing objections"` | A coaching session on a topic you choose. |

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

## How the coaching works

Jarvis keeps a **Jarvis Growth** database in Notion. Each row is a trainable skill or habit with a 1-5 level, dated evidence, the next drill, and a log of sessions and scores.

- **Where the gaps come from:** tasks you keep postponing, plans you overfill, areas of life you're ignoring, frustrations you repeat in your brain dumps, and your coaching scores. You can also just say a goal in a dump ("I want to get better at public speaking") and Jarvis adds it.
- **One Focus skill at a time:** `review` picks it, `plan` adds a 10-15 minute practice item for it to each day, and `coach` trains it.
- **Progress:** each session ends with a score and updates your level, so the next review can tell whether you're actually improving.

Suggested rhythm: run `review` on Sunday evening, and run `coach` for 10 minutes 2-3 times a week. Give Jarvis about a week of daily dumps before the first review, since it needs data to spot patterns.

## Troubleshooting

**"I can't reach Notion" or "Notion needs to be authorized".** Claude Code has the Notion server but hasn't been allowed into your Notion account yet. Fix it once:

```bash
claude mcp list          # notion should say "Connected", not "Needs authentication"
claude                   # then type /mcp, pick notion, choose Authenticate,
                         # approve in the browser, and type /exit
claude mcp list          # check it now says Connected
```

If `notion` isn't in the list at all, add it again (step 2) with `--scope user`, so it works from any folder. If you connected Notion on claude.ai instead (Settings → Connectors), that works too. Make sure it shows as connected there and that `claude` is signed in to the same account.

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
55 18 * * 0   cd /path/to/jarvis && /usr/bin/python3 jarvis.py review >> journal/cron.log 2>&1
```
The second line runs the weekly growth review on Sundays at 18:55.
Windows: in Task Scheduler, create a daily task that runs `python C:\path\to\jarvis\jarvis.py plan`.

## Daily routine

- **Morning:** `plan`, either scheduled or run by hand.
- **During the day:** a quick `dump` whenever something changes.
- **Evening:** a 2-minute `dump` covering what got done, what slipped, and what's new.
- **2-3 times a week:** a 10-minute `coach` session.
- **Sunday:** `review`.

You can also see and edit everything in Notion from your phone. Jarvis picks up your edits next time it runs.

## Files

```
jarvis.py            # record → Whisper → Claude Code + Notion → speak
prompts/jarvis.md    # how Jarvis plans, reviews, coaches and speaks (edit freely)
requirements.txt     # voice packages
journal/             # local log of transcripts and replies (git-ignored)
```
