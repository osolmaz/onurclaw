# ShellBench Public Task Results

Run dates: 2026-07-01 and 2026-07-02 (Mac vLLM Metal + cloud/API rows);
2026-07-05 and 2026-07-06 (DGX Spark GB10, local vLLM, NVFP4 rows).

Public task revision: `ShellBench/public-tasks@30d6135` (Mac/cloud rows);
`ShellBench/public-tasks@8b46e4d4` (DGX Spark rows).

Task set: the Run Summary below is the 20 Harbor public tasks. The DGX Spark
NVFP4 models were additionally run on the separate 115-task bundle; those
scores are kept in their own section (## 115-Task Bundle Results) because it
is a different, larger task set — the two sets share 13 tasks by content, but
neither is a subset of the other.

This report lists scores only. It does not include task prompts, workspace files, generated artifacts, trajectories, judge prompts, or judge rationales.

## Run Summary

All rows are part of the same public-task result stream and are sorted by decreasing mean reward.

| Run | Runtime model id | Model artifact | Completed | Passed | Mean reward | Score | Exceptions | Run via |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| Claude Code Opus 4.8 | `claude-cli/opus` | [`claude-opus-4-8`](https://docs.anthropic.com/en/docs/about-claude/models/all-models) | `20/20` | `6/20` | `0.300` | `30%` | `0` | Claude Code API |
| Claude Code Sonnet 5 | `claude-cli/sonnet` | [`claude-sonnet-5`](https://docs.anthropic.com/en/docs/about-claude/models/all-models) | `20/20` | `5/20` | `0.250` | `25%` | `0` | Claude Code API |
| DeepSeek V4 Pro | `openai/deepseek-v4-pro:cloud` | [`deepseek-v4-pro:cloud`](https://ollama.com/library/deepseek-v4-pro) | `20/20` | `5/20` | `0.250` | `25%` | `1` agent exit | Ollama Cloud API |
| OpenAI GPT-5.5 | `openai/gpt-5.5` | [`gpt-5.5`](https://platform.openai.com/docs/models) | `20/20` | `4/20` | `0.200` | `20%` | `1` timeout | OpenAI/Codex API |
| DeepSeek V4 Flash | `openai/deepseek-v4-flash:cloud` | [`deepseek-v4-flash:cloud`](https://ollama.com/library/deepseek-v4-flash) | `20/20` | `4/20` | `0.200` | `20%` | `0` | Ollama Cloud API |
| GLM 5.2 | `openai/glm-5.2:cloud` | [`glm-5.2:cloud`](https://ollama.com/library/glm-5.2) | `20/20` | `3/20` | `0.150` | `15%` | `0` | Ollama Cloud API |
| MiniMax M3 | `openai/minimax-m3:cloud` | [`minimax-m3:cloud`](https://ollama.com/library/minimax-m3) | `20/20` | `3/20` | `0.150` | `15%` | `1` timeout | Ollama Cloud API |
| OpenAI GPT-5.4 mini | `openai/gpt-5.4-mini` | [`gpt-5.4-mini`](https://platform.openai.com/docs/models) | `20/20` | `2/20` | `0.100` | `10%` | `12` agent exits, `1` timeout | OpenAI/Codex API |
| Kimi K2.7 Code | `openai/kimi-k2.7-code:cloud` | [`kimi-k2.7-code:cloud`](https://ollama.com/library/kimi-k2.7-code) | `20/20` | `2/20` | `0.100` | `10%` | `0` | Ollama Cloud API |
| Qwen 3.5 397B | `openai/qwen3.5:397b-cloud` | [`qwen3.5:397b-cloud`](https://ollama.com/library/qwen3.5/tags) | `20/20` | `2/20` | `0.100` | `10%` | `0` | Ollama Cloud API |
| Qwen dense (Spark NVFP4) | `openai/qwen-dense-vllm` | [`nvidia/Qwen3.6-27B-NVFP4`](https://huggingface.co/nvidia/Qwen3.6-27B-NVFP4) | `20/20` | `2/20` | `0.100` | `10%` | `9` timeouts, `2` agent exits | Local vLLM DGX Spark (GB10) |
| Gemma 4 cloud | `openai/gemma4:cloud` | [`gemma4:cloud`](https://ollama.com/library/gemma4/tags) | `20/20` | `1/20` | `0.050` | `5%` | `1` timeout | Ollama Cloud API |
| Gemma A4B | `openai/gemma-vllm` | [`lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit`](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit) | `20/20` | `1/20` | `0.050` | `5%` | `0` | Local vLLM Metal |
| Gemma dense | `openai/gemma-dense-vllm` | [`mlx-community/gemma-4-31B-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-4-31B-it-qat-4bit) | `20/20` | `1/20` | `0.050` | `5%` | `0` | Local vLLM Metal |
| Qwen A3B | `openai/qwen-vllm` | [`lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit) | `20/20` | `1/20` | `0.050` | `5%` | `1` timeout | Local vLLM Metal |
| Qwen dense | `openai/qwen-dense-vllm` | [`lmstudio-community/Qwen3.6-27B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-27B-MLX-4bit) | `20/20` | `1/20` | `0.050` | `5%` | `2` timeouts | Local vLLM Metal |
| Qwen A3B (Spark NVFP4) | `openai/qwen-vllm` | [`nvidia/Qwen3.6-35B-A3B-NVFP4`](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4) | `20/20` | `1/20` | `0.050` | `5%` | `11` timeouts, `8` agent exits | Local vLLM DGX Spark (GB10) |
| Gemma dense (Spark NVFP4) | `openai/gemma-dense-vllm` | [`nvidia/Gemma-4-31B-IT-NVFP4`](https://huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4) | `20/20` | `1/20` | `0.050` | `5%` | `7` timeouts | Local vLLM DGX Spark (GB10) |
| diffusiongemma A4B (Spark NVFP4) | `openai/gemma-vllm` | [`nvidia/diffusiongemma-26B-A4B-it-NVFP4`](https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4) | `20/20` | `1/20` | `0.050` | `5%` | `5` timeouts | Local vLLM DGX Spark (GB10) |

## Combined Task Results

<details open>
<summary>Task-by-run matrix</summary>

| Public task slug | [`openai/gpt-5.5`](https://platform.openai.com/docs/models) | [`lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit) | [`lmstudio-community/Qwen3.6-27B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-27B-MLX-4bit) | [`lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit`](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit) | [`mlx-community/gemma-4-31B-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-4-31B-it-qat-4bit) | [`glm-5.2:cloud`](https://ollama.com/library/glm-5.2) | [`kimi-k2.7-code:cloud`](https://ollama.com/library/kimi-k2.7-code) | [`minimax-m3:cloud`](https://ollama.com/library/minimax-m3) | [`deepseek-v4-flash:cloud`](https://ollama.com/library/deepseek-v4-flash) | [`deepseek-v4-pro:cloud`](https://ollama.com/library/deepseek-v4-pro) | [`qwen3.5:397b-cloud`](https://ollama.com/library/qwen3.5/tags) | [`gemma4:cloud`](https://ollama.com/library/gemma4/tags) | [`claude-sonnet-5`](https://docs.anthropic.com/en/docs/about-claude/models/all-models) | [`claude-opus-4-8`](https://docs.anthropic.com/en/docs/about-claude/models/all-models) | [`openai/gpt-5.4-mini`](https://platform.openai.com/docs/models) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `001-36a203` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `FAIL` | `FAIL` | `PASS` | `PASS` | `PASS` |
| `4cd38a-review-handoff-packet-processor` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS (agent exit)` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` | `FAIL` | `FAIL (timeout)` | `PASS` | `PASS` | `FAIL (agent exit)` |
| `595546-registration-count-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` |
| `5c4009-email-phishing-payment-review` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` |
| `612757-academic-integrity-case-review` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (timeout)` |
| `7e61b2-calculate-total-expense` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` |
| `b6e11d-calculate-total-shipping-emissions` | `FAIL` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `PASS` | `FAIL` | `PASS` | `PASS` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `FAIL (agent exit)` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `PASS` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `PASS` | `FAIL` | `PASS` | `PASS` | `FAIL` |
| `ded93f-academic-integrity-data-code-review` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `FAIL` | `FAIL` | `PASS` | `PASS` | `FAIL (agent exit)` |
| `harbor-export-acl-reconstruction-package` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` |
| `veladesk-memory-quarantine-review` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |

</details>

## 115-Task Bundle Results (DGX Spark, NVFP4)

Separate, larger task set (`ShellBench/public-tasks@8b46e4d4`, `tasks/115-tasks`),
run only on the DGX Spark local vLLM NVFP4 models. Not comparable row-for-row
with the 20-task Run Summary above; the two sets share 13 tasks by content but
neither is a subset of the other. Mean reward is over all 115 tasks (partial
rubric credit counts fractionally). Each run had exactly one task fail on
infrastructure (not model behavior); those were re-run individually and both
scored 0.0, so totals reflect a full 115/115 scored.

| Run | Model artifact | Completed | Passed | Mean reward | Score | Exceptions |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Qwen A3B (Spark NVFP4) | [`nvidia/Qwen3.6-35B-A3B-NVFP4`](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4) | `115/115` | `5/115` | `0.0435` | `4.3%` | `8` agent exits, `1` timeout (all re-run/scored) |
| diffusiongemma A4B (Spark NVFP4) | [`nvidia/diffusiongemma-26B-A4B-it-NVFP4`](https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4) | `115/115` | `1/115` (+`1` partial `0.625`) | `0.0141` | `1.4%` | `1` docker-net error, `4` timeouts (all re-run/scored) |

<details>
<summary>Qwen A3B 115-task passes</summary>

Passed (`1.0`): `003fed-walnut-frame-apology`, `23e601-omar-mixup-brief`, `3954d9-recall-shipment-traceback`, `39f287-briarlane-review-note`, `59a51f-retail-audience-prune`.

</details>

<details>
<summary>diffusiongemma A4B 115-task passes</summary>

Passed (`1.0`): `3954d9-recall-shipment-traceback`. Partial (`0.625`): `29509f-northstar-agenda-queue`.

</details>

## Per-Run Details

<details>
<summary>OpenAI GPT-5.5, <code>openai/gpt-5.5</code>: 4/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`, `d18909-inbox-calendar-conflict-resolution-local-draft`, `ded93f-academic-integrity-data-code-review`.

Exceptions: `5c4009-email-phishing-payment-review` timed out.

</details>

<details>
<summary>OpenAI GPT-5.4 mini, <code>openai/gpt-5.4-mini</code> with <code>xhigh</code> thinking: 2/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`.

Exceptions: `4cd38a-review-handoff-packet-processor`, `58e6cb-revenue-reconciliation-close`, `595546-registration-count-audit`, `5c4009-email-phishing-payment-review`, `7e61b2-calculate-total-expense`, `9f5c9a-iam-effective-access-audit`, `b6e11d-calculate-total-shipping-emissions`, `ded93f-academic-integrity-data-code-review`, `harbor-export-acl-reconstruction-package`, `morrow-vale-couriers-dispute-evidence-bundle`, `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil`, and `riverstone-paybridge-timeout-reconciliation` failed with `NonZeroAgentExitCodeError`; `612757-academic-integrity-case-review` timed out.

</details>

<details>
<summary>Qwen A3B, <code>openai/qwen-vllm</code>: 1/20 passed</summary>

Passed: `4cd38a-review-handoff-packet-processor`.

Exceptions: `612757-academic-integrity-case-review` timed out.

</details>

<details>
<summary>Qwen dense, <code>openai/qwen-dense-vllm</code>: 1/20 passed</summary>

Passed: `4cd38a-review-handoff-packet-processor`.

Exceptions: `b6e11d-calculate-total-shipping-emissions` and `d18909-inbox-calendar-conflict-resolution-local-draft` timed out.

</details>

<details>
<summary>Gemma A4B, <code>openai/gemma-vllm</code>: 1/20 passed</summary>

Passed: `4cd38a-review-handoff-packet-processor`.

Exceptions: none.

</details>

<details>
<summary>Gemma dense, <code>openai/gemma-dense-vllm</code>: 1/20 passed</summary>

Passed: `4cd38a-review-handoff-packet-processor`.

Exceptions: none.

</details>

<details>
<summary>GLM 5.2, <code>openai/glm-5.2:cloud</code>: 3/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`, `b6e11d-calculate-total-shipping-emissions`.

Exceptions: none.

</details>

<details>
<summary>Kimi K2.7 Code, <code>openai/kimi-k2.7-code:cloud</code>: 2/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`.

Exceptions: none.

</details>

<details>
<summary>MiniMax M3, <code>openai/minimax-m3:cloud</code>: 3/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`, `b6e11d-calculate-total-shipping-emissions`.

Exceptions: `7e61b2-calculate-total-expense` timed out.

</details>

<details>
<summary>DeepSeek V4 Flash, <code>openai/deepseek-v4-flash:cloud</code>: 4/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`, `5c4009-email-phishing-payment-review`, `b6e11d-calculate-total-shipping-emissions`.

Exceptions: none.

</details>

<details>
<summary>DeepSeek V4 Pro, <code>openai/deepseek-v4-pro:cloud</code>: 5/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`, `b6e11d-calculate-total-shipping-emissions`, `d18909-inbox-calendar-conflict-resolution-local-draft`, `ded93f-academic-integrity-data-code-review`.

Exceptions: `58e6cb-revenue-reconciliation-close` failed with `NonZeroAgentExitCodeError`.

</details>

<details>
<summary>Qwen 3.5 397B, <code>openai/qwen3.5:397b-cloud</code>: 2/20 passed</summary>

Passed: `4cd38a-review-handoff-packet-processor`, `d18909-inbox-calendar-conflict-resolution-local-draft`.

Exceptions: none.

</details>

<details>
<summary>Gemma 4 cloud, <code>openai/gemma4:cloud</code>: 1/20 passed</summary>

Passed: `4cd38a-review-handoff-packet-processor`.

Exceptions: `58e6cb-revenue-reconciliation-close` timed out.

</details>

<details>
<summary>Claude Code Sonnet 5, <code>claude-cli/sonnet</code>: 5/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`, `58e6cb-revenue-reconciliation-close`, `d18909-inbox-calendar-conflict-resolution-local-draft`, `ded93f-academic-integrity-data-code-review`.

Exceptions: none.

</details>

<details>
<summary>Claude Code Opus 4.8, <code>claude-cli/opus</code>: 6/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`, `58e6cb-revenue-reconciliation-close`, `b6e11d-calculate-total-shipping-emissions`, `d18909-inbox-calendar-conflict-resolution-local-draft`, `ded93f-academic-integrity-data-code-review`.

Exceptions: none.

</details>

<details>
<summary>Qwen dense (Spark NVFP4), <code>nvidia/Qwen3.6-27B-NVFP4</code>: 2/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`. Best 20-task score of any local model in this report.

Exceptions: 9 `AgentTimeoutError`, 2 `NonZeroAgentExitCodeError`.

</details>

<details>
<summary>Qwen A3B (Spark NVFP4), <code>nvidia/Qwen3.6-35B-A3B-NVFP4</code>: 1/20 passed</summary>

Passed: `4cd38a-review-handoff-packet-processor`.

Exceptions: 11 `AgentTimeoutError`, 8 `NonZeroAgentExitCodeError` (several were manual stall reaps; this run predated the adapter stall-watchdog fix).

</details>

<details>
<summary>Gemma dense (Spark NVFP4), <code>nvidia/Gemma-4-31B-IT-NVFP4</code>: 1/20 passed</summary>

Passed: `4cd38a-review-handoff-packet-processor`.

Exceptions: 7 `AgentTimeoutError`.

</details>

<details>
<summary>diffusiongemma A4B (Spark NVFP4), <code>nvidia/diffusiongemma-26B-A4B-it-NVFP4</code>: 1/20 passed</summary>

Passed: `4cd38a-review-handoff-packet-processor`. Note: this is the diffusion-LM Gemma variant, NOT the plain `Gemma-4-26B-A4B`; it is not the counterpart of the Mac "Gemma A4B" row.

Exceptions: 5 `AgentTimeoutError`.

</details>

## Notes

- Claude Code runs used OpenClaw's `claude-cli` backend. `claude-cli/sonnet` resolved to `claude-sonnet-5`; `claude-cli/opus` resolved to `claude-opus-4-8`.
- The `openai/gpt-5.4-mini` run used the Codex runtime with `OPENCLAW_THINKING=xhigh`.
- Qwen A3B, Qwen dense, and Gemma A4B ran with a 65,536-token context.
- Gemma dense ran with a 22,528-token context because the 31B QAT artifact could not fit a 65k KV cache locally.
- `openai/gpt-5.5-mini` with `OPENCLAW_THINKING=xhigh` was attempted through the local Codex/OpenClaw route but was not scored: OpenClaw rejected it as unsupported for the available ChatGPT-account Codex auth route.
- DGX Spark (GB10, SM121) rows were served on local vLLM (0.24.0 for Qwen, 0.23.1 for Gemma), NVFP4 weights via ModelOpt, FP8 KV cache, prefix caching on, 65,536-token context, judged by a local codex-backed (`gpt-5.5`) OpenAI-compatible verifier proxy. Harness and full run notes: `dutifuldev/shellbench-local` (`reports/dgx-spark-nvfp4-shellbench-runs.md`).
- The Spark "diffusiongemma A4B" row uses `nvidia/diffusiongemma-26B-A4B-it-NVFP4`, a diffusion-LM Gemma variant — a DIFFERENT model from `Gemma-4-26B-A4B`. It is not the NVFP4 counterpart of the Mac "Gemma A4B" (`gemma-4-26B-A4B-it-QAT-MLX-4bit`) row. A run of the actual `nvidia/Gemma-4-26B-A4B-NVFP4` is still pending.
- Spark 20-task runs show high `AgentTimeoutError` counts vs the Mac runs: several 20-task tasks carry tight per-task agent caps (300 s) that Qwen/Gemma thinking=high exceeds at Spark decode speed (~21 tok/s). These are the same tasks the Mac runs also failed, so headline pass counts are unaffected.
