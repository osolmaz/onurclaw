#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


SKILL_RELATIVE_PATH = Path("agents/skills/openclaw-onur-inventory/sandbox/SKILL.md")
LOCAL_SKILL_RELATIVE_PATH = Path("skills/openclaw-onur-inventory/SKILL.md")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def candidate_tools_repos(root: Path) -> list[Path]:
    candidates: list[Path] = []
    if env_path := os.environ.get("ONURCLAW_TOOLS_REPO"):
        candidates.append(Path(env_path).expanduser())
    candidates.append(root.parent / "tools")
    candidates.append(Path.home() / "repos" / "tools")
    return candidates


def resolve_tools_source(root: Path, explicit_tools_repo: str | None) -> Path | None:
    candidates = (
        [Path(explicit_tools_repo).expanduser()]
        if explicit_tools_repo
        else candidate_tools_repos(root)
    )
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        source = resolved / SKILL_RELATIVE_PATH
        if source.exists():
            return source
    return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check that the onurclaw sandbox skill copy matches the tools source."
    )
    parser.add_argument(
        "--tools-repo",
        help=(
            "Path to the osolmaz/tools checkout. Defaults to "
            "ONURCLAW_TOOLS_REPO, a sibling tools checkout, then the user's "
            "standard tools checkout."
        ),
    )
    parser.add_argument(
        "--require-source",
        action="store_true",
        help="Fail instead of skipping when the tools source is unavailable.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()
    local = root / LOCAL_SKILL_RELATIVE_PATH
    if not local.exists():
        print(f"skill_sync_ok=false missing_local={local}", file=sys.stderr)
        return 1

    source = resolve_tools_source(root, args.tools_repo)
    if source is None:
        message = (
            "skill_sync_skipped=true reason=tools_source_unavailable "
            f"expected={SKILL_RELATIVE_PATH}"
        )
        if args.require_source:
            print(message, file=sys.stderr)
            return 2
        print(message)
        return 0

    if local.read_bytes() != source.read_bytes():
        print(f"skill_sync_ok=false source={source} local={local}", file=sys.stderr)
        return 1

    print(f"skill_sync_ok=true source={source} local={local}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
