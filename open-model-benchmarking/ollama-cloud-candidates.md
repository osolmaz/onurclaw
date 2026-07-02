# Ollama Cloud Model Candidates

Captured from the Ollama Cloud catalog on 2026-07-02.

This is a shortlist of hosted Ollama Cloud models worth trying next for ShellBench/OpenClaw. It records exact runnable Ollama tags where available.

Measured ShellBench results for this queue are saved in `shellbench-run-results.md`.

## Priority Queue

| Priority | Ollama model | Provider family | Context shown by Ollama | Capabilities shown by Ollama | Why try it |
| ---: | --- | --- | ---: | --- | --- |
| 1 | [`glm-5.2:cloud`](https://ollama.com/library/glm-5.2) | Z.ai GLM | 976K | tools, thinking | Strongest immediate ShellBench candidate: long-horizon coding focus, tool use, and very large context. |
| 2 | [`kimi-k2.7-code:cloud`](https://ollama.com/library/kimi-k2.7-code) | Moonshot Kimi | 256K | tools, thinking, vision | Coding-focused Kimi release with agentic/tool-use emphasis. |
| 3 | [`minimax-m3:cloud`](https://ollama.com/library/minimax-m3) | MiniMax | 512K guaranteed, 1M claimed | tools, thinking, vision | Agentic coding model with long-context positioning and hosted commercial availability. |
| 4 | [`deepseek-v4-flash:cloud`](https://ollama.com/library/deepseek-v4-flash) | DeepSeek | 1M | tools, thinking | Efficient DeepSeek V4 preview, likely cheaper/faster than Pro. |
| 5 | [`deepseek-v4-pro:cloud`](https://ollama.com/library/deepseek-v4-pro) | DeepSeek | 1M | tools, thinking | Stronger DeepSeek V4 variant; useful if Flash is promising or too weak. |
| 6 | [`qwen3.5:397b-cloud`](https://ollama.com/library/qwen3.5/tags) | Qwen | 256K | tools, thinking, vision | Hosted large Qwen 3.5 tag; useful comparison against local Qwen 3.6 results. |
| 7 | [`gemma4:cloud`](https://ollama.com/library/gemma4/tags) | Google Gemma | 256K | tools, thinking, vision | Hosted Gemma 4 comparison against local Gemma 4 dense/A4B runs. |

## Smoke Test Set

Use the same ShellBench/OpenClaw instructions and judge setup as prior runs. For a cheap first pass, run three public tasks before the full 20-task sweep:

| Task role | Public task slug |
| --- | --- |
| Known easy/control | `4cd38a-review-handoff-packet-processor` |
| Codex-only previous pass | `3954d9-warehouse-recall-lot-traceback` |
| Timeout/fragility probe | `5c4009-email-phishing-payment-review` |

Run the full public set only after the model can complete the smoke set with valid tool use and parsable final output.

## Source Pages

- Ollama Cloud catalog: https://ollama.com/search?c=cloud
- GLM 5.2: https://ollama.com/library/glm-5.2
- Kimi K2.7 Code: https://ollama.com/library/kimi-k2.7-code
- MiniMax M3: https://ollama.com/library/minimax-m3
- DeepSeek V4 Flash: https://ollama.com/library/deepseek-v4-flash
- DeepSeek V4 Pro: https://ollama.com/library/deepseek-v4-pro
- Qwen 3.5 tags: https://ollama.com/library/qwen3.5/tags
- Gemma 4 tags: https://ollama.com/library/gemma4/tags
