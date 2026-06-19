#!/usr/bin/env python3
"""Tests for slug-only model deduplication heuristics."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "generate_report.py"
SPEC = importlib.util.spec_from_file_location("generate_report", SCRIPT_PATH)
assert SPEC is not None
generate_report = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(generate_report)


def row(model_id: str, downloads: int) -> dict[str, str]:
    return {"id": model_id, "downloads": str(downloads)}


class SlugDedupeTests(unittest.TestCase):
    def test_strips_artifact_suffixes(self) -> None:
        cases = {
            "Qwen/Qwen3-8B-AWQ": "qwen3-8b",
            "unsloth/Qwen3-8B-GGUF": "qwen3-8b",
            "mlx-community/Qwen3-8B-4bit": "qwen3-8b",
            "Qwen/Qwen2.5-Coder-7B-Instruct-GPTQ-Int4": "qwen2-5-coder-7b-instruct",
            "nvidia/DeepSeek-R1-0528-NVFP4-v2": "deepseek-r1-0528",
            "google/gemma-4-12B-it-qat-w4a16-ct": "gemma-4-12b-it",
            "google/gemma-4-12B-it-qat-q4_0-gguf": "gemma-4-12b-it",
        }
        for model_id, expected in cases.items():
            with self.subTest(model_id=model_id):
                self.assertEqual(generate_report.slug_dedupe_key(model_id), expected)

    def test_keeps_semantic_suffixes(self) -> None:
        self.assertNotEqual(
            generate_report.slug_dedupe_key("Qwen/Qwen3-8B"),
            generate_report.slug_dedupe_key("Qwen/Qwen3-8B-Instruct"),
        )
        self.assertEqual(
            generate_report.slug_dedupe_key("Qwen/Qwen3-8B-Instruct-FP8"),
            "qwen3-8b-instruct",
        )
        self.assertEqual(
            generate_report.slug_dedupe_key("Qwen/Qwen3-VL-8B-Instruct-FP8"),
            "qwen3-vl-8b-instruct",
        )
        self.assertEqual(
            generate_report.slug_dedupe_key("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"),
            "deepseek-r1-distill-qwen-7b",
        )
        self.assertEqual(
            generate_report.slug_dedupe_key("google/gemma-4-31B-it-qat-q4_0-unquantized-assistant"),
            "gemma-4-31b-it-qat-q4-0-unquantized-assistant",
        )

    def test_token_boundaries_avoid_bad_prefix_merges(self) -> None:
        self.assertNotEqual(
            generate_report.slug_dedupe_key("Qwen/Qwen3-8B-AWQ"),
            generate_report.slug_dedupe_key("Qwen/Qwen3-80B-AWQ"),
        )
        self.assertNotEqual(
            generate_report.slug_dedupe_key("Qwen/Qwen2.5-7B-Instruct-AWQ"),
            generate_report.slug_dedupe_key("Qwen/Qwen2.5-72B-Instruct-AWQ"),
        )

    def test_groups_rows_by_slug_key(self) -> None:
        groups = dict(
            generate_report.slug_dedupe_groups(
                [
                    row("Qwen/Qwen3-8B-AWQ", 10),
                    row("unsloth/Qwen3-8B-GGUF", 5),
                    row("Qwen/Qwen3-8B-Instruct", 20),
                    row("Qwen/Qwen3-80B-AWQ", 30),
                ]
            )
        )

        self.assertEqual([item["id"] for item in groups["qwen3-8b"]], ["Qwen/Qwen3-8B-AWQ", "unsloth/Qwen3-8B-GGUF"])
        self.assertEqual([item["id"] for item in groups["qwen3-8b-instruct"]], ["Qwen/Qwen3-8B-Instruct"])
        self.assertEqual([item["id"] for item in groups["qwen3-80b"]], ["Qwen/Qwen3-80B-AWQ"])

    def test_repairs_gemma_artifact_slug_that_omits_it(self) -> None:
        groups = dict(
            generate_report.slug_dedupe_groups(
                [
                    row("google/gemma-4-26B-A4B-it", 100),
                    row("nvidia/Gemma-4-26B-A4B-NVFP4", 50),
                    row("google/gemma-4-26B-A4B-it-qat-q4_0-gguf", 25),
                ]
            )
        )

        self.assertNotIn("gemma-4-26b-a4b", groups)
        self.assertEqual(
            [item["id"] for item in groups["gemma-4-26b-a4b-it"]],
            [
                "google/gemma-4-26B-A4B-it",
                "google/gemma-4-26B-A4B-it-qat-q4_0-gguf",
                "nvidia/Gemma-4-26B-A4B-NVFP4",
            ],
        )

    def test_gemma_it_repair_does_not_merge_real_base_slug(self) -> None:
        groups = dict(
            generate_report.slug_dedupe_groups(
                [
                    row("google/gemma-4-26B-A4B", 100),
                    row("google/gemma-4-26B-A4B-it", 50),
                ]
            )
        )

        self.assertEqual([item["id"] for item in groups["gemma-4-26b-a4b"]], ["google/gemma-4-26B-A4B"])
        self.assertEqual([item["id"] for item in groups["gemma-4-26b-a4b-it"]], ["google/gemma-4-26B-A4B-it"])

    def test_gemma_it_repair_does_not_apply_to_other_families(self) -> None:
        groups = dict(
            generate_report.slug_dedupe_groups(
                [
                    row("example/Foo-8B-FP8", 100),
                    row("example/Foo-8B-it", 50),
                ]
            )
        )

        self.assertEqual([item["id"] for item in groups["foo-8b"]], ["example/Foo-8B-FP8"])
        self.assertEqual([item["id"] for item in groups["foo-8b-it"]], ["example/Foo-8B-it"])


if __name__ == "__main__":
    unittest.main()
