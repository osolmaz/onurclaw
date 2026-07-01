# ShellBench Public Task Results

Run date: 2026-07-01

Public task revision: `ShellBench/public-tasks@30d6135`

Task set: 20 Harbor public tasks.

This report lists scores only. It does not include task prompts, workspace files, generated artifacts, trajectories, judge prompts, or judge rationales.

## Aggregate Results

| Run | Completed | Passed | Mean reward | Exceptions |
| --- | ---: | ---: | ---: | --- |
| Codex runtime, `openai/gpt-5.5` | `20/20` | `4/20` | `0.200` | `1` timeout |
| Qwen A3B, `openai/qwen-vllm` | `20/20` | `1/20` | `0.050` | `1` timeout |
| Qwen dense, `openai/qwen-dense-vllm` | `20/20` | `1/20` | `0.050` | `2` timeouts |
| Gemma A4B, `openai/gemma-vllm` | `20/20` | `1/20` | `0.050` | `0` |
| Gemma dense, `openai/gemma-dense-vllm` | `20/20` | `1/20` | `0.050` | `0` |

## Models

| Run | Runtime model id | Model artifact |
| --- | --- | --- |
| Codex runtime | `openai/gpt-5.5` | Not a Hugging Face artifact |
| Qwen A3B | `openai/qwen-vllm` | [`lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit) |
| Qwen dense | `openai/qwen-dense-vllm` | [`lmstudio-community/Qwen3.6-27B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-27B-MLX-4bit) |
| Gemma A4B | `openai/gemma-vllm` | [`lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit`](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit) |
| Gemma dense | `openai/gemma-dense-vllm` | [`mlx-community/gemma-4-31B-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-4-31B-it-qat-4bit) |

## Passed Tasks

| Run | Passed task slugs |
| --- | --- |
| Codex runtime | `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`, `d18909-inbox-calendar-conflict-resolution-local-draft`, `ded93f-academic-integrity-data-code-review` |
| Qwen A3B | `4cd38a-review-handoff-packet-processor` |
| Qwen dense | `4cd38a-review-handoff-packet-processor` |
| Gemma A4B | `4cd38a-review-handoff-packet-processor` |
| Gemma dense | `4cd38a-review-handoff-packet-processor` |

## Timeout Failures

| Run | Timeout task slugs |
| --- | --- |
| Codex runtime | `5c4009-email-phishing-payment-review` |
| Qwen A3B | `612757-academic-integrity-case-review` |
| Qwen dense | `b6e11d-calculate-total-shipping-emissions`, `d18909-inbox-calendar-conflict-resolution-local-draft` |
| Gemma A4B | None |
| Gemma dense | None |

## Row-Level Data

Full pass/fail rows are in [`shellbench-run-results.csv`](shellbench-run-results.csv). The CSV has one row per run and task, so this report can stay readable as more models are added.

## Notes

- All runs used Harbor with OpenClaw and the same Codex-backed verifier judge.
- The open-weight runs used vLLM Metal.
- Qwen A3B, Qwen dense, and Gemma A4B ran with a 65,536-token context.
- Gemma dense ran with a 22,528-token context because the 31B QAT artifact could not fit a 65k KV cache locally.
