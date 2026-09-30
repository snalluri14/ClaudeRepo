"""Shared chat loop for all three agents.

Cost controls built in:
  * Cheapest model by default (Claude Haiku 4.5, $1 / $5 per million tokens).
  * Prompt caching on the system prompt + conversation so repeated turns are
    billed at ~10% for the cached part.
  * Web search capped per turn (max_uses) - each search costs $0.01.
  * History is trimmed to the last N turns so long sessions don't grow forever.
"""

import os
from datetime import date
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"

MODELS = {
    "haiku": "claude-haiku-4-5",    # cheapest - default
    "sonnet": "claude-sonnet-5-5",  # better quality, ~2x the price
    "opus": "claude-opus-5-5",      # best quality, ~4x the price
}
DEFAULT_MODEL = os.environ.get("AGENT_MODEL", "haiku")
MAX_HISTORY_MESSAGES = int(os.environ.get("AGENT_MAX_HISTORY", "30"))


def load_prompt(*names: str) -> str:
    """Concatenate prompt files from prompts/ (skips files that don't exist)."""
    parts = []
    for name in names:
        path = PROMPTS / name
        if path.exists():
            parts.append(path.read_text(encoding="utf-8"))
    return "\n\n---\n\n".join(parts)


def web_search_tool(model_id: str, max_uses: int) -> dict:
    # Haiku 4.5 only supports the basic web search variant.
    tool_type = "web_search_20250305" if "haiku" in model_id else "web_search_20260209"
    return {"type": tool_type, "name": "web_search", "max_uses": max_uses}


class Agent:
    def __init__(self, name, system_prompt, tools=None, tool_handlers=None,
                 model=DEFAULT_MODEL, web_search_max_uses=0, effort=None):
        self.name = name
        self.client = anthropic.Anthropic()
        self.model = MODELS.get(model, model)
        self.system = [{"type": "text", "text": system_prompt,
                        "cache_control": {"type": "ephemeral"}}]
        self.tools = list(tools or [])
        if web_search_max_uses:
            self.tools.append(web_search_tool(self.model, web_search_max_uses))
        self.tool_handlers = tool_handlers or {}
        self.effort = effort
        self.messages = []
        self.spent_usd = 0.0

    # -- pricing (per million tokens) used only for the running cost display --
    PRICES = {
        "claude-haiku-4-5": (1.0, 5.0),
        "claude-sonnet-5-5": (2.0, 10.0),
        "claude-opus-5-5": (4.0, 20.0),
    }

    def _track_cost(self, usage):
        inp, out = self.PRICES.get(self.model, (0, 0))
        cost = (
            usage.input_tokens * inp
            + (usage.cache_creation_input_tokens or 0) * inp * 1.25
            + (usage.cache_read_input_tokens or 0) * inp * 0.1
            + usage.output_tokens * out
        ) / 1_000_000
        server = getattr(usage, "server_tool_use", None)
        if server and getattr(server, "web_search_requests", 0):
            cost += server.web_search_requests * 0.01
        self.spent_usd += cost

    def _trim_history(self):
        if len(self.messages) <= MAX_HISTORY_MESSAGES:
            return
        # Keep the tail, but always start on a plain user text turn so we never
        # orphan a tool_result from its tool_use.
        tail = self.messages[-MAX_HISTORY_MESSAGES:]
        while tail and not (tail[0]["role"] == "user" and isinstance(tail[0]["content"], str)):
            tail.pop(0)
        self.messages = tail

    def _run_tool(self, block):
        handler = self.tool_handlers.get(block.name)
        if handler is None:
            return f"Unknown tool: {block.name}", True
        try:
            return handler(**block.input), False
        except Exception as exc:  # report tool errors back to Claude
            return f"Tool error: {exc}", True

    def ask(self, user_text: str) -> str:
        self._trim_history()
        # Today's date rides on the user turn rather than the system prompt, so
        # the system prompt stays byte-identical and cacheable across days.
        self.messages.append({"role": "user", "content": f"[Today: {date.today():%A, %B %d, %Y}]\n{user_text}"})

        for _ in range(10):  # safety cap on tool-loop iterations
            kwargs = dict(
                model=self.model,
                max_tokens=8000,
                system=self.system,
                messages=self.messages,
                cache_control={"type": "ephemeral"},
            )
            if self.tools:
                kwargs["tools"] = self.tools
            if self.effort and "haiku" not in self.model:
                kwargs["output_config"] = {"effort": self.effort}

            response = self.client.messages.create(**kwargs)
            self._track_cost(response.usage)
            self.messages.append({"role": "assistant", "content": response.content})

            if response.stop_reason == "pause_turn":
                continue  # long web search - resend to let it continue
            if response.stop_reason == "refusal":
                return "[The model declined this request.]"
            if response.stop_reason != "tool_use":
                break

            results = []
            for block in response.content:
                if block.type == "tool_use":
                    output, is_error = self._run_tool(block)
                    results.append({"type": "tool_result", "tool_use_id": block.id,
                                    "content": output, "is_error": is_error})
            self.messages.append({"role": "user", "content": results})

        return "\n".join(b.text for b in response.content if b.type == "text").strip()

    def chat(self, intro: str = ""):
        print(f"\n=== {self.name} ({self.model}) ===")
        if intro:
            print(intro)
        print("Type 'exit' to quit, 'reset' to start a new conversation.\n")
        while True:
            try:
                text = input("You: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not text:
                continue
            if text.lower() in {"exit", "quit"}:
                break
            if text.lower() == "reset":
                self.messages = []
                print("(conversation cleared)\n")
                continue
            checkpoint = len(self.messages)
            try:
                reply = self.ask(text)
            except (anthropic.RateLimitError, anthropic.APIStatusError,
                    anthropic.APIConnectionError) as exc:
                self.messages = self.messages[:checkpoint]  # roll back the failed turn
                if isinstance(exc, anthropic.RateLimitError):
                    print("Rate limited - wait a moment and try again.\n")
                elif isinstance(exc, anthropic.APIStatusError):
                    print(f"API error {exc.status_code}: {exc.message}\n")
                else:
                    print("Connection error - check your network.\n")
                continue
            print(f"\n{self.name}: {reply}\n")
            print(f"   [session cost so far: ${self.spent_usd:.4f}]\n")
        print(f"Session total: ${self.spent_usd:.4f}")
