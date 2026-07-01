# ShellBench Public Task Run Results

Date: 2026-07-01

Status: baseline local run complete.

This report records ShellBench public Harbor task results for OpenClaw runtime and local open-weight model experiments. It intentionally excludes task prompts, fixture contents, workspace packets, generated artifacts, verifier rationales, and raw trajectories.

## Non-Sensitive Scope

Included:

- Aggregate pass counts and mean reward.
- Runtime and model identifiers.
- High-level harness notes needed to reproduce the benchmark setup.
- Public task slugs and per-model pass/fail results.

Excluded:

- Task text, task instructions, and scenario descriptions.
- Input data files from task workspaces.
- Agent outputs and generated task artifacts.
- Judge prompts, judge responses, and free-text verdict reasons.
- Raw Harbor job directories.

Raw Harbor outputs remain local under `/Users/onur/repos/shellbench-local/harbor-jobs/` and are not copied into this public repo.

## Benchmark Setup

- Public task checkout: `ShellBench/public-tasks`
- Public task revision: `30d6135`
- Task set: 20 Harbor public tasks under `tasks/harbor`
- Harness: Harbor running OpenClaw
- Scoring: local OpenAI-compatible Codex judge proxy backed by `codex exec -m gpt-5.5`
- Local Docker workaround: temporary task copies rewrote deprecated `allow_internet = false` to `allow_internet = true` because this Harbor Docker backend rejected the corresponding no-network mode. The source public-task checkout was not modified.
- Fairness rule for model comparison: no extra model-specific task instructions were used in the scored runs.

## Aggregate Results

| Runtime / model | Completed | Passed | Mean reward | Exceptions |
| --- | ---: | ---: | ---: | --- |
| OpenClaw Codex runtime + `openai/gpt-5.5` | `20/20` | `4/20` | `0.200` | `1` timeout |
| OpenClaw embedded + vLLM Qwen A3B, `openai/qwen-vllm` | `20/20` | `1/20` | `0.050` | `1` timeout |
| OpenClaw embedded + vLLM Qwen dense 27B, `openai/qwen-dense-vllm` | `20/20` | `1/20` | `0.050` | `2` timeouts |
| OpenClaw embedded + vLLM Gemma A4B, `openai/gemma-vllm` | `20/20` | `1/20` | `0.050` | `0` |
| OpenClaw embedded + vLLM Gemma dense 31B QAT, `openai/gemma-dense-vllm` | `20/20` | `1/20` | `0.050` | `0` |

## Model Artifacts

| Run label | Runtime model id | Hugging Face artifact | Serving notes |
| --- | --- | --- |
| Codex | `openai/gpt-5.5` | Not a Hugging Face artifact | OpenClaw Gateway-backed Codex runtime; not `--local` embedded runtime |
| Qwen A3B | `openai/qwen-vllm` | [`lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit) | vLLM Metal, 65,536-token context |
| Qwen dense | `openai/qwen-dense-vllm` | [`lmstudio-community/Qwen3.6-27B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-27B-MLX-4bit) | vLLM Metal, 65,536-token context |
| Gemma A4B | `openai/gemma-vllm` | [`lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit`](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit) | vLLM Metal, 65,536-token context |
| Gemma dense | `openai/gemma-dense-vllm` | [`mlx-community/gemma-4-31B-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-4-31B-it-qat-4bit) | vLLM Metal, 22,528-token context due to KV-cache capacity |

## Per-Task Results

The table uses public task slugs only. It does not include task prompts, workspace data, generated artifacts, or judge reasoning.

| Public task slug | Codex | Qwen A3B | Qwen dense | Gemma A4B | Gemma dense |
| --- | --- | --- | --- | --- | --- |
| `001-36a203` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `4cd38a-review-handoff-packet-processor` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `595546-registration-count-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `5c4009-email-phishing-payment-review` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `612757-academic-integrity-case-review` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` |
| `7e61b2-calculate-total-expense` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `b6e11d-calculate-total-shipping-emissions` | `FAIL` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `PASS` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` |
| `ded93f-academic-integrity-data-code-review` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `harbor-export-acl-reconstruction-package` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `veladesk-memory-quarantine-review` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |

## Interpretation

- Codex runtime was the strongest baseline in this run: `4/20`, mean reward `0.200`.
- Every tested vLLM open-weight run passed the same single task and scored `1/20`, mean reward `0.050`.
- No Qwen or Gemma vLLM run passed a task that Codex failed.
- Dense variants did not improve aggregate score over the smaller/sparser variants in this harness setup.
- The Gemma dense run is not a perfect context-equivalent comparison because the 31B QAT model could not fit a 65k KV cache locally; it ran at 22,528 tokens.

## Reproducibility Pointers

Canonical local notes with raw job paths and command details:

```text
/Users/onur/repos/shellbench-local/reports/openclaw-local-runtime-benchmark.md
```

Those local notes may reference raw task names and job directories. They should remain outside this public repo unless redacted.
