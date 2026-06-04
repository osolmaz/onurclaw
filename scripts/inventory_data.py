#!/usr/bin/env python3
"""Shared OpenClaw Onur inventory parsing and JSON helpers."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCHEMA_PATH = "schemas/openclaw-onur-inventory.schema.json"
OPEN_THREADS_RE = re.compile(r"^## OPEN THREADS(?: \((?P<count>\d+)\))?$")
OPEN_ISSUES_RE = re.compile(r"^## OPEN ISSUES(?: \((?P<count>\d+)\))?$")
OPEN_PRS_RE = re.compile(r"^## OPEN PRS(?: \((?P<count>\d+)\))?$")
CLOSED_RE = re.compile(r"^## RECENTLY CLOSED OR REMOVED FROM OPEN INVENTORY")
UPDATED_RE = re.compile(r"^Updated:\s*(?P<date>\d{4}-\d{2}-\d{2})\s*$")
WATERMARK_RE = re.compile(r"Last reviewed through (?P<kind>issue|PR): #(?P<number>\d+)")
THREAD_URL_RE = re.compile(
    r"https://github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/(?:issues|pull)/(?P<number>\d+)",
)
THREAD_KIND_BY_MARKER = {
    "📝": "issue",
    "\U0001F41B": "issue",
    "🔀": "pull_request",
}


@dataclass(frozen=True)
class InventoryThread:
    type: str
    number: int
    url: str
    activity: int
    area: str
    creator: str
    title: str
    assignee: str | None = None

    @property
    def notifier_type(self) -> str:
        return "github_pr" if self.type == "pull_request" else "github_issue"


def split_markdown_row(row: str) -> list[str]:
    stripped = row.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        raise ValueError(f"not a markdown table row: {row}")
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in stripped[1:-1]:
        if char == "\\" and not escaped:
            escaped = True
            current.append(char)
            continue
        if char == "|" and not escaped:
            cells.append("".join(current).strip().replace("\\|", "|"))
            current = []
            continue
        current.append(char)
        escaped = False
    cells.append("".join(current).strip().replace("\\|", "|"))
    return cells


def parse_int_cell(value: str) -> int:
    match = re.search(r"-?\d+", value)
    return int(match.group(0)) if match else 0


def parse_title_cell(value: str) -> tuple[str, str | None]:
    marker = "<br>Assignee:"
    if marker not in value:
        return value.strip(), None
    title, assignee = value.split(marker, maxsplit=1)
    assignee = assignee.strip()
    return title.strip(), assignee or None


def thread_type_from_cell(cell: str, fallback: str | None = None) -> str | None:
    if "/pull/" in cell:
        return "pull_request"
    if "/issues/" in cell:
        return "issue"
    marker = cell.lstrip()[:1]
    return THREAD_KIND_BY_MARKER.get(marker, fallback)


def thread_url_from_cell(cell: str) -> str | None:
    match = re.search(r"\]\((?P<url>https://github\.com/[^)]+)\)", cell)
    return match.group("url") if match else None


def thread_number_from_cell(cell: str) -> int | None:
    match = re.search(r"#(\d+)", cell)
    return int(match.group(1)) if match else None


def normalize_creator(value: str) -> str:
    login = value.strip().removeprefix("@").strip()
    return f"@{login}" if login else ""


def parse_open_row(
    row: str,
    *,
    header: list[str],
    fallback_type: str | None,
) -> InventoryThread | None:
    cells = split_markdown_row(row)
    indexes = {name: index for index, name in enumerate(header)}

    def cell(name: str) -> str:
        index = indexes.get(name)
        if index is None or index >= len(cells):
            return ""
        return cells[index]

    first_cell = cells[0] if cells else ""
    number = thread_number_from_cell(first_cell)
    url = thread_url_from_cell(first_cell)
    thread_type = thread_type_from_cell(first_cell, fallback_type)
    if number is None or url is None or thread_type is None:
        return None

    title, assignee = parse_title_cell(cell("Title"))
    return InventoryThread(
        type=thread_type,
        number=number,
        url=url,
        activity=parse_int_cell(cell("Activity")),
        area=cell("Area"),
        creator=normalize_creator(cell("Creator")),
        title=title,
        assignee=assignee,
    )


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(set(cell.strip()) <= {"-", " "} for cell in cells)


def parse_markdown_inventory(path: Path) -> dict[str, Any]:
    updated = ""
    watermark = {"issue": 0, "pr": 0}
    open_threads: list[InventoryThread] = []
    closed_threads: list[dict[str, Any]] = []
    section: str | None = None
    header: list[str] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        updated_match = UPDATED_RE.match(line)
        if updated_match:
            updated = updated_match.group("date")
            continue

        watermark_match = WATERMARK_RE.search(line)
        if watermark_match:
            key = "issue" if watermark_match.group("kind") == "issue" else "pr"
            watermark[key] = int(watermark_match.group("number"))
            continue

        if OPEN_THREADS_RE.match(line):
            section = "open_threads"
            header = None
            continue
        if OPEN_ISSUES_RE.match(line):
            section = "open_issues"
            header = None
            continue
        if OPEN_PRS_RE.match(line):
            section = "open_prs"
            header = None
            continue
        if CLOSED_RE.match(line):
            section = "closed"
            header = None
            continue
        if line.startswith("## "):
            section = None
            header = None
            continue
        if not section or not line.startswith("|"):
            continue

        cells = split_markdown_row(line)
        if cells and cells[0] in {"Thread", "Issue", "PR"}:
            header = cells
            continue
        if is_separator_row(cells):
            continue

        if section in {"open_threads", "open_issues", "open_prs"}:
            if header is None:
                continue
            fallback_type = None
            if section == "open_issues":
                fallback_type = "issue"
            elif section == "open_prs":
                fallback_type = "pull_request"
            parsed = parse_open_row(line, header=header, fallback_type=fallback_type)
            if parsed is not None:
                open_threads.append(parsed)
            continue

        if section == "closed" and len(cells) >= 3:
            number = thread_number_from_cell(cells[0])
            url = thread_url_from_cell(cells[0])
            thread_type = thread_type_from_cell(cells[0])
            if number is None or url is None or thread_type is None:
                continue
            closed_threads.append(
                {
                    "type": thread_type,
                    "number": number,
                    "url": url,
                    "status": cells[1],
                    "title": cells[2],
                }
            )

    issue_count = sum(1 for item in open_threads if item.type == "issue")
    pr_count = sum(1 for item in open_threads if item.type == "pull_request")
    return {
        "$schema": SCHEMA_PATH,
        "schema_version": 1,
        "updated": updated,
        "review_watermark": watermark,
        "counts": {
            "open_threads": len(open_threads),
            "open_issues": issue_count,
            "open_prs": pr_count,
            "closed_threads": len(closed_threads),
        },
        "open_threads": [
            {
                "type": item.type,
                "number": item.number,
                "url": item.url,
                "activity": item.activity,
                "area": item.area,
                "creator": item.creator,
                "title": item.title,
                **({"assignee": item.assignee} if item.assignee else {}),
            }
            for item in open_threads
        ],
        "closed_threads": closed_threads,
    }


def write_inventory_json(markdown_path: Path, json_path: Path) -> None:
    inventory = parse_markdown_inventory(markdown_path)
    json_path.write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def load_inventory_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"inventory JSON must be an object: {path}")
    if data.get("schema_version") != 1:
        raise ValueError(f"unsupported inventory schema_version in {path}")
    return data


def load_open_threads(path: Path) -> list[dict[str, Any]]:
    data = load_inventory_json(path)
    threads = data.get("open_threads")
    if not isinstance(threads, list):
        raise ValueError(f"inventory JSON missing open_threads array: {path}")
    return [thread for thread in threads if isinstance(thread, dict)]
