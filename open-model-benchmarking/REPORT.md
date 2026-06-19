# Open Model Benchmarking Report

Generated from snapshot: `hf-model-metadata-20260619T114556Z`.

This report is generated from the popular Hugging Face model metadata snapshot and `MODEL_MANUAL_CURATION.jsonl`.
The manual curation file contains only include/exclude decisions; downloads, likes, parameter counts, links, and capability signals are joined from the snapshot.

## Inputs

- Metadata: `snapshots/hf-model-metadata-20260619T114556Z/models.over-100k-downloads.csv`
- Manual curation: `MODEL_MANUAL_CURATION.jsonl`
- Popular threshold: `downloads > 100,000`

## Summary

- Popular models curated: 430
- Included OpenClaw candidates: 254
- Excluded models: 176
- Text candidates: 140
- Coding candidates: 21
- Multimodal candidates: 89
- Special-architecture candidates: 4

## Curation Policy

Included models are likely OpenClaw/ShellBench backend candidates: chat, instruct, coding, reasoning, conversational, or agent-like multimodal models.
Excluded models are popular but not primary agent backends: embeddings, rerankers, ASR/TTS/audio utilities, OCR/parser-only models, safety guards, image-only models, base/pretrain-only checkpoints, and narrow domain support models.

## Included Candidate Table

| Model | Downloads | Likes | Params | Class | Pipeline | License | Router | Signals |
| --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | 27,537,244 | 1,342 | 0.75B | text | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) | 16,538,166 | 639 | 4.02B | text | text-generation | apache-2.0 | no |  |
| [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) | 12,905,733 | 1,370 | 7.62B | text | text-generation | apache-2.0 | yes | router, tools, structured, conversational |
| [google/gemma-4-26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it) | 12,670,159 | 1,162 | 26.5B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | 12,574,844 | 1,149 | 8.19B | text | text-generation | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen2.5-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) | 11,534,184 | 504 | 3.09B | text | text-generation | other | no | conversational |
| [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it) | 11,081,369 | 3,026 | 32.7B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) | 10,672,297 | 743 | 1.54B | text | text-generation | apache-2.0 | no | conversational |
| [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | 9,845,394 | 6,112 | 8.03B | text | text-generation | llama3.1 | yes | router, tools, structured, conversational |
| [Qwen/Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) | 9,599,668 | 656 | 4.66B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) | 9,394,272 | 1,578 | 9.65B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) | 8,191,345 | 1,487 | 1.24B | text | text-generation | llama3.2 | no | conversational |
| [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) | 8,018,709 | 1,586 | 8.29B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [Qwen/Qwen3-VL-8B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct) | 7,456,814 | 966 | 8.77B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [deepseek-ai/DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) | 7,228,990 | 2,452 | 685B | text | text-generation | mit | yes | router, tools, structured, quant, conversational |
| [deepseek-ai/DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | 6,838,667 | 13,400 | 685B | text | text-generation | mit | yes | router, tools, structured, quant, conversational |
| [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) | 6,827,013 | 4,714 | 21.5B | text | text-generation | apache-2.0 | yes | router, tools, structured, conversational |
| [google/gemma-4-E4B-it](https://huggingface.co/google/gemma-4-E4B-it) | 6,192,711 | 1,262 | 8.00B | multimodal | any-to-any | apache-2.0 | no |  |
| [Qwen/Qwen3.6-27B-FP8](https://huggingface.co/Qwen/Qwen3.6-27B-FP8) | 5,953,987 | 277 | 27.8B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3.6-27B](https://huggingface.co/Qwen/Qwen3.6-27B) | 5,953,871 | 1,749 | 27.8B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | 5,594,875 | 486 | 2.03B | text | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen3.6-35B-A3B-FP8](https://huggingface.co/Qwen/Qwen3.6-35B-A3B-FP8) | 5,473,777 | 273 | 36.0B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) | 5,375,575 | 659 | 3.75B | multimodal | image-text-to-text | unknown | no | conversational |
| [Qwen/Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) | 5,182,283 | 880 | 4.02B | text | text-generation | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen3.6-35B-A3B](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | 5,009,985 | 2,167 | 36.0B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen2.5-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) | 4,710,885 | 534 | 0.49B | text | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen2.5-Coder-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) | 4,344,322 | 165 | 14.8B | coding | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen3-VL-4B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct) | 4,336,083 | 398 | 4.44B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [Qwen/Qwen3-VL-32B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-32B-Instruct) | 4,204,234 | 205 | 33.4B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) | 4,088,083 | 4,897 | 120B | text | text-generation | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | 3,965,070 | 702 | 32.8B | text | text-generation | apache-2.0 | yes | router, tools, conversational |
| [Qwen/Qwen2-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct) | 3,923,367 | 510 | 2.21B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [Qwen/Qwen2-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct) | 3,719,880 | 162 | 1.54B | text | text-generation | apache-2.0 | no | conversational |
| [deepseek-ai/DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) | 3,520,550 | 1,450 | 685B | text | text-generation | mit | yes | router, tools, structured, quant, conversational |
| [nvidia/Qwen3.6-35B-A3B-NVFP4](https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4) | 3,400,521 | 240 | 18.7B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-7B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-AWQ) | 3,256,939 | 46 | 7.62B | text | text-generation | apache-2.0 | no | quant, conversational |
| [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 3,015,772 | 4,960 | 862B | text | text-generation | mit | yes | router, tools, structured, quant, conversational |
| [MiniMaxAI/MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) | 2,785,657 | 1,217 | 229B | text | text-generation | other | yes | router, tools, structured, quant, conversational |
| [moonshotai/Kimi-K2.6](https://huggingface.co/moonshotai/Kimi-K2.6) | 2,676,473 | 1,466 | 1059B | multimodal | image-text-to-text | other | yes | router, tools, structured, conversational |
| [deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) | 2,548,735 | 1,534 | 158B | text | text-generation | mit | yes | router, tools, structured, quant, conversational |
| [Qwen/Qwen3.5-0.8B](https://huggingface.co/Qwen/Qwen3.5-0.8B) | 2,484,282 | 580 | 0.87B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [Qwen/Qwen3.5-27B](https://huggingface.co/Qwen/Qwen3.5-27B) | 2,447,387 | 987 | 27.8B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [google/gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it) | 2,424,145 | 759 | 12.2B | multimodal | image-text-to-text | gemma | yes | router, tools, structured, conversational |
| [google/gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it) | 2,422,290 | 758 | 5.12B | multimodal | any-to-any | apache-2.0 | no |  |
| [Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) | 2,355,343 | 900 | 30.5B | text | text-generation | apache-2.0 | no | tools |
| [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) | 2,278,905 | 1,447 | 36.0B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen2.5-Coder-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) | 2,198,809 | 735 | 7.62B | coding | text-generation | apache-2.0 | yes | router, structured, conversational |
| [zai-org/GLM-5-FP8](https://huggingface.co/zai-org/GLM-5-FP8) | 2,180,892 | 181 | 754B | text | text-generation | mit | no | quant, conversational |
| [Qwen/Qwen3-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct) | 2,139,105 | 425 | 2.13B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [google/gemma-3-1b-it](https://huggingface.co/google/gemma-3-1b-it) | 2,105,621 | 1,015 | 1.00B | text | text-generation | gemma | no | conversational |
| [Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) | 2,049,724 | 412 | 14.8B | text | text-generation | apache-2.0 | yes | router, tools, conversational |
| [Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) | 2,039,559 | 350 | 14.8B | text | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen3-0.6B-FP8](https://huggingface.co/Qwen/Qwen3-0.6B-FP8) | 2,033,433 | 62 | 0.75B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-Omni-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct) | 2,023,010 | 942 | 35.3B | multimodal | any-to-any | other | no |  |
| [Qwen/Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct) | 1,974,930 | 1,281 | 8.29B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [moonshotai/Kimi-K2-Instruct-0905](https://huggingface.co/moonshotai/Kimi-K2-Instruct-0905) | 1,927,077 | 732 | 1026B | text | text-generation | other | yes | router, tools, quant, conversational |
| [Qwen/Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct) | 1,901,843 | 1,113 | 30.5B | coding | text-generation | apache-2.0 | yes | router, tools, structured, conversational |
| [moonshotai/Kimi-K2.5](https://huggingface.co/moonshotai/Kimi-K2.5) | 1,832,986 | 2,822 | 1059B | multimodal | image-text-to-text | other | yes | router, tools, structured, conversational |
| [Qwen/Qwen3-14B-AWQ](https://huggingface.co/Qwen/Qwen3-14B-AWQ) | 1,808,961 | 69 | 14.8B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2-VL-7B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct-AWQ) | 1,806,884 | 49 | 8.29B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) | 1,787,602 | 2,046 | 32.8B | coding | text-generation | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen3-VL-235B-A22B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct) | 1,783,876 | 394 | 236B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) | 1,772,379 | 2,245 | 3.21B | text | text-generation | llama3.2 | no | conversational |
| [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash) | 1,746,150 | 1,750 | 31.2B | text | text-generation | mit | yes | router, tools, conversational |
| [Qwen/Qwen3.5-2B](https://huggingface.co/Qwen/Qwen3.5-2B) | 1,738,947 | 307 | 2.27B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [nvidia/Gemma-4-31B-IT-NVFP4](https://huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4) | 1,729,159 | 511 | 20.9B | text | text-generation | other | no | quant |
| [Qwen/Qwen2.5-72B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct-AWQ) | 1,722,962 | 78 | 73.0B | text | text-generation | other | no | quant, conversational |
| [nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16) | 1,605,619 | 93 | 3.97B | text | text-generation | other | no | conversational |
| [google/gemma-4-12B-it](https://huggingface.co/google/gemma-4-12B-it) | 1,590,882 | 1,091 | 12.0B | multimodal | any-to-any | apache-2.0 | no |  |
| [nvidia/Gemma-4-26B-A4B-NVFP4](https://huggingface.co/nvidia/Gemma-4-26B-A4B-NVFP4) | 1,590,578 | 79 | 14.4B | text | text-generation | apache-2.0 | no | quant, conversational |
| [google/gemma-3-4b-it](https://huggingface.co/google/gemma-3-4b-it) | 1,588,790 | 1,371 | 4.30B | multimodal | image-text-to-text | gemma | yes | router, tools, structured, conversational |
| [nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4) | 1,576,022 | 357 | 67.2B | text | text-generation | other | no | quant, conversational |
| [Qwen/Qwen3.5-35B-A3B-FP8](https://huggingface.co/Qwen/Qwen3.5-35B-A3B-FP8) | 1,543,801 | 150 | 36.0B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3.5-27B-FP8](https://huggingface.co/Qwen/Qwen3.5-27B-FP8) | 1,539,976 | 134 | 27.8B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3.5-122B-A10B-FP8](https://huggingface.co/Qwen/Qwen3.5-122B-A10B-FP8) | 1,445,141 | 104 | 125B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-14B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-AWQ) | 1,443,371 | 37 | 14.8B | text | text-generation | apache-2.0 | no | quant, conversational |
| [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | 1,434,477 | 4,615 | 8.03B | text | text-generation | llama3 | yes | router, structured, conversational |
| [Qwen/Qwen2.5-Coder-32B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct-AWQ) | 1,425,258 | 37 | 32.8B | coding | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-Coder-Next-FP8](https://huggingface.co/Qwen/Qwen3-Coder-Next-FP8) | 1,418,215 | 151 | 79.7B | coding | text-generation | apache-2.0 | no | quant, conversational |
| [nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16) | 1,407,147 | 769 | 31.6B | text | text-generation | other | no | conversational |
| [zai-org/GLM-5.1-FP8](https://huggingface.co/zai-org/GLM-5.1-FP8) | 1,320,045 | 116 | 754B | text | text-generation | mit | yes | router, tools, quant, conversational |
| [nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4) | 1,316,150 | 142 | 18.3B | multimodal | any-to-any | other | no | quant |
| [nvidia/Kimi-K2.5-NVFP4](https://huggingface.co/nvidia/Kimi-K2.5-NVFP4) | 1,306,569 | 86 |  | text | text-generation | other | no | quant, conversational |
| [google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) | 1,261,246 | 1,981 | 27.4B | multimodal | image-text-to-text | gemma | yes | router, tools, structured, conversational |
| [nvidia/DeepSeek-R1-0528-NVFP4-v2](https://huggingface.co/nvidia/DeepSeek-R1-0528-NVFP4-v2) | 1,248,004 | 23 | 394B | text | text-generation | mit | no | quant, conversational |
| [nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1](https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1) | 1,195,477 | 181 | 8.72B | multimodal | image-text-to-text | other | no |  |
| [google/gemma-4-12B-it-qat-w4a16-ct](https://huggingface.co/google/gemma-4-12B-it-qat-w4a16-ct) | 1,185,286 | 28 | 13.3B | multimodal | any-to-any | apache-2.0 | no | quant |
| [Qwen/Qwen2.5-VL-7B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct-AWQ) | 1,181,803 | 105 | 8.29B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct) | 1,131,794 | 611 | 15.7B | coding | text-generation | other | no | conversational |
| [Qwen/Qwen3-8B-AWQ](https://huggingface.co/Qwen/Qwen3-8B-AWQ) | 1,104,191 | 47 | 8.19B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) | 1,098,539 | 352 | 32.8B | text | text-generation | apache-2.0 | no | conversational |
| [nvidia/Kimi-K2.6-NVFP4](https://huggingface.co/nvidia/Kimi-K2.6-NVFP4) | 1,095,410 | 36 |  | text | text-generation | other | no | quant, conversational |
| [Qwen/Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next) | 1,084,627 | 1,464 | 79.7B | coding | text-generation | apache-2.0 | yes | router, tools, conversational |
| [deepseek-ai/DeepSeek-V2-Lite-Chat](https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite-Chat) | 1,075,958 | 141 | 15.7B | text | text-generation | other | no | conversational |
| [deepseek-ai/DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) | 1,073,183 | 4,089 | 685B | text | text-generation | unknown | yes | router, tools, quant, conversational |
| [nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16) | 1,043,618 | 384 | 124B | text | text-generation | other | no | conversational |
| [deepseek-ai/DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) | 996,458 | 3,128 | 685B | text | text-generation | mit | yes | router, tools, structured, quant, conversational |
| [Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8) | 968,235 | 184 | 30.5B | coding | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-Coder-14B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct-AWQ) | 958,774 | 21 | 14.8B | coding | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3.5-122B-A10B](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) | 937,780 | 574 | 125B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, conversational |
| [Qwen/Qwen3.5-397B-A17B-FP8](https://huggingface.co/Qwen/Qwen3.5-397B-A17B-FP8) | 871,678 | 179 | 403B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-1.5B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-AWQ) | 870,588 | 7 | 1.78B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-32B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-AWQ) | 823,252 | 101 | 32.8B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-4B-Instruct-2507-FP8](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507-FP8) | 822,689 | 78 | 4.41B | text | text-generation | apache-2.0 | no | quant, conversational |
| [nvidia/Llama-3_3-Nemotron-Super-49B-v1_5](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1_5) | 799,175 | 233 | 49.9B | text | text-generation | other | no | conversational |
| [nvidia/NVIDIA-Nemotron-Nano-9B-v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2) | 798,844 | 495 | 8.89B | text | text-generation | other | no | conversational |
| [Qwen/Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) | 796,321 | 815 | 30.5B | text | text-generation | apache-2.0 | no | conversational |
| [nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-NVFP4) | 768,223 | 157 | 18.2B | text | text-generation | other | no | quant, conversational |
| [Qwen/Qwen2.5-Coder-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct) | 761,444 | 128 | 1.54B | coding | text-generation | apache-2.0 | no | conversational |
| [allenai/Molmo2-8B](https://huggingface.co/allenai/Molmo2-8B) | 743,353 | 189 | 8.66B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [Qwen/Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) | 733,641 | 1,096 | 235B | text | text-generation | apache-2.0 | yes | router, tools, conversational |
| [Qwen/Qwen2-7B-Instruct](https://huggingface.co/Qwen/Qwen2-7B-Instruct) | 697,647 | 687 | 7.62B | text | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen2-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct) | 690,251 | 201 | 0.49B | text | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen3-VL-8B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-FP8) | 686,851 | 71 | 8.77B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3.5-35B-A3B-GPTQ-Int4](https://huggingface.co/Qwen/Qwen3.5-35B-A3B-GPTQ-Int4) | 679,136 | 89 | 36.0B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | 676,216 | 2,834 | 70.6B | text | text-generation | llama3.3 | yes | router, tools, structured, conversational |
| [meta-llama/Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | 669,043 | 1,308 | 109B | multimodal | image-text-to-text | other | yes | router, tools, structured, conversational |
| [meta-llama/Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) | 665,910 | 926 | 70.6B | text | text-generation | llama3.1 | yes | router, tools, structured, conversational |
| [nvidia/Cosmos-Reason2-2B](https://huggingface.co/nvidia/Cosmos-Reason2-2B) | 661,409 | 104 | 2.44B | multimodal | image-text-to-text | other | no | conversational |
| [deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) | 654,603 | 1,526 | 1.78B | text | text-generation | mit | no | conversational |
| [deepseek-ai/DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) | 652,637 | 1,567 | 32.8B | text | text-generation | mit | no | conversational |
| [Qwen/Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) | 650,936 | 1,515 | 403B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [Qwen/Qwen3-4B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507) | 650,301 | 599 | 4.02B | text | text-generation | apache-2.0 | yes | router, tools, structured, conversational |
| [nvidia/Qwen3.5-397B-A17B-NVFP4](https://huggingface.co/nvidia/Qwen3.5-397B-A17B-NVFP4) | 632,646 | 100 |  | text | text-generation | apache-2.0 | no | quant, conversational |
| [MiniMaxAI/MiniMax-M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5) | 607,321 | 1,497 | 229B | text | text-generation | other | yes | router, tools, quant, conversational |
| [google/diffusiongemma-26B-A4B-it](https://huggingface.co/google/diffusiongemma-26B-A4B-it) | 601,208 | 1,007 | 25.8B | special-architecture | image-text-to-text | apache-2.0 | no | conversational |
| [Qwen/Qwen3-VL-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Instruct) | 591,966 | 577 | 31.1B | multimodal | image-text-to-text | apache-2.0 | yes | router, tools, structured, conversational |
| [zai-org/GLM-4.1V-9B-Thinking](https://huggingface.co/zai-org/GLM-4.1V-9B-Thinking) | 570,610 | 776 | 10.3B | multimodal | image-text-to-text | mit | no | conversational |
| [deepseek-ai/deepseek-coder-7b-instruct-v1.5](https://huggingface.co/deepseek-ai/deepseek-coder-7b-instruct-v1.5) | 568,295 | 156 | 6.91B | coding | text-generation | other | no | conversational |
| [moonshotai/Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct) | 558,146 | 2,366 | 1026B | text | text-generation | other | yes | router, tools, quant, conversational |
| [Qwen/Qwen2.5-Coder-7B-Instruct-GPTQ-Int4](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GPTQ-Int4) | 538,131 | 14 | 7.62B | coding | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-8B-FP8](https://huggingface.co/Qwen/Qwen3-8B-FP8) | 529,460 | 60 | 8.19B | text | text-generation | apache-2.0 | no | quant, conversational |
| [deepseek-ai/DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) | 520,058 | 656 | 14.8B | text | unknown | mit | no | structured |
| [Qwen/Qwen3-VL-32B-Thinking-FP8](https://huggingface.co/Qwen/Qwen3-VL-32B-Thinking-FP8) | 518,996 | 26 | 33.4B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) | 517,849 | 953 | 72.7B | text | text-generation | other | yes | router, tools, conversational |
| [Qwen/Qwen2.5-VL-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) | 517,047 | 629 | 73.4B | multimodal | image-text-to-text | other | yes | router, structured, conversational |
| [stepfun-ai/Step3-VL-10B](https://huggingface.co/stepfun-ai/Step3-VL-10B) | 505,023 | 409 | 10.2B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8) | 475,041 | 260 | 124B | text | text-generation | other | no | quant, conversational |
| [Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4) | 473,018 | 40 | 32.8B | text | text-generation | apache-2.0 | no | quant, conversational |
| [google/gemma-4-31B-it-assistant](https://huggingface.co/google/gemma-4-31B-it-assistant) | 471,079 | 303 | 0.47B | multimodal | any-to-any | apache-2.0 | no |  |
| [nvidia/Llama-3.1-8B-Instruct-FP8](https://huggingface.co/nvidia/Llama-3.1-8B-Instruct-FP8) | 465,050 | 37 | 8.03B | text | text-generation | llama3.1 | no | quant, conversational |
| [Qwen/Qwen3-1.7B-GPTQ-Int8](https://huggingface.co/Qwen/Qwen3-1.7B-GPTQ-Int8) | 462,847 | 7 | 1.72B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-VL-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct) | 461,591 | 490 | 33.5B | multimodal | image-text-to-text | apache-2.0 | no |  |
| [zai-org/chatglm2-6b](https://huggingface.co/zai-org/chatglm2-6b) | 434,074 | 2,057 |  | text | unknown | unknown | no |  |
| [deepseek-ai/DeepSeek-R1-0528-Qwen3-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528-Qwen3-8B) | 432,223 | 1,078 | 8.19B | text | text-generation | mit | no | conversational |
| [Qwen/Qwen3-32B-AWQ](https://huggingface.co/Qwen/Qwen3-32B-AWQ) | 426,384 | 136 | 32.8B | text | text-generation | apache-2.0 | no | quant, conversational |
| [google/gemma-4-12B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf) | 419,627 | 168 | 11.9B | multimodal | any-to-any | apache-2.0 | no | gguf, quant, conversational |
| [deepseek-ai/DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) | 417,533 | 866 | 8.03B | text | text-generation | mit | yes | router, structured, conversational |
| [Qwen/Qwen3-Next-80B-A3B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct-FP8) | 414,354 | 90 | 81.3B | text | text-generation | apache-2.0 | no | quant, conversational |
| [nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16) | 413,017 | 356 | 33.0B | multimodal | any-to-any | other | no |  |
| [nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8) | 409,868 | 349 | 31.6B | text | text-generation | other | no | quant, conversational |
| [nvidia/diffusiongemma-26B-A4B-it-NVFP4](https://huggingface.co/nvidia/diffusiongemma-26B-A4B-it-NVFP4) | 408,588 | 77 | 14.4B | special-architecture | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-30B-A3B-FP8](https://huggingface.co/Qwen/Qwen3-30B-A3B-FP8) | 402,706 | 84 | 30.5B | text | text-generation | apache-2.0 | no | quant |
| [nvidia/Nemotron-Mini-4B-Instruct](https://huggingface.co/nvidia/Nemotron-Mini-4B-Instruct) | 402,203 | 183 |  | text | text-generation | other | no |  |
| [nvidia/MiniMax-M2.7-NVFP4](https://huggingface.co/nvidia/MiniMax-M2.7-NVFP4) | 376,357 | 59 | 116B | text | text-generation | other | no | quant, conversational |
| [google/gemma-3n-E2B-it](https://huggingface.co/google/gemma-3n-E2B-it) | 375,561 | 305 | 5.44B | multimodal | image-text-to-text | gemma | no | conversational |
| [google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it) | 372,239 | 1,396 | 2.61B | text | text-generation | gemma | no | conversational |
| [Qwen/Qwen3.5-27B-GPTQ-Int4](https://huggingface.co/Qwen/Qwen3.5-27B-GPTQ-Int4) | 368,773 | 55 | 27.8B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [google/gemma-4-31B-it-qat-w4a16-ct](https://huggingface.co/google/gemma-4-31B-it-qat-w4a16-ct) | 367,276 | 26 | 33.6B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [deepseek-ai/DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) | 358,198 | 845 | 7.62B | text | text-generation | mit | yes | router, conversational |
| [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it) | 351,821 | 828 | 9.24B | text | text-generation | gemma | no | conversational |
| [Qwen/Qwen3-VL-4B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct-FP8) | 346,897 | 63 | 4.83B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-VL-32B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-VL-32B-Instruct-FP8) | 346,240 | 46 | 33.4B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [zai-org/GLM-4.5-Air](https://huggingface.co/zai-org/GLM-4.5-Air) | 345,152 | 608 | 110B | text | text-generation | mit | yes | router, tools, conversational |
| [nvidia/Llama-4-Scout-17B-16E-Instruct-FP8](https://huggingface.co/nvidia/Llama-4-Scout-17B-16E-Instruct-FP8) | 340,434 | 16 | 109B | text | unknown | other | no | quant |
| [Qwen/Qwen3-Omni-30B-A3B-Thinking](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Thinking) | 338,886 | 307 | 31.7B | multimodal | any-to-any | other | no |  |
| [nvidia/Cosmos-Reason2-8B](https://huggingface.co/nvidia/Cosmos-Reason2-8B) | 337,048 | 193 | 8.77B | multimodal | image-text-to-text | other | no | conversational |
| [Qwen/Qwen3.5-122B-A10B-GPTQ-Int4](https://huggingface.co/Qwen/Qwen3.5-122B-A10B-GPTQ-Int4) | 319,336 | 41 | 125B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-4B-AWQ](https://huggingface.co/Qwen/Qwen3-4B-AWQ) | 311,014 | 29 | 4.02B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-Next-80B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct) | 306,175 | 1,027 | 81.3B | text | text-generation | apache-2.0 | yes | router, tools, conversational |
| [stepfun-ai/Step-3.5-Flash](https://huggingface.co/stepfun-ai/Step-3.5-Flash) | 304,597 | 819 | 199B | text | text-generation | apache-2.0 | yes | router, tools, conversational |
| [nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4) | 300,883 | 195 | 335B | text | text-generation | other | yes | router, tools, structured, quant, conversational |
| [Qwen/Qwen2.5-Coder-7B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-AWQ) | 300,295 | 25 | 7.62B | coding | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-30B-A3B-GPTQ-Int4](https://huggingface.co/Qwen/Qwen3-30B-A3B-GPTQ-Int4) | 299,756 | 52 | 30.5B | text | text-generation | apache-2.0 | no | quant, conversational |
| [moonshotai/Kimi-VL-A3B-Instruct](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct) | 294,858 | 268 | 16.4B | multimodal | image-text-to-text | mit | no | conversational |
| [Qwen/Qwen3-4B-GGUF](https://huggingface.co/Qwen/Qwen3-4B-GGUF) | 291,243 | 106 | 4.02B | text | text-generation | apache-2.0 | no | gguf, conversational |
| [nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8) | 290,915 | 9 | 8.89B | text | text-generation | other | no | quant, conversational |
| [stepfun-ai/Step-3.7-Flash-NVFP4](https://huggingface.co/stepfun-ai/Step-3.7-Flash-NVFP4) | 289,567 | 51 | 104B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-1.5B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF) | 283,467 | 118 | 1.78B | text | text-generation | apache-2.0 | no | gguf, conversational |
| [google/gemma-4-26B-A4B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-26B-A4B-it-qat-q4_0-gguf) | 276,513 | 74 | 25.2B | multimodal | image-text-to-text | apache-2.0 | no | gguf, quant, conversational |
| [Qwen/Qwen3-30B-A3B-Instruct-2507-FP8](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8) | 275,370 | 129 | 30.5B | text | text-generation | apache-2.0 | no | quant, conversational |
| [moonshotai/Kimi-K2.7-Code](https://huggingface.co/moonshotai/Kimi-K2.7-Code) | 274,865 | 893 | 1059B | multimodal | image-text-to-text | other | yes | router, tools, structured, conversational |
| [Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct-GPTQ-Int4) | 269,756 | 24 | 32.8B | coding | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-3B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF) | 267,192 | 139 | 3.40B | text | text-generation | other | no | gguf, conversational |
| [MiniMaxAI/MiniMax-M3-MXFP8](https://huggingface.co/MiniMaxAI/MiniMax-M3-MXFP8) | 265,619 | 38 | 440B | multimodal | image-text-to-text | other | no | quant, conversational |
| [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) | 265,561 | 4,783 | 6.74B | text | text-generation | llama2 | no | conversational |
| [Qwen/Qwen2.5-Coder-32B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct-GGUF) | 247,616 | 207 | 32.8B | coding | text-generation | apache-2.0 | no | gguf, conversational |
| [Qwen/Qwen2.5-7B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-GGUF) | 245,748 | 154 | 7.62B | text | text-generation | apache-2.0 | no | gguf, conversational |
| [deepseek-ai/DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) | 245,343 | 825 | 685B | text | text-generation | mit | yes | router, tools, structured, quant, conversational |
| [Qwen/Qwen3-VL-8B-Thinking](https://huggingface.co/Qwen/Qwen3-VL-8B-Thinking) | 244,698 | 211 | 8.77B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [Qwen/Qwen2.5-VL-72B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct-AWQ) | 244,103 | 72 | 73.7B | multimodal | image-text-to-text | other | no | quant, conversational |
| [deepseek-ai/deepseek-coder-6.7b-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) | 243,846 | 497 | 6.74B | coding | text-generation | other | no | conversational |
| [nvidia/Llama-3_3-Nemotron-Super-49B-v1_5-FP8](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1_5-FP8) | 237,768 | 28 | 49.9B | text | text-generation | other | no | quant, conversational |
| [google/gemma-4-26B-A4B-it-assistant](https://huggingface.co/google/gemma-4-26B-A4B-it-assistant) | 237,467 | 164 | 0.42B | multimodal | any-to-any | apache-2.0 | no |  |
| [Qwen/Qwen2.5-VL-3B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct-AWQ) | 232,167 | 64 | 3.75B | multimodal | image-text-to-text | unknown | no | quant, conversational |
| [google/gemma-4-E4B-it-assistant](https://huggingface.co/google/gemma-4-E4B-it-assistant) | 229,020 | 110 | 0.08B | multimodal | any-to-any | apache-2.0 | no |  |
| [google/gemma-4-31B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-31B-it-qat-q4_0-gguf) | 228,918 | 76 | 30.7B | multimodal | image-text-to-text | apache-2.0 | no | gguf, quant, conversational |
| [google/gemma-4-E4B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-E4B-it-qat-q4_0-gguf) | 226,487 | 63 | 7.46B | multimodal | any-to-any | apache-2.0 | no | gguf, quant, conversational |
| [allenai/Olmo-3-7B-Instruct-SFT](https://huggingface.co/allenai/Olmo-3-7B-Instruct-SFT) | 223,882 | 4 | 7.30B | text | text-generation | apache-2.0 | no | conversational |
| [nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) | 220,463 | 138 | 8.89B | text | text-generation | other | no | conversational |
| [Qwen/Qwen2.5-0.5B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF) | 219,454 | 104 | 0.63B | text | text-generation | apache-2.0 | no | gguf, conversational |
| [google/gemma-4-E2B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-E2B-it-qat-q4_0-gguf) | 219,161 | 50 | 4.63B | multimodal | any-to-any | apache-2.0 | no | gguf, quant, conversational |
| [nvidia/Llama-3.1-8B-Instruct-NVFP4](https://huggingface.co/nvidia/Llama-3.1-8B-Instruct-NVFP4) | 216,612 | 11 | 4.54B | text | unknown | other | no | quant |
| [meta-llama/Llama-3.1-405B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct) | 213,266 | 596 | 406B | text | text-generation | llama3.1 | no | conversational |
| [Qwen/Qwen2.5-3B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-AWQ) | 210,389 | 16 | 3.40B | text | text-generation | other | no | quant, conversational |
| [Qwen/Qwen3-14B-FP8](https://huggingface.co/Qwen/Qwen3-14B-FP8) | 206,991 | 48 | 14.8B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen3-235B-A22B-Instruct-2507-FP8](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507-FP8) | 206,192 | 147 | 235B | text | text-generation | apache-2.0 | no | quant, conversational |
| [Qwen/Qwen2.5-Coder-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct) | 204,984 | 114 | 3.09B | coding | text-generation | other | yes | router, structured, conversational |
| [Qwen/Qwen3-30B-A3B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507) | 202,569 | 379 | 30.5B | text | text-generation | apache-2.0 | no | conversational |
| [MiniMaxAI/MiniMax-VL-01](https://huggingface.co/MiniMaxAI/MiniMax-VL-01) | 196,972 | 285 | 456B | multimodal | image-text-to-text | unknown | no | conversational |
| [deepseek-ai/DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) | 196,115 | 990 | 685B | text | text-generation | mit | yes | router, tools, structured, quant, conversational |
| [zai-org/GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) | 191,448 | 1,402 | 358B | text | text-generation | mit | yes | router, tools, conversational |
| [inclusionAI/LLaDA2.0-mini](https://huggingface.co/inclusionAI/LLaDA2.0-mini) | 187,502 | 67 | 16.3B | special-architecture | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen3-VL-235B-A22B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct-FP8) | 184,937 | 44 | 236B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [CohereLabs/aya-vision-8b](https://huggingface.co/CohereLabs/aya-vision-8b) | 184,027 | 322 | 8.63B | multimodal | image-text-to-text | cc-by-nc-4.0 | no | conversational |
| [Qwen/Qwen3-4B-Thinking-2507-FP8](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507-FP8) | 180,359 | 66 | 4.41B | text | text-generation | apache-2.0 | no | quant, conversational |
| [google/gemma-1.1-2b-it](https://huggingface.co/google/gemma-1.1-2b-it) | 179,442 | 173 | 2.51B | text | text-generation | gemma | no | conversational |
| [nvidia/Llama-3_3-Nemotron-Super-49B-v1](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1) | 168,389 | 322 | 49.9B | text | text-generation | other | no | conversational |
| [nvidia/DeepSeek-V4-Flash-NVFP4](https://huggingface.co/nvidia/DeepSeek-V4-Flash-NVFP4) | 163,227 | 29 | 167B | text | text-generation | mit | no | quant |
| [moonshotai/Kimi-K2-Thinking](https://huggingface.co/moonshotai/Kimi-K2-Thinking) | 159,056 | 1,704 | 1058B | text | text-generation | other | yes | router, conversational |
| [stepfun-ai/step3](https://huggingface.co/stepfun-ai/step3) | 158,805 | 166 | 321B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [nvidia/Qwen3-32B-NVFP4](https://huggingface.co/nvidia/Qwen3-32B-NVFP4) | 154,431 | 17 | 17.2B | text | text-generation | apache-2.0 | no | quant, conversational |
| [allenai/Molmo2-O-7B](https://huggingface.co/allenai/Molmo2-O-7B) | 154,278 | 26 | 7.76B | multimodal | image-text-to-text | apache-2.0 | no | conversational |
| [inclusionAI/LLaDA2.1-flash](https://huggingface.co/inclusionAI/LLaDA2.1-flash) | 151,310 | 92 | 103B | special-architecture | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen2.5-Coder-7B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF) | 150,855 | 278 | 7.62B | coding | text-generation | apache-2.0 | no | gguf, conversational |
| [nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16) | 150,454 | 84 | 13.2B | multimodal | image-text-to-text | other | no | conversational |
| [allenai/Olmo-3-7B-Instruct](https://huggingface.co/allenai/Olmo-3-7B-Instruct) | 146,568 | 133 | 0.00B | text | text-generation | apache-2.0 | yes | router, tools, conversational |
| [Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8) | 145,883 | 155 | 480B | coding | text-generation | apache-2.0 | no | quant, conversational |
| [google/gemma-4-31B-it-qat-q4_0-unquantized-assistant](https://huggingface.co/google/gemma-4-31B-it-qat-q4_0-unquantized-assistant) | 140,082 | 16 | 0.47B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [moonshotai/Kimi-VL-A3B-Thinking](https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking) | 138,997 | 448 | 16.4B | multimodal | image-text-to-text | mit | no | conversational |
| [google/gemma-3-270m-it](https://huggingface.co/google/gemma-3-270m-it) | 136,282 | 595 | 0.27B | text | text-generation | gemma | no |  |
| [MiniMaxAI/MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2) | 132,741 | 1,500 | 229B | text | text-generation | other | yes | router, tools, quant, conversational |
| [Qwen/Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) | 131,607 | 782 | 235B | text | text-generation | apache-2.0 | yes | router, tools, structured, conversational |
| [nvidia/DeepSeek-V4-Pro-NVFP4](https://huggingface.co/nvidia/DeepSeek-V4-Pro-NVFP4) | 129,800 | 62 | 910B | text | text-generation | mit | no | quant |
| [google/gemma-2-27b-it](https://huggingface.co/google/gemma-2-27b-it) | 129,291 | 568 | 27.2B | text | text-generation | gemma | no | conversational |
| [zai-org/GLM-4.5V](https://huggingface.co/zai-org/GLM-4.5V) | 127,115 | 719 | 108B | multimodal | image-text-to-text | mit | yes | router, tools, conversational |
| [swiss-ai/Apertus-8B-Instruct-2509](https://huggingface.co/swiss-ai/Apertus-8B-Instruct-2509) | 124,737 | 463 | 8.05B | text | text-generation | apache-2.0 | yes | router, structured, conversational |
| [zai-org/chatglm3-6b](https://huggingface.co/zai-org/chatglm3-6b) | 122,126 | 1,163 | 6.24B | text | unknown | unknown | no |  |
| [nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) | 119,506 | 226 | 561B | text | text-generation | other | yes | router, tools, structured, conversational |
| [meta-llama/Llama-2-13b-chat-hf](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf) | 117,914 | 1,117 | 13.0B | text | text-generation | llama2 | no | conversational |
| [meta-llama/Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) | 116,381 | 1,605 | 10.7B | multimodal | image-text-to-text | llama3.2 | no | conversational |
| [zai-org/GLM-5.1](https://huggingface.co/zai-org/GLM-5.1) | 115,778 | 1,805 | 754B | text | text-generation | mit | yes | router, tools, structured, conversational |
| [Qwen/Qwen3-32B-FP8](https://huggingface.co/Qwen/Qwen3-32B-FP8) | 113,344 | 83 | 32.8B | text | text-generation | apache-2.0 | no | quant, conversational |
| [nvidia/Qwen3-14B-NVFP4](https://huggingface.co/nvidia/Qwen3-14B-NVFP4) | 112,543 | 12 | 8.16B | text | text-generation | apache-2.0 | no | quant, conversational |
| [utter-project/EuroLLM-22B-Instruct-2512](https://huggingface.co/utter-project/EuroLLM-22B-Instruct-2512) | 110,408 | 71 | 22.6B | text | text-generation | apache-2.0 | yes | router, conversational |
| [Qwen/Qwen2.5-Coder-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-0.5B-Instruct) | 110,041 | 69 | 0.49B | coding | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen3-VL-30B-A3B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Instruct-FP8) | 109,858 | 111 | 31.1B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |
| [allenai/OLMoE-1B-7B-0125-Instruct](https://huggingface.co/allenai/OLMoE-1B-7B-0125-Instruct) | 109,153 | 65 | 6.92B | text | text-generation | apache-2.0 | no | conversational |
| [Qwen/Qwen-VL-Chat](https://huggingface.co/Qwen/Qwen-VL-Chat) | 107,790 | 384 |  | multimodal | text-generation | unknown | no |  |
| [deepseek-ai/DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B) | 103,526 | 780 | 70.6B | text | text-generation | mit | yes | router, tools, structured, conversational |
| [nvidia/GLM-5.1-NVFP4](https://huggingface.co/nvidia/GLM-5.1-NVFP4) | 102,554 | 36 | 382B | text | text-generation | mit | no | quant, conversational |
| [Qwen/Qwen2.5-14B-Instruct-GPTQ-Int4](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-GPTQ-Int4) | 101,858 | 26 | 14.8B | text | text-generation | apache-2.0 | no | quant, conversational |
| [nvidia/NVIDIA-Nemotron-Nano-12B-v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2) | 100,328 | 165 | 12.3B | text | text-generation | other | no | conversational |
| [Qwen/Qwen3-VL-2B-Instruct-FP8](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct-FP8) | 100,278 | 41 | 2.44B | multimodal | image-text-to-text | apache-2.0 | no | quant, conversational |

### Excluded Summary

Excluded rows are kept in the manual curation file but omitted from the candidate table.

Excluded by pipeline:

- `text-generation`: 38
- `image-text-to-text`: 29
- `unknown`: 27
- `automatic-speech-recognition`: 16
- `zero-shot-image-classification`: 15
- `any-to-any`: 6
- `text-ranking`: 6
- `feature-extraction`: 5
- `text-to-speech`: 4
- `sentence-similarity`: 4
- `image-segmentation`: 4
- `audio-to-audio`: 3

Top excluded creator namespaces:

- `google`: 54
- `Qwen`: 52
- `nvidia`: 28
- `openai`: 11
- `meta-llama`: 10
- `allenai`: 9
- `deepseek-ai`: 4
- `zai-org`: 2
- `baidu`: 2
- `stepfun-ai`: 2
- `CohereLabs`: 1
- `EssentialAI`: 1

## Regeneration

```bash
python3 open-model-benchmarking/scripts/generate_report.py
```
