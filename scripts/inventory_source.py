#!/usr/bin/env python3
"""Validate freshness metadata on an exported Gitcrawl inventory source."""

from __future__ import annotations

import argparse
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


EXPECTED_REPO = "openclaw/openclaw"
DEFAULT_MAX_AGE_SECONDS = 3600


def connect_readonly(path: Path) -> sqlite3.Connection:
    uri = f"file:{quote(str(path), safe='/')}?mode=ro&immutable=1"
    return sqlite3.connect(uri, uri=True)


def parse_timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("inventory source export timestamp has no timezone")
    return parsed.astimezone(timezone.utc)


def validate_exported_source(
    path: Path,
    *,
    expected_repo: str = EXPECTED_REPO,
    max_age_seconds: int = DEFAULT_MAX_AGE_SECONDS,
    now: datetime | None = None,
) -> None:
    if max_age_seconds <= 0:
        raise ValueError("inventory source max age must be positive")
    conn = connect_readonly(path)
    try:
        check = conn.execute("PRAGMA quick_check").fetchone()
        if check is None or check[0] != "ok":
            raise ValueError("inventory source database failed quick_check")
        try:
            rows = conn.execute(
                "SELECT repo, exported_at, source_max_age_seconds FROM inventory_export_metadata"
            ).fetchall()
        except sqlite3.Error as error:
            raise ValueError("inventory source has no export freshness metadata") from error
    finally:
        conn.close()
    if len(rows) != 1:
        raise ValueError("inventory source export freshness metadata is invalid")
    repo, exported_at, source_max_age = rows[0]
    if repo != expected_repo:
        raise ValueError("inventory source repository does not match")
    if not isinstance(source_max_age, int) or source_max_age <= 0:
        raise ValueError("inventory source upstream max age is invalid")
    current = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    age = (current - parse_timestamp(exported_at)).total_seconds()
    if age < -300:
        raise ValueError("inventory source export timestamp is too far in the future")
    if age > max_age_seconds:
        raise ValueError(f"inventory source export is stale ({int(age)}s old)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("database", type=Path)
    parser.add_argument("--repo", default=EXPECTED_REPO)
    parser.add_argument("--max-age", type=int, default=DEFAULT_MAX_AGE_SECONDS)
    args = parser.parse_args()
    try:
        validate_exported_source(args.database, expected_repo=args.repo, max_age_seconds=args.max_age)
    except (OSError, sqlite3.Error, ValueError) as error:
        raise SystemExit(f"invalid inventory source: {error}") from error
    print("inventory source is fresh")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
