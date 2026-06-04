#!/usr/bin/env python3
"""Export OPENCLAW_ONUR_INVENTORY.md to machine-readable JSON."""

from __future__ import annotations

import argparse
from pathlib import Path

from inventory_data import write_inventory_json


DEFAULT_MARKDOWN = Path("OPENCLAW_ONUR_INVENTORY.md")
DEFAULT_JSON = Path("OPENCLAW_ONUR_INVENTORY.json")


def main() -> int:
    parser = argparse.ArgumentParser(description="Export OpenClaw Onur inventory JSON.")
    parser.add_argument("markdown", nargs="?", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument("json", nargs="?", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()

    write_inventory_json(args.markdown, args.json)
    print(f"wrote {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
