#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path


LOCAL_SKILL_RELATIVE_PATH = Path(".agents/skills/openclaw-onur-inventory/SKILL.md")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check that the onurclaw sandbox skill copy matches an explicit source file."
    )
    parser.add_argument(
        "--source",
        type=Path,
        help="Path to an external source SKILL.md to compare against.",
    )
    parser.add_argument(
        "--require-source",
        action="store_true",
        help="Fail instead of skipping when --source is not provided.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()
    local = root / LOCAL_SKILL_RELATIVE_PATH
    if not local.exists():
        print(f"skill_sync_ok=false missing_local={local}", file=sys.stderr)
        return 1

    source = args.source.expanduser().resolve() if args.source else None
    if source is None:
        message = "skill_sync_skipped=true reason=source_not_provided"
        if args.require_source:
            print(message, file=sys.stderr)
            return 2
        print(message)
        return 0
    if not source.exists():
        print(f"skill_sync_ok=false missing_source={source}", file=sys.stderr)
        return 1

    if local.read_bytes() != source.read_bytes():
        print(f"skill_sync_ok=false source={source} local={local}", file=sys.stderr)
        return 1

    print(f"skill_sync_ok=true source={source} local={local}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
