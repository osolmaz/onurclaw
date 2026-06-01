# OPENCLAW ONUR INVENTORY

Updated: 2026-06-01

Review watermark:

- Last reviewed through issue: #89087.
- Last reviewed through PR: #89086.
- Meaning: all GitHub issues and PRs at or below these numbers were considered for local-model and open-weight relevance; later numbers need review on the next run.

This is the curated issue/PR list after an item-by-item audit of the previous broad inventory. The broad 331-issue file was over-inclusive: it kept many rows where a local/open-weight term appeared incidentally in the archived body. This version keeps threads where the actual reported problem or PR change is materially about local models, self-hosted/open-weight serving, OpenAI-compatible/proxy behavior, local embeddings/QMD/GGUF/MLX, model routing/fallback, or specific open-weight model families.

Sources checked:

- Gitcrawl archive synced on 2026-05-26 with 10,352 threads and 6,961 open threads.
- Live GitHub issue list fetched on 2026-05-26 with 3,784 open issues.
- Live GitHub PR list fetched on 2026-05-26 with 3,086 open PRs.
- Incremental local gitcrawl/notifier checks on 2026-05-29 covered local DB through issue #88047 and PR #88052; 20 newer local DB threads above the previous watermark were reviewed and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-30 covered local DB through issue #88087 and PR #88086; 33 newer local DB threads above the previous watermark were reviewed and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-30 covered local DB through issue #88111 and PR #88118; 27 newer local DB threads above the previous watermark were reviewed and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-30 covered local DB through issue #88128 and PR #88137; 14 newer local DB threads above the previous watermark were reviewed, with live state checked only for newly relevant rows, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-31 covered local DB through issue #88457 and PR #88459; 282 newer local DB threads above the previous watermark were reviewed, with no broad network refresh run.
- Incremental local gitcrawl/notifier checks on 2026-05-31 covered local DB through issue #88490 and PR #88487; 27 newer local DB threads above the previous watermark were reviewed, with no broad network refresh run.
- Incremental local gitcrawl/notifier checks on 2026-05-31 covered local DB through issue #88502 and PR #88503; 12 newer local DB threads above the previous watermark were reviewed, one new direct OpenAI-compatible issue was retained, closed local DB rows were moved out of the open tables, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-31 covered local DB through issue #88517 and PR #88518; 12 newer local DB threads above the previous watermark were reviewed, 6 materially relevant model-routing/local-runtime rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-31 covered local DB through issue #88528 and PR #88536; 17 newer local DB threads above the previous watermark were reviewed, one new DeepSeek provider usage PR was retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-31 covered local DB through issue #88568 and PR #88564; 27 newer local DB threads above the previous watermark were reviewed, 10 materially relevant model-routing/OpenAI-compatible rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-31 covered local DB through issue #88586 and PR #88589; 19 newer local DB threads above the previous watermark were reviewed, 2 materially relevant model-routing/provider-auth rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-31 covered local DB through issue #88616 and PR #88625; 25 newer local DB threads above the previous watermark were reviewed, 5 materially relevant model-routing/provider-auth/local-embedding rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-05-31 covered local DB through issue #88671 and PR #88667; 36 newer local DB threads above the previous watermark were reviewed, 8 materially relevant local-runtime/model-routing/open-weight rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #88712 and PR #88716; 44 newer local DB threads above the previous watermark were reviewed, 13 materially relevant local-memory/model-routing/OpenAI-compatible rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #88741 and PR #88746; 24 newer local DB threads above the previous watermark were reviewed, 5 materially relevant local-runtime/model-routing/open-weight rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #88788 and PR #88787; 35 newer local DB threads above the previous watermark were reviewed, 11 materially relevant model-routing/OpenAI-compatible/open-weight rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #88811 and PR #88804; 18 newer local DB threads above the previous watermark were reviewed, 5 materially relevant local-runtime/model-routing/OpenAI-compatible rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #88844 and PR #88842; 33 newer local DB threads above the previous watermark were reviewed, 7 materially relevant local-memory/local-runtime/model-routing/OpenAI-compatible rows were retained, closed local DB rows were moved out of the open tables, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #88874 and PR #88881; 31 newer local DB threads above the previous watermark were reviewed, 10 materially relevant local-memory/full-local/model-routing/OpenAI-compatible/open-weight rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #88918 and PR #88923; 40 newer local DB threads above the previous watermark were reviewed, 13 materially relevant local-memory/local-runtime/model-routing/OpenAI-compatible/open-weight rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #88967 and PR #88963; 35 newer local DB threads above the previous watermark were reviewed, 11 materially relevant local-runtime/model-routing/OpenAI-compatible/open-weight rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #89009 and PR #89014; 39 newer local DB threads above the previous watermark were reviewed, 8 materially relevant local-runtime/model-routing/OpenAI-compatible/open-weight rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #89054 and PR #89055; 37 newer local DB threads above the previous watermark were reviewed, 8 materially relevant local-runtime/model-routing/OpenAI-compatible/open-weight rows were retained, and no broad network refresh was run.
- Incremental local gitcrawl/notifier checks on 2026-06-01 covered local DB through issue #89087 and PR #89086; 29 newer local DB threads above the previous watermark were reviewed, 2 materially relevant local-runtime/model-routing rows were retained, and no broad network refresh was run.
- Prior broad issue inventory audited: 331 live-open rows.
- Raw local/open-weight candidate search: 1,446 open issue matches and 1,184 open PR matches.

Audit result:

- Kept open issues: 247.
- Kept open PRs: 204.
- Removed from the previous broad issue table: 152 rows whose local/open-weight evidence was incidental or too generic.
- Kept items can still vary in priority; inclusion here means related, not necessarily urgent.

Inclusion criteria used:

- Keep: direct local model/runtime failures such as Ollama, LM Studio, vLLM, llama.cpp, GGUF, MLX, or local one-shot infer behavior.
- Keep: OpenAI-compatible, OpenAI completions/responses, LiteLLM, Open-WebUI, proxy, or custom-provider behavior that affects self-hosted/open-weight routing.
- Keep: local embedding, QMD, memory embedding, reranker, vector/FTS, or model-aware memory issues.
- Keep: model routing, fallback, picker, auth-profile, catalog, or actual-model reporting when it affects model/provider correctness.
- Keep: model-family-specific failures for Kimi, Qwen, DeepSeek, Moonshot, GLM/Z.ai, Gemma, Mistral, MiMo/Xiaomi, Nemotron, and similar open-weight/provider paths.
- Drop: generic channel, UI, gateway, Discord/Telegram, cron, memory, bootstrap, docs, or install issues where the only evidence is an incidental provider/model name in the body.

## HIGHEST-RISK OPEN AREAS

1. Local runtime stalls and gateway blocking: #89070, #89051, #89049, #89040, #88999, #88918, #88907, #88890, #88884, #88882, #88881, #88873, #88822, #88789, #88771, #88746, #88705, #88671, #88645, #88632, #88514, #88460, #88457, #88439, #88381, #88366, #88212, #88201, #88181, #87955, #87940, #87856, #87850, #87818, #87768, #87756, #87687, #87642, #87619, #87617, #87616, #87587, #87586, #87558, #87414, #87285, #87262, #86599, #85826, #63229, #54155.
2. OpenAI-compatible/proxy correctness: #89039, #89032, #89016, #89013, #89001, #88964, #88918, #88917, #88893, #88861, #88833, #88804, #88799, #88791, #88787, #88769, #88512, #88499, #88480, #88267, #88098, #88071, #88068, #87996, #87933, #87763, #87737, #87325, #84697, #84575, #79897, #66125.
3. Open-weight tool/reasoning parsing: #89070, #89032, #88999, #88976, #88918, #88907, #88869, #88868, #88769, #88754, #88741, #88671, #88657, #88645, #88457, #88378, #88320, #88289, #88079, #87943, #87766, #87596, #85918, #85321, #85192, #71491, #71273, #51593.
4. Local embeddings/QMD reliability: #88905, #88887, #88873, #88864, #88830, #88806, #88705, #88704, #88696, #88615, #88263, #88238, #88078, #88077, #88009, #87907, #87881, #87854, #87689, #87572, #87443, #85382, #83333, #77645, #74204, #72015, #59808, #57996.
5. Provider routing and model fallback: #89087, #89049, #89039, #89029, #89027, #89016, #89008, #88994, #88977, #88922, #88917, #88907, #88906, #88902, #88896, #88880, #88878, #88874, #88869, #88851, #88837, #88827, #88816, #88800, #88787, #88767, #88748, #88723, #88709, #88707, #88679, #88630, #88616, #88608, #88596, #88579, #88562, #88561, #88553, #88551, #88548, #88512, #88506, #88490, #88482, #88480, #88470, #88468, #88400, #88357, #88351, #88329, #88249, #88241, #88125, #88108, #88082, #88049, #88039, #87958, #87957, #87932, #87927, #87925, #87923, #87895, #87893, #87876, #87801, #87752, #87746, #87740, #87697, #87694, #87628, #87603, #87538, #87484, #87480, #87467, #87462, #87407, #87404, #87381, #87343, #87318, #87277, #85126, #84865.

## OPEN ISSUES (247)

| Issue | Activity | Area | Title |
| --- | --- | --- | --- |
| [#89087](https://github.com/openclaw/openclaw/issues/89087) | 0 | Model routing/config | Bug: Session model override lost on UTC midnight rollover |
| [#89051](https://github.com/openclaw/openclaw/issues/89051) | 0 | Local model runtime | [Bug]: Embedded agent session silently hangs after auto-compaction with no error logging or recovery |
| [#89032](https://github.com/openclaw/openclaw/issues/89032) | 0 | Open-weight/provider behavior | MiMo v2.5: reasoning_content not preserved for custom xiaomi-coding provider (400 in multi-turn tool calls) |
| [#89008](https://github.com/openclaw/openclaw/issues/89008) | 0 | Model routing/config | claude-cli thinking-only (end_turn, empty text) turns trigger empty_response model-fallback re-run on a different model |
| [#88938](https://github.com/openclaw/openclaw/issues/88938) | 0 | Local/media model provider | [Feature]: know what model is used by the image tool |
| [#88918](https://github.com/openclaw/openclaw/issues/88918) | 0 | OpenAI-compatible/proxy | [Bug]: Streaming repairJson injects control chars into unescaped Windows paths in tool-call arguments |
| [#88907](https://github.com/openclaw/openclaw/issues/88907) | 0 | Open-weight/provider behavior | Chronic agent failures on Telegram - LLM timeouts before configured timeout + silent incomplete turns + dead fallbacks (OpenRouter/DeepSeek+V4-Flash, v2026.5.28) |
| [#88902](https://github.com/openclaw/openclaw/issues/88902) | 0 | Model routing/config | [Bug]: Codex OAuth /btw still falls back to OpenAI Responses after /new |
| [#88874](https://github.com/openclaw/openclaw/issues/88874) | 0 | Model routing/config | [Bug]: cron openai/gpt-5.4-mini ignores agentRuntime=openclaw/pi and routes to openai-codex with zero tools |
| [#88868](https://github.com/openclaw/openclaw/issues/88868) | 0 | Open-weight/provider behavior | Add MiniMax M3 support to the bundled MiniMax provider |
| [#88864](https://github.com/openclaw/openclaw/issues/88864) | 0 | Local memory/embedding | [Bug]: `memory-wiki` bridge imports all workspace artifacts into shared vault, causing `path-mismatch` error |
| [#88833](https://github.com/openclaw/openclaw/issues/88833) | 0 | OpenAI-compatible/proxy | Bug: azure-openai-responses can return non_deliverable_terminal_turn with assistantTexts=[] even when direct Azure /responses succeeds |
| [#88816](https://github.com/openclaw/openclaw/issues/88816) | 0 | Model routing/config | [Bug]: v2026.05.28 breaks Google Vertex Express API Key |
| [#88791](https://github.com/openclaw/openclaw/issues/88791) | 0 | OpenAI-compatible/proxy | Bug: structured tool_calls with finish_reason stop are dropped as non_deliverable_terminal_turn |
| [#88741](https://github.com/openclaw/openclaw/issues/88741) | 0 | Open-weight/provider behavior | Stream parser duplicates <think> content into both text and thinking parts (CoT leaks to chat channels with minimax/MiniMax-M2.7) |
| [#88707](https://github.com/openclaw/openclaw/issues/88707) | 0 | Model routing/config | [Bug] Regression 2026.5.27→2026.5.28: "No API provider registered for api: bedrock-converse-stream" — pi-ai removal breaks Bedrock provider registration; bearer token auth broken |
| [#88705](https://github.com/openclaw/openclaw/issues/88705) | 0 | Local memory/embedding | Bug: npm updates drop node-llama-cpp, breaking local memory_search after every OpenClaw update |
| [#88679](https://github.com/openclaw/openclaw/issues/88679) | 0 | Model routing/config | [Feature]: Per-Tool Model Routing — route specific tool calls to different models |
| [#88671](https://github.com/openclaw/openclaw/issues/88671) | 0 | Local model runtime | [Bug]: [assistant reasoning omitted] appears with reasoningDefault off on Ollama models |
| [#88657](https://github.com/openclaw/openclaw/issues/88657) | 0 | Open-weight/provider behavior | Bug: DeepSeek V4 Flash incomplete turn (payloads=0, tools=2, replaySafe=no, stopReason=stop) in 2026.5.27/28 |
| [#88632](https://github.com/openclaw/openclaw/issues/88632) | 0 | Local model runtime | [Bug]: gateway model-run sessions accumulate until session maxEntries cap |
| [#88616](https://github.com/openclaw/openclaw/issues/88616) | 0 | Model routing/config | [Feature]: Forward session_id to OpenRouter for sticky routing & prompt caching |
| [#88615](https://github.com/openclaw/openclaw/issues/88615) | 0 | Local memory/embedding | [Bug]: sqlite-vec fails to load on Node 22 Linux x64 (Vector store: unknown, distinct from #64776 and #65033) |
| [#88596](https://github.com/openclaw/openclaw/issues/88596) | 0 | Model routing/config | xAI models report incorrect context window (200k instead of 1M) — long_context_threshold misinterpreted |
| [#88579](https://github.com/openclaw/openclaw/issues/88579) | 0 | Model routing/config | LLM error: Authorization Not Found - SecretRef apiKey not properly resolved in Gateway |
| [#88562](https://github.com/openclaw/openclaw/issues/88562) | 0 | Model routing/config | [Bug]: models.json generator writes apiKey as plain string instead of secret-ref object |
| [#88561](https://github.com/openclaw/openclaw/issues/88561) | 0 | Model routing/config | lossless-claw compaction breaks tool_calls/tool message chain -> 499 error on model switch |
| [#88548](https://github.com/openclaw/openclaw/issues/88548) | 0 | Model routing/config | GitHub Copilot: static default model list shadows live entitlement discovery |
| [#88499](https://github.com/openclaw/openclaw/issues/88499) | 0 | OpenAI-compatible/proxy | openai-responses provider: 404 on previous_response_id when store=false (default) |
| [#88490](https://github.com/openclaw/openclaw/issues/88490) | 0 | Model routing/config | Session model override from Codex persists in unrelated sessions (e.g. Telegram) |
| [#88480](https://github.com/openclaw/openclaw/issues/88480) | 0 | Model routing/config | Google Gemini chat model routes to openai-responses transport (401), native @google/genai transport never selected |
| [#88470](https://github.com/openclaw/openclaw/issues/88470) | 0 | Model routing/config | [Bug]: Title: OpenAI GPT-5.5 fails through Codex runtime after upgrade to OpenClaw 2026.5.28 |
| [#88457](https://github.com/openclaw/openclaw/issues/88457) | 0 | Open-weight/provider behavior | [Bug]: opencode-go works via direct infer but fails in embedded agent runtime with session takeover |
| [#88439](https://github.com/openclaw/openclaw/issues/88439) | 0 | Local model runtime | [Bug]: cron tool: local llamacpp model parameter serialization corrupts JSON property names (key concatenation) |
| [#88357](https://github.com/openclaw/openclaw/issues/88357) | 0 | Model routing/config | Bug: apply_patch unavailable on non-OpenAI providers due to hardcoded isOpenAIProvider gate |
| [#88267](https://github.com/openclaw/openclaw/issues/88267) | 0 | OpenAI-compatible/proxy | [Bug]: Ollama model added in config is not recognized by runtime after restart |
| [#88201](https://github.com/openclaw/openclaw/issues/88201) | 0 | Local model runtime | [Bug]: OpenClaw 5.22: ~10 sec per-call inference overhead in infer model run (both --gateway and --local) vs ~1.3 sec direct provider call |
| [#88125](https://github.com/openclaw/openclaw/issues/88125) | 0 | Model routing/config | [Docs] Clarify auth profile provider field after openai-codex OAuth login |
| [#88079](https://github.com/openclaw/openclaw/issues/88079) | 0 | Open-weight/provider behavior | [Regression] WebChat: reasoning_content not streamed for Kimi Code & DeepSeek Reasoner — only MiniMax works |
| [#88077](https://github.com/openclaw/openclaw/issues/88077) | 0 | Local memory/embedding | [Bug]: Active Memory recall context uses full OpenClaw prompt envelope |
| [#88068](https://github.com/openclaw/openclaw/issues/88068) | 0 | OpenAI-compatible/proxy | [Bug]: No config key to override dropReasoningFromHistory for openai-completions providers |
| [#88039](https://github.com/openclaw/openclaw/issues/88039) | 0 | Model routing/config | [Bug]: Session-selected model incorrectly included in fallback list in v2026.5.26 |
| [#88009](https://github.com/openclaw/openclaw/issues/88009) | 0 | Local memory/embedding | [Feature]: batched memory embedding should batch over files |
| [#87996](https://github.com/openclaw/openclaw/issues/87996) | 0 | OpenAI-compatible/proxy | Vertex beta INVALID_ARGUMENT can wedge long Enterprise sessions without actionable recovery |
| [#87957](https://github.com/openclaw/openclaw/issues/87957) | 0 | Model routing/config | Refactor session model/auth state resolution |
| [#87943](https://github.com/openclaw/openclaw/issues/87943) | 0 | Open-weight/provider behavior | feat: Add Xiaomi MiMo Web Search provider |
| [#87925](https://github.com/openclaw/openclaw/issues/87925) | 0 | Model routing/config | thinkingLevel: model switch silently downgrades and persists an inherited explicit override |
| [#87881](https://github.com/openclaw/openclaw/issues/87881) | 0 | Local memory/embedding | Gap Analysis: v2026.5.27 config keys rejected as unknown by schema |
| [#87876](https://github.com/openclaw/openclaw/issues/87876) | 0 | Model routing/config | Bug: Bedrock Converse Streaming silently aborts on long-context agent sessions (~6 min timeout, no retry, no fallback) |
| [#87854](https://github.com/openclaw/openclaw/issues/87854) | 0 | Local memory/embedding | Memory Dreaming Promotion: candidates found but applied=0 (rehydratePromotionCandidate returns null for all) |
| [#87816](https://github.com/openclaw/openclaw/issues/87816) | 0 | Local/media model provider | feat(tts): xiaomi voicedesign/voiceclone model support |
| [#87801](https://github.com/openclaw/openclaw/issues/87801) | 4 | Model routing/config | supportsAdaptiveThinking() omits opus-4-8 -> reasoning-enabled requests send thinking.type.enabled -> 400 + silent fallback |
| [#87768](https://github.com/openclaw/openclaw/issues/87768) | 0 | Local model runtime | [Bug]: push to talk mac os companion app hard codes thinking low |
| [#87766](https://github.com/openclaw/openclaw/issues/87766) | 0 | Open-weight/provider behavior | [Bug] Kimi web_search always returns "ungrounded" error - Moonshot API no longer returns search_results field[Bug]: |
| [#87763](https://github.com/openclaw/openclaw/issues/87763) | 0 | OpenAI-compatible/proxy | SSRF guard pinned DNS dispatcher causes model fetch timeouts when autoSelectFamily is enabled |
| [#87756](https://github.com/openclaw/openclaw/issues/87756) | 4 | Local model runtime | [Bug]: Regression: prompt-launched Lobster workflow hangs on nested /tools/invoke, while curl-launched workflow works |
| [#87752](https://github.com/openclaw/openclaw/issues/87752) | 4 | Model routing/config | [Bug]: Failover selects unconfigured model MiniMax-M2.7-highspeed causing complete session failure |
| [#87746](https://github.com/openclaw/openclaw/issues/87746) | 2 | Model routing/config | Add Claude Opus 4.8 (`claude-opus-4-8`) to the model catalog |
| [#87740](https://github.com/openclaw/openclaw/issues/87740) | 0 | Model routing/config | Bug: Explicit thinkingLevel session override permanently reset to 'off' after each agent turn |
| [#87737](https://github.com/openclaw/openclaw/issues/87737) | 4 | OpenAI-compatible/proxy | DeepSeek V4 thinking wrapper ignores thinkingFormat compat override, breaks Azure Foundry deployments |
| [#87689](https://github.com/openclaw/openclaw/issues/87689) | 0 | Local memory/embedding | Dreaming needs supported guard to disable session transcript ingestion during QMD migrations |
| [#87687](https://github.com/openclaw/openclaw/issues/87687) | 0 | Local model runtime | vllm openai-completions streaming parser drops tool_calls when reasoning_content streams first for gpt-oss-120b at large systemPrompt |
| [#87642](https://github.com/openclaw/openclaw/issues/87642) | 0 | Local model runtime | Expose subagent-control waitForRun timeout as a config knob (hardcoded 30s blocks slow local LLMs) |
| [#87616](https://github.com/openclaw/openclaw/issues/87616) | 8 | Local model runtime | [Bug]: GatewayClientRequestError: FailoverError: LLM request timed out. |
| [#87603](https://github.com/openclaw/openclaw/issues/87603) | 0 | Model routing/config | lossless-claw contextThreshold does not adapt to actual model context window after fallback |
| [#87586](https://github.com/openclaw/openclaw/issues/87586) | 0 | Local model runtime | [Feature]: Unixsocket Provider plugin |
| [#87467](https://github.com/openclaw/openclaw/issues/87467) | 4 | Model routing/config | [Bug]: Auto rate-limit fallback override still pins Discord session to fallback after primary recovers |
| [#87466](https://github.com/openclaw/openclaw/issues/87466) | 0 | Local/media model provider | [Bug]:Telegram voice delivery is unstable across model runtimes because voice generation depends on model-generated media tags |
| [#87462](https://github.com/openclaw/openclaw/issues/87462) | 4 | Model routing/config | [Bug]: Auth profile cooldown triggers chain exhaustion without actual Google API errors in v2026.5.26 |
| [#87443](https://github.com/openclaw/openclaw/issues/87443) | 0 | Local memory/embedding | sqlite-vec vector search fails on musl-based systems |
| [#87407](https://github.com/openclaw/openclaw/issues/87407) | 4 | Model routing/config | [Bug]: Anthropic provider: UND_ERR_SOCKET keep-alive failures trigger silent mid-turn fallback to OpenAI/Codex |
| [#87384](https://github.com/openclaw/openclaw/issues/87384) | 0 | Local/media model provider | Bug: CLI audio transcription can use progress stdout when transcript file is empty |
| [#87381](https://github.com/openclaw/openclaw/issues/87381) | 11 | Model routing/config | ACP runtime ignores per-agent model.primary override |
| [#87325](https://github.com/openclaw/openclaw/issues/87325) | 4 | OpenAI-compatible/proxy | Support Azure Foundry GPT Realtime Talk via gateway relay |
| [#87318](https://github.com/openclaw/openclaw/issues/87318) | 4 | Model routing/config | amazon-bedrock provider: Haiku 4.5 inference profile ARN not supported; params.modelId override ignored |
| [#87285](https://github.com/openclaw/openclaw/issues/87285) | 4 | Local model runtime | Gateway frequent restarts: config reload too aggressive + auth pre-warm blocks event loop |
| [#87277](https://github.com/openclaw/openclaw/issues/87277) | 0 | Open-weight/provider behavior | [Feature] Add MiMo-V2.5 to Xiaomi catalog + automatic multimodal routing when DeepSeek V4-Pro is primary model |
| [#87267](https://github.com/openclaw/openclaw/issues/87267) | 0 | Local model runtime | [Bug]: Dream Diary narrative needs separate config for timeout/concurrency or disablement, while keeping dreaming enabled. |
| [#87262](https://github.com/openclaw/openclaw/issues/87262) | 0 | Local model runtime | [Bug]: qqbot + ollama + local model: qwen3.5:27b report: error Embedded agent failed before reply: LLM request failed: network connection was interrupted |
| [#87170](https://github.com/openclaw/openclaw/issues/87170) | 4 | Model routing/config | Agent always returns "Provider returned error" with auto model after gateway restart |
| [#87168](https://github.com/openclaw/openclaw/issues/87168) | 0 | Model routing/config | `image` media-understanding tool can bypass configured Codex image route via model overrides and direct OpenAI auto-selection |
| [#87140](https://github.com/openclaw/openclaw/issues/87140) | 4 | Local/media model provider | [Feature]: Pluggable STT backend for macOS Push-to-Talk |
| [#87110](https://github.com/openclaw/openclaw/issues/87110) | 0 | Local model runtime | When calling a VLLM model, the usage page statistics show no data. How can I calculate usage and cost when using VLLM? |
| [#86880](https://github.com/openclaw/openclaw/issues/86880) | 4 | Open-weight/provider behavior | [Bug]: Context Overflow Bug With OpenRouter Models (Latest Version 2026.05.22) |
| [#86868](https://github.com/openclaw/openclaw/issues/86868) | 4 | Model routing/config | Embedded runtime: model fallback chain breaks at intermediate candidates instead of walking to the last entry |
| [#86813](https://github.com/openclaw/openclaw/issues/86813) | 0 | Model routing/config | `/new` does not clear persisted model override in channel-bound sessions |
| [#86773](https://github.com/openclaw/openclaw/issues/86773) | 0 | Local model runtime | Provider auth prewarm can starve gateway event loop and cause sessions.list timeouts after restart |
| [#86752](https://github.com/openclaw/openclaw/issues/86752) | 0 | Local model runtime | [Bug]: 2026.5.22 Docker/WSL2 gateway event-loop starvation, 284s provider-auth prewarm, slow Telegram turn, and local RPC timeouts |
| [#86632](https://github.com/openclaw/openclaw/issues/86632) | 4 | Local model runtime | OpenClaw local embedded Ollama/Qwen session fails live-data request that Pi coding agent handles via shell/curl |
| [#86599](https://github.com/openclaw/openclaw/issues/86599) | 23 | Local memory/embedding | [Bug]: Local model provider calls thread block gateway event loop on Windows beta; trivial infer run takes ~4 minutes |
| [#86521](https://github.com/openclaw/openclaw/issues/86521) | 0 | OpenAI-compatible/proxy | fix: preserve reasoning_content for DeepSeek models through proxy providers (opencode-native) |
| [#86182](https://github.com/openclaw/openclaw/issues/86182) | 0 | Local model runtime | discord/picker: structural 25-option / 5-row / 100-char limits constrain large wildcard configs |
| [#86174](https://github.com/openclaw/openclaw/issues/86174) | 0 | Model routing/config | [Bug]: WebChat + New Session displays default model but inherits parent's model override |
| [#86090](https://github.com/openclaw/openclaw/issues/86090) | 9 | Local model runtime | runHeartbeatOnce returns {status: "ran"} in 78ms on idle agent — phantom run, no model turn executed |
| [#86048](https://github.com/openclaw/openclaw/issues/86048) | 0 | Local model runtime | WSL2 GPU-PV driver lockup: nvidia-smi hangs after llama-server D-state crash |
| [#86044](https://github.com/openclaw/openclaw/issues/86044) | 4 | OpenAI-compatible/proxy | 2026.5.22: CLI hangs on Windows - provider auth-state pre-warm blocks all CLI commands |
| [#86034](https://github.com/openclaw/openclaw/issues/86034) | 4 | OpenAI-compatible/proxy | Media generation succeeds but completion delivery fails and looks like generation failure |
| [#85918](https://github.com/openclaw/openclaw/issues/85918) | 1 | OpenAI-compatible/proxy | Bug: Foundry DeepSeek V4 tool turns surface DSML text instead of executable tool calls |
| [#85826](https://github.com/openclaw/openclaw/issues/85826) | 4 | Local model runtime | [Bug]: Agent stall detector hard-coded 120s threshold kills legitimate long model calls on local vLLM |
| [#85773](https://github.com/openclaw/openclaw/issues/85773) | 9 | Local model runtime | [Bug]: After reinstalling (v2026.5.20), agents only provide generic replies, completely ignoring workspace files content and skills |
| [#85684](https://github.com/openclaw/openclaw/issues/85684) | 0 | OpenAI-compatible/proxy | pi-embedded-runner: reasoning-only retry short-circuited in group chats by silentReplyPolicy default |
| [#85382](https://github.com/openclaw/openclaw/issues/85382) | 4 | Local memory/embedding | [Bug] post-compaction embedding sync fails with 500 when memorySearch.remote.baseUrl points to non-OpenAI host |
| [#85321](https://github.com/openclaw/openclaw/issues/85321) | 0 | Open-weight/provider behavior | `wrapStreamRepairMalformedToolCallArguments` clears valid tool call arguments for Moonshot/Kimi provider |
| [#85192](https://github.com/openclaw/openclaw/issues/85192) | 13 | OpenAI-compatible/proxy | DeepSeek V4: isSignedThinkingBlock misses unsigned thinking blocks - reasoning-only retry fails |
| [#85126](https://github.com/openclaw/openclaw/issues/85126) | 10 | Local model runtime | Bug: Control UI (TUI/WebChat) sessions auto-select wrong authProfileOverride (deepseek instead of minimax) at creation |
| [#84918](https://github.com/openclaw/openclaw/issues/84918) | 0 | OpenAI-compatible/proxy | OpenWebUI image uploads reach image tool as empty image via /v1/chat/completions on 2026.5.18 |
| [#84865](https://github.com/openclaw/openclaw/issues/84865) | 0 | Open-weight/provider behavior | user-switched model has no fallback chain, causing session deadlock on provider outage |
| [#84697](https://github.com/openclaw/openclaw/issues/84697) | 0 | OpenAI-compatible/proxy | Custom OpenAI-compatible provider with baseUrl without /v1 fails with cryptic 'incomplete terminal response' error |
| [#84575](https://github.com/openclaw/openclaw/issues/84575) | 4 | OpenAI-compatible/proxy | [Bug] /v1/chat/completions: second request with same x-openclaw-session-key during in-flight turn runs in isolated session, loses memory scope |
| [#84569](https://github.com/openclaw/openclaw/issues/84569) | 13 | Local model runtime | WhatsApp session stalls on long model_call: incomplete turn with payloads=0, reply never delivered |
| [#84384](https://github.com/openclaw/openclaw/issues/84384) | 0 | OpenAI-compatible/proxy | [Bug]: Gemini 2.5 Flash via vertex-ai (OpenAI-compatible) streaming times out - thinking tokens not handled |
| [#84218](https://github.com/openclaw/openclaw/issues/84218) | 4 | Local model runtime | Heartbeat isolatedSession=true replays prior heartbeat context, causing deterministic overflow/restart loop |
| [#84217](https://github.com/openclaw/openclaw/issues/84217) | 0 | Local model runtime | [Bug]: Heartbeat dispatch delivers free text block alongside message-tool call (chatty non-Codex providers, v2026.5.18) |
| [#84070](https://github.com/openclaw/openclaw/issues/84070) | 0 | Local model runtime | Active Memory embedded runner fails to expose plugin tools when hidden runner is on the DeepSeek provider path |
| [#83709](https://github.com/openclaw/openclaw/issues/83709) | 0 | Open-weight/provider behavior | [Feature]: Add `supportsPromptCacheKey` to Mistral transport compat patch |
| [#83584](https://github.com/openclaw/openclaw/issues/83584) | 4 | OpenAI-compatible/proxy | [Bug]: Outbound MEDIA: directive on /v1/responses and /v1/chat/completions is passed through as raw text instead of translated to image_url / file content block |
| [#83402](https://github.com/openclaw/openclaw/issues/83402) | 5 | OpenAI-compatible/proxy | [Bug]: Providers/Xiaomi: MiMo mimo-v2.5-pro still rejects cron embedded agent tool schema with 400 after 2026.5.12 fix |
| [#83399](https://github.com/openclaw/openclaw/issues/83399) | 0 | OpenAI-compatible/proxy | Bug: Tool call loop when assistant generates text + toolCall with openai-completions API |
| [#83333](https://github.com/openclaw/openclaw/issues/83333) | 0 | Local memory/embedding | [Bug]: Memory provider cutover to Ollama leaves production index in mixed OpenAI/Ollama vector state after live sync/reload |
| [#82594](https://github.com/openclaw/openclaw/issues/82594) | 2 | Local model runtime | [Bug]: openclaw onboard extremely slow on Windows during model loading |
| [#81961](https://github.com/openclaw/openclaw/issues/81961) | 5 | OpenAI-compatible/proxy | [Feature]: Add a simple Dashboard UX to manage multiple model providers |
| [#81960](https://github.com/openclaw/openclaw/issues/81960) | 4 | Local model runtime | [Feature]: Allow onboarding to configure multiple providers and models |
| [#81925](https://github.com/openclaw/openclaw/issues/81925) | 0 | Local memory/embedding | Compaction: `after_compaction` not emitted when `result.compacted:false`; validation: single-quote delimiter trips tool-caller retries |
| [#81835](https://github.com/openclaw/openclaw/issues/81835) | 0 | OpenAI-compatible/proxy | Bug: thinking parameter format incompatible with Volcengine CodingPlan v3 API |
| [#81530](https://github.com/openclaw/openclaw/issues/81530) | 13 | Local model runtime | [Bug]: [5.12-beta.8] Telegram Supergroup Forum Topics - Inbound Messages Not Processed |
| [#81525](https://github.com/openclaw/openclaw/issues/81525) | 5 | OpenAI-compatible/proxy | [Bug]: media-understanding silently routes images to user-declared vision models without validating declared capabilities |
| [#81214](https://github.com/openclaw/openclaw/issues/81214) | 9 | Local model runtime | [Bug]: OpenClaw 2026.5.7 subagent regression |
| [#80722](https://github.com/openclaw/openclaw/issues/80722) | 4 | Local model runtime | config set "Restart the gateway to apply" warning is misleading for active agents without agentRuntime override |
| [#80521](https://github.com/openclaw/openclaw/issues/80521) | 0 | Local model runtime | UI feature request: model picker + drag-to-reorder for primary/fallback model selection in Agents > Overview |
| [#80336](https://github.com/openclaw/openclaw/issues/80336) | 0 | Local model runtime | [Bug]: placeholder.openclaw.cloud unreachable on WSL2 with custom gateway port |
| [#80317](https://github.com/openclaw/openclaw/issues/80317) | 0 | OpenAI-compatible/proxy | TTS OpenAI provider: MP3 responseFormat not voice-compatible for Telegram, unlike Edge TTS |
| [#80081](https://github.com/openclaw/openclaw/issues/80081) | 4 | OpenAI-compatible/proxy | Need documented config keys for disabling plugin/tool/channel/owner-elevated surfaces for proposal-only mode |
| [#79897](https://github.com/openclaw/openclaw/issues/79897) | 4 | OpenAI-compatible/proxy | OpenAI-compatible streaming with llama.cpp saves zero usage (stream closed before final usage chunk) |
| [#79847](https://github.com/openclaw/openclaw/issues/79847) | 13 | Local memory/embedding | qmd-manager leaks XDG_CONFIG_HOME / XDG_CACHE_HOME to all child spawns, breaking mcporter >= 0.10 integration |
| [#79437](https://github.com/openclaw/openclaw/issues/79437) | 0 | Local memory/embedding | Prebuilt `node-llama-cpp` Windows binaries crash (0xC0000005) on Intel Alder Lake-N (N95) - qmd LLM half unusable |
| [#79380](https://github.com/openclaw/openclaw/issues/79380) | 2 | OpenAI-compatible/proxy | [Bug]: Gateway CPU spin / crash loop on Raspberry Pi 4 (ARM64) - regression from 4.23 to 4.25+ |
| [#78897](https://github.com/openclaw/openclaw/issues/78897) | 4 | OpenAI-compatible/proxy | OpenAI Responses provider should allow store=true for LiteLLM gpt-5.5 continuations |
| [#78091](https://github.com/openclaw/openclaw/issues/78091) | 0 | OpenAI-compatible/proxy | [Bug]: Open-WebUI creates new session per message instead of reusing persistent session |
| [#77792](https://github.com/openclaw/openclaw/issues/77792) | 0 | OpenAI-compatible/proxy | fix(tts/xiaomi): support per-call voice and model overrides |
| [#77692](https://github.com/openclaw/openclaw/issues/77692) | 4 | OpenAI-compatible/proxy | fix(tts/xiaomi): Xiaomi Token Plan endpoint uses Bearer auth, not api-key header |
| [#77675](https://github.com/openclaw/openclaw/issues/77675) | 4 | Local model runtime | [Bug]: request.headers SecretRefs on model providers fail in embedded agent context with "unresolved SecretRef" error |
| [#77645](https://github.com/openclaw/openclaw/issues/77645) | 1 | Local memory/embedding | memory status --deep reports QMD embeddings unavailable when searchMode=search intentionally disables vectors |
| [#77336](https://github.com/openclaw/openclaw/issues/77336) | 4 | OpenAI-compatible/proxy | [Feature Request]: Built-in handling of strict role alternation for Mistral / SGLang backends |
| [#77142](https://github.com/openclaw/openclaw/issues/77142) | 4 | Local memory/embedding | [Feature]: Parametric consolidation channel for dreaming pipeline (CLS Phase 4) |
| [#77090](https://github.com/openclaw/openclaw/issues/77090) | 1 | Local model runtime | Feature: Auto-revert to primary model after image analysis |
| [#76884](https://github.com/openclaw/openclaw/issues/76884) | 5 | Local model runtime | [Bug]: OpenClaw on native Windows getting notably slower and slower with each new version??? |
| [#76665](https://github.com/openclaw/openclaw/issues/76665) | 8 | Open-weight/provider behavior | Session context silently lost between consecutive turns with z.ai provider (GLM gateway) |
| [#76612](https://github.com/openclaw/openclaw/issues/76612) | 4 | Open-weight/provider behavior | Kimi Code returns empty content when Anthropic cache_control markers are sent |
| [#75959](https://github.com/openclaw/openclaw/issues/75959) | 6 | OpenAI-compatible/proxy | [Feature]: Support image analysis for Kimi Code Plan |
| [#75811](https://github.com/openclaw/openclaw/issues/75811) | 0 | Local model runtime | [Bug]: `exec` tool schema exposes `security`/`elevated`/`ask` fields as model-controllable; model self-imposes denial |
| [#75378](https://github.com/openclaw/openclaw/issues/75378) | 22 | Local model runtime | [Bug] Gateway event loop saturation during parallel subagent spawn causes 1012 restart (v2026.4.29) |
| [#75312](https://github.com/openclaw/openclaw/issues/75312) | 0 | Local memory/embedding | Bug: wiki_search throws 'sharedMemoryManager.search is not a function' when search.backend=shared and corpus includes memory/all |
| [#75301](https://github.com/openclaw/openclaw/issues/75301) | 4 | Local model runtime | [Feature]: `openclaw caches` command to inspect and prune unbounded `~/.openclaw/` cache dirs (plugin-runtime-deps, browser, tools, orphan transcripts) |
| [#75189](https://github.com/openclaw/openclaw/issues/75189) | 0 | Local model runtime | [Bug]: Default `bootstrapMaxChars=20000` + verbose auto-generated bootstrap content degrades tool dispatch on small/mid models |
| [#75187](https://github.com/openclaw/openclaw/issues/75187) | 0 | Local model runtime | [Bug]: Auto-generated `AGENTS.md` puts load-bearing tool-use rules at the bottom; head-truncation by `bootstrapMaxChars` strips them |
| [#75163](https://github.com/openclaw/openclaw/issues/75163) | 4 | OpenAI-compatible/proxy | Bug: TUI mid-session model switch passes raw alias instead of resolved model ID |
| [#75105](https://github.com/openclaw/openclaw/issues/75105) | 5 | Open-weight/provider behavior | [Feature]: Allow per-model setting for Deepseek `reasoning_content` fix |
| [#75040](https://github.com/openclaw/openclaw/issues/75040) | 0 | Local model runtime | [Bug]: extra_body overwriting request payload keys: thinking - framework-level thinking field collision affecting all providers |
| [#75026](https://github.com/openclaw/openclaw/issues/75026) | 0 | OpenAI-compatible/proxy | MiniMax token usage shows 0 in Control UI Usage page (only message count works) |
| [#74986](https://github.com/openclaw/openclaw/issues/74986) | 14 | Local model runtime | [Bug]: openclaw infer hangs indefinitely on 2026.4.27 - openclaw-infer child spins at 100% CPU with zero network I/O |
| [#74910](https://github.com/openclaw/openclaw/issues/74910) | 4 | Local memory/embedding | doctor: agents.defaults.llm.idleTimeoutSeconds auto-fix discards the user value; runtime gives no signal until doctor runs |
| [#74900](https://github.com/openclaw/openclaw/issues/74900) | 0 | Local memory/embedding | [Feature]: stable public SDK path for embedding provider API (independent of memory-core) |
| [#74835](https://github.com/openclaw/openclaw/issues/74835) | 0 | OpenAI-compatible/proxy | Add global provider request proxy/default SSRF policy for model providers |
| [#74732](https://github.com/openclaw/openclaw/issues/74732) | 5 | Local memory/embedding | docs+feat: Document oMLX (Apple Silicon MLX) as memorySearch embedding provider |
| [#74586](https://github.com/openclaw/openclaw/issues/74586) | 17 | Local memory/embedding | AM embedded run aborts memory_search tool calls; classifies as timeout despite model completion |
| [#74481](https://github.com/openclaw/openclaw/issues/74481) | 0 | OpenAI-compatible/proxy | feat: dynamic catalog refresh from configured provider /v1/models |
| [#74310](https://github.com/openclaw/openclaw/issues/74310) | 4 | Open-weight/provider behavior | Bug Report: `normalizeProviderId` breaks provider-namespaced models like `kimi-coding/k2p5` |
| [#74204](https://github.com/openclaw/openclaw/issues/74204) | 0 | Local memory/embedding | memory.qmd.update.embedTimeoutMs default (120 s) is too low for local GGUF; error message doesn't surface the fix |
| [#74021](https://github.com/openclaw/openclaw/issues/74021) | 8 | OpenAI-compatible/proxy | Support reasoning-field outputs and visible final-answer handling for native reasoning models |
| [#74020](https://github.com/openclaw/openclaw/issues/74020) | 0 | OpenAI-compatible/proxy | Gateway startup: models.mode=replace should skip pricing fetches |
| [#73801](https://github.com/openclaw/openclaw/issues/73801) | 4 | OpenAI-compatible/proxy | Active Memory with Cerebras gpt-oss-120b times out and can pin gateway CPU |
| [#73432](https://github.com/openclaw/openclaw/issues/73432) | 9 | Local memory/embedding | [Bug]: qmd embedding is never triggered per memory.qmd.update.interval/embedInterval |
| [#73186](https://github.com/openclaw/openclaw/issues/73186) | 0 | OpenAI-compatible/proxy | [Bug]: Thinking/reasoning content leaks into cron announce delivery for Matrix/Feishu |
| [#73144](https://github.com/openclaw/openclaw/issues/73144) | 1 | Open-weight/provider behavior | Model switch experience: 5 issues when switching from qwen3.6-plus to deepseek-v4-pro |
| [#72927](https://github.com/openclaw/openclaw/issues/72927) | 0 | Open-weight/provider behavior | feat(tts): support MiMo v2.5 TTS VoiceDesign |
| [#72359](https://github.com/openclaw/openclaw/issues/72359) | 0 | Local memory/embedding | Active Memory: add single-shot mode (no embedded agent loop) for low-latency preflight injection |
| [#72015](https://github.com/openclaw/openclaw/issues/72015) | 29 | Local memory/embedding | Reliability: active-memory blocks replies and QMD boot initialization can overload multi-agent gateways |
| [#71784](https://github.com/openclaw/openclaw/issues/71784) | 9 | Local memory/embedding | Bug: memory search live embedding fails ~20-40% with `fetch failed \ |
| [#71491](https://github.com/openclaw/openclaw/issues/71491) | 25 | Open-weight/provider behavior | Kimi K2.6 reasoning_content 400 regression in long conversations after LCM compaction (follow-up #70392) |
| [#71273](https://github.com/openclaw/openclaw/issues/71273) | 0 | Open-weight/provider behavior | Bug: Kimi Code model enters infinite tool call loop |
| [#70559](https://github.com/openclaw/openclaw/issues/70559) | 0 | Local memory/embedding | runUnsafeReindex crashes with "no such table: chunks_vec" when sqlite-vec is enabled |
| [#69943](https://github.com/openclaw/openclaw/issues/69943) | 4 | Local memory/embedding | [Bug]: session-memory hook persists raw chat-template tokens and unparsed tool calls - re-injected context creates self-reinforcing poisoning loop, agents emit role tokens / NO_REPLY across all subsequent /new sessions |
| [#68920](https://github.com/openclaw/openclaw/issues/68920) | 14 | Local memory/embedding | HTTP /v1/chat/completions: 10-15s TTFB due to full agent context assembly - needs lightContext/voice mode |
| [#68812](https://github.com/openclaw/openclaw/issues/68812) | 0 | Local memory/embedding | Make memory embedding retry/concurrency parameters configurable |
| [#68222](https://github.com/openclaw/openclaw/issues/68222) | 0 | Open-weight/provider behavior | [Bug]: Kimi Code model frequent sessions_yield tool call/output interrupts long-running tasks, requires manual intervention to resume |
| [#67593](https://github.com/openclaw/openclaw/issues/67593) | 1 | Open-weight/provider behavior | feat: add Kimi/Moonshot provider usage and balance display |
| [#67423](https://github.com/openclaw/openclaw/issues/67423) | 4 | Open-weight/provider behavior | [Bug] Auth router ignores provider entry's apiKey field, resolves via auth.order by canonical provider ID - wrong key for split provider entries |
| [#67379](https://github.com/openclaw/openclaw/issues/67379) | 0 | Local memory/embedding | qmd scope denies subagent sessions - channel/chatType resolve to undefined |
| [#67035](https://github.com/openclaw/openclaw/issues/67035) | 34 | Local model runtime | [Bug]: 2026.4.14 Windows chat UI regression: input text swallowed, streamed replies often invisible until refresh, typing indicator flashes then blanks |
| [#66339](https://github.com/openclaw/openclaw/issues/66339) | 0 | Local memory/embedding | memory search can hit QMD SQLite lock contention during normal runtime |
| [#66125](https://github.com/openclaw/openclaw/issues/66125) | 5 | OpenAI-compatible/proxy | [Bug]: openai-completions fallback candidate is selected, but fallback does not complete successfully through an OpenAI-compatible proxy |
| [#65557](https://github.com/openclaw/openclaw/issues/65557) | 0 | Local model runtime | Provider & model selection per session/account with admin-controlled allowlists |
| [#64438](https://github.com/openclaw/openclaw/issues/64438) | 8 | Local memory/embedding | Feature Request: Remote Reranker Endpoint Support |
| [#64224](https://github.com/openclaw/openclaw/issues/64224) | 0 | OpenAI-compatible/proxy | Billing cooldown flags entire provider instead of individual model - breaks proxy/litellm setups |
| [#64212](https://github.com/openclaw/openclaw/issues/64212) | 0 | Open-weight/provider behavior | [Bug]: Image tool fails with "Request was aborted" for NVIDIA Kimi K2.5 |
| [#63990](https://github.com/openclaw/openclaw/issues/63990) | 6 | Local memory/embedding | Feature: Multi-index embedding memory with model-aware failover (no mixed vector spaces) |
| [#63685](https://github.com/openclaw/openclaw/issues/63685) | 8 | Open-weight/provider behavior | [Bug]: Cannot run gemma 4 models from google ai studio |
| [#63531](https://github.com/openclaw/openclaw/issues/63531) | 0 | Local memory/embedding | [Feature]: Add MLX Talk provider MVP for local macOS TTS |
| [#63229](https://github.com/openclaw/openclaw/issues/63229) | 4 | Local model runtime | Bug: Gateway falsely marks healthy local vLLM endpoints as timed out/overloaded, causing 1-23 min fallback cascades |
| [#62924](https://github.com/openclaw/openclaw/issues/62924) | 4 | Local model runtime | Expose actual media-understanding chosen model in inbound body to avoid guessed media model reporting |
| [#62780](https://github.com/openclaw/openclaw/issues/62780) | 0 | Local model runtime | Feature: message:before_send hook to enable content-quality fallback gating |
| [#62599](https://github.com/openclaw/openclaw/issues/62599) | 4 | Local model runtime | [Bug]: openclaw status loads memory plugins locally and can report false vector state |
| [#62436](https://github.com/openclaw/openclaw/issues/62436) | 0 | OpenAI-compatible/proxy | Feature: Lightweight LLM passthrough mode for /v1/chat/completions - skip session persistence entirely |
| [#62432](https://github.com/openclaw/openclaw/issues/62432) | 0 | Open-weight/provider behavior | [Bug]: Xiaomi/MiMo sessions can repeatedly relaunch exec after 'Command still running' instead of switching to process poll |
| [#62328](https://github.com/openclaw/openclaw/issues/62328) | 17 | Local memory/embedding | node:sqlite missing FTS5 module - memory search keyword fallback broken |
| [#62121](https://github.com/openclaw/openclaw/issues/62121) | 8 | Local model runtime | DeepSeek preamble text leaks to Telegram after 3.13 -> 4.5 upgrade (untagged assistant text bypasses commentary filter) |
| [#62109](https://github.com/openclaw/openclaw/issues/62109) | 0 | OpenAI-compatible/proxy | Interactive runs fail with auth-style 403 when custom OpenAI-compatible provider baseUrl uses Unicode/IDN or punycode hostname, but ASCII hostname/IP works |
| [#61834](https://github.com/openclaw/openclaw/issues/61834) | 1 | Local memory/embedding | [Feature]: expose QMD no-rerank for memory.qmd query mode |
| [#61716](https://github.com/openclaw/openclaw/issues/61716) | 0 | OpenAI-compatible/proxy | [Feature]: Add model parameter prompts (context window, max_tokens, modalities) during OpenAI-compatible provider onboarding CLI flow |
| [#60546](https://github.com/openclaw/openclaw/issues/60546) | 9 | OpenAI-compatible/proxy | [Bug]: microsoft-foundry provider selects Claude deployments but routes them through OpenAI Foundry endpoints |
| [#60344](https://github.com/openclaw/openclaw/issues/60344) | 4 | Open-weight/provider behavior | [Bug]: Recursive output of system marker [image data removed - already processed by model] in kimi-coding/k2p |
| [#60078](https://github.com/openclaw/openclaw/issues/60078) | 0 | Local model runtime | [Bug]: Announce delivery ignores modelByChannel, always uses agent default model |
| [#59168](https://github.com/openclaw/openclaw/issues/59168) | 2 | Local model runtime | feat(models): use provider/name as internal key to decouple from API model ID |
| [#58765](https://github.com/openclaw/openclaw/issues/58765) | 0 | Local memory/embedding | Feature: Support output dimensionality truncation for local GGUF embedding models |
| [#57996](https://github.com/openclaw/openclaw/issues/57996) | 4 | Local memory/embedding | QMD per-agent SQLite caches cause extreme disk I/O on multi-agent deployments<br>Assignee: vincentkoc |
| [#57638](https://github.com/openclaw/openclaw/issues/57638) | 0 | OpenAI-compatible/proxy | feat: cron.defaults for model, delivery, and contextTokens |
| [#57443](https://github.com/openclaw/openclaw/issues/57443) | 0 | OpenAI-compatible/proxy | [Bug]: Tool JSON Schema patternProperties causes 400 errors on BytePlus Ark (doubao) - schema cleaning should be universal, not provider-specific |
| [#54463](https://github.com/openclaw/openclaw/issues/54463) | 10 | Local memory/embedding | QMD memory indexing can recurse into symlink loops in workspace-visible temp monorepos and fail with ENAMETOOLONG<br>Assignee: vincentkoc |
| [#54155](https://github.com/openclaw/openclaw/issues/54155) | 12 | Local memory/embedding | Gateway memory leak: 389MB -> 14.7GB over 4 days with session accumulation |
| [#54128](https://github.com/openclaw/openclaw/issues/54128) | 0 | Local memory/embedding | Add maxThreads config for local embedding (node-llama-cpp) |
| [#53810](https://github.com/openclaw/openclaw/issues/53810) | 0 | OpenAI-compatible/proxy | Subagent Premature Announce Bug - Model-Specific Tool Call Handling Issues |
| [#53550](https://github.com/openclaw/openclaw/issues/53550) | 4 | Local memory/embedding | experimental.sessionMemory does not surface gateway-dispatched sessions in memory_search |
| [#52029](https://github.com/openclaw/openclaw/issues/52029) | 8 | Local model runtime | Feature Request: heartbeat.tools option to disable tools during heartbeat |
| [#51593](https://github.com/openclaw/openclaw/issues/51593) | 0 | Open-weight/provider behavior | [Bug]: HTTP 400: "tool call id exec:26 is duplicated" with moonshot/kimi-k2.5 in WhatsApp group chats |
| [#51441](https://github.com/openclaw/openclaw/issues/51441) | 12 | OpenAI-compatible/proxy | feat: expose resolved backend model in session_status and agent runtime |
| [#49205](https://github.com/openclaw/openclaw/issues/49205) | 4 | OpenAI-compatible/proxy | [Bug]: Control UI messages can reach shared context but still not appear in Open WebUI visible chat history |
| [#48300](https://github.com/openclaw/openclaw/issues/48300) | 6 | Local memory/embedding | Bug: memory_search hybrid mode not returning FTS matches |
| [#47884](https://github.com/openclaw/openclaw/issues/47884) | 0 | Local memory/embedding | [Bug]: memory_search tool fails with "fetch failed" despite embedding provider configured |
| [#46661](https://github.com/openclaw/openclaw/issues/46661) | 4 | OpenAI-compatible/proxy | [Feature]: Support Custom ASR (Speech-to-Text) Server Configuration |
| [#45508](https://github.com/openclaw/openclaw/issues/45508) | 8 | OpenAI-compatible/proxy | [Feature]: Self-hosted STT/TTS provider support in webchat (Route webchat TTS through the gateway instead of browser Speech API) |
| [#45049](https://github.com/openclaw/openclaw/issues/45049) | 12 | OpenAI-compatible/proxy | Agent loop allows simulated tool calls instead of enforcing real tool invocation |
| [#44870](https://github.com/openclaw/openclaw/issues/44870) | 4 | Model/provider behavior | [Bug]: I have been unable to verify using the codex from the transfer station |
| [#44789](https://github.com/openclaw/openclaw/issues/44789) | 0 | OpenAI-compatible/proxy | [Bug]: openclaw 2026.03.11 partially config litellm |
| [#43432](https://github.com/openclaw/openclaw/issues/43432) | 0 | Local memory/embedding | [Feature]: Memory durability config - hard flush threshold, priority-aware compaction, cache TTL |
| [#42408](https://github.com/openclaw/openclaw/issues/42408) | 0 | Local memory/embedding | [Bug/Docs]: local+hybrid memory_search quality can appear unstable due to extraPaths path drift + benchmark-file contamination |
| [#41372](https://github.com/openclaw/openclaw/issues/41372) | 8 | Model/provider behavior | Field Report: 25 findings from 4 weeks of self-hosted production use (config crashes, CLI docs, Discord, cron) |
| [#41135](https://github.com/openclaw/openclaw/issues/41135) | 1 | Local model runtime | [Feature]: Add provider-profile routing policies for multi-account OAuth/API pools (starting with google-gemini-cli) |
| [#37966](https://github.com/openclaw/openclaw/issues/37966) | 9 | OpenAI-compatible/proxy | [Bug]: cacheRetention ignored for LiteLLM-proxied Anthropic models |
| [#33962](https://github.com/openclaw/openclaw/issues/33962) | 15 | Local model runtime | [Feature]: slug-generator: use lightweight model instead of agent primary to prevent lane congestion |
| [#33329](https://github.com/openclaw/openclaw/issues/33329) | 10 | Local model runtime | Document and add config toggles for all implicit discovery mechanisms |
| [#32496](https://github.com/openclaw/openclaw/issues/32496) | 14 | OpenAI-compatible/proxy | [Feature]: Support frequency_penalty and presence_penalty Parameters for OpenAI-Compatible Providers |
| [#30381](https://github.com/openclaw/openclaw/issues/30381) | 7 | OpenAI-compatible/proxy | chatCompletions: ignore request model when x-openclaw-agent-id header is present |
| [#22021](https://github.com/openclaw/openclaw/issues/22021) | 4 | Local model runtime | [Feature]: Add X-Actual-Model header to expose runtime model in HTTP responses |
| [#17925](https://github.com/openclaw/openclaw/issues/17925) | 20 | Open-weight/provider behavior | [Feature]: Support native web_search passthrough for ZAI (GLM) and Google (Gemini) providers |
| [#15073](https://github.com/openclaw/openclaw/issues/15073) | 8 | Local model runtime | Feature Request: Per-agent context/workspace on model fallback |
| [#13962](https://github.com/openclaw/openclaw/issues/13962) | 4 | Local model runtime | Feature: Per-mention model routing + context window for group mentions |
| [#10480](https://github.com/openclaw/openclaw/issues/10480) | 9 | OpenAI-compatible/proxy | Support Workers AI model selection during onboard |

## OPEN PRS (204)

| PR | Activity | Area | Title |
| --- | --- | --- | --- |
| [#89070](https://github.com/openclaw/openclaw/pull/89070) | 0 | Local model runtime | fix(stream): handle cumulative JSON chunks from local llama.cpp tool calls |
| [#89049](https://github.com/openclaw/openclaw/pull/89049) | 0 | Local model runtime | fix(idle-timeout): honor provider timeout for no-timeout runs |
| [#89040](https://github.com/openclaw/openclaw/pull/89040) | 0 | Local model runtime | perf: avoid event-loop stall during embedded_run bootstrap-context |
| [#89039](https://github.com/openclaw/openclaw/pull/89039) | 0 | OpenAI-compatible/proxy | fix: prevent silent message loss from EmbeddedAttemptSessionTakeoverError |
| [#89029](https://github.com/openclaw/openclaw/pull/89029) | 0 | Model routing/config | fix(cli): accept empty Claude end turns |
| [#89027](https://github.com/openclaw/openclaw/pull/89027) | 0 | Model routing/config | fix(cli): prevent empty_response failover for completed thinking-only turns |
| [#89016](https://github.com/openclaw/openclaw/pull/89016) | 0 | OpenAI-compatible/proxy | fix(agents): guard OpenAI transport tool descriptors |
| [#89013](https://github.com/openclaw/openclaw/pull/89013) | 0 | OpenAI-compatible/proxy | fix(agents): materialize OpenAI tool schemas |
| [#89001](https://github.com/openclaw/openclaw/pull/89001) | 0 | OpenAI-compatible/proxy | fix: support Azure Responses text stream events |
| [#88999](https://github.com/openclaw/openclaw/pull/88999) | 0 | Local model runtime | fix(cron): repair concatenated JSON keys from local-model tool-call parsers |
| [#88994](https://github.com/openclaw/openclaw/pull/88994) | 0 | Model routing/config | fix(agents): quarantine normalized runtime tools |
| [#88977](https://github.com/openclaw/openclaw/pull/88977) | 0 | Model routing/config | fix(agents): tolerate provider tool schema hook failures |
| [#88976](https://github.com/openclaw/openclaw/pull/88976) | 0 | Open-weight/provider behavior | fix(mistral): enable prompt cache key compat |
| [#88964](https://github.com/openclaw/openclaw/pull/88964) | 0 | OpenAI-compatible/proxy | [codex] Repair context-engine tool-result pairing |
| [#88959](https://github.com/openclaw/openclaw/pull/88959) | 0 | Model routing/config | fix(plugins): ignore throwing provider runtime hooks |
| [#88958](https://github.com/openclaw/openclaw/pull/88958) | 0 | Model routing/config | Fix BTW OAuth side-question routing |
| [#88956](https://github.com/openclaw/openclaw/pull/88956) | 0 | Model routing/config | Repair compacted tool-result chains |
| [#88950](https://github.com/openclaw/openclaw/pull/88950) | 0 | Model routing/config | fix(plugins): ignore throwing provider policy hooks |
| [#88946](https://github.com/openclaw/openclaw/pull/88946) | 0 | Model routing/config | Fix live model inference edge cases |
| [#88940](https://github.com/openclaw/openclaw/pull/88940) | 0 | OpenAI-compatible/proxy | fix(llm): repairJson injects control chars for backslash b/f/n/r/t into Windows paths |
| [#88931](https://github.com/openclaw/openclaw/pull/88931) | 0 | Local model runtime | fix(agents): cap tool search fanout in lean mode |
| [#88928](https://github.com/openclaw/openclaw/pull/88928) | 0 | OpenAI-compatible/proxy | fix(llm): preserve Windows path control escapes |
| [#88926](https://github.com/openclaw/openclaw/pull/88926) | 0 | OpenAI-compatible/proxy | fix(llm): preserve Windows path escapes in streamed args |
| [#88924](https://github.com/openclaw/openclaw/pull/88924) | 0 | Open-weight/provider behavior | fix(agents): strip streamed reasoning tags |
| [#88922](https://github.com/openclaw/openclaw/pull/88922) | 0 | Model routing/config | fix(google): forward stop sequences to Gemini generationConfig |
| [#88917](https://github.com/openclaw/openclaw/pull/88917) | 0 | OpenAI-compatible/proxy | fix: retry stale Responses reasoning replay safely |
| [#88906](https://github.com/openclaw/openclaw/pull/88906) | 0 | Model routing/config | fix(openai): allow Codex Spark via harness |
| [#88905](https://github.com/openclaw/openclaw/pull/88905) | 0 | Local memory/embedding | feat(dreaming): expose shadow-trial scoring in reports |
| [#88896](https://github.com/openclaw/openclaw/pull/88896) | 0 | Local/media model provider | fix: harden CLI and plugin edge cases |
| [#88893](https://github.com/openclaw/openclaw/pull/88893) | 0 | OpenAI-compatible/proxy | fix: support Azure Responses API text content type |
| [#88890](https://github.com/openclaw/openclaw/pull/88890) | 0 | Local model runtime | fix #87768: [Bug]: push to talk mac os companion app hard codes thinking low |
| [#88887](https://github.com/openclaw/openclaw/pull/88887) | 0 | Local memory/embedding | fix(memory-core): don't run the LLM reranker in vsearch/search modes |
| [#88884](https://github.com/openclaw/openclaw/pull/88884) | 0 | Local model runtime | fix(agents): trim web tools in lean mode |
| [#88882](https://github.com/openclaw/openclaw/pull/88882) | 0 | Local model runtime | test(gateway): add small model live profile |
| [#88881](https://github.com/openclaw/openclaw/pull/88881) | 0 | Local model runtime | fix(agents): trim media tools in lean mode |
| [#88880](https://github.com/openclaw/openclaw/pull/88880) | 0 | Model routing/config | fix(agents): project nullable tool schemas for providers |
| [#88878](https://github.com/openclaw/openclaw/pull/88878) | 0 | Model routing/config | fix(agents): project cron tool schemas for providers |
| [#88873](https://github.com/openclaw/openclaw/pull/88873) | 0 | Local model runtime | fix(agent-os): harden full-local substrate |
| [#88869](https://github.com/openclaw/openclaw/pull/88869) | 0 | Open-weight/provider behavior | Add MiniMax M3 support to the bundled MiniMax provider |
| [#88861](https://github.com/openclaw/openclaw/pull/88861) | 0 | OpenAI-compatible/proxy | Fix OpenResponses callback message context |
| [#88851](https://github.com/openclaw/openclaw/pull/88851) | 0 | Model routing/config | Persist OpenRouter model cache in SQLite |
| [#88837](https://github.com/openclaw/openclaw/pull/88837) | 0 | Model routing/config | fix(agent): use static catalog for skip-agent model resolution |
| [#88830](https://github.com/openclaw/openclaw/pull/88830) | 0 | Local memory/embedding | feat(dreaming): score candidates with shadow trial results |
| [#88827](https://github.com/openclaw/openclaw/pull/88827) | 0 | Model routing/config | Add Vertex API key model config regression coverage |
| [#88822](https://github.com/openclaw/openclaw/pull/88822) | 0 | Local model runtime | fix(agents): compact lean local tool catalogs |
| [#88806](https://github.com/openclaw/openclaw/pull/88806) | 0 | Local memory/embedding | fix(memory-lancedb): reject envelope metadata sludge (incl. marker-free shapes) |
| [#88804](https://github.com/openclaw/openclaw/pull/88804) | 0 | OpenAI-compatible/proxy | fix(openai): keep stop-finished tool calls |
| [#88800](https://github.com/openclaw/openclaw/pull/88800) | 0 | Model routing/config | fix(models): keep generated secret refs out of plaintext |
| [#88799](https://github.com/openclaw/openclaw/pull/88799) | 0 | OpenAI-compatible/proxy | fix(openai): honor streamed tool calls with stop finish |
| [#88789](https://github.com/openclaw/openclaw/pull/88789) | 0 | Local model runtime | feat(agents): auto-trim lean local tools |
| [#88787](https://github.com/openclaw/openclaw/pull/88787) | 0 | OpenAI-compatible/proxy | feat(openai): support gpt-5.5 azure routing and reasoning, restrict telegram bot access |
| [#88771](https://github.com/openclaw/openclaw/pull/88771) | 0 | Local model runtime | fix(agents): stream phased text deltas incrementally |
| [#88769](https://github.com/openclaw/openclaw/pull/88769) | 0 | OpenAI-compatible/proxy | fix(agents): keep inline <think> reasoning out of OpenAI-compatible visible text |
| [#88767](https://github.com/openclaw/openclaw/pull/88767) | 0 | Model routing/config | fix(plugin-sdk): isolate provider catalog projection failures |
| [#88754](https://github.com/openclaw/openclaw/pull/88754) | 0 | Open-weight/provider behavior | fix(text): normalize CJK/fullwidth quotes in reasoning tag delimiters |
| [#88748](https://github.com/openclaw/openclaw/pull/88748) | 0 | Model routing/config | fix(gemini): bridge OAuth profiles into CLI runtime |
| [#88746](https://github.com/openclaw/openclaw/pull/88746) | 0 | Local model runtime | feat: add Agent OS full-local substrate |
| [#88723](https://github.com/openclaw/openclaw/pull/88723) | 0 | Model routing/config | fix(doctor): respect explicit PI runtime policy |
| [#88709](https://github.com/openclaw/openclaw/pull/88709) | 0 | Model routing/config | fix(auth): cooldown inline api key billing failures |
| [#88704](https://github.com/openclaw/openclaw/pull/88704) | 0 | Local memory/embedding | fix(memory): rehydrate daily list promotions |
| [#88696](https://github.com/openclaw/openclaw/pull/88696) | 0 | Local memory/embedding | fix #70559: runUnsafeReindex crashes with "no such table: chunks_vec" when sqlite-vec is enabled |
| [#88645](https://github.com/openclaw/openclaw/pull/88645) | 0 | Local model runtime | fix(llm): use JSON5 as intermediate fallback in parseStreamingJson to avoid partial-json key corruption |
| [#88630](https://github.com/openclaw/openclaw/pull/88630) | 0 | Model routing/config | fix(codex): avoid guardian review for local models |
| [#88608](https://github.com/openclaw/openclaw/pull/88608) | 0 | Model routing/config | fix(minimax): use account OAuth device endpoints |
| [#88553](https://github.com/openclaw/openclaw/pull/88553) | 0 | Model routing/config | fix(agents): unblock fallback classification tests |
| [#88551](https://github.com/openclaw/openclaw/pull/88551) | 0 | Model routing/config | fix(agents): skip auth gate for CLI-owned transport |
| [#88514](https://github.com/openclaw/openclaw/pull/88514) | 0 | Local model runtime | fix(gateway): avoid default provider auth startup prewarm |
| [#88512](https://github.com/openclaw/openclaw/pull/88512) | 0 | OpenAI-compatible/proxy | fix: resolve google provider default API to google-generative-ai |
| [#88506](https://github.com/openclaw/openclaw/pull/88506) | 0 | Model routing/config | feat: add per-agent compaction overrides |
| [#88482](https://github.com/openclaw/openclaw/pull/88482) | 0 | Model routing/config | docs: clarify auth profile provider field after openai-codex OAuth login |
| [#88468](https://github.com/openclaw/openclaw/pull/88468) | 0 | Model routing/config | fix(configure): migrate stale Codex defaults after OpenAI auth |
| [#88460](https://github.com/openclaw/openclaw/pull/88460) | 0 | Local model runtime | fix(cron): recover from local-llamacpp parameter serialization bugs |
| [#88400](https://github.com/openclaw/openclaw/pull/88400) | 0 | Model routing/config | fix(config): accept overlays for bundled provider aliases |
| [#88381](https://github.com/openclaw/openclaw/pull/88381) | 0 | Local model runtime | fix(agents): preserve runtime tools in lean mode |
| [#88378](https://github.com/openclaw/openclaw/pull/88378) | 0 | Open-weight/provider behavior | fix(xiaomi): support MiMo voicedesign TTS |
| [#88366](https://github.com/openclaw/openclaw/pull/88366) | 0 | Local model runtime | fix(agents): preserve required replies in lean local mode |
| [#88351](https://github.com/openclaw/openclaw/pull/88351) | 0 | Model routing/config | fix(plugin-sdk): isolate provider catalog projection failures |
| [#88329](https://github.com/openclaw/openclaw/pull/88329) | 0 | Model routing/config | fix: user-pinned model falls back to global chain on quota exhaustion |
| [#88320](https://github.com/openclaw/openclaw/pull/88320) | 0 | Open-weight/provider behavior | fix(agents): recover DeepSeek DSML tool calls |
| [#88289](https://github.com/openclaw/openclaw/pull/88289) | 0 | Open-weight/provider behavior | fix(microsoft-foundry): skip DeepSeek V4 thinking params on Foundry fallback |
| [#88263](https://github.com/openclaw/openclaw/pull/88263) | 0 | Local memory/embedding | fix(memory-core): use native recursive fs.watch in QMD watcher to prevent per-file FD leak |
| [#88249](https://github.com/openclaw/openclaw/pull/88249) | 0 | Model routing/config | feat(desktop): add Tauri model setup app |
| [#88241](https://github.com/openclaw/openclaw/pull/88241) | 0 | Model routing/config | test(crabbox): pin wrapper provider expectations |
| [#88238](https://github.com/openclaw/openclaw/pull/88238) | 0 | Local memory/embedding | perf(memory): batch memory embeddings across files |
| [#88212](https://github.com/openclaw/openclaw/pull/88212) | 0 | Local model runtime | feat(agents): auto-trim lean local model tools |
| [#88181](https://github.com/openclaw/openclaw/pull/88181) | 0 | Local model runtime | feat(agents): add strict local model lean profile |
| [#88108](https://github.com/openclaw/openclaw/pull/88108) | 0 | Local model runtime | fix(agents): compact lean local tool catalogs |
| [#88098](https://github.com/openclaw/openclaw/pull/88098) | 0 | OpenAI-compatible/proxy | feat(onboard): add --custom-context-window flag for non-interactive setup |
| [#88082](https://github.com/openclaw/openclaw/pull/88082) | 0 | Model routing/config | feat(stepfun): add step-3.7-flash model |
| [#88078](https://github.com/openclaw/openclaw/pull/88078) | 0 | Local memory/embedding | fix(active-memory): trim recall prompt envelope |
| [#88071](https://github.com/openclaw/openclaw/pull/88071) | 0 | OpenAI-compatible/proxy | fix(config): add dropReasoningFromHistory config for openai-completions providers (#88068) |
| [#88049](https://github.com/openclaw/openclaw/pull/88049) | 0 | Model routing/config | fix(status): exclude session-selected model from fallback display list |
| [#87958](https://github.com/openclaw/openclaw/pull/87958) | 0 | Model routing/config | fix(agents): scale read output for small contexts |
| [#87955](https://github.com/openclaw/openclaw/pull/87955) | 0 | Local model runtime | fix(agents): keep lean tools behind catalog controls |
| [#87940](https://github.com/openclaw/openclaw/pull/87940) | 0 | Local model runtime | fix(gateway): keep dense stream updates incremental |
| [#87933](https://github.com/openclaw/openclaw/pull/87933) | 0 | OpenAI-compatible/proxy | fix(agents): respect compat.thinkingFormat override for DeepSeek V4 models |
| [#87932](https://github.com/openclaw/openclaw/pull/87932) | 4 | Model routing/config | feat(compaction): support percentage strings for token thresholds |
| [#87927](https://github.com/openclaw/openclaw/pull/87927) | 0 | Model routing/config | fix(agents): cap compaction budgets for small contexts |
| [#87923](https://github.com/openclaw/openclaw/pull/87923) | 0 | Model routing/config | fix(thinking): keep explicit session thinkingLevel when runtime downgrades (#87740) |
| [#87907](https://github.com/openclaw/openclaw/pull/87907) | 0 | Local memory/embedding | fix(memory): validate memory index identity |
| [#87895](https://github.com/openclaw/openclaw/pull/87895) | 0 | Open-weight/provider behavior | test(agents): broaden small live hosted model matrix |
| [#87893](https://github.com/openclaw/openclaw/pull/87893) | 0 | Model routing/config | fix(auth-profiles): repair stale auto runtime auth selection |
| [#87874](https://github.com/openclaw/openclaw/pull/87874) | 4 | Local model runtime | fix(macos): inherit thinking for voice wake forwarding |
| [#87856](https://github.com/openclaw/openclaw/pull/87856) | 0 | Local model runtime | fix(agents): count streamed model deltas incrementally |
| [#87850](https://github.com/openclaw/openclaw/pull/87850) | 0 | Local model runtime | fix(agents): avoid constructing lean local model tools<br>Assignee: vincentkoc |
| [#87838](https://github.com/openclaw/openclaw/pull/87838) | 0 | Local model runtime | test(agents): include Ollama in small live model matrix |
| [#87818](https://github.com/openclaw/openclaw/pull/87818) | 0 | Local model runtime | fix(ollama): yield during dense stream processing |
| [#87705](https://github.com/openclaw/openclaw/pull/87705) | 5 | Local model runtime | fix(agents): make subagent-control timeout configurable |
| [#87697](https://github.com/openclaw/openclaw/pull/87697) | 0 | Model routing/config | fix(auth): clear stale provider cooldowns after reauth |
| [#87694](https://github.com/openclaw/openclaw/pull/87694) | 5 | Model routing/config | fix(auth): tighten billing cooldown defaults to recover from multi-hour lockouts (#70903) |
| [#87628](https://github.com/openclaw/openclaw/pull/87628) | 15 | Model routing/config | feat(agents): inherit requester model for subagents |
| [#87619](https://github.com/openclaw/openclaw/pull/87619) | 5 | Local model runtime | fix(diagnostics): account stream deltas incrementally |
| [#87617](https://github.com/openclaw/openclaw/pull/87617) | 5 | Local model runtime | fix(agents): broaden local model lean profile |
| [#87596](https://github.com/openclaw/openclaw/pull/87596) | 0 | Open-weight/provider behavior | fix(moonshot): rewrite duplicate native Kimi tool_call ids on replay |
| [#87587](https://github.com/openclaw/openclaw/pull/87587) | 0 | Local model runtime | fix(agents): keep exec visible for lean local models |
| [#87572](https://github.com/openclaw/openclaw/pull/87572) | 4 | Local memory/embedding | fix(memory): increase QMD embedTimeoutMs default to 600s for local GGUF |
| [#87562](https://github.com/openclaw/openclaw/pull/87562) | 0 | Open-weight/provider behavior | fix(openrouter): reconcile streamed cost with /generation total_cost |
| [#87558](https://github.com/openclaw/openclaw/pull/87558) | 0 | Local model runtime | test(gateway): add Ollama dense stream repro |
| [#87538](https://github.com/openclaw/openclaw/pull/87538) | 4 | Model routing/config | fix(agents): model-scope cooldown for transport timeout (#87462) |
| [#87484](https://github.com/openclaw/openclaw/pull/87484) | 8 | Model routing/config | fix(agents): clear legacy auto fallback pins |
| [#87480](https://github.com/openclaw/openclaw/pull/87480) | 4 | Model routing/config | fix(anthropic): configure undici Agent with extended keep-alive to prevent socket failures |
| [#87414](https://github.com/openclaw/openclaw/pull/87414) | 0 | Local model runtime | [codex] Key llama.cpp sessions for local reuse |
| [#87404](https://github.com/openclaw/openclaw/pull/87404) | 9 | Model routing/config | fix(agents): honor ACP alias model.primary overrides (Fixes #87381) |
| [#87393](https://github.com/openclaw/openclaw/pull/87393) | 8 | Local/media model provider | fix(media): suppress local whisper progress transcripts |
| [#87343](https://github.com/openclaw/openclaw/pull/87343) | 0 | Model routing/config | feat(cron): surface fallback progress |
| [#87300](https://github.com/openclaw/openclaw/pull/87300) | 8 | Model routing/config | feat: group model select with collapsible panel in Control UI |
| [#87296](https://github.com/openclaw/openclaw/pull/87296) | 5 | Model routing/config | feat: group model select with collapsible panel in Control UI |
| [#87247](https://github.com/openclaw/openclaw/pull/87247) | 12 | Local memory/embedding | docs: note LanceDB dreaming v0.2.3 via memory-lancedb-dreaming plugin |
| [#86776](https://github.com/openclaw/openclaw/pull/86776) | 0 | Model routing/config | fix(models): apply provider policy defaults to inline models |
| [#86637](https://github.com/openclaw/openclaw/pull/86637) | 1 | Open-weight/provider behavior | fix(agents): recover tool calls from DeepSeek DSML text markup |
| [#86564](https://github.com/openclaw/openclaw/pull/86564) | 9 | Model/provider behavior | fix(gateway): disable provider auth prewarm by default |
| [#86554](https://github.com/openclaw/openclaw/pull/86554) | 8 | OpenAI-compatible/proxy | fix(agents): add missing DeepSeek V4 proxy models to reasoning_content replay set |
| [#86551](https://github.com/openclaw/openclaw/pull/86551) | 4 | OpenAI-compatible/proxy | fix(agents): add missing DeepSeek V4 proxy models to reasoning_content replay set |
| [#85931](https://github.com/openclaw/openclaw/pull/85931) | 4 | Local memory/embedding | fix(memory): serialize qmd update writes across processes to stop SQLITE_BUSY |
| [#84977](https://github.com/openclaw/openclaw/pull/84977) | 9 | Local model runtime | feat: handle gemma 4 format tool call |
| [#84581](https://github.com/openclaw/openclaw/pull/84581) | 17 | OpenAI-compatible/proxy | fix(agents): strip plaintext model provider keys |
| [#84554](https://github.com/openclaw/openclaw/pull/84554) | 0 | Local memory/embedding | fix(memory-core): guard builtin fallback after qmd failures |
| [#84228](https://github.com/openclaw/openclaw/pull/84228) | 4 | Open-weight/provider behavior | fix(nvidia): update Nemotron 3 Super contextWindow to 1M per NVIDIA spec |
| [#84072](https://github.com/openclaw/openclaw/pull/84072) | 0 | Model routing/config | Add model fallback circuit breaker |
| [#83436](https://github.com/openclaw/openclaw/pull/83436) | 0 | Model routing/config | fix(agents): rethrow EmbeddedAttemptSessionTakeoverError before model fallback |
| [#83227](https://github.com/openclaw/openclaw/pull/83227) | 4 | OpenAI-compatible/proxy | fix(openai): mark mp3 TTS voice output compatible |
| [#83213](https://github.com/openclaw/openclaw/pull/83213) | 0 | Model routing/config | fix(gateway): clear live model switch on reset |
| [#82557](https://github.com/openclaw/openclaw/pull/82557) | 0 | Model routing/config | Allow onboarding to configure multiple model providers |
| [#82145](https://github.com/openclaw/openclaw/pull/82145) | 0 | Local model runtime | cron: allow retries for local model preflight |
| [#81834](https://github.com/openclaw/openclaw/pull/81834) | 13 | Local/media model provider | feat(senseaudio): add SenseAudio TTS provider |
| [#81443](https://github.com/openclaw/openclaw/pull/81443) | 11 | Local memory/embedding | fix: resolve QMD Windows shims and guard image URL downloads |
| [#81170](https://github.com/openclaw/openclaw/pull/81170) | 4 | Local memory/embedding | fix(openai): preserve custom provider id through memory embedding adapter |
| [#80957](https://github.com/openclaw/openclaw/pull/80957) | 0 | OpenAI-compatible/proxy | fix: refresh status context window after model switch |
| [#80947](https://github.com/openclaw/openclaw/pull/80947) | 4 | Local memory/embedding | fix(doctor): warn and document QMD session recall gates |
| [#80418](https://github.com/openclaw/openclaw/pull/80418) | 0 | OpenAI-compatible/proxy | fix(/v1/responses): accept text field on requests for OpenAI SDK 6.x parity |
| [#80033](https://github.com/openclaw/openclaw/pull/80033) | 0 | Open-weight/provider behavior | fix(opencode-go): add supportedReasoningEfforts to DeepSeek V4 model entries |
| [#79745](https://github.com/openclaw/openclaw/pull/79745) | 14 | Local memory/embedding | Memory/QMD: isolate mcporter sidecars per agent |
| [#79185](https://github.com/openclaw/openclaw/pull/79185) | 0 | Open-weight/provider behavior | fix(tts/xiaomi): support Token Plan TTS endpoint |
| [#78747](https://github.com/openclaw/openclaw/pull/78747) | 10 | Model/provider behavior | fix(cache): emit `tools` before `input` in OpenAI Responses request body for prefix-cache stability |
| [#78085](https://github.com/openclaw/openclaw/pull/78085) | 5 | OpenAI-compatible/proxy | fix(agents): parse prompt_tokens/completion_tokens in CLI usage for llama.cpp compatibility (#77992) |
| [#77339](https://github.com/openclaw/openclaw/pull/77339) | 11 | Model routing/config | fix(auto-reply): clear runtime model cache on reset |
| [#77158](https://github.com/openclaw/openclaw/pull/77158) | 12 | Local memory/embedding | perf(qmd): persistent export-state cache + stat fast path in exportSessions |
| [#77053](https://github.com/openclaw/openclaw/pull/77053) | 7 | OpenAI-compatible/proxy | feat(lmstudio): opt-in idle TTL via native load API |
| [#76928](https://github.com/openclaw/openclaw/pull/76928) | 7 | Model routing/config | feat(plugins): let hooks prefer auth profiles |
| [#76741](https://github.com/openclaw/openclaw/pull/76741) | 8 | Open-weight/provider behavior | fix(kimi): strip anthropic cache markers |
| [#76002](https://github.com/openclaw/openclaw/pull/76002) | 4 | OpenAI-compatible/proxy | fix(kimi): switch to openai-completions endpoint for image support |
| [#75860](https://github.com/openclaw/openclaw/pull/75860) | 4 | Local memory/embedding | fix(memory): improve QMD recall for channel queries |
| [#75350](https://github.com/openclaw/openclaw/pull/75350) | 4 | Open-weight/provider behavior | fix(deepseek): strip reasoning_content from input messages when thinking is enabled |
| [#75274](https://github.com/openclaw/openclaw/pull/75274) | 0 | Local model runtime | fix(ollama): per-request URL routing for multi-provider setups |
| [#75270](https://github.com/openclaw/openclaw/pull/75270) | 8 | OpenAI-compatible/proxy | fix(agent): prevent sticky model fallback |
| [#75267](https://github.com/openclaw/openclaw/pull/75267) | 0 | Model routing/config | Fix model picker alias/provider scoped options |
| [#75075](https://github.com/openclaw/openclaw/pull/75075) | 6 | OpenAI-compatible/proxy | feat(gateway): surface built-in tool calls as function_call output items on /v1/responses |
| [#74761](https://github.com/openclaw/openclaw/pull/74761) | 2 | Local memory/embedding | docs: Document oMLX (Apple Silicon MLX) as memorySearch embedding provider |
| [#74403](https://github.com/openclaw/openclaw/pull/74403) | 5 | Open-weight/provider behavior | fix(deepseek): strip reasoning_content when extra_body disables thinking |
| [#74185](https://github.com/openclaw/openclaw/pull/74185) | 5 | Model/provider behavior | fix(infra): wrap provider auth resolution in timeout for status --usage --json |
| [#73817](https://github.com/openclaw/openclaw/pull/73817) | 2 | OpenAI-compatible/proxy | fix(media): allow private openai compatible audio transcription endpoints |
| [#73667](https://github.com/openclaw/openclaw/pull/73667) | 1 | Local memory/embedding | Bound active-memory recall latency and jitter QMD startup |
| [#73594](https://github.com/openclaw/openclaw/pull/73594) | 5 | Open-weight/provider behavior | feat(openrouter): inject cache_control for closed-source qwen models |
| [#73512](https://github.com/openclaw/openclaw/pull/73512) | 8 | Local memory/embedding | fix(memory): schedule qmd embed when embedInterval is configured regardless of searchMode |
| [#72537](https://github.com/openclaw/openclaw/pull/72537) | 4 | Local memory/embedding | fix(tts): honor provider timeoutMs in chat synthesis |
| [#71678](https://github.com/openclaw/openclaw/pull/71678) | 5 | Local memory/embedding | Fix: Issue 71522 memory embeddings |
| [#71062](https://github.com/openclaw/openclaw/pull/71062) | 9 | OpenAI-compatible/proxy | fix(/v1/responses): drop the extra phantom assistant turn on client-tool calls |
| [#70739](https://github.com/openclaw/openclaw/pull/70739) | 9 | OpenAI-compatible/proxy | fix(gateway): add SSE heartbeat to keep /v1/responses and /v1/chat/completions streams alive through idle-timeout proxies |
| [#70647](https://github.com/openclaw/openclaw/pull/70647) | 0 | Open-weight/provider behavior | test(agents): pin empty-turn coverage for non-strict-agentic nemotron |
| [#70596](https://github.com/openclaw/openclaw/pull/70596) | 9 | Local memory/embedding | perf(memory): prewarm explicit local embeddings on gateway startup |
| [#69729](https://github.com/openclaw/openclaw/pull/69729) | 0 | OpenAI-compatible/proxy | fix(qwen): enable qwen3.6-plus on Coding Plan CN, correct reasoning flag |
| [#69495](https://github.com/openclaw/openclaw/pull/69495) | 0 | Model routing/config | feat(heartbeat): support model fallbacks via {primary,fallbacks} (#69434) |
| [#69245](https://github.com/openclaw/openclaw/pull/69245) | 0 | OpenAI-compatible/proxy | feat: enable cache-ttl context pruning for openai-completions providers |
| [#68996](https://github.com/openclaw/openclaw/pull/68996) | 4 | OpenAI-compatible/proxy | fix(google): route Gemma models through native Generative AI API |
| [#68975](https://github.com/openclaw/openclaw/pull/68975) | 0 | Local memory/embedding | feat(memory): switch default local embedding model to bge-m3 Q8_0 AI-assisted |
| [#68725](https://github.com/openclaw/openclaw/pull/68725) | 9 | OpenAI-compatible/proxy | feat(amazon-bedrock-mantle): add known context windows for open-weight Mantle models |
| [#68590](https://github.com/openclaw/openclaw/pull/68590) | 0 | Local memory/embedding | fix(memory-core): rewrite qmd index on managed collection repair |
| [#68435](https://github.com/openclaw/openclaw/pull/68435) | 0 | OpenAI-compatible/proxy | feat(gateway): accept audio/file content blocks in /v1/chat/completions |
| [#68079](https://github.com/openclaw/openclaw/pull/68079) | 11 | OpenAI-compatible/proxy | feat(providers/zai): inject X-Session-Id header for prompt cache stickiness |
| [#67008](https://github.com/openclaw/openclaw/pull/67008) | 8 | Open-weight/provider behavior | feat(chutes): add zai-org/GLM-5.1-TEE to static model catalog |
| [#65914](https://github.com/openclaw/openclaw/pull/65914) | 17 | Local memory/embedding | fix(memory): respect qmd status timeout and skip checkpoint exports |
| [#65547](https://github.com/openclaw/openclaw/pull/65547) | 0 | Local memory/embedding | test(memory-qmd): verify extraCollections pattern reaches qmd collection add CLI args |
| [#65423](https://github.com/openclaw/openclaw/pull/65423) | 0 | Model routing/config | feat(agents): shuffle auth profile candidates for subagent runs |
| [#65180](https://github.com/openclaw/openclaw/pull/65180) | 0 | Local model runtime | fix(cli,sessions): make local model run stateless by default and keep transcript fallback profile-scoped |
| [#64335](https://github.com/openclaw/openclaw/pull/64335) | 0 | Open-weight/provider behavior | fix(zai): rotate env-backed API keys on rate limit |
| [#62733](https://github.com/openclaw/openclaw/pull/62733) | 0 | Local memory/embedding | Fix local memory embedding VRAM fallback and logging file resolution |
| [#62710](https://github.com/openclaw/openclaw/pull/62710) | 0 | Model routing/config | fix(auth): stop new sessions inheriting auto-selected auth profile overrides |
| [#61187](https://github.com/openclaw/openclaw/pull/61187) | 5 | Open-weight/provider behavior | fix(kimi, moonshot): model picker shows wrong models |
| [#59208](https://github.com/openclaw/openclaw/pull/59208) | 16 | Model routing/config | fix(status): honor selected usage auth profile<br>Assignee: vincentkoc |
| [#58434](https://github.com/openclaw/openclaw/pull/58434) | 4 | OpenAI-compatible/proxy | feat(openresponses): add per-request tool_deny override to /v1/responses |
| [#58405](https://github.com/openclaw/openclaw/pull/58405) | 0 | OpenAI-compatible/proxy | feat(openresponses): add per-request skills override to /v1/responses |
| [#56674](https://github.com/openclaw/openclaw/pull/56674) | 17 | OpenAI-compatible/proxy | feat(openresponses): return reasoning/thinking content in /v1/responses output |
| [#55477](https://github.com/openclaw/openclaw/pull/55477) | 0 | OpenAI-compatible/proxy | feat: stamp session_key, message_channel, context_limit into LiteLLM request metadata |
| [#50051](https://github.com/openclaw/openclaw/pull/50051) | 12 | Local/media model provider | feat(macos): ExecuTorch Parakeet-TDT STT for Talk Mode + model-plugin runtime |

## RECENTLY CLOSED OR REMOVED FROM OPEN INVENTORY

These were in earlier local-model notes or candidate pools but are not counted as live-open retained threads now.

<details>
<summary>Recently closed or removed threads (111)</summary>

| Thread | Status checked | Note |
| --- | --- | --- |
| [#88781](https://github.com/openclaw/openclaw/pull/88781) | Closed in local gitcrawl 2026-06-01 | fix(models): strip remaining provider self prefixes; no longer open. |
| [#88770](https://github.com/openclaw/openclaw/issues/88770) | Closed in local gitcrawl 2026-06-01 | [Bug]: Self-prefix normalization gap remaining in google/xai/openai providers after #88587; no longer open. |
| [#88761](https://github.com/openclaw/openclaw/pull/88761) | Closed in local gitcrawl 2026-06-01 | [codex] Surface disabled Codex plugin routes in doctor lint; no longer open. |
| [#88759](https://github.com/openclaw/openclaw/pull/88759) | Closed in local gitcrawl 2026-06-01 | fix: repair providerless Codex session overrides; no longer open. |
| [#88751](https://github.com/openclaw/openclaw/issues/88751) | Closed in local gitcrawl 2026-06-01 | [Bug]: doctor lint misses disabled codex plugin required by native codex runtime; no longer open. |
| [#88745](https://github.com/openclaw/openclaw/pull/88745) | Closed in local gitcrawl 2026-06-01 | fix: preserve explicit provider in resolveConfiguredProviderFallback (v2); no longer open. |
| [#88719](https://github.com/openclaw/openclaw/pull/88719) | Closed in local gitcrawl 2026-06-01 | fix(auth): enforce canonical openai-codex OAuth owner; no longer open. |
| [#88715](https://github.com/openclaw/openclaw/pull/88715) | Closed in local gitcrawl 2026-06-01 | perf(plugins): avoid duplicate provider hook load probes; no longer open. |
| [#88711](https://github.com/openclaw/openclaw/pull/88711) | Closed in local gitcrawl 2026-06-01 | fix: preserve explicit provider in resolveConfiguredProviderFallback; no longer open. |
| [#88710](https://github.com/openclaw/openclaw/issues/88710) | Closed in local gitcrawl 2026-06-01 | Bug: resolveConfiguredProviderFallback replaces explicit provider/model with wrong provider when default provider is unconfigured; no longer open. |
| [#88708](https://github.com/openclaw/openclaw/issues/88708) | Closed in local gitcrawl 2026-06-01 | memory-tencentdb OpenAI-compatible prompt cache regression; no longer open. |
| [#88693](https://github.com/openclaw/openclaw/pull/88693) | Closed in local gitcrawl 2026-06-01 | docs(openai): clarify openai-codex auth profile mismatch; no longer open. |
| [#88672](https://github.com/openclaw/openclaw/pull/88672) | Closed in local gitcrawl 2026-06-01 | fix(plugins): reuse current metadata snapshot in provider hot paths; no longer open. |
| [#88669](https://github.com/openclaw/openclaw/pull/88669) | Closed in local gitcrawl 2026-06-01 | fix(auth): skip no-op auth-profile disk writes on success; no longer open. |
| [#88667](https://github.com/openclaw/openclaw/pull/88667) | Closed in local gitcrawl 2026-06-01 | fix #81214: OpenClaw 2026.5.7 subagent regression; no longer open. |
| [#88654](https://github.com/openclaw/openclaw/issues/88654) | Closed in local gitcrawl 2026-06-01 | markAuthProfileSuccess rewrites auth-profiles.json on every success; no longer open. |
| [#88644](https://github.com/openclaw/openclaw/issues/88644) | Closed in local gitcrawl 2026-06-01 | doctor --fix breaks Codex model routing by rewriting openai-codex/ to openai/; no longer open. |
| [#88612](https://github.com/openclaw/openclaw/pull/88612) | Closed in local gitcrawl 2026-06-01 | fix(models): keep auth login out of main config; no longer open. |
| [#88587](https://github.com/openclaw/openclaw/pull/88587) | Closed in local gitcrawl 2026-06-01 | fix(agents): normalize prefixed Anthropic fallback model ids (#88560); no longer open. |
| [#88565](https://github.com/openclaw/openclaw/issues/88565) | Closed in local gitcrawl 2026-06-01 | models auth login overwrites and truncates main openclaw.json; no longer open. |
| [#88563](https://github.com/openclaw/openclaw/pull/88563) | Closed in local gitcrawl 2026-06-01 | fix(agents): resolve exact static-catalog models for plugin-harness cold start (#88510); no longer open. |
| [#88560](https://github.com/openclaw/openclaw/issues/88560) | Closed in local gitcrawl 2026-06-01 | fallback iterator leaks one candidate modelId into subsequent provider lookup; no longer open. |
| [#88558](https://github.com/openclaw/openclaw/pull/88558) | Closed in local gitcrawl 2026-06-01 | fix(gateway): enforce OpenAI tool_choice required/function contracts; no longer open. |
| [#88547](https://github.com/openclaw/openclaw/pull/88547) | Closed in local gitcrawl 2026-06-01 | feat(github-copilot): add Claude Opus 4.8 to default model catalog; no longer open. |
| [#88525](https://github.com/openclaw/openclaw/pull/88525) | Closed in local gitcrawl 2026-06-01 | feat(deepseek): show provider balance in usage status; no longer open. |
| [#88517](https://github.com/openclaw/openclaw/issues/88517) | Closed in local gitcrawl 2026-06-01 | v2026.5.28 regression: claude-haiku-4-5 cron model override fails again; no longer open. |
| [#88516](https://github.com/openclaw/openclaw/pull/88516) | Closed in local gitcrawl 2026-06-01 | fix(doctor): preserve Codex routes in non-interactive repair; no longer open. |
| [#88510](https://github.com/openclaw/openclaw/issues/88510) | Closed in local gitcrawl 2026-06-01 | Codex model catalog cold-start miss for gpt-5.3-codex after gateway restart; no longer open. |
| [#88275](https://github.com/openclaw/openclaw/pull/88275) | Closed in local gitcrawl 2026-05-31 | fix(models-config): allow self-hosted providers without apiKey in models.json (#88267); no longer open. |
| [#88266](https://github.com/openclaw/openclaw/pull/88266) | Closed in local gitcrawl 2026-05-31 | refactor: extract model catalog core package; no longer open. |
| [#88247](https://github.com/openclaw/openclaw/pull/88247) | Closed in local gitcrawl 2026-05-31 | feat: add hosted model providers; no longer open. |
| [#88237](https://github.com/openclaw/openclaw/pull/88237) | Closed in local gitcrawl 2026-05-31 | fix(agents): preserve qualified model alias targets; no longer open. |
| [#88232](https://github.com/openclaw/openclaw/pull/88232) | Closed in local gitcrawl 2026-05-31 | fix(models): prefer exact configured provider refs before aliases; no longer open. |
| [#88218](https://github.com/openclaw/openclaw/issues/88218) | Closed in local gitcrawl 2026-05-31 | [Bug]: agents.defaults.models aliases silently re-resolve target refs to openai/<alias-key> on 5.x; no longer open. |
| [#88145](https://github.com/openclaw/openclaw/pull/88145) | Closed in local gitcrawl 2026-05-31 | feat: add Hermes provider parity for hosted models; no longer open. |
| [#88135](https://github.com/openclaw/openclaw/pull/88135) | Closed in local gitcrawl 2026-05-31 | fix(codex): refresh stale managed runtime plugin; no longer open. |
| [#88130](https://github.com/openclaw/openclaw/pull/88130) | Closed in local gitcrawl 2026-05-31 | fix(agents): preserve Codex auth for compaction fallback; no longer open. |
| [#88120](https://github.com/openclaw/openclaw/issues/88120) | Closed live 2026-05-30 | [Bug]: 2026.5.27 upgrade leaves stale Codex plugin providerIds, breaking openai/gpt-5.5 route and status usage workaround; no longer open. |
| [#88110](https://github.com/openclaw/openclaw/pull/88110) | Closed in local gitcrawl 2026-05-31 | fix(session): normalize codex oauth session routes; no longer open. |
| [#88102](https://github.com/openclaw/openclaw/issues/88102) | Closed in local gitcrawl 2026-05-31 | [Bug]: 2026.5.27 Codex runtime rejects openai/gpt-5.5; codex/gpt-5.5 workaround drops Telegram /status usage; no longer open. |
| [#88091](https://github.com/openclaw/openclaw/issues/88091) | Closed in local gitcrawl 2026-05-31 | Guard MiniMax OAuth fetches in bundled plugin runtime; no longer open. |
| [#88086](https://github.com/openclaw/openclaw/pull/88086) | Closed in local gitcrawl 2026-05-31 | fix(minimax): guard oauth fetches; no longer open. |
| [#88072](https://github.com/openclaw/openclaw/pull/88072) | Closed in local gitcrawl 2026-05-31 | fix(agents): classify expired thinking signatures; no longer open. |
| [#88067](https://github.com/openclaw/openclaw/pull/88067) | Closed in local gitcrawl 2026-05-31 | fix(responses): drop orphaned assistant msg_* id when reasoning is dropped (#88019); no longer open. |
| [#88065](https://github.com/openclaw/openclaw/issues/88065) | Closed in local gitcrawl 2026-05-31 | Gateway crash on exit: SIGABRT in ggml_metal_rsets_free (node-llama-cpp Metal backend); no longer open. |
| [#88019](https://github.com/openclaw/openclaw/issues/88019) | Closed in local gitcrawl 2026-05-31 | [Bug]: Azure Responses session replay keeps msg id without required reasoning after fallback; no longer open. |
| [#87963](https://github.com/openclaw/openclaw/pull/87963) | Closed in local gitcrawl 2026-05-31 | fix(agents): downgrade thinking blocks with empty signatures to text before anthropic-messages replay; no longer open. |
| [#87935](https://github.com/openclaw/openclaw/issues/87935) | Closed in local gitcrawl 2026-05-31 | feat: Add Xiaomi MiMo Web Search provider; no longer open. |
| [#87920](https://github.com/openclaw/openclaw/pull/87920) | Closed in local gitcrawl 2026-05-31 | feat(gateway): forward OpenAI stop sequences through chat completions; no longer open. |
| [#87877](https://github.com/openclaw/openclaw/issues/87877) | Closed in local gitcrawl 2026-05-31 | Codex runtime persists openai-codex as session modelProvider, causing recurring legacy route doctor warning; no longer open. |
| [#87862](https://github.com/openclaw/openclaw/pull/87862) | Closed in local gitcrawl 2026-05-31 | Add Claude Opus 4.8 defaults; no longer open. |
| [#87851](https://github.com/openclaw/openclaw/pull/87851) | Closed in local gitcrawl 2026-05-31 | fix(agents): preserve logical OpenAI session routes; no longer open. |
| [#87835](https://github.com/openclaw/openclaw/pull/87835) | Closed in local gitcrawl 2026-05-31 | fix(agents): add opus-4-8 to adaptive thinking allowlist; no longer open. |
| [#87833](https://github.com/openclaw/openclaw/pull/87833) | Closed in local gitcrawl 2026-05-31 | fix: probe stale rate-limit cooldown primaries; no longer open. |
| [#87819](https://github.com/openclaw/openclaw/pull/87819) | Closed in local gitcrawl 2026-05-31 | fix: remove reset hint from pinned model status; no longer open. |
| [#87802](https://github.com/openclaw/openclaw/pull/87802) | Closed in local gitcrawl 2026-05-31 | feat(opencode): add resolveDynamicModel and augmentModelCatalog hooks to Zen plugin; no longer open. |
| [#87794](https://github.com/openclaw/openclaw/pull/87794) | Closed in local gitcrawl 2026-05-31 | refactor(tts): catalog voice models through providers; no longer open. |
| [#87762](https://github.com/openclaw/openclaw/pull/87762) | Closed in local gitcrawl 2026-05-31 | feat(opencode): support separate Zen and Go API key env vars; no longer open. |
| [#87719](https://github.com/openclaw/openclaw/pull/87719) | Closed in local gitcrawl 2026-05-29 | fix(anthropic): stop migrating current claude-haiku-4-5 to sonnet; no longer open. |
| [#87675](https://github.com/openclaw/openclaw/pull/87675) | Closed in local gitcrawl 2026-05-29 | fix(ollama): promote plain text tool calls; no longer open. |
| [#87641](https://github.com/openclaw/openclaw/issues/87641) | Closed in local gitcrawl 2026-05-31 | `opencode-go/kimi-k2.6`: every multi-turn task rejected with opaque 400 "Provider returned error" (reason=format), rotates to fallback (2026.5.26+5.27); no longer open. |
| [#87638](https://github.com/openclaw/openclaw/pull/87638) | Closed in local gitcrawl 2026-05-29 | test(agents): add small model live profile; no longer open. |
| [#87621](https://github.com/openclaw/openclaw/pull/87621) | Closed in local gitcrawl 2026-05-29 | fix(ollama): yield during dense ndjson bursts; no longer open. |
| [#87608](https://github.com/openclaw/openclaw/issues/87608) | Closed in local gitcrawl 2026-05-31 | [Bug] Ollama Cloud rate-limit cooldown permanently blocks agents — not released after API recovery; no longer open. |
| [#87606](https://github.com/openclaw/openclaw/pull/87606) | Closed in local gitcrawl 2026-05-29 | fix(active-memory): raise recall timeout ceiling; no longer open. |
| [#87594](https://github.com/openclaw/openclaw/pull/87594) | Closed in local gitcrawl 2026-05-29 | fix(openrouter): apply strict9 tool_call_id sanitisation for Mistral routes; no longer open. |
| [#87593](https://github.com/openclaw/openclaw/pull/87593) | Closed in local gitcrawl 2026-05-29 | fix(agents): preserve reasoning_content replay across DeepSeek tier suffixes; no longer open. |
| [#87575](https://github.com/openclaw/openclaw/issues/87575) | Closed in local gitcrawl 2026-05-29 | Bug: DeepSeek V4 Flash Free via OpenCode Zen provider fails with 400 on follow-up API calls; no longer open. |
| [#87463](https://github.com/openclaw/openclaw/pull/87463) | Closed in local gitcrawl 2026-05-31 | fix(session): normalize openai-codex provider to openai for session route persistence; no longer open. |
| [#87456](https://github.com/openclaw/openclaw/pull/87456) | Closed in local gitcrawl 2026-05-29 | Restore Codex Spark OAuth routes; no longer open. |
| [#87436](https://github.com/openclaw/openclaw/issues/87436) | Closed in local gitcrawl 2026-05-31 | Codex harness runs recreate legacy openai-codex session route state after doctor --fix; no longer open. |
| [#87416](https://github.com/openclaw/openclaw/pull/87416) | Closed in local gitcrawl 2026-05-29 | fix(agents): resolve Codex runtime models first; no longer open. |
| [#87274](https://github.com/openclaw/openclaw/pull/87274) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor OpenAI-compatible cache retention; no longer open. |
| [#87252](https://github.com/openclaw/openclaw/pull/87252) | Closed in local gitcrawl 2026-05-28 | fix(agents): use runtime alias equivalence in live model switch comparison; no longer open. |
| [#87225](https://github.com/openclaw/openclaw/pull/87225) | Closed in local gitcrawl 2026-05-28 | fix(memory): salvage qmd search JSON after nonzero exit; no longer open. |
| [#86765](https://github.com/openclaw/openclaw/pull/86765) | Closed in local gitcrawl 2026-05-28 | [codex] Fix memory close sync race; no longer open. |
| [#86748](https://github.com/openclaw/openclaw/pull/86748) | Closed in local gitcrawl 2026-05-28 | perf(plugins): resolve provider policy from current snapshot first; no longer open. |
| [#86702](https://github.com/openclaw/openclaw/issues/86702) | Closed in local gitcrawl 2026-05-28 | MemoryIndexManager.close() races with in-flight sync — provider/DB closed before sync settles; no longer open. |
| [#86690](https://github.com/openclaw/openclaw/pull/86690) | Closed in local gitcrawl 2026-05-28 | fix(plugin-sdk): preserve string-const unions as flat enum for deepseek tool schemas; no longer open. |
| [#86689](https://github.com/openclaw/openclaw/pull/86689) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor per-agent thinking defaults for ingress runs; no longer open. |
| [#86669](https://github.com/openclaw/openclaw/issues/86669) | Closed in local gitcrawl 2026-05-28 | [Bug]: openclaw openai-compat /v1/chat/completions strips chat_template_kwargs entirely on vLLM/Nemotron — causes reasoning-only death-spiral; no longer open. |
| [#86644](https://github.com/openclaw/openclaw/pull/86644) | Closed in local gitcrawl 2026-05-28 | fix(models): skip wildcard catalog aliases; no longer open. |
| [#86633](https://github.com/openclaw/openclaw/pull/86633) | Closed in local gitcrawl 2026-05-31 | fix(ollama): yield during dense stream processing; no longer open. |
| [#86613](https://github.com/openclaw/openclaw/issues/86613) | Closed in local gitcrawl 2026-05-28 | [Bug]: Every memory_search call leaks ~N FDs (one per .md file in workspace memory tree) on macOS; long-lived gateways degrade toward FD exhaustion; no longer open. |
| [#86552](https://github.com/openclaw/openclaw/pull/86552) | Closed in local gitcrawl 2026-05-28 | perf(agents): reuse manifest metadata during model resolution; no longer open. |
| [#86515](https://github.com/openclaw/openclaw/pull/86515) | Closed in local gitcrawl 2026-05-27 | Ollama/Kimi reasoning leak PR; no longer open. |
| [#86506](https://github.com/openclaw/openclaw/issues/86506) | Closed in local gitcrawl 2026-05-28 | [BUG] Auth pre-warming blocks event loop for 60-90s, causing cascading timeouts; no longer open. |
| [#86504](https://github.com/openclaw/openclaw/pull/86504) | Closed in local gitcrawl 2026-05-28 | fix(diagnostics): track model stream progress; no longer open. |
| [#86499](https://github.com/openclaw/openclaw/pull/86499) | Closed in local gitcrawl 2026-05-31 | fix: normalizeDeepSeekSchema collapses anyOf const unions to first variant; no longer open. |
| [#86497](https://github.com/openclaw/openclaw/pull/86497) | Closed in local gitcrawl 2026-05-27 | OpenAI chat payload PR; no longer open. |
| [#86474](https://github.com/openclaw/openclaw/pull/86474) | Closed in local gitcrawl 2026-05-28 | fix: preserve const union variants as enum in normalizeDeepSeekSchema; no longer open. |
| [#86473](https://github.com/openclaw/openclaw/pull/86473) | Closed in local gitcrawl 2026-05-28 | fix(plugin-sdk): preserve all const literals in anyOf unions for DeepSeek (#86468); no longer open. |
| [#86471](https://github.com/openclaw/openclaw/pull/86471) | Closed in local gitcrawl 2026-05-27 | DeepSeek const-union PR; no longer open. |
| [#86468](https://github.com/openclaw/openclaw/issues/86468) | Closed 2026-05-26 | DeepSeek schema issue from the heuristic pass; no longer open. |
| [#86443](https://github.com/openclaw/openclaw/pull/86443) | Closed in local gitcrawl 2026-05-28 | fix(runtime-llm): forward reasoning param in LlmCompleteParams; no longer open. |
| [#86409](https://github.com/openclaw/openclaw/pull/86409) | Closed in local gitcrawl 2026-05-27 | Provider tool-call stream wrapper PR; no longer open. |
| [#86281](https://github.com/openclaw/openclaw/pull/86281) | Closed in local gitcrawl 2026-05-29 | [Fix] Warm provider auth off main thread; no longer open. |
| [#86225](https://github.com/openclaw/openclaw/pull/86225) | Closed in local gitcrawl 2026-05-28 | fix(vllm): wire configured thinking params; no longer open. |
| [#86212](https://github.com/openclaw/openclaw/issues/86212) | Closed in local gitcrawl 2026-05-27 | Provider auth pre-warm event-loop issue; no longer open. |
| [#86181](https://github.com/openclaw/openclaw/pull/86181) | Closed in local gitcrawl 2026-05-28 | discord/picker: alpha-bucket select for >25 providers or models; no longer open. |
| [#86179](https://github.com/openclaw/openclaw/pull/86179) | Closed in local gitcrawl 2026-05-31 | feat:Add Xiaomi Token Plan provider support; no longer open. |
| [#86169](https://github.com/openclaw/openclaw/issues/86169) | Closed in local gitcrawl 2026-05-31 | [Feature]: Add Xiaomi MiMo Token Plan provider support / fix Token Plan connection; no longer open. |
| [#86151](https://github.com/openclaw/openclaw/issues/86151) | Closed in local gitcrawl 2026-05-27 | Gemini model-switch/catalog issue; no longer open. |
| [#86145](https://github.com/openclaw/openclaw/issues/86145) | Closed 2026-05-25 | Assigned to osolmaz before close. |
| [#86129](https://github.com/openclaw/openclaw/issues/86129) | Closed 2026-05-25 | Ollama/Kimi routing issue; assigned to osolmaz before close. |
| [#86065](https://github.com/openclaw/openclaw/issues/86065) | Closed in local gitcrawl 2026-05-29 | [Enhancement]: Increase or make configurable the Active Memory timeoutMs hard cap; no longer open. |
| [#86032](https://github.com/openclaw/openclaw/pull/86032) | Closed in local gitcrawl 2026-05-31 | fix(agents): recover DeepSeek DSML tool markup into synthetic tool calls; no longer open. |
| [#86003](https://github.com/openclaw/openclaw/pull/86003) | Closed in local gitcrawl 2026-05-28 | fix(gateway): add provider auth prewarm operator controls; no longer open. |
| [#85883](https://github.com/openclaw/openclaw/issues/85883) | Closed in local gitcrawl 2026-05-31 | openai-completions provider leaks channel-output JSON to channel (works correctly on ollama provider); no longer open. |
| [#85715](https://github.com/openclaw/openclaw/pull/85715) | Closed in local gitcrawl 2026-05-31 | feat(deepseek): parse leaked DSML tags into synthetic tool calls instead of dropping them; no longer open. |
| [#85269](https://github.com/openclaw/openclaw/pull/85269) | Closed in local gitcrawl 2026-05-28 | feat(openai): add generic OpenAI-compatible embeddings; no longer open. |
| [#85267](https://github.com/openclaw/openclaw/issues/85267) | Closed 2026-05-25 | Assigned to osolmaz before close. |
| [#85217](https://github.com/openclaw/openclaw/issues/85217) | Closed in local gitcrawl 2026-05-28 | [Bug]: QMD query mode unusable on macOS Apple Silicon — Metal GPU cleanup crash discards valid search results; no longer open. |
| [#85161](https://github.com/openclaw/openclaw/issues/85161) | Closed in local gitcrawl 2026-05-31 | [Bug]: valid tool call XML in LLM reasoning block is sometimes executed by gateway; no longer open. |
| [#85072](https://github.com/openclaw/openclaw/pull/85072) | Closed in local gitcrawl 2026-05-28 | Deprecate memory-specific embedding provider registration; no longer open. |
| [#84998](https://github.com/openclaw/openclaw/pull/84998) | Closed in local gitcrawl 2026-05-28 | feat(plugins): add OpenAI-compatible embedding provider; no longer open. |
| [#84991](https://github.com/openclaw/openclaw/pull/84991) | Closed in local gitcrawl 2026-05-28 | feat(memory-core): consume generic embedding providers; no longer open. |
| [#84621](https://github.com/openclaw/openclaw/pull/84621) | Closed in local gitcrawl 2026-05-29 | Fix Kimi tool-call rewriting stop reason handling; no longer open. |
| [#83461](https://github.com/openclaw/openclaw/issues/83461) | Not resolvable as live issue | Earlier notes referenced it, but live GitHub issue view did not resolve it as an open issue. |
| [#83107](https://github.com/openclaw/openclaw/issues/83107) | Closed in local gitcrawl 2026-05-31 | Model registry name matching is load-bearing — silent fallback to picker selection on registry miss (2026.5.12); no longer open. |
| [#82973](https://github.com/openclaw/openclaw/pull/82973) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor explicit cacheRetention for openai-completions providers; no longer open. |
| [#82887](https://github.com/openclaw/openclaw/pull/82887) | Closed in local gitcrawl 2026-05-31 | fix(cron): preflight model fallbacks before skip; no longer open. |
| [#81281](https://github.com/openclaw/openclaw/issues/81281) | Closed in local gitcrawl 2026-05-28 | [Bug]: OpenAI-completions prompt_cache_key regression — caching worked in 2026.3.x, broken in 2026.5.x; no longer open. |
| [#81249](https://github.com/openclaw/openclaw/issues/81249) | Closed 2026-05-24 | No longer counted as live-open. |
| [#80495](https://github.com/openclaw/openclaw/issues/80495) | Closed in local gitcrawl 2026-05-31 | [Bug]: LM Studio Provider Fails: Environment Variable Expansion + API Endpoint Mismatch; no longer open. |
| [#80476](https://github.com/openclaw/openclaw/issues/80476) | Closed in local gitcrawl 2026-05-28 | [Feature]: bundled openai-compatible embedding provider for self-hosted servers (llama.cpp, Ollama, vLLM, TGI, LocalAI); no longer open. |
| [#80379](https://github.com/openclaw/openclaw/issues/80379) | Closed in local gitcrawl 2026-05-28 | [Bug]: Tool result secret redaction mutates session history, breaking KV cache prefix matching for local LLM providers; no longer open. |
| [#80226](https://github.com/openclaw/openclaw/issues/80226) | Closed 2026-05-25 | No longer counted as live-open. |
| [#79329](https://github.com/openclaw/openclaw/issues/79329) | Closed in local gitcrawl 2026-05-31 | Cron model preflight skips entire run when local primary is unreachable, ignoring configured cloud fallbacks [AI]; no longer open. |
| [#77678](https://github.com/openclaw/openclaw/pull/77678) | Closed in local gitcrawl 2026-05-28 | fix(memory): don't report QMD embeddings as unavailable when searchMode=search; no longer open. |
| [#77655](https://github.com/openclaw/openclaw/issues/77655) | Closed in local gitcrawl 2026-05-31 | Model fallback chain interrupted by race condition — 6 fallback models configured but task terminates before all are tried; no longer open. |
| [#76654](https://github.com/openclaw/openclaw/issues/76654) | Closed in local gitcrawl 2026-05-31 | [webchat] Agent responses disappear after heartbeat tool calls (model-specific, MiMo V2 Pro); no longer open. |
| [#75720](https://github.com/openclaw/openclaw/issues/75720) | Closed in local gitcrawl 2026-05-28 | [Bug]: Auto-onboard / plugin presets unconditionally overwrite user-set agents.defaults.model.primary; no longer open. |
| [#75657](https://github.com/openclaw/openclaw/issues/75657) | Closed in local gitcrawl 2026-05-29 | fix: local GGUF embedding model warmup blocks Node.js event loop for minutes on startup; no longer open. |
| [#74644](https://github.com/openclaw/openclaw/issues/74644) | Closed in local gitcrawl 2026-05-31 | mediaUnderstandingProviders audio path hard-requires API key, breaking no-auth/local STT providers; no longer open. |
| [#74315](https://github.com/openclaw/openclaw/pull/74315) | Closed in local gitcrawl 2026-05-31 | fix(agents): remove kimi-coding from normalizeProviderId alias chain; no longer open. |
| [#65502](https://github.com/openclaw/openclaw/issues/65502) | Closed in local gitcrawl 2026-05-31 | feat(agents): resilient model fallback with retry + context-aware safe mode; no longer open. |
| [#58012](https://github.com/openclaw/openclaw/issues/58012) | Closed in local gitcrawl 2026-05-29 | strict9 tool-call-id regression for Mistral via proxy providers; no longer open. |
| [#48680](https://github.com/openclaw/openclaw/issues/48680) | Closed in local gitcrawl 2026-05-31 | [Bug] Model fallback treats HTTP 403 business rejection as 'candidate_succeeded', skipping remaining fallback models; no longer open. |

</details>

## REGENERATION NOTES

Do not regenerate this file by dumping keyword hits. The correct workflow is:

1. Verify Gitcrawl freshness and fetch live GitHub open issue/PR state.
2. Build a broad candidate pool from local/open-weight/provider terms.
3. Review every candidate for whether the actual problem or PR change is materially about local/open-weight/model-provider behavior.
4. Keep direct/material matches, drop incidental body mentions, and preserve closed/removed notable items in the collapsed details block above.
5. Recount rows and compare against the retained issue/PR number sets before committing.
6. Run `python3 scripts/sort_openclaw_onur_inventory.py` before committing so issue and PR tables stay newest-first by GitHub number.
