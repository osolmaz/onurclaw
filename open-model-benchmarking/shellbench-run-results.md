# ShellBench Public Task Results

Run dates: 2026-07-01 and 2026-07-02

Public task revision: `ShellBench/public-tasks@30d6135`

Task set: 20 Harbor public tasks.

This report lists scores only. It does not include task prompts, workspace files, generated artifacts, trajectories, judge prompts, or judge rationales.

## Run Summary

All rows are part of the same public-task result stream.

| Run | Runtime model id | Model artifact | Completed | Passed | Mean reward | Exceptions |
| --- | --- | --- | ---: | ---: | ---: | --- |
| Codex runtime | `openai/gpt-5.5` | Not a Hugging Face artifact | `20/20` | `4/20` | `0.200` | `1` timeout |
| Qwen A3B | `openai/qwen-vllm` | [`lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit) | `20/20` | `1/20` | `0.050` | `1` timeout |
| Qwen dense | `openai/qwen-dense-vllm` | [`lmstudio-community/Qwen3.6-27B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-27B-MLX-4bit) | `20/20` | `1/20` | `0.050` | `2` timeouts |
| Gemma A4B | `openai/gemma-vllm` | [`lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit`](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit) | `20/20` | `1/20` | `0.050` | `0` |
| Gemma dense | `openai/gemma-dense-vllm` | [`mlx-community/gemma-4-31B-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-4-31B-it-qat-4bit) | `20/20` | `1/20` | `0.050` | `0` |
| GLM 5.2 | `openai/glm-5.2:cloud` | [`glm-5.2:cloud`](https://ollama.com/library/glm-5.2) | `20/20` | `3/20` | `0.150` | `0` |
| Kimi K2.7 Code | `openai/kimi-k2.7-code:cloud` | [`kimi-k2.7-code:cloud`](https://ollama.com/library/kimi-k2.7-code) | `20/20` | `2/20` | `0.100` | `0` |
| MiniMax M3 | `openai/minimax-m3:cloud` | [`minimax-m3:cloud`](https://ollama.com/library/minimax-m3) | `20/20` | `3/20` | `0.150` | `1` timeout |
| DeepSeek V4 Flash | `openai/deepseek-v4-flash:cloud` | [`deepseek-v4-flash:cloud`](https://ollama.com/library/deepseek-v4-flash) | `20/20` | `4/20` | `0.200` | `0` |
| DeepSeek V4 Pro | `openai/deepseek-v4-pro:cloud` | [`deepseek-v4-pro:cloud`](https://ollama.com/library/deepseek-v4-pro) | `20/20` | `5/20` | `0.250` | `1` agent exit |
| Qwen 3.5 397B | `openai/qwen3.5:397b-cloud` | [`qwen3.5:397b-cloud`](https://ollama.com/library/qwen3.5/tags) | `20/20` | `2/20` | `0.100` | `0` |
| Gemma 4 cloud | `openai/gemma4:cloud` | [`gemma4:cloud`](https://ollama.com/library/gemma4/tags) | `20/20` | `1/20` | `0.050` | `1` timeout |

## Combined Task Results

<details open>
<summary>Task-by-run matrix</summary>

| Public task slug | [`openai/gpt-5.5`](https://platform.openai.com/docs/models) | [`lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit) | [`lmstudio-community/Qwen3.6-27B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-27B-MLX-4bit) | [`lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit`](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit) | [`mlx-community/gemma-4-31B-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-4-31B-it-qat-4bit) | [`glm-5.2:cloud`](https://ollama.com/library/glm-5.2) | [`kimi-k2.7-code:cloud`](https://ollama.com/library/kimi-k2.7-code) | [`minimax-m3:cloud`](https://ollama.com/library/minimax-m3) | [`deepseek-v4-flash:cloud`](https://ollama.com/library/deepseek-v4-flash) | [`deepseek-v4-pro:cloud`](https://ollama.com/library/deepseek-v4-pro) | [`qwen3.5:397b-cloud`](https://ollama.com/library/qwen3.5/tags) | [`gemma4:cloud`](https://ollama.com/library/gemma4/tags) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `001-36a203` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `FAIL` | `FAIL` |
| `4cd38a-review-handoff-packet-processor` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` | `FAIL` | `FAIL (timeout)` |
| `595546-registration-count-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `5c4009-email-phishing-payment-review` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `FAIL` | `FAIL` | `FAIL` |
| `612757-academic-integrity-case-review` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `7e61b2-calculate-total-expense` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `b6e11d-calculate-total-shipping-emissions` | `FAIL` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `PASS` | `FAIL` | `PASS` | `PASS` | `PASS` | `FAIL` | `FAIL` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `PASS` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `PASS` | `FAIL` |
| `ded93f-academic-integrity-data-code-review` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `FAIL` | `FAIL` |
| `harbor-export-acl-reconstruction-package` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `veladesk-memory-quarantine-review` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |

</details>

## Per-Run Details

<details>
<summary>Codex runtime, <code>openai/gpt-5.5</code>: 4/20 passed</summary>

Passed: `3954d9-warehouse-recall-lot-traceback`, `4cd38a-review-handoff-packet-processor`, `d18909-inbox-calendar-conflict-resolution-local-draft`, `ded93f-academic-integrity-data-code-review`.

Exceptions: `5c4009-email-phishing-payment-review` timed out.

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

## Notes

- All runs used Harbor with OpenClaw and the same Codex-backed verifier judge.
- The local open-weight runs used vLLM Metal.
- The hosted Ollama Cloud runs used the stock OpenClaw embedded runtime against Ollama Cloud.
- Qwen A3B, Qwen dense, and Gemma A4B ran with a 65,536-token context.
- Gemma dense ran with a 22,528-token context because the 31B QAT artifact could not fit a 65k KV cache locally.
