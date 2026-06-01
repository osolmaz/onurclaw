#!/usr/bin/env python3
"""Compare OpenClaw Onur inventory rows with notifier routing state."""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote


DEFAULT_INVENTORY = Path(
    os.environ.get("OPENCLAW_ONUR_INVENTORY_PATH", "/workspace/OPENCLAW_ONUR_INVENTORY.md")
)
DEFAULT_NOTIFIER_DB = Path(
    os.environ.get("OPENCLAW_ONUR_NOTIFIER_DB", "/gitcrawl/notifier.sqlite")
)
DEFAULT_STATE_FILE = Path(
    os.environ.get(
        "OPENCLAW_ONUR_COMPARE_STATE",
        "/state/inventory-notifier-compare-state.json",
    )
)
GITHUB_REPO_URL = "https://github.com/openclaw/openclaw"
LIVE_NOTIFICATION_STATUSES = {"pending", "sending", "sent"}


def parse_inventory(path: Path) -> list[dict[str, Any]]:
    section = None
    items = []
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if line.startswith("## OPEN ISSUES"):
            section = "github_issue"
            continue
        if line.startswith("## OPEN PRS"):
            section = "github_pr"
            continue
        if line.startswith("## ") and section:
            section = None
            continue
        if not section or not line.startswith("| [#"):
            continue

        columns = [column.strip() for column in line.strip("|").split("|")]
        if len(columns) >= 6:
            priority = columns[1]
            area = columns[3]
            title = columns[5]
        elif len(columns) >= 4:
            priority = ""
            area = columns[2]
            title = columns[3]
        else:
            continue

        match = re.search(r"#(\d+)", columns[0])
        if not match:
            continue
        items.append(
            {
                "type": section,
                "number": int(match.group(1)),
                "priority": priority,
                "area": area,
                "title": title,
            }
        )
    return items


def load_latest_result(conn: sqlite3.Connection, item_id: int) -> sqlite3.Row | None:
    return conn.execute(
        """
        SELECT interest, topics_json
        FROM notifier_results
        WHERE item_id = ?
        ORDER BY created_at DESC, id DESC
        LIMIT 1
        """,
        (item_id,),
    ).fetchone()


def load_latest_notification(conn: sqlite3.Connection, item_id: int) -> sqlite3.Row | None:
    return conn.execute(
        """
        SELECT status, suppression_reason, external_message_id
        FROM notifier_notifications
        WHERE item_id = ?
        ORDER BY created_at DESC, id DESC
        LIMIT 1
        """,
        (item_id,),
    ).fetchone()


def decode_topics(value: str | None) -> list[str]:
    if not value:
        return []
    try:
        decoded = json.loads(value)
    except json.JSONDecodeError:
        return []
    if not isinstance(decoded, list):
        return []
    return [topic for topic in decoded if isinstance(topic, str)]


def kind_label(item_type: str) -> str:
    return "PR" if item_type == "github_pr" else "Issue"


def item_url(item_type: str, number: int) -> str:
    path = "pull" if item_type == "github_pr" else "issues"
    return f"{GITHUB_REPO_URL}/{path}/{number}"


def markdown_title(title: str, max_title: int) -> str:
    title = title.replace("|", "\\|").strip()
    if len(title) <= max_title:
        return title
    return title[: max_title - 1].rstrip() + "..."


def topic_list(topics: list[str]) -> str:
    return ", ".join(f"`{topic}`" for topic in topics) if topics else "`none`"


def markdown_item_line(item: dict[str, Any], max_title: int) -> str:
    label = kind_label(item["type"])
    number = item["number"]
    return f"- [{label} #{number}]({item_url(item['type'], number)}) {markdown_title(item['title'], max_title)}"


def state_key(item: dict[str, Any]) -> str:
    return f"{item['type']}:{item['number']}"


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "false_negatives": [], "false_positives": []}
    data = json.loads(path.read_text())
    if not isinstance(data, dict):
        data = {}
    data.setdefault("version", 1)
    data.setdefault("false_negatives", [])
    data.setdefault("false_positives", [])
    return data


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def filter_new(items: list[dict[str, Any]], seen_keys: set[str]) -> list[dict[str, Any]]:
    return [item for item in items if state_key(item) not in seen_keys]


def compare(inventory_path: Path, notifier_db: Path) -> dict[str, Any]:
    inventory = parse_inventory(inventory_path)
    inventory_numbers = {(item["type"], item["number"]) for item in inventory}
    counters: Counter[str] = Counter()
    false_negatives = []
    false_positives = []

    db_uri = f"file:{quote(str(notifier_db), safe='/')}?mode=ro&immutable=1"
    conn = sqlite3.connect(db_uri, uri=True)
    conn.row_factory = sqlite3.Row
    try:
        for inventory_item in inventory:
            ref = f"openclaw/openclaw#{inventory_item['number']}"
            row = conn.execute(
                """
                SELECT id, title, state
                FROM notifier_items
                WHERE (source = 'gitcrawl' AND type = ? AND ref = ?)
                   OR (source_kind = ? AND source_ref = ?)
                ORDER BY id DESC
                LIMIT 1
                """,
                (
                    inventory_item["type"],
                    ref,
                    inventory_item["type"],
                    f"gitcrawl:{ref}",
                ),
            ).fetchone()
            if not row:
                counters["not_in_notifier"] += 1
                continue

            result = load_latest_result(conn, row["id"])
            if not result:
                counters["not_classified"] += 1
                continue

            notification = load_latest_notification(conn, row["id"])
            if not notification or notification["status"] not in LIVE_NOTIFICATION_STATUSES:
                entry = dict(inventory_item)
                entry["title"] = row["title"] or inventory_item["title"]
                entry["notifier_interest"] = result["interest"]
                entry["notifier_topics"] = decode_topics(result["topics_json"])
                entry["notifier_state"] = row["state"]
                if notification:
                    entry["notification_status"] = notification["status"]
                    entry["suppression_reason"] = notification["suppression_reason"]
                false_negatives.append(entry)

        rows = conn.execute(
            """
            SELECT notifier_items.id, notifier_items.type, notifier_items.ref,
                   notifier_items.title, notifier_items.state,
                   notifier_results.interest, notifier_results.topics_json,
                   notifier_notifications.status, notifier_notifications.suppression_reason
            FROM notifier_notifications
            JOIN notifier_items ON notifier_items.id = notifier_notifications.item_id
            LEFT JOIN notifier_results ON notifier_results.id = notifier_notifications.result_id
            WHERE notifier_items.source = 'gitcrawl'
              AND notifier_items.type IN ('github_issue', 'github_pr')
              AND notifier_items.state = 'open'
              AND notifier_notifications.notification_kind = 'github_interest'
              AND notifier_notifications.status IN ('pending', 'sending', 'sent')
            ORDER BY notifier_notifications.created_at DESC
            """
        ).fetchall()

        seen = set()
        for row in rows:
            match = re.search(r"#(\d+)$", row["ref"] or "")
            if not match:
                continue
            number = int(match.group(1))
            item_type = row["type"]
            key = f"{item_type}:{number}"
            if key in seen or (item_type, number) in inventory_numbers:
                continue
            seen.add(key)
            false_positives.append(
                {
                    "type": item_type,
                    "number": number,
                    "title": row["title"] or "",
                    "notifier_interest": row["interest"],
                    "notifier_topics": decode_topics(row["topics_json"]),
                    "notification_status": row["status"],
                    "suppression_reason": row["suppression_reason"],
                }
            )
    finally:
        conn.close()

    false_negatives.sort(key=lambda item: (item["type"], item["number"]), reverse=True)
    false_positives.sort(key=lambda item: (item["type"], item["number"]), reverse=True)
    return {
        "inventory_total": len(inventory),
        "false_negatives": false_negatives,
        "false_positives": false_positives,
        "not_in_notifier": counters["not_in_notifier"],
        "not_classified": counters["not_classified"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare OpenClaw Onur inventory with notifier routing."
    )
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--notifier-db", type=Path, default=DEFAULT_NOTIFIER_DB)
    parser.add_argument("--state-file", type=Path, default=DEFAULT_STATE_FILE)
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--title-chars", type=int, default=140)
    parser.add_argument(
        "--no-state",
        action="store_true",
        help="Report the full current mismatch set without reading or writing state.",
    )
    parser.add_argument(
        "--initialize-state",
        action="store_true",
        help="Mark the current mismatch set as already reported and exit.",
    )
    parser.add_argument(
        "--always-report",
        action="store_true",
        help="Print a markdown report even when no new items are found.",
    )
    args = parser.parse_args()

    result = compare(args.inventory, args.notifier_db)
    state = (
        {"version": 1, "false_negatives": [], "false_positives": []}
        if args.no_state
        else load_state(args.state_file)
    )

    current_false_negatives = {state_key(item) for item in result["false_negatives"]}
    current_false_positives = {state_key(item) for item in result["false_positives"]}
    seen_false_negatives = set(state.get("false_negatives", []))
    seen_false_positives = set(state.get("false_positives", []))

    new_false_negatives = filter_new(result["false_negatives"], seen_false_negatives)
    new_false_positives = filter_new(result["false_positives"], seen_false_positives)

    counts = {
        "inventory": result["inventory_total"],
        "false_negatives_total": len(result["false_negatives"]),
        "false_positives_total": len(result["false_positives"]),
        "new_false_negatives": len(new_false_negatives),
        "new_false_positives": len(new_false_positives),
        "not_in_notifier": result["not_in_notifier"],
        "not_classified": result["not_classified"],
    }

    if not args.no_state:
        state["false_negatives"] = sorted(current_false_negatives)
        state["false_positives"] = sorted(current_false_positives)
        state["last_counts"] = counts
        save_state(args.state_file, state)

    if args.initialize_state:
        print(
            f"initialized state: false_negatives={counts['false_negatives_total']} "
            f"false_positives={counts['false_positives_total']}"
        )
        return 0

    if (
        not args.always_report
        and counts["new_false_negatives"] == 0
        and counts["new_false_positives"] == 0
    ):
        print("NO_REPLY")
        return 0

    print(
        "Inventory/notifier mismatch: "
        f"{counts['false_negatives_total']} false negatives "
        f"({counts['new_false_negatives']} new), "
        f"{counts['false_positives_total']} false positives "
        f"({counts['new_false_positives']} new). "
        f"Inventory={counts['inventory']}; not_in_notifier={counts['not_in_notifier']}; "
        f"not_classified={counts['not_classified']}."
    )
    if new_false_negatives:
        print()
        print("### False negatives")
        for item in new_false_negatives[: args.limit]:
            print(markdown_item_line(item, args.title_chars))
            print(
                f"  - inventory area: `{item.get('area') or 'unknown'}`; "
                f"notifier topics: {topic_list(item.get('notifier_topics', []))}; "
                f"notification: `{item.get('notification_status') or 'none'}`"
            )
    if new_false_positives:
        print()
        print("### False positives")
        for item in new_false_positives[: args.limit]:
            print(markdown_item_line(item, args.title_chars))
            print(
                f"  - notifier interest: `{item.get('notifier_interest') or 'none'}`; "
                f"topics: {topic_list(item.get('notifier_topics', []))}; "
                f"notification: `{item.get('notification_status') or 'none'}`"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
