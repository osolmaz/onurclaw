#!/usr/bin/env python3

from __future__ import annotations

import sqlite3
import tempfile
import unittest
from pathlib import Path

from list_inventory_review_candidates import load_threads


class InventoryCandidatesTest(unittest.TestCase):
    def database(self, body_column: str) -> Path:
        root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        path = root / "gitcrawl.db"
        conn = sqlite3.connect(path)
        conn.execute(
            f"""
            CREATE TABLE threads (
              kind TEXT NOT NULL,
              number INTEGER NOT NULL,
              state TEXT NOT NULL,
              title TEXT NOT NULL,
              {body_column} TEXT,
              labels_json TEXT NOT NULL,
              assignees_json TEXT NOT NULL,
              html_url TEXT NOT NULL,
              updated_at_gh TEXT
            )
            """
        )
        conn.execute(
            f"""
            INSERT INTO threads (
              kind, number, state, title, {body_column}, labels_json,
              assignees_json, html_url, updated_at_gh
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "pull_request",
                44,
                "open",
                "Ollama streaming",
                "portable body",
                "[]",
                "[]",
                "https://github.com/openclaw/openclaw/pull/44",
                "2026-07-20T00:00:00Z",
            ),
        )
        conn.commit()
        conn.close()
        return path

    def test_reads_full_database_body(self) -> None:
        threads = load_threads(self.database("body"), 0, 0)
        self.assertEqual(threads[0].body, "portable body")

    def test_reads_portable_database_body_excerpt(self) -> None:
        threads = load_threads(self.database("body_excerpt"), 0, 0)
        self.assertEqual(threads[0].body, "portable body")


if __name__ == "__main__":
    unittest.main()
