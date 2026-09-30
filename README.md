# My AI Agents

Three personal agents built on the Claude API, tuned to keep costs low.

| # | Agent | Command | What it does |
|---|-------|---------|--------------|
| 1 | **Sales Coach** | `python run.py sales` | Role-plays prospects, builds pitches, drills objections, and reviews your messages. Trains you to sell yourself, Arohak, OmniTapScan, and Negen Technologies. |
| 2 | **Daily Assistant** | `python run.py assistant` | Makes brochures (saved as printable HTML), researches topics on the web, and drafts or creates Jira issues. |
| 3 | **Market Analyst** | `python run.py stocks` | Searches the latest US market news and gives briefs, stock analysis, and ideas with catalysts and risks. |

## Setup (5 minutes)

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...        # from console.anthropic.com
```

**Then edit `prompts/company_profiles.md`.** Fill in the real facts about you, Arohak, OmniTapScan, and Negen. The agents are told never to invent clients or numbers, so this file is what makes their output specific to you.

### Optional: connect Jira

```bash
export JIRA_BASE_URL=https://yourcompany.atlassian.net
export JIRA_EMAIL=you@company.com
export JIRA_API_TOKEN=...                  # id.atlassian.com → Security → API tokens
export JIRA_DEFAULT_PROJECT=ARO
```

Without these variables, Jira issues are saved as drafts in `output/`.

## Usage

```bash
python run.py sales                          # interactive chat
python run.py stocks -q "morning brief"      # one question, then exit
python run.py assistant --model sonnet       # higher quality for an important brochure
```

In a chat, type `reset` to start over and `exit` to quit. After every reply, the chat shows the session cost so far.

## Cost: why this is the cheap option

| Choice | Why it's cheap |
|---|---|
| **Claude Haiku 4.5** by default | $1 / $5 per million input/output tokens, the cheapest current Claude model. Switch to `--model sonnet` ($2/$10) only when quality matters, such as a client-facing brochure. |
| **Prompt caching** | The system prompt and earlier conversation are cached, so repeated turns are billed at about 10% for those tokens. |
| **Web search capped** | 5 searches per turn for the assistant and 8 for stocks, at $0.01 each. The sales coach doesn't search at all. |
| **History trimmed** | Only the last 30 messages are sent, so long sessions don't get more expensive every turn. |
| **Pay per use** | No subscription and nothing running in the background. |

Rough estimates with Haiku:

- A 30-minute sales roleplay costs about $0.10-0.30.
- A stock morning brief costs about $0.05-0.15, mostly for searches.
- A brochure costs about $0.02-0.05.

Typical daily use comes to around **$3-10 per month**. Set a monthly spend limit in the Anthropic Console so you can't overspend.

### The no-code alternative

With a **Claude Pro subscription ($20/month flat)**, you can run the same agents without any code. Create three **Projects** on claude.ai and paste the matching prompt file into each project's instructions:

- Sales Coach: `prompts/sales_coach.md` + `prompts/company_profiles.md`
- Daily Assistant: `prompts/daily_assistant.md` + `prompts/company_profiles.md` (turn on web search, and connect the Atlassian connector for Jira)
- Market Analyst: `prompts/stock_advisor.md` (turn on web search)

Pro also gives you voice mode in the mobile app, which is useful for practicing sales conversations out loud. Pick Pro if you prefer a fixed monthly price and the chat UI. Pick this code if you use the agents lightly (it usually costs less than $20) or want to automate them later, for example a scheduled morning stock brief.

## Files

```
run.py                       # entry point: picks the agent
agents/core.py               # shared chat loop, caching, cost tracking
agents/tools.py              # save_document + create_jira_issue tools
prompts/*.md                 # each agent's instructions (edit freely)
output/                      # brochures, research briefs, Jira drafts
```

> The Market Analyst is a research aid, not financial advice. Verify prices and do your own due diligence before you trade.
