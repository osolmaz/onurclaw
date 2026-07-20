#!/usr/bin/env python3

from __future__ import annotations

import sqlite3
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from inventory_source import validate_exported_source


class InventorySourceTest(unittest.TestCase):
    def database(self, exported_at: datetime, *, metadata: bool = True) -> Path:
        root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        path = root / "gitcrawl.db"
        conn = sqlite3.connect(path)
        if metadata:
            conn.execute(
                "CREATE TABLE inventory_export_metadata "
                "(repo TEXT NOT NULL, exported_at TEXT NOT NULL, source_max_age_seconds INTEGER NOT NULL)"
            )
            conn.execute(
                "INSERT INTO inventory_export_metadata VALUES (?, ?, ?)",
                ("openclaw/openclaw", exported_at.isoformat().replace("+00:00", "Z"), 3600),
            )
        conn.commit()
        conn.close()
        return path

    def test_accepts_fresh_export(self) -> None:
        now = datetime(2026, 7, 20, tzinfo=timezone.utc)
        validate_exported_source(self.database(now - timedelta(minutes=5)), now=now)

    def test_rejects_stale_export(self) -> None:
        now = datetime(2026, 7, 20, tzinfo=timezone.utc)
        with self.assertRaisesRegex(ValueError, "stale"):
            validate_exported_source(self.database(now - timedelta(hours=2)), now=now)

    def test_rejects_unstamped_database(self) -> None:
        now = datetime(2026, 7, 20, tzinfo=timezone.utc)
        with self.assertRaisesRegex(ValueError, "no export freshness metadata"):
            validate_exported_source(self.database(now, metadata=False), now=now)


if __name__ == "__main__":
    unittest.main()
