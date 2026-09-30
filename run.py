"""Launch one of the three agents.

    python run.py sales        # Agent 1: sales & pitch coach (role-play)
    python run.py assistant    # Agent 2: brochures, research, Jira
    python run.py stocks       # Agent 3: US market news & stock ideas

Add --model sonnet (or opus) for higher quality at higher cost. Default is haiku.
"""

import argparse
from datetime import date

from agents.core import DEFAULT_MODEL, Agent, load_prompt
from agents.tools import (CREATE_JIRA_TOOL, SAVE_DOCUMENT_TOOL,
                          create_jira_issue, save_document)


def build(kind: str, model: str) -> tuple[Agent, str]:
    if kind == "sales":
        agent = Agent(
            "Sales Coach",
            load_prompt("sales_coach.md", "company_profiles.md"),
            model=model,
        )
        intro = ("Try: 'roleplay: I'm cold-calling a VP of Engineering at a fintech about Arohak' "
                 "or 'give me a 30-second pitch for OmniTapScan' or 'drill me on objections'.")
        return agent, intro

    if kind == "assistant":
        agent = Agent(
            "Daily Assistant",
            load_prompt("daily_assistant.md", "company_profiles.md"),
            tools=[SAVE_DOCUMENT_TOOL, CREATE_JIRA_TOOL],
            tool_handlers={"save_document": save_document,
                           "create_jira_issue": create_jira_issue},
            model=model,
            web_search_max_uses=5,
        )
        intro = ("Try: 'make a brochure for Negen Technologies' or 'research the market for "
                 "NFC/QR scanning products' or 'create Jira stories for a login feature'.")
        return agent, intro

    if kind == "stocks":
        agent = Agent(
            "Market Analyst",
            load_prompt("stock_advisor.md"),
            model=model,
            web_search_max_uses=8,
        )
        intro = (f"Today is {date.today():%A %B %d, %Y}. Try: 'morning brief', "
                 "'what's moving AI stocks today', or 'analyze NVDA'.")
        return agent, intro

    raise SystemExit(f"Unknown agent '{kind}'. Use: sales, assistant, stocks")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("agent", choices=["sales", "assistant", "stocks"])
    parser.add_argument("--model", default=DEFAULT_MODEL, help="haiku (cheapest, default), sonnet, or opus")
    parser.add_argument("-q", "--question", help="Ask one question and exit instead of chatting")
    args = parser.parse_args()

    agent, intro = build(args.agent, args.model)
    if args.question:
        print(agent.ask(args.question))
        print(f"\n[cost: ${agent.spent_usd:.4f}]")
    else:
        agent.chat(intro)


if __name__ == "__main__":
    main()
