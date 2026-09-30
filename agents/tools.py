"""Local tools the Daily Assistant can call: save documents and create Jira issues."""

import base64
import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime

from .core import ROOT

OUTPUT_DIR = ROOT / "output"


def _slug(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()[:60] or "document"


# ---------------------------------------------------------------- save_document
SAVE_DOCUMENT_TOOL = {
    "name": "save_document",
    "description": (
        "Save a finished document (brochure, research brief, email, one-pager, "
        "meeting notes) to the user's output/ folder. Use format 'html' for "
        "brochures that should look designed and print well; 'md' for everything else."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string", "description": "Short document title, used for the filename."},
            "format": {"type": "string", "enum": ["md", "html"]},
            "content": {"type": "string", "description": "Full document body in the chosen format."},
        },
        "required": ["title", "format", "content"],
        "additionalProperties": False,
    },
}


def save_document(title: str, format: str, content: str) -> str:
    OUTPUT_DIR.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M")
    path = OUTPUT_DIR / f"{stamp}-{_slug(title)}.{format}"
    path.write_text(content, encoding="utf-8")
    return f"Saved to {path.relative_to(ROOT)}"


# ------------------------------------------------------------ create_jira_issue
CREATE_JIRA_TOOL = {
    "name": "create_jira_issue",
    "description": (
        "Create a Jira issue. Only call this after the user has confirmed the "
        "summary and description. If Jira credentials are not configured the "
        "issue is saved as a draft file instead."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "project_key": {"type": "string", "description": "Jira project key, e.g. 'ARO'. Use the default if the user didn't name one."},
            "issue_type": {"type": "string", "enum": ["Task", "Story", "Bug", "Epic"]},
            "summary": {"type": "string", "description": "One-line title."},
            "description": {"type": "string", "description": "Plain-text description including acceptance criteria."},
            "priority": {"type": "string", "enum": ["Highest", "High", "Medium", "Low", "Lowest"]},
            "labels": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["issue_type", "summary", "description"],
        "additionalProperties": False,
    },
}


def _adf(text: str) -> dict:
    """Convert plain text to Atlassian Document Format (required by Jira Cloud v3)."""
    paragraphs = [p for p in text.split("\n") if p.strip()] or [text]
    return {
        "type": "doc",
        "version": 1,
        "content": [{"type": "paragraph", "content": [{"type": "text", "text": p}]} for p in paragraphs],
    }


def create_jira_issue(summary: str, description: str, issue_type: str = "Task",
                      project_key: str = "", priority: str = "", labels=None) -> str:
    base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")
    project_key = project_key or os.environ.get("JIRA_DEFAULT_PROJECT", "")

    fields = {
        "project": {"key": project_key},
        "issuetype": {"name": issue_type},
        "summary": summary,
        "description": _adf(description),
    }
    if priority:
        fields["priority"] = {"name": priority}
    if labels:
        fields["labels"] = labels

    if not (base_url and email and token and project_key):
        draft = f"# [{issue_type}] {summary}\n\nProject: {project_key or '(not set)'}\n" \
                f"Priority: {priority or '-'}\nLabels: {', '.join(labels or []) or '-'}\n\n{description}\n"
        where = save_document(f"jira-draft-{summary}", "md", draft)
        return f"Jira is not configured (set JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_DEFAULT_PROJECT). Draft {where}"

    auth = base64.b64encode(f"{email}:{token}".encode()).decode()
    req = urllib.request.Request(
        f"{base_url}/rest/api/3/issue",
        data=json.dumps({"fields": fields}).encode(),
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json",
                 "Accept": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            key = json.loads(resp.read())["key"]
        return f"Created {key}: {base_url}/browse/{key}"
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"Jira returned {exc.code}: {exc.read().decode()[:500]}")
