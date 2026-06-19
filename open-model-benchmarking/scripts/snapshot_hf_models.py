#!/usr/bin/env python3
"""Snapshot Hugging Face model metadata for creator slugs.

This script only calls Hugging Face JSON metadata APIs. It does not download
model weights, tokenizer files, configs through /resolve, or other model blobs.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HF_MODELS_API = "https://huggingface.co/api/models"
USER_AGENT = "onurclaw-open-model-benchmarking/0.1"

# Keep config out by default. Some tokenizer/model configs include huge chat
# templates; these snapshots are for model discovery and ranking metadata.
EXPAND_FIELDS = [
    "author",
    "cardData",
    "createdAt",
    "downloads",
    "downloadsAllTime",
    "evalResults",
    "gated",
    "gguf",
    "inferenceProviderMapping",
    "lastModified",
    "library_name",
    "likes",
    "model-index",
    "pipeline_tag",
    "private",
    "safetensors",
    "sha",
    "siblings",
    "tags",
    "transformersInfo",
    "trendingScore",
]

CSV_FIELDS = [
    "id",
    "author",
    "downloads",
    "downloads_all_time",
    "likes",
    "trending_score",
    "parameter_count",
    "parameter_count_b",
    "capacity_class",
    "pipeline_tag",
    "library_name",
    "license",
    "gated",
    "private",
    "created_at",
    "last_modified",
    "sha",
    "base_models",
    "has_safetensors",
    "has_gguf",
    "has_tokenizer",
    "has_chat_template",
    "siblings_count",
    "safetensors_files",
    "gguf_files",
    "bin_files",
    "eval_results_count",
    "inference_provider_count",
    "inference_providers",
    "live_inference_providers",
    "supports_tools_any",
    "supports_structured_output_any",
    "max_context_length",
    "router_served",
    "router_provider_count",
    "router_providers",
    "router_supports_tools_any",
    "router_supports_structured_output_any",
    "router_max_context_length",
    "tags",
]


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def read_creator_file(path: Path) -> list[str]:
    creators: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        creators.append(line)
    return creators


def unique_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def parse_next_link(link_header: str | None) -> str | None:
    if not link_header:
        return None
    for part in link_header.split(","):
        match = re.search(r'<([^>]+)>;\s*rel="next"', part)
        if match:
            return match.group(1)
    return None


def request_json(url: str, token: str | None, retries: int = 4) -> tuple[Any, dict[str, str]]:
    headers = {"User-Agent": USER_AGENT}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.loads(response.read().decode("utf-8"))
                return payload, dict(response.headers.items())
        except urllib.error.HTTPError as err:
            if err.code in {429, 500, 502, 503, 504} and attempt < retries:
                time.sleep(min(2**attempt, 8))
                continue
            body = err.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"HTTP {err.code} for {url}: {body[:500]}") from err
        except urllib.error.URLError as err:
            if attempt < retries:
                time.sleep(min(2**attempt, 8))
                continue
            raise RuntimeError(f"Request failed for {url}: {err}") from err
    raise RuntimeError(f"Request failed after retries: {url}")


def list_creator_models(
    creator: str,
    *,
    page_size: int,
    sort: str,
    direction: int,
    token: str | None,
    limit: int | None,
    include_config: bool,
    sleep_seconds: float,
) -> list[dict[str, Any]]:
    expand = list(EXPAND_FIELDS)
    if include_config:
        expand.append("config")
    params: list[tuple[str, str | int]] = [
        ("author", creator),
        ("limit", page_size),
        ("sort", sort),
        ("direction", direction),
    ]
    params.extend(("expand", field) for field in expand)
    url = f"{HF_MODELS_API}?{urllib.parse.urlencode(params, doseq=True)}"
    models: list[dict[str, Any]] = []
    while url:
        payload, headers = request_json(url, token)
        if not isinstance(payload, list):
            raise RuntimeError(f"Expected list payload for {creator}, got {type(payload).__name__}")
        for item in payload:
            if isinstance(item, dict):
                models.append(item)
                if limit is not None and len(models) >= limit:
                    return models
        url = parse_next_link(headers.get("Link") or headers.get("link"))
        if url and sleep_seconds > 0:
            time.sleep(sleep_seconds)
    return models


def load_router_snapshot(path: Path | None) -> dict[str, dict[str, Any]]:
    if path is None or not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    entries = payload.get("data", []) if isinstance(payload, dict) else []
    return {entry.get("id"): entry for entry in entries if isinstance(entry, dict) and entry.get("id")}


def latest_router_snapshot() -> Path | None:
    candidates = sorted((ROOT / "data").glob("hf-router-models-*.json"))
    return candidates[-1] if candidates else None


def portable_path(path: Path | None) -> str | None:
    if path is None:
        return None
    resolved = path.resolve()
    for base in (ROOT, Path.cwd().resolve()):
        try:
            return str(resolved.relative_to(base))
        except ValueError:
            continue
    return str(path)


def str_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def find_license(record: dict[str, Any]) -> str:
    card = record.get("cardData")
    if isinstance(card, dict) and isinstance(card.get("license"), str):
        return card["license"]
    for tag in str_list(record.get("tags")):
        if tag.startswith("license:"):
            return tag.split(":", 1)[1]
    return ""


def find_base_models(record: dict[str, Any]) -> list[str]:
    values: list[str] = []
    card = record.get("cardData")
    if isinstance(card, dict):
        values.extend(str_list(card.get("base_model")))
    for tag in str_list(record.get("tags")):
        if tag.startswith("base_model:"):
            values.append(tag.split(":", 1)[1])
    return unique_preserve_order(values)


def file_counts(record: dict[str, Any]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for sibling in record.get("siblings") or []:
        if not isinstance(sibling, dict):
            continue
        name = sibling.get("rfilename")
        if not isinstance(name, str):
            continue
        lower = name.lower()
        if lower.endswith(".safetensors"):
            counts["safetensors"] += 1
        elif lower.endswith(".gguf"):
            counts["gguf"] += 1
        elif lower.endswith(".bin"):
            counts["bin"] += 1
        elif lower.endswith(".json"):
            counts["json"] += 1
        if lower.endswith("tokenizer.json") or lower.endswith("tokenizer_config.json"):
            counts["tokenizer"] += 1
        if lower.endswith("chat_template.jinja"):
            counts["chat_template"] += 1
    return counts


def extract_parameter_count(record: dict[str, Any]) -> int | None:
    safetensors = record.get("safetensors")
    if isinstance(safetensors, dict):
        total = safetensors.get("total")
        if isinstance(total, int):
            return total
        params = safetensors.get("parameters")
        if isinstance(params, dict):
            numeric_values = [value for value in params.values() if isinstance(value, int)]
            if numeric_values:
                return max(numeric_values)
    gguf = record.get("gguf")
    if isinstance(gguf, dict):
        for key in ("total", "parameters", "parameter_count", "parameterCount"):
            value = gguf.get(key)
            if isinstance(value, int):
                return value
    return None


def capacity_class(parameter_count: int | None) -> str:
    if parameter_count is None:
        return ""
    billion = parameter_count / 1_000_000_000
    if billion <= 1:
        return "tiny"
    if billion <= 20:
        return "small"
    if billion <= 50:
        return "medium"
    return "large"


def provider_summary(mapping: Any) -> dict[str, Any]:
    if not isinstance(mapping, list):
        mapping = []
    providers: list[str] = []
    live: list[str] = []
    supports_tools = False
    supports_structured = False
    context_lengths: list[int] = []
    for item in mapping:
        if not isinstance(item, dict):
            continue
        provider = item.get("provider")
        if isinstance(provider, str):
            providers.append(provider)
            if item.get("status") == "live":
                live.append(provider)
        features = item.get("features")
        if isinstance(features, dict):
            supports_tools = supports_tools or features.get("toolCalling") is True
            supports_structured = supports_structured or features.get("structuredOutput") is True
        details = item.get("providerDetails")
        if isinstance(details, dict):
            context = details.get("context_length")
            if isinstance(context, int):
                context_lengths.append(context)
    return {
        "providers": sorted(set(providers)),
        "live": sorted(set(live)),
        "supports_tools_any": supports_tools,
        "supports_structured_output_any": supports_structured,
        "max_context_length": max(context_lengths) if context_lengths else "",
    }


def router_summary(router_entry: dict[str, Any] | None) -> dict[str, Any]:
    if not router_entry:
        return {
            "router_served": False,
            "router_provider_count": 0,
            "router_providers": [],
            "router_supports_tools_any": False,
            "router_supports_structured_output_any": False,
            "router_max_context_length": "",
        }
    providers = router_entry.get("providers") if isinstance(router_entry, dict) else []
    if not isinstance(providers, list):
        providers = []
    provider_names: list[str] = []
    context_lengths: list[int] = []
    supports_tools = False
    supports_structured = False
    for provider in providers:
        if not isinstance(provider, dict):
            continue
        name = provider.get("provider")
        if isinstance(name, str):
            provider_names.append(name)
        supports_tools = supports_tools or provider.get("supports_tools") is True
        supports_structured = supports_structured or provider.get("supports_structured_output") is True
        context = provider.get("context_length")
        if isinstance(context, int):
            context_lengths.append(context)
    return {
        "router_served": True,
        "router_provider_count": len(provider_names),
        "router_providers": sorted(set(provider_names)),
        "router_supports_tools_any": supports_tools,
        "router_supports_structured_output_any": supports_structured,
        "router_max_context_length": max(context_lengths) if context_lengths else "",
    }


def normalize_record(record: dict[str, Any], router_entry: dict[str, Any] | None) -> dict[str, Any]:
    counts = file_counts(record)
    parameter_count = extract_parameter_count(record)
    provider = provider_summary(record.get("inferenceProviderMapping"))
    router = router_summary(router_entry)
    tags = str_list(record.get("tags"))
    normalized = {
        "id": record.get("id") or record.get("modelId") or "",
        "author": record.get("author") or "",
        "downloads": record.get("downloads") if isinstance(record.get("downloads"), int) else 0,
        "downloads_all_time": record.get("downloadsAllTime")
        if isinstance(record.get("downloadsAllTime"), int)
        else "",
        "likes": record.get("likes") if isinstance(record.get("likes"), int) else 0,
        "trending_score": record.get("trendingScore")
        if isinstance(record.get("trendingScore"), int)
        else 0,
        "parameter_count": parameter_count or "",
        "parameter_count_b": round(parameter_count / 1_000_000_000, 3)
        if parameter_count is not None
        else "",
        "capacity_class": capacity_class(parameter_count),
        "pipeline_tag": record.get("pipeline_tag") or "",
        "library_name": record.get("library_name") or "",
        "license": find_license(record),
        "gated": record.get("gated"),
        "private": record.get("private"),
        "created_at": record.get("createdAt") or "",
        "last_modified": record.get("lastModified") or "",
        "sha": record.get("sha") or "",
        "base_models": ",".join(find_base_models(record)),
        "has_safetensors": bool(record.get("safetensors")) or counts["safetensors"] > 0,
        "has_gguf": bool(record.get("gguf")) or counts["gguf"] > 0,
        "has_tokenizer": counts["tokenizer"] > 0,
        "has_chat_template": counts["chat_template"] > 0,
        "siblings_count": len(record.get("siblings") or []),
        "safetensors_files": counts["safetensors"],
        "gguf_files": counts["gguf"],
        "bin_files": counts["bin"],
        "eval_results_count": len(record.get("evalResults") or []),
        "inference_provider_count": len(provider["providers"]),
        "inference_providers": ",".join(provider["providers"]),
        "live_inference_providers": ",".join(provider["live"]),
        "supports_tools_any": provider["supports_tools_any"],
        "supports_structured_output_any": provider["supports_structured_output_any"],
        "max_context_length": provider["max_context_length"],
        "router_served": router["router_served"],
        "router_provider_count": router["router_provider_count"],
        "router_providers": ",".join(router["router_providers"]),
        "router_supports_tools_any": router["router_supports_tools_any"],
        "router_supports_structured_output_any": router["router_supports_structured_output_any"],
        "router_max_context_length": router["router_max_context_length"],
        "tags": ",".join(tags),
    }
    return normalized


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, ensure_ascii=False) + "\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in CSV_FIELDS})


def write_ids(path: Path, rows: list[dict[str, Any]]) -> None:
    ids = [str(row.get("id") or "") for row in rows if row.get("id")]
    path.write_text("\n".join(ids) + "\n", encoding="utf-8")


def build_summary(
    *,
    creators: list[str],
    raw_rows: list[dict[str, Any]],
    normalized_rows: list[dict[str, Any]],
    errors: list[dict[str, str]],
    router_snapshot: Path | None,
    started_at: str,
    finished_at: str,
) -> dict[str, Any]:
    creator_counts = Counter(row["author"] for row in normalized_rows)
    provider_counts: Counter[str] = Counter()
    license_counts = Counter(row["license"] or "unknown" for row in normalized_rows)
    pipeline_counts = Counter(row["pipeline_tag"] or "unknown" for row in normalized_rows)
    capacity_counts = Counter(row["capacity_class"] or "unknown" for row in normalized_rows)
    for row in normalized_rows:
        for provider in str(row.get("router_providers") or row.get("inference_providers") or "").split(","):
            if provider:
                provider_counts[provider] += 1
    return {
        "schema_version": 1,
        "source": "huggingface_hub_models_api",
        "started_at": started_at,
        "finished_at": finished_at,
        "creators_requested": creators,
        "creator_count": len(creators),
        "raw_model_records": len(raw_rows),
        "normalized_model_records": len(normalized_rows),
        "router_snapshot": portable_path(router_snapshot),
        "router_served_records": sum(1 for row in normalized_rows if row.get("router_served") is True),
        "over_100k_download_records": sum(
            1 for row in normalized_rows if int(row.get("downloads") or 0) > 100_000
        ),
        "tool_supported_records": sum(
            1
            for row in normalized_rows
            if row.get("supports_tools_any") is True or row.get("router_supports_tools_any") is True
        ),
        "structured_output_supported_records": sum(
            1
            for row in normalized_rows
            if row.get("supports_structured_output_any") is True
            or row.get("router_supports_structured_output_any") is True
        ),
        "with_parameter_count": sum(1 for row in normalized_rows if row.get("parameter_count") != ""),
        "with_license": sum(1 for row in normalized_rows if row.get("license")),
        "creator_counts": dict(sorted(creator_counts.items())),
        "provider_counts": dict(sorted(provider_counts.items())),
        "license_counts": dict(sorted(license_counts.items())),
        "pipeline_counts": dict(sorted(pipeline_counts.items())),
        "capacity_class_counts": dict(sorted(capacity_counts.items())),
        "errors": errors,
    }


def build_creator_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("author") or "")].append(row)
    summary_rows: list[dict[str, Any]] = []
    for creator, items in sorted(grouped.items()):
        summary_rows.append(
            {
                "id": creator,
                "author": creator,
                "downloads": sum(int(item.get("downloads") or 0) for item in items),
                "downloads_all_time": "",
                "likes": sum(int(item.get("likes") or 0) for item in items),
                "trending_score": sum(int(item.get("trending_score") or 0) for item in items),
                "parameter_count": "",
                "parameter_count_b": "",
                "capacity_class": "",
                "pipeline_tag": f"models={len(items)}",
                "library_name": "",
                "license": "",
                "gated": sum(1 for item in items if item.get("gated") is True),
                "private": sum(1 for item in items if item.get("private") is True),
                "created_at": "",
                "last_modified": "",
                "sha": "",
                "base_models": "",
                "has_safetensors": sum(1 for item in items if item.get("has_safetensors") is True),
                "has_gguf": sum(1 for item in items if item.get("has_gguf") is True),
                "has_tokenizer": "",
                "has_chat_template": "",
                "siblings_count": "",
                "safetensors_files": "",
                "gguf_files": "",
                "bin_files": "",
                "eval_results_count": sum(int(item.get("eval_results_count") or 0) for item in items),
                "inference_provider_count": "",
                "inference_providers": "",
                "live_inference_providers": "",
                "supports_tools_any": sum(
                    1
                    for item in items
                    if item.get("supports_tools_any") is True
                    or item.get("router_supports_tools_any") is True
                ),
                "supports_structured_output_any": sum(
                    1
                    for item in items
                    if item.get("supports_structured_output_any") is True
                    or item.get("router_supports_structured_output_any") is True
                ),
                "max_context_length": "",
                "router_served": sum(1 for item in items if item.get("router_served") is True),
                "router_provider_count": "",
                "router_providers": "",
                "router_supports_tools_any": "",
                "router_supports_structured_output_any": "",
                "router_max_context_length": "",
                "tags": "",
            }
        )
    return summary_rows


def sorted_by_downloads(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda row: (
            int(row.get("downloads") or 0),
            int(row.get("likes") or 0),
            int(row.get("trending_score") or 0),
            str(row.get("id") or ""),
        ),
        reverse=True,
    )


def over_download_threshold(rows: list[dict[str, Any]], threshold: int) -> list[dict[str, Any]]:
    return [row for row in sorted_by_downloads(rows) if int(row.get("downloads") or 0) > threshold]


def sorted_by_likes(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda row: (
            int(row.get("likes") or 0),
            int(row.get("downloads") or 0),
            int(row.get("trending_score") or 0),
            str(row.get("id") or ""),
        ),
        reverse=True,
    )


def sorted_by_params(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda row: (
            int(row.get("parameter_count") or 0),
            int(row.get("downloads") or 0),
            str(row.get("id") or ""),
        ),
        reverse=True,
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--creator", action="append", default=[], help="Creator slug. Repeatable.")
    parser.add_argument(
        "--creators-file",
        type=Path,
        default=ROOT / "creators.txt",
        help="Newline-delimited creator slugs. Defaults to open-model-benchmarking/creators.txt.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "snapshots",
        help="Directory where a timestamped snapshot folder will be created.",
    )
    parser.add_argument(
        "--router-snapshot",
        type=Path,
        default=latest_router_snapshot(),
        help="Optional HF router JSON snapshot used to enrich served-model fields.",
    )
    parser.add_argument("--page-size", type=int, default=100, help="HF API page size.")
    parser.add_argument("--limit-per-creator", type=int, help="Debug limit for each creator.")
    parser.add_argument("--sort", default="downloads", help="HF model-list sort key.")
    parser.add_argument("--direction", type=int, default=-1, choices=[-1, 1], help="Sort direction.")
    parser.add_argument("--sleep-seconds", type=float, default=0.1, help="Delay between paginated requests.")
    parser.add_argument(
        "--token-env",
        default="HF_TOKEN",
        help="Environment variable containing an optional HF token. Token is never written.",
    )
    parser.add_argument(
        "--include-config",
        action="store_true",
        help="Also request expanded config metadata. This can make snapshots much larger.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    creators = list(args.creator)
    if args.creators_file.exists():
        creators.extend(read_creator_file(args.creators_file))
    creators = unique_preserve_order([creator.strip() for creator in creators if creator.strip()])
    if not creators:
        print("No creators supplied. Use --creator or --creators-file.", file=sys.stderr)
        return 2

    started_at = datetime.now(timezone.utc).isoformat()
    stamp = utc_stamp()
    output_dir = args.output_dir / f"hf-model-metadata-{stamp}"
    output_dir.mkdir(parents=True, exist_ok=False)
    token = os.environ.get(args.token_env) or None
    router = load_router_snapshot(args.router_snapshot)

    raw_rows: list[dict[str, Any]] = []
    normalized_rows: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []

    for creator in creators:
        print(f"Fetching {creator}...", file=sys.stderr)
        try:
            creator_rows = list_creator_models(
                creator,
                page_size=args.page_size,
                sort=args.sort,
                direction=args.direction,
                token=token,
                limit=args.limit_per_creator,
                include_config=args.include_config,
                sleep_seconds=args.sleep_seconds,
            )
        except Exception as err:  # noqa: BLE001 - CLI should continue other creators.
            errors.append({"creator": creator, "error": str(err)})
            print(f"ERROR {creator}: {err}", file=sys.stderr)
            continue
        for row in creator_rows:
            raw_rows.append(row)
            model_id = str(row.get("id") or row.get("modelId") or "")
            normalized_rows.append(normalize_record(row, router.get(model_id)))

    normalized_rows = sorted(normalized_rows, key=lambda row: str(row.get("id") or ""))
    finished_at = datetime.now(timezone.utc).isoformat()
    summary = build_summary(
        creators=creators,
        raw_rows=raw_rows,
        normalized_rows=normalized_rows,
        errors=errors,
        router_snapshot=args.router_snapshot,
        started_at=started_at,
        finished_at=finished_at,
    )

    (output_dir / "creators.txt").write_text("\n".join(creators) + "\n", encoding="utf-8")
    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    write_jsonl(output_dir / "models.raw.jsonl", raw_rows)
    write_jsonl(output_dir / "models.normalized.jsonl", normalized_rows)
    write_csv(output_dir / "models.normalized.csv", normalized_rows)
    write_csv(output_dir / "models.by-downloads.csv", sorted_by_downloads(normalized_rows))
    over_100k_download_rows = over_download_threshold(normalized_rows, 100_000)
    write_csv(output_dir / "models.over-100k-downloads.csv", over_100k_download_rows)
    write_ids(output_dir / "models.over-100k-downloads.ids.txt", over_100k_download_rows)
    write_csv(output_dir / "models.by-likes.csv", sorted_by_likes(normalized_rows))
    write_csv(output_dir / "models.by-params.csv", sorted_by_params(normalized_rows))
    write_csv(output_dir / "creators.summary.csv", build_creator_summary(normalized_rows))

    print(json.dumps({"output_dir": str(output_dir), **summary}, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
