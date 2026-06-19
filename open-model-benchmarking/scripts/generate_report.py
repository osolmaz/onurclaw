#!/usr/bin/env python3
"""Generate REPORT.md from manual curation plus HF metadata snapshots."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
AS_OF_DATE = date(2026, 6, 19)
OLDER_THAN_ONE_YEAR_CUTOFF = date(2025, 6, 19)
ARTIFACT_REVISION_SUFFIX_RE = re.compile(r"-(?:gguf|awq|gptq|fp8|fp4|mxfp8|nvfp4)-v[0-9]+$")
ARTIFACT_SUFFIX_RE = re.compile(
    r"-(?:"
    r"gguf|awq|gptq|fp8|fp4|mxfp8|nvfp4|bf16|fp16|int2|int3|int4|int8|"
    r"q[2-8](?:-(?:0|1|k|m|s|l))*|"
    r"4bit|8bit|bnb|bitsandbytes|mlx|exl2|onnx|openvino|tensorrt|"
    r"modelopt|qat|quantized|quant|compressed|safetensors|hf"
    r")$"
)
QAT_SUFFIX_RE = re.compile(r"-qat-w[0-9]+a[0-9]+-ct$")


def latest_snapshot_dir() -> Path:
    candidates = sorted((ROOT / "snapshots").glob("hf-model-metadata-*"))
    if not candidates:
        raise SystemExit("No snapshot directories found.")
    return candidates[-1]


def parse_args() -> argparse.Namespace:
    snapshot_dir = latest_snapshot_dir()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--metadata",
        type=Path,
        default=snapshot_dir / "models.over-100k-downloads.csv",
        help="Popular-model metadata CSV.",
    )
    parser.add_argument(
        "--curation",
        type=Path,
        default=ROOT / "MODEL_MANUAL_CURATION.jsonl",
        help="Manual JSONL curation file with id/include records.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "REPORT.md",
        help="Markdown report to write.",
    )
    return parser.parse_args()


def read_metadata(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_curation(path: Path) -> dict[str, bool]:
    decisions: dict[str, bool] = {}
    with path.open(encoding="utf-8") as handle:
        for lineno, raw in enumerate(handle, start=1):
            line = raw.strip()
            if not line:
                continue
            record = json.loads(line)
            model_id = record.get("id")
            include = record.get("include")
            if not isinstance(model_id, str) or not model_id:
                raise ValueError(f"{path}:{lineno} missing string id")
            if not isinstance(include, bool):
                raise ValueError(f"{path}:{lineno} missing boolean include")
            if model_id in decisions:
                raise ValueError(f"{path}:{lineno} duplicate id {model_id}")
            decisions[model_id] = include
    return decisions


def validate_curation(rows: list[dict[str, str]], decisions: dict[str, bool]) -> None:
    metadata_ids = {row["id"] for row in rows}
    curation_ids = set(decisions)
    missing = sorted(metadata_ids - curation_ids)
    extra = sorted(curation_ids - metadata_ids)
    errors: list[str] = []
    if missing:
        errors.append(f"Missing curation decisions for {len(missing)} models: {', '.join(missing[:10])}")
    if extra:
        errors.append(f"Curation has {len(extra)} ids not in metadata: {', '.join(extra[:10])}")
    if errors:
        raise ValueError("; ".join(errors))


def as_int(value: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def yes_no(value: str) -> str:
    return "yes" if value == "True" else "no"


def fmt_int(value: str) -> str:
    return f"{as_int(value):,}"


def fmt_params(value: str) -> str:
    if not value:
        return ""
    try:
        number = float(value)
    except ValueError:
        return value
    if number >= 100:
        return f"{number:.0f}B"
    if number >= 10:
        return f"{number:.1f}B"
    return f"{number:.2f}B"


def created_date(row: dict[str, str]) -> date | None:
    value = row.get("created_at") or ""
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00")).date()


def created_display(row: dict[str, str]) -> str:
    created = created_date(row)
    return created.isoformat() if created else "unknown"


def older_than_one_year(row: dict[str, str]) -> bool:
    created = created_date(row)
    return created is not None and created < OLDER_THAN_ONE_YEAR_CUTOFF


def normalized_repo_slug(model_id: str) -> str:
    slug = model_id.rsplit("/", 1)[-1].lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def slug_dedupe_key(model_id: str) -> str:
    slug = normalized_repo_slug(model_id)
    previous = None
    while slug and slug != previous:
        previous = slug
        slug = QAT_SUFFIX_RE.sub("", slug)
        slug = ARTIFACT_REVISION_SUFFIX_RE.sub("", slug)
        slug = ARTIFACT_SUFFIX_RE.sub("", slug)
    return slug or normalized_repo_slug(model_id)


def is_artifact_slug(model_id: str) -> bool:
    return normalized_repo_slug(model_id) != slug_dedupe_key(model_id)


def model_link(model_id: str) -> str:
    return f"[{model_id}](https://huggingface.co/{quote(model_id, safe='/')})"


def model_class(row: dict[str, str]) -> str:
    model_id = row["id"].lower()
    text = f"{row['id']} {row['pipeline_tag']} {row['tags']}".lower()
    if "diffusiongemma" in text or "llada" in text:
        return "special-architecture"
    if (
        row["pipeline_tag"] in {"image-text-to-text", "any-to-any"}
        or "vision-language" in text
        or "multimodal" in text
        or "omni" in text
        or bool(re.search(r"(^|[-_/])vl($|[-_/])", model_id))
    ):
        return "multimodal"
    if re.search(r"coder|coding|codeqwen|(^|[-_/])code($|[-_/])", model_id):
        return "coding"
    return "text"


def model_signals(row: dict[str, str]) -> str:
    text = f"{row['id']} {row['tags']}".lower()
    signals: list[str] = []
    if row["router_served"] == "True":
        signals.append("router")
    if row["supports_tools_any"] == "True" or row["router_supports_tools_any"] == "True":
        signals.append("tools")
    if row["supports_structured_output_any"] == "True" or row["router_supports_structured_output_any"] == "True":
        signals.append("structured")
    if row["has_gguf"] == "True":
        signals.append("gguf")
    if any(token in text for token in ("awq", "gptq", "fp8", "nvfp4", "qat")):
        signals.append("quant")
    if "conversational" in text:
        signals.append("conversational")
    return ", ".join(signals)


def table_row(row: dict[str, str]) -> str:
    values = [
        model_link(row["id"]),
        fmt_int(row["downloads"]),
        fmt_int(row["likes"]),
        created_display(row),
        fmt_params(row["parameter_count_b"]),
        model_class(row),
        row["pipeline_tag"] or "unknown",
        row["license"] or "unknown",
        yes_no(row["router_served"]),
        model_signals(row),
    ]
    return "| " + " | ".join(values) + " |"


def slug_dedupe_groups(rows: list[dict[str, str]]) -> list[tuple[str, list[dict[str, str]]]]:
    groups: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        groups.setdefault(slug_dedupe_key(row["id"]), []).append(row)
    for slug in list(groups):
        target = f"{slug}-it"
        if slug.startswith("gemma-") and target in groups and all(is_artifact_slug(row["id"]) for row in groups[slug]):
            groups[target].extend(groups.pop(slug))
    return sorted(
        groups.items(),
        key=lambda item: max(as_int(row["downloads"]) for row in item[1]),
        reverse=True,
    )


def slug_dedupe_table_row(slug: str, rows: list[dict[str, str]]) -> str:
    ordered = sorted(rows, key=lambda row: as_int(row["downloads"]), reverse=True)
    representative = ordered[0]
    examples = [model_link(row["id"]) for row in ordered[:4]]
    if len(ordered) > 4:
        examples.append(f"+ {len(ordered) - 4} more")
    values = [
        f"`{slug}`",
        model_link(representative["id"]),
        str(len(rows)),
        fmt_int(representative["downloads"]),
        ", ".join(examples),
    ]
    return "| " + " | ".join(values) + " |"


def excluded_summary(rows: list[dict[str, str]]) -> list[str]:
    pipelines = Counter(row["pipeline_tag"] or "unknown" for row in rows)
    authors = Counter(row["author"] or "unknown" for row in rows)
    lines = ["### Excluded Summary", ""]
    lines.append("Excluded rows are kept in the manual curation file but omitted from the candidate table.")
    lines.append("")
    lines.append("Excluded by pipeline:")
    lines.append("")
    for name, count in pipelines.most_common(12):
        lines.append(f"- `{name}`: {count}")
    lines.append("")
    lines.append("Top excluded creator namespaces:")
    lines.append("")
    for name, count in authors.most_common(12):
        lines.append(f"- `{name}`: {count}")
    return lines


def write_report(
    *,
    rows: list[dict[str, str]],
    decisions: dict[str, bool],
    metadata_path: Path,
    curation_path: Path,
    output_path: Path,
) -> None:
    included = [row for row in rows if decisions[row["id"]]]
    recent_included = [row for row in included if not older_than_one_year(row)]
    older_included = [row for row in included if older_than_one_year(row)]
    excluded = [row for row in rows if not decisions[row["id"]]]
    slug_groups = slug_dedupe_groups(recent_included)
    duplicate_slug_groups = [group_rows for _, group_rows in slug_groups if len(group_rows) > 1]
    included_by_class = Counter(model_class(row) for row in included)

    lines: list[str] = [
        "# Open Model Benchmarking Report",
        "",
        f"Generated from snapshot: `{metadata_path.parent.name}`.",
        "",
        "This report is generated from the popular Hugging Face model metadata snapshot and `MODEL_MANUAL_CURATION.jsonl`.",
        "The manual curation file contains only include/exclude decisions; downloads, likes, parameter counts, links, and capability signals are joined from the snapshot.",
        "",
        "## Inputs",
        "",
        f"- Metadata: `{metadata_path.relative_to(ROOT)}`",
        f"- Manual curation: `{curation_path.relative_to(ROOT)}`",
        "- Popular threshold: `downloads > 100,000`",
        f"- As-of date for age split: `{AS_OF_DATE.isoformat()}`",
        f"- Older-than-one-year cutoff: `created_at < {OLDER_THAN_ONE_YEAR_CUTOFF.isoformat()}`",
        "",
        "## Filters Used",
        "",
        "This report starts from the creator-wide Hugging Face metadata snapshot, not just router-served models.",
        "The first filter keeps popular rows with current Hugging Face `downloads > 100,000`.",
        "The second filter applies `MODEL_MANUAL_CURATION.jsonl`, where `include: true` means the model is a likely OpenClaw/ShellBench backend candidate.",
        "The age split uses Hugging Face `created_at` as the release-date proxy.",
        f"Rows with `created_at < {OLDER_THAN_ONE_YEAR_CUTOFF.isoformat()}` are treated as older than one year and moved into the collapsible reference table at the bottom.",
        "Slug deduplication is slug-only: it normalizes repo names, strips packaging/runtime/quantization suffixes, and keeps semantic suffixes like `instruct`, `chat`, `coder`, `vl`, `vision`, `thinking`, `reasoning`, `base`, and `distill`.",
        "",
        "## Summary",
        "",
        f"- Popular models curated: {len(rows):,}",
        f"- Included OpenClaw candidates: {len(included):,}",
        f"- Current/recent included candidates: {len(recent_included):,}",
        f"- Older-than-one-year included candidates: {len(older_included):,}",
        f"- Slug-deduped current/recent model groups: {len(slug_groups):,}",
        f"- Multi-artifact slug groups: {len(duplicate_slug_groups):,}",
        f"- Excluded models: {len(excluded):,}",
        f"- Text candidates: {included_by_class['text']:,}",
        f"- Coding candidates: {included_by_class['coding']:,}",
        f"- Multimodal candidates: {included_by_class['multimodal']:,}",
        f"- Special-architecture candidates: {included_by_class['special-architecture']:,}",
        "",
        "## Slug Deduplication",
        "",
        f"The current/recent table has {len(recent_included):,} included rows and {len(slug_groups):,} slug-deduplicated model groups.",
        "The heuristic is intentionally simple: group by the repo slug after removing artifact suffixes such as `GGUF`, `AWQ`, `GPTQ`, `FP8`, `NVFP4`, `BF16`, `MLX`, `4bit`, `8bit`, `bnb`, and QAT suffixes.",
        "It does not merge semantic variants: instruct/base, chat, coder, vision/VL, thinking/reasoning, distill, and similarly named variants stay separate unless the remaining slug is identical.",
        "There is one narrow Gemma repair after suffix stripping: if an artifact-only `gemma-*` group has key `x` and an existing canonical group has key `x-it`, the artifact group is merged into `x-it`.",
        "",
        "| Slug key | Representative repo | Rows | Top downloads | Grouped repos |",
        "| --- | --- | ---: | ---: | --- |",
    ]
    lines.extend(slug_dedupe_table_row(slug, group_rows) for slug, group_rows in slug_groups)
    lines.extend(
        [
            "",
            "## Curation Policy",
            "",
            "Included models are likely OpenClaw/ShellBench backend candidates: chat, instruct, coding, reasoning, conversational, or agent-like multimodal models.",
            "Excluded models are popular but not primary agent backends: embeddings, rerankers, ASR/TTS/audio utilities, OCR/parser-only models, safety guards, image-only models, base/pretrain-only checkpoints, and narrow domain support models.",
            "",
            "## Current / Recent Included Candidate Table",
            "",
            f"This table excludes included candidates with `created_at < {OLDER_THAN_ONE_YEAR_CUTOFF.isoformat()}`. Those older candidates are kept in a collapsible reference section at the bottom.",
            "",
            "| Model | Downloads | Likes | Created | Params | Class | Pipeline | License | Router | Signals |",
            "| --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |",
        ]
    )
    lines.extend(table_row(row) for row in recent_included)
    lines.append("")
    lines.extend(excluded_summary(excluded))
    lines.extend(
        [
            "",
            "## Regeneration",
            "",
            "```bash",
            "python3 open-model-benchmarking/scripts/generate_report.py",
            "```",
            "",
            "## Older Included Candidates",
            "",
            "<details>",
            f"<summary>Show {len(older_included):,} included candidates created before {OLDER_THAN_ONE_YEAR_CUTOFF.isoformat()}</summary>",
            "",
            "| Model | Downloads | Likes | Created | Params | Class | Pipeline | License | Router | Signals |",
            "| --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |",
        ]
    )
    lines.extend(table_row(row) for row in older_included)
    lines.extend(["", "</details>"])
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    rows = read_metadata(args.metadata)
    decisions = read_curation(args.curation)
    validate_curation(rows, decisions)
    write_report(
        rows=rows,
        decisions=decisions,
        metadata_path=args.metadata,
        curation_path=args.curation,
        output_path=args.output,
    )
    included = sum(1 for row in rows if decisions[row["id"]])
    print(json.dumps({"curated": len(rows), "included": included, "excluded": len(rows) - included}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
