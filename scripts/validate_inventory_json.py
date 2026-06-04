#!/usr/bin/env python3
"""Validate the OpenClaw Onur inventory JSON mirror."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from inventory_data import load_inventory_json


DEFAULT_JSON = Path("OPENCLAW_ONUR_INVENTORY.json")
DEFAULT_SCHEMA = Path("schemas/openclaw-onur-inventory.schema.json")
URL_RE = re.compile(
    r"^https://github\.com/openclaw/openclaw/(?P<path>issues|pull)/(?P<number>\d+)$",
)


def validate_thread(thread: dict, *, closed: bool) -> list[str]:
    errors: list[str] = []
    thread_type = thread.get("type")
    number = thread.get("number")
    url = thread.get("url")
    if thread_type not in {"issue", "pull_request"}:
        errors.append(f"bad type for thread #{number}: {thread_type!r}")
    if not isinstance(number, int) or number < 1:
        errors.append(f"bad number: {number!r}")
    if not isinstance(url, str):
        errors.append(f"missing url for thread #{number}")
    else:
        match = URL_RE.match(url)
        if not match:
            errors.append(f"bad url for thread #{number}: {url}")
        else:
            url_number = int(match.group("number"))
            expected_path = "pull" if thread_type == "pull_request" else "issues"
            if url_number != number or match.group("path") != expected_path:
                errors.append(f"url/type mismatch for thread #{number}: {url}")
    for field in ("title", "area") if not closed else ("title", "status"):
        if not isinstance(thread.get(field), str) or not thread[field].strip():
            errors.append(f"missing {field} for thread #{number}")
    if not closed:
        if not isinstance(thread.get("activity"), int) or thread["activity"] < 0:
            errors.append(f"bad activity for thread #{number}")
        creator = thread.get("creator")
        if not isinstance(creator, str) or not creator.startswith("@"):
            errors.append(f"bad creator for thread #{number}: {creator!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate OpenClaw Onur inventory JSON.")
    parser.add_argument("json", nargs="?", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    args = parser.parse_args()

    json.loads(args.schema.read_text(encoding="utf-8"))
    data = load_inventory_json(args.json)
    open_threads = data.get("open_threads", [])
    closed_threads = data.get("closed_threads", [])
    counts = data.get("counts", {})

    errors: list[str] = []
    seen: set[tuple[str, int]] = set()
    for thread in open_threads:
        key = (thread.get("type"), thread.get("number"))
        if key in seen:
            errors.append(f"duplicate open thread: {key}")
        seen.add(key)
        errors.extend(validate_thread(thread, closed=False))
    for thread in closed_threads:
        errors.extend(validate_thread(thread, closed=True))

    expected_counts = {
        "open_threads": len(open_threads),
        "open_issues": sum(1 for item in open_threads if item.get("type") == "issue"),
        "open_prs": sum(1 for item in open_threads if item.get("type") == "pull_request"),
        "closed_threads": len(closed_threads),
    }
    for key, expected in expected_counts.items():
        if counts.get(key) != expected:
            errors.append(f"count mismatch for {key}: expected {expected}, got {counts.get(key)!r}")

    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1

    print(
        "valid: "
        f"open_threads={expected_counts['open_threads']} "
        f"issues={expected_counts['open_issues']} "
        f"prs={expected_counts['open_prs']} "
        f"closed={expected_counts['closed_threads']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
