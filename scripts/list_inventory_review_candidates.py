#!/usr/bin/env python3
"""List new OpenClaw inventory review candidates from exported Gitcrawl data."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from textwrap import shorten
from urllib.parse import quote


DEFAULT_INVENTORY = Path("OPENCLAW_ONUR_INVENTORY.md")
DEFAULT_GITCRAWL_DB = Path("/gitcrawl/gitcrawl.db")
REPO_URL = "https://github.com/openclaw/openclaw"
WATERMARK_RE = re.compile(r"Last reviewed through (?P<kind>issue|PR): #(?P<number>\d+)")

KEYWORD_AREAS: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "Local model runtime",
        (
            "local model",
            "ollama",
            "lm studio",
            "lmstudio",
            "vllm",
            "llama.cpp",
            "llamacpp",
            "gguf",
            "mlx",
            "local infer",
            "local llm",
            "local vllm",
            "local gpu",
        ),
    ),
    (
        "OpenAI-compatible/proxy",
        (
            "openai-compatible",
            "openai compatible",
            "openai-completions",
            "openai completions",
            "openai responses",
            "litellm",
            "open-webui",
            "open webui",
            "baseurl",
            "base url",
            "proxy provider",
            "custom provider",
            "custom endpoint",
            "self-hosted",
        ),
    ),
    (
        "Local memory/embedding",
        (
            "qmd",
            "embedding",
            "embeddings",
            "memory_search",
            "memory search",
            "vector",
            "fts",
            "reranker",
            "lancedb",
            "node-llama-cpp",
        ),
    ),
    (
        "Model routing/config",
        (
            "model routing",
            "model switch",
            "model picker",
            "fallback",
            "auth profile",
            "authprofile",
            "model.primary",
            "catalog",
            "backend model",
            "actual model",
        ),
    ),
    (
        "Open-weight/provider behavior",
        (
            "kimi",
            "moonshot",
            "qwen",
            "deepseek",
            "glm",
            "z.ai",
            "zai",
            "gemma",
            "mistral",
            "mimo",
            "xiaomi",
            "nemotron",
            "chutes",
            "openrouter",
        ),
    ),
)


@dataclass(frozen=True)
class Thread:
    kind: str
    number: int
    state: str
    title: str
    body: str
    labels_json: str
    assignees_json: str
    html_url: str
    updated_at_gh: str | None


def read_watermark(path: Path) -> tuple[int, int]:
    issue = pr = None
    for line in path.read_text(encoding="utf-8").splitlines():
        match = WATERMARK_RE.search(line)
        if not match:
            continue
        if match.group("kind") == "issue":
            issue = int(match.group("number"))
        else:
            pr = int(match.group("number"))
    if issue is None or pr is None:
        raise SystemExit("missing Review watermark in inventory")
    return issue, pr


def connect_readonly(path: Path) -> sqlite3.Connection:
    uri = f"file:{quote(str(path), safe='/')}?mode=ro&immutable=1"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def load_threads(db: Path, issue_watermark: int, pr_watermark: int) -> list[Thread]:
    conn = connect_readonly(db)
    try:
        rows = conn.execute(
            """
            SELECT kind, number, state, title, COALESCE(body, '') AS body,
                   labels_json, assignees_json, html_url, updated_at_gh
            FROM threads
            WHERE html_url LIKE ?
              AND (
                (kind = 'issue' AND number > ?)
                OR (kind = 'pull_request' AND number > ?)
              )
            ORDER BY number ASC
            """,
            (f"{REPO_URL}/%", issue_watermark, pr_watermark),
        ).fetchall()
    finally:
        conn.close()
    return [
        Thread(
            kind=row["kind"],
            number=int(row["number"]),
            state=row["state"],
            title=row["title"],
            body=row["body"],
            labels_json=row["labels_json"],
            assignees_json=row["assignees_json"],
            html_url=row["html_url"],
            updated_at_gh=row["updated_at_gh"],
        )
        for row in rows
    ]


def labels_text(value: str) -> str:
    try:
        decoded = json.loads(value)
    except json.JSONDecodeError:
        return ""
    if not isinstance(decoded, list):
        return ""
    labels = []
    for item in decoded:
        if isinstance(item, str):
            labels.append(item)
        elif isinstance(item, dict) and isinstance(item.get("name"), str):
            labels.append(item["name"])
    return " ".join(labels)


def assignees_text(value: str) -> str:
    try:
        decoded = json.loads(value)
    except json.JSONDecodeError:
        return ""
    if not isinstance(decoded, list):
        return ""
    assignees = []
    for item in decoded:
        if isinstance(item, str):
            assignees.append(item)
        elif isinstance(item, dict) and isinstance(item.get("login"), str):
            assignees.append(item["login"])
    return ", ".join(assignees)


def classify(thread: Thread) -> tuple[str, list[str]]:
    haystack = f"{thread.title}\n{thread.body}\n{labels_text(thread.labels_json)}".lower()
    matched_areas = []
    for area, keywords in KEYWORD_AREAS:
        if any(keyword in haystack for keyword in keywords):
            matched_areas.append(area)
    area = matched_areas[0] if matched_areas else "Needs manual review"
    return area, matched_areas


def snippet(text: str) -> str:
    compact = " ".join(text.split())
    return shorten(compact, width=260, placeholder="...")


def markdown(threads: list[Thread], *, include_all: bool) -> str:
    lines = []
    for thread in threads:
        area, matched = classify(thread)
        if not matched and not include_all:
            continue
        label = "PR" if thread.kind == "pull_request" else "Issue"
        assignees = assignees_text(thread.assignees_json)
        lines.append(f"### {label} #{thread.number}: {thread.title}")
        lines.append(f"- URL: {thread.html_url}")
        lines.append(f"- State: {thread.state}")
        lines.append(f"- Suggested area: {area}")
        lines.append(f"- Matched areas: {', '.join(matched) if matched else 'none'}")
        if assignees:
            lines.append(f"- Assignees: {assignees}")
        if thread.updated_at_gh:
            lines.append(f"- Updated: {thread.updated_at_gh}")
        if thread.body.strip():
            lines.append(f"- Body snippet: {snippet(thread.body)}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n" if lines else "NO_CANDIDATES\n"


def json_lines(threads: list[Thread], *, include_all: bool) -> str:
    rows = []
    for thread in threads:
        area, matched = classify(thread)
        if not matched and not include_all:
            continue
        rows.append(
            {
                "kind": thread.kind,
                "number": thread.number,
                "state": thread.state,
                "title": thread.title,
                "url": thread.html_url,
                "suggested_area": area,
                "matched_areas": matched,
                "assignees": assignees_text(thread.assignees_json),
                "body_snippet": snippet(thread.body),
            }
        )
    return "\n".join(json.dumps(row, sort_keys=True) for row in rows) + ("\n" if rows else "")


def candidate_count(text: str, *, format_name: str) -> int:
    if not text:
        return 0
    if format_name == "jsonl":
        return len(text.rstrip("\n").splitlines())
    return sum(1 for line in text.splitlines() if line.startswith("### "))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--gitcrawl-db", type=Path, default=DEFAULT_GITCRAWL_DB)
    parser.add_argument("--format", choices=("markdown", "jsonl"), default="markdown")
    parser.add_argument(
        "--output",
        type=Path,
        help="Write candidates to this file and print only a concise summary.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Include new threads that did not match the broad local-model keyword pool.",
    )
    args = parser.parse_args()

    issue_watermark, pr_watermark = read_watermark(args.inventory)
    threads = load_threads(args.gitcrawl_db, issue_watermark, pr_watermark)
    if args.format == "jsonl":
        output = json_lines(threads, include_all=args.all)
    else:
        output = markdown(threads, include_all=args.all)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
        count = candidate_count(output, format_name=args.format)
        print(f"WROTE {count} candidates to {args.output}")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
