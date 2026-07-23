# OPENCLAW ONUR INVENTORY

Updated: 2026-07-23

Review watermark:

- Last reviewed through issue: #111969.
- Last reviewed through PR: #111964.
- Meaning: all GitHub issues and PRs at or below these numbers were considered for local-model and open-weight relevance; later numbers need review on the next run.

## NEW OPEN THREADS (50)

| Thread | Created | Activity | Area | Creator | Title |
| --- | --- | --- | --- | --- | --- |
| 📝&nbsp;[#111966](https://github.com/openclaw/openclaw/issues/111966) | 2026-07-20 | 0 | Model/provider behavior | @markcallow-jpg | Bug: `extractRawAssistantText()` flattens multi-segment assistant output with no delimiter |
| 🔀&nbsp;[#111964](https://github.com/openclaw/openclaw/pull/111964) | 2026-07-20 | 0 | Model routing/config | @dillona | fix(google): default web_search model to rolling alias, not retired gemini-2.5-flash |
| 📝&nbsp;[#111943](https://github.com/openclaw/openclaw/issues/111943) | 2026-07-20 | 0 | Model routing/config | @Zeus-Deus | [Feature]: Configurable model + reasoning effort for background "learning" subsystems |
| 📝&nbsp;[#111924](https://github.com/openclaw/openclaw/issues/111924) | 2026-07-20 | 0 | Model routing/config | @japr26 | [Feature]: Buscador/filtro en dropdown de modelos del Control UI |
| 📝&nbsp;[#111923](https://github.com/openclaw/openclaw/issues/111923) | 2026-07-20 | 0 | Local memory/embedding | @makominsk | Dreaming REM phase extracts junk topics (stop words, numbers, ranges) with no filter/config exposed |
| 🔀&nbsp;[#111901](https://github.com/openclaw/openclaw/pull/111901) | 2026-07-20 | 0 | Model/provider behavior | @Vicenteut | feat(plugin-runtime): support declarative tools and single-attempt completions |
| 🔀&nbsp;[#111899](https://github.com/openclaw/openclaw/pull/111899) | 2026-07-20 | 0 | Model routing/config | @xialonglee | fix(cli): block embedded fallback for gateway-accepted agent turns on transport error |
| 🔀&nbsp;[#111895](https://github.com/openclaw/openclaw/pull/111895) | 2026-07-20 | 0 | Open-weight/provider behavior | @xbrxr03 | fix(failover): classify provider finish_reason: error as server_error, not timeout |
| 🔀&nbsp;[#111894](https://github.com/openclaw/openclaw/pull/111894) | 2026-07-20 | 0 | Local/media model provider | @xbrxr03 | fix(openai): add handshakeTimeout to realtime voice WebSocket |
| 🔀&nbsp;[#111892](https://github.com/openclaw/openclaw/pull/111892) | 2026-07-20 | 0 | Model routing/config | @xbrxr03 | fix(compaction): skip preflight compaction when backend owns native compaction |
| 📝&nbsp;[#111889](https://github.com/openclaw/openclaw/issues/111889) | 2026-07-20 | 0 | Model/provider behavior | @Vicenteut | Plugin runtime: support declarative tools and single-attempt completions |
| 📝&nbsp;[#111886](https://github.com/openclaw/openclaw/issues/111886) | 2026-07-20 | 0 | Model routing/config | @Olivaryne | Compaction frees zero tokens when transcript estimates undershoot the context-usage trigger (firstKeptEntryId stuck at first entry) |
| 🔀&nbsp;[#111885](https://github.com/openclaw/openclaw/pull/111885) | 2026-07-20 | 0 | Model routing/config | @xbrxr03 | fix(config): add compaction.enabled to schema so users can disable auto-compaction |
| 📝&nbsp;[#111884](https://github.com/openclaw/openclaw/issues/111884) | 2026-07-20 | 0 | Model routing/config | @MontanaIrish | [Bug]: Regression of #67988 — model picker shows alias ("Opus"/"Sonnet") instead of versioned display name, now on Opus 4.8 / Sonnet 5 |
| 🔀&nbsp;[#111882](https://github.com/openclaw/openclaw/pull/111882) | 2026-07-20 | 0 | Open-weight/provider behavior | @xbrxr03 | fix(minimax): recognize coding-plan response shape with remaining-percent fields |
| 📝&nbsp;[#111879](https://github.com/openclaw/openclaw/issues/111879) | 2026-07-20 | 0 | Model/provider behavior | @shayshimon | [Bug]: Parallel Codex hook relays can exhaust gateway resources and block the control plane |
| 🔀&nbsp;[#111878](https://github.com/openclaw/openclaw/pull/111878) | 2026-07-20 | 0 | Open-weight/provider behavior | @xbrxr03 | fix(kimi-coding): remove k3[1m] from catalog, normalize to k3, raise context window |
| 🔀&nbsp;[#111872](https://github.com/openclaw/openclaw/pull/111872) | 2026-07-20 | 0 | Model/provider behavior | @Pick-cat | fix(amazon-bedrock): reject malformed inbound image base64 |
| 📝&nbsp;[#111870](https://github.com/openclaw/openclaw/issues/111870) | 2026-07-20 | 0 | Model/provider behavior | @Flagrare | [Bug]: @openclaw/codex fails to register in CLI context — TypeError: undefined 'openSyncKeyedStore' |
| 🔀&nbsp;[#111864](https://github.com/openclaw/openclaw/pull/111864) | 2026-07-20 | 0 | Model/provider behavior | @ooiuuii | fix(ai): trim replay tool call ids |
| 📝&nbsp;[#111863](https://github.com/openclaw/openclaw/issues/111863) | 2026-07-20 | 0 | Model/provider behavior | @ooiuuii | Provider replay mispairs tool results when call IDs contain surrounding whitespace |
| 📝&nbsp;[#111857](https://github.com/openclaw/openclaw/issues/111857) | 2026-07-20 | 0 | Model routing/config | @itanyplus | [Bug]: CLI budget reopens the full compacted JSONL branch, inflating prompt estimates and repeatedly compacting low-context parent sessions |
| 📝&nbsp;[#111856](https://github.com/openclaw/openclaw/issues/111856) | 2026-07-20 | 0 | Model routing/config | @nierob-cmd | Compaction summarization bypasses per-turn image-history pruning, can overflow context |
| 🔀&nbsp;[#111852](https://github.com/openclaw/openclaw/pull/111852) | 2026-07-20 | 0 | OpenAI-compatible/proxy | @chenyangjun-xy | fix: reject malformed UTF-8 in proxy gateway error response bodies |
| 📝&nbsp;[#111850](https://github.com/openclaw/openclaw/issues/111850) | 2026-07-20 | 0 | Local memory/embedding | @chrislro | stt-tts Talk: aborted active-memory pre-run surfaces as user-facing "voice config failed" |
| 📝&nbsp;[#111848](https://github.com/openclaw/openclaw/issues/111848) | 2026-07-20 | 0 | Model routing/config | @Enominera | [Bug]: acp-agent.js env construction missing settingsManager.getSettings().env — auto-compaction relies on gateway coincidence |
| 📝&nbsp;[#111846](https://github.com/openclaw/openclaw/issues/111846) | 2026-07-20 | 0 | Open-weight/provider behavior | @Enominera | Thinking block loop silently exhausts output tokens → session permanently unusable (976K tokens accumulated) |
| 🔀&nbsp;[#111845](https://github.com/openclaw/openclaw/pull/111845) | 2026-07-20 | 0 | Model/provider behavior | @dwc1997 | fix(codex): bound app-server websocket upgrade with handshake timeout |
| 🔀&nbsp;[#111841](https://github.com/openclaw/openclaw/pull/111841) | 2026-07-20 | 0 | Model routing/config | @xialonglee | fix(agents): allow configless gateway rebind to activate standalone owner |
| 📝&nbsp;[#111839](https://github.com/openclaw/openclaw/issues/111839) | 2026-07-20 | 0 | Model/provider behavior | @LeeroyDing | [Bug]: Channel follow-ups never steer active Codex app-server runs — steer always rejected (transcript_commit_wait_unsupported) and queued as follow-ups, unlike /steer and message-tool paths |
| 🔀&nbsp;[#111835](https://github.com/openclaw/openclaw/pull/111835) | 2026-07-20 | 0 | Local model runtime | @masatohoshino | fix(ollama): bound DNS preflight with guard-owned request timeouts |
| 📝&nbsp;[#111827](https://github.com/openclaw/openclaw/issues/111827) | 2026-07-20 | 0 | Model routing/config | @maharrer79-ops | Codex (openai-codex) provider: newer models report "Unknown model" + OAuth refresh_token_reused token race |
| 🔀&nbsp;[#111826](https://github.com/openclaw/openclaw/pull/111826) | 2026-07-20 | 0 | Model routing/config | @Zeus-Deus | fix: /think off does not disable thinking on claude-cli |
| 🔀&nbsp;[#111825](https://github.com/openclaw/openclaw/pull/111825) | 2026-07-20 | 0 | OpenAI-compatible/proxy | @wuqxuan | fix(agents): tools-disabled finalizer after blank post-tool stop |
| 🔀&nbsp;[#111818](https://github.com/openclaw/openclaw/pull/111818) | 2026-07-20 | 0 | OpenAI-compatible/proxy | @ooiuuii | fix(openai): fail fast on invalid TLS certificates |
| 📝&nbsp;[#111817](https://github.com/openclaw/openclaw/issues/111817) | 2026-07-20 | 0 | OpenAI-compatible/proxy | @ooiuuii | [Bug]: ChatGPT Responses retries deterministic TLS certificate failures |
| 📝&nbsp;[#111815](https://github.com/openclaw/openclaw/issues/111815) | 2026-07-20 | 0 | Model/provider behavior | @LarrysChef | image tool: 60s timeout for Anthropic vision when direct API returns in ~2s |
| 🔀&nbsp;[#111813](https://github.com/openclaw/openclaw/pull/111813) | 2026-07-20 | 0 | OpenAI-compatible/proxy | @vyncint | fix: Azure OpenAI memory indexing fails for custom providers |
| 🔀&nbsp;[#111811](https://github.com/openclaw/openclaw/pull/111811) | 2026-07-20 | 0 | Local memory/embedding | @Atlas-crete | fix(memory): prevent active session ingestion starvation |
| 🔀&nbsp;[#111810](https://github.com/openclaw/openclaw/pull/111810) | 2026-07-20 | 0 | Open-weight/provider behavior | @Monkey-wusky | fix(zai,amazon-bedrock-mantle): reject invalid UTF-8 in extension API response JSON |
| 📝&nbsp;[#111807](https://github.com/openclaw/openclaw/issues/111807) | 2026-07-20 | 0 | Model routing/config | @Zeus-Deus | /think off doesn't disable thinking on claude-cli — inherits Claude Code's default effort (contradicts docs) |
| 📝&nbsp;[#111804](https://github.com/openclaw/openclaw/issues/111804) | 2026-07-20 | 0 | Local memory/embedding | @dom521 | [Bug]: memory-wiki bridge-mode wiki_search/wiki_get/wiki_apply intermittent "path mismatch" causing gateway OOM |
| 🔀&nbsp;[#111802](https://github.com/openclaw/openclaw/pull/111802) | 2026-07-20 | 0 | Local model runtime | @dwc1997 | fix(ollama): release failed setup response bodies before returning |
| 📝&nbsp;[#111799](https://github.com/openclaw/openclaw/issues/111799) | 2026-07-20 | 0 | Local memory/embedding | @chrislro | active-memory: ~45% timeout rate and zero cached results during agent turns (2026.7.1-2) |
| 🔀&nbsp;[#111796](https://github.com/openclaw/openclaw/pull/111796) | 2026-07-20 | 0 | Model routing/config | @steipete | feat(gateway,ui): agent-scoped model provider credentials |
| 🔀&nbsp;[#111775](https://github.com/openclaw/openclaw/pull/111775) | 2026-07-20 | 0 | Model/provider behavior | @chenyangjun-xy | fix: reject malformed UTF-8 in provider HTTP text responses |
| 🔀&nbsp;[#111774](https://github.com/openclaw/openclaw/pull/111774) | 2026-07-20 | 0 | Model routing/config | @zhangguiping-xydt | fix(providers): usage returns empty data when a provider response is malformed |
| 🔀&nbsp;[#111766](https://github.com/openclaw/openclaw/pull/111766) | 2026-07-20 | 0 | Model routing/config | @chenyangjun-xy | fix(plugin-sdk): reject malformed UTF-8 in live provider model catalog responses |
| 📝&nbsp;[#111764](https://github.com/openclaw/openclaw/issues/111764) | 2026-07-20 | 0 | OpenAI-compatible/proxy | @forrystudio | Empty final completion (whitespace-only thinking, stop) surfaces as generic failure despite all tool work succeeding — add one-shot finalizer before non_deliverable_terminal_turn |
| 🔀&nbsp;[#111709](https://github.com/openclaw/openclaw/pull/111709) | 2026-07-20 | 0 | Model routing/config | @kesava500 | feat: show thinking level in model summary |

## OPEN THREADS (953)

| Thread | Activity | Area | Creator | Title |
| --- | --- | --- | --- | --- |
| 📝&nbsp;[#72015](https://github.com/openclaw/openclaw/issues/72015) | 29 | Local memory/embedding | @0xCNAI | Reliability: active-memory blocks replies and QMD boot initialization can overload multi-agent gateways<br>Assignee: osolmaz |
| 📝&nbsp;[#74586](https://github.com/openclaw/openclaw/issues/74586) | 17 | Local memory/embedding | @islandpreneur007 | AM embedded run aborts memory_search tool calls; classifies as timeout despite model completion<br>Assignee: osolmaz |
| 📝&nbsp;[#62328](https://github.com/openclaw/openclaw/issues/62328) | 17 | Local memory/embedding | @TimeAground | node:sqlite missing FTS5 module - memory search keyword fallback broken<br>Assignee: osolmaz |
| 📝&nbsp;[#74986](https://github.com/openclaw/openclaw/issues/74986) | 14 | Local model runtime | @mlaihk | [Bug]: openclaw infer hangs indefinitely on 2026.4.27 - openclaw-infer child spins at 100% CPU with zero network I/O<br>Assignee: osolmaz |
| 📝&nbsp;[#68920](https://github.com/openclaw/openclaw/issues/68920) | 14 | Local memory/embedding | @mehdic | HTTP /v1/chat/completions: 10-15s TTFB due to full agent context assembly - needs lightContext/voice mode |
| 📝&nbsp;[#84569](https://github.com/openclaw/openclaw/issues/84569) | 13 | Local model runtime | @kiagentkronos-cell | WhatsApp session stalls on long model_call: incomplete turn with payloads=0, reply never delivered<br>Assignee: osolmaz |
| 🔀&nbsp;[#81834](https://github.com/openclaw/openclaw/pull/81834) | 13 | Local/media model provider | @KLilyZ | feat(senseaudio): add SenseAudio TTS provider |
| 📝&nbsp;[#79847](https://github.com/openclaw/openclaw/issues/79847) | 13 | Local memory/embedding | @ChrisBot2026 | qmd-manager leaks XDG_CONFIG_HOME / XDG_CACHE_HOME to all child spawns, breaking mcporter >= 0.10 integration<br>Assignee: osolmaz |
| 🔀&nbsp;[#87247](https://github.com/openclaw/openclaw/pull/87247) | 12 | Local memory/embedding | @airbing11 | docs: note LanceDB dreaming v0.2.3 via memory-lancedb-dreaming plugin |
| 📝&nbsp;[#51441](https://github.com/openclaw/openclaw/issues/51441) | 12 | OpenAI-compatible/proxy | @Kyzcreig | feat: expose resolved backend model in session_status and agent runtime |
| 📝&nbsp;[#45049](https://github.com/openclaw/openclaw/issues/45049) | 12 | OpenAI-compatible/proxy | @ArnoldJr | Agent loop allows simulated tool calls instead of enforcing real tool invocation |
| 🔀&nbsp;[#68079](https://github.com/openclaw/openclaw/pull/68079) | 11 | OpenAI-compatible/proxy | @Frrrrrrrrank | feat(providers/zai): inject X-Session-Id header for prompt cache stickiness |
| 📝&nbsp;[#85126](https://github.com/openclaw/openclaw/issues/85126) | 10 | Local model runtime | @mlaihk | Bug: Control UI (TUI/WebChat) sessions auto-select wrong authProfileOverride (deepseek instead of minimax) at creation<br>Assignee: osolmaz |
| 🔀&nbsp;[#78747](https://github.com/openclaw/openclaw/pull/78747) | 10 | Model/provider behavior | @ashvinnagarajan | fix(cache): emit `tools` before `input` in OpenAI Responses request body for prefix-cache stability |
| 📝&nbsp;[#54463](https://github.com/openclaw/openclaw/issues/54463) | 10 | Local memory/embedding | @bwjoke | QMD memory indexing can recurse into symlink loops in workspace-visible temp monorepos and fail with ENAMETOOLONG<br>Assignee: vincentkoc |
| 🔀&nbsp;[#84977](https://github.com/openclaw/openclaw/pull/84977) | 9 | Local model runtime | @ouchuan | feat: handle gemma 4 format tool call |
| 📝&nbsp;[#73432](https://github.com/openclaw/openclaw/issues/73432) | 9 | Local memory/embedding | @danielngn | [Bug]: qmd embedding is never triggered per memory.qmd.update.interval/embedInterval<br>Assignee: osolmaz |
| 🔀&nbsp;[#71062](https://github.com/openclaw/openclaw/pull/71062) | 9 | OpenAI-compatible/proxy | @PopFlamingo | fix(/v1/responses): drop the extra phantom assistant turn on client-tool calls |
| 📝&nbsp;[#37966](https://github.com/openclaw/openclaw/issues/37966) | 9 | OpenAI-compatible/proxy | @V0v1kkkAssistant | [Bug]: cacheRetention ignored for LiteLLM-proxied Anthropic models |
| 📝&nbsp;[#10480](https://github.com/openclaw/openclaw/issues/10480) | 9 | OpenAI-compatible/proxy | @sidharthachatterjee | Support Workers AI model selection during onboard |
| 🔀&nbsp;[#87300](https://github.com/openclaw/openclaw/pull/87300) | 8 | Model routing/config | @newbie-yu | feat: group model select with collapsible panel in Control UI |
| 📝&nbsp;[#76665](https://github.com/openclaw/openclaw/issues/76665) | 8 | Open-weight/provider behavior | @Nelsoncongbao | Session context silently lost between consecutive turns with z.ai provider (GLM gateway) |
| 🔀&nbsp;[#75270](https://github.com/openclaw/openclaw/pull/75270) | 8 | OpenAI-compatible/proxy | @Komzpa | fix(agent): prevent sticky model fallback |
| 📝&nbsp;[#74021](https://github.com/openclaw/openclaw/issues/74021) | 8 | OpenAI-compatible/proxy | @jmystaki-create | Support reasoning-field outputs and visible final-answer handling for native reasoning models |
| 📝&nbsp;[#64438](https://github.com/openclaw/openclaw/issues/64438) | 8 | Local memory/embedding | @GravenSm | Feature Request: Remote Reranker Endpoint Support |
| 📝&nbsp;[#45508](https://github.com/openclaw/openclaw/issues/45508) | 8 | OpenAI-compatible/proxy | @mcfex | [Feature]: Self-hosted STT/TTS provider support in webchat (Route webchat TTS through the gateway instead of browser Speech API) |
| 📝&nbsp;[#41372](https://github.com/openclaw/openclaw/issues/41372) | 8 | Model/provider behavior | @e740554 | Field Report: 25 findings from 4 weeks of self-hosted production use (config crashes, CLI docs, Discord, cron) |
| 📝&nbsp;[#15073](https://github.com/openclaw/openclaw/issues/15073) | 8 | Local model runtime | @lucca-alma | Feature Request: Per-agent context/workspace on model fallback |
| 📝&nbsp;[#30381](https://github.com/openclaw/openclaw/issues/30381) | 7 | OpenAI-compatible/proxy | @mr-slurpy-wildcard | chatCompletions: ignore request model when x-openclaw-agent-id header is present |
| 📝&nbsp;[#63990](https://github.com/openclaw/openclaw/issues/63990) | 6 | Local memory/embedding | @DIZ-admin | Feature: Multi-index embedding memory with model-aware failover (no mixed vector spaces)<br>Assignee: osolmaz |
| 🔀&nbsp;[#87694](https://github.com/openclaw/openclaw/pull/87694) | 5 | Model routing/config | @sweetcornna | fix(auth): tighten billing cooldown defaults to recover from multi-hour lockouts (#70903) |
| 📝&nbsp;[#83402](https://github.com/openclaw/openclaw/issues/83402) | 5 | OpenAI-compatible/proxy | @Guardl1n | [Bug]: Providers/Xiaomi: MiMo mimo-v2.5-pro still rejects cron embedded agent tool schema with 400 after 2026.5.12 fix |
| 🔀&nbsp;[#78085](https://github.com/openclaw/openclaw/pull/78085) | 5 | OpenAI-compatible/proxy | @Beandon13 | fix(agents): parse prompt_tokens/completion_tokens in CLI usage for llama.cpp compatibility (#77992) |
| 📝&nbsp;[#74732](https://github.com/openclaw/openclaw/issues/74732) | 5 | Local memory/embedding | @mppyes-ai | docs+feat: Document oMLX (Apple Silicon MLX) as memorySearch embedding provider<br>Assignee: osolmaz |
| 🔀&nbsp;[#73594](https://github.com/openclaw/openclaw/pull/73594) | 5 | Open-weight/provider behavior | @simpx | feat(openrouter): inject cache_control for closed-source qwen models |
| 📝&nbsp;[#66125](https://github.com/openclaw/openclaw/issues/66125) | 5 | OpenAI-compatible/proxy | @Cybertr0n313 | [Bug]: openai-completions fallback candidate is selected, but fallback does not complete successfully through an OpenAI-compatible proxy<br>Assignee: osolmaz |
| 🔀&nbsp;[#87932](https://github.com/openclaw/openclaw/pull/87932) | 4 | Model routing/config | @tanshanshan | feat(compaction): support percentage strings for token thresholds |
| 📝&nbsp;[#87756](https://github.com/openclaw/openclaw/issues/87756) | 4 | Local model runtime | @rogerallen1 | [Bug]: Regression: prompt-launched Lobster workflow hangs on nested /tools/invoke, while curl-launched workflow works |
| 📝&nbsp;[#87407](https://github.com/openclaw/openclaw/issues/87407) | 4 | Model routing/config | @chrisgarcia-cpu | [Bug]: Anthropic provider: UND_ERR_SOCKET keep-alive failures trigger silent mid-turn fallback to OpenAI/Codex |
| 📝&nbsp;[#87325](https://github.com/openclaw/openclaw/issues/87325) | 4 | OpenAI-compatible/proxy | @BSG2000 | Support Azure Foundry GPT Realtime Talk via gateway relay |
| 📝&nbsp;[#87318](https://github.com/openclaw/openclaw/issues/87318) | 4 | Model routing/config | @Haderach-Ram | amazon-bedrock provider: Haiku 4.5 inference profile ARN not supported; params.modelId override ignored |
| 📝&nbsp;[#87140](https://github.com/openclaw/openclaw/issues/87140) | 4 | Local/media model provider | @StephenCYL | [Feature]: Pluggable STT backend for macOS Push-to-Talk |
| 📝&nbsp;[#86632](https://github.com/openclaw/openclaw/issues/86632) | 4 | Local model runtime | @ebelo | OpenClaw local embedded Ollama/Qwen session fails live-data request that Pi coding agent handles via shell/curl<br>Assignee: osolmaz |
| 📝&nbsp;[#86034](https://github.com/openclaw/openclaw/issues/86034) | 4 | OpenAI-compatible/proxy | @tianxiaochannel-oss88 | Media generation succeeds but completion delivery fails and looks like generation failure |
| 📝&nbsp;[#84575](https://github.com/openclaw/openclaw/issues/84575) | 4 | OpenAI-compatible/proxy | @juergenvh | [Bug] /v1/chat/completions: second request with same x-openclaw-session-key during in-flight turn runs in isolated session, loses memory scope<br>Assignee: osolmaz |
| 📝&nbsp;[#84218](https://github.com/openclaw/openclaw/issues/84218) | 4 | Local model runtime | @reboost-openclaw-team[bot] | Heartbeat isolatedSession=true replays prior heartbeat context, causing deterministic overflow/restart loop |
| 📝&nbsp;[#83584](https://github.com/openclaw/openclaw/issues/83584) | 4 | OpenAI-compatible/proxy | @kwizzlek | [Bug]: Outbound MEDIA: directive on /v1/responses and /v1/chat/completions is passed through as raw text instead of translated to image_url / file content block |
| 📝&nbsp;[#81960](https://github.com/openclaw/openclaw/issues/81960) | 4 | Local model runtime | @alexandre-leng | [Feature]: Allow onboarding to configure multiple providers and models |
| 📝&nbsp;[#80081](https://github.com/openclaw/openclaw/issues/80081) | 4 | OpenAI-compatible/proxy | @torbisoc | Need documented config keys for disabling plugin/tool/channel/owner-elevated surfaces for proposal-only mode |
| 📝&nbsp;[#77692](https://github.com/openclaw/openclaw/issues/77692) | 4 | OpenAI-compatible/proxy | @kidding1412 | fix(tts/xiaomi): Xiaomi Token Plan endpoint uses Bearer auth, not api-key header |

<details>
<summary>Remaining 903 open threads, sorted by activity</summary>

| Thread | Activity | Area | Creator | Title |
| --- | --- | --- | --- | --- |
| 📝&nbsp;[#77675](https://github.com/openclaw/openclaw/issues/77675) | 4 | Local model runtime | @nickytonline | [Bug]: request.headers SecretRefs on model providers fail in embedded agent context with "unresolved SecretRef" error |
| 📝&nbsp;[#77142](https://github.com/openclaw/openclaw/issues/77142) | 4 | Local memory/embedding | @vuho60-byte | [Feature]: Parametric consolidation channel for dreaming pipeline (CLS Phase 4) |
| 📝&nbsp;[#73801](https://github.com/openclaw/openclaw/issues/73801) | 4 | OpenAI-compatible/proxy | @iannwu | Active Memory with Cerebras gpt-oss-120b times out and can pin gateway CPU |
| 📝&nbsp;[#69943](https://github.com/openclaw/openclaw/issues/69943) | 4 | Local memory/embedding | @reidperyam | [Bug]: session-memory hook persists raw chat-template tokens and unparsed tool calls - re-injected context creates self-reinforcing poisoning loop, agents emit role tokens / NO_REPLY across all subsequent /new sessions |
| 📝&nbsp;[#63229](https://github.com/openclaw/openclaw/issues/63229) | 4 | Local model runtime | @clawdia-lobster | Bug: Gateway falsely marks healthy local vLLM endpoints as timed out/overloaded, causing 1-23 min fallback cascades<br>Assignee: osolmaz |
| 📝&nbsp;[#62599](https://github.com/openclaw/openclaw/issues/62599) | 4 | Local model runtime | @shawnpetros | [Bug]: openclaw status loads memory plugins locally and can report false vector state |
| 📝&nbsp;[#57996](https://github.com/openclaw/openclaw/issues/57996) | 4 | Local memory/embedding | @Orionation | QMD per-agent SQLite caches cause extreme disk I/O on multi-agent deployments<br>Assignee: vincentkoc |
| 📝&nbsp;[#53550](https://github.com/openclaw/openclaw/issues/53550) | 4 | Local memory/embedding | @shivasymbl | experimental.sessionMemory does not surface gateway-dispatched sessions in memory_search |
| 📝&nbsp;[#49205](https://github.com/openclaw/openclaw/issues/49205) | 4 | OpenAI-compatible/proxy | @SHAREN | [Bug]: Control UI messages can reach shared context but still not appear in Open WebUI visible chat history |
| 📝&nbsp;[#46661](https://github.com/openclaw/openclaw/issues/46661) | 4 | OpenAI-compatible/proxy | @sheldon123z | [Feature]: Support Custom ASR (Speech-to-Text) Server Configuration |
| 📝&nbsp;[#22021](https://github.com/openclaw/openclaw/issues/22021) | 4 | Local model runtime | @dekaru | [Feature]: Add X-Actual-Model header to expose runtime model in HTTP responses |
| 📝&nbsp;[#13962](https://github.com/openclaw/openclaw/issues/13962) | 4 | Local model runtime | @dantaik | Feature: Per-mention model routing + context window for group mentions |
| 🔀&nbsp;[#73817](https://github.com/openclaw/openclaw/pull/73817) | 2 | OpenAI-compatible/proxy | @spi3 | fix(media): allow private openai compatible audio transcription endpoints |
| 📝&nbsp;[#59168](https://github.com/openclaw/openclaw/issues/59168) | 2 | Local model runtime | @Kaspre | feat(models): use provider/name as internal key to decouple from API model ID |
| 📝&nbsp;[#77090](https://github.com/openclaw/openclaw/issues/77090) | 1 | Local model runtime | @djpollock | Feature: Auto-revert to primary model after image analysis |
| 📝&nbsp;[#41135](https://github.com/openclaw/openclaw/issues/41135) | 1 | Local model runtime | @tardis-create | [Feature]: Add provider-profile routing policies for multi-account OAuth/API pools (starting with google-gemini-cli) |
| 📝&nbsp;[#111966](https://github.com/openclaw/openclaw/issues/111966) | 0 | Model/provider behavior | @markcallow-jpg | Bug: `extractRawAssistantText()` flattens multi-segment assistant output with no delimiter |
| 🔀&nbsp;[#111964](https://github.com/openclaw/openclaw/pull/111964) | 0 | Model routing/config | @dillona | fix(google): default web_search model to rolling alias, not retired gemini-2.5-flash |
| 📝&nbsp;[#111943](https://github.com/openclaw/openclaw/issues/111943) | 0 | Model routing/config | @Zeus-Deus | [Feature]: Configurable model + reasoning effort for background "learning" subsystems |
| 📝&nbsp;[#111924](https://github.com/openclaw/openclaw/issues/111924) | 0 | Model routing/config | @japr26 | [Feature]: Buscador/filtro en dropdown de modelos del Control UI |
| 📝&nbsp;[#111923](https://github.com/openclaw/openclaw/issues/111923) | 0 | Local memory/embedding | @makominsk | Dreaming REM phase extracts junk topics (stop words, numbers, ranges) with no filter/config exposed |
| 🔀&nbsp;[#111901](https://github.com/openclaw/openclaw/pull/111901) | 0 | Model/provider behavior | @Vicenteut | feat(plugin-runtime): support declarative tools and single-attempt completions |
| 🔀&nbsp;[#111899](https://github.com/openclaw/openclaw/pull/111899) | 0 | Model routing/config | @xialonglee | fix(cli): block embedded fallback for gateway-accepted agent turns on transport error |
| 🔀&nbsp;[#111895](https://github.com/openclaw/openclaw/pull/111895) | 0 | Open-weight/provider behavior | @xbrxr03 | fix(failover): classify provider finish_reason: error as server_error, not timeout |
| 🔀&nbsp;[#111894](https://github.com/openclaw/openclaw/pull/111894) | 0 | Local/media model provider | @xbrxr03 | fix(openai): add handshakeTimeout to realtime voice WebSocket |
| 🔀&nbsp;[#111892](https://github.com/openclaw/openclaw/pull/111892) | 0 | Model routing/config | @xbrxr03 | fix(compaction): skip preflight compaction when backend owns native compaction |
| 📝&nbsp;[#111889](https://github.com/openclaw/openclaw/issues/111889) | 0 | Model/provider behavior | @Vicenteut | Plugin runtime: support declarative tools and single-attempt completions |
| 📝&nbsp;[#111886](https://github.com/openclaw/openclaw/issues/111886) | 0 | Model routing/config | @Olivaryne | Compaction frees zero tokens when transcript estimates undershoot the context-usage trigger (firstKeptEntryId stuck at first entry) |
| 🔀&nbsp;[#111885](https://github.com/openclaw/openclaw/pull/111885) | 0 | Model routing/config | @xbrxr03 | fix(config): add compaction.enabled to schema so users can disable auto-compaction |
| 📝&nbsp;[#111884](https://github.com/openclaw/openclaw/issues/111884) | 0 | Model routing/config | @MontanaIrish | [Bug]: Regression of #67988 — model picker shows alias ("Opus"/"Sonnet") instead of versioned display name, now on Opus 4.8 / Sonnet 5 |
| 🔀&nbsp;[#111882](https://github.com/openclaw/openclaw/pull/111882) | 0 | Open-weight/provider behavior | @xbrxr03 | fix(minimax): recognize coding-plan response shape with remaining-percent fields |
| 📝&nbsp;[#111879](https://github.com/openclaw/openclaw/issues/111879) | 0 | Model/provider behavior | @shayshimon | [Bug]: Parallel Codex hook relays can exhaust gateway resources and block the control plane |
| 🔀&nbsp;[#111878](https://github.com/openclaw/openclaw/pull/111878) | 0 | Open-weight/provider behavior | @xbrxr03 | fix(kimi-coding): remove k3[1m] from catalog, normalize to k3, raise context window |
| 🔀&nbsp;[#111872](https://github.com/openclaw/openclaw/pull/111872) | 0 | Model/provider behavior | @Pick-cat | fix(amazon-bedrock): reject malformed inbound image base64 |
| 📝&nbsp;[#111870](https://github.com/openclaw/openclaw/issues/111870) | 0 | Model/provider behavior | @Flagrare | [Bug]: @openclaw/codex fails to register in CLI context — TypeError: undefined 'openSyncKeyedStore' |
| 🔀&nbsp;[#111864](https://github.com/openclaw/openclaw/pull/111864) | 0 | Model/provider behavior | @ooiuuii | fix(ai): trim replay tool call ids |
| 📝&nbsp;[#111863](https://github.com/openclaw/openclaw/issues/111863) | 0 | Model/provider behavior | @ooiuuii | Provider replay mispairs tool results when call IDs contain surrounding whitespace |
| 📝&nbsp;[#111857](https://github.com/openclaw/openclaw/issues/111857) | 0 | Model routing/config | @itanyplus | [Bug]: CLI budget reopens the full compacted JSONL branch, inflating prompt estimates and repeatedly compacting low-context parent sessions |
| 📝&nbsp;[#111856](https://github.com/openclaw/openclaw/issues/111856) | 0 | Model routing/config | @nierob-cmd | Compaction summarization bypasses per-turn image-history pruning, can overflow context |
| 🔀&nbsp;[#111852](https://github.com/openclaw/openclaw/pull/111852) | 0 | OpenAI-compatible/proxy | @chenyangjun-xy | fix: reject malformed UTF-8 in proxy gateway error response bodies |
| 📝&nbsp;[#111850](https://github.com/openclaw/openclaw/issues/111850) | 0 | Local memory/embedding | @chrislro | stt-tts Talk: aborted active-memory pre-run surfaces as user-facing "voice config failed" |
| 📝&nbsp;[#111848](https://github.com/openclaw/openclaw/issues/111848) | 0 | Model routing/config | @Enominera | [Bug]: acp-agent.js env construction missing settingsManager.getSettings().env — auto-compaction relies on gateway coincidence |
| 📝&nbsp;[#111846](https://github.com/openclaw/openclaw/issues/111846) | 0 | Open-weight/provider behavior | @Enominera | Thinking block loop silently exhausts output tokens → session permanently unusable (976K tokens accumulated) |
| 🔀&nbsp;[#111845](https://github.com/openclaw/openclaw/pull/111845) | 0 | Model/provider behavior | @dwc1997 | fix(codex): bound app-server websocket upgrade with handshake timeout |
| 🔀&nbsp;[#111841](https://github.com/openclaw/openclaw/pull/111841) | 0 | Model routing/config | @xialonglee | fix(agents): allow configless gateway rebind to activate standalone owner |
| 📝&nbsp;[#111839](https://github.com/openclaw/openclaw/issues/111839) | 0 | Model/provider behavior | @LeeroyDing | [Bug]: Channel follow-ups never steer active Codex app-server runs — steer always rejected (transcript_commit_wait_unsupported) and queued as follow-ups, unlike /steer and message-tool paths |
| 🔀&nbsp;[#111835](https://github.com/openclaw/openclaw/pull/111835) | 0 | Local model runtime | @masatohoshino | fix(ollama): bound DNS preflight with guard-owned request timeouts |
| 📝&nbsp;[#111827](https://github.com/openclaw/openclaw/issues/111827) | 0 | Model routing/config | @maharrer79-ops | Codex (openai-codex) provider: newer models report "Unknown model" + OAuth refresh_token_reused token race |
| 🔀&nbsp;[#111826](https://github.com/openclaw/openclaw/pull/111826) | 0 | Model routing/config | @Zeus-Deus | fix: /think off does not disable thinking on claude-cli |
| 🔀&nbsp;[#111825](https://github.com/openclaw/openclaw/pull/111825) | 0 | OpenAI-compatible/proxy | @wuqxuan | fix(agents): tools-disabled finalizer after blank post-tool stop |
| 🔀&nbsp;[#111818](https://github.com/openclaw/openclaw/pull/111818) | 0 | OpenAI-compatible/proxy | @ooiuuii | fix(openai): fail fast on invalid TLS certificates |
| 📝&nbsp;[#111817](https://github.com/openclaw/openclaw/issues/111817) | 0 | OpenAI-compatible/proxy | @ooiuuii | [Bug]: ChatGPT Responses retries deterministic TLS certificate failures |
| 📝&nbsp;[#111815](https://github.com/openclaw/openclaw/issues/111815) | 0 | Model/provider behavior | @LarrysChef | image tool: 60s timeout for Anthropic vision when direct API returns in ~2s |
| 🔀&nbsp;[#111813](https://github.com/openclaw/openclaw/pull/111813) | 0 | OpenAI-compatible/proxy | @vyncint | fix: Azure OpenAI memory indexing fails for custom providers |
| 🔀&nbsp;[#111811](https://github.com/openclaw/openclaw/pull/111811) | 0 | Local memory/embedding | @Atlas-crete | fix(memory): prevent active session ingestion starvation |
| 🔀&nbsp;[#111810](https://github.com/openclaw/openclaw/pull/111810) | 0 | Open-weight/provider behavior | @Monkey-wusky | fix(zai,amazon-bedrock-mantle): reject invalid UTF-8 in extension API response JSON |
| 📝&nbsp;[#111807](https://github.com/openclaw/openclaw/issues/111807) | 0 | Model routing/config | @Zeus-Deus | /think off doesn't disable thinking on claude-cli — inherits Claude Code's default effort (contradicts docs) |
| 📝&nbsp;[#111804](https://github.com/openclaw/openclaw/issues/111804) | 0 | Local memory/embedding | @dom521 | [Bug]: memory-wiki bridge-mode wiki_search/wiki_get/wiki_apply intermittent "path mismatch" causing gateway OOM |
| 🔀&nbsp;[#111802](https://github.com/openclaw/openclaw/pull/111802) | 0 | Local model runtime | @dwc1997 | fix(ollama): release failed setup response bodies before returning |
| 📝&nbsp;[#111799](https://github.com/openclaw/openclaw/issues/111799) | 0 | Local memory/embedding | @chrislro | active-memory: ~45% timeout rate and zero cached results during agent turns (2026.7.1-2) |
| 🔀&nbsp;[#111796](https://github.com/openclaw/openclaw/pull/111796) | 0 | Model routing/config | @steipete | feat(gateway,ui): agent-scoped model provider credentials |
| 🔀&nbsp;[#111775](https://github.com/openclaw/openclaw/pull/111775) | 0 | Model/provider behavior | @chenyangjun-xy | fix: reject malformed UTF-8 in provider HTTP text responses |
| 🔀&nbsp;[#111774](https://github.com/openclaw/openclaw/pull/111774) | 0 | Model routing/config | @zhangguiping-xydt | fix(providers): usage returns empty data when a provider response is malformed |
| 🔀&nbsp;[#111766](https://github.com/openclaw/openclaw/pull/111766) | 0 | Model routing/config | @chenyangjun-xy | fix(plugin-sdk): reject malformed UTF-8 in live provider model catalog responses |
| 📝&nbsp;[#111764](https://github.com/openclaw/openclaw/issues/111764) | 0 | OpenAI-compatible/proxy | @forrystudio | Empty final completion (whitespace-only thinking, stop) surfaces as generic failure despite all tool work succeeding — add one-shot finalizer before non_deliverable_terminal_turn |
| 🔀&nbsp;[#111709](https://github.com/openclaw/openclaw/pull/111709) | 0 | Model routing/config | @kesava500 | feat: show thinking level in model summary |
| 🔀&nbsp;[#111696](https://github.com/openclaw/openclaw/pull/111696) | 0 | Open-weight/provider behavior | @lee-xydt | fix(provider-usage): recognize current MiniMax coding-plan API response shape |
| 📝&nbsp;[#111654](https://github.com/openclaw/openclaw/issues/111654) | 0 | Model routing/config | @NOVA-Openclaw | runWithModelFallback shares one abortSignal/deadline across all fallback attempts, mislabeling instant failures as provider timeouts |
| 🔀&nbsp;[#111612](https://github.com/openclaw/openclaw/pull/111612) | 0 | Model routing/config | @ljy-1351 | fix(agents): use \ |
| 🔀&nbsp;[#111611](https://github.com/openclaw/openclaw/pull/111611) | 0 | Model routing/config | @ljy-1351 | fix(infra): use \ |
| 🔀&nbsp;[#111594](https://github.com/openclaw/openclaw/pull/111594) | 0 | Model routing/config | @yetval | fix(google): surface public client PKCE mode when OAuth client secret is missing |
| 🔀&nbsp;[#111587](https://github.com/openclaw/openclaw/pull/111587) | 0 | Open-weight/provider behavior | @yangxiansheng | fix(kimi): use k3 as single API model id, drop k3[1m] wire-id (#111561) |
| 🔀&nbsp;[#111492](https://github.com/openclaw/openclaw/pull/111492) | 0 | Model routing/config | @wenrizc | fix: honor provider token defaults for custom models |
| 🔀&nbsp;[#111434](https://github.com/openclaw/openclaw/pull/111434) | 0 | Model routing/config | @mushuiyu886 | fix(vercel-ai-gateway): long-context usage costs are underreported |
| 🔀&nbsp;[#111428](https://github.com/openclaw/openclaw/pull/111428) | 0 | Model routing/config | @mushuiyu886 | fix(deepinfra): model list fails when HTTP proxy is required |
| 🔀&nbsp;[#111392](https://github.com/openclaw/openclaw/pull/111392) | 0 | Local memory/embedding | @wuqxuan | fix(memory-core): skip unchanged Dreaming workspace state writes |
| 🔀&nbsp;[#111389](https://github.com/openclaw/openclaw/pull/111389) | 0 | Model routing/config | @steipete | fix(usage): price usage rows with the owning agent's model registry |
| 📝&nbsp;[#111386](https://github.com/openclaw/openclaw/issues/111386) | 0 | OpenAI-compatible/proxy | @OliPlus | Azure OpenAI embedding provider fails — api-version not forwarded as URL query parameter |
| 📝&nbsp;[#111376](https://github.com/openclaw/openclaw/issues/111376) | 0 | Local memory/embedding | @khenn | [Bug]: memory-core Dreaming rewrites unchanged workspace state and stalls the gateway event loop |
| 📝&nbsp;[#111359](https://github.com/openclaw/openclaw/issues/111359) | 0 | Open-weight/provider behavior | @greggchen308 | Cron job `delivered: false` when deliveryBestEffort: true and interim-message guard fires without active subagents |
| 📝&nbsp;[#111354](https://github.com/openclaw/openclaw/issues/111354) | 0 | OpenAI-compatible/proxy | @gnnave-sudo | RFC: Declarative provider manifests instead of per-vendor lifecycle re-implementation |
| 🔀&nbsp;[#111343](https://github.com/openclaw/openclaw/pull/111343) | 0 | OpenAI-compatible/proxy | @mjnkao | feat(durable): persist agent turn front doors |
| 🔀&nbsp;[#111332](https://github.com/openclaw/openclaw/pull/111332) | 0 | Model routing/config | @nocodet888-arch | fix(agents): web_fetch leaves body open after provider fallback |
| 🔀&nbsp;[#111304](https://github.com/openclaw/openclaw/pull/111304) | 0 | Open-weight/provider behavior | @yuvrajlaptop2008-byte | fix(agents): strip MiniMax stream-boundary marker from transport payload text (#104403) |
| 🔀&nbsp;[#111284](https://github.com/openclaw/openclaw/pull/111284) | 0 | Model routing/config | @zenglingbiao | fix(plugin-sdk): decode live model catalog JSON with fatal UTF-8 validation |
| 🔀&nbsp;[#111279](https://github.com/openclaw/openclaw/pull/111279) | 0 | Local memory/embedding | @zenglingbiao | fix(memory-host-sdk): decode JSON response bodies with fatal UTF-8 validation |
| 🔀&nbsp;[#111266](https://github.com/openclaw/openclaw/pull/111266) | 0 | Open-weight/provider behavior | @mushuiyu886 | fix(chutes): discover models when HTTP proxy is required |
| 📝&nbsp;[#111255](https://github.com/openclaw/openclaw/issues/111255) | 0 | Model routing/config | @nftant | Bug: Gateway SIGUSR1 restart regenerates agent models.json with missing providers (reproduced: empty providers when only deepseek configured) |
| 🔀&nbsp;[#111253](https://github.com/openclaw/openclaw/pull/111253) | 0 | Open-weight/provider behavior | @mushuiyu886 | fix(chutes): cache-read usage is reported as free |
| 🔀&nbsp;[#111240](https://github.com/openclaw/openclaw/pull/111240) | 0 | Model routing/config | @xydt-juyaohui | fix(usage): reject invalid UTF-8 in Anthropic and OpenAI admin usage responses |
| 🔀&nbsp;[#111239](https://github.com/openclaw/openclaw/pull/111239) | 0 | Model routing/config | @mushuiyu886 | fix(kilocode): image-output models appear in chat catalog |
| 🔀&nbsp;[#111237](https://github.com/openclaw/openclaw/pull/111237) | 0 | Model routing/config | @mushuiyu886 | fix(venice): model list shows current live context limits |
| 🔀&nbsp;[#111226](https://github.com/openclaw/openclaw/pull/111226) | 0 | Local model runtime | @hugenshen | fix(cron): cancel unread local model preflight bodies |
| 📝&nbsp;[#111219](https://github.com/openclaw/openclaw/issues/111219) | 0 | Model routing/config | @boycez | secrets audit: auth-profile SQLite store scanned for default agent only (multi-agent blind spot) |
| 🔀&nbsp;[#111212](https://github.com/openclaw/openclaw/pull/111212) | 0 | Model routing/config | @fuller-stack-dev | feat(mcp-apps): support bounded model context updates |
| 🔀&nbsp;[#111209](https://github.com/openclaw/openclaw/pull/111209) | 0 | Open-weight/provider behavior | @mushuiyu886 | fix(vercel-ai-gateway): discover models when HTTP proxy is required |
| 🔀&nbsp;[#111198](https://github.com/openclaw/openclaw/pull/111198) | 0 | Open-weight/provider behavior | @ZengWen-DT | fix(xiaomi): reject malformed base64 TTS audio |
| 🔀&nbsp;[#111182](https://github.com/openclaw/openclaw/pull/111182) | 0 | Open-weight/provider behavior | @wahaha1223 | fix(openrouter): reject invalid UTF-8 usage responses |
| 🔀&nbsp;[#111180](https://github.com/openclaw/openclaw/pull/111180) | 0 | Open-weight/provider behavior | @wahaha1223 | fix(venice): reject invalid UTF-8 usage responses |
| 🔀&nbsp;[#111175](https://github.com/openclaw/openclaw/pull/111175) | 0 | Model routing/config | @xydigit-zt | fix(usage): omit costUsd when model pricing is all-zero (unknown) |
| 🔀&nbsp;[#111173](https://github.com/openclaw/openclaw/pull/111173) | 0 | Model routing/config | @steipete | refactor: own model discovery by runtime lifecycle |
| 🔀&nbsp;[#111137](https://github.com/openclaw/openclaw/pull/111137) | 0 | Model routing/config | @steipete | refactor(agents): make API registry ownership lifecycle-local |
| 🔀&nbsp;[#111115](https://github.com/openclaw/openclaw/pull/111115) | 0 | Local memory/embedding | @jwest75674 | fix(memory-core): unify QMD multi-collection search, add phase timings, fix archived-session identity loss |
| 🔀&nbsp;[#111113](https://github.com/openclaw/openclaw/pull/111113) | 0 | OpenAI-compatible/proxy | @zenglingbiao | fix(plugins): decode self-hosted discovery JSON with fatal UTF-8 validation |
| 🔀&nbsp;[#111098](https://github.com/openclaw/openclaw/pull/111098) | 0 | Model routing/config | @lsr911-code | fix(model-pricing): guard loopback host checks with isIP to prevent DNS SSRF bypass |
| 📝&nbsp;[#111085](https://github.com/openclaw/openclaw/issues/111085) | 0 | OpenAI-compatible/proxy | @EricChan2028 | Tool-result truncation jitter invalidates prompt-cache prefixes — quantize truncation to stable steps |
| 📝&nbsp;[#111084](https://github.com/openclaw/openclaw/issues/111084) | 0 | OpenAI-compatible/proxy | @EricChan2028 | showInjected persists injected context into session history, degrading OpenAI-compatible prompt-cache hit rates |
| 📝&nbsp;[#111083](https://github.com/openclaw/openclaw/issues/111083) | 0 | OpenAI-compatible/proxy | @EricChan2028 | Feature: documented cache-stable placement for hook-injected system context (`beforeCacheBoundary` variant + `stableSystemContext` hook-result field) |
| 🔀&nbsp;[#111056](https://github.com/openclaw/openclaw/pull/111056) | 0 | Open-weight/provider behavior | @ZengWen-DT | fix(openrouter): preserve completed music when stream cleanup fails |
| 🔀&nbsp;[#111016](https://github.com/openclaw/openclaw/pull/111016) | 0 | Open-weight/provider behavior | @yuvrajlaptop2008-byte | fix(agents): strip MiniMax stream-boundary marker from transport payload text |
| 🔀&nbsp;[#111004](https://github.com/openclaw/openclaw/pull/111004) | 0 | Model routing/config | @cxbAsDev | fix(auth-profiles): bound auth-profile JSON reads with size cap |
| 🔀&nbsp;[#110998](https://github.com/openclaw/openclaw/pull/110998) | 0 | OpenAI-compatible/proxy | @mushuiyu886 | fix(opencode): public models work without API keys |
| 🔀&nbsp;[#110990](https://github.com/openclaw/openclaw/pull/110990) | 0 | Model routing/config | @zhangguiping-xydt | fix(plugins): model catalog discovery stalls on an unresponsive plugin |
| 🔀&nbsp;[#110979](https://github.com/openclaw/openclaw/pull/110979) | 0 | Open-weight/provider behavior | @wuqxuan | fix(provider-usage): parse MiniMax remaining-percent usage payload |
| 🔀&nbsp;[#110975](https://github.com/openclaw/openclaw/pull/110975) | 0 | Model routing/config | @Duplicity604 | fix(codex): mid-turn usage-limit errors hang the turn until an outer timeout |
| 📝&nbsp;[#110974](https://github.com/openclaw/openclaw/issues/110974) | 0 | Model routing/config | @Duplicity604 | [Bug]: Codex mid-turn usageLimitExceeded (willRetry) stalls the turn until an outer timeout instead of failing fast with the usage-limit error |
| 🔀&nbsp;[#110956](https://github.com/openclaw/openclaw/pull/110956) | 0 | Open-weight/provider behavior | @christiandesantis | fix: distinct Responses tool-call ids for repeated native Kimi calls |
| 📝&nbsp;[#110953](https://github.com/openclaw/openclaw/issues/110953) | 0 | Local model runtime | @Dharaneesh20 | [Bug]: Fresh LM Studio session on Ubuntu fails with "Context overflow" or "Message ordering conflict" after first message |
| 🔀&nbsp;[#110917](https://github.com/openclaw/openclaw/pull/110917) | 0 | OpenAI-compatible/proxy | @knowhycodata | feat: add LLMTR provider for Turkey-hosted and global models |
| 📝&nbsp;[#110915](https://github.com/openclaw/openclaw/issues/110915) | 0 | OpenAI-compatible/proxy | @knowhycodata | Add LLMTR provider (Turkey-hosted OpenAI-compatible AI gateway) |
| 🔀&nbsp;[#110898](https://github.com/openclaw/openclaw/pull/110898) | 0 | Local memory/embedding | @joeykrug | fix(active-memory): recall sub-agent receives huge prompt envelopes; bound recall context to 25K chars |
| 📝&nbsp;[#110887](https://github.com/openclaw/openclaw/issues/110887) | 0 | Open-weight/provider behavior | @pitcockchris79 | [Bug]: /status reports MiniMax "Unsupported response shape" — fetcher does not recognize current MiniMax API payload (no chat-model entry, remaining percent fields ignored) |
| 🔀&nbsp;[#110873](https://github.com/openclaw/openclaw/pull/110873) | 0 | Open-weight/provider behavior | @IWhatsskill | fix(minimax): restore X-Api-Key authentication |
| 🔀&nbsp;[#110866](https://github.com/openclaw/openclaw/pull/110866) | 0 | OpenAI-compatible/proxy | @YangManBOBO | fix(agents): mid-turn assistant text from claude-cli turns never reaches the channel even with block streaming enabled |
| 🔀&nbsp;[#110858](https://github.com/openclaw/openclaw/pull/110858) | 0 | Model routing/config | @nocodet888-arch | fix(auth): bound auth-profile source JSON probe reads |
| 🔀&nbsp;[#110855](https://github.com/openclaw/openclaw/pull/110855) | 0 | Open-weight/provider behavior | @mushuiyu886 | fix(models): report accurate limits in OpenRouter scans |
| 🔀&nbsp;[#110823](https://github.com/openclaw/openclaw/pull/110823) | 0 | Local model runtime | @chenyangjun-xy | fix(agents): repair double-escaped JSON strings in tool call argument… |
| 🔀&nbsp;[#110785](https://github.com/openclaw/openclaw/pull/110785) | 0 | Open-weight/provider behavior | @Leon-SK668 | fix(usage): guard malformed DeepSeek balance payloads |
| 🔀&nbsp;[#110773](https://github.com/openclaw/openclaw/pull/110773) | 0 | Local memory/embedding | @cxbAsDev | fix(session-memory): bound session transcript file read with size cap |
| 📝&nbsp;[#110763](https://github.com/openclaw/openclaw/issues/110763) | 0 | Open-weight/provider behavior | @najef1979-code | [Bug]: No API key in header for Minimax?? |
| 🔀&nbsp;[#110741](https://github.com/openclaw/openclaw/pull/110741) | 0 | Open-weight/provider behavior | @Leon-SK668 | fix(usage): guard malformed Z.AI usage payloads |
| 🔀&nbsp;[#110734](https://github.com/openclaw/openclaw/pull/110734) | 0 | Open-weight/provider behavior | @wangyan2026 | fix(codex-native): interrupt live Codex subagent thread on tasks cancel |
| 🔀&nbsp;[#110731](https://github.com/openclaw/openclaw/pull/110731) | 0 | Open-weight/provider behavior | @zhangguiping-xydt | fix(plugins): agent runs hang when tool-result middleware never settles |
| 🔀&nbsp;[#110700](https://github.com/openclaw/openclaw/pull/110700) | 0 | Local memory/embedding | @MaheshBhushan | fix(codex): MEMORY.md silently truncated when memory plugin exposes only memory_recall |
| 🔀&nbsp;[#110693](https://github.com/openclaw/openclaw/pull/110693) | 0 | OpenAI-compatible/proxy | @lsr911 | fix(litellm): guard loopback hostname auto-allow with isIP to prevent DNS SSRF bypass |
| 🔀&nbsp;[#110678](https://github.com/openclaw/openclaw/pull/110678) | 0 | Model routing/config | @YangManBOBO | fix(auth): expired OAuth credentials survive per-provider credential discovery and silently break background operations |
| 🔀&nbsp;[#110676](https://github.com/openclaw/openclaw/pull/110676) | 0 | Open-weight/provider behavior | @ZengWen-DT | fix(amazon-bedrock): ignore blank region env overrides<br>Assignee: steipete |
| 📝&nbsp;[#110672](https://github.com/openclaw/openclaw/issues/110672) | 0 | OpenAI-compatible/proxy | @DerekEXS | fix(prompt-assembly): runtime-context block header misleads smaller models into reporting the current message body as 'not injected' |
| 📝&nbsp;[#110665](https://github.com/openclaw/openclaw/issues/110665) | 0 | Local memory/embedding | @islandpreneur007 | Codex bootstrap accounting misses memory_recall and doctor is harness-blind |
| 🔀&nbsp;[#110661](https://github.com/openclaw/openclaw/pull/110661) | 0 | Model routing/config | @IWhatsskill | improve(android): move Wear agent, session, and model pickers to Home<br>Assignee: steipete |
| 🔀&nbsp;[#110655](https://github.com/openclaw/openclaw/pull/110655) | 0 | Local model runtime | @Yigtwxx | fix(ai): ChatGPT Responses retries errors it classified as non-retryable<br>Assignee: steipete |
| 🔀&nbsp;[#110642](https://github.com/openclaw/openclaw/pull/110642) | 0 | OpenAI-compatible/proxy | @coder-master-0915 | fix(openai-http): keep SSE argument chunking UTF-16 safe |
| 🔀&nbsp;[#110633](https://github.com/openclaw/openclaw/pull/110633) | 0 | OpenAI-compatible/proxy | @shaoohh | fix(agents): stop runs at the critical tool-loop threshold |
| 🔀&nbsp;[#110588](https://github.com/openclaw/openclaw/pull/110588) | 0 | Model routing/config | @kapelame | fix(minimax): persist OAuth model context metadata |
| 📝&nbsp;[#110578](https://github.com/openclaw/openclaw/issues/110578) | 0 | Local model runtime | @apixhed | [Bug]: No connection between ollama in linux |
| 🔀&nbsp;[#110571](https://github.com/openclaw/openclaw/pull/110571) | 0 | Local memory/embedding | @headbouyJB | fix(memory): corpus dreaming eligibility contract + heartbeat provenance test |
| 📝&nbsp;[#110564](https://github.com/openclaw/openclaw/issues/110564) | 0 | Model routing/config | @KaiserCaiser | Compaction: use single-pass summarization when the summarizer's context window fits the whole history (skip forced map-reduce) |
| 🔀&nbsp;[#110544](https://github.com/openclaw/openclaw/pull/110544) | 0 | Local memory/embedding | @RileyJJY | fix(active-memory): bound legacy toggle migration reads |
| 🔀&nbsp;[#110542](https://github.com/openclaw/openclaw/pull/110542) | 0 | Model routing/config | @wuqxuan | fix(agents): prefer ordered eligible credentials in discovery map |
| 🔀&nbsp;[#110537](https://github.com/openclaw/openclaw/pull/110537) | 0 | Local memory/embedding | @wahaha1223 | fix(memory-core): guard invalid timestamps in dreaming rankings |
| 🔀&nbsp;[#110531](https://github.com/openclaw/openclaw/pull/110531) | 0 | Local model runtime | @chegherian | fix(agents): unblock router-to-value-agent delegation + fix compaction reconcile TypeError |
| 🔀&nbsp;[#110529](https://github.com/openclaw/openclaw/pull/110529) | 0 | Local memory/embedding | @chenyangjun-xy | fix(memory-core): use longer backoff for 429 rate-limit embedding errors (#108893) |
| 🔀&nbsp;[#110521](https://github.com/openclaw/openclaw/pull/110521) | 0 | Local model runtime | @Pick-cat | fix(ollama): strip unconsumed response body on non-OK HTTP responses |
| 🔀&nbsp;[#110507](https://github.com/openclaw/openclaw/pull/110507) | 0 | OpenAI-compatible/proxy | @dwc1997 | fix(plugin-sdk): guard provider isConfigured probe against malformed config throws |
| 📝&nbsp;[#110488](https://github.com/openclaw/openclaw/issues/110488) | 0 | Model routing/config | @ari-hjunk | Provider-level credential discovery ignores auth.order, OAuth preference, and expiry — silently breaks ChatGPT-mode background paths |
| 🔀&nbsp;[#110471](https://github.com/openclaw/openclaw/pull/110471) | 0 | OpenAI-compatible/proxy | @Pick-cat | fix(ai): keep OpenAI tool call id truncation UTF-16 safe |
| 🔀&nbsp;[#110458](https://github.com/openclaw/openclaw/pull/110458) | 0 | OpenAI-compatible/proxy | @YangManBOBO | fix(config): model compat schema rejects eight fields present in the TypeScript type and consumed at runtime |
| 🔀&nbsp;[#110450](https://github.com/openclaw/openclaw/pull/110450) | 0 | Local memory/embedding | @RileyJJY | fix(memory-core): bound dreaming markdown reads |
| 🔀&nbsp;[#110321](https://github.com/openclaw/openclaw/pull/110321) | 0 | Model routing/config | @chenxiaoyu209 | fix: separate allowPluginSyntheticAuth from allowAuthProfileFallback in model auth |
| 📝&nbsp;[#110309](https://github.com/openclaw/openclaw/issues/110309) | 0 | Local memory/embedding | @sglion777 | Bug: Hybrid memory search silently fails when node:sqlite is compiled without extension loading support |
| 🔀&nbsp;[#110299](https://github.com/openclaw/openclaw/pull/110299) | 0 | OpenAI-compatible/proxy | @misbahsy | docs(providers): add Azure OpenAI setup page and directory entry |
| 🔀&nbsp;[#110244](https://github.com/openclaw/openclaw/pull/110244) | 0 | Open-weight/provider behavior | @wuqxuan | fix(agents): do not treat zero-exit exec success as tool failure |
| 🔀&nbsp;[#110216](https://github.com/openclaw/openclaw/pull/110216) | 0 | Local memory/embedding | @VACInc | fix(memory): recover from same-file legacy index divergence |
| 📝&nbsp;[#110190](https://github.com/openclaw/openclaw/issues/110190) | 0 | OpenAI-compatible/proxy | @consoleaf | Runtime context carrier positioned AFTER user message causes severe model confusion and reasoning token waste |
| 🔀&nbsp;[#110175](https://github.com/openclaw/openclaw/pull/110175) | 0 | Model routing/config | @qingminlong | fix(baseten): reject malformed model metadata numbers |
| 📝&nbsp;[#110157](https://github.com/openclaw/openclaw/issues/110157) | 0 | Open-weight/provider behavior | @maxatv | [Feature]: Bedrock provider should support guardrail input tagging (guardContent) so Prompt-attack filter doesn't false-block on the system prompt |
| 🔀&nbsp;[#110138](https://github.com/openclaw/openclaw/pull/110138) | 0 | Open-weight/provider behavior | @novalis78 | fix(openrouter): add model-aware tool schema normalization for proxied providers |
| 🔀&nbsp;[#110128](https://github.com/openclaw/openclaw/pull/110128) | 0 | Local memory/embedding | @qingminglong | fix(memory-host): accept repeated content lengths |
| 🔀&nbsp;[#110120](https://github.com/openclaw/openclaw/pull/110120) | 0 | Local memory/embedding | @chengzhichao-xydt | fix(active-memory): honor abortSignal during recall cleanup retry delays |
| 🔀&nbsp;[#110114](https://github.com/openclaw/openclaw/pull/110114) | 0 | OpenAI-compatible/proxy | @chengzhichao-xydt | fix(agents): honor abort signal during compaction summary retry backoff |
| 📝&nbsp;[#110103](https://github.com/openclaw/openclaw/issues/110103) | 0 | Model routing/config | @danieljimz | anthropic-vertex: Gateway-routed calls fail synthetic ADC auth resolution that --local and the plugin itself confirm works |
| 🔀&nbsp;[#110097](https://github.com/openclaw/openclaw/pull/110097) | 0 | Local memory/embedding | @headbouyJB | feat(memory-core): skip tool construction for dreaming narrative subagent runs (no-tools mode from #93756 review guidance) |
| 📝&nbsp;[#110074](https://github.com/openclaw/openclaw/issues/110074) | 0 | Open-weight/provider behavior | @luigidm9111 | bug: embedded agent hangs ~13min then fails with EmbeddedAttemptSessionTakeoverError after gateway restart |
| 🔀&nbsp;[#110073](https://github.com/openclaw/openclaw/pull/110073) | 0 | Local model runtime | @hugenshen | fix(ollama): use CJK-aware char estimate for usage fallback |
| 🔀&nbsp;[#110059](https://github.com/openclaw/openclaw/pull/110059) | 0 | OpenAI-compatible/proxy | @LiLan0125 | fix: preserve OpenAI Responses message boundaries |
| 🔀&nbsp;[#110031](https://github.com/openclaw/openclaw/pull/110031) | 0 | Local model runtime | @zw-xysk | fix(lmstudio): set supportsTools only for native tool-trained models |
| 🔀&nbsp;[#110020](https://github.com/openclaw/openclaw/pull/110020) | 0 | Model routing/config | @smfworks | fix(coding-agent): scope CODEX_HOME to prevent OAuth collision with OpenClaw |
| 🔀&nbsp;[#110016](https://github.com/openclaw/openclaw/pull/110016) | 0 | Model routing/config | @wahaha1223 | fix(mcp): avoid memory spikes from oversized client TLS files |
| 🔀&nbsp;[#109986](https://github.com/openclaw/openclaw/pull/109986) | 0 | Model routing/config | @LZY3538 | fix(plugin-sdk): guard provider catalog live URL parsing against malformed responses |
| 🔀&nbsp;[#109972](https://github.com/openclaw/openclaw/pull/109972) | 0 | Open-weight/provider behavior | @LiLan0125 | fix(bedrock): avoid replaying partial thinking signatures |
| 🔀&nbsp;[#109971](https://github.com/openclaw/openclaw/pull/109971) | 0 | Local model runtime | @zw-xysk | fix(ollama): models advertise tools when /api/show fails |
| 🔀&nbsp;[#109967](https://github.com/openclaw/openclaw/pull/109967) | 0 | Local model runtime | @RileyJJY | fix(ollama): release failed discovery bodies |
| 🔀&nbsp;[#109950](https://github.com/openclaw/openclaw/pull/109950) | 0 | Model routing/config | @sunlit-deng | fix(kilocode): cancel failed model discovery bodies |
| 📝&nbsp;[#109948](https://github.com/openclaw/openclaw/issues/109948) | 0 | Open-weight/provider behavior | @Andy-Xie-1145 | [Bug]: Steer message during active tool call crashes embedded agent (EmbeddedAttemptSessionTakeoverError) |
| 📝&nbsp;[#109942](https://github.com/openclaw/openclaw/issues/109942) | 0 | Local model runtime | @JasonHsu31 | [Bug]: OpenClaw v7.1 Dashboard Returns 400 Error with llamacpp due to Missing Regex Anchors in Auto-Generated GBNF Schema |
| 🔀&nbsp;[#109904](https://github.com/openclaw/openclaw/pull/109904) | 0 | OpenAI-compatible/proxy | @Yigtwxx | fix(agents): Responses turns that end incomplete report zero tokens and zero cost<br>Assignee: steipete |
| 📝&nbsp;[#109881](https://github.com/openclaw/openclaw/issues/109881) | 0 | Open-weight/provider behavior | @AWTammsaar | [Bug]: Bedrock (bedrock-converse-stream) has no thinking-signature replay protection; "Invalid signature in thinking block" permanently bricks Claude 4+ sessions |
| 🔀&nbsp;[#109865](https://github.com/openclaw/openclaw/pull/109865) | 0 | Local memory/embedding | @Serhii-Leniv | fix(memory): memory index fails to open when same-file legacy tables diverge |
| 🔀&nbsp;[#109821](https://github.com/openclaw/openclaw/pull/109821) | 0 | Open-weight/provider behavior | @Bartok9 | fix(agents): sanitize native Anthropic text_delta for MiniMax stream noise |
| 🔀&nbsp;[#109786](https://github.com/openclaw/openclaw/pull/109786) | 0 | OpenAI-compatible/proxy | @Leon-SK668 | fix(ai): preserve Unicode in provider error bodies |
| 📝&nbsp;[#109779](https://github.com/openclaw/openclaw/issues/109779) | 0 | OpenAI-compatible/proxy | @wcdma020 | feat(models): support explicit provider display order and displayName in models.providers |
| 🔀&nbsp;[#109763](https://github.com/openclaw/openclaw/pull/109763) | 0 | Model routing/config | @wuqxuan | fix: isolate coding-agent Codex CLI with dedicated CODEX_HOME |
| 🔀&nbsp;[#109745](https://github.com/openclaw/openclaw/pull/109745) | 0 | Local memory/embedding | @licheer-zte | fix: honor Retry-After header in memory embeddings batch retry (#108893) |
| 📝&nbsp;[#109726](https://github.com/openclaw/openclaw/issues/109726) | 0 | Model routing/config | @yangbo1014 | Runtime-level model fallback on API call failure |
| 📝&nbsp;[#109704](https://github.com/openclaw/openclaw/issues/109704) | 0 | Model routing/config | @wangwllu | [Bug]: bundled coding-agent Codex CLI can invalidate OpenClaw ChatGPT OAuth via ambient CODEX_HOME |
| 🔀&nbsp;[#109680](https://github.com/openclaw/openclaw/pull/109680) | 0 | Open-weight/provider behavior | @ZengWen-DT | fix(amazon-bedrock): keep blank credentials from overriding AWS auth |
| 📝&nbsp;[#109656](https://github.com/openclaw/openclaw/issues/109656) | 0 | OpenAI-compatible/proxy | @etotheo2020 | contextInjection: "continuation-skip" has no effect — full workspace bootstrap reinjected every turn regardless of setting |
| 📝&nbsp;[#109611](https://github.com/openclaw/openclaw/issues/109611) | 0 | Open-weight/provider behavior | @QQSHI13 | Add support for Kimi K3 model |
| 🔀&nbsp;[#109528](https://github.com/openclaw/openclaw/pull/109528) | 0 | Local model runtime | @ccaum | fix: thinking level silently clamps to off for Ollama-backed models |
| 📝&nbsp;[#109527](https://github.com/openclaw/openclaw/issues/109527) | 0 | Local model runtime | @ccaum | [Bug]: Ollama-backed models silently lose thinking level due to resolveCandidateThinkingLevel missing catalog |
| 🔀&nbsp;[#109514](https://github.com/openclaw/openclaw/pull/109514) | 0 | Model routing/config | @Leon-SK668 | fix(discord): preserve Unicode model picker buckets |
| 🔀&nbsp;[#109512](https://github.com/openclaw/openclaw/pull/109512) | 0 | Local memory/embedding | @fmx8747821 | fix(memory-embeddings): use longer backoff for rate-limit (429) errors |
| 📝&nbsp;[#109478](https://github.com/openclaw/openclaw/issues/109478) | 0 | Open-weight/provider behavior | @kai-ocean-kurt | Literal \n injected into multi-line tool-call string arguments at colon-then-indent boundary (2026.7.1, intermittent, cross-model) |
| 📝&nbsp;[#109436](https://github.com/openclaw/openclaw/issues/109436) | 0 | Model routing/config | @davidste | Model fallback selection ignores candidate context windows, causing overflow/compaction storms on mid-turn failover |
| 🔀&nbsp;[#109368](https://github.com/openclaw/openclaw/pull/109368) | 0 | OpenAI-compatible/proxy | @Mohl | fix: self-hosted model discovery ignores top-level context_size/context_length field |
| 📝&nbsp;[#109367](https://github.com/openclaw/openclaw/issues/109367) | 0 | OpenAI-compatible/proxy | @Mohl | [Bug]: Self-hosted/custom OpenAI-compatible model discovery ignores top-level context_size/context_length field, under-reports context window (e.g. Cortecs GLM-5.2 shows 131k instead of 1M) |
| 🔀&nbsp;[#109313](https://github.com/openclaw/openclaw/pull/109313) | 0 | Model routing/config | @SebTardif | fix(agents): do not label finish_reason error as LLM timeout |
| 🔀&nbsp;[#109312](https://github.com/openclaw/openclaw/pull/109312) | 0 | OpenAI-compatible/proxy | @Franklin-Yao | feat: add LLMRouter provider plugin |
| 🔀&nbsp;[#109283](https://github.com/openclaw/openclaw/pull/109283) | 0 | Local memory/embedding | @jgrandguillaume | feat(memory-lancedb): make auto-recall selectivity configurable |
| 📝&nbsp;[#109270](https://github.com/openclaw/openclaw/issues/109270) | 0 | Open-weight/provider behavior | @Enominera | [Bug]: ACP binding session generates new acp_session_id after gateway restart, causing resume failure with misleading 'model not found' error |
| 📝&nbsp;[#109256](https://github.com/openclaw/openclaw/issues/109256) | 0 | Model routing/config | @acidyards | [Bug]: Auto auth profile override can become stuck on an unavailable OAuth profile, preventing new agent sessions |
| 📝&nbsp;[#109228](https://github.com/openclaw/openclaw/issues/109228) | 0 | Local model runtime | @steipete | [Feature]: Apple Foundation Models provider plugin (on-device zero-key onboarding on Apple Silicon) |
| 📝&nbsp;[#109218](https://github.com/openclaw/openclaw/issues/109218) | 0 | Open-weight/provider behavior | @devodriqroberts | OpenRouter/Google finish_reason: "error" (returns in seconds) mislabeled as LLM request timed out / 408 |
| 📝&nbsp;[#109186](https://github.com/openclaw/openclaw/issues/109186) | 0 | Local model runtime | @yetisoldier | Subagent completion events silently killed by NO_REPLY instruction after sessions_yield |
| 🔀&nbsp;[#109177](https://github.com/openclaw/openclaw/pull/109177) | 0 | Local memory/embedding | @ZOOWH | fix(github-copilot): redact credential-shaped text in embedding API errors |
| 🔀&nbsp;[#109155](https://github.com/openclaw/openclaw/pull/109155) | 0 | Local model runtime | @Pick-cat | fix(ollama): bound model pull body reads past idle timeout |
| 🔀&nbsp;[#109133](https://github.com/openclaw/openclaw/pull/109133) | 0 | OpenAI-compatible/proxy | @LiLan0125 | fix(agents): fail unterminated Responses streams |
| 🔀&nbsp;[#109085](https://github.com/openclaw/openclaw/pull/109085) | 0 | Model routing/config | @wanyongstar | fix(fal): apply request policy to provider HTTP config |
| 🔀&nbsp;[#109080](https://github.com/openclaw/openclaw/pull/109080) | 0 | Model routing/config | @wanyongstar | fix(vydra): apply request policy to shared provider HTTP config |
| 📝&nbsp;[#109079](https://github.com/openclaw/openclaw/issues/109079) | 0 | Model routing/config | @claw0gang | [Bug]: Cache-inclusive cumulative usage is treated as current context size, causing false overflow and compaction |
| 🔀&nbsp;[#109074](https://github.com/openclaw/openclaw/pull/109074) | 0 | OpenAI-compatible/proxy | @lsr911 | fix(tts): bound response body read with timeout in OpenAI-compatible providers |
| 🔀&nbsp;[#109067](https://github.com/openclaw/openclaw/pull/109067) | 0 | Open-weight/provider behavior | @hugenshen | fix(agents): idle-timeout stalled provider response body reads |
| 🔀&nbsp;[#109057](https://github.com/openclaw/openclaw/pull/109057) | 0 | Local model runtime | @aspalagin | fix(agents): completions-API models leak tool-call preambles into chats — tag pre-tool narration as commentary |
| 🔀&nbsp;[#109039](https://github.com/openclaw/openclaw/pull/109039) | 0 | Model routing/config | @SunnyShu0925 | fix(gateway): add accumulatedText to non-streaming fallback for toolChoiceConstraint buffering |
| 📝&nbsp;[#109017](https://github.com/openclaw/openclaw/issues/109017) | 0 | Model routing/config | @fulgerulnegru | [Bug]: Anthropic provider disappears from model picker + models list crashes on manually-added Anthropic models + static catalog never pulls new models (Fable 5 / Haiku 4.5) |
| 🔀&nbsp;[#109014](https://github.com/openclaw/openclaw/pull/109014) | 0 | Model routing/config | @xydt-juyaohui | fix(agents): reject non-decimal OpenRouter pricing tokens |
| 🔀&nbsp;[#109009](https://github.com/openclaw/openclaw/pull/109009) | 0 | Local memory/embedding | @wangyan2026 | fix(agents): exclude MEMORY.md from shared channel session bootstrap |
| 🔀&nbsp;[#109004](https://github.com/openclaw/openclaw/pull/109004) | 0 | OpenAI-compatible/proxy | @LZY3538 | fix: suppress Chat Completions tool-call preambles |
| 🔀&nbsp;[#108989](https://github.com/openclaw/openclaw/pull/108989) | 0 | OpenAI-compatible/proxy | @lee-xydt | fix(agents): treat unterminated Responses SSE stream as error, not success |
| 🔀&nbsp;[#108962](https://github.com/openclaw/openclaw/pull/108962) | 0 | Local model runtime | @ChengKe771 | fix(ollama): update bundled static MiniMax Cloud default from m2.7 to m3 |
| 📝&nbsp;[#108958](https://github.com/openclaw/openclaw/issues/108958) | 0 | OpenAI-compatible/proxy | @zjx111234 | [Bug]: Interrupted Responses SSE (502 stream_interrupted) is persisted as an empty successful response |
| 📝&nbsp;[#108945](https://github.com/openclaw/openclaw/issues/108945) | 0 | OpenAI-compatible/proxy | @junwei1213 | Chat Completions transport never tags mid-turn commentary — tool-call preambles are delivered to chats (Responses transport tags them correctly) |
| 📝&nbsp;[#108893](https://github.com/openclaw/openclaw/issues/108893) | 0 | Local memory/embedding | @developercrocodiles | [Bug]: Memory embeddings are destined to fail. |
| 🔀&nbsp;[#108789](https://github.com/openclaw/openclaw/pull/108789) | 0 | Local model runtime | @Bartok9 | fix(status): hydrate thinking catalog for Ollama status card surface |
| 🔀&nbsp;[#108782](https://github.com/openclaw/openclaw/pull/108782) | 0 | Local memory/embedding | @jgrandguillaume | feat(memory-lancedb): scope memory_recall and memory_forget in a shared store |
| 🔀&nbsp;[#108732](https://github.com/openclaw/openclaw/pull/108732) | 0 | Local model runtime | @SymbolStar | fix(cron): tighten cron tool schema to prevent llama.cpp GBNF grammar overflow (#108690) |
| 📝&nbsp;[#108705](https://github.com/openclaw/openclaw/issues/108705) | 0 | Local model runtime | @Serial17 | [Bug]: 2026.7.1 — Codex plugin fails: "does not provide an export named 'formatToolExecutionErrorMessage'" in agent-harness-runtime |
| 📝&nbsp;[#108695](https://github.com/openclaw/openclaw/issues/108695) | 0 | Local model runtime | @Tangjian18 | [Bug]: The agent run failed before producing a reply. |
| 🔀&nbsp;[#108687](https://github.com/openclaw/openclaw/pull/108687) | 0 | OpenAI-compatible/proxy | @LiuwqGit | fix(ai): prevent crash from circular references in provider error handlers |
| 🔀&nbsp;[#108671](https://github.com/openclaw/openclaw/pull/108671) | 0 | Local model runtime | @wsyjh8 | fix(agents): make model-facing tool schemas llama.cpp GBNF-compatible (#108580) |
| 📝&nbsp;[#108645](https://github.com/openclaw/openclaw/issues/108645) | 0 | Local memory/embedding | @chac4l | 2026.7.2-beta.1 startup migration rejects Memory Core FTS triggers created by the same build |
| 📝&nbsp;[#108644](https://github.com/openclaw/openclaw/issues/108644) | 0 | Local model runtime | @bminicore | Clarify or update bundled Ollama Cloud MiniMax static default model |
| 🔀&nbsp;[#108624](https://github.com/openclaw/openclaw/pull/108624) | 0 | Local model runtime | @abhi-0203 | fix(cron): fix cron tool schema for llama.cpp GBNF compatibility |
| 📝&nbsp;[#108614](https://github.com/openclaw/openclaw/issues/108614) | 0 | OpenAI-compatible/proxy | @kopl-blip | [Bug]: ChatGPT/Codex OAuth ignores transport="websocket"; OpenClaw runtime still sends HTTP POST |
| 📝&nbsp;[#108599](https://github.com/openclaw/openclaw/issues/108599) | 0 | Model routing/config | @WoodyKim554 | sessions_send announce delivery causes 2-3x turn amplification on claude-cli agents (session-limit exhaustion observed) |
| 📝&nbsp;[#108580](https://github.com/openclaw/openclaw/issues/108580) | 0 | Local model runtime | @arbilli82 | [Bug]: cron tool schema incompatible with llama.cpp grammar-constrained tool calling (2026.7.1 regression) |
| 📝&nbsp;[#108568](https://github.com/openclaw/openclaw/issues/108568) | 0 | Model routing/config | @waeckerlinfederowicz66-sketch | [Feature]: Add Image to Video AI video generation provider |
| 🔀&nbsp;[#108557](https://github.com/openclaw/openclaw/pull/108557) | 0 | Model routing/config | @arkyu2077 | fix: avoid reporting model context window as session context usage |
| 📝&nbsp;[#108555](https://github.com/openclaw/openclaw/issues/108555) | 0 | Local model runtime | @grevock68 | Subagent runtime: exec-tool stalls inside subagent sessions while write-tool and LLM traffic continue to function |
| 📝&nbsp;[#108473](https://github.com/openclaw/openclaw/issues/108473) | 0 | Local model runtime | @danydavila | [Bug]: cron tool schema breaks llama.cpp tool-calling |
| 🔀&nbsp;[#108469](https://github.com/openclaw/openclaw/pull/108469) | 0 | Local model runtime | @DecentralizedJM | fix(agents): route llama.cpp GBNF cleaning through provider tool-schema hooks |
| 🔀&nbsp;[#108462](https://github.com/openclaw/openclaw/pull/108462) | 0 | OpenAI-compatible/proxy | @fanyangCS | fix(ai): recover stale Responses reasoning replay in streamSimple |
| 🔀&nbsp;[#108461](https://github.com/openclaw/openclaw/pull/108461) | 0 | OpenAI-compatible/proxy | @snotty | fix(openai-responses): flush completed tool calls instead of throwing on response.completed |
| 📝&nbsp;[#108460](https://github.com/openclaw/openclaw/issues/108460) | 0 | OpenAI-compatible/proxy | @snotty | Bug: gpt-5.6-sol fails every turn with "Responses stream completed with unresolved tool calls" |
| 📝&nbsp;[#108443](https://github.com/openclaw/openclaw/issues/108443) | 0 | OpenAI-compatible/proxy | @aikohoshinoai-prog | [persistence] thinkingSignature truncated at persist time (literal U+2026 in stored base64) → deterministic 'Invalid signature in thinking block' 400 once prompt cache expires |
| 📝&nbsp;[#108384](https://github.com/openclaw/openclaw/issues/108384) | 0 | OpenAI-compatible/proxy | @itss78-code | exec tool call never completes in embedded `openclaw agent --session-id` runs — stuck at tool:exec:started until stuck-session watchdog abort (v2026.6.11) |
| 📝&nbsp;[#108379](https://github.com/openclaw/openclaw/issues/108379) | 0 | OpenAI-compatible/proxy | @haldana88 | [Bug]: Duplicate assistant generation attempts for Xiaomi MiMo (openai-completions) cause repeated narrative text before abort |
| 📝&nbsp;[#108367](https://github.com/openclaw/openclaw/issues/108367) | 0 | Local model runtime | @ProFire | [Bug]: Unanchored regex pattern in schema causes 400 from Ornith1.0 model running llama.cpp when cron tool is enabled |
| 📝&nbsp;[#108337](https://github.com/openclaw/openclaw/issues/108337) | 0 | Local model runtime | @pr10mail5 | [Bug]: WhatsApp /think menu shows "off" for Ollama live-discovered models despite thinkingDefault: "high" and reasoning: true — regression in v2026.7.1 |
| 📝&nbsp;[#108331](https://github.com/openclaw/openclaw/issues/108331) | 0 | Model routing/config | @Enominera | Session state corrupted to 'unknown' after provider 503, permanently blocks new messages |
| 🔀&nbsp;[#108323](https://github.com/openclaw/openclaw/pull/108323) | 0 | Local model runtime | @hxy91819 | fix: prevent cumulative usage from inflating session context<br>Assignee: hxy91819 |
| 📝&nbsp;[#108262](https://github.com/openclaw/openclaw/issues/108262) | 0 | Model routing/config | @DerekEXS | Bug: Agent fallback chain fires on every model.completed (including primary success) — duplicate responses and wasted tokens |
| 🔀&nbsp;[#108229](https://github.com/openclaw/openclaw/pull/108229) | 0 | Local memory/embedding | @xxxxxmax | fix(memory): use FTS-only when optional embeddings are unavailable |
| 🔀&nbsp;[#108222](https://github.com/openclaw/openclaw/pull/108222) | 0 | Local memory/embedding | @xydt-juyaohui | fix(memory-core): reject non-decimal recall store line numbers and counts |
| 📝&nbsp;[#108216](https://github.com/openclaw/openclaw/issues/108216) | 0 | Open-weight/provider behavior | @rayvader | [Bug]: Bedrock Mantle discovers GPT-5.6 models but no supported transport can invoke them |
| 📝&nbsp;[#108215](https://github.com/openclaw/openclaw/issues/108215) | 0 | OpenAI-compatible/proxy | @itanyplus | [Bug]: Context usage drops from 57% to 13% without compaction after large tool output |
| 🔀&nbsp;[#108178](https://github.com/openclaw/openclaw/pull/108178) | 0 | Model routing/config | @Gary-Jia-new | fix(session): avoid storing model contextWindow as contextTokens without usage data |
| 📝&nbsp;[#108148](https://github.com/openclaw/openclaw/issues/108148) | 0 | Model routing/config | @woohahahaaa | [Bug]: session entry's contextTokens shows model contextWindow when no fresh usage snapshot — false "context full" warnings |
| 🔀&nbsp;[#108141](https://github.com/openclaw/openclaw/pull/108141) | 0 | Model routing/config | @zhanxingxin1998 | fix(config): fall back to provider-level contextWindow/maxTokens in model defaults |
| 📝&nbsp;[#108128](https://github.com/openclaw/openclaw/issues/108128) | 0 | OpenAI-compatible/proxy | @waeckerlinfederowicz66-sketch | [Feature]: Add FlowSpeech text-to-speech provider |
| 📝&nbsp;[#108117](https://github.com/openclaw/openclaw/issues/108117) | 0 | OpenAI-compatible/proxy | @realmehmetali | [Feature]: Add stateless bounded research responses mode |
| 📝&nbsp;[#108068](https://github.com/openclaw/openclaw/issues/108068) | 0 | Local memory/embedding | @aaajiao | [Bug]: memory_search intermittently returns "database is not open" on healthy index in 2026.7.1 |
| 🔀&nbsp;[#108066](https://github.com/openclaw/openclaw/pull/108066) | 0 | OpenAI-compatible/proxy | @gachon-star-want | feat(providers): add PleumRouter bundled provider plugin |
| 📝&nbsp;[#108033](https://github.com/openclaw/openclaw/issues/108033) | 0 | Local model runtime | @wayni208 | Ollama provider: ProviderAuthError on configured apiKey; model missing from Control UI picker despite allowlist |
| 🔀&nbsp;[#107910](https://github.com/openclaw/openclaw/pull/107910) | 0 | Local memory/embedding | @arkyu2077 | fix(memory-core): clamp dreaming lead head safely |
| 📝&nbsp;[#107899](https://github.com/openclaw/openclaw/issues/107899) | 0 | Local model runtime | @rainbow0432-dev | Embedded-agent runtime missing llm_output, before_agent_finalize, and agent_end hook firing for non-Codex providers |
| 🔀&nbsp;[#107897](https://github.com/openclaw/openclaw/pull/107897) | 0 | Model routing/config | @wahaha1223 | fix(models): reject oversized piped auth secrets |
| 🔀&nbsp;[#107882](https://github.com/openclaw/openclaw/pull/107882) | 0 | Local memory/embedding | @moguangyu5-design | fix(memory-core): use surrogate-safe UTF-16 slicing in short-term promotion |
| 📝&nbsp;[#107876](https://github.com/openclaw/openclaw/issues/107876) | 0 | Local memory/embedding | @moguangyu5-design | Memory-core short-term promotion can slice inside UTF-16 surrogate pairs |
| 📝&nbsp;[#107839](https://github.com/openclaw/openclaw/issues/107839) | 0 | OpenAI-compatible/proxy | @hashtag1974 | Successful OpenAI responses do not clear auth_profile_state cooldown after subscription_limit |
| 🔀&nbsp;[#107834](https://github.com/openclaw/openclaw/pull/107834) | 0 | Model routing/config | @Pluviobyte | fix(github-copilot): honor catalog max thinking effort |
| 🔀&nbsp;[#107821](https://github.com/openclaw/openclaw/pull/107821) | 0 | Local model runtime | @harjothkhara | fix(agents): avoid premature compaction in tool-heavy sessions |
| 🔀&nbsp;[#107800](https://github.com/openclaw/openclaw/pull/107800) | 0 | OpenAI-compatible/proxy | @harjothkhara | fix(ai): make provider stream error formatting total |
| 📝&nbsp;[#107792](https://github.com/openclaw/openclaw/issues/107792) | 0 | OpenAI-compatible/proxy | @ncksol | [Bug]: GitHub Copilot discards catalog-advertised max thinking for GPT-5.6 Sol |
| 📝&nbsp;[#107713](https://github.com/openclaw/openclaw/issues/107713) | 0 | OpenAI-compatible/proxy | @matthimelstein1 | [Bug]: models.providers.<id>.timeoutSeconds ignored for channel sessions (static-catalog model keeps 120s idle watchdog) |
| 🔀&nbsp;[#107671](https://github.com/openclaw/openclaw/pull/107671) | 0 | Model routing/config | @Glucksberg | fix(models): clear stale auth cooldowns after early limit resets |
| 📝&nbsp;[#107668](https://github.com/openclaw/openclaw/issues/107668) | 0 | Model routing/config | @josh-cornelius | [Feature]: claude-cli runtime should consume per-agent auth profiles for turn auth (multiple subscription accounts on one gateway) |
| 🔀&nbsp;[#107588](https://github.com/openclaw/openclaw/pull/107588) | 0 | Model routing/config | @VACInc | fix(agents): preserve native runtime controls on Codex routes |
| 📝&nbsp;[#107491](https://github.com/openclaw/openclaw/issues/107491) | 0 | OpenAI-compatible/proxy | @aniruddhaadak80 | [Bug] Stale OAuth tokens stored in memory cache when oauth.ts refresh fails |
| 🔀&nbsp;[#107473](https://github.com/openclaw/openclaw/pull/107473) | 0 | Local model runtime | @wahaha1223 | fix(ollama): stop oversized stream records from growing memory |
| 📝&nbsp;[#107430](https://github.com/openclaw/openclaw/issues/107430) | 0 | Local model runtime | @knight-666 | [Bug]: Unable to connect to llama.cpp |
| 📝&nbsp;[#107408](https://github.com/openclaw/openclaw/issues/107408) | 0 | Model routing/config | @jarvis-drakon | Scoped agent-harness plugin activation silently evicts unrelated plugins' CLI backends from the global runtime registry |
| 🔀&nbsp;[#107378](https://github.com/openclaw/openclaw/pull/107378) | 0 | Model routing/config | @jzakirov | feat(minimax): route /fast to MiniMax's faster paid lanes with correct pricing |
| 📝&nbsp;[#107334](https://github.com/openclaw/openclaw/issues/107334) | 0 | OpenAI-compatible/proxy | @alexandre-leng | [Feature request] UX : Simplify multi-provider LLM management in the OpenClaw dashboard |
| 🔀&nbsp;[#107329](https://github.com/openclaw/openclaw/pull/107329) | 0 | Local memory/embedding | @zhangqueping | fix(memory): recover real on-disk path for slugified QMD search results |
| 📝&nbsp;[#107281](https://github.com/openclaw/openclaw/issues/107281) | 0 | Local model runtime | @hypothesis-next | [Bug]: memsearch-summarize sub-session compaction fails with "No API provider registered for api: ollama" on 2026.7.1, while main-session compaction with the same provider succeeds |
| 🔀&nbsp;[#107209](https://github.com/openclaw/openclaw/pull/107209) | 0 | Model routing/config | @NehoraiHadad | Suppress model fallback notices in rooms |
| 🔀&nbsp;[#107152](https://github.com/openclaw/openclaw/pull/107152) | 0 | Local memory/embedding | @BlackFrameAI | fix(memory): hide QMD transport metadata from recalled content |
| 📝&nbsp;[#107099](https://github.com/openclaw/openclaw/issues/107099) | 0 | Open-weight/provider behavior | @xyzhaang | [Bug]: `image` tool returns 401 for `moonshot/kimi-k2.6` despite valid API key |
| 📝&nbsp;[#107093](https://github.com/openclaw/openclaw/issues/107093) | 0 | Local memory/embedding | @jamesachurchill | [Feature]: Support native contextual memory embeddings |
| 📝&nbsp;[#107082](https://github.com/openclaw/openclaw/issues/107082) | 0 | Local memory/embedding | @jamesachurchill | [Feature]: Support non-durable native dreaming mode / explicit phase controls |
| 🔀&nbsp;[#107052](https://github.com/openclaw/openclaw/pull/107052) | 0 | OpenAI-compatible/proxy | @LeonidasLux | fix(elevenlabs): validate baseUrl with user-friendly error for malformed endpoints |
| 📝&nbsp;[#107036](https://github.com/openclaw/openclaw/issues/107036) | 0 | Model routing/config | @aniruddhaadak80 | [Bug] Agent context window fragmentation during concurrent subagent tool calls |
| 🔀&nbsp;[#106982](https://github.com/openclaw/openclaw/pull/106982) | 0 | OpenAI-compatible/proxy | @arkyu2077 | fix: validate ElevenLabs baseUrl before realtime or speech requests |
| 🔀&nbsp;[#106963](https://github.com/openclaw/openclaw/pull/106963) | 0 | Model routing/config | @SunnyShu0925 | fix(agents): repair interrupted tool calls at provider-bound replay seam |
| 🔀&nbsp;[#106946](https://github.com/openclaw/openclaw/pull/106946) | 0 | OpenAI-compatible/proxy | @dwc1997 | fix(elevenlabs): validate baseUrl with descriptive errors for malformed endpoints (fixes #106943) |
| 📝&nbsp;[#106943](https://github.com/openclaw/openclaw/issues/106943) | 0 | OpenAI-compatible/proxy | @dwc1997 | [Bug]: ElevenLabs baseUrl accepts invalid URLs without validation — missing user-friendly error for malformed endpoints |
| 📝&nbsp;[#106937](https://github.com/openclaw/openclaw/issues/106937) | 0 | Local memory/embedding | @BlackFrameAI | [Bug]: QMD transport metadata leaks into memory search and dreaming |
| 🔀&nbsp;[#106930](https://github.com/openclaw/openclaw/pull/106930) | 0 | Model routing/config | @snotty | fix: preserve discovered context limits over static metadata |
| 📝&nbsp;[#106911](https://github.com/openclaw/openclaw/issues/106911) | 0 | Local model runtime | @alphabid-arch | [Bug]: 2026.6.11 agent --local times out before provider request with Ollama after fix for #97871 |
| 📝&nbsp;[#106894](https://github.com/openclaw/openclaw/issues/106894) | 0 | Open-weight/provider behavior | @najef1979-code | [Bug]: Cannot change Agent Image |
| 📝&nbsp;[#106866](https://github.com/openclaw/openclaw/issues/106866) | 0 | Local memory/embedding | @BlueboxC | [Bug]: Native QMD returns active slugified paths that do not exist on disk |
| 🔀&nbsp;[#106752](https://github.com/openclaw/openclaw/pull/106752) | 0 | Model routing/config | @steipete | fix(ui): show readable model fallback removal action<br>Assignee: steipete |
| 🔀&nbsp;[#106706](https://github.com/openclaw/openclaw/pull/106706) | 0 | Model routing/config | @alithia-dev | Harden Hermes daemon adapter: validate model on session resume (AIA-1231) |
| 📝&nbsp;[#106704](https://github.com/openclaw/openclaw/issues/106704) | 0 | Open-weight/provider behavior | @Cyb3rb1ade | [Bug]: sessions_yield on a subagent's first turn (no children, no wake source) silently finalizes the run as ok with an empty result — tool descriptions invite the misuse |
| 📝&nbsp;[#106679](https://github.com/openclaw/openclaw/issues/106679) | 0 | Model routing/config | @aniruddhaadak80 | [Bug] Infinite fallback loop on generic provider errors |
| 🔀&nbsp;[#106657](https://github.com/openclaw/openclaw/pull/106657) | 0 | Model routing/config | @harjothkhara | fix: stop model fallback on sandbox provisioning failures |
| 📝&nbsp;[#106617](https://github.com/openclaw/openclaw/issues/106617) | 0 | OpenAI-compatible/proxy | @aniruddhaadak80 | [Bug] Global SSL Verification Disabling Bypass in openai-compatible-embedding-provider.ts |
| 📝&nbsp;[#106570](https://github.com/openclaw/openclaw/issues/106570) | 0 | OpenAI-compatible/proxy | @aniruddhaadak80 | [Bug] Circular Structure Serialization Crash in OpenAI Completions Stream Error Handler |
| 📝&nbsp;[#106569](https://github.com/openclaw/openclaw/issues/106569) | 0 | OpenAI-compatible/proxy | @aniruddhaadak80 | [Bug] False-Positive Message Merge/Collapse Bug in resolveResponsesMessageSnapshotCollapse |
| 📝&nbsp;[#106516](https://github.com/openclaw/openclaw/issues/106516) | 0 | Model routing/config | @devodriqroberts | Bug: sandbox image missing classified as model.fallback_step; burns full model fallback chain |
| 🔀&nbsp;[#106414](https://github.com/openclaw/openclaw/pull/106414) | 0 | Model routing/config | @zaktrue | fix: models fallbacks --agent silently edits global defaults instead of the agent |
| 🔀&nbsp;[#106404](https://github.com/openclaw/openclaw/pull/106404) | 0 | Local memory/embedding | @bladin | fix(memory-core): dreaming narrative subagent receives full generic prompt instead of minimal |
| 🔀&nbsp;[#106391](https://github.com/openclaw/openclaw/pull/106391) | 0 | Model routing/config | @zilokki-bot | fix(model-catalog): keep profile-specific model rows distinct |
| 📝&nbsp;[#106374](https://github.com/openclaw/openclaw/issues/106374) | 0 | Model routing/config | @VanessaHammes | [Bug]: openai/gpt-5.6-terra listed by OpenAI provider but Gateway run fails with missing models.providers.openai.models[] entry |
| 🔀&nbsp;[#106364](https://github.com/openclaw/openclaw/pull/106364) | 0 | OpenAI-compatible/proxy | @wonfong | fix(agents): preserve yielded subagent continuations |
| 📝&nbsp;[#106346](https://github.com/openclaw/openclaw/issues/106346) | 0 | Model routing/config | @zaktrue | openclaw models fallbacks {list,add,remove,clear} ignores --agent, always operates on agents.defaults.model.fallbacks |
| 🔀&nbsp;[#106284](https://github.com/openclaw/openclaw/pull/106284) | 0 | Model routing/config | @gangcaiyoule | fix(cli): stop stale session retry loops after failover |
| 📝&nbsp;[#106239](https://github.com/openclaw/openclaw/issues/106239) | 0 | Local memory/embedding | @yailas | [Bug] memory_search permanently broken for default main agent: index identity auto-vacated on every gateway restart |
| 📝&nbsp;[#106204](https://github.com/openclaw/openclaw/issues/106204) | 0 | Model routing/config | @ditingdapeng | [Bug]: Opaque error message when tool output causes unrecoverable context overflow |
| 📝&nbsp;[#106149](https://github.com/openclaw/openclaw/issues/106149) | 0 | Open-weight/provider behavior | @emyjflovver75-dotcom | [Bug]: [Bug]: Embedded agent gets "401 User not found" from OpenRouter despite valid API key |
| 📝&nbsp;[#106080](https://github.com/openclaw/openclaw/issues/106080) | 0 | OpenAI-compatible/proxy | @dltlaos11 | [Bug]: Model cost reports $0 since 2026.6.10 — model_capability_cache never populates (persists on 2026.6.11) |
| 🔀&nbsp;[#106023](https://github.com/openclaw/openclaw/pull/106023) | 0 | Model routing/config | @teaspoonai | feat: advertise realtime voice provider voices in talk.catalog |
| 📝&nbsp;[#106009](https://github.com/openclaw/openclaw/issues/106009) | 0 | OpenAI-compatible/proxy | @andrea-kingautomation | Effort/thinking level clamps are silent across all providers (no warning when xhigh/max is reduced) |
| 📝&nbsp;[#106008](https://github.com/openclaw/openclaw/issues/106008) | 0 | Model routing/config | @andrea-kingautomation | Feature: expose the per-spawn resolved model to the ACP agent launch env (startup-flag lane, complements session/set_model) |
| 📝&nbsp;[#105999](https://github.com/openclaw/openclaw/issues/105999) | 0 | Local model runtime | @Bruce-G-S | [Feature]: Could a ollama simulation billing setting be added to assess the cost of expenses |
| 🔀&nbsp;[#105896](https://github.com/openclaw/openclaw/pull/105896) | 0 | Local memory/embedding | @momothemage | fix(memory-lancedb): make table initialization atomic |
| 🔀&nbsp;[#105895](https://github.com/openclaw/openclaw/pull/105895) | 0 | Local memory/embedding | @xydt-tanshanshan | fix(memory): backfill provider.model with resolved model name |
| 🔀&nbsp;[#105887](https://github.com/openclaw/openclaw/pull/105887) | 0 | Open-weight/provider behavior | @Alix-007 | fix(deepinfra): apply request policy to video generation requests |
| 🔀&nbsp;[#105824](https://github.com/openclaw/openclaw/pull/105824) | 0 | Local model runtime | @SymbolStar | fix(openai-transport): keep configured completion cap when context budget covers request (#105729) |
| 🔀&nbsp;[#105807](https://github.com/openclaw/openclaw/pull/105807) | 0 | Local model runtime | @moguangyu5-design | fix(config): apply provider-level contextWindow/maxTokens defaults to models |
| 📝&nbsp;[#105803](https://github.com/openclaw/openclaw/issues/105803) | 0 | Local model runtime | @moguangyu5-design | Provider-level contextWindow/maxTokens are ignored when applying model defaults |
| 🔀&nbsp;[#105796](https://github.com/openclaw/openclaw/pull/105796) | 0 | OpenAI-compatible/proxy | @morluto | perf(agents): reuse prepared plugin metadata for middleware |
| 📝&nbsp;[#105729](https://github.com/openclaw/openclaw/issues/105729) | 0 | OpenAI-compatible/proxy | @glebsergeevich | [Bug]: OpenAI-compatible proxy transport clamps max_completion_tokens to 1 after context precheck |
| 📝&nbsp;[#105680](https://github.com/openclaw/openclaw/issues/105680) | 0 | Local memory/embedding | @aniruddhaadak80 | [Bug] Multi-Process Table Initialization Race Condition in LanceDB Memory Store |
| 📝&nbsp;[#105666](https://github.com/openclaw/openclaw/issues/105666) | 0 | Model routing/config | @aniruddhaadak80 | [Bug] Bricked OAuth Token Family on Slow Network Refresh API Call (Lock-Compromised Race Condition) |
| 📝&nbsp;[#105514](https://github.com/openclaw/openclaw/issues/105514) | 0 | Model routing/config | @mauricelsy | Model fallback skips OpenAI provider cooldown even when another auth profile is healthy |
| 📝&nbsp;[#105513](https://github.com/openclaw/openclaw/issues/105513) | 0 | Local memory/embedding | @OskarSwierad | [Bug]: Dreaming - system prompt includes a lot of redundant instructions, irrelevant or invalid for dreams |
| 📝&nbsp;[#105496](https://github.com/openclaw/openclaw/issues/105496) | 0 | OpenAI-compatible/proxy | @gustav-bliss | Config hot-reload re-resolution loses ChatGPT-OAuth (codex) routing for gpt-5.6-sol; boot-time resolution is correct (2026.7.1-beta.2) |
| 📝&nbsp;[#105494](https://github.com/openclaw/openclaw/issues/105494) | 0 | Local memory/embedding | @kip-claw | [Feature]: Interactive "memory therapy" session to resolve open questions & contradictions with the user |
| 📝&nbsp;[#105378](https://github.com/openclaw/openclaw/issues/105378) | 0 | Model routing/config | @Papilionidae | ModelSelectionLockedError when sending messages in adopted Claude Code sessions |
| 📝&nbsp;[#105338](https://github.com/openclaw/openclaw/issues/105338) | 0 | Open-weight/provider behavior | @mputiyon1985 | Anthropic requests hardcode thinking.type="enabled", causing 400+retry on every claude-sonnet-5 call |
| 🔀&nbsp;[#105316](https://github.com/openclaw/openclaw/pull/105316) | 0 | Local memory/embedding | @ZOOWH | fix(active-memory): bound timeout circuit breakers |
| 🔀&nbsp;[#105243](https://github.com/openclaw/openclaw/pull/105243) | 0 | Open-weight/provider behavior | @NianJiuZst | fix(text): strip MiniMax marker from channel replies<br>Assignee: hxy91819 |
| 📝&nbsp;[#105203](https://github.com/openclaw/openclaw/issues/105203) | 0 | Model routing/config | @aniruddhaadak80 | [Enhancement]: Dynamically cap metadata lengths in agent steering queue |
| 🔀&nbsp;[#105171](https://github.com/openclaw/openclaw/pull/105171) | 0 | OpenAI-compatible/proxy | @hugenshen | fix(embeddings): bound openai-compatible requests without AbortSignal |
| 📝&nbsp;[#105164](https://github.com/openclaw/openclaw/issues/105164) | 0 | Open-weight/provider behavior | @Papilionidae | Claude Code v2.x sessions not showing in session catalog (entrypoint: "cli" not recognized) |
| 📝&nbsp;[#105131](https://github.com/openclaw/openclaw/issues/105131) | 0 | Open-weight/provider behavior | @mtnezdilarduya | cron add one-shot with sessionTarget:"current" + agentTurn causes phantom sessions and message duplication |
| 🔀&nbsp;[#105125](https://github.com/openclaw/openclaw/pull/105125) | 0 | Open-weight/provider behavior | @wangmiao0668000666 | fix(moonshot): forward abort signal through Kimi web search provider |
| 🔀&nbsp;[#105098](https://github.com/openclaw/openclaw/pull/105098) | 0 | Local memory/embedding | @ZOOWH | fix(memory-wiki): honor deadline and skip supplement exhaustive fallback |
| 🔀&nbsp;[#105070](https://github.com/openclaw/openclaw/pull/105070) | 0 | Model routing/config | @LavyaTandel | fix(oauth): make getOAuthApiKey refresh within the standard margin (issue #103846) |
| 🔀&nbsp;[#105040](https://github.com/openclaw/openclaw/pull/105040) | 0 | Open-weight/provider behavior | @moguangyu5-design | fix(config): apply Mistral maxTokens safe cap for all values |
| 📝&nbsp;[#105036](https://github.com/openclaw/openclaw/issues/105036) | 0 | Model routing/config | @moguangyu5-design | Mistral maxTokens safe cap is bypassed for values between safe max and context window |
| 📝&nbsp;[#104992](https://github.com/openclaw/openclaw/issues/104992) | 0 | Model routing/config | @forrystudio | [Bug]: Transcript redaction (`***`) is replayed into model context on session resume — model reuses masked values in new tool calls |
| 🔀&nbsp;[#104916](https://github.com/openclaw/openclaw/pull/104916) | 0 | Model routing/config | @lumin24 | fix: omit model.maxTokens as default completions output reservation |
| 🔀&nbsp;[#104904](https://github.com/openclaw/openclaw/pull/104904) | 0 | OpenAI-compatible/proxy | @MonkeyLeeT | fix(groq): keep default Llama agent turns within TPM limit |
| 🔀&nbsp;[#104829](https://github.com/openclaw/openclaw/pull/104829) | 0 | Local model runtime | @Leon-SK668 | fix(ollama): resolve web search secret refs |
| 🔀&nbsp;[#104820](https://github.com/openclaw/openclaw/pull/104820) | 0 | OpenAI-compatible/proxy | @Leon-SK668 | fix(searxng): fail closed on unresolved base url refs |
| 🔀&nbsp;[#104812](https://github.com/openclaw/openclaw/pull/104812) | 0 | Open-weight/provider behavior | @Leon-SK668 | fix(moonshot): resolve Kimi search secret refs |
| 📝&nbsp;[#104719](https://github.com/openclaw/openclaw/issues/104719) | 0 | Local memory/embedding | @context-down | [Bug]: memory-wiki supplement exhaustive fallback ignores tool deadline |
| 🔀&nbsp;[#104667](https://github.com/openclaw/openclaw/pull/104667) | 0 | Open-weight/provider behavior | @Leon-SK668 | fix(minimax): resolve search env secret refs |
| 🔀&nbsp;[#104569](https://github.com/openclaw/openclaw/pull/104569) | 0 | Model routing/config | @samrusani | fix(ui): explain replace-mode filtering in model picker |
| 📝&nbsp;[#104545](https://github.com/openclaw/openclaw/issues/104545) | 0 | Model routing/config | @100yenadmin | [Bug]: Model picker silently hides newer models when models.mode=replace |
| 📝&nbsp;[#104533](https://github.com/openclaw/openclaw/issues/104533) | 0 | OpenAI-compatible/proxy | @woohahahaaa | [Bug] Prompt Cache hit rate nearly zero when using third-party relay proxy with GPT models (works fine with OpenCode/Codex CLI) |
| 🔀&nbsp;[#104530](https://github.com/openclaw/openclaw/pull/104530) | 0 | Open-weight/provider behavior | @tzy-17 | fix(transport): strip MiniMax stream-boundary marker and sanitize text_delta |
| 📝&nbsp;[#104403](https://github.com/openclaw/openclaw/issues/104403) | 0 | Open-weight/provider behavior | @konggil | [Bug]: [e~[` stream-boundary marker from minimax-portal leaks into assistantTexts on anthropic-messages transport |
| 📝&nbsp;[#104389](https://github.com/openclaw/openclaw/issues/104389) | 0 | OpenAI-compatible/proxy | @forrystudio | [Bug]: Auto-backgrounded exec failure posts raw system card (internal agent id + command line) to end user |
| 🔀&nbsp;[#104335](https://github.com/openclaw/openclaw/pull/104335) | 0 | Model routing/config | @owen-ever | fix(openai): guard Codex GPT-5.6 discovery boundary |
| 📝&nbsp;[#104312](https://github.com/openclaw/openclaw/issues/104312) | 0 | Model routing/config | @ssavitang | [Feature]: Intent-scoped MCP activation for large MCP catalogs |
| 🔀&nbsp;[#104292](https://github.com/openclaw/openclaw/pull/104292) | 0 | Local memory/embedding | @tzy-17 | fix(active-memory): log circuit-breaker trips and aborts at warn level |
| 📝&nbsp;[#104212](https://github.com/openclaw/openclaw/issues/104212) | 0 | Local model runtime | @Velkan | [Bug] Cron agentTurn force-resolves thinking default for Ollama models, causing empty responses |
| 📝&nbsp;[#104165](https://github.com/openclaw/openclaw/issues/104165) | 0 | Local model runtime | @yidp | [Bug]: Weather Tool (china-weather/weather) Not Found in Catalog |
| 🔀&nbsp;[#104149](https://github.com/openclaw/openclaw/pull/104149) | 0 | Model routing/config | @LZY3538 | fix(agents): honor Anthropic Retry-After in auto-retry backoff (#103849) |
| 🔀&nbsp;[#104076](https://github.com/openclaw/openclaw/pull/104076) | 0 | Open-weight/provider behavior | @sheyanmin | fix(agents): distinguish z.ai code 1305 content rejection from generic overload |
| 📝&nbsp;[#103917](https://github.com/openclaw/openclaw/issues/103917) | 0 | Local model runtime | @dandesilva | Gateway crashes on unhandled FsSafeError: root dir not found when a subagent spawns after its role-named workspace directory is deleted |
| 📝&nbsp;[#103911](https://github.com/openclaw/openclaw/issues/103911) | 0 | Local memory/embedding | @Andy-Xie-1145 | Dreaming sweep triggers EmbeddedAttemptSessionTakeoverError when user is actively chatting in main session |
| 📝&nbsp;[#103879](https://github.com/openclaw/openclaw/issues/103879) | 0 | Model routing/config | @1127426159 | Migration from old catalog.json to plugin system leaves stale `plugins.entries.<name>` config causing auth failures |
| 🔀&nbsp;[#103852](https://github.com/openclaw/openclaw/pull/103852) | 0 | OpenAI-compatible/proxy | @lonexreb | fix(agents): count env/config credentials in plugin tool provider-auth gating (#103828) |
| 📝&nbsp;[#103847](https://github.com/openclaw/openclaw/issues/103847) | 0 | Model routing/config | @yetval | embedded-agent-runner: live tool-result truncation cap undercounts CJK content by up to 4x with no correction |
| 📝&nbsp;[#103846](https://github.com/openclaw/openclaw/issues/103846) | 0 | Model routing/config | @yetval | Anthropic OAuth refresh silently no-ops during the intended pre-expiry margin window |
| 📝&nbsp;[#103828](https://github.com/openclaw/openclaw/issues/103828) | 0 | OpenAI-compatible/proxy | @3F3Feng | bug: image tool auth resolution does not check OPENCLAW_SERVICE_MANAGED_ENV_KEYS |
| 🔀&nbsp;[#103807](https://github.com/openclaw/openclaw/pull/103807) | 0 | Local memory/embedding | @LZY3538 | fix(memory): drop bare heartbeat acks (with decoration) from dreaming corpus |
| 🔀&nbsp;[#103791](https://github.com/openclaw/openclaw/pull/103791) | 0 | OpenAI-compatible/proxy | @lonexreb | fix(plugins): treat path-like provider ids as no bundled policy surface (#103744) |
| 📝&nbsp;[#103788](https://github.com/openclaw/openclaw/issues/103788) | 0 | Model routing/config | @winterRanger-getsome | [Bug]: Gateway memory pressure silently kills all tool responses — degraded state before OOM |
| 📝&nbsp;[#103744](https://github.com/openclaw/openclaw/issues/103744) | 0 | Model routing/config | @bbpfish | sessions_list crashes: Bundled plugin dirName must be a single directory for custom-provider model references |
| 🔀&nbsp;[#103723](https://github.com/openclaw/openclaw/pull/103723) | 0 | Model routing/config | @ArnoldChiou | feat(anthropic): add claude-haiku-4-5 to claude-cli catalog |
| 📝&nbsp;[#103720](https://github.com/openclaw/openclaw/issues/103720) | 0 | Local memory/embedding | @btrailor | [Bug]: Deleted transcripts ingested by dreaming + incomplete heartbeat filter leaks heartbeat noise into dream corpus |
| 📝&nbsp;[#103710](https://github.com/openclaw/openclaw/issues/103710) | 0 | Open-weight/provider behavior | @romannekrasovaillm | Moonshot/Kimi provider: ECONNRESET/timeout through SSRF-guarded fetch (works with direct undici/curl) |
| 🔀&nbsp;[#103686](https://github.com/openclaw/openclaw/pull/103686) | 0 | Model routing/config | @LZY3538 | fix(novita): discover live account model catalog for listing and runtime (#103532) |
| 📝&nbsp;[#103659](https://github.com/openclaw/openclaw/issues/103659) | 0 | Local model runtime | @1Vision365-PeterTijsma | [Feature]: Per-agent/per-provider override for tools.toolSearch |
| 🔀&nbsp;[#103614](https://github.com/openclaw/openclaw/pull/103614) | 0 | Local memory/embedding | @Leon-SK668 | fix(active-memory): accept max thinking config |
| 🔀&nbsp;[#103578](https://github.com/openclaw/openclaw/pull/103578) | 0 | Open-weight/provider behavior | @ZOOWH | fix(openai): redact token refresh error response body |
| 🔀&nbsp;[#103567](https://github.com/openclaw/openclaw/pull/103567) | 0 | Open-weight/provider behavior | @ZOOWH | fix(openai): redact token exchange error response body |
| 📝&nbsp;[#103558](https://github.com/openclaw/openclaw/issues/103558) | 0 | Model routing/config | @alexandre-leng | Feature: agent-controlled model profiles and task-aware model switching from Telegram |
| 📝&nbsp;[#103532](https://github.com/openclaw/openclaw/issues/103532) | 0 | Model routing/config | @alexandre-leng | Novita LLM provider does not retrieve the available AI model list |
| 📝&nbsp;[#103531](https://github.com/openclaw/openclaw/issues/103531) | 0 | Local memory/embedding | @jgrandguillaume | feat(memory-lancedb): record channel/conversation origin in capture metadata and recall logs |
| 🔀&nbsp;[#103521](https://github.com/openclaw/openclaw/pull/103521) | 0 | Model routing/config | @injinj | fix(agents): surface provider server-side model fallbacks as lifecycle fallback_step events |
| 📝&nbsp;[#103520](https://github.com/openclaw/openclaw/issues/103520) | 0 | Model routing/config | @aksheyw | Silent, un-warned substitution to the paid catalog default when a configured model isn't in the allowlist |
| 🔀&nbsp;[#103391](https://github.com/openclaw/openclaw/pull/103391) | 0 | OpenAI-compatible/proxy | @ss251 | fix(agents): log Anthropic provider rejections with status, redacted detail, and payload stats |
| 📝&nbsp;[#103365](https://github.com/openclaw/openclaw/issues/103365) | 0 | Model routing/config | @harjothkhara | [Bug]: iOS model picker renders untrimmed model names (decodeModelChoices discards the trimmed value) |
| 📝&nbsp;[#103231](https://github.com/openclaw/openclaw/issues/103231) | 0 | Model routing/config | @dankorotin | `claude-cli` backend: `ownsNativeCompaction` assumption is false for `claude -p` sessions — nobody compacts, sessions grow past 200% context, and every recovery path (stuck-session abort, safeguard compaction) fails silently |
| 🔀&nbsp;[#103103](https://github.com/openclaw/openclaw/pull/103103) | 0 | Model routing/config | @steipete | fix(models): honor replace mode in list output |
| 📝&nbsp;[#103087](https://github.com/openclaw/openclaw/issues/103087) | 0 | Local memory/embedding | @yetval | memory-wiki vault-page reads have zero agent/session scoping, letting a sandboxed sub-agent read another agent's bridged memory content |
| 📝&nbsp;[#103083](https://github.com/openclaw/openclaw/issues/103083) | 0 | Open-weight/provider behavior | @yetval | Video-generation providers fetch the result URL with no SSRF guard (byteplus, minimax, xai, runway, vydra) |
| 🔀&nbsp;[#103035](https://github.com/openclaw/openclaw/pull/103035) | 0 | Local memory/embedding | @NianJiuZst | fix(memory): keep QMD search hits on the matching file |
| 📝&nbsp;[#102973](https://github.com/openclaw/openclaw/issues/102973) | 0 | Local memory/embedding | @jgrandguillaume | feat(memory-lancedb): per-agent / per-channel scoping for autoCapture and autoRecall |
| 📝&nbsp;[#102907](https://github.com/openclaw/openclaw/issues/102907) | 0 | OpenAI-compatible/proxy | @aniruddhaadak80 | Azure OpenAI Responses throws 400 when prompt_cache_key is sent to endpoints that do not support it |
| 🔀&nbsp;[#102886](https://github.com/openclaw/openclaw/pull/102886) | 0 | Local memory/embedding | @chengzhichao-xydt | fix(github-copilot): add timeout to embedding model discovery |
| 🔀&nbsp;[#102831](https://github.com/openclaw/openclaw/pull/102831) | 0 | OpenAI-compatible/proxy | @moguangyu5-design | fix(auto-reply): honor compat reasoning efforts for openai-completions session thinking |
| 📝&nbsp;[#102807](https://github.com/openclaw/openclaw/issues/102807) | 0 | Model routing/config | @steipete | Usage/cost attribution is provider-keyed: mixed API+subscription and multi-account setups show wrong billing mode/quota |
| 📝&nbsp;[#102779](https://github.com/openclaw/openclaw/issues/102779) | 0 | OpenAI-compatible/proxy | @chaboncarpentier-blip | Bug: custom openai-completions GPT-5.5 accepts request-level thinking but rejects session-level /think |
| 🔀&nbsp;[#102701](https://github.com/openclaw/openclaw/pull/102701) | 0 | Model routing/config | @ishangodawatta | feat: add auth list shortcut |
| 🔀&nbsp;[#102554](https://github.com/openclaw/openclaw/pull/102554) | 0 | Local memory/embedding | @gorkem2020 | fix(active-memory): skip prompt-build hooks in the recall sub-run |
| 🔀&nbsp;[#102402](https://github.com/openclaw/openclaw/pull/102402) | 0 | Model routing/config | @zezaeoh | fix(codex): rotate bounded-turn auth profiles on usage limits |
| 🔀&nbsp;[#102329](https://github.com/openclaw/openclaw/pull/102329) | 0 | Open-weight/provider behavior | @ZOOWH | fix(anthropic): drop image blocks from tool results for text-only models |
| 📝&nbsp;[#102324](https://github.com/openclaw/openclaw/issues/102324) | 0 | Model routing/config | @yetval | anthropic-messages transport sends tool_result image blocks to text-only models (input:[text]) -> 400 |
| 📝&nbsp;[#102323](https://github.com/openclaw/openclaw/issues/102323) | 0 | OpenAI-compatible/proxy | @yetval | anthropic: within-limit HEIC/TIFF images 400 as media_type passes through verbatim (succeeds on OpenAI and Gemini) |
| 📝&nbsp;[#102288](https://github.com/openclaw/openclaw/issues/102288) | 0 | Local model runtime | @erathia65 | [Bug]: agents set-identity --workspace does not set the agent's stored workspace, but its success response implies it does |
| 📝&nbsp;[#102286](https://github.com/openclaw/openclaw/issues/102286) | 0 | Model routing/config | @juanjoseesper-blip | Windows: multiple gateway-down failure modes (kill-and-rebind restart loop, config-edit no-relaunch, browser launch crash, blocking pricing fetches) |
| 📝&nbsp;[#102273](https://github.com/openclaw/openclaw/issues/102273) | 0 | Model routing/config | @bergaeduardo | Add config flag to always show provider in model picker (not only on name collisions) |
| 🔀&nbsp;[#102242](https://github.com/openclaw/openclaw/pull/102242) | 0 | Model routing/config | @qingminlong | fix: bound gateway model pricing cache |
| 🔀&nbsp;[#102213](https://github.com/openclaw/openclaw/pull/102213) | 0 | Open-weight/provider behavior | @zhucegep | fix(auto-reply,agents/tools): strip foreign provider prefix in formatProviderModelRef |
| 🔀&nbsp;[#102204](https://github.com/openclaw/openclaw/pull/102204) | 0 | Model routing/config | @Hackerismydream | fix: stop model catalog warning loop during sidecar refresh<br>Assignee: vincentkoc |
| 🔀&nbsp;[#102189](https://github.com/openclaw/openclaw/pull/102189) | 0 | OpenAI-compatible/proxy | @baanish | fix: stabilize embedded prompt caching across policy and Responses boundaries |
| 📝&nbsp;[#102175](https://github.com/openclaw/openclaw/issues/102175) | 0 | OpenAI-compatible/proxy | @baanish | [Bug]: embedded prompt cache breaks across room-event, policy, and Responses boundaries |
| 🔀&nbsp;[#102170](https://github.com/openclaw/openclaw/pull/102170) | 0 | Model routing/config | @LiLan0125 | fix(google): repair legacy provider catalog config |
| 🔀&nbsp;[#102163](https://github.com/openclaw/openclaw/pull/102163) | 0 | Local model runtime | @LZY3538 | fix(doctor): migrate legacy google provider config to current catalog schema (#102138) |
| 📝&nbsp;[#102152](https://github.com/openclaw/openclaw/issues/102152) | 0 | OpenAI-compatible/proxy | @phenix3443 | Gateway runtime: "no such table: plugin_state_entries / acp_sessions" despite tables existing in state/openclaw.sqlite (agent turns produce no reply) |
| 📝&nbsp;[#102138](https://github.com/openclaw/openclaw/issues/102138) | 0 | OpenAI-compatible/proxy | @zarfmedia | Legacy google provider block fails current model-catalog schema (missing api, input audio/video, cost.cacheWrite) → provider silently unavailable + 120s idle timeout on fallback |
| 📝&nbsp;[#102135](https://github.com/openclaw/openclaw/issues/102135) | 0 | OpenAI-compatible/proxy | @Enominera | ACP dispatch passes raw image attachments to text-only model after successful applyMediaUnderstanding |
| 🔀&nbsp;[#102116](https://github.com/openclaw/openclaw/pull/102116) | 0 | Local model runtime | @tonibofarull | fix(cron): mirror runner env proxy in model preflight |
| 🔀&nbsp;[#102045](https://github.com/openclaw/openclaw/pull/102045) | 0 | Model routing/config | @ZOOWH | fix(gateway): pass authProfileStore through loopback MCP bridge for OAuth-only plugin tools |
| 🔀&nbsp;[#102003](https://github.com/openclaw/openclaw/pull/102003) | 0 | Local memory/embedding | @moguangyu5-design | fix(gateway): OAuth-only xAI tools are missing from CLI-backend sessions |
| 📝&nbsp;[#101967](https://github.com/openclaw/openclaw/issues/101967) | 0 | Model routing/config | @PhoenixCo-Founder | [Bug]: OAuth-only xAI: x_search/code_execution never register for CLI-backend (claude-cli) sessions — loopback MCP bridge omits auth profile store |
| 📝&nbsp;[#101929](https://github.com/openclaw/openclaw/issues/101929) | 0 | Model routing/config | @sercada | [Bug]: context-overflow-midturn-precheck estimator over-counts ~2.3-2.6x vs billed usage (tool-result chars at 2 chars/token over the untruncated transcript) |
| 📝&nbsp;[#101868](https://github.com/openclaw/openclaw/issues/101868) | 0 | Model routing/config | @andrea-kingautomation | Embedded agent: auto-rotate (or persist a marker) on context-overflow give_up instead of wedging the session until manual /reset |
| 🔀&nbsp;[#101715](https://github.com/openclaw/openclaw/pull/101715) | 0 | Model routing/config | @LZY3538 | fix(model-fallback): re-throw LiveSessionModelSwitchError for outer retry loop (#101676) |
| 📝&nbsp;[#101676](https://github.com/openclaw/openclaw/issues/101676) | 0 | Model routing/config | @tford-ui | Live model switch mid-attempt terminates the run instead of retrying against the new model |
| 📝&nbsp;[#101672](https://github.com/openclaw/openclaw/issues/101672) | 0 | Local model runtime | @cpwilhelmi | Session→model/runtime binding drift persists across doctor --fix --deep because the repair's provider-ownership registry is missing the literal id "openai" |
| 📝&nbsp;[#101603](https://github.com/openclaw/openclaw/issues/101603) | 0 | Local memory/embedding | @mathias-owl | [Bug] Dreaming narrative: hardcoded 60s timeout includes lane-queue wait; timeout disposal aborts the primary call then discards the successful fallback-model output |
| 📝&nbsp;[#101586](https://github.com/openclaw/openclaw/issues/101586) | 0 | Local model runtime | @iXandru | [Feature]: Allow Codex harness configured app-server provider IDs |
| 📝&nbsp;[#101543](https://github.com/openclaw/openclaw/issues/101543) | 0 | Model routing/config | @aniruddhaadak80 | Unbounded memory growth in model-pricing-cache.ts leads to heap exhaustion (OOM) |
| 📝&nbsp;[#101537](https://github.com/openclaw/openclaw/issues/101537) | 0 | Open-weight/provider behavior | @Linyi4012 | [Bug]:  cron scheduled wake to main session is skipped (status=skipped, error="disabled"), so the main agent is never woken |
| 📝&nbsp;[#101459](https://github.com/openclaw/openclaw/issues/101459) | 0 | OpenAI-compatible/proxy | @woohahahaaa | [Bug]: openai-responses sends role="system" instead of role="developer" for reasoning models |
| 📝&nbsp;[#101446](https://github.com/openclaw/openclaw/issues/101446) | 0 | Model routing/config | @danniel0976 | Dropdown model switch to claude-cli causes "reply session initialization conflicted" on follow-up turns |
| 📝&nbsp;[#101445](https://github.com/openclaw/openclaw/issues/101445) | 0 | Local model runtime | @Zvimarmor | [Bug]: Embedded Ollama agent reports payloads=0 tools=0 (incomplete_result) for certain prompts even though Ollama's own response contains a valid tool_calls entry |
| 🔀&nbsp;[#101414](https://github.com/openclaw/openclaw/pull/101414) | 0 | Model routing/config | @lzyyzznl | fix(agents): classify Anthropic invalid_request_error as format for failover |
| 🔀&nbsp;[#101367](https://github.com/openclaw/openclaw/pull/101367) | 0 | Open-weight/provider behavior | @Robinnnnn | fix(openrouter): use dedicated /api/v1/images endpoint for image generation |
| 🔀&nbsp;[#101323](https://github.com/openclaw/openclaw/pull/101323) | 0 | Local memory/embedding | @CYCheng9527 | feat: add i18n support for dreaming journal |
| 📝&nbsp;[#101314](https://github.com/openclaw/openclaw/issues/101314) | 0 | Local memory/embedding | @CYCheng9527 | [Feature] i18n Support for Dreaming Journal |
| 📝&nbsp;[#101059](https://github.com/openclaw/openclaw/issues/101059) | 0 | OpenAI-compatible/proxy | @aniruddhaadak80 | [Bug]: OpenAI streaming provider fails to map refusal chunks to ModelRefusalError |
| 🔀&nbsp;[#100886](https://github.com/openclaw/openclaw/pull/100886) | 0 | Local model runtime | @yoneyy | feat(senseaudio): add SenseAudio web_search provider |
| 📝&nbsp;[#100824](https://github.com/openclaw/openclaw/issues/100824) | 0 | Model routing/config | @ndj888 | [Bug]: Fallback model does not report progress correctly during long tasks |
| 🔀&nbsp;[#100797](https://github.com/openclaw/openclaw/pull/100797) | 0 | Local memory/embedding | @lin-hongkuan | docs(memory): add QMD CPU-only VPS guidance |
| 🔀&nbsp;[#100592](https://github.com/openclaw/openclaw/pull/100592) | 0 | OpenAI-compatible/proxy | @medns | fix(pdf): PDF analysis fails for plugin-provided and bundled-catalog models |
| 📝&nbsp;[#100537](https://github.com/openclaw/openclaw/issues/100537) | 0 | Local memory/embedding | @guarismo | [Bug]: active-memory embedded run cannot resolve Lossless Claw lcm_* tools despite runtime plugin inspect showing them registered |
| 🔀&nbsp;[#100500](https://github.com/openclaw/openclaw/pull/100500) | 0 | Model routing/config | @heymoezy | fix(delivery): fall back to deliveryContext.to / origin.to when session lastTo is missing |
| 📝&nbsp;[#100348](https://github.com/openclaw/openclaw/issues/100348) | 0 | Local model runtime | @morukparker93 | [Bug]: Local memory indexer (llama-cpp-provider) hangs indefinitely at 0 chunks |
| 🔀&nbsp;[#100176](https://github.com/openclaw/openclaw/pull/100176) | 0 | Local memory/embedding | @souvikDevloper | fix(active-memory): keep recall circuit breaker tripped across cooldown |
| 📝&nbsp;[#100167](https://github.com/openclaw/openclaw/issues/100167) | 0 | Local memory/embedding | @ddonathan | active-memory recall sub-agent gets 0 assembled messages, always times out |
| 📝&nbsp;[#100121](https://github.com/openclaw/openclaw/issues/100121) | 0 | OpenAI-compatible/proxy | @ccaum | Exec/tool failures show "(see attached image)" and suppress model response |
| 📝&nbsp;[#100097](https://github.com/openclaw/openclaw/issues/100097) | 0 | OpenAI-compatible/proxy | @JeffSteinbok | [Feature]: Expose actual AI Credits consumed per request for GitHub Copilot provider |
| 📝&nbsp;[#100079](https://github.com/openclaw/openclaw/issues/100079) | 0 | Local model runtime | @riazrahaman | [Bug] provider: "ollama" for web search still routes through DuckDuckGo — bot-detection persists |
| 📝&nbsp;[#100067](https://github.com/openclaw/openclaw/issues/100067) | 0 | Model routing/config | @Jason-Vaughan | [bug] 2026.6.x auth-store migration to SQLite silently strands existing JSON auth profiles — all OAuth/token providers lose auth, fallback chains die silently |
| 📝&nbsp;[#100036](https://github.com/openclaw/openclaw/issues/100036) | 0 | Model routing/config | @zqchris | Codex native compaction discards topic diversity — agent misinterprets subsequent messages after topic switch |
| 🔀&nbsp;[#99966](https://github.com/openclaw/openclaw/pull/99966) | 0 | Model routing/config | @in-liberty420 | fix(sessions): forward requester session key from subagent spawn writes (AI-assisted) |
| 📝&nbsp;[#99947](https://github.com/openclaw/openclaw/issues/99947) | 0 | Model routing/config | @jamiezigelbaum | [Bug]: codex harness mirrored-session-history read fails for ephemeral sessions and on failover; one-shot cleanup retires shared app-server client while turns are in flight |
| 📝&nbsp;[#99925](https://github.com/openclaw/openclaw/issues/99925) | 0 | Local memory/embedding | @wsh819 | [Bug] WebChat: new session loses all prior conversation context - AI 'blind' on session start |
| 🔀&nbsp;[#99911](https://github.com/openclaw/openclaw/pull/99911) | 0 | Model routing/config | @849261680 | fix(cron): retry fallback on empty embedded cron results |
| 📝&nbsp;[#99910](https://github.com/openclaw/openclaw/issues/99910) | 0 | Local memory/embedding | @davidbennett1979 | Memory dreaming run pegs the gateway event loop for ~10 min until killed; short-term recall store can never persist (2026.6.9, reproduces on unmodified dist) |
| 📝&nbsp;[#99856](https://github.com/openclaw/openclaw/issues/99856) | 0 | Model routing/config | @bhagyaraj-create | [Bug]: OpenAI provider fails with "Invalid value: 'custom'" – tool parameter incompatibility |
| 🔀&nbsp;[#99810](https://github.com/openclaw/openclaw/pull/99810) | 0 | Model routing/config | @CryptoKylan | fix(auth-profiles): scope subscription_limit blocks to the failing model |
| 📝&nbsp;[#99809](https://github.com/openclaw/openclaw/issues/99809) | 0 | Model routing/config | @CryptoKylan | Codex subscription_limit block on one model incorrectly blocks other models sharing the same auth profile (blockedModel not wired) |
| 🔀&nbsp;[#99798](https://github.com/openclaw/openclaw/pull/99798) | 0 | Local memory/embedding | @Darren2030 | fix(github-copilot): preserve thinking levels for Claude models |
| 📝&nbsp;[#99773](https://github.com/openclaw/openclaw/issues/99773) | 0 | Model routing/config | @NOVA-Openclaw | [Bug]: Hot reload drops include-defined models from in-memory model registry — phantom "Unknown model" failover errors until restart |
| 🔀&nbsp;[#99772](https://github.com/openclaw/openclaw/pull/99772) | 0 | Model routing/config | @SunnyShu0925 | fix(agents): drop orphaned thinking blocks when NO_REPLY text leaves an assistant message with only thinking content (#99620) |
| 🔀&nbsp;[#99751](https://github.com/openclaw/openclaw/pull/99751) | 0 | Local model runtime | @giladgd | fix: make `@openclaw/llama-cpp-provider` install never fail |
| 📝&nbsp;[#99732](https://github.com/openclaw/openclaw/issues/99732) | 0 | Local memory/embedding | @yaorenliang | Gateway crash: ERR_INVALID_STATE — FileHandle closed during GC (active-memory plugin session.jsonl.lock) |
| 🔀&nbsp;[#99685](https://github.com/openclaw/openclaw/pull/99685) | 0 | Model routing/config | @dankarization | docs: propose Codex auth-profile fallback |
| 📝&nbsp;[#99654](https://github.com/openclaw/openclaw/issues/99654) | 0 | OpenAI-compatible/proxy | @dexiosmb | [Bug]: replay_invalid thinking-signature crashes on process restart: 3 findings from 2026-07-03 |
| 🔀&nbsp;[#99643](https://github.com/openclaw/openclaw/pull/99643) | 0 | Open-weight/provider behavior | @mushuiyu886 | fix(opencode-go): expose DeepSeek V4 max thinking levels |
| 🔀&nbsp;[#99618](https://github.com/openclaw/openclaw/pull/99618) | 0 | Open-weight/provider behavior | @34262315716 | fix(opencode-go): enable xhigh/max thinking levels for DeepSeek V4 |
| 📝&nbsp;[#99617](https://github.com/openclaw/openclaw/issues/99617) | 0 | Open-weight/provider behavior | @34262315716 | opencode-go: DeepSeek V4 xhigh/max thinking levels not selectable |
| 🔀&nbsp;[#99608](https://github.com/openclaw/openclaw/pull/99608) | 0 | Open-weight/provider behavior | @brian-bell | fix: fall back after replay-safe Bedrock prompt aborts |
| 📝&nbsp;[#99601](https://github.com/openclaw/openclaw/issues/99601) | 0 | Open-weight/provider behavior | @34262315716 | bug(opencode-go): DeepSeek V4 models silently drop max/xhigh thinking level due to missing thinkingLevelMap |
| 📝&nbsp;[#99583](https://github.com/openclaw/openclaw/issues/99583) | 0 | Open-weight/provider behavior | @apoapostolov | [Proposal] Intelligent Session Auto-Titling: lazy generation, cheap models, topic-aware renames |
| 🔀&nbsp;[#99574](https://github.com/openclaw/openclaw/pull/99574) | 0 | OpenAI-compatible/proxy | @lin-hongkuan | fix(litellm): honor Anthropic cache retention |
| 🔀&nbsp;[#99563](https://github.com/openclaw/openclaw/pull/99563) | 0 | Local memory/embedding | @welfo-beo | fix(memory): spawn embedding worker from launched node |
| 🔀&nbsp;[#99472](https://github.com/openclaw/openclaw/pull/99472) | 0 | Model routing/config | @NOVA-Openclaw | fix(failover): provider refusals now trigger the model fallback chain |
| 📝&nbsp;[#99390](https://github.com/openclaw/openclaw/issues/99390) | 0 | Model routing/config | @thorec | [model-catalog] FsSafeError: directory changed during operation — catalog write races with reader, loops every ~1min<br>Assignee: vincentkoc |
| 🔀&nbsp;[#99381](https://github.com/openclaw/openclaw/pull/99381) | 0 | Model routing/config | @LLagoon3 | feat: add model auth profile removal command |
| 📝&nbsp;[#99380](https://github.com/openclaw/openclaw/issues/99380) | 0 | Model routing/config | @LLagoon3 | [Feature]: add CLI command to remove saved model auth profiles |
| 🔀&nbsp;[#99344](https://github.com/openclaw/openclaw/pull/99344) | 0 | Local model runtime | @medns | fix(web-search): advertise the selected provider's real parameters |
| 🔀&nbsp;[#99318](https://github.com/openclaw/openclaw/pull/99318) | 0 | Local memory/embedding | @LeonidasLux | fix(memory-host-sdk): resolve stable execPath for worker fork to survive Homebrew Node upgrades |
| 📝&nbsp;[#99273](https://github.com/openclaw/openclaw/issues/99273) | 0 | OpenAI-compatible/proxy | @Digitalenergyllc | [Bug]: openai/* provider: runner hardcodes api="openai-responses", ignores provider-level and per-model api:"openai-completions" config |
| 📝&nbsp;[#99251](https://github.com/openclaw/openclaw/issues/99251) | 0 | Local model runtime | @jpjlane-source | Ollama local provider: native tool_calls not recognized, falls back to unreliable JSON-text parsing |
| 📝&nbsp;[#99240](https://github.com/openclaw/openclaw/issues/99240) | 0 | Model routing/config | @alinsavix | [Bug]: /thinking levels not available for github-copilot provider models (e.g. claude-sonnet-4.6) |
| 📝&nbsp;[#99227](https://github.com/openclaw/openclaw/issues/99227) | 0 | Local model runtime | @joelnishanth | [Feature]: On-device LLM option for iOS Talk Mode |
| 🔀&nbsp;[#99208](https://github.com/openclaw/openclaw/pull/99208) | 0 | Local memory/embedding | @0xopaque | fix(agent-core): resolve tool-name mismatches for Claude Code alias calls |
| 📝&nbsp;[#99183](https://github.com/openclaw/openclaw/issues/99183) | 0 | Local model runtime | @zote | Local embedding worker fork fails with ENOENT after Node upgrade — fork() inherits execPath of a deleted binary |
| 📝&nbsp;[#99174](https://github.com/openclaw/openclaw/issues/99174) | 0 | Model routing/config | @sunkencity999 | [Bug]: Anthropic-shaped 400 bodies (no leading HTTP status) classify as null in failover classification, so the model fallback chain is never consulted |
| 🔀&nbsp;[#99166](https://github.com/openclaw/openclaw/pull/99166) | 0 | Local memory/embedding | @Sedrak-Hovhannisyan | Fix QMD vector search timeout defaults |
| 🔀&nbsp;[#99105](https://github.com/openclaw/openclaw/pull/99105) | 0 | Local memory/embedding | @gorkem2020 | fix: active-memory recalls from all agents serialize on one shared lane |
| 🔀&nbsp;[#99064](https://github.com/openclaw/openclaw/pull/99064) | 0 | Local model runtime | @sunlit-deng | fix(copilot): bound BYOK proxy request bodies |
| 🔀&nbsp;[#99041](https://github.com/openclaw/openclaw/pull/99041) | 0 | Model routing/config | @nankingjing | fix(agents): resolve legacy modelstudio profile aliases |
| 🔀&nbsp;[#99036](https://github.com/openclaw/openclaw/pull/99036) | 0 | OpenAI-compatible/proxy | @aydinke | fix(openai-embedding): re-add openai/ prefix for proxy providers even with bare model IDs |
| 📝&nbsp;[#98976](https://github.com/openclaw/openclaw/issues/98976) | 0 | Model routing/config | @NOVA-Openclaw | [Bug]: Provider refusals (Anthropic refusal / OpenAI content_filter) never trigger the model fallback chain — turn dies with generic 'LLM request failed.' |
| 🔀&nbsp;[#98901](https://github.com/openclaw/openclaw/pull/98901) | 0 | Model routing/config | @yetval | fix(config): preserve provider models during merge |
| 📝&nbsp;[#98760](https://github.com/openclaw/openclaw/issues/98760) | 0 | Model routing/config | @dexiosmb | [Bug]: Retry path modifies thinking blocks in conversation history, causing unrecoverable 400 "cannot be modified" error (distinct from #92286) |
| 🔀&nbsp;[#98737](https://github.com/openclaw/openclaw/pull/98737) | 0 | Open-weight/provider behavior | @ly-wang19 | fix(zai): send User-Agent header on endpoint detection probe |
| 📝&nbsp;[#98713](https://github.com/openclaw/openclaw/issues/98713) | 0 | Open-weight/provider behavior | @C1-BA-B1-F3 | [Bug]: opencode-go/kimi-k2.6 resolves to deepseek-v4-pro at runtime despite config |
| 🔀&nbsp;[#98694](https://github.com/openclaw/openclaw/pull/98694) | 0 | Model routing/config | @zw-xysk | fix(telegram): use index-based callback_data to avoid silent model drops in /model picker (fixes #98221) |
| 🔀&nbsp;[#98662](https://github.com/openclaw/openclaw/pull/98662) | 0 | Model routing/config | @welfo-beo | fix(models): add provider request rate limits |
| 🔀&nbsp;[#98632](https://github.com/openclaw/openclaw/pull/98632) | 0 | OpenAI-compatible/proxy | @crh-code | fix(commands): widen isLocalBaseUrl to full 127.0.0.0/8 loopback range |
| 🔀&nbsp;[#98630](https://github.com/openclaw/openclaw/pull/98630) | 0 | Local model runtime | @crh-code | fix(proxy-capture): widen local peer detection to full 127.0.0.0/8 range |
| 🔀&nbsp;[#98627](https://github.com/openclaw/openclaw/pull/98627) | 0 | Open-weight/provider behavior | @crh-code | fix(chutes): widen OAuth redirect loopback check to full 127.0.0.0/8 range |
| 🔀&nbsp;[#98626](https://github.com/openclaw/openclaw/pull/98626) | 0 | OpenAI-compatible/proxy | @crh-code | fix(openai): widen local image endpoint loopback check to full 127.0.0.0/8 range |
| 🔀&nbsp;[#98580](https://github.com/openclaw/openclaw/pull/98580) | 0 | Open-weight/provider behavior | @fmx8747821 | fix(diagnostics): stuck session recovery respects cron isolated agentTurn timeout budget |
| 🔀&nbsp;[#98574](https://github.com/openclaw/openclaw/pull/98574) | 0 | Local memory/embedding | @steipete | fix(session-memory): contain leaked role markers<br>Assignee: steipete |
| 🔀&nbsp;[#98449](https://github.com/openclaw/openclaw/pull/98449) | 0 | Open-weight/provider behavior | @sheyanmin | fix(zai): add User-Agent header to endpoint detection probe<br>Assignee: steipete |
| 🔀&nbsp;[#98441](https://github.com/openclaw/openclaw/pull/98441) | 0 | Open-weight/provider behavior | @jnzhang233 | Fix issue98298:Prune stale thinking blocks from older assistant turns in contextPruning |
| 📝&nbsp;[#98427](https://github.com/openclaw/openclaw/issues/98427) | 0 | OpenAI-compatible/proxy | @luxi233 | [Enhancement] Add per-provider `stream: false` config to disable streaming at request level (not just channel rendering) |
| 📝&nbsp;[#98426](https://github.com/openclaw/openclaw/issues/98426) | 0 | Model routing/config | @redactedcitizenprivacy-maker | Irreversible context compaction when swapping to a model with a smaller context window |
| 🔀&nbsp;[#98407](https://github.com/openclaw/openclaw/pull/98407) | 0 | OpenAI-compatible/proxy | @howardpark | fix(mcp): proactively refresh OAuth tokens for long-lived MCP servers |
| 📝&nbsp;[#98377](https://github.com/openclaw/openclaw/issues/98377) | 0 | Model routing/config | @howardpark | MCP auth:"oauth" tokens not refreshed by the long-running gateway — server latches "needs authorization" at access-token expiry despite a valid refresh token |
| 📝&nbsp;[#98298](https://github.com/openclaw/openclaw/issues/98298) | 0 | Open-weight/provider behavior | @NOVA-Openclaw | feat: Prune stale thinking blocks from older assistant turns in contextPruning |
| 🔀&nbsp;[#98259](https://github.com/openclaw/openclaw/pull/98259) | 0 | OpenAI-compatible/proxy | @BSG2000 | fix(openai): enable prompt cache keys for Azure |
| 🔀&nbsp;[#98248](https://github.com/openclaw/openclaw/pull/98248) | 0 | Model routing/config | @hannesrudolph | fix: Codex catalog honors app-server context caps |
| 🔀&nbsp;[#98245](https://github.com/openclaw/openclaw/pull/98245) | 0 | Model routing/config | @yetval | fix(doctor): merge legacy flat auth repair into existing SQLite store |
| 🔀&nbsp;[#98230](https://github.com/openclaw/openclaw/pull/98230) | 0 | Model routing/config | @luoyanglang | fix(telegram): keep over-limit-name models selectable in /model picker (#98221) |
| 📝&nbsp;[#98221](https://github.com/openclaw/openclaw/issues/98221) | 0 | Model routing/config | @riazrahaman | Telegram /model picker silently drops models when callback_data exceeds 64 bytes |
| 🔀&nbsp;[#98174](https://github.com/openclaw/openclaw/pull/98174) | 0 | OpenAI-compatible/proxy | @fmx8747821 | fix(llm): summarize ephemeral tool results to preserve prefix cache |
| 📝&nbsp;[#98156](https://github.com/openclaw/openclaw/issues/98156) | 0 | Open-weight/provider behavior | @syfvb | Session reset on abort settle timeout causes complete context loss (session amnesia) |
| 🔀&nbsp;[#98123](https://github.com/openclaw/openclaw/pull/98123) | 0 | Open-weight/provider behavior | @yungchentang | fix(zai): send user agent during endpoint detection |
| 🔀&nbsp;[#98110](https://github.com/openclaw/openclaw/pull/98110) | 0 | Model routing/config | @r33drichards | feat(models): add provider request.timeoutMs and retry configuration |
| 📝&nbsp;[#98100](https://github.com/openclaw/openclaw/issues/98100) | 0 | Open-weight/provider behavior | @mir-stream | [Bug]: z.ai endpoint auto-detection probe sends no User-Agent → z.ai 429s it, detectZaiEndpoint returns null, Coding Plan onboarding fails<br>Assignee: steipete |
| 📝&nbsp;[#98084](https://github.com/openclaw/openclaw/issues/98084) | 0 | Open-weight/provider behavior | @AxelHu | [MiniMax] M3 native video input support with timestamp-scaling metadata hint (reference branch only) |
| 📝&nbsp;[#97887](https://github.com/openclaw/openclaw/issues/97887) | 0 | Model routing/config | @riazrahaman | FailoverError during cli-backend turn does not clear stale cliSessionIds from sessions.json, causing infinite retry loop |
| 🔀&nbsp;[#97881](https://github.com/openclaw/openclaw/pull/97881) | 0 | Model routing/config | @yetval | fix(auth-profiles): preserve secret refs and OAuth fields during doctor auth migration |
| 📝&nbsp;[#97844](https://github.com/openclaw/openclaw/issues/97844) | 0 | Model routing/config | @difujia | [Bug]: github-copilot Claude models capped at 128k on published 2026.6.10 (PR #91728 not released yet) |
| 📝&nbsp;[#97817](https://github.com/openclaw/openclaw/issues/97817) | 0 | OpenAI-compatible/proxy | @CHE10X | [Bug]: API keys can leak in error messages when a custom provider's base URL is unreachable |
| 📝&nbsp;[#97772](https://github.com/openclaw/openclaw/issues/97772) | 0 | Open-weight/provider behavior | @Andy-Xie-1145 | [Bug]: zai thinkingFormat uses stale `enable_thinking` param — GLM-5.2 requires `thinking: {"type": "enabled"}` |
| 🔀&nbsp;[#97770](https://github.com/openclaw/openclaw/pull/97770) | 0 | Model routing/config | @mathias15010 | fix: parse provider rate-limit reset timestamps for smarter cooldowns |
| 📝&nbsp;[#97764](https://github.com/openclaw/openclaw/issues/97764) | 0 | Model routing/config | @mathias15010 | Rate-limit cooldown ignores provider reset timestamp; rotation cap too aggressive for multi-key providers |
| 📝&nbsp;[#97741](https://github.com/openclaw/openclaw/issues/97741) | 0 | OpenAI-compatible/proxy | @Suidge | [Bug]: 2026.6.10 tool/runtime aborts surface as model idle timeout |
| 📝&nbsp;[#97692](https://github.com/openclaw/openclaw/issues/97692) | 0 | Local memory/embedding | @lg320531124 | [Feature]: Dreaming phase crash recovery — detect and record interrupted runs |
| 🔀&nbsp;[#97672](https://github.com/openclaw/openclaw/pull/97672) | 0 | Model routing/config | @SYU8384 | fix(agents): keep attempts running after auth and MCP fallback failures |
| 📝&nbsp;[#97660](https://github.com/openclaw/openclaw/issues/97660) | 0 | Model routing/config | @yetval | secrets apply env scrub deletes a non-migrated provider credential when two env vars share a value |
| 📝&nbsp;[#97651](https://github.com/openclaw/openclaw/issues/97651) | 0 | Open-weight/provider behavior | @wanrendl | [Bug]: Tool call output contaminates conversation prefix, collapsing DeepSeek prefix cache hit rate |
| 🔀&nbsp;[#97644](https://github.com/openclaw/openclaw/pull/97644) | 0 | Open-weight/provider behavior | @wyf027 | fix(agents): load generated Bedrock catalogs without snapshots |
| 🔀&nbsp;[#97580](https://github.com/openclaw/openclaw/pull/97580) | 0 | Local model runtime | @alexm-redhat | feat(agents): add multi-pass context compaction with progress tracking<br>Assignee: sallyom |
| 🔀&nbsp;[#97566](https://github.com/openclaw/openclaw/pull/97566) | 0 | Model routing/config | @samrathreddy | feat: add Pioneer.ai as an inference provider with live model discovery |
| 🔀&nbsp;[#97505](https://github.com/openclaw/openclaw/pull/97505) | 0 | Open-weight/provider behavior | @aditya-vithaldas | [codex] Add current OpenRouter image models |
| 🔀&nbsp;[#97485](https://github.com/openclaw/openclaw/pull/97485) | 0 | Local model runtime | @alexm-redhat | feat(agents): add iteration budget for agent loop safety<br>Assignee: sallyom |
| 📝&nbsp;[#97475](https://github.com/openclaw/openclaw/issues/97475) | 0 | Local memory/embedding | @beebox196-art | [Bug] memory-core dreaming cron tokens executed as shell commands (zsh: command not found) — 20+ consecutive cycles |
| 🔀&nbsp;[#97464](https://github.com/openclaw/openclaw/pull/97464) | 0 | OpenAI-compatible/proxy | @lee101 | docs: add app.nz OpenAI-compatible gateway provider page |
| 📝&nbsp;[#97457](https://github.com/openclaw/openclaw/issues/97457) | 0 | Open-weight/provider behavior | @hades0856-art | [Bug]: Webchat abort loses session context — reroutes to new session after compaction |
| 🔀&nbsp;[#97375](https://github.com/openclaw/openclaw/pull/97375) | 0 | Model routing/config | @zhanghang02 | fix(config): prune orphan model refs when provider is missing |
| 📝&nbsp;[#97335](https://github.com/openclaw/openclaw/issues/97335) | 0 | Model routing/config | @Suidge | Cron fallback model works in normal session but LLM request fails when triggered via cron |
| 📝&nbsp;[#97333](https://github.com/openclaw/openclaw/issues/97333) | 0 | Model routing/config | @nova-cds | [Feature]: Support Computer Use tool type across AI provider transports |
| 📝&nbsp;[#97329](https://github.com/openclaw/openclaw/issues/97329) | 0 | Model routing/config | @VixieTodd | [Feature]: Make channel metadata injection configurable to reduce agent context token waste |
| 📝&nbsp;[#97317](https://github.com/openclaw/openclaw/issues/97317) | 0 | Local memory/embedding | @redasadki | [Bug]: Isolated cron defaults inherit full toolbox + full project context — 60–100K tokens/run, –80/day silent waste |
| 🔀&nbsp;[#97302](https://github.com/openclaw/openclaw/pull/97302) | 0 | Local memory/embedding | @ly-wang19 | fix(memory-core): recover primary embedding provider after fallback latch (#96534) |
| 📝&nbsp;[#97290](https://github.com/openclaw/openclaw/issues/97290) | 0 | Model routing/config | @galiniliev | [Bug]: GitHub Copilot idle timeouts abort with no fallback candidate |
| 🔀&nbsp;[#97280](https://github.com/openclaw/openclaw/pull/97280) | 0 | OpenAI-compatible/proxy | @yungchentang | fix(auth): allow OpenAI OAuth for audio transcription |
| 📝&nbsp;[#97241](https://github.com/openclaw/openclaw/issues/97241) | 0 | Model routing/config | @Harsh01007 | [Bug]: Amazon Bedrock provider plugin loads successfully but provider registry is never populated, causing "Unknown model" runtime failure |
| 🔀&nbsp;[#97193](https://github.com/openclaw/openclaw/pull/97193) | 0 | Local model runtime | @LiLan0125 | fix(agents): narrow small-context prompt admission |
| 🔀&nbsp;[#97160](https://github.com/openclaw/openclaw/pull/97160) | 0 | OpenAI-compatible/proxy | @lin-hongkuan | fix(openai): honor ChatGPT Responses compaction |
| 📝&nbsp;[#97115](https://github.com/openclaw/openclaw/issues/97115) | 0 | Model routing/config | @tbertran | Bug: Cron fallback chain broken — models return zero-token success or killed by shared AbortController |
| 🔀&nbsp;[#97059](https://github.com/openclaw/openclaw/pull/97059) | 0 | Local memory/embedding | @harjothkhara | fix(ollama): preserve custom memory provider endpoints |
| 📝&nbsp;[#97055](https://github.com/openclaw/openclaw/issues/97055) | 0 | Local memory/embedding | @Tabytha-Stryker | Provider resolution ignores memorySearch.provider config, routing to wrong Ollama instance |
| 📝&nbsp;[#97011](https://github.com/openclaw/openclaw/issues/97011) | 0 | Open-weight/provider behavior | @lileilei-camera | perf: token consumption ~2× higher than OpenCode for equivalent coding tasks |
| 📝&nbsp;[#96974](https://github.com/openclaw/openclaw/issues/96974) | 0 | Model/provider behavior | @anguslogan01 | [Bug]: web_search (gemini) default model `gemini-2.5-flash` is retired → 404 out-of-the-box |
| 🔀&nbsp;[#96969](https://github.com/openclaw/openclaw/pull/96969) | 0 | OpenAI-compatible/proxy | @SymbolStar | fix(runtime): drop intermediate monologue text blocks from visible delivery |
| 📝&nbsp;[#96947](https://github.com/openclaw/openclaw/issues/96947) | 0 | OpenAI-compatible/proxy | @FriendofTob | Bug: OpenRouter Anthropic cacheWrite drops to zero after v2026.6.10 upgrade (conversation cache regression) |
| 🔀&nbsp;[#96895](https://github.com/openclaw/openclaw/pull/96895) | 0 | OpenAI-compatible/proxy | @arkyu2077 | fix(llm): preserve structured tool results as text across providers |
| 📝&nbsp;[#96882](https://github.com/openclaw/openclaw/issues/96882) | 0 | Model routing/config | @YaxiuElm | Feature Request: Group model dropdown by provider |
| 📝&nbsp;[#96879](https://github.com/openclaw/openclaw/issues/96879) | 0 | Model/provider behavior | @fenglanhua | [Feature]:  Add Interactions API transport for Gemini provider |
| 🔀&nbsp;[#96870](https://github.com/openclaw/openclaw/pull/96870) | 0 | OpenAI-compatible/proxy | @flashosophy | fix(stream): recover visible content when reasoning_delta straddles an inline code span (closes #96869) |
| 📝&nbsp;[#96869](https://github.com/openclaw/openclaw/issues/96869) | 0 | OpenAI-compatible/proxy | @flashosophy | [Bug]: Reasoning+content streaming chunk loses visible content when an inline code span straddles the boundary (visible persisted with unclosed backtick, remainder routed to thinking) |
| 🔀&nbsp;[#96819](https://github.com/openclaw/openclaw/pull/96819) | 0 | Open-weight/provider behavior | @andreacasini | fix: allow bailian provider in resolveThinkingProfile |
| 📝&nbsp;[#96771](https://github.com/openclaw/openclaw/issues/96771) | 0 | Model routing/config | @FreddieM-engpai | OpenClaw 2026.6.10 provider-unification gotcha: openai/gpt-5.5 requires provider openai to route to the subscription backend |
| 🔀&nbsp;[#96748](https://github.com/openclaw/openclaw/pull/96748) | 0 | OpenAI-compatible/proxy | @ly-wang19 | fix(llm): trust control escapes in JSON strings that escape backslashes |
| 🔀&nbsp;[#96747](https://github.com/openclaw/openclaw/pull/96747) | 0 | Local memory/embedding | @ly-wang19 | fix(memory): stop chunkMarkdown injecting newlines into single-line chunks |
| 🔀&nbsp;[#96721](https://github.com/openclaw/openclaw/pull/96721) | 0 | OpenAI-compatible/proxy | @yangxiansheng | fix(moonshot): inherit custom baseUrl for kimi web search |
| 🔀&nbsp;[#96682](https://github.com/openclaw/openclaw/pull/96682) | 0 | Open-weight/provider behavior | @tomsun28 | chore: update glm-5.2 model cost pricing for input, output, and cache |
| 📝&nbsp;[#96658](https://github.com/openclaw/openclaw/issues/96658) | 0 | Local model runtime | @RedEye1605 | Context overflow in isolated cron sessions with lightweight bootstrap (lightContext: true) |
| 🔀&nbsp;[#96635](https://github.com/openclaw/openclaw/pull/96635) | 0 | Local model runtime | @henrybrewer00-dotcom | fix(ollama): remote Ollama streaming stalls at model_call:started on slow hosts |
| 📝&nbsp;[#96597](https://github.com/openclaw/openclaw/issues/96597) | 0 | Model routing/config | @randompup | [Feature]: Update google-vertex models dynamically and also provide an override option |
| 📝&nbsp;[#96561](https://github.com/openclaw/openclaw/issues/96561) | 0 | Local memory/embedding | @bek91 | Reduce QMD memory search wrapper overhead in CLI and tool paths |
| 📝&nbsp;[#96534](https://github.com/openclaw/openclaw/issues/96534) | 0 | Local memory/embedding | @cknzraposo | memory_search latches fallback embedding model after provider outage; only full restart recovers (soft reload insufficient) |
| 📝&nbsp;[#96467](https://github.com/openclaw/openclaw/issues/96467) | 0 | Model routing/config | @jackmtl71 | openclaw models status --probe: wallclock dominated by /v1/messages completion call; --probe-timeout not honored |
| 📝&nbsp;[#96463](https://github.com/openclaw/openclaw/issues/96463) | 0 | Local model runtime | @bazhang1618 | [Bug]: Usage always 0 for custom OpenAI-compatible provider when using embedded runner (--local)<br>Assignee: vincentkoc |
| 🔀&nbsp;[#96425](https://github.com/openclaw/openclaw/pull/96425) | 0 | Model/provider behavior | @outdog-hwh | feat(bedrock): enable prompt caching for Nova models |
| 🔀&nbsp;[#96364](https://github.com/openclaw/openclaw/pull/96364) | 0 | Model routing/config | @SushantGautam | Treat HTTP 530 as transient failover timeout |
| 📝&nbsp;[#96337](https://github.com/openclaw/openclaw/issues/96337) | 0 | Model/provider behavior | @danieljimz | [anthropic-vertex] route=native in 2026.6.10 causes non-visible-output for pure text responses (regression from proxy-like in 2026.6.8) |
| 🔀&nbsp;[#96291](https://github.com/openclaw/openclaw/pull/96291) | 0 | Local memory/embedding | @AdrianIp0204 | [codex] Bound memory flush append payloads |
| 🔀&nbsp;[#96285](https://github.com/openclaw/openclaw/pull/96285) | 0 | Open-weight/provider behavior | @idootop | feat(xiaomi): expose MiMo V2.5 on pay-as-you-go and default to mimo-v2.5-pro |
| 🔀&nbsp;[#96184](https://github.com/openclaw/openclaw/pull/96184) | 0 | Local memory/embedding | @rm0nroe | fix(memory): large legacy memory index stalls and restarts instead of finishing |
| 🔀&nbsp;[#96167](https://github.com/openclaw/openclaw/pull/96167) | 0 | Model routing/config | @natannobre | Guard overflow recovery retries |
| 📝&nbsp;[#96135](https://github.com/openclaw/openclaw/issues/96135) | 0 | Local/media model provider | @kAIborg24 | [Bug]: OAuth-backed OpenAI batch audio transcription no longer works after provider migration |
| 🔀&nbsp;[#96132](https://github.com/openclaw/openclaw/pull/96132) | 0 | Local memory/embedding | @yetval | fix(memory-core): keep live reindex of reset/deleted session archives |
| 🔀&nbsp;[#96127](https://github.com/openclaw/openclaw/pull/96127) | 0 | Local model runtime | @hanZeng-08 | fix(tool-search): normalize flattened target-tool args for tool_call |
| 📝&nbsp;[#96115](https://github.com/openclaw/openclaw/issues/96115) | 0 | Local model runtime | @cbertucci33 | [Bug]: localModelLean compact tool_call drops flattened target args, causing sticky missing-parameter failures |
| 🔀&nbsp;[#96073](https://github.com/openclaw/openclaw/pull/96073) | 0 | OpenAI-compatible/proxy | @wm0018 | feat(openshell): add non-secret env config for sandbox creation |
| 📝&nbsp;[#96046](https://github.com/openclaw/openclaw/issues/96046) | 0 | Local memory/embedding | @hearace1 | Gateway 'plugins.slots.memory: plugin not found' for an extensions/ plugin present in plugins list — 2026.6.9 regression |
| 🔀&nbsp;[#95936](https://github.com/openclaw/openclaw/pull/95936) | 0 | Local memory/embedding | @xmoxmo | feat(memory): shared memory store by directory binding |
| 📝&nbsp;[#95904](https://github.com/openclaw/openclaw/issues/95904) | 0 | Model routing/config | @buyuangtampan | [Bug]: Non-Codex fallback models fail code-mode tool calls with internal_error in 2026.6.9 |
| 📝&nbsp;[#95891](https://github.com/openclaw/openclaw/issues/95891) | 0 | Open-weight/provider behavior | @DemonGiggle | [Bug]: opencode-go/minimax-m3 thinking content leaks to channel via Anthropic Messages path |
| 🔀&nbsp;[#95859](https://github.com/openclaw/openclaw/pull/95859) | 0 | Model/provider behavior | @solodmd | fix(#95840): contextPruning (mode: cache-ttl) never fires on OpenAI models: isCacheTtlEligibleProvider excludes OpenAI, so the idle-gap tool-result firebreak is dead for the highest-volume provider |
| 📝&nbsp;[#95840](https://github.com/openclaw/openclaw/issues/95840) | 0 | Model/provider behavior | @aleps001 | contextPruning (mode: cache-ttl) never fires on OpenAI models: isCacheTtlEligibleProvider excludes OpenAI, so the idle-gap tool-result firebreak is dead for the highest-volume provider |
| 🔀&nbsp;[#95824](https://github.com/openclaw/openclaw/pull/95824) | 0 | OpenAI-compatible/proxy | @ats3v | fix(deepinfra): use OpenAI video end point and tag DeepSeek thinking format |
| 📝&nbsp;[#95821](https://github.com/openclaw/openclaw/issues/95821) | 0 | Local model runtime | @BryceMurray | [Feature]: log memory-core-local-embedding-worker.js spawn/exit + per-call CPU time at INFO level for CPU-forensics traceability (2026.6.9) |
| 🔀&nbsp;[#95820](https://github.com/openclaw/openclaw/pull/95820) | 0 | Local memory/embedding | @moeedahmed | fix(session-memory): skip transcript-only assistant rows |
| 🔀&nbsp;[#95819](https://github.com/openclaw/openclaw/pull/95819) | 0 | Model/provider behavior | @CrypticDriver | fix(bedrock): stop replaying stale signed thinking from completed turns |
| 🔀&nbsp;[#95806](https://github.com/openclaw/openclaw/pull/95806) | 0 | OpenAI-compatible/proxy | @crh-code | fix(gateway): replace buggy isPrivateOrLoopbackHost with canonical net.ts import |
| 🔀&nbsp;[#95798](https://github.com/openclaw/openclaw/pull/95798) | 0 | Model/provider behavior | @hanZeng-08 | fix(heartbeat): allow reasoning/thinking blocks in heartbeat ack filt… |
| 📝&nbsp;[#95796](https://github.com/openclaw/openclaw/issues/95796) | 0 | Model/provider behavior | @DinoMC | [Bug]: Heartbeat transcript filtering ignores HEARTBEAT_OK when assistant message contains reasoning/thinking block |
| 📝&nbsp;[#95788](https://github.com/openclaw/openclaw/issues/95788) | 0 | OpenAI-compatible/proxy | @FLAT-HAT | [Bug]: OpenAI Responses server compaction config is read but not emitted on chatgpt-responses request path |
| 📝&nbsp;[#95746](https://github.com/openclaw/openclaw/issues/95746) | 0 | Local model runtime | @rogerallen1 | [Bug]: memory-core dreaming can exhaust local model context due to parallel/internal Dream Diary subagent runs |
| 🔀&nbsp;[#95739](https://github.com/openclaw/openclaw/pull/95739) | 0 | Local memory/embedding | @ralf003 | feat(memory): add excludePaths option to memorySearch config |
| 📝&nbsp;[#95724](https://github.com/openclaw/openclaw/issues/95724) | 0 | Local memory/embedding | @xmoxmo | feat(memory): index by source directory, not by agent - eliminate duplicate vector stores for same-workspace agents |
| 🔀&nbsp;[#95713](https://github.com/openclaw/openclaw/pull/95713) | 0 | Model routing/config | @0xghost42 | fix(agents): keep auto-compaction on the live session model (#95696) |
| 📝&nbsp;[#95696](https://github.com/openclaw/openclaw/issues/95696) | 0 | Model routing/config | @davidxu00 | [Bug]: Compaction resets session model override to previous provider |
| 🔀&nbsp;[#95692](https://github.com/openclaw/openclaw/pull/95692) | 0 | Model routing/config | @vinitasher | feat(openrouter): support models fallback array for automatic failover |
| 🔀&nbsp;[#95676](https://github.com/openclaw/openclaw/pull/95676) | 0 | Model routing/config | @anyech | fix(agents): retry same profile before timeout auth rotation |
| 📝&nbsp;[#95672](https://github.com/openclaw/openclaw/issues/95672) | 0 | Local model runtime | @KanopiAndPetra | [Bug]: C++ Practice cron trips EmbeddedAttemptSessionTakeoverError after provider overloaded_error + model-pin bypass (regression on Jun 9 12:48 fix) |
| 🔀&nbsp;[#95671](https://github.com/openclaw/openclaw/pull/95671) | 0 | Model routing/config | @hansraj316 | fix(agents): scrub non-conforming tool-call ids at the Anthropic wire (#95623) |
| 🔀&nbsp;[#95665](https://github.com/openclaw/openclaw/pull/95665) | 0 | Model routing/config | @amknight | Configure heartbeat model fallback policy |
| 🔀&nbsp;[#95629](https://github.com/openclaw/openclaw/pull/95629) | 0 | OpenAI-compatible/proxy | @arkyu2077 | fix(replay): sanitize raw OpenAI Responses tool ids for strict-target replay |
| 📝&nbsp;[#95623](https://github.com/openclaw/openclaw/issues/95623) | 0 | Model routing/config | @jrex-jooni | tool_use.id sanitizer (#61254) misses OpenAI-responses composite id on cross-provider failover replay → Anthropic 400 bricks session |
| 📝&nbsp;[#95606](https://github.com/openclaw/openclaw/issues/95606) | 0 | Local memory/embedding | @muskfeel | Memory system: Cannot delete stale memories, conflicting entries persist |
| 🔀&nbsp;[#95605](https://github.com/openclaw/openclaw/pull/95605) | 0 | Local memory/embedding | @bobrenze-bot | fix(agents): skip empty allowlist guard for modelRun shapes |
| 🔀&nbsp;[#95598](https://github.com/openclaw/openclaw/pull/95598) | 0 | Local memory/embedding | @harjothkhara | fix(memory): skip placeholder short-term promotions |
| 🔀&nbsp;[#95590](https://github.com/openclaw/openclaw/pull/95590) | 0 | Local model runtime | @yu-xin-c | [codex] fix(reply): let preflight compaction use compaction timeout |
| 🔀&nbsp;[#95587](https://github.com/openclaw/openclaw/pull/95587) | 0 | OpenAI-compatible/proxy | @fanyangCS | fix(openai-responses): recover streamed invalid_encrypted_content via drain-level retry (#95441) |
| 🔀&nbsp;[#95564](https://github.com/openclaw/openclaw/pull/95564) | 0 | OpenAI-compatible/proxy | @reatang | fix(openai): Codex OAuth token refresh bypasses proxy in restricted regions |
| 📝&nbsp;[#95553](https://github.com/openclaw/openclaw/issues/95553) | 0 | Local model runtime | @kiagentkronos-cell | Bug: preflight (budget-triggered) compaction hard-capped at ~60s, ignores compaction.timeoutSeconds |
| 🔀&nbsp;[#95493](https://github.com/openclaw/openclaw/pull/95493) | 0 | OpenAI-compatible/proxy | @openperf | fix(github-copilot): strip encrypted_content from reasoning replay items |
| 📝&nbsp;[#95441](https://github.com/openclaw/openclaw/issues/95441) | 0 | OpenAI-compatible/proxy | @fanyangCS | github-copilot/gpt-5.5 still persists/replays thinkingSignature encrypted_content after #84367/#90682/#92941, causing channel/direct LLM request failed |
| 🔀&nbsp;[#95436](https://github.com/openclaw/openclaw/pull/95436) | 0 | Model routing/config | @mikasa0818 | fix #91171: [Bug]: Sub-agent model routing ignores model parameter, silently falls back to deepseek |
| 🔀&nbsp;[#95391](https://github.com/openclaw/openclaw/pull/95391) | 0 | Local memory/embedding | @liuhao1024 | fix(active-memory): filter assistant chitchat from recall summary (fixes #84034) |
| 🔀&nbsp;[#95386](https://github.com/openclaw/openclaw/pull/95386) | 0 | Model routing/config | @mikasa0818 | fix #95351: [Feature]: Generic JSONL line-parsing hook for CliBackendPlugin (native tool-card support beyond claude-stream-json) |
| 🔀&nbsp;[#95370](https://github.com/openclaw/openclaw/pull/95370) | 0 | Open-weight/provider behavior | @mikasa0818 | fix #94919: [Bug]: Z.AI Coding-Plan: ECONNRESET triggers model fallback — fallback notice is invisible to the user in async contexts (cron jobs, sub-agents, isolated runs) |
| 📝&nbsp;[#95351](https://github.com/openclaw/openclaw/issues/95351) | 0 | Model routing/config | @jrluis | [Feature]: Generic JSONL line-parsing hook for CliBackendPlugin (native tool-card support beyond claude-stream-json) |
| 🔀&nbsp;[#95333](https://github.com/openclaw/openclaw/pull/95333) | 0 | Local memory/embedding | @mikasa0818 | fix #95279: Provide a trusted inbound-decoration contract so consumers can strip/dedup without forgeable text heuristics |
| 🔀&nbsp;[#95311](https://github.com/openclaw/openclaw/pull/95311) | 0 | Open-weight/provider behavior | @sunlit-deng | feat: add disableBoundaryAwareCache compat option for prefix-matching prompt cache providers |
| 🔀&nbsp;[#95303](https://github.com/openclaw/openclaw/pull/95303) | 0 | Model routing/config | @liaoyl830 | [codex] fix security audit request headers |
| 🔀&nbsp;[#95289](https://github.com/openclaw/openclaw/pull/95289) | 0 | Model routing/config | @summerview1997 | fix: bound Codex Telegram turns fail after /codex bind on OAuth refresh |
| 🔀&nbsp;[#95285](https://github.com/openclaw/openclaw/pull/95285) | 0 | Local memory/embedding | @mmyzwl | fix(memory-wiki): resolve bridge zero-artifact report in CLI snapshot mode |
| 📝&nbsp;[#95279](https://github.com/openclaw/openclaw/issues/95279) | 0 | Local memory/embedding | @gorkem2020 | Provide a trusted inbound-decoration contract so consumers can strip/dedup without forgeable text heuristics |
| 🔀&nbsp;[#95167](https://github.com/openclaw/openclaw/pull/95167) | 0 | Model routing/config | @moguangyu5-design | fix(config): allow Nix-mode doctor --fix and auth login for non-config writes |
| 📝&nbsp;[#95135](https://github.com/openclaw/openclaw/issues/95135) | 0 | Model routing/config | @cattyclaw-bot | Nix-mode write guard blocks auth-profile and session-state writes that never touch openclaw.json |
| 🔀&nbsp;[#95127](https://github.com/openclaw/openclaw/pull/95127) | 0 | Local memory/embedding | @Nas01010101 | perf(memory-lancedb): cache query embeddings per embeddings instance |
| 🔀&nbsp;[#95113](https://github.com/openclaw/openclaw/pull/95113) | 0 | Local memory/embedding | @849261680 | fix(memory): keep cleaning reindex sidecars after lock errors<br>Assignee: vincentkoc |
| 🔀&nbsp;[#95088](https://github.com/openclaw/openclaw/pull/95088) | 0 | Local memory/embedding | @aniruddhaadak80 | [AI-assisted] fix(memory): close cached agent and state databases in test teardowns |
| 🔀&nbsp;[#95070](https://github.com/openclaw/openclaw/pull/95070) | 0 | Local memory/embedding | @Nas01010101 | perf(memory-core): store embedding cache as Float32 BLOB instead of JSON TEXT [AI] |
| 📝&nbsp;[#95042](https://github.com/openclaw/openclaw/issues/95042) | 0 | Local memory/embedding | @1attila2 | [Bug]: 2026.6.x regression cascade — memory search broken, then sessions lost on every reconnect (multi-agent deployment broken) |
| 🔀&nbsp;[#95034](https://github.com/openclaw/openclaw/pull/95034) | 0 | Model/provider behavior | @AxelHu | fix(embedded-agent): auto-recover provider-rejected image history (closes #94906) |
| 🔀&nbsp;[#95006](https://github.com/openclaw/openclaw/pull/95006) | 0 | Local memory/embedding | @mmyzwl | fix(memory): default memorySearch provider to "auto" instead of "openai" |
| 🔀&nbsp;[#94945](https://github.com/openclaw/openclaw/pull/94945) | 0 | OpenAI-compatible/proxy | @ai-hpc | fix(openai-completions): keep cache-boundary suffix out of DeepSeek's implicit prefix cache |
| 📝&nbsp;[#94919](https://github.com/openclaw/openclaw/issues/94919) | 0 | Open-weight/provider behavior | @moccassins | [Bug]: Z.AI Coding-Plan: ECONNRESET triggers model fallback — fallback notice is invisible to the user in async contexts (cron jobs, sub-agents, isolated runs) |
| 📝&nbsp;[#94906](https://github.com/openclaw/openclaw/issues/94906) | 0 | Model/provider behavior | @AxelHu | Add recovery path for provider-rejected image blocks in session history |
| 📝&nbsp;[#94888](https://github.com/openclaw/openclaw/issues/94888) | 0 | Local memory/embedding | @bizzle12368239 | Memory indexer fails to pick up files in agents that haven't been invoked in the current session |
| 📝&nbsp;[#94769](https://github.com/openclaw/openclaw/issues/94769) | 0 | Local memory/embedding | @ITHACAJASON | Memory dreaming promotion: short-term recall signals collected but never promote with Gemini embeddings (structural threshold mismatch + read/exec signal gap) |
| 🔀&nbsp;[#94735](https://github.com/openclaw/openclaw/pull/94735) | 0 | Model routing/config | @Monkey-wusky | fix(models): respect models.mode=replace in 'openclaw models list' output<br>Assignee: steipete |
| 📝&nbsp;[#94705](https://github.com/openclaw/openclaw/issues/94705) | 0 | Model routing/config | @apoapostolov | models.mode: "replace" does not filter openclaw models list output |
| 📝&nbsp;[#94686](https://github.com/openclaw/openclaw/issues/94686) | 0 | Model/provider behavior | @CarotaWealth | Critical Fleet Stability Issues — Multi-Agent Session Crashes (thinking block corruption, session bloat, cron contention) |
| 🔀&nbsp;[#94625](https://github.com/openclaw/openclaw/pull/94625) | 0 | Local memory/embedding | @googlerest | investigate(memory-core): root-cause for #84882 dreaming silent daily-file deletion |
| 📝&nbsp;[#94557](https://github.com/openclaw/openclaw/issues/94557) | 0 | OpenAI-compatible/proxy | @alexminza | [Feature]: Use any native model provider through the Cloudflare AI Gateway by allowing `modelIdNormalization` in `models.providers.<provider>` config |
| 📝&nbsp;[#94554](https://github.com/openclaw/openclaw/issues/94554) | 0 | OpenAI-compatible/proxy | @alexminza | [Feature]: `cloudflare-ai-gateway` is a single-model Anthropic passthrough, not a bridge to AI Gateway |
| 🔀&nbsp;[#94473](https://github.com/openclaw/openclaw/pull/94473) | 0 | OpenAI-compatible/proxy | @LiuwqGit | fix(provider-catalog): use apiKey fallback for self-hosted discovery when discoveryApiKey is undefined (fixes #83461) |
| 🔀&nbsp;[#94430](https://github.com/openclaw/openclaw/pull/94430) | 0 | Model routing/config | @xiongxiaoyang-cell | fix(errors): recognize content policy / new_sensitive errors as rate_limit for fallback |
| 🔀&nbsp;[#94344](https://github.com/openclaw/openclaw/pull/94344) | 0 | Local memory/embedding | @mushuiyu886 | fix #94166: memory-core OpenAI-compatible embeddings: honor provider request.allowPrivateNetwork |
| 📝&nbsp;[#94289](https://github.com/openclaw/openclaw/issues/94289) | 0 | Model routing/config | @Nardoa375 | [Bug]: LCM compaction fails: allowModelOverride not propagated to plugin runtime client until config hot-reload |
| 🔀&nbsp;[#94252](https://github.com/openclaw/openclaw/pull/94252) | 0 | Local memory/embedding | @bennewell35 | fix(memory): scrub stale dreaming sessions on startup |
| 📝&nbsp;[#94251](https://github.com/openclaw/openclaw/issues/94251) | 0 | Local model runtime | @tborer | [Bug]: Ollama remote provider streaming not consumed — model_call:started never progresses in chat sessions |
| 📝&nbsp;[#94228](https://github.com/openclaw/openclaw/issues/94228) | 0 | Model routing/config | @eugkhp | Native Anthropic path: replaying historical `thinking` blocks bricks long tool-use threads (`Invalid signature in thinking block` 400) |
| 📝&nbsp;[#94166](https://github.com/openclaw/openclaw/issues/94166) | 0 | Local memory/embedding | @dmorn | memory-core OpenAI-compatible embeddings cannot use explicitly configured private endpoints |
| 📝&nbsp;[#94125](https://github.com/openclaw/openclaw/issues/94125) | 0 | Local memory/embedding | @thedoctormes-hue | [Bug]: Memory search completely broken — FTS-only hangs, embeddings hang, --force corrupts meta (Ollama/bge-m3, Linux, 2026.6.8) |
| 📝&nbsp;[#93968](https://github.com/openclaw/openclaw/issues/93968) | 0 | Local memory/embedding | @edisonxl | [Bug 6.1] Silent config auto-patch from memory-core + error-message auto-fix breaks all cron jobs on hosts without Docker |
| 🔀&nbsp;[#93878](https://github.com/openclaw/openclaw/pull/93878) | 0 | Local memory/embedding | @sheyanmin | fix: route memory embeddings to configured baseURL for openai provider |
| 🔀&nbsp;[#93868](https://github.com/openclaw/openclaw/pull/93868) | 0 | Local/media model provider | @harjothkhara | fix(gateway): dedupe TTS status provider diagnostics [AI-assisted] |
| 📝&nbsp;[#93741](https://github.com/openclaw/openclaw/issues/93741) | 0 | Model routing/config | @clemenshelm | Allow the `agent` RPC to offload images to `imageModel` for text-only models (opt-in) |
| 🔀&nbsp;[#93655](https://github.com/openclaw/openclaw/pull/93655) | 0 | OpenAI-compatible/proxy | @mushuiyu886 | fix(agent): classify stuck recovery as idle timeout<br>Assignee: vincentkoc |
| 📝&nbsp;[#93598](https://github.com/openclaw/openclaw/issues/93598) | 0 | OpenAI-compatible/proxy | @ikaijian | [Feature]: Can the streaming output increase the size of the configuration control block? |
| 📝&nbsp;[#93485](https://github.com/openclaw/openclaw/issues/93485) | 0 | Local memory/embedding | @A1fred-AI | memory-wiki: Stale Pages report flags intentionally durable references (concepts, syntheses) as aging |
| 📝&nbsp;[#93436](https://github.com/openclaw/openclaw/issues/93436) | 0 | OpenAI-compatible/proxy | @asupian | [Feature]: Forward run context to the model as opt-in request headers (cost attribution behind a proxy) |
| 📝&nbsp;[#93396](https://github.com/openclaw/openclaw/issues/93396) | 0 | Local model runtime | @pineapple82 | [Bug]:  Provider name "openai" misleading when using local Ollama – causes fallback to real OpenAI API for embeddings |
| 🔀&nbsp;[#93388](https://github.com/openclaw/openclaw/pull/93388) | 0 | Model/provider behavior | @vortexopenclaw | fix(google): use stable Gemini image model |
| 🔀&nbsp;[#93377](https://github.com/openclaw/openclaw/pull/93377) | 0 | Model routing/config | @pandaAIGC | fix(model-fallback): classify Codex/OpenAI auth failures |
| 🔀&nbsp;[#93352](https://github.com/openclaw/openclaw/pull/93352) | 0 | Model routing/config | @jailbirt | fix(auth-profiles): import legacy auth-profiles.json into SQLite store on load |
| 📝&nbsp;[#93346](https://github.com/openclaw/openclaw/issues/93346) | 0 | Model routing/config | @davidstoll | [Bug]: Model dropdown does not reflect effective runtime model after fallback/default drift |
| 📝&nbsp;[#93312](https://github.com/openclaw/openclaw/issues/93312) | 0 | Local memory/embedding | @doubleji817-lang | [Bug]: memory] openai-compatible embedding batch hangs on "batch start" - never produces "batch completed" |
| 📝&nbsp;[#93272](https://github.com/openclaw/openclaw/issues/93272) | 0 | Model routing/config | @pandaAIGC | Model fallback does not trigger for Codex/OpenAI auth and zero-output assistant failures |
| 🔀&nbsp;[#93226](https://github.com/openclaw/openclaw/pull/93226) | 0 | Model routing/config | @mmyzwl | fix(auth-health): prefer usable OAuth over expired inventory in provider status |
| 🔀&nbsp;[#93206](https://github.com/openclaw/openclaw/pull/93206) | 0 | Open-weight/provider behavior | @extrasmall0 | fix(minimax): wrap simple completion requests |
| 📝&nbsp;[#93199](https://github.com/openclaw/openclaw/issues/93199) | 0 | Local memory/embedding | @chaboncarpentier-blip | memory_search fails in non-default agent session while CLI --agent search works; current session resolves inconsistently |
| 📝&nbsp;[#93150](https://github.com/openclaw/openclaw/issues/93150) | 0 | Local memory/embedding | @rrrrrredy | [Feature]: Add keyword fallback for memory_search when node:sqlite is unavailable |
| 📝&nbsp;[#93120](https://github.com/openclaw/openclaw/issues/93120) | 0 | Model routing/config | @shichuzhu | [Feature]: Expose MAX_SAME_MODEL_RATE_LIMIT_RETRIES as configurable (currently hardcoded to 3) |
| 🔀&nbsp;[#93116](https://github.com/openclaw/openclaw/pull/93116) | 0 | OpenAI-compatible/proxy | @xydt-tanshanshan | fix(xai): respect ssrfPolicy and request.allowPrivateNetwork in image_generate |
| 🔀&nbsp;[#93100](https://github.com/openclaw/openclaw/pull/93100) | 0 | Local memory/embedding | @yetval | fix(compaction): emit after_compaction on no-op and use JSON-safe validator delimiters (#81925) |
| 🔀&nbsp;[#93056](https://github.com/openclaw/openclaw/pull/93056) | 0 | Model routing/config | @samson910022 | fix(agents): sync stale this.model snapshot after /model switch |
| 🔀&nbsp;[#93007](https://github.com/openclaw/openclaw/pull/93007) | 0 | OpenAI-compatible/proxy | @Lellansin | feat(gateway): forward web_search_options through OpenAI-compatible chat completions |
| 🔀&nbsp;[#92900](https://github.com/openclaw/openclaw/pull/92900) | 0 | Model routing/config | @YonganZhang | fix(ui): refresh overview model auth status on demand |
| 🔀&nbsp;[#92892](https://github.com/openclaw/openclaw/pull/92892) | 0 | Model routing/config | @YonganZhang | fix(gateway): allow Gemini CLI image-capable models |
| 📝&nbsp;[#92888](https://github.com/openclaw/openclaw/issues/92888) | 0 | Model routing/config | @buyuangtampan | Control UI model auth badge still shows expired on 2026.6.6 while runtime auth is usable |
| 📝&nbsp;[#92866](https://github.com/openclaw/openclaw/issues/92866) | 0 | OpenAI-compatible/proxy | @Kambrian | Feature: image_generate should support custom/third-party providers, not only built-in ones |
| 🔀&nbsp;[#92819](https://github.com/openclaw/openclaw/pull/92819) | 0 | Model routing/config | @TurboTheTurtle | Fix stale auto-fallback origin model selection |
| 📝&nbsp;[#92776](https://github.com/openclaw/openclaw/issues/92776) | 0 | Model routing/config | @falonrozfatemi | Session model pinning persists indefinitely: snap-back probe (PR #82676) defeated by origin-field pollution upstream — repros on 2026.5.28 through 2026.6.7-beta.1, byte-identical paths |
| 📝&nbsp;[#92769](https://github.com/openclaw/openclaw/issues/92769) | 0 | OpenAI-compatible/proxy | @Wizongod | [Bug]: Regression of #65533 — reasoning/reasoning_details completely dropped from message history for MiniMax M3 via OpenRouter (both plain-text and tool-call turns) |
| 📝&nbsp;[#92728](https://github.com/openclaw/openclaw/issues/92728) | 0 | Local memory/embedding | @rrriiiccckkk | memory-core: CJK LIKE fallback returns wrong results for multi-character queries |
| 🔀&nbsp;[#92676](https://github.com/openclaw/openclaw/pull/92676) | 0 | Model routing/config | @kumaxs | feat: Rate-limit fallback user-visible error notification (message-lifecycle Phase 2 extension) |
| 📝&nbsp;[#92674](https://github.com/openclaw/openclaw/issues/92674) | 0 | Model routing/config | @xxtyyq | [Bug] Thinking level fallback to "adaptive" silently increases token usage 4-5x when user requests "medium" on models that only support [off, adaptive] |
| 📝&nbsp;[#92672](https://github.com/openclaw/openclaw/issues/92672) | 0 | Model routing/config | @kumaxs | [RFC] Rate-limit fallback: user-visible error + immediate switch notification (message-lifecycle Phase 2 extension) |
| 📝&nbsp;[#92655](https://github.com/openclaw/openclaw/issues/92655) | 0 | Model routing/config | @renaudcerrato | [Bug]: Telegram: /models provider buttons do nothing when clicked in a forum topic group |
| 🔀&nbsp;[#92649](https://github.com/openclaw/openclaw/pull/92649) | 0 | Open-weight/provider behavior | @litang9 | feat(kimi): show code quota in usage status |
| 🔀&nbsp;[#92647](https://github.com/openclaw/openclaw/pull/92647) | 0 | Local memory/embedding | @Bartok9 | fix(memory): attribute corpus=all timeouts to the slow branch instead of the provider |
| 📝&nbsp;[#92633](https://github.com/openclaw/openclaw/issues/92633) | 0 | Local memory/embedding | @desksk | memory_search corpus=all times out while individual corpora succeed |
| 📝&nbsp;[#92559](https://github.com/openclaw/openclaw/issues/92559) | 0 | OpenAI-compatible/proxy | @fmsonic | Feature: Session-aware template variables in extra_body (e.g. {{session.channel}}) |
| 🔀&nbsp;[#92557](https://github.com/openclaw/openclaw/pull/92557) | 0 | Local model runtime | @Patrick-Erichsen | Validate ClawHub plugin metadata in PRs |
| 🔀&nbsp;[#92556](https://github.com/openclaw/openclaw/pull/92556) | 0 | OpenAI-compatible/proxy | @smolskayanastassia | feat(llm): add Inworld as built-in llm provider |
| 📝&nbsp;[#92500](https://github.com/openclaw/openclaw/issues/92500) | 0 | Local/media model provider | @100yenadmin | Add Telegram voice/STT handoff telemetry into agent context |
| 🔀&nbsp;[#92499](https://github.com/openclaw/openclaw/pull/92499) | 0 | Local memory/embedding | @SYU8384 | Memory/QMD: isolate mcporter sidecars per agent |
| 📝&nbsp;[#92478](https://github.com/openclaw/openclaw/issues/92478) | 0 | Local/media model provider | @novaagentia-cpu | [Bug]: Native Talk button triggers OpenAI Realtime WebRTC call and fails with 500 when Realtime is not configured |
| 📝&nbsp;[#92473](https://github.com/openclaw/openclaw/issues/92473) | 0 | Model routing/config | @guscamara | Model fallback notice leaks to external user-facing channels |
| 📝&nbsp;[#92405](https://github.com/openclaw/openclaw/issues/92405) | 0 | Model routing/config | @oiGaDio | subagent spawn persists raw provider instead of CLI runtime — depth-2 cold spawns silently die with 'lost execution context' (two unpatched #57326 call sites, fix included) |
| 🔀&nbsp;[#92359](https://github.com/openclaw/openclaw/pull/92359) | 0 | OpenAI-compatible/proxy | @jiewent1-cmyk | fix(config): allow model.compat.sendSessionAffinityHeaders in ModelCompatSchema |
| 🔀&nbsp;[#92341](https://github.com/openclaw/openclaw/pull/92341) | 0 | Local memory/embedding | @rrriiiccckkk | fix(memory-core): remove CJK length threshold for trigram LIKE matching |
| 🔀&nbsp;[#92288](https://github.com/openclaw/openclaw/pull/92288) | 0 | OpenAI-compatible/proxy | @ai-hpc | fix(agents): quiet extra_body tuning-key collisions |
| 🔀&nbsp;[#92261](https://github.com/openclaw/openclaw/pull/92261) | 0 | Local memory/embedding | @skocher | Fix live orphan session transcript visibility |
| 🔀&nbsp;[#92254](https://github.com/openclaw/openclaw/pull/92254) | 0 | Model routing/config | @jbetala7 | fix(model-picker): preserve auth profile override when selecting a model |
| 📝&nbsp;[#92244](https://github.com/openclaw/openclaw/issues/92244) | 0 | Model routing/config | @saphoroth | [bug] Telegram model picker call to applyModelOverrideToSessionEntry doesn't pass preserveAuthProfileOverride, causing silent destruction of auth profile overrides set by non-picker sources |
| 🔀&nbsp;[#92230](https://github.com/openclaw/openclaw/pull/92230) | 0 | Model routing/config | @clawSean | feat: add model switch choices to /model |
| 🔀&nbsp;[#92217](https://github.com/openclaw/openclaw/pull/92217) | 0 | Open-weight/provider behavior | @obuchowski | feat(fireworks): catalog DeepSeek V4 Pro, MiniMax M2.7, GLM-5.1, GPT-OSS 120B reasoning models |
| 🔀&nbsp;[#92196](https://github.com/openclaw/openclaw/pull/92196) | 0 | Local memory/embedding | @yetval | fix(memory-search): stop hybrid fusion from discounting vector-only multimodal results |
| 🔀&nbsp;[#92114](https://github.com/openclaw/openclaw/pull/92114) | 0 | Local memory/embedding | @TurboTheTurtle | fix(memory): report indexed vector store in status<br>Assignee: vincentkoc |
| 📝&nbsp;[#92105](https://github.com/openclaw/openclaw/issues/92105) | 0 | Local memory/embedding | @qiaokuan1992 | [Feature]: Configurable page groups for memory-wiki with custom index directories and recursive scanning |
| 📝&nbsp;[#92102](https://github.com/openclaw/openclaw/issues/92102) | 0 | Local memory/embedding | @pepe-hern | [Bug]: openclaw memory status shows "Vector store: unknown" despite working vectors (sqlite-vec lazy init in CLI fast path) |
| 📝&nbsp;[#92043](https://github.com/openclaw/openclaw/issues/92043) | 0 | Model routing/config | @yetval | Bug: 180s compaction timeout is a single wall clock over the whole chunk pipeline with no partial-progress reuse, so a legitimately-long compaction fails identically every turn |
| 🔀&nbsp;[#92040](https://github.com/openclaw/openclaw/pull/92040) | 0 | OpenAI-compatible/proxy | @849261680 | fix(provider): route thinking profiles by model API |
| 🔀&nbsp;[#92035](https://github.com/openclaw/openclaw/pull/92035) | 0 | Local memory/embedding | @fall4knight | feat(memory): apply temporal decay to QMD search results |
| 📝&nbsp;[#92013](https://github.com/openclaw/openclaw/issues/92013) | 0 | Local memory/embedding | @islandpreneur007 | Active Memory `queryMode: "message"` can receive full assembled request envelopes; needs latest-message cap or slim-intent field |
| 📝&nbsp;[#91951](https://github.com/openclaw/openclaw/issues/91951) | 0 | Local memory/embedding | @workingpleasewait | [Feature]: memory index: support maxAgeDays config to limit indexed window |
| 📝&nbsp;[#91945](https://github.com/openclaw/openclaw/issues/91945) | 0 | OpenAI-compatible/proxy | @alexminza | [Feature]: Upgrade Cloudflare AI Gateway provider to the REST API |
| 📝&nbsp;[#91892](https://github.com/openclaw/openclaw/issues/91892) | 0 | Open-weight/provider behavior | @luciaski | Cron jobs stall during AI model calls (model_call:stream_progress never completes) |
| 📝&nbsp;[#91806](https://github.com/openclaw/openclaw/issues/91806) | 0 | Model routing/config | @Cornil79 | [Bug]: Session shows openai/gpt-5.5 in UI, but new turns execute via DeepSeek and chat history collapses into new leaf sessions |
| 🔀&nbsp;[#91770](https://github.com/openclaw/openclaw/pull/91770) | 0 | Local memory/embedding | @ai-hpc | fix(memory): abort search embeddings on tool timeout |
| 📝&nbsp;[#91739](https://github.com/openclaw/openclaw/issues/91739) | 0 | Model routing/config | @ruben2000de | google-gemini-cli rejects image attachments before CLI image prestage |
| 📝&nbsp;[#91683](https://github.com/openclaw/openclaw/issues/91683) | 0 | Model/provider behavior | @GabeMillikan | [Feature]: Add provider-native file/document forwarding for non-image attachments |
| 📝&nbsp;[#91572](https://github.com/openclaw/openclaw/issues/91572) | 0 | Local memory/embedding | @Orionation | Dreaming light phase should ingest workspace file creation events, not just memory/*.md |
| 📝&nbsp;[#91563](https://github.com/openclaw/openclaw/issues/91563) | 0 | Local memory/embedding | @Orionation | Dreaming deep phase: minUniqueQueries gate bypassed by day-diversity counting |
| 🔀&nbsp;[#91549](https://github.com/openclaw/openclaw/pull/91549) | 0 | OpenAI-compatible/proxy | @studentzhou-svg | fix: enable DeepSeek DSML filtering for proxy providers via model id detection |
| 📝&nbsp;[#91504](https://github.com/openclaw/openclaw/issues/91504) | 0 | Model/provider behavior | @resYuto | [Feature]: Support another Image generation models on OpenRouter |
| 📝&nbsp;[#91498](https://github.com/openclaw/openclaw/issues/91498) | 0 | Model routing/config | @medikoo | [Feature]: Allow model aliases or runtimes to select different auth profiles for the same provider |
| 📝&nbsp;[#91434](https://github.com/openclaw/openclaw/issues/91434) | 0 | Local model runtime | @lily-oc | [Bug]: LM Studio sessions start without tools |
| 📝&nbsp;[#91396](https://github.com/openclaw/openclaw/issues/91396) | 0 | Local memory/embedding | @xiangcaoni | Memory embedding fails with HTTP 400 when using SiliconFlow (fetchWithSsrFGuard incompatibility) |
| 📝&nbsp;[#91354](https://github.com/openclaw/openclaw/issues/91354) | 0 | Local memory/embedding | @Louisone1 | memory: Gemini embeddings still use inline batch requests after remote.batch.enabled=false, causing 429 on low quota |
| 📝&nbsp;[#91259](https://github.com/openclaw/openclaw/issues/91259) | 0 | Local memory/embedding | @sasan1200 | memory(qmd): drop redundant agent-id scoping from collection names |
| 🔀&nbsp;[#91237](https://github.com/openclaw/openclaw/pull/91237) | 0 | OpenAI-compatible/proxy | @Bartok9 | fix(providers/openrouter): treat openrouter.ai as long-TTL-eligible for Anthropic cache_control |
| 📝&nbsp;[#91223](https://github.com/openclaw/openclaw/issues/91223) | 0 | Local memory/embedding | @Enominera | [Bug]: Active memory injection breaks prompt cache hit rate (99.9% → 22%) |
| 🔀&nbsp;[#91222](https://github.com/openclaw/openclaw/pull/91222) | 0 | Model/provider behavior | @damianFelixPago | fix(google-vertex): retry transient pre-stream failures and stale ADC |
| 🔀&nbsp;[#91217](https://github.com/openclaw/openclaw/pull/91217) | 0 | Model routing/config | @safrano9999 | feat(gateway): add deterministic dummy model (AI-assisted) |
| 🔀&nbsp;[#91211](https://github.com/openclaw/openclaw/pull/91211) | 0 | Model routing/config | @Kirchlive | feat(tui): classify every model as CLI / OAuth / API in /model picker |
| 📝&nbsp;[#91171](https://github.com/openclaw/openclaw/issues/91171) | 0 | Model routing/config | @wolfeee | [Bug]: Sub-agent model routing ignores model parameter, silently falls back to deepseek |
| 🔀&nbsp;[#91091](https://github.com/openclaw/openclaw/pull/91091) | 0 | Local memory/embedding | @amknight | fix(memory): do not prune session index from a failed directory scan<br>Assignee: amknight |
| 📝&nbsp;[#91052](https://github.com/openclaw/openclaw/issues/91052) | 0 | Local/media model provider | @xueqingli1 | [Feature]: make voice-call realtime barge-in detection configurable |
| 🔀&nbsp;[#91028](https://github.com/openclaw/openclaw/pull/91028) | 0 | Model routing/config | @bosszukung | feat(lobster): in-process LLM adapters for embedded runner (#90909) |
| 📝&nbsp;[#91009](https://github.com/openclaw/openclaw/issues/91009) | 0 | Local model runtime | @aspalagin | Codex PreToolUse native hook relay spawns CPU-bound openclaw-hooks processes and stalls gateway RPC |
| 📝&nbsp;[#91007](https://github.com/openclaw/openclaw/issues/91007) | 0 | Local/media model provider | @Countermarch | [Bug]: iOS Talk realtime session closes before audio append and ignores server stt-tts routing |
| 🔀&nbsp;[#90975](https://github.com/openclaw/openclaw/pull/90975) | 0 | Model/provider behavior | @Kirchlive | feat(google): add Antigravity CLI backend |
| 📝&nbsp;[#90974](https://github.com/openclaw/openclaw/issues/90974) | 0 | Model routing/config | @itanyplus | [Feedback] Stop shipping features. Start shipping a product that works. |
| 🔀&nbsp;[#90968](https://github.com/openclaw/openclaw/pull/90968) | 0 | Model routing/config | @moeedahmed | fix: avoid reapplying ACP startup runtime options |
| 📝&nbsp;[#90909](https://github.com/openclaw/openclaw/issues/90909) | 0 | Model routing/config | @bosszukung | [Feature]: Host-provided in-process LLM adapters for the embedded Lobster runner (#76101 bridge) |
| 🔀&nbsp;[#90903](https://github.com/openclaw/openclaw/pull/90903) | 0 | Model routing/config | @thinhkhang97 | fix(agents): inherit default agent model catalog for secondary agents |
| 🔀&nbsp;[#90827](https://github.com/openclaw/openclaw/pull/90827) | 0 | Local memory/embedding | @lonexreb | fix(memory-core): surface empty narrative generation instead of silent fallback (#90781) |
| 📝&nbsp;[#90801](https://github.com/openclaw/openclaw/issues/90801) | 0 | Local memory/embedding | @fenglanhua | [Bug]: memory status shows inconsistent Dirty state, watcher stops auto-indexing, and --deep required to confirm health on 2026.6.1 |
| 📝&nbsp;[#90787](https://github.com/openclaw/openclaw/issues/90787) | 0 | Local memory/embedding | @fenglanhua | [Bug]: memorySearch provider silently resets to "openai" after upgrade to 2026.6.1, causing permanent Dirty index and vector search outage |
| 📝&nbsp;[#90786](https://github.com/openclaw/openclaw/issues/90786) | 0 | Local memory/embedding | @fenglanhua | [Bug]: memory status --index and --deep fail with "Unknown memory embedding provider: google" on 2026.6.1 |
| 📝&nbsp;[#90781](https://github.com/openclaw/openclaw/issues/90781) | 0 | Local memory/embedding | @xdengli | [Bug]: memory-core narrative generation silently produces no text and writes fallback diary entries (light/rem/deep phases) |
| 📝&nbsp;[#90763](https://github.com/openclaw/openclaw/issues/90763) | 0 | Model routing/config | @A1fred-AI | [Feature]: Add agents.list[].subagents.allowedModels to restrict model overrides in sessions_spawn |
| 📝&nbsp;[#90746](https://github.com/openclaw/openclaw/issues/90746) | 0 | Local memory/embedding | @holgergruenhagen | Document practical requirements for QMD memory backend on CPU-only VPS deployments |
| 🔀&nbsp;[#90703](https://github.com/openclaw/openclaw/pull/90703) | 0 | OpenAI-compatible/proxy | @Alex-Govorov | Support compat reasoning levels for thinking xhigh |
| 🔀&nbsp;[#90689](https://github.com/openclaw/openclaw/pull/90689) | 0 | OpenAI-compatible/proxy | @ly85206559 | fix(agents): align custom provider auth labels with runtime (#82020) |
| 📝&nbsp;[#90684](https://github.com/openclaw/openclaw/issues/90684) | 0 | Open-weight/provider behavior | @studentzhou-svg | Feishu (and non-Discord channels) should apply sanitizeAssistantVisibleText() on outbound text |
| 📝&nbsp;[#90674](https://github.com/openclaw/openclaw/issues/90674) | 0 | Model/provider behavior | @motteman | Gateway writes usage.cost: 0 for model strings absent from its internal price table (silent cost under-reporting) |
| 🔀&nbsp;[#90603](https://github.com/openclaw/openclaw/pull/90603) | 0 | Model routing/config | @Bartok9 | fix(secrets): use configured default agent ID in auth/model path discovery (#90573) |
| 📝&nbsp;[#90556](https://github.com/openclaw/openclaw/issues/90556) | 0 | Local model runtime | @Wsq-159 | Chat UI: Display response latency under each message |
| 📝&nbsp;[#90536](https://github.com/openclaw/openclaw/issues/90536) | 0 | Model routing/config | @ozp | OpenAI OAuth missing 'model.request' scope — GPT-5.5 falls back silently |
| 🔀&nbsp;[#90514](https://github.com/openclaw/openclaw/pull/90514) | 0 | Model routing/config | @baskduf | fix(session): clear stale fallback model state on reset |
| 📝&nbsp;[#90508](https://github.com/openclaw/openclaw/issues/90508) | 0 | Local memory/embedding | @joeykrug | memory-core main reindex thrashes, leaks main.sqlite.tmp files, and leaves memory_search paused after repair |
| 🔀&nbsp;[#90500](https://github.com/openclaw/openclaw/pull/90500) | 0 | Model routing/config | @TurboTheTurtle | Fix stale session routes for removed providers |
| 📝&nbsp;[#90471](https://github.com/openclaw/openclaw/issues/90471) | 0 | Model routing/config | @centralpc | [Bug]: Deleted provider session overrides persist in sessions.json — silent financial damage risk |
| 🔀&nbsp;[#90453](https://github.com/openclaw/openclaw/pull/90453) | 0 | Local memory/embedding | @849261680 | fix(memory-core): guard searches during safe reindex |
| 📝&nbsp;[#90448](https://github.com/openclaw/openclaw/issues/90448) | 0 | Model routing/config | @ooiuuii | Codex context override can fall back to 272k after 2026.6.1 OpenAI route unification |
| 📝&nbsp;[#90445](https://github.com/openclaw/openclaw/issues/90445) | 0 | Model routing/config | @openkralle | Control Panel: Add tooltips/clarifying labels for Reasoning and Thinking dropdowns (Config↔UI naming collision) |
| 📝&nbsp;[#90414](https://github.com/openclaw/openclaw/issues/90414) | 0 | Local memory/embedding | @AS76 | agentmemory__memory_search returns "index metadata is missing" persistently (memory-core manager state cache) |
| 🔀&nbsp;[#90401](https://github.com/openclaw/openclaw/pull/90401) | 0 | OpenAI-compatible/proxy | @danyurkin | docs(local-models): add Atomic Chat as an OpenAI-compatible local server |
| 📝&nbsp;[#90361](https://github.com/openclaw/openclaw/issues/90361) | 0 | Local memory/embedding | @AyitLabs | [Bug]:Intermittent memory_search "index metadata is missing" despite valid builtin memory index; likely search/reindex race. Locally hotfixed. |
| 🔀&nbsp;[#90356](https://github.com/openclaw/openclaw/pull/90356) | 0 | Model routing/config | @sovushik | fix(status): use legacy Codex OAuth profiles for OpenAI usage |
| 📝&nbsp;[#90349](https://github.com/openclaw/openclaw/issues/90349) | 0 | Model routing/config | @AungMyoKyaw | Feature: Context Budget/Compactor — intelligent prompt slimming for small-context models |
| 🔀&nbsp;[#90331](https://github.com/openclaw/openclaw/pull/90331) | 0 | Model routing/config | @Daozheyuanxi | fix(agents): harden gateway config self-edits |
| 📝&nbsp;[#90276](https://github.com/openclaw/openclaw/issues/90276) | 0 | Local/media model provider | @WilhelminaVonHunt | TTS timeoutMs hard cap of 120000ms (120s) too low for local TTS models — silent fallback to default provider |
| 📝&nbsp;[#90243](https://github.com/openclaw/openclaw/issues/90243) | 0 | Model routing/config | @silvesterxm | feat(llm/google-vertex): Support physical model mapping/aliasing to support Google's Priority and Flex PayGo tiers |
| 📝&nbsp;[#90193](https://github.com/openclaw/openclaw/issues/90193) | 0 | OpenAI-compatible/proxy | @jalehman | Refactor duplicate Codex Responses paths for agent turns and llm.complete |
| 📝&nbsp;[#90082](https://github.com/openclaw/openclaw/issues/90082) | 0 | Local memory/embedding | @ryswork1993 | [Bug] active-memory circuit breaker too aggressive; fallback prompt pollutes main session (v2026.6.1) |
| 📝&nbsp;[#90074](https://github.com/openclaw/openclaw/issues/90074) | 0 | Model routing/config | @holgergruenhagen | OpenAI image generation uses direct API-key route instead of Codex OAuth when explicit provider config exists |
| 📝&nbsp;[#90042](https://github.com/openclaw/openclaw/issues/90042) | 0 | Local memory/embedding | @Bizman365 | Gateway memory_search index stuck dirty: provider.model empty during boot overwrites correct index identity |
| 🔀&nbsp;[#90033](https://github.com/openclaw/openclaw/pull/90033) | 0 | OpenAI-compatible/proxy | @obuchowski | fix(llm): apply model.compat.sendSessionAffinityHeaders at openai-transport-stream |
| 🔀&nbsp;[#90019](https://github.com/openclaw/openclaw/pull/90019) | 0 | Local memory/embedding | @sahibzada-allahyar | fix(memory-search): default periodic sync fallback |
| 📝&nbsp;[#90015](https://github.com/openclaw/openclaw/issues/90015) | 0 | Open-weight/provider behavior | @SebTardif | DSML recovery buffer grows without bound on unclosed DSML blocks |
| 📝&nbsp;[#89927](https://github.com/openclaw/openclaw/issues/89927) | 0 | Model routing/config | @A1fred-AI | Fallback sessions don't terminate parent lane → concurrent orchestrator lanes, duplicate billed subagent dispatches, and wedged sessions |
| 🔀&nbsp;[#89818](https://github.com/openclaw/openclaw/pull/89818) | 0 | Model/provider behavior | @masatohoshino | fix(providers): forward stop sequences in bundled Anthropic transports |
| 📝&nbsp;[#89664](https://github.com/openclaw/openclaw/issues/89664) | 0 | Model routing/config | @Stache73 | [Bug] secrets audit / doctor falsely flags static routing header as plaintext secret |
| 🔀&nbsp;[#89618](https://github.com/openclaw/openclaw/pull/89618) | 0 | Local model runtime | @danyurkin | feat(atomicchat): add Atomic Chat as a bundled local provider |
| 🔀&nbsp;[#89602](https://github.com/openclaw/openclaw/pull/89602) | 0 | Model routing/config | @zerone0x | fix(status): show effective channel model override |
| 🔀&nbsp;[#89584](https://github.com/openclaw/openclaw/pull/89584) | 0 | Local memory/embedding | @ubehera | feat(memory-core): optional cross-encoder rerank stage for memory search |
| 📝&nbsp;[#89532](https://github.com/openclaw/openclaw/issues/89532) | 0 | Model routing/config | @tess020126-cmyk | Bug: /status does not show effective model from channels.modelByChannel |
| 📝&nbsp;[#89522](https://github.com/openclaw/openclaw/issues/89522) | 0 | Model routing/config | @Gausons | [Feature]: Inherit requester session model for native subagents |
| 📝&nbsp;[#89477](https://github.com/openclaw/openclaw/issues/89477) | 0 | Local memory/embedding | @ubehera | [Feature]: optional cross-encoder rerank stage for memory search |
| 📝&nbsp;[#89473](https://github.com/openclaw/openclaw/issues/89473) | 0 | Model/provider behavior | @zax0rz | [Bug]: Reasoning tokens leak to chat channels when models stream interleaved text/thinking blocks |
| 🔀&nbsp;[#89469](https://github.com/openclaw/openclaw/pull/89469) | 0 | Model routing/config | @Gausons | feat(agents): inherit requester model for subagents |
| 📝&nbsp;[#89444](https://github.com/openclaw/openclaw/issues/89444) | 0 | Local memory/embedding | @Josephur | Dreaming promotion still writes raw/junk data into MEMORY.md (regression from #67580) |
| 📝&nbsp;[#89362](https://github.com/openclaw/openclaw/issues/89362) | 0 | Local memory/embedding | @BomBastikDE | Expose batchEmbed from the Ollama memory adapter so batch indexing can be enabled |
| 🔀&nbsp;[#89334](https://github.com/openclaw/openclaw/pull/89334) | 0 | Local memory/embedding | @AdrianIp0204 | docs: note active memory timeout circuit breaker |
| 📝&nbsp;[#89278](https://github.com/openclaw/openclaw/issues/89278) | 0 | Model routing/config | @kopl-blip | [Bug]: Codex OAuth refresh succeeds but cron/heartbeat fail with 10s auth refresh timeout |
| 🔀&nbsp;[#89155](https://github.com/openclaw/openclaw/pull/89155) | 0 | Open-weight/provider behavior | @Alex-vonAllmen | feat(openrouter): forward OpenClaw session id as session_id |
| 📝&nbsp;[#89147](https://github.com/openclaw/openclaw/issues/89147) | 0 | Model/provider behavior | @scipher888 | Native hook relay starves mid-turn after long model-thinking gap (renewal loop tool-call-driven) |
| 🔀&nbsp;[#89117](https://github.com/openclaw/openclaw/pull/89117) | 0 | Local memory/embedding | @abel-zer0 | Support Gemini Embedding 2 GA |
| 📝&nbsp;[#89114](https://github.com/openclaw/openclaw/issues/89114) | 0 | Open-weight/provider behavior | @superandylin | Minimax M3: /think menu missing xhigh, adaptive, max levels (provider profile limitation) |
| 📝&nbsp;[#89100](https://github.com/openclaw/openclaw/issues/89100) | 0 | Open-weight/provider behavior | @bobgitmcgrath | Sanitise outbound message.send tool arguments to prevent runtime scaffolding leak (FM-3) and chat_id routing bleed (FM-2) on weaker models |
| 🔀&nbsp;[#89040](https://github.com/openclaw/openclaw/pull/89040) | 0 | Local model runtime | @Jerry-Xin | perf: avoid event-loop stall during embedded_run bootstrap-context |
| 🔀&nbsp;[#89039](https://github.com/openclaw/openclaw/pull/89039) | 0 | OpenAI-compatible/proxy | @Jerry-Xin | fix: prevent silent message loss from EmbeddedAttemptSessionTakeoverError |
| 🔀&nbsp;[#88905](https://github.com/openclaw/openclaw/pull/88905) | 0 | Local memory/embedding | @iFiras-Max1 | feat(dreaming): expose shadow-trial scoring in reports |
| 📝&nbsp;[#88868](https://github.com/openclaw/openclaw/issues/88868) | 0 | Open-weight/provider behavior | @NianJiuZst | Add MiniMax M3 support to the bundled MiniMax provider |
| 🔀&nbsp;[#88754](https://github.com/openclaw/openclaw/pull/88754) | 0 | Open-weight/provider behavior | @Kailigithub | fix(text): normalize CJK/fullwidth quotes in reasoning tag delimiters |
| 🔀&nbsp;[#88709](https://github.com/openclaw/openclaw/pull/88709) | 0 | Model routing/config | @MertBasar0 | fix(auth): cooldown inline api key billing failures |
| 📝&nbsp;[#88707](https://github.com/openclaw/openclaw/issues/88707) | 0 | Model routing/config | @podulator | [Bug] Regression 2026.5.27→2026.5.28: "No API provider registered for api: bedrock-converse-stream" — pi-ai removal breaks Bedrock provider registration; bearer token auth broken |
| 📝&nbsp;[#88657](https://github.com/openclaw/openclaw/issues/88657) | 0 | Open-weight/provider behavior | @mikefaierberg-byte | Bug: DeepSeek V4 Flash incomplete turn (payloads=0, tools=2, replaySafe=no, stopReason=stop) in 2026.5.27/28 |
| 📝&nbsp;[#88616](https://github.com/openclaw/openclaw/issues/88616) | 0 | Model routing/config | @Alex-vonAllmen | [Feature]: Forward session_id to OpenRouter for sticky routing & prompt caching |
| 📝&nbsp;[#88562](https://github.com/openclaw/openclaw/issues/88562) | 0 | Model routing/config | @mnowrot | [Bug]: models.json generator writes apiKey as plain string instead of secret-ref object |
| 🔀&nbsp;[#88329](https://github.com/openclaw/openclaw/pull/88329) | 0 | Model routing/config | @Knowcheng | fix: user-pinned model falls back to global chain on quota exhaustion |
| 🔀&nbsp;[#88249](https://github.com/openclaw/openclaw/pull/88249) | 0 | Model routing/config | @Darclindy | feat(desktop): add Tauri model setup app |
| 📝&nbsp;[#88201](https://github.com/openclaw/openclaw/issues/88201) | 0 | Local model runtime | @adamdksaad-ops | [Bug]: OpenClaw 5.22: ~10 sec per-call inference overhead in infer model run (both --gateway and --local) vs ~1.3 sec direct provider call<br>Assignee: steipete |
| 📝&nbsp;[#88079](https://github.com/openclaw/openclaw/issues/88079) | 0 | Open-weight/provider behavior | @xx1170822819 | [Regression] WebChat: reasoning_content not streamed for Kimi Code & DeepSeek Reasoner — only MiniMax works |
| 🔀&nbsp;[#88078](https://github.com/openclaw/openclaw/pull/88078) | 0 | Local memory/embedding | @gisk0 | fix(active-memory): trim recall prompt envelope |
| 📝&nbsp;[#88077](https://github.com/openclaw/openclaw/issues/88077) | 0 | Local memory/embedding | @gisk0 | [Bug]: Active Memory recall context uses full OpenClaw prompt envelope |
| 📝&nbsp;[#87957](https://github.com/openclaw/openclaw/issues/87957) | 0 | Model routing/config | @osolmaz | Refactor session model/auth state resolution |
| 📝&nbsp;[#87925](https://github.com/openclaw/openclaw/issues/87925) | 0 | Model routing/config | @hoobnn | thinkingLevel: model switch silently downgrades and persists an inherited explicit override |
| 📝&nbsp;[#87816](https://github.com/openclaw/openclaw/issues/87816) | 0 | Local/media model provider | @DoiiarX | feat(tts): xiaomi voicedesign/voiceclone model support |
| 📝&nbsp;[#87763](https://github.com/openclaw/openclaw/issues/87763) | 0 | OpenAI-compatible/proxy | @georgenaz | SSRF guard pinned DNS dispatcher causes model fetch timeouts when autoSelectFamily is enabled |
| 📝&nbsp;[#87689](https://github.com/openclaw/openclaw/issues/87689) | 0 | Local memory/embedding | @Countermarch | Dreaming needs supported guard to disable session transcript ingestion during QMD migrations |
| 📝&nbsp;[#87687](https://github.com/openclaw/openclaw/issues/87687) | 0 | Local model runtime | @sonofanton44 | vllm openai-completions streaming parser drops tool_calls when reasoning_content streams first for gpt-oss-120b at large systemPrompt |
| 📝&nbsp;[#87466](https://github.com/openclaw/openclaw/issues/87466) | 0 | Local/media model provider | @UrsineBear | [Bug]:Telegram voice delivery is unstable across model runtimes because voice generation depends on model-generated media tags |
| 📝&nbsp;[#87443](https://github.com/openclaw/openclaw/issues/87443) | 0 | Local memory/embedding | @bxf471494973 | sqlite-vec vector search fails on musl-based systems |
| 🔀&nbsp;[#87414](https://github.com/openclaw/openclaw/pull/87414) | 0 | Local model runtime | @ezcoder | [codex] Key llama.cpp sessions for local reuse |
| 🔀&nbsp;[#87343](https://github.com/openclaw/openclaw/pull/87343) | 0 | Model routing/config | @riosbotchen-source | feat(cron): surface fallback progress |
| 📝&nbsp;[#87277](https://github.com/openclaw/openclaw/issues/87277) | 0 | Open-weight/provider behavior | @0mlkrizzz655335v | [Feature] Add MiMo-V2.5 to Xiaomi catalog + automatic multimodal routing when DeepSeek V4-Pro is primary model |
| 📝&nbsp;[#87267](https://github.com/openclaw/openclaw/issues/87267) | 0 | Local model runtime | @rogerallen1 | [Bug]: Dream Diary narrative needs separate config for timeout/concurrency or disablement, while keeping dreaming enabled. |
| 🔀&nbsp;[#86776](https://github.com/openclaw/openclaw/pull/86776) | 0 | Model routing/config | @kierandotai | fix(models): apply provider policy defaults to inline models |
| 📝&nbsp;[#86182](https://github.com/openclaw/openclaw/issues/86182) | 0 | Local model runtime | @rendrag-git | discord/picker: structural 25-option / 5-row / 100-char limits constrain large wildcard configs |
| 📝&nbsp;[#86174](https://github.com/openclaw/openclaw/issues/86174) | 0 | Model routing/config | @rqlangley | [Bug]: WebChat + New Session displays default model but inherits parent's model override |
| 📝&nbsp;[#85684](https://github.com/openclaw/openclaw/issues/85684) | 0 | OpenAI-compatible/proxy | @iFwu | pi-embedded-runner: reasoning-only retry short-circuited in group chats by silentReplyPolicy default |
| 📝&nbsp;[#84918](https://github.com/openclaw/openclaw/issues/84918) | 0 | OpenAI-compatible/proxy | @killo3967 | OpenWebUI image uploads reach image tool as empty image via /v1/chat/completions on 2026.5.18 |
| 📝&nbsp;[#84865](https://github.com/openclaw/openclaw/issues/84865) | 0 | Open-weight/provider behavior | @njuboy11 | user-switched model has no fallback chain, causing session deadlock on provider outage<br>Assignee: osolmaz |
| 🔀&nbsp;[#84554](https://github.com/openclaw/openclaw/pull/84554) | 0 | Local memory/embedding | @jetd1 | fix(memory-core): guard builtin fallback after qmd failures |
| 📝&nbsp;[#84217](https://github.com/openclaw/openclaw/issues/84217) | 0 | Local model runtime | @fanispoulinakisai-boop | [Bug]: Heartbeat dispatch delivers free text block alongside message-tool call (chatty non-Codex providers, v2026.5.18) |
| 🔀&nbsp;[#84072](https://github.com/openclaw/openclaw/pull/84072) | 0 | Model routing/config | @wiatrM | Add model fallback circuit breaker |
| 📝&nbsp;[#83399](https://github.com/openclaw/openclaw/issues/83399) | 0 | OpenAI-compatible/proxy | @yuzhihui886 | Bug: Tool call loop when assistant generates text + toolCall with openai-completions API |
| 📝&nbsp;[#81925](https://github.com/openclaw/openclaw/issues/81925) | 0 | Local memory/embedding | @castigiova | Compaction: `after_compaction` not emitted when `result.compacted:false`; validation: single-quote delimiter trips tool-caller retries |
| 📝&nbsp;[#81835](https://github.com/openclaw/openclaw/issues/81835) | 0 | OpenAI-compatible/proxy | @STLI69 | Bug: thinking parameter format incompatible with Volcengine CodingPlan v3 API |
| 🔀&nbsp;[#80957](https://github.com/openclaw/openclaw/pull/80957) | 0 | OpenAI-compatible/proxy | @chenyanchen | fix: refresh status context window after model switch |
| 📝&nbsp;[#80521](https://github.com/openclaw/openclaw/issues/80521) | 0 | Local model runtime | @wherewolf87 | UI feature request: model picker + drag-to-reorder for primary/fallback model selection in Agents > Overview |
| 🔀&nbsp;[#80418](https://github.com/openclaw/openclaw/pull/80418) | 0 | OpenAI-compatible/proxy | @logicbridgedev | fix(/v1/responses): accept text field on requests for OpenAI SDK 6.x parity |
| 📝&nbsp;[#80336](https://github.com/openclaw/openclaw/issues/80336) | 0 | Local model runtime | @kinerliu | [Bug]: placeholder.openclaw.cloud unreachable on WSL2 with custom gateway port |
| 🔀&nbsp;[#80033](https://github.com/openclaw/openclaw/pull/80033) | 0 | Open-weight/provider behavior | @wrcno1 | fix(opencode-go): add supportedReasoningEfforts to DeepSeek V4 model entries |
| 📝&nbsp;[#79437](https://github.com/openclaw/openclaw/issues/79437) | 0 | Local memory/embedding | @bp2u | Prebuilt `node-llama-cpp` Windows binaries crash (0xC0000005) on Intel Alder Lake-N (N95) - qmd LLM half unusable |
| 🔀&nbsp;[#79185](https://github.com/openclaw/openclaw/pull/79185) | 0 | Open-weight/provider behavior | @kidding1412 | fix(tts/xiaomi): support Token Plan TTS endpoint |
| 📝&nbsp;[#78091](https://github.com/openclaw/openclaw/issues/78091) | 0 | OpenAI-compatible/proxy | @wurdzy | [Bug]: Open-WebUI creates new session per message instead of reusing persistent session |
| 📝&nbsp;[#75189](https://github.com/openclaw/openclaw/issues/75189) | 0 | Local model runtime | @camerono | [Bug]: Default `bootstrapMaxChars=20000` + verbose auto-generated bootstrap content degrades tool dispatch on small/mid models |
| 📝&nbsp;[#75187](https://github.com/openclaw/openclaw/issues/75187) | 0 | Local model runtime | @camerono | [Bug]: Auto-generated `AGENTS.md` puts load-bearing tool-use rules at the bottom; head-truncation by `bootstrapMaxChars` strips them |
| 📝&nbsp;[#75040](https://github.com/openclaw/openclaw/issues/75040) | 0 | Local model runtime | @kingkong9817 | [Bug]: extra_body overwriting request payload keys: thinking - framework-level thinking field collision affecting all providers |
| 📝&nbsp;[#74481](https://github.com/openclaw/openclaw/issues/74481) | 0 | OpenAI-compatible/proxy | @sunapi386 | feat: dynamic catalog refresh from configured provider /v1/models |
| 📝&nbsp;[#74204](https://github.com/openclaw/openclaw/issues/74204) | 0 | Local memory/embedding | @Skeptomenos | memory.qmd.update.embedTimeoutMs default (120 s) is too low for local GGUF; error message doesn't surface the fix<br>Assignee: osolmaz |
| 📝&nbsp;[#72359](https://github.com/openclaw/openclaw/issues/72359) | 0 | Local memory/embedding | @thecolormaroun | Active Memory: add single-shot mode (no embedded agent loop) for low-latency preflight injection |
| 📝&nbsp;[#63531](https://github.com/openclaw/openclaw/issues/63531) | 0 | Local memory/embedding | @ImLukeF | [Feature]: Add MLX Talk provider MVP for local macOS TTS |
| 📝&nbsp;[#61716](https://github.com/openclaw/openclaw/issues/61716) | 0 | OpenAI-compatible/proxy | @Andy-Xie-1145 | [Feature]: Add model parameter prompts (context window, max_tokens, modalities) during OpenAI-compatible provider onboarding CLI flow |
| 📝&nbsp;[#57443](https://github.com/openclaw/openclaw/issues/57443) | 0 | OpenAI-compatible/proxy | @wujiaming88 | [Bug]: Tool JSON Schema patternProperties causes 400 errors on BytePlus Ark (doubao) - schema cleaning should be universal, not provider-specific |
| 📝&nbsp;[#54128](https://github.com/openclaw/openclaw/issues/54128) | 0 | Local memory/embedding | @hsuaaron | Add maxThreads config for local embedding (node-llama-cpp) |
| 📝&nbsp;[#53810](https://github.com/openclaw/openclaw/issues/53810) | 0 | OpenAI-compatible/proxy | @FiredMosquito831 | Subagent Premature Announce Bug - Model-Specific Tool Call Handling Issues |
| 📝&nbsp;[#44789](https://github.com/openclaw/openclaw/issues/44789) | 0 | OpenAI-compatible/proxy | @Hylance | [Bug]: openclaw 2026.03.11 partially config litellm |
| 📝&nbsp;[#43432](https://github.com/openclaw/openclaw/issues/43432) | 0 | Local memory/embedding | @omegabyte-ai | [Feature]: Memory durability config - hard flush threshold, priority-aware compaction, cache TTL |
| 📝&nbsp;[#42408](https://github.com/openclaw/openclaw/issues/42408) | 0 | Local memory/embedding | @1sexywoo8 | [Bug/Docs]: local+hybrid memory_search quality can appear unstable due to extraPaths path drift + benchmark-file contamination |

</details>

## RECENTLY CLOSED OR REMOVED FROM OPEN INVENTORY

<details>
<summary>2586 closed or removed reviewed threads</summary>

| Thread | Status checked | Note |
| --- | --- | --- |
| [#110683](https://github.com/openclaw/openclaw/pull/110683) | Closed in local gitcrawl 2026-07-18 | fix(agents): repeated tool-call ids bind results to the wrong call on replay; no longer open. |
| [#110627](https://github.com/openclaw/openclaw/pull/110627) | Closed in local gitcrawl | fix: bound pasted input and provider response bodies; no longer open. |
| [#110617](https://github.com/openclaw/openclaw/pull/110617) | Closed in local gitcrawl | fix: custom Anthropic models work without maxTokens; no longer open. |
| [#110612](https://github.com/openclaw/openclaw/pull/110612) | Closed in local gitcrawl | fix(agents): use fatal TextDecoder to reject malformed UTF-8 in provider transport streams; no longer open. |
| [#110597](https://github.com/openclaw/openclaw/pull/110597) | Closed in local gitcrawl | feat(memory): default cross-conversation recall for personal installs; no longer open. |
| [#110596](https://github.com/openclaw/openclaw/pull/110596) | Closed in local gitcrawl | feat(onboarding): enable lean mode for local models; no longer open. |
| [#110506](https://github.com/openclaw/openclaw/pull/110506) | Closed in local gitcrawl | fix(tts): guard persona provider isConfigured against malformed config throws; no longer open. |
| [#110502](https://github.com/openclaw/openclaw/pull/110502) | Closed in local gitcrawl | fix(memory): reject malformed embedding batch JSONL bytes; no longer open. |
| [#110495](https://github.com/openclaw/openclaw/pull/110495) | Closed in local gitcrawl | fix(signal): preserve reverse-proxy path prefixes; no longer open. |
| [#110474](https://github.com/openclaw/openclaw/pull/110474) | Closed in local gitcrawl | fix(status): consolidate live model switches so /status stops reporting stale state; no longer open. |
| [#110468](https://github.com/openclaw/openclaw/pull/110468) | Closed in local gitcrawl | fix: show background commands after agent turns; no longer open. |
| [#110439](https://github.com/openclaw/openclaw/issues/110439) | Closed in local gitcrawl | [Bug]: models status reports Codex usable when the harness plugin is unavailable; no longer open. |
| [#110405](https://github.com/openclaw/openclaw/pull/110405) | Closed in local gitcrawl | fix(opencode): Zen GPT-5.6 models are missing from discovery; no longer open. |
| [#110364](https://github.com/openclaw/openclaw/pull/110364) | Closed in local gitcrawl | fix(model-selection): preserve pinned override when the model catalog is degraded; no longer open. |
| [#110339](https://github.com/openclaw/openclaw/pull/110339) | Closed in local gitcrawl | feat(clients): provider-grouped model picker with fast, verbosity, and inherited-thinking controls; no longer open. |
| [#110313](https://github.com/openclaw/openclaw/pull/110313) | Closed in local gitcrawl | fix(agents): reduce cron trigger script maxLength to 2000 for llama.cpp GBNF compatibility; no longer open. |
| [#110308](https://github.com/openclaw/openclaw/pull/110308) | Closed in local gitcrawl | improve(agents): normalized web_search output contract with boundary-owned wrapping; no longer open. |
| [#110243](https://github.com/openclaw/openclaw/pull/110243) | Closed in local gitcrawl | fix(release): carry the Z.AI API Platform waiver; no longer open. |
| [#110233](https://github.com/openclaw/openclaw/pull/110233) | Closed in local gitcrawl | fix(llama-cpp): prevent local GGUF asset path failures; no longer open. |
| [#110113](https://github.com/openclaw/openclaw/pull/110113) | Closed in local gitcrawl | feat(omniroute): add bundled OmniRoute provider plugin; no longer open. |
| [#110093](https://github.com/openclaw/openclaw/issues/110093) | Closed in local gitcrawl | sessions_spawn ignores model parameter for non-default providers; no longer open. |
| [#110080](https://github.com/openclaw/openclaw/pull/110080) | Closed in local gitcrawl | fix(ai): signed thinking replays across providers permanently bricks Claude 5 sessions; no longer open. |
| [#110079](https://github.com/openclaw/openclaw/issues/110079) | Closed in local gitcrawl | [Bug]: signed thinking replays across providers — switching Claude 5 sessions between anthropic/Bedrock-Mantle/Vertex permanently bricks the session; no longer open. |
| [#110056](https://github.com/openclaw/openclaw/issues/110056) | Closed in local gitcrawl | [Bug]: Docker runtime image omits packages/, so bundled ollama extension fails to load (@openclaw/model-catalog-core/configured-model-refs unresolved); no longer open. |
| [#110055](https://github.com/openclaw/openclaw/issues/110055) | Closed in local gitcrawl | [Bug]: Compaction triggers at 9-16% context usage despite 1M window and 30K reserve floor; no longer open. |
| [#109977](https://github.com/openclaw/openclaw/pull/109977) | Closed in local gitcrawl | fix: keep memory SecretRef failures agent-scoped; no longer open. |
| [#109975](https://github.com/openclaw/openclaw/pull/109975) | Closed in local gitcrawl | fix(google-oauth): cancel unread response body on non-ok HTTP responses; no longer open. |
| [#109921](https://github.com/openclaw/openclaw/pull/109921) | Closed in local gitcrawl | fix(ollama): failed inspections must not advertise tools capability; no longer open. |
| [#109895](https://github.com/openclaw/openclaw/pull/109895) | Closed in local gitcrawl | fix(ollama): one broken local model no longer bricks interactive setup; no longer open. |
| [#109891](https://github.com/openclaw/openclaw/pull/109891) | Closed in local gitcrawl | fix(openrouter): cancel response body on OAuth key exchange error; no longer open. |
| [#109848](https://github.com/openclaw/openclaw/pull/109848) | Closed in local gitcrawl | fix(openrouter): guard video URL resolution against malformed base URLs; no longer open. |
| [#109810](https://github.com/openclaw/openclaw/pull/109810) | Closed in local gitcrawl | fix(qa-lab): omit empty openai.baseUrl in live-frontier child config; no longer open. |
| [#109800](https://github.com/openclaw/openclaw/pull/109800) | Closed in local gitcrawl | fix(models): reject oversized piped auth input; no longer open. |
| [#109796](https://github.com/openclaw/openclaw/pull/109796) | Closed in local gitcrawl | fix: provider usage accounting, retry/overflow classification, and output clamping; no longer open. |
| [#109764](https://github.com/openclaw/openclaw/pull/109764) | Closed in local gitcrawl | feat(setup): stream provider prepare progress to every surface; no longer open. |
| [#109760](https://github.com/openclaw/openclaw/pull/109760) | Closed in local gitcrawl | fix(coding-agent): prevent workers from invalidating OpenClaw OAuth; no longer open. |
| [#109740](https://github.com/openclaw/openclaw/pull/109740) | Closed in local gitcrawl | fix: Bedrock ARN region routing, Copilot device-flow pacing, TUI input fixes; no longer open. |
| [#109718](https://github.com/openclaw/openclaw/pull/109718) | Closed in local gitcrawl | fix(lmstudio): cancel model discovery response body on non-ok; no longer open. |
| [#109691](https://github.com/openclaw/openclaw/pull/109691) | Closed in local gitcrawl 2026-07-18 | fix(ai): skip blank environment credentials during provider auth; no longer open. |
| [#109681](https://github.com/openclaw/openclaw/pull/109681) | Closed in local gitcrawl | feat(onboarding): unified empty-state with provider icons, websites, and recommended installs; no longer open. |
| [#109677](https://github.com/openclaw/openclaw/pull/109677) | Closed in local gitcrawl | fix(chutes): cancel userinfo error response body before returning null; no longer open. |
| [#109666](https://github.com/openclaw/openclaw/pull/109666) | Closed in local gitcrawl | fix(providers): refresh zai/kimi/moonshot/xai catalogs against July 2026 vendor docs; no longer open. |
| [#109636](https://github.com/openclaw/openclaw/pull/109636) | Closed in local gitcrawl | refactor(memory): move QMD coordination to SQLite; no longer open. |
| [#109615](https://github.com/openclaw/openclaw/pull/109615) | Closed in local gitcrawl | fix: Responses streams mishandle interleaved output items and silent truncation; no longer open. |
| [#109585](https://github.com/openclaw/openclaw/pull/109585) | Closed in local gitcrawl | feat(llama-cpp): RAM-gated Gemma 4 E4B default, drop Qwen; no longer open. |
| [#109556](https://github.com/openclaw/openclaw/pull/109556) | Closed in local gitcrawl | fix: OpenAI-compatible provider compat and error-body surfacing; no longer open. |
| [#109474](https://github.com/openclaw/openclaw/pull/109474) | Closed in local gitcrawl | fix(xai): treat blank env API key as unconfigured in speech provider; no longer open. |
| [#109472](https://github.com/openclaw/openclaw/pull/109472) | Closed in local gitcrawl | fix(vydra): treat blank env API key as unconfigured in speech provider; no longer open. |
| [#109464](https://github.com/openclaw/openclaw/pull/109464) | Closed in local gitcrawl | fix(huggingface): release connections after failed model discovery; no longer open. |
| [#109447](https://github.com/openclaw/openclaw/pull/109447) | Closed in local gitcrawl | fix: model calls fail with provider 400 when tool-call ids repeat across assistant turns; no longer open. |
| [#109445](https://github.com/openclaw/openclaw/pull/109445) | Closed in local gitcrawl | feat(system-agent): local-model viability — context cap, thinking off, route-aware timeout; no longer open. |
| [#109444](https://github.com/openclaw/openclaw/pull/109444) | Closed in local gitcrawl | feat(llama-cpp): in-process local GGUF text inference provider; no longer open. |
| [#109443](https://github.com/openclaw/openclaw/issues/109443) | Closed in local gitcrawl | Transcript repair drops tool results when tool-call ids repeat across turns — every model call fails with provider 400 until session reset; no longer open. |
| [#109403](https://github.com/openclaw/openclaw/pull/109403) | Closed in local gitcrawl | fix(dreaming): drop heartbeat assistant responses from dream corpus; no longer open. |
| [#109396](https://github.com/openclaw/openclaw/pull/109396) | Closed in local gitcrawl | fix(agents): add global thinkingDefault fallback in resolveAgentConfig (#109276); no longer open. |
| [#109375](https://github.com/openclaw/openclaw/issues/109375) | Closed in local gitcrawl | [Bug]: Steer message causes error when model is mid-tool-call; no longer open. |
| [#109355](https://github.com/openclaw/openclaw/pull/109355) | Closed in local gitcrawl | fix: prevent doctor hangs on large Memory Core migrations; no longer open. |
| [#109335](https://github.com/openclaw/openclaw/pull/109335) | Closed in local gitcrawl | fix(kimi): honor K3 thinking off; no longer open. |
| [#109334](https://github.com/openclaw/openclaw/issues/109334) | Closed in local gitcrawl | Kimi Code K3 ignores /think off; no longer open. |
| [#109291](https://github.com/openclaw/openclaw/pull/109291) | Closed in local gitcrawl | improve: prove Codex auth migration product flow; no longer open. |
| [#109276](https://github.com/openclaw/openclaw/issues/109276) | Closed in local gitcrawl | [Bug]: thinkingDefault missing global fallback in resolveAgentConfig — agents.defaults.thinkingDefault has no effect for per-agent entries; no longer open. |
| [#109265](https://github.com/openclaw/openclaw/pull/109265) | Closed in local gitcrawl | fix(memory): bound qmd taskkill cleanup; no longer open. |
| [#109250](https://github.com/openclaw/openclaw/pull/109250) | Closed in local gitcrawl | feat(onboarding): prefer strongest local model in guided detection; no longer open. |
| [#109246](https://github.com/openclaw/openclaw/pull/109246) | Closed in local gitcrawl | test(ci): temporarily omit Z.AI API Platform validation; no longer open. |
| [#109216](https://github.com/openclaw/openclaw/pull/109216) | Closed in local gitcrawl | fix(gateway): bound optional model catalog slow-load log cache; no longer open. |
| [#109202](https://github.com/openclaw/openclaw/pull/109202) | Closed in local gitcrawl | feat(moonshot): add Kimi K3 support; no longer open. |
| [#109181](https://github.com/openclaw/openclaw/pull/109181) | Closed in local gitcrawl | fix: shard OpenAI transport stream tests; no longer open. |
| [#109095](https://github.com/openclaw/openclaw/pull/109095) | Closed in local gitcrawl | fix(openai): idle-timeout stalled OAuth token response bodies; no longer open. |
| [#109094](https://github.com/openclaw/openclaw/pull/109094) | Closed in local gitcrawl | fix(models): idle-timeout stalled OpenRouter capabilities catalog body; no longer open. |
| [#109071](https://github.com/openclaw/openclaw/pull/109071) | Closed in local gitcrawl | fix(github-copilot): prevent stalled catalog error streams; no longer open. |
| [#109069](https://github.com/openclaw/openclaw/pull/109069) | Closed in local gitcrawl | fix(models): idle-timeout stalled OpenRouter capabilities catalog body; no longer open. |
| [#109066](https://github.com/openclaw/openclaw/pull/109066) | Closed in local gitcrawl | fix(agents): short-circuit model fallback chain when result has delivery evidence (#108262); no longer open. |
| [#109027](https://github.com/openclaw/openclaw/pull/109027) | Closed in local gitcrawl | fix: tag Chat Completions tool-call preambles as commentary; no longer open. |
| [#109026](https://github.com/openclaw/openclaw/pull/109026) | Closed in local gitcrawl | fix(zai): keep probe deadline through stalled error-body reads; no longer open. |
| [#109018](https://github.com/openclaw/openclaw/pull/109018) | Closed in local gitcrawl | fix(memory): indexing survives transient embedding rate limits; no longer open. |
| [#108994](https://github.com/openclaw/openclaw/pull/108994) | Closed in local gitcrawl | fix(memory-core): differentiate rate-limit (429) backoff from transient errors in embedding retry (#108893); no longer open. |
| [#108982](https://github.com/openclaw/openclaw/pull/108982) | Closed in local gitcrawl | fix(openai): bound stalled generated video download body reads with idle timeout; no longer open. |
| [#108972](https://github.com/openclaw/openclaw/pull/108972) | Closed in local gitcrawl | fix(models): honor scan timeout while reading OpenRouter catalog; no longer open. |
| [#108966](https://github.com/openclaw/openclaw/pull/108966) | Closed in local gitcrawl | fix(agents): safe codex tool-terminal continuation, auth-true simple-completion routes, doctor opt-out; no longer open. |
| [#108939](https://github.com/openclaw/openclaw/pull/108939) | Closed in local gitcrawl | fix: honor Retry-After header in memory embeddings batch retry (#108893); no longer open. |
| [#108872](https://github.com/openclaw/openclaw/pull/108872) | Closed in local gitcrawl | fix(memory-host): accept repeated content length values; no longer open. |
| [#108783](https://github.com/openclaw/openclaw/pull/108783) | Closed in local gitcrawl | fix(inworld): treat blank env API key as unconfigured in speech provider; no longer open. |
| [#108777](https://github.com/openclaw/openclaw/pull/108777) | Closed in local gitcrawl | fix(minimax): ignore blank environment API key; no longer open. |
| [#108773](https://github.com/openclaw/openclaw/pull/108773) | Closed in local gitcrawl | fix(plugins): allow runtime.llm.complete to pass reasoning effort; no longer open. |
| [#108759](https://github.com/openclaw/openclaw/pull/108759) | Closed in local gitcrawl | fix(plugin-sdk): let runtime completions request reasoning; no longer open. |
| [#108758](https://github.com/openclaw/openclaw/pull/108758) | Closed in local gitcrawl | fix(clawrouter): normalize Perplexity tool schemas and harden dynamic model cache; no longer open. |
| [#108753](https://github.com/openclaw/openclaw/issues/108753) | Closed in local gitcrawl | [Bug]: Bedrock application profile lookup can hang indefinitely; no longer open. |
| [#108751](https://github.com/openclaw/openclaw/pull/108751) | Closed in local gitcrawl | fix(anthropic): declare GA 1M context window for opus-4-7/sonnet-4-6/opus-4-6 (issue #108152); no longer open. |
| [#108721](https://github.com/openclaw/openclaw/pull/108721) | Closed in local gitcrawl | refactor(agents): share Responses tool-call tracking; no longer open. |
| [#108708](https://github.com/openclaw/openclaw/pull/108708) | Closed in local gitcrawl | feat: add Baseten Model API provider; no longer open. |
| [#108683](https://github.com/openclaw/openclaw/pull/108683) | Closed in local gitcrawl | fix(openai): harden codex catalog, routing opt-out, and WHAM half-open reprobe; no longer open. |
| [#108680](https://github.com/openclaw/openclaw/pull/108680) | Closed in local gitcrawl | fix(auth): session refresh preserves OAuth providers; no longer open. |
| [#108674](https://github.com/openclaw/openclaw/pull/108674) | Closed in local gitcrawl | fix: standalone OAuth test teardown failures; no longer open. |
| [#108665](https://github.com/openclaw/openclaw/issues/108665) | Closed in local gitcrawl | [Feature]: Add Baseten Model API provider support; no longer open. |
| [#108646](https://github.com/openclaw/openclaw/pull/108646) | Closed in local gitcrawl | test(agents): harden Z.AI live output probe; no longer open. |
| [#108640](https://github.com/openclaw/openclaw/pull/108640) | Closed in local gitcrawl | fix(zai): backport documented transport payloads; no longer open. |
| [#108635](https://github.com/openclaw/openclaw/pull/108635) | Closed in local gitcrawl | fix(config): inherit provider-level model token defaults; no longer open. |
| [#108633](https://github.com/openclaw/openclaw/pull/108633) | Closed in local gitcrawl | fix(zai): use documented thinking payload; no longer open. |
| [#108631](https://github.com/openclaw/openclaw/issues/108631) | Closed in local gitcrawl | Feedback: embedding setup experience on v2026.5.28 — default OpenAI assumption and Intel macOS GGUF SIGKILL; no longer open. |
| [#108617](https://github.com/openclaw/openclaw/pull/108617) | Closed in local gitcrawl | fix(onboarding): preserve OAuth across runtime defaults; no longer open. |
| [#108613](https://github.com/openclaw/openclaw/issues/108613) | Closed in local gitcrawl | Duplicate model id "claude-sonnet-5" across claude-cli/anthropic providers causes blank dropdown entry; no longer open. |
| [#108612](https://github.com/openclaw/openclaw/pull/108612) | Closed in local gitcrawl | fix(zai): return text from constrained GLM completions; no longer open. |
| [#108607](https://github.com/openclaw/openclaw/pull/108607) | Closed in local gitcrawl | fix: retain tool arguments when Responses item IDs rotate; no longer open. |
| [#108605](https://github.com/openclaw/openclaw/pull/108605) | Closed in local gitcrawl | feat(onboarding): detect local inference providers; no longer open. |
| [#108592](https://github.com/openclaw/openclaw/pull/108592) | Closed in local gitcrawl | fix: provider dead exports no longer block changed checks; no longer open. |
| [#108583](https://github.com/openclaw/openclaw/pull/108583) | Closed in local gitcrawl | refactor(memory-core): split manager sync operations; no longer open. |
| [#108569](https://github.com/openclaw/openclaw/pull/108569) | Closed in local gitcrawl | fix(gradium): return false from isConfigured on invalid baseUrl instead of throwing; no longer open. |
| [#108559](https://github.com/openclaw/openclaw/issues/108559) | Closed in local gitcrawl | Bug: Dreaming promotes daily-only operational residue despite recall/query gates; no longer open. |
| [#108558](https://github.com/openclaw/openclaw/pull/108558) | Closed in local gitcrawl | fix(xiaomi): treat blank env API key as unconfigured in speech provider; no longer open. |
| [#108551](https://github.com/openclaw/openclaw/pull/108551) | Closed in local gitcrawl | fix(gradium): keep isConfigured from throwing on invalid baseUrl; no longer open. |
| [#108550](https://github.com/openclaw/openclaw/issues/108550) | Closed in local gitcrawl | [Bug]: Gradium speech provider isConfigured throws on invalid baseUrl; no longer open. |
| [#108532](https://github.com/openclaw/openclaw/issues/108532) | Closed in local gitcrawl | [Bug]: Memory Core legacy migration fails on v2026.7.1 upgrade — 'legacy memory meta rows conflict with canonical memory index rows'; no longer open. |
| [#108525](https://github.com/openclaw/openclaw/pull/108525) | Closed in local gitcrawl | fix(release): retry empty live provider responses; no longer open. |
| [#108511](https://github.com/openclaw/openclaw/issues/108511) | Closed in local gitcrawl | Responses streaming transport drops tool-call argument deltas when the provider rotates per-event item_id (breaks GitHub Copilot gpt-5.6-sol tool use); no longer open. |
| [#108503](https://github.com/openclaw/openclaw/pull/108503) | Closed in local gitcrawl | fix(ci): remove unused vLLM runtime bridge; no longer open. |
| [#108500](https://github.com/openclaw/openclaw/pull/108500) | Closed in local gitcrawl | refactor(vllm): remove unused registration shim; no longer open. |
| [#108475](https://github.com/openclaw/openclaw/issues/108475) | Closed in local gitcrawl | active-memory: recall subagent output is injected without validation — fluent confabulations pass the untrusted-context wrapper; no longer open. |
| [#108474](https://github.com/openclaw/openclaw/pull/108474) | Closed in local gitcrawl | refactor(codex)!: fold the codex text provider into openai with a doctor migration; no longer open. |
| [#108471](https://github.com/openclaw/openclaw/issues/108471) | Closed in local gitcrawl | iOS app: quick agent/model switch, session name in header, message queueing during processing; no longer open. |
| [#108400](https://github.com/openclaw/openclaw/pull/108400) | Closed in local gitcrawl | fix(ci): authenticate live Codex Docker release probe; no longer open. |
| [#108397](https://github.com/openclaw/openclaw/pull/108397) | Closed in local gitcrawl | fix(memory-core): write MEMORY.md atomically during short-term promotion; no longer open. |
| [#108396](https://github.com/openclaw/openclaw/pull/108396) | Closed in local gitcrawl | fix(media-understanding): add 3-level model fallback chain to video buildRequest; no longer open. |
| [#108372](https://github.com/openclaw/openclaw/pull/108372) | Closed in local gitcrawl | fix(agents): surface claude-cli logged-out sessions as actionable re-auth errors; no longer open. |
| [#108369](https://github.com/openclaw/openclaw/pull/108369) | Closed in local gitcrawl | fix(doctor): pass collectModelsMap for agents.list model ref scan; no longer open. |
| [#108360](https://github.com/openclaw/openclaw/pull/108360) | Closed in local gitcrawl | fix(agents,cron): remove pattern field from model-facing cron tool schema; no longer open. |
| [#108327](https://github.com/openclaw/openclaw/pull/108327) | Closed in local gitcrawl | fix(retry): recognize provider-wrapped 5xx status codes for session retry (fixes #106824); no longer open. |
| [#108310](https://github.com/openclaw/openclaw/pull/108310) | Closed in local gitcrawl | fix(plugin-sdk): drop unreachable openai tool-compat branch; no longer open. |
| [#108272](https://github.com/openclaw/openclaw/pull/108272) | Closed in local gitcrawl | fix(sessions): snapshot last-call context, not aggregate cacheRead (#108238); no longer open. |
| [#108267](https://github.com/openclaw/openclaw/pull/108267) | Closed in local gitcrawl | fix(media): propagate SSRF policy to provider poll and download sub-requests; no longer open. |
| [#108261](https://github.com/openclaw/openclaw/pull/108261) | Closed in local gitcrawl | chore(plugins): gate deprecation hygiene in CI and purge internal deprecated usage; no longer open. |
| [#108260](https://github.com/openclaw/openclaw/pull/108260) | Closed in local gitcrawl | refactor(agents): privatize auth test seams; no longer open. |
| [#108255](https://github.com/openclaw/openclaw/issues/108255) | Closed in local gitcrawl | runtime.llm.complete cannot pass a reasoning effort, and the omitted field can hard-fail reasoning-mandatory models; no longer open. |
| [#108254](https://github.com/openclaw/openclaw/pull/108254) | Closed in local gitcrawl | fix(codex): model-scoped usage-limit blocks, structural 429 classification, no silent API-key billing; no longer open. |
| [#108232](https://github.com/openclaw/openclaw/pull/108232) | Closed in local gitcrawl | fix(cron): close C4 re-arm gap in agent watchdog timer; no longer open. |
| [#108188](https://github.com/openclaw/openclaw/pull/108188) | Closed in local gitcrawl | fix(agents,cron): remove pattern field from model-facing cron tool schema; no longer open. |
| [#108152](https://github.com/openclaw/openclaw/issues/108152) | Closed in local gitcrawl | [Bug]: direct anthropic-messages claude-opus-4-7 / opus-4-6 / sonnet-4-6 capped at 200k on 2026.6.10 despite ANTHROPIC_GA_1M_MODEL_PREFIXES listing them (stale plugin manifest, no user-side workaround); no longer open. |
| [#108144](https://github.com/openclaw/openclaw/pull/108144) | Closed in local gitcrawl | fix(cron): remove llama.cpp-incompatible regex pattern from declarationKey schema; no longer open. |
| [#108126](https://github.com/openclaw/openclaw/pull/108126) | Closed in local gitcrawl | fix(retry): detect provider-wrapped 5xx status codes for session retry; no longer open. |
| [#108124](https://github.com/openclaw/openclaw/pull/108124) | Closed in local gitcrawl | fix(doctor): force refresh when accepting the expiring OAuth repair (#108098); no longer open. |
| [#108123](https://github.com/openclaw/openclaw/pull/108123) | Closed in local gitcrawl | fix: clear stale task and OAuth doctor warnings; no longer open. |
| [#108098](https://github.com/openclaw/openclaw/issues/108098) | Closed in local gitcrawl | [Bug]: Doctor OAuth refresh repair can leave expiring warnings unchanged; no longer open. |
| [#108086](https://github.com/openclaw/openclaw/pull/108086) | Closed in local gitcrawl | fix(openai): safe error serialization in stream error handler; no longer open. |
| [#108043](https://github.com/openclaw/openclaw/pull/108043) | Closed in local gitcrawl 2026-07-15 | feat(active-memory): add recall-specific fast mode; no longer open. |
| [#108015](https://github.com/openclaw/openclaw/pull/108015) | Closed in local gitcrawl | fix(release): retry transient live provider failures; no longer open. |
| [#108010](https://github.com/openclaw/openclaw/pull/108010) | Closed in local gitcrawl | fix(ci): avoid unbound agent failover callbacks; no longer open. |
| [#107985](https://github.com/openclaw/openclaw/pull/107985) | Closed in local gitcrawl | refactor(auto-reply): split agent runner execution; no longer open. |
| [#107979](https://github.com/openclaw/openclaw/pull/107979) | Closed in local gitcrawl | fix(codex): keep selectable models in the OpenAI namespace; no longer open. |
| [#107939](https://github.com/openclaw/openclaw/pull/107939) | Closed in local gitcrawl | fix(cron): anchor regex patterns with ^...$ for llama.cpp JSON Schema compatibility; no longer open. |
| [#107922](https://github.com/openclaw/openclaw/issues/107922) | Closed in local gitcrawl | Isolated cron job payload.model override leaks back to parent/main session model; no longer open. |
| [#107916](https://github.com/openclaw/openclaw/issues/107916) | Closed in local gitcrawl | sessions.usage still re-parses actively-written session files on every call on 2026.6.10 (15-28s + ~1-2GB transient heap; lineage #82773/#87894); no longer open. |
| [#107914](https://github.com/openclaw/openclaw/issues/107914) | Closed in local gitcrawl | No user-facing notification when an agent run is aborted (timeout / stuck-session / cancel); no longer open. |
| [#107877](https://github.com/openclaw/openclaw/pull/107877) | Closed in local gitcrawl | feat(active-memory): add recall-specific fast mode; no longer open. |
| [#107831](https://github.com/openclaw/openclaw/pull/107831) | Closed in local gitcrawl | fix(providers): add itemId check to message snapshot collapse; no longer open. |
| [#107829](https://github.com/openclaw/openclaw/pull/107829) | Closed in local gitcrawl | fix(doctor): skip embedding-provider check when memorySearch.provider is "none" (#107736); no longer open. |
| [#107827](https://github.com/openclaw/openclaw/pull/107827) | Closed in local gitcrawl | test(memory): model qmd child stream encoding; no longer open. |
| [#107815](https://github.com/openclaw/openclaw/issues/107815) | Closed in local gitcrawl | [Bug]: memory-core dreaming narrative fails with "no low surrogate in string" API 400 — clampDiaryContextEntry truncates mid-surrogate-pair (fix on main, missing from v2026.7.1); no longer open. |
| [#107791](https://github.com/openclaw/openclaw/pull/107791) | Closed in local gitcrawl | fix: OpenAI OAuth models fail on cloud workers; no longer open. |
| [#107778](https://github.com/openclaw/openclaw/pull/107778) | Closed in local gitcrawl | fix(doctor): accept memory provider none without api key; no longer open. |
| [#107754](https://github.com/openclaw/openclaw/pull/107754) | Closed in local gitcrawl | fix(channels): prevent base URL credentials in status output; no longer open. |
| [#107743](https://github.com/openclaw/openclaw/issues/107743) | Closed in local gitcrawl | v2026.7.1: `models list` crashes in applyAnthropicSonnet5Cost (TypeError: reading 'input') with multi-provider configured catalog; no longer open. |
| [#107740](https://github.com/openclaw/openclaw/pull/107740) | Closed in local gitcrawl | test(memory): model qmd child stream encoding; no longer open. |
| [#107738](https://github.com/openclaw/openclaw/pull/107738) | Closed in local gitcrawl | test: isolate live model switch suite; no longer open. |
| [#107723](https://github.com/openclaw/openclaw/pull/107723) | Closed in local gitcrawl | test: preload provider auth parity plugins; no longer open. |
| [#107650](https://github.com/openclaw/openclaw/pull/107650) | Closed in local gitcrawl | fix(ollama): preserve caller AbortSignal alongside request timeout; no longer open. |
| [#107646](https://github.com/openclaw/openclaw/pull/107646) | Closed in local gitcrawl | refactor(agents): split embedded runner model setup; no longer open. |
| [#107630](https://github.com/openclaw/openclaw/pull/107630) | Closed in local gitcrawl | fix(session): persist fresh usage snapshot instead of stale totalTokens fallback; no longer open. |
| [#107619](https://github.com/openclaw/openclaw/pull/107619) | Closed in local gitcrawl | fix(memory): reject hex/exponent dreaming integer config strings; no longer open. |
| [#107605](https://github.com/openclaw/openclaw/pull/107605) | Closed in local gitcrawl | fix(agents,cron): remove pattern field from JSON Schema string constraints; no longer open. |
| [#107510](https://github.com/openclaw/openclaw/issues/107510) | Closed in local gitcrawl | [Bug] Deadlock during concurrent auth validation in OpenAI Codex integrations; no longer open. |
| [#107468](https://github.com/openclaw/openclaw/pull/107468) | Closed in local gitcrawl | fix(agents,cron): remove pattern field from JSON Schema string constraints; no longer open. |
| [#107465](https://github.com/openclaw/openclaw/pull/107465) | Closed in local gitcrawl | fix: anchor JSON Schema patterns for llama.cpp HTTP server compatibility; no longer open. |
| [#107454](https://github.com/openclaw/openclaw/pull/107454) | Closed in local gitcrawl | fix(usage): stop provider usage hangs after response headers; no longer open. |
| [#107453](https://github.com/openclaw/openclaw/pull/107453) | Closed in local gitcrawl | docs: add llama.cpp HTTP server setup guide; no longer open. |
| [#107449](https://github.com/openclaw/openclaw/issues/107449) | Closed in local gitcrawl | [Bug]: cron tool JSON Schema is incompatible with llama.cpp tool parser (pattern: "\S"); no longer open. |
| [#107381](https://github.com/openclaw/openclaw/pull/107381) | Closed in local gitcrawl | refactor(memory): split QMD manager responsibilities; no longer open. |
| [#107333](https://github.com/openclaw/openclaw/issues/107333) | Closed in local gitcrawl | [Bug]: OpenClaw 2026.6.11: The streaming SSE consumer does not parse the trailing usage chunk, and model usage is completely uncaptured.; no longer open. |
| [#107325](https://github.com/openclaw/openclaw/pull/107325) | Closed in local gitcrawl | fix(agents): guard null response body in proxy stream reader; no longer open. |
| [#107304](https://github.com/openclaw/openclaw/pull/107304) | Closed in local gitcrawl | fix(zai): Coding Plan chat turns always fail with fake rate-limit when system prompt carries OpenClaw signature line; no longer open. |
| [#107303](https://github.com/openclaw/openclaw/issues/107303) | Closed in local gitcrawl | [Bug]: Codex app-server intermittently produces no model events for 120s, then profile cooldown causes cascading fallbacks; no longer open. |
| [#107276](https://github.com/openclaw/openclaw/pull/107276) | Closed in local gitcrawl | fix(memory-core): preserve canonical embedding cache on migration; no longer open. |
| [#107263](https://github.com/openclaw/openclaw/pull/107263) | Closed in local gitcrawl | fix(memory): preserve UTF-8 when qmd output splits across pipe chunks; no longer open. |
| [#107262](https://github.com/openclaw/openclaw/issues/107262) | Closed in local gitcrawl | [Bug]: Codex quota recovery/reset credits do not re-probe long WHAM cooldowns when fallbacks exist; no longer open. |
| [#107256](https://github.com/openclaw/openclaw/pull/107256) | Closed in local gitcrawl | fix(oauth): align getOAuthApiKey expiry check with auth manager refresh margin; no longer open. |
| [#107250](https://github.com/openclaw/openclaw/pull/107250) | Closed in local gitcrawl | feat: add aionly provider plugin and wire contract tests; no longer open. |
| [#107243](https://github.com/openclaw/openclaw/pull/107243) | Closed in local gitcrawl | fix(memory-core): preserve canonical cache rows during legacy migration; no longer open. |
| [#107167](https://github.com/openclaw/openclaw/pull/107167) | Closed in local gitcrawl | test: isolate provider auth parity suite; no longer open. |
| [#107076](https://github.com/openclaw/openclaw/issues/107076) | Closed in local gitcrawl | [Bug] Dynamic tool list before CACHE_BOUNDARY breaks prefix caching for exact-match providers (GLM-5.2, DeepSeek); no longer open. |
| [#107058](https://github.com/openclaw/openclaw/pull/107058) | Closed in local gitcrawl | perf(plugins): reuse current snapshot in isPluginProvidersLoadInFlight to avoid repeated disk I/O; no longer open. |
| [#106986](https://github.com/openclaw/openclaw/pull/106986) | Closed in local gitcrawl | fix(diagnostics): prevent broken emoji in long model identifiers; no longer open. |
| [#106940](https://github.com/openclaw/openclaw/pull/106940) | Closed in local gitcrawl | fix(memory): hide QMD transport metadata from recalled content; no longer open. |
| [#106897](https://github.com/openclaw/openclaw/pull/106897) | Closed in local gitcrawl | fix(retry): recognize provider-wrapped transient 5xx for session retry; no longer open. |
| [#106851](https://github.com/openclaw/openclaw/pull/106851) | Closed in local gitcrawl | fix(retry): recognize provider-wrapped 5xx errors in retry classifier; no longer open. |
| [#106850](https://github.com/openclaw/openclaw/pull/106850) | Closed in local gitcrawl | fix: recognize provider-wrapped HTTP status for session retry; no longer open. |
| [#106840](https://github.com/openclaw/openclaw/pull/106840) | Closed in local gitcrawl | fix: active-memory recall fails with billing rejections on subscription-only Claude CLI setups; no longer open. |
| [#106839](https://github.com/openclaw/openclaw/issues/106839) | Closed in local gitcrawl | [BUG] Active-memory recall fails every turn with a billing rejection on subscription-only Claude CLI setups; no longer open. |
| [#106824](https://github.com/openclaw/openclaw/issues/106824) | Closed in local gitcrawl | retry: provider-wrapped 5xx errors skip session retry; no longer open. |
| [#106758](https://github.com/openclaw/openclaw/pull/106758) | Closed in local gitcrawl | fix(migrate): import current Hermes state and provider contracts; no longer open. |
| [#106754](https://github.com/openclaw/openclaw/pull/106754) | Closed in local gitcrawl | fix: keep unresolved API-key providers visible; no longer open. |
| [#106747](https://github.com/openclaw/openclaw/issues/106747) | Closed in local gitcrawl | refactor(amazon-bedrock): use exact AWS SDK contracts; no longer open. |
| [#106539](https://github.com/openclaw/openclaw/pull/106539) | Closed in local gitcrawl | refactor(active-memory): split recall helpers; no longer open. |
| [#106500](https://github.com/openclaw/openclaw/pull/106500) | Closed in local gitcrawl | feat(codex): show the account email with app-server usage windows; no longer open. |
| [#106467](https://github.com/openclaw/openclaw/issues/106467) | Closed in local gitcrawl | [Bug]: openai/gpt-5.6-terra routes to API-key Responses instead of Codex OAuth; no longer open. |
| [#106448](https://github.com/openclaw/openclaw/issues/106448) | Closed in local gitcrawl | Display Bug: non-multimodal models get "(see attached image)" instead of tool output when image blocks lack data payload; no longer open. |
| [#106421](https://github.com/openclaw/openclaw/pull/106421) | Closed in local gitcrawl | fix(usage): ignore invalid Z.ai reset timestamps; no longer open. |
| [#106375](https://github.com/openclaw/openclaw/issues/106375) | Closed in local gitcrawl | [Bug]: Native Codex subagents silently fall back from ChatGPT OAuth to API-key billing; no longer open. |
| [#106360](https://github.com/openclaw/openclaw/issues/106360) | Closed in local gitcrawl | Hermes importer misses current state and provider contracts; no longer open. |
| [#106338](https://github.com/openclaw/openclaw/pull/106338) | Closed in local gitcrawl | fix(model-catalog): keep profile-specific model rows distinct; no longer open. |
| [#106285](https://github.com/openclaw/openclaw/pull/106285) | Closed in local gitcrawl | refactor(active-memory): split runtime modules; no longer open. |
| [#106271](https://github.com/openclaw/openclaw/pull/106271) | Closed in local gitcrawl | fix(model-catalog): keep profile-specific model rows distinct; no longer open. |
| [#106235](https://github.com/openclaw/openclaw/pull/106235) | Closed in local gitcrawl | fix(usage-bar): add webchat surface with block scale to prevent Braille character leak; no longer open. |
| [#106226](https://github.com/openclaw/openclaw/pull/106226) | Closed in local gitcrawl | fix(status): show Codex usage/quota in /status when runtime resolves to auto/default; no longer open. |
| [#106200](https://github.com/openclaw/openclaw/pull/106200) | Closed in local gitcrawl | feat(usage): show the account email with plan windows in the chat context popover; no longer open. |
| [#106198](https://github.com/openclaw/openclaw/pull/106198) | Closed in local gitcrawl | fix: restore GitHub Copilot turns and account context limits; no longer open. |
| [#106173](https://github.com/openclaw/openclaw/pull/106173) | Closed in local gitcrawl | fix(memory-core): clear pending-update wait timer after update settles; no longer open. |
| [#106170](https://github.com/openclaw/openclaw/issues/106170) | Closed in local gitcrawl | [Bug]: GitHub Copilot turns fail after runtime auth and use stale model limits; no longer open. |
| [#106163](https://github.com/openclaw/openclaw/pull/106163) | Closed in local gitcrawl | fix(agents): use fetchWithSsrFGuard in minimax-vlm.ts instead of raw fetch; no longer open. |
| [#106051](https://github.com/openclaw/openclaw/pull/106051) | Closed in local gitcrawl | refactor: move usage cost cache into agent database; no longer open. |
| [#105997](https://github.com/openclaw/openclaw/pull/105997) | Closed in local gitcrawl | fix(agents): route unbound OAuth compaction through auth-aware harness selection; no longer open. |
| [#105873](https://github.com/openclaw/openclaw/issues/105873) | Closed in local gitcrawl | [Bug]: # Bug Report: Tool output becomes image after workboard operations (minimax + deepseek observed separately); no longer open. |
| [#105835](https://github.com/openclaw/openclaw/pull/105835) | Closed in local gitcrawl | fix: inherit provider-level contextWindow/maxTokens when applying model defaults; no longer open. |
| [#105821](https://github.com/openclaw/openclaw/issues/105821) | Closed in local gitcrawl | config: provider-level contextTokens default is not propagated to models; no longer open. |
| [#105820](https://github.com/openclaw/openclaw/issues/105820) | Closed in local gitcrawl | config: provider-level contextTokens default is not propagated to models; no longer open. |
| [#105815](https://github.com/openclaw/openclaw/pull/105815) | Closed in local gitcrawl | refactor(agents): trim embedded helper dead exports; no longer open. |
| [#105746](https://github.com/openclaw/openclaw/pull/105746) | Closed in local gitcrawl | fix(release): unblock Discord and Kimi beta publication; no longer open. |
| [#105720](https://github.com/openclaw/openclaw/pull/105720) | Closed in local gitcrawl | refactor(ai): trim private Responses exports; no longer open. |
| [#105584](https://github.com/openclaw/openclaw/pull/105584) | Closed in local gitcrawl | fix(github-copilot): reject unsupported OAuth enterprise domain before refresh and model routing; no longer open. |
| [#105561](https://github.com/openclaw/openclaw/issues/105561) | Closed in local gitcrawl | [Bug]: Codex model catalog returns codex/* while canonical config and execution use openai/*; no longer open. |
| [#105552](https://github.com/openclaw/openclaw/pull/105552) | Closed in local gitcrawl | improve(agents): reduce warm model resolution latency; no longer open. |
| [#105548](https://github.com/openclaw/openclaw/pull/105548) | Closed in local gitcrawl | fix(memory): bound unsignaled remote HTTP with default timeoutMs; no longer open. |
| [#105543](https://github.com/openclaw/openclaw/issues/105543) | Closed in local gitcrawl | [Bug]: Warm Gateway turns rescan plugin manifests during model resolution; no longer open. |
| [#105539](https://github.com/openclaw/openclaw/pull/105539) | Closed in local gitcrawl | fix(openai): preserve authored openai-completions through provider normalization; no longer open. |
| [#105519](https://github.com/openclaw/openclaw/pull/105519) | Closed in local gitcrawl | fix(ai): clean up abort listener after provider retry sleep; no longer open. |
| [#105518](https://github.com/openclaw/openclaw/pull/105518) | Closed in local gitcrawl | fix(openai): preserve image routing before catalog load; no longer open. |
| [#105507](https://github.com/openclaw/openclaw/pull/105507) | Closed in local gitcrawl | fix(openai): allow omitted image model catalog; no longer open. |
| [#105488](https://github.com/openclaw/openclaw/pull/105488) | Closed in local gitcrawl | fix(qa): keep mock memory embeddings offline; no longer open. |
| [#105448](https://github.com/openclaw/openclaw/pull/105448) | Closed in local gitcrawl | fix: OpenRouter OAuth denial redirects show provider errors; no longer open. |
| [#105447](https://github.com/openclaw/openclaw/issues/105447) | Closed in local gitcrawl | OpenRouter OAuth pasted denial redirects report missing code; no longer open. |
| [#105445](https://github.com/openclaw/openclaw/issues/105445) | Closed in local gitcrawl | [Bug]: gpt-5.6-luna is listed but OpenAI Codex Responses returns 404; no longer open. |
| [#105419](https://github.com/openclaw/openclaw/issues/105419) | Closed in local gitcrawl | [Bug]: QMD session exporter writes "(empty)" exports for reset session artifacts (*.jsonl.reset.*) — follow-up to #30220: files are now listed, but content extraction yields nothing; no longer open. |
| [#105391](https://github.com/openclaw/openclaw/pull/105391) | Closed in local gitcrawl | Fix/elevenlabs reject malformed base url; no longer open. |
| [#105334](https://github.com/openclaw/openclaw/pull/105334) | Closed in local gitcrawl | fix(deepgram): validate realtime base URL overrides, preserving ws(s):// endpoints; no longer open. |
| [#105303](https://github.com/openclaw/openclaw/pull/105303) | Closed in local gitcrawl | fix(memory): repair SQLite prerelease fixtures; no longer open. |
| [#105295](https://github.com/openclaw/openclaw/pull/105295) | Closed in local gitcrawl | fix(bedrock-mantle): isolate discovery cache by credential; no longer open. |
| [#105256](https://github.com/openclaw/openclaw/pull/105256) | Closed in local gitcrawl | test(openai): align prerelease contracts; no longer open. |
| [#105255](https://github.com/openclaw/openclaw/pull/105255) | Closed in local gitcrawl | fix(active-memory): restore SQLite recall sessions; no longer open. |
| [#105207](https://github.com/openclaw/openclaw/issues/105207) | Closed in local gitcrawl | [Bug]: Agent turns rematerialize the same auth route twice; no longer open. |
| [#105184](https://github.com/openclaw/openclaw/issues/105184) | Closed in local gitcrawl | [Bug]: /status drops Codex usage/quota line for codex app-server sessions when runtime falls back to OpenClaw Default; no longer open. |
| [#105163](https://github.com/openclaw/openclaw/pull/105163) | Closed in local gitcrawl | fix(elevenlabs): fall back to default base URL when config value is malformed; no longer open. |
| [#105161](https://github.com/openclaw/openclaw/pull/105161) | Closed in local gitcrawl | fix(memory-wiki): honor memory_search deadline during wiki exhaustive scan; no longer open. |
| [#105110](https://github.com/openclaw/openclaw/issues/105110) | Closed in local gitcrawl | [Bug]: Plugin source-transform fallback retries native ESM loading; no longer open. |
| [#105057](https://github.com/openclaw/openclaw/pull/105057) | Closed in local gitcrawl | feat(agents): sessions_search tool for full-text recall over past session transcripts; no longer open. |
| [#105050](https://github.com/openclaw/openclaw/pull/105050) | Closed in local gitcrawl | test(agents): keep model discovery assertions hermetic against bundled plugin runtime; no longer open. |
| [#105035](https://github.com/openclaw/openclaw/issues/105035) | Closed in local gitcrawl | [Bug]: openai plugin normalization overrides authored openai-completions api when plugin runtime is active; no longer open. |
| [#104995](https://github.com/openclaw/openclaw/pull/104995) | Closed in local gitcrawl | fix(tests): relocate provider auth-literal parity test outside core source; no longer open. |
| [#104986](https://github.com/openclaw/openclaw/pull/104986) | Closed in local gitcrawl | fix(google): anchor model-ID regexes to prevent false-positive substring matches; no longer open. |
| [#104977](https://github.com/openclaw/openclaw/issues/104977) | Closed in local gitcrawl | oauth: per-session ModelRegistry.refresh clears the process-global OAuth provider registry, wiping other live sessions' providers; no longer open. |
| [#104974](https://github.com/openclaw/openclaw/pull/104974) | Closed in local gitcrawl | test: move provider auth parity coverage out of core source; no longer open. |
| [#104886](https://github.com/openclaw/openclaw/pull/104886) | Closed in local gitcrawl | fix(core): converge model-API ownership, provider auth-literal parity, and structured failover classification; no longer open. |
| [#104841](https://github.com/openclaw/openclaw/pull/104841) | Closed in local gitcrawl | fix(amazon-bedrock): add timeouts to model discovery requests; no longer open. |
| [#104835](https://github.com/openclaw/openclaw/pull/104835) | Closed in local gitcrawl | fix(openrouter): apply request policy to music generation requests; no longer open. |
| [#104825](https://github.com/openclaw/openclaw/pull/104825) | Closed in local gitcrawl | fix(memory-core): guard direct wiki reads and share supplement registry; no longer open. |
| [#104806](https://github.com/openclaw/openclaw/issues/104806) | Closed in local gitcrawl | Beta blocker: codex - subagent completion announce never runs for codex-runtime parent sessions; no longer open. |
| [#104793](https://github.com/openclaw/openclaw/pull/104793) | Closed in local gitcrawl | fix(memory-wiki): propagate deadline signal and skip exhaustive fallback for supplement search; no longer open. |
| [#104779](https://github.com/openclaw/openclaw/issues/104779) | Closed in local gitcrawl | OpenAI simple-completion (utility model) pairs api_key auth with the ChatGPT-backend Codex transport — narration/titles 401; no longer open. |
| [#104778](https://github.com/openclaw/openclaw/pull/104778) | Closed in local gitcrawl | fix(zai): honor max thinking through gateway; no longer open. |
| [#104770](https://github.com/openclaw/openclaw/pull/104770) | Closed in local gitcrawl | fix(agents): surface utility-model narration failures and show the utility model in models status; no longer open. |
| [#104764](https://github.com/openclaw/openclaw/issues/104764) | Closed in local gitcrawl | Utility-model narration fails silently on dead API-key profiles; models status hides the utility model; no longer open. |
| [#104759](https://github.com/openclaw/openclaw/pull/104759) | Closed in local gitcrawl | fix(google): exclude versioned Gemini client header from memory identity; no longer open. |
| [#104741](https://github.com/openclaw/openclaw/pull/104741) | Closed in local gitcrawl 2026-07-11 | fix(memory): isolate local embedding services across runtimes; no longer open. |
| [#104734](https://github.com/openclaw/openclaw/pull/104734) | Closed in local gitcrawl | fix(models): redact synthetic auth credentials from models status --json; no longer open. |
| [#104720](https://github.com/openclaw/openclaw/issues/104720) | Closed in local gitcrawl | [Bug]: Gemini x-goog-api-client version invalidates compatible memory indexes; no longer open. |
| [#104716](https://github.com/openclaw/openclaw/issues/104716) | Closed in local gitcrawl | [Bug]: Gateway ignores Z.AI GLM-5.2 max thinking profile while local infer succeeds; no longer open. |
| [#104714](https://github.com/openclaw/openclaw/pull/104714) | Closed in local gitcrawl | fix(providers): complete repaired tool call streams; no longer open. |
| [#104713](https://github.com/openclaw/openclaw/issues/104713) | Closed in local gitcrawl | [Beta 2026.7.1-beta.5] models status --json can expose raw credential material; no longer open. |
| [#104704](https://github.com/openclaw/openclaw/issues/104704) | Closed in local gitcrawl | [Bug]: Telegram /login codex can keep a new OpenAI account under the old auth profile id; no longer open. |
| [#104685](https://github.com/openclaw/openclaw/pull/104685) | Closed in local gitcrawl | fix(openai): align auth availability with effective routes; no longer open. |
| [#104684](https://github.com/openclaw/openclaw/pull/104684) | Closed in local gitcrawl | fix(release/2026.7.1): low-risk stable sweep — pairing authz, UTF-16 chunk safety, channel timeouts; no longer open. |
| [#104635](https://github.com/openclaw/openclaw/pull/104635) | Closed in local gitcrawl | fix(discord): refresh model picker after default changes; no longer open. |
| [#104614](https://github.com/openclaw/openclaw/issues/104614) | Closed in local gitcrawl | [Bug]: Discord /model picker shows stale model after hot-reloaded default switch; no longer open. |
| [#104592](https://github.com/openclaw/openclaw/pull/104592) | Closed in local gitcrawl | fix(clawrouter): guard usage snapshot fetch against SSRF redirects; no longer open. |
| [#104547](https://github.com/openclaw/openclaw/pull/104547) | Closed in local gitcrawl | fix(agents): protect provider auth exchange output by sensitivity, not input marker; no longer open. |
| [#104546](https://github.com/openclaw/openclaw/pull/104546) | Closed in local gitcrawl | fix(gateway): classify chat error kind via canonical failover reasons; no longer open. |
| [#104502](https://github.com/openclaw/openclaw/pull/104502) | Closed in local gitcrawl | feat(onboarding): add provider sign-in; no longer open. |
| [#104487](https://github.com/openclaw/openclaw/pull/104487) | Closed in local gitcrawl | fix(agents): keep failover detail truncation UTF-16 safe; no longer open. |
| [#104465](https://github.com/openclaw/openclaw/pull/104465) | Closed in local gitcrawl | feat(cloud-workers): add crabbox worker provider plugin and profile-aware lease lifecycle; no longer open. |
| [#104433](https://github.com/openclaw/openclaw/pull/104433) | Closed in local gitcrawl | fix(openrouter): Fusion prompt corrupts boundary emoji in model IDs; no longer open. |
| [#104401](https://github.com/openclaw/openclaw/pull/104401) | Closed in local gitcrawl | feat(gateway): durable cloud worker environments, provider SDK contract, and lifecycle RPCs; no longer open. |
| [#104395](https://github.com/openclaw/openclaw/pull/104395) | Closed in local gitcrawl | fix(agents): escalate Codex usage-limit prompt errors to model fallback; no longer open. |
| [#104310](https://github.com/openclaw/openclaw/pull/104310) | Closed in local gitcrawl | feat(memory): expose llama.cpp runtime diagnostics; no longer open. |
| [#104309](https://github.com/openclaw/openclaw/issues/104309) | Closed in local gitcrawl | Expose llama.cpp runtime diagnostics and context-aware GPU offload; no longer open. |
| [#104294](https://github.com/openclaw/openclaw/issues/104294) | Closed in local gitcrawl | [Feature]: Cloud workers — run agent sessions on ephemeral SSH-reachable machines; no longer open. |
| [#104248](https://github.com/openclaw/openclaw/pull/104248) | Closed in local gitcrawl | fix(agents): respect provider default thinking level over global thinkingDefault; no longer open. |
| [#104233](https://github.com/openclaw/openclaw/pull/104233) | Closed in local gitcrawl | fix(ci): register local-audio-acceleration doctor contribution and wrap overlong MLX log line; no longer open. |
| [#104231](https://github.com/openclaw/openclaw/issues/104231) | Closed in local gitcrawl | test harness: changed-run routing skips active-memory tests; unit lane double-runs gateway packages; forceRerunTriggers drift; orphan configs; no longer open. |
| [#104214](https://github.com/openclaw/openclaw/issues/104214) | Closed in local gitcrawl | [Feature]: Start configured local services for embedding requests; no longer open. |
| [#104200](https://github.com/openclaw/openclaw/pull/104200) | Closed in local gitcrawl | feat(macos): keep MLX TTS model resident; no longer open. |
| [#104197](https://github.com/openclaw/openclaw/issues/104197) | Closed in local gitcrawl | [Feature]: Keep macOS MLX TTS model resident; no longer open. |
| [#104196](https://github.com/openclaw/openclaw/pull/104196) | Closed in local gitcrawl | fix(cron): keep memory search available with agent overrides; no longer open. |
| [#104194](https://github.com/openclaw/openclaw/issues/104194) | Closed in local gitcrawl | [Bug]: Isolated cron drops global memorySearch settings for partial agent overrides; no longer open. |
| [#104133](https://github.com/openclaw/openclaw/pull/104133) | Closed in local gitcrawl | fix(memory-core): defer dreaming sweep when main session has active runs; no longer open. |
| [#104085](https://github.com/openclaw/openclaw/pull/104085) | Closed in local gitcrawl | fix(dreaming): drop heartbeat assistant responses from dream corpus; no longer open. |
| [#104070](https://github.com/openclaw/openclaw/pull/104070) | Closed in local gitcrawl | fix(agents): prevent local provider sidecars surviving canceled startup; no longer open. |
| [#103998](https://github.com/openclaw/openclaw/pull/103998) | Closed in local gitcrawl | fix(cli): avoid zero usage cost during cache refresh; no longer open. |
| [#103996](https://github.com/openclaw/openclaw/pull/103996) | Closed in local gitcrawl | fix(memory): preserve Unicode in QMD search snippets; no longer open. |
| [#103988](https://github.com/openclaw/openclaw/pull/103988) | Closed in local gitcrawl | fix(auth): refresh OAuth tokens inside pre-expiry margin; no longer open. |
| [#103974](https://github.com/openclaw/openclaw/pull/103974) | Closed in local gitcrawl | fix(llm): share one rate-limit window policy across session and failover retries (alt to #103200); no longer open. |
| [#103933](https://github.com/openclaw/openclaw/pull/103933) | Closed in local gitcrawl | fix(memory-core): keep same-agent session hits in memory recall under tree visibility (#103732); no longer open. |
| [#103901](https://github.com/openclaw/openclaw/pull/103901) | Closed in local gitcrawl | fix(agents): CJK-aware tool-result truncation budget allocation (#103847); no longer open. |
| [#103882](https://github.com/openclaw/openclaw/issues/103882) | Closed in local gitcrawl | gateway usage-cost --all-agents returns $0 (per-agent query works); no longer open. |
| [#103868](https://github.com/openclaw/openclaw/pull/103868) | Closed in local gitcrawl | fix(codex): trigger model fallback on usage-limit promptError (#103734); no longer open. |
| [#103850](https://github.com/openclaw/openclaw/issues/103850) | Closed in local gitcrawl | Feature: Add per-model RPM/TPM rate limiting to prevent 429 errors; no longer open. |
| [#103829](https://github.com/openclaw/openclaw/pull/103829) | Closed in local gitcrawl | fix(agents): surface claude-cli logged-out failures as actionable re-auth errors (#103773); no longer open. |
| [#103813](https://github.com/openclaw/openclaw/pull/103813) | Closed in local gitcrawl | fix(memory-host): keep redacted token hints UTF-16 safe; no longer open. |
| [#103799](https://github.com/openclaw/openclaw/pull/103799) | Closed in local gitcrawl | fix(memory-lancedb): gate auto-recall/auto-capture on per-agent memorySearch.enabled (#103590); no longer open. |
| [#103771](https://github.com/openclaw/openclaw/pull/103771) | Closed in local gitcrawl | fix(memory): filter heartbeat acks robustly in dreaming ingestion (#1…; no longer open. |
| [#103769](https://github.com/openclaw/openclaw/pull/103769) | Closed in local gitcrawl | feat(agents): derive a provider-declared default utility model when unset; no longer open. |
| [#103767](https://github.com/openclaw/openclaw/pull/103767) | Closed in local gitcrawl | fix(apple): prevent stale thinking after model switches and reconnects; no longer open. |
| [#103766](https://github.com/openclaw/openclaw/issues/103766) | Closed in local gitcrawl | [Bug]: Apple chat can send stale or unsupported thinking levels after model switches and reconnects; no longer open. |
| [#103734](https://github.com/openclaw/openclaw/issues/103734) | Closed in local gitcrawl | Codex usage-limit surfaced as promptError, not thrown — model fallback never fires; no longer open. |
| [#103732](https://github.com/openclaw/openclaw/issues/103732) | Closed in local gitcrawl | memory_search tool returns 0 results for corpus=sessions, CLI works fine; no longer open. |
| [#103716](https://github.com/openclaw/openclaw/pull/103716) | Closed in local gitcrawl | feat(plugin-sdk): propose CLI backend auth-forwarding contract; no longer open. |
| [#103680](https://github.com/openclaw/openclaw/pull/103680) | Closed in local gitcrawl | fix(providers): align Meta Model API contract; no longer open. |
| [#103667](https://github.com/openclaw/openclaw/issues/103667) | Closed in local gitcrawl | Meta provider uses stale Model API endpoint and output limit; no longer open. |
| [#103652](https://github.com/openclaw/openclaw/issues/103652) | Closed in local gitcrawl | [Bug]: workflow dispatch omits focused live-provider jobs; no longer open. |
| [#103641](https://github.com/openclaw/openclaw/issues/103641) | Closed in local gitcrawl | QA reports need explicit usage applicability for non-assistant parity flows; no longer open. |
| [#103638](https://github.com/openclaw/openclaw/pull/103638) | Closed in local gitcrawl | fix(compaction): allow compaction under Bedrock aws-sdk auth with no static key; no longer open. |
| [#103637](https://github.com/openclaw/openclaw/issues/103637) | Closed in local gitcrawl | [Bug]: Compaction wedges every message under Bedrock aws-sdk auth (keyless SigV4); no longer open. |
| [#103636](https://github.com/openclaw/openclaw/issues/103636) | Closed in local gitcrawl | Backend loopback client loses operator scope when the relay forwards from the host's own interface IP (agent RPC fails: missing scope: operator.write); no longer open. |
| [#103628](https://github.com/openclaw/openclaw/pull/103628) | Closed in local gitcrawl | fix(agents): prevent transcript redaction from corrupting signed reasoning; no longer open. |
| [#103627](https://github.com/openclaw/openclaw/pull/103627) | Closed in local gitcrawl | fix(googlechat): add timeout to Google auth fetch requests; no longer open. |
| [#103592](https://github.com/openclaw/openclaw/pull/103592) | Closed in local gitcrawl | fix(model-selection): log warning when model is not in allowlist before falling back; no longer open. |
| [#103591](https://github.com/openclaw/openclaw/pull/103591) | Closed in local gitcrawl | fix: warn when model not in allowlist falls back to catalog default; no longer open. |
| [#103590](https://github.com/openclaw/openclaw/issues/103590) | Closed in local gitcrawl | memory-lancedb auto-recall ignores per-agent memorySearch.enabled, causing cross-agent memory leakage; no longer open. |
| [#103569](https://github.com/openclaw/openclaw/pull/103569) | Closed in local gitcrawl | fix(chutes): redact OAuth error response body; no longer open. |
| [#103566](https://github.com/openclaw/openclaw/pull/103566) | Closed in local gitcrawl | fix(memory): qmd search fails when logs prefix results; no longer open. |
| [#103533](https://github.com/openclaw/openclaw/issues/103533) | Closed in local gitcrawl | ClawRouter E2E races model-fetch stdout after a successful turn; no longer open. |
| [#103529](https://github.com/openclaw/openclaw/issues/103529) | Closed in local gitcrawl | [Bug]: z.ai Coding Plan returns 429/1305 deterministically when the system prompt contains OpenClaw's signature line — disguised as "overloaded", breaks all chat after successful onboarding; no longer open. |
| [#103510](https://github.com/openclaw/openclaw/pull/103510) | Closed in local gitcrawl | fix: preserve selected models through hot reloads and fallbacks; no longer open. |
| [#103488](https://github.com/openclaw/openclaw/pull/103488) | Closed in local gitcrawl | fix(xai): route provider alias to native endpoint; no longer open. |
| [#103482](https://github.com/openclaw/openclaw/pull/103482) | Closed in local gitcrawl | fix(ios): trim model names in model picker; no longer open. |
| [#103476](https://github.com/openclaw/openclaw/pull/103476) | Closed in local gitcrawl | feat: correlate managed agent turns with ClawRouter requests; no longer open. |
| [#103454](https://github.com/openclaw/openclaw/issues/103454) | Closed in local gitcrawl | [Bug]: x-ai provider alias fails Gateway startup; no longer open. |
| [#103417](https://github.com/openclaw/openclaw/pull/103417) | Closed in local gitcrawl | fix(agents): make model pins survive fallback, hot reloads, and stale auth profiles; no longer open. |
| [#103400](https://github.com/openclaw/openclaw/issues/103400) | Closed in local gitcrawl | Memory Wiki wiki_apply partially succeeds under concurrent agent writes; no longer open. |
| [#103375](https://github.com/openclaw/openclaw/pull/103375) | Closed in local gitcrawl | fix(opencode-go): remove deprecated mimo-v2-omni and mimo-v2-pro aliases; no longer open. |
| [#103329](https://github.com/openclaw/openclaw/pull/103329) | Closed in local gitcrawl | fix(opencode-go): remove deprecated mimo-v2-omni and mimo-v2-pro model aliases; no longer open. |
| [#103324](https://github.com/openclaw/openclaw/issues/103324) | Closed in local gitcrawl | [Bug]: Model fallback silently rewrites user session model pin; expired OAuth profile poisons availability probe; no longer open. |
| [#103322](https://github.com/openclaw/openclaw/pull/103322) | Closed in local gitcrawl | fix(opencode-go): stop listing rejected MiMo routes; no longer open. |
| [#103321](https://github.com/openclaw/openclaw/pull/103321) | Closed in local gitcrawl | fix(ci): restore DeepSeek live gateway coverage; no longer open. |
| [#103319](https://github.com/openclaw/openclaw/issues/103319) | Closed in local gitcrawl | [Bug]: DeepSeek release lane selects no native V4 models; no longer open. |
| [#103314](https://github.com/openclaw/openclaw/pull/103314) | Closed in local gitcrawl | fix(cron): diversify dead-provider auto-reassign instead of collapsing to one model; no longer open. |
| [#103311](https://github.com/openclaw/openclaw/issues/103311) | Closed in local gitcrawl | [Bug]: OpenCode Go exposes deprecated MiMo aliases that reject agent requests; no longer open. |
| [#103306](https://github.com/openclaw/openclaw/pull/103306) | Closed in local gitcrawl | fix(google): bound embedding batch file upload error body read; no longer open. |
| [#103298](https://github.com/openclaw/openclaw/issues/103298) | Closed in local gitcrawl | [Bug]: ClawRouter rejects baseUrl-only managed provider configuration; no longer open. |
| [#103296](https://github.com/openclaw/openclaw/pull/103296) | Closed in local gitcrawl | fix: claude-cli backend silently runs adaptive thinking at pinned medium effort; no longer open. |
| [#103269](https://github.com/openclaw/openclaw/pull/103269) | Closed in local gitcrawl | fix(oauth): redact Anthropic OAuth error response body and URL; no longer open. |
| [#103260](https://github.com/openclaw/openclaw/pull/103260) | Closed in local gitcrawl | fix(xai): align current model catalog and tools; no longer open. |
| [#103256](https://github.com/openclaw/openclaw/pull/103256) | Closed in local gitcrawl | fix(memory): normalize malformed batch failure attempts [AI-assisted]; no longer open. |
| [#103245](https://github.com/openclaw/openclaw/issues/103245) | Closed in local gitcrawl | `claude-cli` backend: `thinkingDefault: "adaptive"` is silently pinned to `--effort medium` — validation accepts adaptive, the spawn path flattens it; no longer open. |
| [#103242](https://github.com/openclaw/openclaw/issues/103242) | Closed in local gitcrawl | xAI catalog and server-tool defaults lag current models; no longer open. |
| [#103241](https://github.com/openclaw/openclaw/pull/103241) | Closed in local gitcrawl | fix(deepseek): align catalog costs and legacy aliases; no longer open. |
| [#103216](https://github.com/openclaw/openclaw/pull/103216) | Closed in local gitcrawl | fix(ai): honor Azure deployment maps with mixed-case model ids; no longer open. |
| [#103212](https://github.com/openclaw/openclaw/pull/103212) | Closed in local gitcrawl | fix(memory-core): use truncateUtf16Safe for dreaming narrative lead text; no longer open. |
| [#103204](https://github.com/openclaw/openclaw/pull/103204) | Closed in local gitcrawl | fix(test): restore OpenRouter and Fireworks live coverage; no longer open. |
| [#103197](https://github.com/openclaw/openclaw/pull/103197) | Closed in local gitcrawl | fix(opencode): list current Zen models in offline discovery; no longer open. |
| [#103196](https://github.com/openclaw/openclaw/pull/103196) | Closed in local gitcrawl | fix(memory-wiki): scope wiki_status bridgePublicArtifactCount to calling agent; no longer open. |
| [#103192](https://github.com/openclaw/openclaw/issues/103192) | Closed in local gitcrawl | [Bug]: DeepSeek catalog overstates V4 costs and mislabels legacy aliases; no longer open. |
| [#103189](https://github.com/openclaw/openclaw/issues/103189) | Closed in local gitcrawl | Release live gateway profiles can skip authenticated provider coverage; no longer open. |
| [#103184](https://github.com/openclaw/openclaw/issues/103184) | Closed in local gitcrawl | Beta blocker: opencode - refresh Zen static catalog; no longer open. |
| [#103150](https://github.com/openclaw/openclaw/issues/103150) | Closed in local gitcrawl | OpenAI auth availability diverges from effective model routing; no longer open. |
| [#103127](https://github.com/openclaw/openclaw/pull/103127) | Closed in local gitcrawl | improve(webchat): compact the model picker reasoning and speed rows; no longer open. |
| [#103116](https://github.com/openclaw/openclaw/pull/103116) | Closed in local gitcrawl | fix(active-memory): normalize legacy toggle timestamps; no longer open. |
| [#103114](https://github.com/openclaw/openclaw/pull/103114) | Closed in local gitcrawl | ci(release): retry transient MiniMax image failures; no longer open. |
| [#103112](https://github.com/openclaw/openclaw/pull/103112) | Closed in local gitcrawl | fix: preserve tools when local-model lean agents use provider overrides; no longer open. |
| [#103081](https://github.com/openclaw/openclaw/issues/103081) | Closed in local gitcrawl | `infer model run` leaves a persistent session + transcript on every invocation (unbounded growth); no longer open. |
| [#103078](https://github.com/openclaw/openclaw/issues/103078) | Closed in local gitcrawl | github-copilot: legacy OAuth token refresh sends bearer credential to unvalidated enterpriseUrl domain; no longer open. |
| [#103063](https://github.com/openclaw/openclaw/issues/103063) | Closed in local gitcrawl | [Bug]: diagnostics timeline omits provider request events; no longer open. |
| [#103051](https://github.com/openclaw/openclaw/pull/103051) | Closed in local gitcrawl | fix(models): preserve static provider catalog metadata; no longer open. |
| [#103038](https://github.com/openclaw/openclaw/pull/103038) | Closed in local gitcrawl | fix(auth-profiles): add AES-256-GCM encryption for persisted auth secrets; no longer open. |
| [#103026](https://github.com/openclaw/openclaw/issues/103026) | Closed in local gitcrawl | [Bug] Model generates natural language descriptions instead of shell commands, causing exec tool failures; no longer open. |
| [#103007](https://github.com/openclaw/openclaw/issues/103007) | Closed in local gitcrawl | Expose Dreaming promotion thresholds and light-phase lookback as user-configurable; no longer open. |
| [#103005](https://github.com/openclaw/openclaw/pull/103005) | Closed in local gitcrawl | fix(ai): cache and case-insensitively match Azure deployment map; no longer open. |
| [#102993](https://github.com/openclaw/openclaw/pull/102993) | Closed in local gitcrawl | fix(ai): match reasoning efforts case-insensitively without lowering provider values; no longer open. |
| [#102966](https://github.com/openclaw/openclaw/pull/102966) | Closed in local gitcrawl | feat(memory-lancedb): scope memory_recall and memory_forget + configurable thresholds; no longer open. |
| [#102964](https://github.com/openclaw/openclaw/issues/102964) | Closed in local gitcrawl | [Bug] Model registry schema requires cacheRead/cacheWrite but Ollama live discovery returns only input/output; no longer open. |
| [#102958](https://github.com/openclaw/openclaw/pull/102958) | Closed in local gitcrawl | fix(ai): fold case in OpenAI reasoning-effort matching (#102908); no longer open. |
| [#102940](https://github.com/openclaw/openclaw/pull/102940) | Closed in local gitcrawl | fix(active-memory): keep timeout partial replies valid at emoji caps; no longer open. |
| [#102890](https://github.com/openclaw/openclaw/pull/102890) | Closed in local gitcrawl | fix(llm-slug): use UTF-16-safe truncation for session content; no longer open. |
| [#102877](https://github.com/openclaw/openclaw/pull/102877) | Closed in local gitcrawl | fix(active-memory): recall context breaks when recent turns contain emoji; no longer open. |
| [#102871](https://github.com/openclaw/openclaw/pull/102871) | Closed in local gitcrawl | improve(webchat): model picker applies changes immediately, no Save/Discard row; no longer open. |
| [#102866](https://github.com/openclaw/openclaw/pull/102866) | Closed in local gitcrawl | fix(gateway): guard thinkingLevel re-validation against only relevant patch fields; no longer open. |
| [#102862](https://github.com/openclaw/openclaw/pull/102862) | Closed in local gitcrawl | fix(minimax): add timeouts to OAuth HTTP requests; no longer open. |
| [#102860](https://github.com/openclaw/openclaw/pull/102860) | Closed in local gitcrawl | fix(openai): add timeout to realtime client-secret requests; no longer open. |
| [#102854](https://github.com/openclaw/openclaw/issues/102854) | Closed in local gitcrawl | bundle-mcp tools not available in subagent sessions; no longer open. |
| [#102849](https://github.com/openclaw/openclaw/issues/102849) | Closed in local gitcrawl | [Bug]: EmbeddedAttemptSessionTakeoverError still occurs in active-memory plugin embedded sessions on 2026.6.10; no longer open. |
| [#102837](https://github.com/openclaw/openclaw/issues/102837) | Closed in local gitcrawl | voice-call: media-stream WebSocket accepts unauthenticated start frames for non-Twilio providers (plivo, telnyx); no longer open. |
| [#102819](https://github.com/openclaw/openclaw/pull/102819) | Closed in local gitcrawl | fix(models): align model list truncation by terminal width; no longer open. |
| [#102801](https://github.com/openclaw/openclaw/pull/102801) | Closed in local gitcrawl | fix(thinking): honor compat.supportedReasoningEfforts for custom models; no longer open. |
| [#102797](https://github.com/openclaw/openclaw/issues/102797) | Closed in local gitcrawl | [Bug]: Invalid `signature` in `thinking` block (replay_invalid) still occurring on 2026.6.11 — likely restart-during-generation / compaction path (edge case flagged in #40512); no longer open. |
| [#102791](https://github.com/openclaw/openclaw/pull/102791) | Closed in local gitcrawl | feat(providers): add Qwen 3.6 Flash and Gemini 3.1 Live; no longer open. |
| [#102784](https://github.com/openclaw/openclaw/pull/102784) | Closed in local gitcrawl | feat: show provider plan usage (5h/weekly/credits) in the chat context popover, keep API cost for API billing; no longer open. |
| [#102774](https://github.com/openclaw/openclaw/pull/102774) | Closed in local gitcrawl | fix(embedding-provider): use truncateUtf16Safe for text truncation; no longer open. |
| [#102771](https://github.com/openclaw/openclaw/issues/102771) | Closed in local gitcrawl | Chat context popover: show Anthropic plan usage (5h/weekly/credits) instead of meaningless cost on subscription billing; no longer open. |
| [#102767](https://github.com/openclaw/openclaw/pull/102767) | Closed in local gitcrawl | fix(memory-lancedb): use truncateUtf16Safe for sanitize text truncation; no longer open. |
| [#102751](https://github.com/openclaw/openclaw/issues/102751) | Closed in local gitcrawl | [Feature]: Add Qwen 3.6 Flash and current Gemini Live model; no longer open. |
| [#102744](https://github.com/openclaw/openclaw/pull/102744) | Closed in local gitcrawl | fix(plugins,media): keep embedding error and input file truncation surrogate-safe; no longer open. |
| [#102730](https://github.com/openclaw/openclaw/issues/102730) | Closed in local gitcrawl | [Feature Request]: Partner with Figma to get OpenClaw listed in Figma MCP Catalog; no longer open. |
| [#102724](https://github.com/openclaw/openclaw/pull/102724) | Closed in local gitcrawl | fix(memory-core): use truncateUtf16Safe for short-term promotion truncation; no longer open. |
| [#102662](https://github.com/openclaw/openclaw/pull/102662) | Closed in local gitcrawl | fix(fallback-state): use truncateUtf16Safe for fallback reason truncation; no longer open. |
| [#102657](https://github.com/openclaw/openclaw/pull/102657) | Closed in local gitcrawl | fix(auto-reply): use typed FailoverError.reason for rate_limit classification [AI-assisted]; no longer open. |
| [#102653](https://github.com/openclaw/openclaw/pull/102653) | Closed in local gitcrawl | fix(memory-core): keep promotion text truncation UTF-16 safe; no longer open. |
| [#102631](https://github.com/openclaw/openclaw/pull/102631) | Closed in local gitcrawl | fix(auto-reply): keep fallback reason truncation UTF-16 safe; no longer open. |
| [#102621](https://github.com/openclaw/openclaw/pull/102621) | Closed in local gitcrawl | fix(active-memory): use truncateUtf16Safe for log value and search query truncation; no longer open. |
| [#102610](https://github.com/openclaw/openclaw/pull/102610) | Closed in local gitcrawl | fix(agents): keep prompt history append-only mid-session for prompt-cache stability; no longer open. |
| [#102598](https://github.com/openclaw/openclaw/issues/102598) | Closed in local gitcrawl | Periodic usage-limit failures (weekly/monthly) are silently swallowed in group chats — user-copy path ignores typed FailoverError.reason; no longer open. |
| [#102593](https://github.com/openclaw/openclaw/pull/102593) | Closed in local gitcrawl | fix(ollama): use truncateUtf16Safe for malformed NDJSON log truncation; no longer open. |
| [#102589](https://github.com/openclaw/openclaw/pull/102589) | Closed in local gitcrawl | fix(memory-host-sdk): use truncateUtf16Safe for qmd stderr truncation; no longer open. |
| [#102571](https://github.com/openclaw/openclaw/pull/102571) | Closed in local gitcrawl | fix(mistral): keep error text truncation surrogate-safe; no longer open. |
| [#102563](https://github.com/openclaw/openclaw/pull/102563) | Closed in local gitcrawl | feat(cohere): add current Command models; no longer open. |
| [#102551](https://github.com/openclaw/openclaw/pull/102551) | Closed in local gitcrawl | fix(active-memory): use truncateUtf16Safe for log value truncation; no longer open. |
| [#102547](https://github.com/openclaw/openclaw/pull/102547) | Closed in local gitcrawl | fix(memory-host): use truncateUtf16Safe for QMD stderr context truncation; no longer open. |
| [#102542](https://github.com/openclaw/openclaw/pull/102542) | Closed in local gitcrawl | fix(agent-core,memory-core): keep compaction summary and memory snippet truncation UTF-16 safe; no longer open. |
| [#102539](https://github.com/openclaw/openclaw/pull/102539) | Closed in local gitcrawl | fix(mistral): use truncateUtf16Safe for error text truncation; no longer open. |
| [#102524](https://github.com/openclaw/openclaw/pull/102524) | Closed in local gitcrawl | fix(memory-core): use truncateUtf16Safe for diary context truncation; no longer open. |
| [#102479](https://github.com/openclaw/openclaw/pull/102479) | Closed in local gitcrawl | fix: transient failures no longer trigger false 12h OpenAI cooldown on expired access tokens; no longer open. |
| [#102471](https://github.com/openclaw/openclaw/issues/102471) | Closed in local gitcrawl | [Bug]: WHAM probe with expired access token puts refreshable OpenAI profile into false 12h cooldown; no longer open. |
| [#102461](https://github.com/openclaw/openclaw/pull/102461) | Closed in local gitcrawl | fix(openai): clarify rejected Realtime Talk API keys [AI]; no longer open. |
| [#102460](https://github.com/openclaw/openclaw/issues/102460) | Closed in local gitcrawl | [Feature]: Refresh direct provider catalogs for Qwen 3.7, North Mini Code, and Mistral Small 4; no longer open. |
| [#102451](https://github.com/openclaw/openclaw/pull/102451) | Closed in local gitcrawl | fix(memory-host): reject queued worker requests on shutdown; no longer open. |
| [#102375](https://github.com/openclaw/openclaw/pull/102375) | Closed in local gitcrawl | fix(llm): session auto-retry no longer retries permanent provider errors; no longer open. |
| [#102352](https://github.com/openclaw/openclaw/pull/102352) | Closed in local gitcrawl | fix(google): add regex anchors and prefix boundaries in google-shared model id checks; no longer open. |
| [#102344](https://github.com/openclaw/openclaw/pull/102344) | Closed in local gitcrawl | fix: surface OpenAI chat-completions refusal as assistant text; no longer open. |
| [#102305](https://github.com/openclaw/openclaw/pull/102305) | Closed in local gitcrawl | fix(gateway): re-check session runtime model against current agent defaults after hot-reload; no longer open. |
| [#102244](https://github.com/openclaw/openclaw/issues/102244) | Closed in local gitcrawl | Transcript redaction corrupts Anthropic/Bedrock reasoning signatures (AIza/LTAI false positive), causing persistent replay_invalid; no longer open. |
| [#102160](https://github.com/openclaw/openclaw/pull/102160) | Closed in local gitcrawl | fix(agents): run-lifecycle reliability — bounded release, evidence-based liveness, watchdog semantics; no longer open. |
| [#102148](https://github.com/openclaw/openclaw/pull/102148) | Closed in local gitcrawl | fix(google): normalize legacy provider config with api + cost.cacheWrite compat migration; no longer open. |
| [#102072](https://github.com/openclaw/openclaw/pull/102072) | Closed in local gitcrawl | fix(minimax): apply request policy to media generation requests; no longer open. |
| [#102062](https://github.com/openclaw/openclaw/pull/102062) | Closed in local gitcrawl | fix(openrouter): apply request policy to video catalog requests; no longer open. |
| [#102051](https://github.com/openclaw/openclaw/pull/102051) | Closed in local gitcrawl | fix(agents): emit model.failover diagnostic on normal model fallback transitions; no longer open. |
| [#102026](https://github.com/openclaw/openclaw/pull/102026) | Closed in local gitcrawl | fix(chutes): add timeouts to OAuth HTTP requests; no longer open. |
| [#101989](https://github.com/openclaw/openclaw/pull/101989) | Closed in local gitcrawl | fix(gateway): pass authProfileStore through loopback MCP bridge for OAuth-only plugin tools; no longer open. |
| [#101952](https://github.com/openclaw/openclaw/pull/101952) | Closed in local gitcrawl | fix(agents): align mid-turn tool-result projection precheck; no longer open. |
| [#101950](https://github.com/openclaw/openclaw/pull/101950) | Closed in local gitcrawl | fix(agents): reduce tool-result token over-count in mid-turn precheck; no longer open. |
| [#101943](https://github.com/openclaw/openclaw/pull/101943) | Closed in local gitcrawl | fix(memory-core): guard catch-block async calls and supplement search against unhandled rejections; no longer open. |
| [#101928](https://github.com/openclaw/openclaw/pull/101928) | Closed in local gitcrawl | fix(agents): allow re-entrant session write lock for overflow-recovery compaction; no longer open. |
| [#101763](https://github.com/openclaw/openclaw/issues/101763) | Closed in local gitcrawl | Hosted Molty (usemolty.com): model selector doesn't persist — API always receives dotted id claude-opus-4.8[Błąd]:; no longer open. |
| [#101762](https://github.com/openclaw/openclaw/pull/101762) | Closed in local gitcrawl | fix(agent-core): skip handleRunFailure error forwarding for control-flow signals; no longer open. |
| [#101714](https://github.com/openclaw/openclaw/pull/101714) | Closed in local gitcrawl | Bound model pricing cache size; no longer open. |
| [#101713](https://github.com/openclaw/openclaw/pull/101713) | Closed in local gitcrawl | fix(gateway): cap pricing cache entries to prevent unbounded memory growth (#101543); no longer open. |
| [#101703](https://github.com/openclaw/openclaw/pull/101703) | Closed in local gitcrawl | fix: lower successful agent stop completion logs; no longer open. |
| [#101608](https://github.com/openclaw/openclaw/pull/101608) | Closed in local gitcrawl | fix(ai): record token usage on Responses early-abort (#100954); no longer open. |
| [#101587](https://github.com/openclaw/openclaw/pull/101587) | Closed in local gitcrawl | feat(codex): allow configured app-server provider ids; no longer open. |
| [#101570](https://github.com/openclaw/openclaw/issues/101570) | Closed in local gitcrawl | [Bug]: mimo-v2.5 / mimo-v2.5-pro thinking content leaked into text reply causing severe repetition; no longer open. |
| [#101488](https://github.com/openclaw/openclaw/pull/101488) | Closed in local gitcrawl | fix(openrouter): bound music SSE buffering; no longer open. |
| [#101475](https://github.com/openclaw/openclaw/pull/101475) | Closed in local gitcrawl | fix(session-memory): bound session transcript reads to prevent OOM; no longer open. |
| [#101453](https://github.com/openclaw/openclaw/pull/101453) | Closed in local gitcrawl | fix(anthropic): add claude-fable-5 to CLI allowlist, aliases, labels, and context window; no longer open. |
| [#101433](https://github.com/openclaw/openclaw/pull/101433) | Closed in local gitcrawl | fix(openai): map Responses refusal chunks during tool calls; no longer open. |
| [#101432](https://github.com/openclaw/openclaw/pull/101432) | Closed in local gitcrawl | fix(gateway): reset model discovery cache on hot reload; no longer open. |
| [#101368](https://github.com/openclaw/openclaw/pull/101368) | Closed in local gitcrawl | fix(agents): resolve fable-5 1M context window for claude-cli provider; no longer open. |
| [#101280](https://github.com/openclaw/openclaw/pull/101280) | Closed in local gitcrawl | fix(gradium): TTS rejects untrusted base URLs before sending API keys; no longer open. |
| [#101272](https://github.com/openclaw/openclaw/pull/101272) | Closed in local gitcrawl | [AI] fix(embedding): retry without dimensions and degrade non-local providers on persistent failure; no longer open. |
| [#101257](https://github.com/openclaw/openclaw/pull/101257) | Closed in local gitcrawl | feat(agents): sessions_search tool for full-text recall over past session transcripts; no longer open. |
| [#101181](https://github.com/openclaw/openclaw/pull/101181) | Closed in local gitcrawl | fix(agents): preserve preflight overflow token counts into recovery budgeting; no longer open. |
| [#101177](https://github.com/openclaw/openclaw/pull/101177) | Closed in local gitcrawl | fix(usage): preserve provider-billed zero totals; no longer open. |
| [#101092](https://github.com/openclaw/openclaw/pull/101092) | Closed in local gitcrawl | feat(provider): add Featherless AI integration; no longer open. |
| [#101089](https://github.com/openclaw/openclaw/issues/101089) | Closed in local gitcrawl | Fix: Context overflow hallucination loop caused by unscrubbed preemptive message; no longer open. |
| [#101079](https://github.com/openclaw/openclaw/pull/101079) | Closed in local gitcrawl | fix(extensions/huggingface): bound model discovery JSON response read to prevent OOM; no longer open. |
| [#101078](https://github.com/openclaw/openclaw/pull/101078) | Closed in local gitcrawl | fix(cron): preserve cron context in session entry for async completion wakes; no longer open. |
| [#101075](https://github.com/openclaw/openclaw/pull/101075) | Closed in local gitcrawl | fix(extensions/openai): bound ChatGPT OAuth token response reads to prevent OOM; no longer open. |
| [#101065](https://github.com/openclaw/openclaw/issues/101065) | Closed in local gitcrawl | Add an official Featherless AI provider plugin; no longer open. |
| [#100978](https://github.com/openclaw/openclaw/issues/100978) | Closed in local gitcrawl | [Feature]: sessions_search — full-text search over the agent's own session transcripts; no longer open. |
| [#100957](https://github.com/openclaw/openclaw/issues/100957) | Closed in local gitcrawl | fix(agents): prompt-cache stability fails to normalize surrogate pairs in JSON; no longer open. |
| [#100954](https://github.com/openclaw/openclaw/issues/100954) | Closed in local gitcrawl | fix(llm): token usage mismatch during early stream aborts on Azure OpenAI models; no longer open. |
| [#100917](https://github.com/openclaw/openclaw/pull/100917) | Closed in local gitcrawl | fix(agents): route provider-local-service health probe through fetchWithSsrFGuard; no longer open. |
| [#100916](https://github.com/openclaw/openclaw/pull/100916) | Closed in local gitcrawl | fix(agents): route streamProxy request through fetchWithSsrFGuard; no longer open. |
| [#100841](https://github.com/openclaw/openclaw/pull/100841) | Closed in local gitcrawl | fix(oauth): pass workspace context to resolveProviderIdForAuth on refresh failure; no longer open. |
| [#100839](https://github.com/openclaw/openclaw/pull/100839) | Closed in local gitcrawl | fix(auth): prioritize explicit models.json apiKey over store profiles; no longer open. |
| [#100794](https://github.com/openclaw/openclaw/pull/100794) | Closed in local gitcrawl | fix(model-catalog): retry readdirSync on FsSafeError transient catalog write race; no longer open. |
| [#100699](https://github.com/openclaw/openclaw/issues/100699) | Closed in local gitcrawl | [Feature]: Mobile chat polish pack: model picker favorites, reasoning gating, context usage, link previews, math, streaming reveal; no longer open. |
| [#100640](https://github.com/openclaw/openclaw/issues/100640) | Closed in local gitcrawl | [Bug]: Active memory compaction uses default context window metrics when dispatching to secondary providers in fallback chains; no longer open. |
| [#100632](https://github.com/openclaw/openclaw/pull/100632) | Closed in local gitcrawl | fix(onboard): keep the wizard alive through provider auth failures and polish standalone install UX; no longer open. |
| [#100518](https://github.com/openclaw/openclaw/pull/100518) | Closed in local gitcrawl | fix(memory): resolve stable Node execPath for local embedding worker after Node upgrade; no longer open. |
| [#100460](https://github.com/openclaw/openclaw/issues/100460) | Closed in local gitcrawl | [Bug]:Ollama "stream ended without a final response" errors are not failover-eligible, causing dead-end failures with no fallback; no longer open. |
| [#100456](https://github.com/openclaw/openclaw/pull/100456) | Closed in local gitcrawl 2026-07-05 | fix(auto-reply): surface empty interactive completions; no longer open. |
| [#100312](https://github.com/openclaw/openclaw/issues/100312) | Closed in local gitcrawl | [Bug] Compaction-timeout recovery still leaves session assistant-last on 2026.6.11 (regression of #87472 / #88118) — and the continuation throw is scored as model candidate_failed; no longer open. |
| [#100281](https://github.com/openclaw/openclaw/pull/100281) | Closed in local gitcrawl | fix: replace image blocks comprehensively in non-vision model downgrade; no longer open. |
| [#100272](https://github.com/openclaw/openclaw/pull/100272) | Closed in local gitcrawl | fix(agents): carry current-turn inbound metadata in a tail runtime-context message for byte-stable prompt caching; no longer open. |
| [#100271](https://github.com/openclaw/openclaw/issues/100271) | Closed in local gitcrawl | Active user message keeps inbound metadata that history strips, breaking prompt-cache byte-stability every turn; no longer open. |
| [#100233](https://github.com/openclaw/openclaw/pull/100233) | Closed in local gitcrawl | fix(agents): send session_id affinity header to ChatGPT Responses backend; no longer open. |
| [#100232](https://github.com/openclaw/openclaw/issues/100232) | Closed in local gitcrawl | ChatGPT Responses backend: missing session_id affinity header tanks prompt-cache hit rate; no longer open. |
| [#100161](https://github.com/openclaw/openclaw/pull/100161) | Closed in local gitcrawl | fix: legacy Codex model miss no longer suggests invalid config; no longer open. |
| [#100140](https://github.com/openclaw/openclaw/pull/100140) | Closed in local gitcrawl | feat: let agents remember across private conversations; no longer open. |
| [#100120](https://github.com/openclaw/openclaw/pull/100120) | Closed in local gitcrawl | fix(agents): detect bundled and legacy providers in model-not-found hint; no longer open. |
| [#100118](https://github.com/openclaw/openclaw/pull/100118) | Closed in local gitcrawl | fix(agents): allow model fallback when takeover wrapper holds classifiable promptError; no longer open. |
| [#100104](https://github.com/openclaw/openclaw/pull/100104) | Closed in local gitcrawl | fix: suggest auth check for bundled provider model-not-found errors; no longer open. |
| [#100086](https://github.com/openclaw/openclaw/pull/100086) | Closed in local gitcrawl | fix: suggest checking auth for bundled providers in model-not-found error (fixes #100066); no longer open. |
| [#100077](https://github.com/openclaw/openclaw/pull/100077) | Closed in local gitcrawl | fix(agents): scale aggregate tool-result budget with context window and compact on pressure; no longer open. |
| [#100057](https://github.com/openclaw/openclaw/pull/100057) | Closed in local gitcrawl | Scope memory dreaming sweeps by agent; no longer open. |
| [#100042](https://github.com/openclaw/openclaw/issues/100042) | Closed in local gitcrawl | [Bug]: Window-relative compaction never triggers while the absolute aggregate tool-result cap silently zeroes fresh tool results (large configured contextWindow); no longer open. |
| [#99963](https://github.com/openclaw/openclaw/issues/99963) | Closed in local gitcrawl | Main-turn timeouts wrapped in EmbeddedAttemptPromptErrorWithCleanupTakeoverError bypass model fallback; no longer open. |
| [#99961](https://github.com/openclaw/openclaw/pull/99961) | Closed in local gitcrawl | fix(bedrock): bound Mantle model discovery fetches; no longer open. |
| [#99954](https://github.com/openclaw/openclaw/pull/99954) | Closed in local gitcrawl | feat(clickclack): publish durable agent activity rows (commentary + tool); no longer open. |
| [#99933](https://github.com/openclaw/openclaw/pull/99933) | Closed in local gitcrawl | fix: reject unsupported custom tool_choice in OpenAI Responses; no longer open. |
| [#99913](https://github.com/openclaw/openclaw/pull/99913) | Closed in local gitcrawl | fix #97115: classify isolated cron fallback results; no longer open. |
| [#99892](https://github.com/openclaw/openclaw/pull/99892) | Closed in local gitcrawl | fix(plugins): wrap self-hosted discovery JSON parse in try/catch; no longer open. |
| [#99881](https://github.com/openclaw/openclaw/issues/99881) | Closed in local gitcrawl | [Bug]: All tool outputs display "(see attached image)" after uploading image to a non-multimodal model; no longer open. |
| [#99880](https://github.com/openclaw/openclaw/pull/99880) | Closed in local gitcrawl | chore: remove dead sanitizeThinkingSignatures field from transcript policy; no longer open. |
| [#99860](https://github.com/openclaw/openclaw/pull/99860) | Closed in local gitcrawl | test(clawrouter): avoid mocked oversized usage fetch; no longer open. |
| [#99853](https://github.com/openclaw/openclaw/pull/99853) | Closed in local gitcrawl | fix(gateway): clear model discovery cache during hot reload to prevent stale registries; no longer open. |
| [#99834](https://github.com/openclaw/openclaw/pull/99834) | Closed in local gitcrawl | fix(gateway): clear embedded-agent discovery cache on hot reload to preserve include-defined models; no longer open. |
| [#99791](https://github.com/openclaw/openclaw/pull/99791) | Closed in local gitcrawl | fix(media-understanding): video auto-selection runs without a model; no longer open. |
| [#99789](https://github.com/openclaw/openclaw/pull/99789) | Closed in local gitcrawl | fix(gateway): clear model discovery cache during hot reload to prevent stale registries; no longer open. |
| [#99787](https://github.com/openclaw/openclaw/pull/99787) | Closed in local gitcrawl | fix(huggingface): bound model discovery response body size with readProviderJsonResponse; no longer open. |
| [#99756](https://github.com/openclaw/openclaw/pull/99756) | Closed in local gitcrawl | fix: preserve tool-result text across media fallback and context pressure; no longer open. |
| [#99733](https://github.com/openclaw/openclaw/pull/99733) | Closed in local gitcrawl | feat(google): add Antigravity agy auth bridge; no longer open. |
| [#99684](https://github.com/openclaw/openclaw/issues/99684) | Closed in local gitcrawl | Codex usage-limit errors should retry compatible auth profiles; no longer open. |
| [#99657](https://github.com/openclaw/openclaw/issues/99657) | Closed in local gitcrawl | Add bundled ClawRouter models and quota integration; no longer open. |
| [#99641](https://github.com/openclaw/openclaw/pull/99641) | Closed in local gitcrawl | feat(providers): add Runware provider; no longer open. |
| [#99637](https://github.com/openclaw/openclaw/pull/99637) | Closed in local gitcrawl | fix: preserve OpenCode Go DeepSeek V4 max thinking; no longer open. |
| [#99613](https://github.com/openclaw/openclaw/pull/99613) | Closed in local gitcrawl | fix(lmstudio): embedding preload ignores configured context length; no longer open. |
| [#99607](https://github.com/openclaw/openclaw/pull/99607) | Closed in local gitcrawl | fix: keep Bedrock live smoke on Bedrock runtime; no longer open. |
| [#99605](https://github.com/openclaw/openclaw/pull/99605) | Closed in local gitcrawl | fix(google): bound OAuth token error response reads; no longer open. |
| [#99585](https://github.com/openclaw/openclaw/pull/99585) | Closed in local gitcrawl | fix(ollama): bound native streaming 200 success-body NDJSON reads at 16 MiB; no longer open. |
| [#99564](https://github.com/openclaw/openclaw/pull/99564) | Closed in local gitcrawl | fix(agents): prevent malformed HTML entities from breaking tool calls; no longer open. |
| [#99543](https://github.com/openclaw/openclaw/pull/99543) | Closed in local gitcrawl | fix: store usage-cost pricing fingerprint once; no longer open. |
| [#99541](https://github.com/openclaw/openclaw/pull/99541) | Closed in local gitcrawl | fix(memory): keep local embedding worker forks working after Homebrew Node upgrades; no longer open. |
| [#99533](https://github.com/openclaw/openclaw/pull/99533) | Closed in local gitcrawl | fix(usage-cost-cache): deduplicate pricingFingerprint by storing it at cache-object level (#99511); no longer open. |
| [#99529](https://github.com/openclaw/openclaw/pull/99529) | Closed in local gitcrawl | fix(infra): deduplicate pricing fingerprint in usage-cost cache; no longer open. |
| [#99528](https://github.com/openclaw/openclaw/pull/99528) | Closed in local gitcrawl | fix(session-cost-usage): deduplicate pricingFingerprint by storing it…; no longer open. |
| [#99511](https://github.com/openclaw/openclaw/issues/99511) | Closed in local gitcrawl | Usage-cost cache duplicates an identical `pricingFingerprint` on every entry (~57% of file size); no longer open. |
| [#99495](https://github.com/openclaw/openclaw/issues/99495) | Closed in local gitcrawl | Prompt history is not append-only mid-session → Anthropic prompt-cache thrash (two reproducible invalidators); no longer open. |
| [#99463](https://github.com/openclaw/openclaw/pull/99463) | Closed in local gitcrawl | fix(anthropic): add claude-sonnet-5 to bundled model catalog and GA-1M prefix lists; no longer open. |
| [#99462](https://github.com/openclaw/openclaw/pull/99462) | Closed in local gitcrawl | fix: add claude-sonnet-5 to Anthropic model catalog and GA-1M context prefixes; no longer open. |
| [#99449](https://github.com/openclaw/openclaw/issues/99449) | Closed in local gitcrawl | [Bug]: Enabling Codex plugin causes Runtime to switch to OpenAI Codex and ignore configured primary model, resulting in GPT-5.4-nano TPM failures; no longer open. |
| [#99445](https://github.com/openclaw/openclaw/pull/99445) | Closed in local gitcrawl | fix(agents): clamp custom model maxTokens to contextWindow in parseModels; no longer open. |
| [#99416](https://github.com/openclaw/openclaw/pull/99416) | Closed in local gitcrawl | fix: stop model catalog sidecar read/write races; no longer open. |
| [#99404](https://github.com/openclaw/openclaw/pull/99404) | Closed in local gitcrawl | fix: escape assistant-authored transcript role headers; no longer open. |
| [#99338](https://github.com/openclaw/openclaw/pull/99338) | Closed in local gitcrawl | fix(llm): tool results vanish for OpenAI-compatible providers (DeepSeek); no longer open. |
| [#99324](https://github.com/openclaw/openclaw/pull/99324) | Closed in local gitcrawl | fix(amazon-bedrock): enable prompt caching for Claude 5 models; no longer open. |
| [#99313](https://github.com/openclaw/openclaw/pull/99313) | Closed in local gitcrawl | fix(anthropic): add claude-sonnet-5 to bundled 1M-context catalog; no longer open. |
| [#99305](https://github.com/openclaw/openclaw/issues/99305) | Closed in local gitcrawl | [Bug]: Bedrock provider — claude-sonnet-5 prompt caching broken (cache-control blocks not attached, zero cache hits); no longer open. |
| [#99282](https://github.com/openclaw/openclaw/pull/99282) | Closed in local gitcrawl | fix(openai): respect api:"openai-completions" config in transport normalization (#99273); no longer open. |
| [#99242](https://github.com/openclaw/openclaw/pull/99242) | Closed in local gitcrawl | fix(nvidia): sync recommended models with featured catalog; no longer open. |
| [#99239](https://github.com/openclaw/openclaw/issues/99239) | Closed in local gitcrawl | claude-sonnet-5 missing from bundled Anthropic model catalog / GA-1M-context prefix list; no longer open. |
| [#99234](https://github.com/openclaw/openclaw/pull/99234) | Closed in local gitcrawl | feat(nodes): add auto-discovered Ollama inference; no longer open. |
| [#99228](https://github.com/openclaw/openclaw/issues/99228) | Closed in local gitcrawl | [Feature]: Add auto-discovered Ollama inference on nodes; no longer open. |
| [#99222](https://github.com/openclaw/openclaw/pull/99222) | Closed in local gitcrawl | fix(memory-host-sdk): retry fork on ENOENT from stale Homebrew Cellar Node path; no longer open. |
| [#99205](https://github.com/openclaw/openclaw/pull/99205) | Closed in local gitcrawl | fix #99174: classify structured invalid request failover; no longer open. |
| [#99187](https://github.com/openclaw/openclaw/pull/99187) | Closed in local gitcrawl | fix: resolve node execPath before forking embedding worker; no longer open. |
| [#99184](https://github.com/openclaw/openclaw/pull/99184) | Closed in local gitcrawl | fix: use fallback for structured invalid request errors; no longer open. |
| [#99179](https://github.com/openclaw/openclaw/pull/99179) | Closed in local gitcrawl | fix #98866: Embedded local agent runs should serialize globally across session keys when sharing one app-server; no longer open. |
| [#99164](https://github.com/openclaw/openclaw/pull/99164) | Closed in local gitcrawl | fix(agents): classify Anthropic refusal and OpenAI content_filter as failover-eligible refusals; no longer open. |
| [#99140](https://github.com/openclaw/openclaw/pull/99140) | Closed in local gitcrawl | fix: [Bug]: opencode-go/kimi-k2.6 resolves to deepseek-v4-pro at runtime despite config; no longer open. |
| [#99114](https://github.com/openclaw/openclaw/pull/99114) | Closed in local gitcrawl | fix(session-memory): use shortenHomePath for safe home-path display in logs; no longer open. |
| [#99097](https://github.com/openclaw/openclaw/pull/99097) | Closed in local gitcrawl | fix: 429 errors without rate-limit wording skip the same-model retry; no longer open. |
| [#99096](https://github.com/openclaw/openclaw/issues/99096) | Closed in local gitcrawl | [Bug]: transient 429 provider errors without rate-limit wording are surfaced instead of retried; no longer open. |
| [#99091](https://github.com/openclaw/openclaw/pull/99091) | Closed in local gitcrawl | fix: unblock replies after multi-agent room reset; no longer open. |
| [#99079](https://github.com/openclaw/openclaw/pull/99079) | Closed in local gitcrawl | fix: avoid model-not-found fallback on OpenRouter image-input 404s; no longer open. |
| [#99078](https://github.com/openclaw/openclaw/issues/99078) | Closed in local gitcrawl | OpenRouter image-input 404 is classified as model not found; no longer open. |
| [#99076](https://github.com/openclaw/openclaw/pull/99076) | Closed in local gitcrawl | feat(tencent): add Tencent Hy3 provider (TokenHub and TokenPlan); no longer open. |
| [#99069](https://github.com/openclaw/openclaw/issues/99069) | Closed in local gitcrawl | [Feature]: feat(tencent): add Tencent hy3 provider (TokenHub and TokenPlan); no longer open. |
| [#98992](https://github.com/openclaw/openclaw/pull/98992) | Closed in local gitcrawl | fix: emit plugin LLM usage diagnostics; no longer open. |
| [#98954](https://github.com/openclaw/openclaw/pull/98954) | Closed in local gitcrawl | feat(runtime): report model fallback transitions; no longer open. |
| [#98858](https://github.com/openclaw/openclaw/pull/98858) | Closed in local gitcrawl | fix(bedrock-mantle): bound model discovery JSON response read; no longer open. |
| [#98841](https://github.com/openclaw/openclaw/pull/98841) | Closed in local gitcrawl | fix(gateway): include session label in deriveSessionTitle fallback chain; no longer open. |
| [#98816](https://github.com/openclaw/openclaw/pull/98816) | Closed in local gitcrawl | Fix compaction fallback for OpenAI Responses auth; no longer open. |
| [#98814](https://github.com/openclaw/openclaw/issues/98814) | Closed in local gitcrawl | [Bug]: Direct-session compaction inherits OpenAI OAuth profile and fails OpenAI Responses API-key auth; no longer open. |
| [#98795](https://github.com/openclaw/openclaw/pull/98795) | Closed in local gitcrawl | test(shared): add unit tests for modelKey; no longer open. |
| [#98771](https://github.com/openclaw/openclaw/pull/98771) | Closed in local gitcrawl | fix(models): render model context window in decimal K; no longer open. |
| [#98711](https://github.com/openclaw/openclaw/pull/98711) | Closed in local gitcrawl | fix(active-memory): keep recall summaries UTF-16 safe at truncation boundary; no longer open. |
| [#98692](https://github.com/openclaw/openclaw/pull/98692) | Closed in local gitcrawl | fix(google): bound embedding batch response reads; no longer open. |
| [#98679](https://github.com/openclaw/openclaw/pull/98679) | Closed in local gitcrawl | fix(minimax-vlm): bound VLM API response reads; no longer open. |
| [#98651](https://github.com/openclaw/openclaw/pull/98651) | Closed in local gitcrawl | fix(zai): use thinking object for GLM-4.5+ reasoning format; no longer open. |
| [#98650](https://github.com/openclaw/openclaw/issues/98650) | Closed in local gitcrawl | Codex harness: "native hook relay unavailable" — bridge record written but every tool fail-closes (2026.6.11, isolated multi-agent gateway); no longer open. |
| [#98645](https://github.com/openclaw/openclaw/pull/98645) | Closed in local gitcrawl | fix(openrouter): bound OAuth API key response read to prevent OOM; no longer open. |
| [#98633](https://github.com/openclaw/openclaw/issues/98633) | Closed in local gitcrawl | [Bug]: status --all can print credentials hidden in channel base URLs; no longer open. |
| [#98624](https://github.com/openclaw/openclaw/pull/98624) | Closed in local gitcrawl | fix(memory-host-sdk): do not wipe archive on user-typed [cron: prefix; no longer open. |
| [#98599](https://github.com/openclaw/openclaw/pull/98599) | Closed in local gitcrawl | fix(status): redact channel base URLs in status-all; no longer open. |
| [#98578](https://github.com/openclaw/openclaw/pull/98578) | Closed in local gitcrawl | fix(memory-search): stop wiping archive content on user-typed [cron: prefix; no longer open. |
| [#98559](https://github.com/openclaw/openclaw/pull/98559) | Closed in local gitcrawl | improve(web-fetch): speed up provider fallback loading; no longer open. |
| [#98527](https://github.com/openclaw/openclaw/pull/98527) | Closed in local gitcrawl | fix(agents): Anthropic replay fails after boundaryless compaction; no longer open. |
| [#98514](https://github.com/openclaw/openclaw/pull/98514) | Closed in local gitcrawl | fix(memory-host-sdk): prevent mid-transcript [cron:] from wiping archive content; no longer open. |
| [#98490](https://github.com/openclaw/openclaw/pull/98490) | Closed in local gitcrawl | fix(llm): add zai thinking handler to transport stream for GLM-4.5+ models; no longer open. |
| [#98430](https://github.com/openclaw/openclaw/pull/98430) | Closed in local gitcrawl | fix: omit synthesized maxTokens fallback for custom Xiaomi models; no longer open. |
| [#98381](https://github.com/openclaw/openclaw/pull/98381) | Closed in local gitcrawl | fix(memory-core): guard qmd mcporter JSON.parse against non-JSON stdout; no longer open. |
| [#98378](https://github.com/openclaw/openclaw/issues/98378) | Closed in local gitcrawl | Model switch in same session breaks all tool calls (2026.6.10 regression); no longer open. |
| [#98363](https://github.com/openclaw/openclaw/pull/98363) | Closed in local gitcrawl | fix(memory-host-sdk): stop text-pattern cron detection from wiping archive content; no longer open. |
| [#98361](https://github.com/openclaw/openclaw/pull/98361) | Closed in local gitcrawl | fix(llm): omit max_completion_tokens when maxTokens is not configured for custom models; no longer open. |
| [#98351](https://github.com/openclaw/openclaw/pull/98351) | Closed in local gitcrawl | fix: guard JSON.parse calls against malformed external responses; no longer open. |
| [#98343](https://github.com/openclaw/openclaw/pull/98343) | Closed in local gitcrawl | feat(google): restore Antigravity and harden Gemini auth boundary; no longer open. |
| [#98321](https://github.com/openclaw/openclaw/pull/98321) | Closed in local gitcrawl | fix(memory-host-sdk): prevent mid-transcript [cron:...] from wiping archive content; no longer open. |
| [#98312](https://github.com/openclaw/openclaw/pull/98312) | Closed in local gitcrawl | fix(agent-model): omit synthesized maxTokens fallback when nothing was configured; no longer open. |
| [#98295](https://github.com/openclaw/openclaw/issues/98295) | Closed in local gitcrawl | [Bug]: custom Xiaomi MiMo models generate invalid max_completion_tokens when maxTokens is not specified; no longer open. |
| [#98281](https://github.com/openclaw/openclaw/pull/98281) | Closed in local gitcrawl | fix(gateway): strip provider defaults for config.patch; no longer open. |
| [#98270](https://github.com/openclaw/openclaw/issues/98270) | Closed in local gitcrawl | [Bug]: gateway config.patch rejects empty baseUrl injected for built-in providers (stripBundledProviderRuntimeDefaults not applied on patch path); no longer open. |
| [#98264](https://github.com/openclaw/openclaw/issues/98264) | Closed in local gitcrawl | [Bug]: Skill-prescribed imageModel fallback was skipped after primary image model 429; no longer open. |
| [#98254](https://github.com/openclaw/openclaw/pull/98254) | Closed in local gitcrawl | feat(models): add Claude Sonnet 5 support; no longer open. |
| [#98253](https://github.com/openclaw/openclaw/pull/98253) | Closed in local gitcrawl | fix(openai-transport): implement proper SSE stream control for Responses API timeout; no longer open. |
| [#98246](https://github.com/openclaw/openclaw/pull/98246) | Closed in local gitcrawl | fix(memory): stop message-level [cron: classification from wiping non-cron archives (fixes #98241) (AI-assisted); no longer open. |
| [#98244](https://github.com/openclaw/openclaw/issues/98244) | Closed in local gitcrawl | fix(openai-transport): 120-second timeout in OpenAI Responses API streaming; no longer open. |
| [#98241](https://github.com/openclaw/openclaw/issues/98241) | Closed in local gitcrawl | memory_search: reset/deleted session archive silently drops all content when a user message starts with [cron:; no longer open. |
| [#98231](https://github.com/openclaw/openclaw/pull/98231) | Closed in local gitcrawl | fix(xai): prefer catalog contextWindow for grok-4.3 (fixes 200k vs 1M) [AI-assisted]; no longer open. |
| [#98213](https://github.com/openclaw/openclaw/pull/98213) | Closed in local gitcrawl | fix(agents): bound MiniMax VLM JSON response reads, fix test mocks and lint; no longer open. |
| [#98191](https://github.com/openclaw/openclaw/pull/98191) | Closed in local gitcrawl | fix(agents): bound MiniMax VLM and native PDF provider JSON response reads to prevent OOM; no longer open. |
| [#98187](https://github.com/openclaw/openclaw/pull/98187) | Closed in local gitcrawl | fix(openrouter): send explicit auth headers; no longer open. |
| [#98182](https://github.com/openclaw/openclaw/pull/98182) | Closed in local gitcrawl | fix(agent): allow silent-error retry for empty turns regardless of tool definitions; no longer open. |
| [#98178](https://github.com/openclaw/openclaw/pull/98178) | Closed in local gitcrawl | fix(zai): add user-agent header to endpoint detection probe; no longer open. |
| [#98165](https://github.com/openclaw/openclaw/pull/98165) | Closed in local gitcrawl | fix(agents): classify HTTP 429 overloaded bodies as overloaded, not rate_limit; no longer open. |
| [#98148](https://github.com/openclaw/openclaw/pull/98148) | Closed in local gitcrawl | fix(zai): send User-Agent on endpoint detection probes; no longer open. |
| [#98124](https://github.com/openclaw/openclaw/pull/98124) | Closed in local gitcrawl | fix(openai): preserve complete tool calls from clean streams without finish_reason; no longer open. |
| [#98109](https://github.com/openclaw/openclaw/pull/98109) | Closed in local gitcrawl | fix: classify overloaded 429 responses as overloaded, not rate_limit (fixes #98101); no longer open. |
| [#98105](https://github.com/openclaw/openclaw/pull/98105) | Closed in local gitcrawl | fix(auth): count token-type profiles in provider health status rollup; no longer open. |
| [#98101](https://github.com/openclaw/openclaw/issues/98101) | Closed in local gitcrawl | [Bug]: HTTP 429 + 'overloaded' body (e.g. z.ai code 1305) misclassified as rate_limit → false 'API rate limit reached' instead of overloaded; no longer open. |
| [#98092](https://github.com/openclaw/openclaw/issues/98092) | Closed in local gitcrawl | [Feature]: LLM distillation/extraction gate for memory-core deep-phase promotion (distill, don't dump raw snippets into MEMORY.md); no longer open. |
| [#98079](https://github.com/openclaw/openclaw/pull/98079) | Closed in local gitcrawl | fix(ollama): release stream reader lock to prevent resource leak; no longer open. |
| [#98048](https://github.com/openclaw/openclaw/pull/98048) | Closed in local gitcrawl | fix(minimax): guard music generation SSE JSON.parse against malformed frames; no longer open. |
| [#98047](https://github.com/openclaw/openclaw/pull/98047) | Closed in local gitcrawl | fix(openrouter): guard music generation SSE JSON.parse against malformed frames; no longer open. |
| [#98036](https://github.com/openclaw/openclaw/pull/98036) | Closed in local gitcrawl | fix(auth): classify claude-cli 401 output as oauth refresh failure; no longer open. |
| [#98031](https://github.com/openclaw/openclaw/pull/98031) | Closed in local gitcrawl | fix(llm): skip native DeepSeek V4 wrapper for OpenRouter routes; no longer open. |
| [#98021](https://github.com/openclaw/openclaw/pull/98021) | Closed in local gitcrawl | Support Ultra thinking for the native Codex runtime; no longer open. |
| [#97994](https://github.com/openclaw/openclaw/issues/97994) | Closed in local gitcrawl | [Bug]: OpenAI-compatible streaming tool calls are dropped when provider omits finish_reason; no longer open. |
| [#97984](https://github.com/openclaw/openclaw/issues/97984) | Closed in local gitcrawl | Channel-friendly reauth for expired model logins; no longer open. |
| [#97968](https://github.com/openclaw/openclaw/pull/97968) | Closed in local gitcrawl | fix(status): surface unregistered memory embedding providers; no longer open. |
| [#97966](https://github.com/openclaw/openclaw/pull/97966) | Closed in local gitcrawl | fix(agents): allow empty-error-retry when replayMetadata is absent (#97877); no longer open. |
| [#97934](https://github.com/openclaw/openclaw/issues/97934) | Closed in local gitcrawl | [Bug]: OpenRouter "401 Missing Authentication header" on OpenClaw 2026.6.10 — confirmed fixed by downgrade to 2026.6.1; no longer open. |
| [#97930](https://github.com/openclaw/openclaw/pull/97930) | Closed in local gitcrawl | fix: count harness context in overflow guard; no longer open. |
| [#97928](https://github.com/openclaw/openclaw/pull/97928) | Closed in local gitcrawl | fix(agents): estimate harness role sizes in context guard char estimator (fixes #97927); no longer open. |
| [#97927](https://github.com/openclaw/openclaw/issues/97927) | Closed in local gitcrawl | Bug: in-loop context-overflow guard undercounts bashExecution/compactionSummary turns as flat 256 chars and skips overflow protection; no longer open. |
| [#97926](https://github.com/openclaw/openclaw/pull/97926) | Closed in local gitcrawl | fix(agents): xAI/Grok requests fail after a stale reasoning replay ("could not decrypt encrypted_content"); no longer open. |
| [#97899](https://github.com/openclaw/openclaw/pull/97899) | Closed in local gitcrawl | Fix silent provider-error retry after prior side effects; no longer open. |
| [#97895](https://github.com/openclaw/openclaw/pull/97895) | Closed in local gitcrawl | fix: clear stale Claude CLI sessions after failover; no longer open. |
| [#97894](https://github.com/openclaw/openclaw/pull/97894) | Closed in local gitcrawl | fix: surface Claude CLI OAuth reauth hints; no longer open. |
| [#97883](https://github.com/openclaw/openclaw/pull/97883) | Closed in local gitcrawl | fix(openrouter): avoid DeepSeek V4 reasoning conflicts; no longer open. |
| [#97876](https://github.com/openclaw/openclaw/pull/97876) | Closed in local gitcrawl | test(openai-completions): add fetch-proof test for buildGuardedModelFetch wiring; no longer open. |
| [#97872](https://github.com/openclaw/openclaw/pull/97872) | Closed in local gitcrawl | fix(pdf): guard native provider requests; no longer open. |
| [#97871](https://github.com/openclaw/openclaw/issues/97871) | Closed in local gitcrawl | [Bug]: Agent --local hangs with both Ollama and LM Studio while capability model run succeeds; no longer open. |
| [#97858](https://github.com/openclaw/openclaw/pull/97858) | Closed in local gitcrawl | fix(models): preserve audio and video input modalities; no longer open. |
| [#97848](https://github.com/openclaw/openclaw/pull/97848) | Closed in local gitcrawl | fix(openai-responses): bound SSE response reads via buildGuardedModelFetch; no longer open. |
| [#97843](https://github.com/openclaw/openclaw/pull/97843) | Closed in local gitcrawl | fix(openrouter): bound OAuth API key response read to prevent OOM; no longer open. |
| [#97790](https://github.com/openclaw/openclaw/pull/97790) | Closed in local gitcrawl | fix: estimate DeepSeek spend when API reports zero cost; no longer open. |
| [#97788](https://github.com/openclaw/openclaw/pull/97788) | Closed in local gitcrawl | fix(zai): send current GLM thinking params; no longer open. |
| [#97786](https://github.com/openclaw/openclaw/pull/97786) | Closed in local gitcrawl | fix(llm): zai GLM-4.5+ reasoning uses nested thinking object instead of stale enable_thinking; no longer open. |
| [#97776](https://github.com/openclaw/openclaw/pull/97776) | Closed in local gitcrawl | fix(zai): send GLM thinking params; no longer open. |
| [#97750](https://github.com/openclaw/openclaw/issues/97750) | Closed in local gitcrawl | [Bug]: Anthropic `antml:` namespaced tool-call XML leaks into visible content (and fails the turn) when proxy degrades tool_use to text; no longer open. |
| [#97745](https://github.com/openclaw/openclaw/pull/97745) | Closed in local gitcrawl | fix(openrouter,google): bound OAuth response body reads; no longer open. |
| [#97743](https://github.com/openclaw/openclaw/pull/97743) | Closed in local gitcrawl | fix(huggingface): bound model-discovery JSON response via shared provider reader; no longer open. |
| [#97742](https://github.com/openclaw/openclaw/pull/97742) | Closed in local gitcrawl | fix(llm): preserve structured tool result text across providers; no longer open. |
| [#97710](https://github.com/openclaw/openclaw/pull/97710) | Closed in local gitcrawl | fix(memory-core): stop leaking per-agent XDG_CONFIG_HOME to mcporter child spawns; no longer open. |
| [#97694](https://github.com/openclaw/openclaw/pull/97694) | Closed in local gitcrawl | fix(google): bound Gemini batch embedding file content reads to prevent OOM; no longer open. |
| [#97669](https://github.com/openclaw/openclaw/pull/97669) | Closed in local gitcrawl | fix(claude-cli): surface re-auth hint when subprocess OAuth token expires; no longer open. |
| [#97652](https://github.com/openclaw/openclaw/pull/97652) | Closed in local gitcrawl | fix(memory-core): intercept legacy dreaming tokens in before_agent_reply hook; no longer open. |
| [#97633](https://github.com/openclaw/openclaw/pull/97633) | Closed in local gitcrawl | fix(acp): resolve delivery threadId from session deliveryContext for ACP sessions; no longer open. |
| [#97621](https://github.com/openclaw/openclaw/issues/97621) | Closed in local gitcrawl | xAI server-side tools (`code_execution` / `x_search`) are offered to agents on non-xAI models and silently bill xAI; they auto-enable from key presence; no longer open. |
| [#97572](https://github.com/openclaw/openclaw/pull/97572) | Closed in local gitcrawl | fix(agents): escalate retry-limit model_not_found to configured fallbacks; no longer open. |
| [#97571](https://github.com/openclaw/openclaw/pull/97571) | Closed in local gitcrawl | fix(failover): allow model_not_found to trigger fallback chain when configured (fixes #97564); no longer open. |
| [#97564](https://github.com/openclaw/openclaw/issues/97564) | Closed in local gitcrawl | [Bug]: Failover skips configured fallbacks when a model is decommissioned (model_not_found treated as terminal); no longer open. |
| [#97561](https://github.com/openclaw/openclaw/pull/97561) | Closed in local gitcrawl | fix(auth): show claude-cli reauth hint for expired OAuth; no longer open. |
| [#97554](https://github.com/openclaw/openclaw/pull/97554) | Closed in local gitcrawl | Add SNES Studio PCC real local model execution; no longer open. |
| [#97542](https://github.com/openclaw/openclaw/pull/97542) | Closed in local gitcrawl | fix(claude-cli): treat apiKeyHelper in settings.json as valid auth; no longer open. |
| [#97540](https://github.com/openclaw/openclaw/pull/97540) | Closed in local gitcrawl | fix(zai): bound Z.AI endpoint-probe error body reads to prevent OOM; no longer open. |
| [#97539](https://github.com/openclaw/openclaw/pull/97539) | Closed in local gitcrawl | fix(signal): cap container REST responses so a hostile signal-cli-rest-api host cannot exhaust memory; no longer open. |
| [#97517](https://github.com/openclaw/openclaw/issues/97517) | Closed in local gitcrawl | /status runtime label + "not allowed; reverted" misreport during a pending cross-harness live model switch (claude-cli → codex), while the codex app-server is actually running; no longer open. |
| [#97492](https://github.com/openclaw/openclaw/pull/97492) | Closed in local gitcrawl | fix(anthropic): accept Claude CLI apiKeyHelper auth; no longer open. |
| [#97453](https://github.com/openclaw/openclaw/pull/97453) | Closed in local gitcrawl | fix(litellm): pass Anthropic cache control; no longer open. |
| [#97450](https://github.com/openclaw/openclaw/pull/97450) | Closed in local gitcrawl | fix(llm): preserve structured tool result text across providers; no longer open. |
| [#97355](https://github.com/openclaw/openclaw/pull/97355) | Closed in local gitcrawl | fix(ollama): keep OpenAI-compatible tool_call arguments as strings; no longer open. |
| [#97349](https://github.com/openclaw/openclaw/pull/97349) | Closed in local gitcrawl | fix(azure-openai-responses): bound SSE response reads via buildGuardedModelFetch; no longer open. |
| [#97344](https://github.com/openclaw/openclaw/pull/97344) | Closed in local gitcrawl | fix(zai): reject onboarding command auth profiles; no longer open. |
| [#97343](https://github.com/openclaw/openclaw/pull/97343) | Closed in local gitcrawl | fix(bedrock): honor adaptive model max tokens; no longer open. |
| [#97332](https://github.com/openclaw/openclaw/pull/97332) | Closed in local gitcrawl | fix: avoid stale dashboard child context budgets; no longer open. |
| [#97328](https://github.com/openclaw/openclaw/pull/97328) | Closed in local gitcrawl | fix(google): rotate Gemini API keys for LLM requests; no longer open. |
| [#97309](https://github.com/openclaw/openclaw/pull/97309) | Closed in local gitcrawl | fix(openrouter): avoid dual DeepSeek V4 reasoning fields; no longer open. |
| [#97262](https://github.com/openclaw/openclaw/pull/97262) | Closed in local gitcrawl | fix(bedrock): apply model maxTokens to adaptive-thinking and Fable 5 requests (fixes #97176); no longer open. |
| [#97255](https://github.com/openclaw/openclaw/pull/97255) | Closed in local gitcrawl | fix(cron): restore isolated model fallback chain after timeout and empty results; no longer open. |
| [#97252](https://github.com/openclaw/openclaw/pull/97252) | Closed in local gitcrawl | fix(agents): keep multimodal models when generated catalogs include audio/video inputs; no longer open. |
| [#97248](https://github.com/openclaw/openclaw/pull/97248) | Closed in local gitcrawl | fix: honor Bedrock adaptive max token caps; no longer open. |
| [#97245](https://github.com/openclaw/openclaw/pull/97245) | Closed in local gitcrawl | fix(memory-core): propagate pending sync/init errors during close (#96766); no longer open. |
| [#97244](https://github.com/openclaw/openclaw/pull/97244) | Closed in local gitcrawl | fix(infra): estimate cost when API returns 0 for known-pricing models; no longer open. |
| [#97243](https://github.com/openclaw/openclaw/pull/97243) | Closed in local gitcrawl | fix(openrouter): avoid DeepSeek V4 reasoning field conflict; no longer open. |
| [#97228](https://github.com/openclaw/openclaw/pull/97228) | Closed in local gitcrawl | fix(openai-completions): bound SSE response reads via buildGuardedModelFetch; no longer open. |
| [#97221](https://github.com/openclaw/openclaw/pull/97221) | Closed in local gitcrawl | fix(plugin-sdk): remove stale reasoning envelope when DeepSeek V4 wrapper emits native effort (#97196); no longer open. |
| [#97220](https://github.com/openclaw/openclaw/pull/97220) | Closed in local gitcrawl | fix(ollama): send tool_call arguments as strings on OpenAI-compatible path; no longer open. |
| [#97208](https://github.com/openclaw/openclaw/pull/97208) | Closed in local gitcrawl | fix: avoid DeepSeek-native thinking on OpenRouter V4; no longer open. |
| [#97206](https://github.com/openclaw/openclaw/pull/97206) | Closed in local gitcrawl | improve(memory-core): count keyword overlap without allocation; no longer open. |
| [#97199](https://github.com/openclaw/openclaw/pull/97199) | Closed in local gitcrawl | fix(plugin-sdk): drop OpenRouter reasoning for DeepSeek V4; no longer open. |
| [#97196](https://github.com/openclaw/openclaw/issues/97196) | Closed in local gitcrawl | DeepSeek V4 wrapper fires for OpenRouter-routed models, sending both reasoning_effort and reasoning.effort (HTTP 400); no longer open. |
| [#97182](https://github.com/openclaw/openclaw/pull/97182) | Closed in local gitcrawl | fix(bedrock): apply model maxTokens to adaptive-thinking and Fable 5 requests; no longer open. |
| [#97180](https://github.com/openclaw/openclaw/issues/97180) | Closed in local gitcrawl | doctor --fix silently adds and enables the uninstalled `codex` plugin (routing-altering) when `openai` is enabled; no longer open. |
| [#97170](https://github.com/openclaw/openclaw/pull/97170) | Closed in local gitcrawl | Fix voice-call streaming provider resolution; no longer open. |
| [#97149](https://github.com/openclaw/openclaw/pull/97149) | Closed in local gitcrawl | feat: add tokenomics plugin for local-first LLM spend accounting; no longer open. |
| [#97147](https://github.com/openclaw/openclaw/pull/97147) | Closed in local gitcrawl | fix(openai-completions): bound SSE response reads via buildGuardedModelFetch; no longer open. |
| [#97146](https://github.com/openclaw/openclaw/pull/97146) | Closed in local gitcrawl | fix(azure-openai-responses): bound SSE response reads via buildGuardedModelFetch; no longer open. |
| [#97139](https://github.com/openclaw/openclaw/pull/97139) | Closed in local gitcrawl | fix(openai-responses): bound SSE response reads via buildGuardedModelFetch; no longer open. |
| [#97137](https://github.com/openclaw/openclaw/pull/97137) | Closed in local gitcrawl | doctor: add memory search lint findings; no longer open. |
| [#97136](https://github.com/openclaw/openclaw/pull/97136) | Closed in local gitcrawl | Add TrustedRouter provider extension; no longer open. |
| [#97134](https://github.com/openclaw/openclaw/pull/97134) | Closed in local gitcrawl | fix(deepseek): recover V4 zero-cost spend; no longer open. |
| [#97132](https://github.com/openclaw/openclaw/pull/97132) | Closed in local gitcrawl | fix(cron): classify empty fallback results so isolated cron chains recover; no longer open. |
| [#97129](https://github.com/openclaw/openclaw/pull/97129) | Closed in local gitcrawl | fix(cron): classify empty/incomplete embedded results for isolated cron fallback chain (fixes #97115); no longer open. |
| [#97128](https://github.com/openclaw/openclaw/pull/97128) | Closed in local gitcrawl | fix(opencode-go): re-arm idle timer on block-boundary events to prevent false stalled-stream abort; no longer open. |
| [#97125](https://github.com/openclaw/openclaw/pull/97125) | Closed in local gitcrawl | Doctor: expose auth profile findings; no longer open. |
| [#97102](https://github.com/openclaw/openclaw/pull/97102) | Closed in local gitcrawl | feat(onboarding): add browser Gemma setup assistant; no longer open. |
| [#97095](https://github.com/openclaw/openclaw/pull/97095) | Closed in local gitcrawl | fix: memory_search honors generic embedding providers; no longer open. |
| [#97094](https://github.com/openclaw/openclaw/pull/97094) | Closed in local gitcrawl | fix(ollama): strip markerless Kimi reasoning preambles; no longer open. |
| [#97083](https://github.com/openclaw/openclaw/pull/97083) | Closed in local gitcrawl | fix(cost): estimate cost when API returns cost.total=0 but pricing is known (fixes #97047); no longer open. |
| [#97082](https://github.com/openclaw/openclaw/pull/97082) | Closed in local gitcrawl | fix(cost): recalculate usage cost if api returns confident zero (DeepSeek V4); no longer open. |
| [#97071](https://github.com/openclaw/openclaw/pull/97071) | Closed in local gitcrawl | fix(openai-completions): bound SSE response reads via buildGuardedModelFetch; no longer open. |
| [#97070](https://github.com/openclaw/openclaw/pull/97070) | Closed in local gitcrawl | fix(azure-openai-responses): bound SSE response reads via buildGuardedModelFetch; no longer open. |
| [#97068](https://github.com/openclaw/openclaw/pull/97068) | Closed in local gitcrawl | fix(openai-responses): bound SSE response reads via buildGuardedModelFetch; no longer open. |
| [#97066](https://github.com/openclaw/openclaw/pull/97066) | Closed in local gitcrawl | [codex] Accept audio and video model catalog inputs; no longer open. |
| [#97065](https://github.com/openclaw/openclaw/pull/97065) | Closed in local gitcrawl | [codex] Estimate known zero transcript costs; no longer open. |
| [#97054](https://github.com/openclaw/openclaw/pull/97054) | Closed in local gitcrawl | fix(cost): estimate usage cost when API returns cost.total=0 but pricing is known; no longer open. |
| [#97052](https://github.com/openclaw/openclaw/pull/97052) | Closed in local gitcrawl | [codex] fix(agents): accept media input catalog modalities; no longer open. |
| [#97048](https://github.com/openclaw/openclaw/issues/97048) | Closed in local gitcrawl | Model catalog validation rejects audio/video input modalities produced by OpenClaw's own catalog fetch (MiniMax-M3, phi-4-multimodal dropped); no longer open. |
| [#97047](https://github.com/openclaw/openclaw/issues/97047) | Closed in local gitcrawl | [Bug]: DeepSeek V4 API returns usage.cost total as 0, causing Control UI Spend to show zero; no longer open. |
| [#97037](https://github.com/openclaw/openclaw/pull/97037) | Closed in local gitcrawl | fix(llm-core): coerce JSON-stringified array/object tool arguments; no longer open. |
| [#97034](https://github.com/openclaw/openclaw/pull/97034) | Closed in local gitcrawl | fix(session-memory): strip orphan plain-text role lines from session-memory transcripts; no longer open. |
| [#97033](https://github.com/openclaw/openclaw/pull/97033) | Closed in local gitcrawl | fix(lmstudio): pass configured contextWindow to embedding model preload; no longer open. |
| [#97023](https://github.com/openclaw/openclaw/pull/97023) | Closed in local gitcrawl | fix: OpenAI bridge rejects Anthropic custom tools; no longer open. |
| [#97022](https://github.com/openclaw/openclaw/pull/97022) | Closed in local gitcrawl | fix(stream-wrapper): convert Anthropic custom tools to OpenAI function format in bridge; no longer open. |
| [#97020](https://github.com/openclaw/openclaw/issues/97020) | Closed in local gitcrawl | OpenAI↔Anthropic bridge leaks Anthropic custom tools (type:"custom") → OpenAI 400 "Invalid value: 'custom'"; no longer open. |
| [#97018](https://github.com/openclaw/openclaw/pull/97018) | Closed in local gitcrawl | fix(lmstudio): pass contextWindow to embedding model preload; no longer open. |
| [#97017](https://github.com/openclaw/openclaw/pull/97017) | Closed in local gitcrawl | fix: zhipu silentOverflow + cron watchdog stage misclassification; no longer open. |
| [#97016](https://github.com/openclaw/openclaw/issues/97016) | Closed in local gitcrawl | Bug: LM Studio embedding preload ignores contextWindow config, causes CUDA OOM; no longer open. |
| [#97015](https://github.com/openclaw/openclaw/issues/97015) | Closed in local gitcrawl | memory_search: index identity check blocks use of valid chunks when memory_index_meta is empty (Ubuntu IP change recovery); no longer open. |
| [#97012](https://github.com/openclaw/openclaw/pull/97012) | Closed in local gitcrawl | fix(plugin-sdk): follow paginated live model catalogs; no longer open. |
| [#97009](https://github.com/openclaw/openclaw/pull/97009) | Closed in local gitcrawl | fix: classify HTTP 429 'temporarily overloaded' as overloaded, not rate_limit; no longer open. |
| [#97007](https://github.com/openclaw/openclaw/pull/97007) | Closed in local gitcrawl | fix(session-memory): forward hook config model to LLM slug generator; no longer open. |
| [#96996](https://github.com/openclaw/openclaw/pull/96996) | Closed in local gitcrawl | fix(opencode-go): disable thinking for minimax-m3 anthropic-messages path; no longer open. |
| [#96995](https://github.com/openclaw/openclaw/pull/96995) | Closed in local gitcrawl | fix(opencode-go): treat block-boundary SSE events as liveness for idle timer; no longer open. |
| [#96993](https://github.com/openclaw/openclaw/pull/96993) | Closed in local gitcrawl | fix(proxy): bound SSE parser buffer to prevent OOM; no longer open. |
| [#96992](https://github.com/openclaw/openclaw/pull/96992) | Closed in local gitcrawl | fix(opencode-go): disable thinking for minimax-m3 anthropic-messages path; no longer open. |
| [#96991](https://github.com/openclaw/openclaw/pull/96991) | Closed in local gitcrawl | fix(opencode-go): treat block-boundary SSE events as liveness for idle timer; no longer open. |
| [#96990](https://github.com/openclaw/openclaw/pull/96990) | Closed in local gitcrawl | fix(webchat): make model selector width adaptive to prevent long name…; no longer open. |
| [#96989](https://github.com/openclaw/openclaw/pull/96989) | Closed in local gitcrawl | fix(provider-transport-fetch): bound SSE buffer to prevent OOM; no longer open. |
| [#96988](https://github.com/openclaw/openclaw/issues/96988) | Closed in local gitcrawl | [Feature]: Request to Add GHE.com Model Integration Feature in OpenCLAW; no longer open. |
| [#96985](https://github.com/openclaw/openclaw/pull/96985) | Closed in local gitcrawl | fix(google): default web_search model to rolling alias, not retired gemini-2.5-flash; no longer open. |
| [#96984](https://github.com/openclaw/openclaw/pull/96984) | Closed in local gitcrawl | fix(google): bound TTS success JSON response reads; no longer open. |
| [#96978](https://github.com/openclaw/openclaw/pull/96978) | Closed in local gitcrawl | fix(together): bound video generation JSON response reads; no longer open. |
| [#96977](https://github.com/openclaw/openclaw/pull/96977) | Closed in local gitcrawl | fix(fal): bound video generation JSON response reads; no longer open. |
| [#96976](https://github.com/openclaw/openclaw/pull/96976) | Closed in local gitcrawl | fix(fal): bound image generation JSON response reads; no longer open. |
| [#96972](https://github.com/openclaw/openclaw/pull/96972) | Closed in local gitcrawl | fix(openai): bound SSE parser buffer to prevent OOM; no longer open. |
| [#96970](https://github.com/openclaw/openclaw/pull/96970) | Closed in local gitcrawl | fix(clickclack): bound REST success JSON response reads; no longer open. |
| [#96968](https://github.com/openclaw/openclaw/pull/96968) | Closed in local gitcrawl | fix(qqbot): bound STT transcription JSON response; no longer open. |
| [#96960](https://github.com/openclaw/openclaw/pull/96960) | Closed in local gitcrawl | fix(auth): resolve alias provider profiles when explicit profileId fails; no longer open. |
| [#96952](https://github.com/openclaw/openclaw/pull/96952) | Closed in local gitcrawl | perf(memory): copy only requested embedding dimensions; no longer open. |
| [#96927](https://github.com/openclaw/openclaw/pull/96927) | Closed in local gitcrawl | fix(comfy): bound JSON response reads via readProviderJsonResponse; no longer open. |
| [#96922](https://github.com/openclaw/openclaw/pull/96922) | Closed in local gitcrawl | fix(llm): coerce stringified JSON arrays/objects in tool argument validation (fixes #96916) (AI-assisted); no longer open. |
| [#96920](https://github.com/openclaw/openclaw/pull/96920) | Closed in local gitcrawl | fix(google-media): bound JSON response reads; no longer open. |
| [#96916](https://github.com/openclaw/openclaw/issues/96916) | Closed in local gitcrawl | [Bug]: MCP tool calls fail when LLMs serialize array/object parameters as strings (MiMo, Ollama, etc.); no longer open. |
| [#96913](https://github.com/openclaw/openclaw/pull/96913) | Closed in local gitcrawl | [AI] fix(ollama): preserve tool_calls.arguments as JSON string for OpenAI-compatible payloads; no longer open. |
| [#96907](https://github.com/openclaw/openclaw/pull/96907) | Closed in local gitcrawl | fix(runway): bound video create/poll response reads; no longer open. |
| [#96905](https://github.com/openclaw/openclaw/pull/96905) | Closed in local gitcrawl | fix(openai): bound video create-submit response reads; no longer open. |
| [#96904](https://github.com/openclaw/openclaw/pull/96904) | Closed in local gitcrawl | fix(together, pixverse): bound video response reads; no longer open. |
| [#96903](https://github.com/openclaw/openclaw/pull/96903) | Closed in local gitcrawl | fix(xai): bound video response reads; no longer open. |
| [#96899](https://github.com/openclaw/openclaw/pull/96899) | Closed in local gitcrawl | fix(runway-video): bound JSON response reads; no longer open. |
| [#96897](https://github.com/openclaw/openclaw/pull/96897) | Closed in local gitcrawl | Fix #96588: Use numeric collation for model alias version sorting; no longer open. |
| [#96896](https://github.com/openclaw/openclaw/pull/96896) | Closed in local gitcrawl | fix: streaming chat fails when gateway mislabels SSE as JSON [AI-assisted]; no longer open. |
| [#96893](https://github.com/openclaw/openclaw/pull/96893) | Closed in local gitcrawl | fix(image): bound image-generation provider response reads; no longer open. |
| [#96890](https://github.com/openclaw/openclaw/pull/96890) | Closed in local gitcrawl | Fix #96525: Engage model fallback chain on cron result-level failures; no longer open. |
| [#96889](https://github.com/openclaw/openclaw/pull/96889) | Closed in local gitcrawl | fix(minimax): bound video control response reads; no longer open. |
| [#96886](https://github.com/openclaw/openclaw/pull/96886) | Closed in local gitcrawl | fix(fal): bound music/video generation response reads; no longer open. |
| [#96885](https://github.com/openclaw/openclaw/pull/96885) | Closed in local gitcrawl | fix(pixverse): bound video-generation success JSON response reads at 16 MiB; no longer open. |
| [#96877](https://github.com/openclaw/openclaw/pull/96877) | Closed in local gitcrawl | fix(copilot-oauth): bound OAuth and API endpoint response reads; no longer open. |
| [#96876](https://github.com/openclaw/openclaw/pull/96876) | Closed in local gitcrawl | feat(local-realtime-voice): route voice turns through main OpenClaw agent loop; no longer open. |
| [#96875](https://github.com/openclaw/openclaw/pull/96875) | Closed in local gitcrawl | fix(vydra): bound control response reads; no longer open. |
| [#96874](https://github.com/openclaw/openclaw/pull/96874) | Closed in local gitcrawl | fix(speech): bound TTS response reads; no longer open. |
| [#96873](https://github.com/openclaw/openclaw/pull/96873) | Closed in local gitcrawl | fix(openrouter): bound video response reads; no longer open. |
| [#96868](https://github.com/openclaw/openclaw/pull/96868) | Closed in local gitcrawl | fix(embedding): bound OpenAI-compatible embedding response reads; no longer open. |
| [#96864](https://github.com/openclaw/openclaw/pull/96864) | Closed in local gitcrawl 2026-07-13 | feat(memory): carry source actor context into recall; no longer open. |
| [#96829](https://github.com/openclaw/openclaw/pull/96829) | Closed in local gitcrawl | fix: detect already-SSE-formatted body to avoid double data: prefix (#96497); no longer open. |
| [#96812](https://github.com/openclaw/openclaw/pull/96812) | Closed in local gitcrawl | fix(opencode-go): treat block-boundary SSE events as liveness for idle timer; no longer open. |
| [#96799](https://github.com/openclaw/openclaw/pull/96799) | Closed in local gitcrawl | fix(memory): distinguish QMD search outcomes; no longer open. |
| [#96796](https://github.com/openclaw/openclaw/issues/96796) | Closed in local gitcrawl | QMD memory_search can force blocking sync after non-result outcomes; no longer open. |
| [#96795](https://github.com/openclaw/openclaw/pull/96795) | Closed in local gitcrawl | fix(codex): move turn-scoped workspace context to thread-level developer instructions; no longer open. |
| [#96787](https://github.com/openclaw/openclaw/pull/96787) | Closed in local gitcrawl | fix(memory-core): report pending close work errors; no longer open. |
| [#96786](https://github.com/openclaw/openclaw/pull/96786) | Closed in local gitcrawl | fix(openai-video-gen): bound video submit response JSON read at 16 MiB; no longer open. |
| [#96785](https://github.com/openclaw/openclaw/issues/96785) | Closed in local gitcrawl | Model Switch (gpt-5.5 → kimi/k2p6) Triggers Context Overflow Without Proper Compaction; no longer open. |
| [#96782](https://github.com/openclaw/openclaw/pull/96782) | Closed in local gitcrawl | fix(video-generation): bound dashscope JSON response reads at 16 MiB; no longer open. |
| [#96781](https://github.com/openclaw/openclaw/pull/96781) | Closed in local gitcrawl | fix: log pending sync and provider init errors on manager close; no longer open. |
| [#96779](https://github.com/openclaw/openclaw/pull/96779) | Closed in local gitcrawl | fix(chutes-oauth-plugin): bound plugin JSON response reads at 16 MiB; no longer open. |
| [#96777](https://github.com/openclaw/openclaw/pull/96777) | Closed in local gitcrawl | fix(chutes-oauth): bound core helper JSON response reads at 16 MiB; no longer open. |
| [#96776](https://github.com/openclaw/openclaw/pull/96776) | Closed in local gitcrawl | fix(image-generation): replace unbounded response.json() with readProviderJsonResponse; no longer open. |
| [#96773](https://github.com/openclaw/openclaw/issues/96773) | Closed in local gitcrawl | [Bug]: Turn-scoped developer instructions (SOUL.md/IDENTITY.md/USER.md) create different message prefixes between full-turn and tool-continuation calls, breaking DeepSeek KV cache (20%/99% oscillation); no longer open. |
| [#96768](https://github.com/openclaw/openclaw/pull/96768) | Closed in local gitcrawl | fix(runtime/proxy): bound streaming success-body SSE reads at 16 MiB; no longer open. |
| [#96766](https://github.com/openclaw/openclaw/issues/96766) | Closed in local gitcrawl | awaitPendingManagerWork silently swallows all errors from pending sync/provider init on close; no longer open. |
| [#96764](https://github.com/openclaw/openclaw/pull/96764) | Closed in local gitcrawl | fix(ollama): preserve custom provider id through memory embedding adapter (#96742); no longer open. |
| [#96762](https://github.com/openclaw/openclaw/pull/96762) | Closed in local gitcrawl | fix(openai-chatgpt-responses): bound streaming success-body SSE reads at 16 MiB; no longer open. |
| [#96753](https://github.com/openclaw/openclaw/pull/96753) | Closed in local gitcrawl | fix(moonshot): prevent reasoning_content leak when reasoning is disabled; no longer open. |
| [#96745](https://github.com/openclaw/openclaw/pull/96745) | Closed in local gitcrawl | fix(markdown): a fenced-code line with trailing text is content, not a closing fence; no longer open. |
| [#96734](https://github.com/openclaw/openclaw/pull/96734) | Closed in local gitcrawl | refactor(memory-core): use replaceFileAtomic for dreaming file writes; no longer open. |
| [#96732](https://github.com/openclaw/openclaw/issues/96732) | Closed in local gitcrawl | [Bug]: reasoning_content leaks into chat output with moonshot/kimi-k2.6, frontend reasoning status out of sync; no longer open. |
| [#96731](https://github.com/openclaw/openclaw/pull/96731) | Closed in local gitcrawl | fix(cron): wire result classifier into isolated cron model fallback chain; no longer open. |
| [#96724](https://github.com/openclaw/openclaw/pull/96724) | Closed in local gitcrawl | fix(agents): fall back to generic embedding provider registry in memory-search config resolution; no longer open. |
| [#96723](https://github.com/openclaw/openclaw/pull/96723) | Closed in local gitcrawl | fix(anthropic): bound streaming 200 success-body SSE reads at 16 MiB (provider path); no longer open. |
| [#96717](https://github.com/openclaw/openclaw/pull/96717) | Closed in local gitcrawl | fix(openai-completions): avoid double-stringifying tool call arguments; no longer open. |
| [#96706](https://github.com/openclaw/openclaw/pull/96706) | Closed in local gitcrawl | fix(media): forward scanned PDF page images as current-turn images; no longer open. |
| [#96701](https://github.com/openclaw/openclaw/pull/96701) | Closed in local gitcrawl | fix(anthropic): bound streaming 200 success-body SSE reads at 16 MiB; no longer open. |
| [#96695](https://github.com/openclaw/openclaw/pull/96695) | Closed in local gitcrawl | fix(cron): classify result-level failures so the model fallback chain engages (#96525); no longer open. |
| [#96690](https://github.com/openclaw/openclaw/pull/96690) | Closed in local gitcrawl | fix(media): forward scanned PDF page images; no longer open. |
| [#96688](https://github.com/openclaw/openclaw/pull/96688) | Closed in local gitcrawl | fix(sdk): promote streaming-byte-guard to plugin-sdk + bound 4 core streaming reads; no longer open. |
| [#96686](https://github.com/openclaw/openclaw/pull/96686) | Closed in local gitcrawl | fix(agents): isolated cron busts prompt prefix cache via per-run session id; no longer open. |
| [#96683](https://github.com/openclaw/openclaw/pull/96683) | Closed in local gitcrawl | fix(model-resolver): use numeric-aware collation for alias/version sort; no longer open. |
| [#96677](https://github.com/openclaw/openclaw/issues/96677) | Closed in local gitcrawl | [Bug]: 2026.6.9 re-busts prompt prefix caching — per-run :run:<UUID> injected into the system-prompt "Runtime:" line (regression of #43148); no longer open. |
| [#96673](https://github.com/openclaw/openclaw/pull/96673) | Closed in local gitcrawl | Harden embedded memory flush isolation; no longer open. |
| [#96669](https://github.com/openclaw/openclaw/pull/96669) | Closed in local gitcrawl | fix(agents): keep lightContext cron prompts within small-context budget; no longer open. |
| [#96668](https://github.com/openclaw/openclaw/pull/96668) | Closed in local gitcrawl | fix(agents): keep lightweight cron prompts out of no-op compaction; no longer open. |
| [#96667](https://github.com/openclaw/openclaw/issues/96667) | Closed in local gitcrawl | Context trimming corrupts thinking blocks, causing Claude API rejection; no longer open. |
| [#96666](https://github.com/openclaw/openclaw/pull/96666) | Closed in local gitcrawl | fix(openai,proxy): bound streaming 200 success-body SSE reads via shared internal guard; no longer open. |
| [#96664](https://github.com/openclaw/openclaw/issues/96664) | Closed in local gitcrawl | Cross-model thinking-signature blocks persist in transcript and permanently brick sessions on replay (Anthropic); no longer open. |
| [#96661](https://github.com/openclaw/openclaw/pull/96661) | Closed in local gitcrawl | fix(gateway): skip secrets.resolve when target SecretRefs use exec providers; no longer open. |
| [#96655](https://github.com/openclaw/openclaw/pull/96655) | Closed in local gitcrawl | perf(memory): add QMD search diagnostics and runtime cache; no longer open. |
| [#96653](https://github.com/openclaw/openclaw/issues/96653) | Closed in local gitcrawl | [Bug]: reply-path secrets.resolve floods gateway log with UNAVAILABLE for model-provider exec SecretRefs (degrades correctly, ~1 line/turn); no longer open. |
| [#96651](https://github.com/openclaw/openclaw/pull/96651) | Closed in local gitcrawl | fix(memory-core): recover primary embedding provider after transient outage; no longer open. |
| [#96643](https://github.com/openclaw/openclaw/pull/96643) | Closed in local gitcrawl | fix(line): forward FileMessage fileName to media store for audio MIME detection; no longer open. |
| [#96641](https://github.com/openclaw/openclaw/pull/96641) | Closed in local gitcrawl | fix(media-understanding): forward scanned PDF page images to vision models on chat channels; no longer open. |
| [#96640](https://github.com/openclaw/openclaw/pull/96640) | Closed in local gitcrawl | fix: use numeric sort for model alias resolution; no longer open. |
| [#96638](https://github.com/openclaw/openclaw/pull/96638) | Closed in local gitcrawl | fix(openai-completions): relocate dynamic cache-boundary suffix for implicit prefix-cache providers; no longer open. |
| [#96632](https://github.com/openclaw/openclaw/pull/96632) | Closed in local gitcrawl | fix(anthropic): bound streaming 200 success-body SSE reads via shared plugin-sdk guard; no longer open. |
| [#96627](https://github.com/openclaw/openclaw/pull/96627) | Closed in local gitcrawl | fix(failover): allow model fallback on harness transport timeout; no longer open. |
| [#96622](https://github.com/openclaw/openclaw/issues/96622) | Closed in local gitcrawl | Gateway event-loop starvation delays/drops WS response delivery to the CLI; no longer open. |
| [#96620](https://github.com/openclaw/openclaw/pull/96620) | Closed in local gitcrawl | fix(feishu,browser,msteams,azure-speech,bedrock-mantle,googlechat,huggingface,perplexity): bound JSON response reads; no longer open. |
| [#96619](https://github.com/openclaw/openclaw/pull/96619) | Closed in local gitcrawl | fix(agents): classify upstream transport errors as fallback-worthy; no longer open. |
| [#96618](https://github.com/openclaw/openclaw/pull/96618) | Closed in local gitcrawl | fix(discord,telegram,github-copilot,google-meet): bound JSON response reads to prevent OOM; no longer open. |
| [#96616](https://github.com/openclaw/openclaw/pull/96616) | Closed in local gitcrawl | fix(line): forward FileMessage fileName to media store for audio MIME detection; no longer open. |
| [#96609](https://github.com/openclaw/openclaw/pull/96609) | Closed in local gitcrawl | fix(model-resolver): use numeric-aware version comparison for model alias resolution; no longer open. |
| [#96608](https://github.com/openclaw/openclaw/pull/96608) | Closed in local gitcrawl | fix(voyage): bound embedding-batch status and error reads; no longer open. |
| [#96606](https://github.com/openclaw/openclaw/pull/96606) | Closed in local gitcrawl | fix(byteplus): bound video-generation success response reads; no longer open. |
| [#96605](https://github.com/openclaw/openclaw/pull/96605) | Closed in local gitcrawl | fix(google): bound Veo video operation response reads; no longer open. |
| [#96604](https://github.com/openclaw/openclaw/pull/96604) | Closed in local gitcrawl | fix(qwen): bound video description success response reads; no longer open. |
| [#96600](https://github.com/openclaw/openclaw/issues/96600) | Closed in local gitcrawl | [Bug]: Google vertex models cannot be overriden via openclaw.json; no longer open. |
| [#96596](https://github.com/openclaw/openclaw/pull/96596) | Closed in local gitcrawl | fix(sessions): use numeric-aware collation in model alias resolution (fixes #96588) (AI-assisted); no longer open. |
| [#96588](https://github.com/openclaw/openclaw/issues/96588) | Closed in local gitcrawl | model resolution: alias selects older version via lexicographic ordering once a family reaches double-digit minor versions; no longer open. |
| [#96568](https://github.com/openclaw/openclaw/pull/96568) | Closed in local gitcrawl | fix(media): forward scanned PDF page images in chat turns; no longer open. |
| [#96544](https://github.com/openclaw/openclaw/pull/96544) | Closed in local gitcrawl | fix(doctor): merge colliding model-ref map keys instead of dropping; no longer open. |
| [#96541](https://github.com/openclaw/openclaw/issues/96541) | Closed in local gitcrawl | [Bug]: scanned / image-only PDFs are silently dropped on chat channels (rendered page images extracted then discarded); no longer open. |
| [#96529](https://github.com/openclaw/openclaw/pull/96529) | Closed in local gitcrawl | fix(cron): engage model fallback on embedded result-level failures (reasoning-only / empty / incomplete_turn); no longer open. |
| [#96526](https://github.com/openclaw/openclaw/pull/96526) | Closed in local gitcrawl | fix(opencode-go): treat stream block boundaries as liveness; no longer open. |
| [#96525](https://github.com/openclaw/openclaw/issues/96525) | Closed in local gitcrawl | [Bug]: isolated cron model-fallback chain never engages on result-level failures (reasoning-only / empty / incomplete_turn), silently dropping the answer; no longer open. |
| [#96523](https://github.com/openclaw/openclaw/pull/96523) | Closed in local gitcrawl | fix(agents): preserve embedded OpenAI completions usage; no longer open. |
| [#96518](https://github.com/openclaw/openclaw/issues/96518) | Closed in local gitcrawl | [Bug]: opencode-go stalled-stream watchdog aborts a live stream and drops the completed answer (idle timer re-arms only on token deltas, not block-boundary events); no longer open. |
| [#96517](https://github.com/openclaw/openclaw/pull/96517) | Closed in local gitcrawl | fix(memory-core): route dreaming corpus through session metadata; no longer open. |
| [#96509](https://github.com/openclaw/openclaw/pull/96509) | Closed in local gitcrawl | fix(agents): classify upstream_error provider transport failures as fallbackable; no longer open. |
| [#96505](https://github.com/openclaw/openclaw/pull/96505) | Closed in local gitcrawl | fix(openrouter): bound video catalog JSON reads; no longer open. |
| [#96503](https://github.com/openclaw/openclaw/pull/96503) | Closed in local gitcrawl | fix(openai): stop double-prefixing SSE bodies mislabeled as JSON; no longer open. |
| [#96502](https://github.com/openclaw/openclaw/pull/96502) | Closed in local gitcrawl | fix(moonshot): bound video description JSON response reads; no longer open. |
| [#96500](https://github.com/openclaw/openclaw/pull/96500) | Closed in local gitcrawl | fix(openrouter): bound video model catalog JSON response reads; no longer open. |
| [#96499](https://github.com/openclaw/openclaw/pull/96499) | Closed in local gitcrawl | fix(github-copilot): bound model discovery and embeddings JSON response; no longer open. |
| [#96498](https://github.com/openclaw/openclaw/pull/96498) | Closed in local gitcrawl | fix(ollama): stop forcing tool_calls.arguments back to an object on the openai-completions path; no longer open. |
| [#96497](https://github.com/openclaw/openclaw/issues/96497) | Closed in local gitcrawl | [Bug]: openai-completions SSE parser double-prefixes data: causing JSON parse failures; no longer open. |
| [#96496](https://github.com/openclaw/openclaw/pull/96496) | Closed in local gitcrawl | fix(speech): bound TTS/STT voice-list and transcription JSON responses; no longer open. |
| [#96495](https://github.com/openclaw/openclaw/pull/96495) | Closed in local gitcrawl | fix(image-gen): bound image generation provider JSON response reads; no longer open. |
| [#96480](https://github.com/openclaw/openclaw/pull/96480) | Closed in local gitcrawl | fix(agents): bound model catalog JSON response reads for bedrock-mantle and huggingface; no longer open. |
| [#96474](https://github.com/openclaw/openclaw/pull/96474) | Closed in local gitcrawl | fix: Ollama Cloud tool calls fail on second turn; no longer open. |
| [#96473](https://github.com/openclaw/openclaw/pull/96473) | Closed in local gitcrawl | fix(ollama): Ollama Cloud tool calls fail after first turn; no longer open. |
| [#96472](https://github.com/openclaw/openclaw/issues/96472) | Closed in local gitcrawl | Bug: Ollama tool_calls.function.arguments sent as object instead of string (regression in 2026.6.10); no longer open. |
| [#96465](https://github.com/openclaw/openclaw/pull/96465) | Closed in local gitcrawl | fix(memory): separate active-memory resource release from manager close; no longer open. |
| [#96461](https://github.com/openclaw/openclaw/pull/96461) | Closed in local gitcrawl | fix: preserve flattened tool call arguments; no longer open. |
| [#96459](https://github.com/openclaw/openclaw/pull/96459) | Closed in local gitcrawl | fix(memory): keep shared QMD manager alive on active-memory recall timeout; no longer open. |
| [#96457](https://github.com/openclaw/openclaw/pull/96457) | Closed in local gitcrawl | fix(auth): allow OpenAI OAuth tokens for audio transcription API; no longer open. |
| [#96455](https://github.com/openclaw/openclaw/issues/96455) | Closed in local gitcrawl | [Bug]: active-memory timeout closes shared QMD memory_search manager; no longer open. |
| [#96441](https://github.com/openclaw/openclaw/issues/96441) | Closed in local gitcrawl | [Bug]: Ollama Cloud tool_calls fail on 2nd turn — arguments sent as JSON object instead of string (400 from Go server) — regression in 2026.6.9; no longer open. |
| [#96430](https://github.com/openclaw/openclaw/pull/96430) | Closed in local gitcrawl | fix(media-generation): preserve trimmed default model flag; no longer open. |
| [#96426](https://github.com/openclaw/openclaw/pull/96426) | Closed in local gitcrawl | fix(model-catalog): normalize manifest alias keys; no longer open. |
| [#96390](https://github.com/openclaw/openclaw/pull/96390) | Closed in local gitcrawl | fix(document-extract): render PDF image fallback per page so multi-page scans don't starve later pages; no longer open. |
| [#96389](https://github.com/openclaw/openclaw/issues/96389) | Closed in local gitcrawl | document-extract fallback mode: "images" renders multi-page scanned PDFs to 1x1 pixels due to clawpdf 4M pixel budget; no longer open. |
| [#96388](https://github.com/openclaw/openclaw/pull/96388) | Closed in local gitcrawl | feat: add Manifest LLM router provider plugin; no longer open. |
| [#96372](https://github.com/openclaw/openclaw/pull/96372) | Closed in local gitcrawl | fix(agents): classify upstream_error as fallbackable to harden model fallback; no longer open. |
| [#96368](https://github.com/openclaw/openclaw/pull/96368) | Closed in local gitcrawl | [AI] fix(model): /model <default> writes override when session runs non-default model; no longer open. |
| [#96355](https://github.com/openclaw/openclaw/issues/96355) | Closed in local gitcrawl | [Bug]: memory_search tool fails on subsequent queries after cold start (index metadata is missing); no longer open. |
| [#96354](https://github.com/openclaw/openclaw/pull/96354) | Closed in local gitcrawl | fix(vydra,xai,runway,pixverse,deepinfra,together,elevenlabs,microsoft): bound JSON response reads to prevent OOM; no longer open. |
| [#96345](https://github.com/openclaw/openclaw/pull/96345) | Closed in local gitcrawl | feat(copilot): add BYOK provider parity; no longer open. |
| [#96328](https://github.com/openclaw/openclaw/issues/96328) | Closed in local gitcrawl | [Bug] openai-compatible embeddings: CLI and runtime compute different providerKey → permanent "index metadata is missing"; no longer open. |
| [#96325](https://github.com/openclaw/openclaw/pull/96325) | Closed in local gitcrawl | Add custom image provider plugin; no longer open. |
| [#96324](https://github.com/openclaw/openclaw/pull/96324) | Closed in local gitcrawl | fix(google): bound JSON response reads to prevent OOM; no longer open. |
| [#96323](https://github.com/openclaw/openclaw/pull/96323) | Closed in local gitcrawl | fix(openai): bound JSON/text response reads to prevent OOM; no longer open. |
| [#96322](https://github.com/openclaw/openclaw/pull/96322) | Closed in local gitcrawl | fix(minimax): bound JSON response reads to prevent OOM; no longer open. |
| [#96321](https://github.com/openclaw/openclaw/pull/96321) | Closed in local gitcrawl | fix(fal): bound JSON response reads to prevent OOM; no longer open. |
| [#96318](https://github.com/openclaw/openclaw/pull/96318) | Closed in local gitcrawl | fix(model-overrides): set liveModelSwitchPending when switching to default model with runtime fields mismatch; no longer open. |
| [#96304](https://github.com/openclaw/openclaw/pull/96304) | Closed in local gitcrawl | fix(memory-core): keep short protected-glossary terms past the min-length gate; no longer open. |
| [#96293](https://github.com/openclaw/openclaw/pull/96293) | Closed in local gitcrawl | fix(cron): clear agentTurn thinking override by blanking the field; no longer open. |
| [#96288](https://github.com/openclaw/openclaw/pull/96288) | Closed in local gitcrawl | fix(model-param-b): match both adjacent <num>b tokens sharing one delimiter; no longer open. |
| [#96287](https://github.com/openclaw/openclaw/issues/96287) | Closed in local gitcrawl | Bug: Cron Control UI cannot clear saved agentTurn model/thinking overrides by blanking fields; no longer open. |
| [#96269](https://github.com/openclaw/openclaw/issues/96269) | Closed in local gitcrawl | Bug: /model silently fails when switching to default model while running a different model; no longer open. |
| [#96264](https://github.com/openclaw/openclaw/pull/96264) | Closed in local gitcrawl | fix(minimax-vlm): bound VLM API response reads; no longer open. |
| [#96262](https://github.com/openclaw/openclaw/pull/96262) | Closed in local gitcrawl | fix(chutes): bound OAuth token exchange and userinfo JSON response reads; no longer open. |
| [#96261](https://github.com/openclaw/openclaw/pull/96261) | Closed in local gitcrawl | fix(image-generation): bound OpenAI-compatible image API response reads; no longer open. |
| [#96260](https://github.com/openclaw/openclaw/pull/96260) | Closed in local gitcrawl | fix(agents): fallback on embedded upstream errors; no longer open. |
| [#96257](https://github.com/openclaw/openclaw/pull/96257) | Closed in local gitcrawl | fix(config): name openai-chatgpt-responses for the removed openai-codex-responses api id; no longer open. |
| [#96254](https://github.com/openclaw/openclaw/issues/96254) | Closed in local gitcrawl | [Bug]: openclaw内部tool的toolcall信息返回; no longer open. |
| [#96253](https://github.com/openclaw/openclaw/pull/96253) | Closed in local gitcrawl | fix(plugins): bound OpenAI-compatible embeddings JSON response reads; no longer open. |
| [#96249](https://github.com/openclaw/openclaw/pull/96249) | Closed in local gitcrawl | fix(chutes-oauth): bound Chutes OAuth JSON response reads; no longer open. |
| [#96248](https://github.com/openclaw/openclaw/pull/96248) | Closed in local gitcrawl | fix(video-generation): bound DashScope JSON response reads; no longer open. |
| [#96245](https://github.com/openclaw/openclaw/pull/96245) | Closed in local gitcrawl | fix(fallback): treat upstream_error as fallbackable; no longer open. |
| [#96238](https://github.com/openclaw/openclaw/pull/96238) | Closed in local gitcrawl | fix(auth): restore OAuth-backed OpenAI batch audio transcription; no longer open. |
| [#96227](https://github.com/openclaw/openclaw/pull/96227) | Closed in local gitcrawl | fix(diagnostics): emit model.usage for HTTP ingress traffic; no longer open. |
| [#96196](https://github.com/openclaw/openclaw/pull/96196) | Closed in local gitcrawl | fix: run fallback models on upstream provider errors; no longer open. |
| [#96193](https://github.com/openclaw/openclaw/pull/96193) | Closed in local gitcrawl | fix(memory-core): migrate dreaming cleanup lifecycle; no longer open. |
| [#96180](https://github.com/openclaw/openclaw/pull/96180) | Closed in local gitcrawl | fix: models status auth, browser local-file nav, codex workspace app-server, tui empty sessions; no longer open. |
| [#96177](https://github.com/openclaw/openclaw/pull/96177) | Closed in local gitcrawl | fix(memory-wiki): wiki_apply errors when another page has bad frontmatter; no longer open. |
| [#96175](https://github.com/openclaw/openclaw/pull/96175) | Closed in local gitcrawl | fix #96116: memory index: openclaw memory index --force exits early without processing full backlog, no error logged; no longer open. |
| [#96173](https://github.com/openclaw/openclaw/pull/96173) | Closed in local gitcrawl | Add local-realtime-voice extension (gateway-relay realtime voice/dictation); no longer open. |
| [#96162](https://github.com/openclaw/openclaw/pull/96162) | Closed in local gitcrawl | refactor: use accessor-backed transcript corpus for memory; no longer open. |
| [#96160](https://github.com/openclaw/openclaw/issues/96160) | Closed in local gitcrawl | [Bug]: Cron agentTurn jobs hang at model-call-started — isolated and persistent sessions, all providers, all settings; no longer open. |
| [#96157](https://github.com/openclaw/openclaw/pull/96157) | Closed in local gitcrawl | fix(memory-core): clamp widen-fallback kNN k to sqlite-vec 4096 limit; no longer open. |
| [#96152](https://github.com/openclaw/openclaw/pull/96152) | Closed in local gitcrawl | fix(agent): emit model.usage diagnostic for HTTP ingress traffic; no longer open. |
| [#96151](https://github.com/openclaw/openclaw/pull/96151) | Closed in local gitcrawl | fix(status): surface fallback model selections in status mismatch detection; no longer open. |
| [#96150](https://github.com/openclaw/openclaw/issues/96150) | Closed in local gitcrawl | [Feature Request] Auto-failover on invalid model selection; no longer open. |
| [#96144](https://github.com/openclaw/openclaw/pull/96144) | Closed in local gitcrawl | fix(video-generation): bound OpenAI video submitted response reads; no longer open. |
| [#96142](https://github.com/openclaw/openclaw/pull/96142) | Closed in local gitcrawl | fix(failover): fallback on replay-safe prompt timeouts; no longer open. |
| [#96136](https://github.com/openclaw/openclaw/pull/96136) | Closed in local gitcrawl | fix(image-generation): bound OpenAI-compatible image response reads; no longer open. |
| [#96131](https://github.com/openclaw/openclaw/issues/96131) | Closed in local gitcrawl | [Bug]: OpenClaw 2026.6.9 Discord + OpenAI Route Regression Report; no longer open. |
| [#96129](https://github.com/openclaw/openclaw/pull/96129) | Closed in local gitcrawl | fix: correct loopback address detection across multiple subsystems; no longer open. |
| [#96126](https://github.com/openclaw/openclaw/issues/96126) | Closed in local gitcrawl | [openclaw status] Model field should distinguish base model from active fallback; no longer open. |
| [#96122](https://github.com/openclaw/openclaw/pull/96122) | Closed in local gitcrawl | docs(gateway): document high-memory local Ollama compaction tuning; no longer open. |
| [#96118](https://github.com/openclaw/openclaw/issues/96118) | Closed in local gitcrawl | [6.9 Regression] Dreaming runs but memory never promotes + Dreams UI shows dash; no longer open. |
| [#96116](https://github.com/openclaw/openclaw/issues/96116) | Closed in local gitcrawl | memory index: openclaw memory index --force exits early without processing full backlog, no error logged; no longer open. |
| [#96114](https://github.com/openclaw/openclaw/pull/96114) | Closed in local gitcrawl | docs: add MegaBrain Gateway (OpenAI-compatible) to model providers; no longer open. |
| [#96111](https://github.com/openclaw/openclaw/issues/96111) | Closed in local gitcrawl | Improve custom provider configuration experience on Windows (4 issues: dual-registration docs, api field reference, schtasks ghost, gateway.cmd path); no longer open. |
| [#96110](https://github.com/openclaw/openclaw/pull/96110) | Closed in local gitcrawl | fix(failover): classify upstream_error as server_error to trigger model fallback; no longer open. |
| [#96097](https://github.com/openclaw/openclaw/pull/96097) | Closed in local gitcrawl | fix: allow fallback on prompt-stage harness-owned timeouts; no longer open. |
| [#96096](https://github.com/openclaw/openclaw/pull/96096) | Closed in local gitcrawl | fix: cron stream stalls fail over before job timeout; no longer open. |
| [#96094](https://github.com/openclaw/openclaw/pull/96094) | Closed in local gitcrawl | fix(memory): prove live manager recovery after CLI reindex; no longer open. |
| [#96093](https://github.com/openclaw/openclaw/issues/96093) | Closed in local gitcrawl | Diagnostics: no model.usage emitted for HTTP ingress (/v1/responses, /v1/chat/completions) — exporters blind to API traffic; no longer open. |
| [#96092](https://github.com/openclaw/openclaw/pull/96092) | Closed in local gitcrawl | fix(memory): schedule qmd embed when embedInterval is explicitly configured in lexical search mode; no longer open. |
| [#96074](https://github.com/openclaw/openclaw/pull/96074) | Closed in local gitcrawl | fix(memory): pass request.proxy to embedding HTTP client for explicit…; no longer open. |
| [#96070](https://github.com/openclaw/openclaw/pull/96070) | Closed in local gitcrawl | fix(agents): enable bundled static catalog fallback for cron Attempt 2; no longer open. |
| [#96068](https://github.com/openclaw/openclaw/pull/96068) | Closed in local gitcrawl | fix(acpx): consume acpx 0.11.1 model capability errors; no longer open. |
| [#96065](https://github.com/openclaw/openclaw/pull/96065) | Closed in local gitcrawl | fix(install): manage config-secretref env refs via OPENCLAW_SERVICE_MANAGED_ENV_KEYS; no longer open. |
| [#96059](https://github.com/openclaw/openclaw/pull/96059) | Closed in local gitcrawl | fix(install): manage auth-profile env refs via OPENCLAW_SERVICE_MANAGED_ENV_KEYS; no longer open. |
| [#96052](https://github.com/openclaw/openclaw/pull/96052) | Closed in local gitcrawl | fix(memory-core): index memory path in FTS text for filename queries (fixes #94102); no longer open. |
| [#96047](https://github.com/openclaw/openclaw/pull/96047) | Closed in local gitcrawl | fix(opencode-go): disable thinking for minimax-m3 anthropic-messages path; no longer open. |
| [#96042](https://github.com/openclaw/openclaw/pull/96042) | Closed in local gitcrawl | fix(lmstudio): bound model load success response body to prevent OOM; no longer open. |
| [#96041](https://github.com/openclaw/openclaw/pull/96041) | Closed in local gitcrawl | fix: classify upstream provider errors as server_error to enable fallback; no longer open. |
| [#96036](https://github.com/openclaw/openclaw/pull/96036) | Closed in local gitcrawl | fix(video-generation): bound dashscope task response reads; no longer open. |
| [#96027](https://github.com/openclaw/openclaw/pull/96027) | Closed in local gitcrawl | fix(ollama): bound model-discovery JSON response reads; no longer open. |
| [#96021](https://github.com/openclaw/openclaw/pull/96021) | Closed in local gitcrawl | fix: heartbeat filter ignores reasoning/thinking blocks in HEARTBEAT_OK detection; no longer open. |
| [#96010](https://github.com/openclaw/openclaw/pull/96010) | Closed in local gitcrawl | fix(codex): stamp transcript messages with explicit harness field (#95875); no longer open. |
| [#95981](https://github.com/openclaw/openclaw/pull/95981) | Closed in local gitcrawl | Add hosted catalog config profiles; no longer open. |
| [#95969](https://github.com/openclaw/openclaw/pull/95969) | Closed in local gitcrawl | Add hosted catalog source profile validation; no longer open. |
| [#95964](https://github.com/openclaw/openclaw/pull/95964) | Closed in local gitcrawl | Persist hosted catalog snapshots in state; no longer open. |
| [#95962](https://github.com/openclaw/openclaw/pull/95962) | Closed in local gitcrawl | fix(acpx): sessions_spawn fails for harnesses lacking model support; no longer open. |
| [#95957](https://github.com/openclaw/openclaw/pull/95957) | Closed in local gitcrawl | improve: speed up provider tool-call streaming; no longer open. |
| [#95951](https://github.com/openclaw/openclaw/pull/95951) | Closed in local gitcrawl | fix(google): add google-gemini-cli auth alias and expand model runtime bindings; no longer open. |
| [#95945](https://github.com/openclaw/openclaw/pull/95945) | Closed in local gitcrawl | fix(media): retry direct delivery when wake returns false after successful generation; no longer open. |
| [#95943](https://github.com/openclaw/openclaw/pull/95943) | Closed in local gitcrawl | fix(cron): preserve provider/model on isolated-run timeout row; no longer open. |
| [#95934](https://github.com/openclaw/openclaw/pull/95934) | Closed in local gitcrawl | fix(xiaomi): correct mimo-v2.5 and mimo-v2.5-pro max output tokens to 128K; no longer open. |
| [#95929](https://github.com/openclaw/openclaw/pull/95929) | Closed in local gitcrawl | [AI] fix(memory-lancedb): expose memory ID in recall and add text-fal…; no longer open. |
| [#95926](https://github.com/openclaw/openclaw/pull/95926) | Closed in local gitcrawl | fix(media-understanding): append actionable install hint when a media provider is missing (#95658); no longer open. |
| [#95916](https://github.com/openclaw/openclaw/pull/95916) | Closed in local gitcrawl | fix(memory): improve node:sqlite unavailable guidance; no longer open. |
| [#95912](https://github.com/openclaw/openclaw/pull/95912) | Closed in local gitcrawl | fix: ignore reasoning-only heartbeat ack blocks; no longer open. |
| [#95910](https://github.com/openclaw/openclaw/issues/95910) | Closed in local gitcrawl | follow-up to #86034: wake-false path bypasses direct media fallback (Hypothesis B); no longer open. |
| [#95906](https://github.com/openclaw/openclaw/pull/95906) | Closed in local gitcrawl | fix(code-mode): surface QuickJS error name and message to the model; no longer open. |
| [#95897](https://github.com/openclaw/openclaw/pull/95897) | Closed in local gitcrawl | fix(heartbeat-filter): preserve HEARTBEAT_OK detection with reasoning/thinking blocks; no longer open. |
| [#95896](https://github.com/openclaw/openclaw/pull/95896) | Closed in local gitcrawl | fix(model-catalog): stripPrefixes over-strips when prefix has whitespace; no longer open. |
| [#95877](https://github.com/openclaw/openclaw/pull/95877) | Closed in local gitcrawl | Add hosted catalog snapshot fallback; no longer open. |
| [#95875](https://github.com/openclaw/openclaw/issues/95875) | Closed in local gitcrawl | Codex-backed cron runs can appear as canonical openai/openai-chatgpt-responses in transcript metadata, obscuring actual harness selection; no longer open. |
| [#95874](https://github.com/openclaw/openclaw/issues/95874) | Closed in local gitcrawl | openclaw cron edit has --model but no --clear-model, so payload.model cannot be removed via the supported CLI; no longer open. |
| [#95873](https://github.com/openclaw/openclaw/issues/95873) | Closed in local gitcrawl | cron_run_logs can drop session_id, provider, and model on early agent failure; no longer open. |
| [#95869](https://github.com/openclaw/openclaw/issues/95869) | Closed in local gitcrawl | sessions_spawn ACP runtime always passes model even when harness lacks session/set_model capability; no longer open. |
| [#95868](https://github.com/openclaw/openclaw/pull/95868) | Closed in local gitcrawl | Add hosted external catalog feed loader; no longer open. |
| [#95852](https://github.com/openclaw/openclaw/pull/95852) | Closed in local gitcrawl | fix(acpx): keep leaked non-openai model out of the Codex ACP thinking slot; no longer open. |
| [#95838](https://github.com/openclaw/openclaw/pull/95838) | Closed in local gitcrawl | feat(heartbeat): add config to preserve silent task results in agent context; no longer open. |
| [#95831](https://github.com/openclaw/openclaw/pull/95831) | Closed in local gitcrawl | fix: compact Codex OAuth OpenAI sessions without API keys; no longer open. |
| [#95816](https://github.com/openclaw/openclaw/pull/95816) | Closed in local gitcrawl | fix(model-ref): use normalized prefix length for stripPrefixes; no longer open. |
| [#95813](https://github.com/openclaw/openclaw/pull/95813) | Closed in local gitcrawl | Fix/95784 cron setup timeout no restart; no longer open. |
| [#95811](https://github.com/openclaw/openclaw/issues/95811) | Closed in local gitcrawl | [Feature]: decouple heartbeat delivery suppression from transcript/context stripping; no longer open. |
| [#95804](https://github.com/openclaw/openclaw/pull/95804) | Closed in local gitcrawl | fix(agent): emit context_management for openai-chatgpt-responses when…; no longer open. |
| [#95802](https://github.com/openclaw/openclaw/pull/95802) | Closed in local gitcrawl | feat(minimax): opt M3 into MiniMax priority lane via fastMode; no longer open. |
| [#95792](https://github.com/openclaw/openclaw/pull/95792) | Closed in local gitcrawl | fix(onboard): refresh provider plugin registry after setup installs; no longer open. |
| [#95791](https://github.com/openclaw/openclaw/pull/95791) | Closed in local gitcrawl | fix(session-memory): sanitize model artifacts before saving memory; no longer open. |
| [#95789](https://github.com/openclaw/openclaw/issues/95789) | Closed in local gitcrawl | 2026.6.8: subagent spawn helper export change and stale cron model migration gap; no longer open. |
| [#95786](https://github.com/openclaw/openclaw/pull/95786) | Closed in local gitcrawl | feat(memory-core): make memory_search tool timeout configurable; no longer open. |
| [#95784](https://github.com/openclaw/openclaw/issues/95784) | Closed in local gitcrawl | [Bug]: onIsolatedAgentSetupTimeout triggers full-process gateway restart on event-loop saturation — destroys in-flight work and re-enters the same saturation on next tick (2026.6.9); no longer open. |
| [#95780](https://github.com/openclaw/openclaw/issues/95780) | Closed in local gitcrawl | [Bug]: ACP spawn of `codex` injects default model id (`gemini-3.1-flash-lite`) into the thinking-level slot; no longer open. |
| [#95779](https://github.com/openclaw/openclaw/pull/95779) | Closed in local gitcrawl | fix(auth): suppress recovery hint for format failures; no longer open. |
| [#95777](https://github.com/openclaw/openclaw/pull/95777) | Closed in local gitcrawl | fix(onboard): external provider plugin install skips selected auth flow; no longer open. |
| [#95775](https://github.com/openclaw/openclaw/pull/95775) | Closed in local gitcrawl | fix(memory): bound dreaming narrative concurrency for heartbeat triggers; no longer open. |
| [#95773](https://github.com/openclaw/openclaw/issues/95773) | Closed in local gitcrawl | task-guard: silence mandate has no exit condition, causes 6902 on ALLOW with instruction-literal models; no longer open. |
| [#95769](https://github.com/openclaw/openclaw/pull/95769) | Closed in local gitcrawl | fix(memory-lancedb): surface memory ID in memory_recall content; no longer open. |
| [#95765](https://github.com/openclaw/openclaw/issues/95765) | Closed in local gitcrawl | bug(onboard): external provider plugin install skips selected auth flow after DeepSeek install; no longer open. |
| [#95760](https://github.com/openclaw/openclaw/issues/95760) | Closed in local gitcrawl | [Bug]: Incomplete turn / stream cut mid-tool-calls with NVIDIA Build provider (GLM 5.1, MiniMax M2.7); no longer open. |
| [#95757](https://github.com/openclaw/openclaw/pull/95757) | Closed in local gitcrawl | fix(memory): respect QMD timeout for memory_search; no longer open. |
| [#95756](https://github.com/openclaw/openclaw/pull/95756) | Closed in local gitcrawl | fix(model-catalog): use normalizedPrefix.length when stripping stripPrefixes; no longer open. |
| [#95755](https://github.com/openclaw/openclaw/pull/95755) | Closed in local gitcrawl | fix(model-catalog): use normalized prefix length in stripPrefixes instead of raw length; no longer open. |
| [#95753](https://github.com/openclaw/openclaw/pull/95753) | Closed in local gitcrawl | fix(run): apply live model switch before each attempt iteration; no longer open. |
| [#95748](https://github.com/openclaw/openclaw/pull/95748) | Closed in local gitcrawl | fix(agents): skip empty-conversation compaction boundary, tolerate fence takeover in cron; no longer open. |
| [#95744](https://github.com/openclaw/openclaw/pull/95744) | Closed in local gitcrawl | fix(model-catalog): strip manifest model-id prefixes by the matched length; no longer open. |
| [#95743](https://github.com/openclaw/openclaw/issues/95743) | Closed in local gitcrawl | [Bug]: Manifest stripPrefixes over-strips the model id - slices by raw prefix length after matching the trimmed/lowercased prefix; no longer open. |
| [#95740](https://github.com/openclaw/openclaw/issues/95740) | Closed in local gitcrawl | [Bug]: google-vertex model_not_found at runtime with authorized_user ADC — regression persists after #90609; no longer open. |
| [#95731](https://github.com/openclaw/openclaw/pull/95731) | Closed in local gitcrawl | fix(cron): pass manifestPlugins through cron model selection for plugin provider resolution; no longer open. |
| [#95729](https://github.com/openclaw/openclaw/pull/95729) | Closed in local gitcrawl | fix: classify provider code-only failover errors; no longer open. |
| [#95727](https://github.com/openclaw/openclaw/pull/95727) | Closed in local gitcrawl | fix(agents): ensure wrapAnthropicStreamWithRecovery works with async streamFn; no longer open. |
| [#95726](https://github.com/openclaw/openclaw/pull/95726) | Closed in local gitcrawl | fix(state): migrate legacy memory store to per-agent database on upgrade; no longer open. |
| [#95722](https://github.com/openclaw/openclaw/pull/95722) | Closed in local gitcrawl | fix: normalize provider keys during model config merge; no longer open. |
| [#95721](https://github.com/openclaw/openclaw/pull/95721) | Closed in local gitcrawl | fix(active-memory): exclude dreaming-narrative session keys from eligibility gate; no longer open. |
| [#95719](https://github.com/openclaw/openclaw/pull/95719) | Closed in local gitcrawl | fix(cli): sync capability inspect metadata flags with registered options; no longer open. |
| [#95715](https://github.com/openclaw/openclaw/pull/95715) | Closed in local gitcrawl | fix: preserve user model override during compaction; no longer open. |
| [#95710](https://github.com/openclaw/openclaw/pull/95710) | Closed in local gitcrawl | fix(vercel-ai-gateway): resolve dynamic model selections; no longer open. |
| [#95702](https://github.com/openclaw/openclaw/pull/95702) | Closed in local gitcrawl | fix(gateway): apply config env vars during startup for systemd-manage…; no longer open. |
| [#95698](https://github.com/openclaw/openclaw/pull/95698) | Closed in local gitcrawl | fix(cron): prevent model-pin bypass, empty compaction, and fence self…; no longer open. |
| [#95693](https://github.com/openclaw/openclaw/issues/95693) | Closed in local gitcrawl | Compaction (/compact) fails with 'No API key found' when model uses codex/claude-cli OAuth runtime; no longer open. |
| [#95675](https://github.com/openclaw/openclaw/pull/95675) | Closed in local gitcrawl | feat(compaction): add compaction.preflight.enabled config gate (#95553); no longer open. |
| [#95670](https://github.com/openclaw/openclaw/pull/95670) | Closed in local gitcrawl | fix(memory): skip memory-wiki vault subtree in workspace memory scan (#95657); no longer open. |
| [#95666](https://github.com/openclaw/openclaw/pull/95666) | Closed in local gitcrawl | Fix memory-wiki bridge self-import loop; no longer open. |
| [#95663](https://github.com/openclaw/openclaw/pull/95663) | Closed in local gitcrawl | fix(memory-wiki): filter self-referential artifacts from bridge import to prevent recursive loop (fixes #95657) (AI-assisted); no longer open. |
| [#95658](https://github.com/openclaw/openclaw/issues/95658) | Closed in local gitcrawl | [Bug]: 2026.6.9 breaks Groq voice transcription — "Media provider not available: groq" (externalized provider plugin not auto-installed); no longer open. |
| [#95657](https://github.com/openclaw/openclaw/issues/95657) | Closed in local gitcrawl | [Bug]: memory-wiki bridge mode creates recursive self-import loop — wiki sources indexed by memory indexer and re-imported as bridge artifacts; no longer open. |
| [#95650](https://github.com/openclaw/openclaw/pull/95650) | Closed in local gitcrawl | fix(agents): retry compaction with backup auth profiles; no longer open. |
| [#95648](https://github.com/openclaw/openclaw/pull/95648) | Closed in local gitcrawl | feat(compaction): add compaction.preflight.enabled config gate (#95553); no longer open. |
| [#95647](https://github.com/openclaw/openclaw/issues/95647) | Closed in local gitcrawl | DeepSeek prompt cache broken since 6.1 - v2026.6.9 still has <10% hit rate, burning money; no longer open. |
| [#95641](https://github.com/openclaw/openclaw/pull/95641) | Closed in local gitcrawl | fix(bedrock): retry Converse Streaming on transient connection drops (#87876); no longer open. |
| [#95634](https://github.com/openclaw/openclaw/pull/95634) | Closed in local gitcrawl | fix(agents): recognize snake_case tool_use types in id sanitizer for cross-provider failover (#95623); no longer open. |
| [#95632](https://github.com/openclaw/openclaw/pull/95632) | Closed in local gitcrawl | fix(agents): classify stream abort errors as transient for fallback rotation; no longer open. |
| [#95631](https://github.com/openclaw/openclaw/pull/95631) | Closed in local gitcrawl | fix #95495: [Bug]: 2026.6.9 silently relocates memory store with no migration, forcing a full re-embed (1499 files) with zero upgrade-time warning; no longer open. |
| [#95627](https://github.com/openclaw/openclaw/issues/95627) | Closed in local gitcrawl | Preserved Claude thinking signatures (opus-4/sonnet-4) fail unrecoverably on prefix-reconstruction replay; strip-and-retry recovery not reached; no longer open. |
| [#95614](https://github.com/openclaw/openclaw/pull/95614) | Closed in local gitcrawl | fix(memory-wiki): preserve human notes block on source re-ingest; no longer open. |
| [#95599](https://github.com/openclaw/openclaw/pull/95599) | Closed in local gitcrawl | fix(memory): backfill provider.model in createWithAdapter when adapter returns empty string; no longer open. |
| [#95596](https://github.com/openclaw/openclaw/pull/95596) | Closed in local gitcrawl | fix: preserve steered audio for inbound TTS; no longer open. |
| [#95595](https://github.com/openclaw/openclaw/pull/95595) | Closed in local gitcrawl | fix(memory-core): skip forced sync for healthy zero-hit search; no longer open. |
| [#95594](https://github.com/openclaw/openclaw/pull/95594) | Closed in local gitcrawl | fix(agent-runner): classify transient provider errors as fallback-worthy; no longer open. |
| [#95586](https://github.com/openclaw/openclaw/issues/95586) | Closed in local gitcrawl | [Bug]: Kimi Coding auth fallback in systemd Gateway when config env is not injected; no longer open. |
| [#95584](https://github.com/openclaw/openclaw/pull/95584) | Closed in local gitcrawl | fix(agents): null-guard baseUrl in getAttributionHeaders (fixes #92974); no longer open. |
| [#95580](https://github.com/openclaw/openclaw/pull/95580) | Closed in local gitcrawl | fix(compaction): preflight compaction uses configured compaction timeout instead of reply operation abort signal; no longer open. |
| [#95579](https://github.com/openclaw/openclaw/pull/95579) | Closed in local gitcrawl | fix(agents): allow model fallback on harness-owned prompt timeout; no longer open. |
| [#95576](https://github.com/openclaw/openclaw/pull/95576) | Closed in local gitcrawl | fix(failover): allow model fallback on harness transport timeout; no longer open. |
| [#95574](https://github.com/openclaw/openclaw/issues/95574) | Closed in local gitcrawl | [Bug]: Behavior bug (incorrect output/state without crash); no longer open. |
| [#95563](https://github.com/openclaw/openclaw/pull/95563) | Closed in local gitcrawl | [codex] feat(mcp): share bundled runtime scope and fix preflight compaction abort; no longer open. |
| [#95562](https://github.com/openclaw/openclaw/issues/95562) | Closed in local gitcrawl | [Bug]: DeepSeek token cost spikes 15-37x after upgrading from 2026.5.27 → 2026.6.x; no longer open. |
| [#95561](https://github.com/openclaw/openclaw/pull/95561) | Closed in local gitcrawl | fix: preflight compaction uses reply abort signal (~60s) instead of configurable compaction timeout (#95553); no longer open. |
| [#95544](https://github.com/openclaw/openclaw/issues/95544) | Closed in local gitcrawl | Feature: Voice Wake should optionally start a realtime Talk session instead of STT→chat→TTS; no longer open. |
| [#95543](https://github.com/openclaw/openclaw/pull/95543) | Closed in local gitcrawl | fix #95474: [Bug]: missing_tool_result (local tool-execution failure) is classified unclassified and triggers cross-provider model fallback; no longer open. |
| [#95542](https://github.com/openclaw/openclaw/pull/95542) | Closed in local gitcrawl | fix #95519: [Bug]: Fallback should trigger on provider upstream_error / LLM request failed; no longer open. |
| [#95537](https://github.com/openclaw/openclaw/pull/95537) | Closed in local gitcrawl 2026-06-28 | fix(agents): expand embedded fallback classifier to accept transient provider errors; no longer open. |
| [#95530](https://github.com/openclaw/openclaw/issues/95530) | Closed in local gitcrawl | opencode-go streaming hangs in isolated cron sessions (model_call:stream_progress stalls); no longer open. |
| [#95524](https://github.com/openclaw/openclaw/pull/95524) | Closed in local gitcrawl | fix(agents): classify upstream_error errorType as server_error for model fallback (fixes #95519) (AI-assisted); no longer open. |
| [#95523](https://github.com/openclaw/openclaw/pull/95523) | Closed in local gitcrawl | fix(agents): classify provider upstream_error as fallbackable transient failure; no longer open. |
| [#95521](https://github.com/openclaw/openclaw/pull/95521) | Closed in local gitcrawl | fix(agents): classify 'upstream request failed' as server_error for failover; no longer open. |
| [#95520](https://github.com/openclaw/openclaw/pull/95520) | Closed in local gitcrawl | fix(agents): prevent Codex missing_tool_result from triggering cross-provider model fallback; no longer open. |
| [#95519](https://github.com/openclaw/openclaw/issues/95519) | Closed in local gitcrawl | [Bug]: Fallback should trigger on provider upstream_error / LLM request failed; no longer open. |
| [#95513](https://github.com/openclaw/openclaw/pull/95513) | Closed in local gitcrawl | fix: treat claude-cli out-of-credits error as fallback-triggering failure (#95489); no longer open. |
| [#95512](https://github.com/openclaw/openclaw/pull/95512) | Closed in local gitcrawl | fix(agents): detect CLI generic failure text in fallback classifier (#95489); no longer open. |
| [#95509](https://github.com/openclaw/openclaw/pull/95509) | Closed in local gitcrawl | feat(ui): per-agent ElevenLabs Voice/TTS settings in control-ui; no longer open. |
| [#95508](https://github.com/openclaw/openclaw/pull/95508) | Closed in local gitcrawl | fix #95489: [Bug]: claude-cli out-of-credits error bypasses model fallback chain — error text delivered as final response; no longer open. |
| [#95501](https://github.com/openclaw/openclaw/pull/95501) | Closed in local gitcrawl | fix(agents): classify generic external runner failure text as fallback-worthy; no longer open. |
| [#95500](https://github.com/openclaw/openclaw/issues/95500) | Closed in local gitcrawl | [Bug]: Plugin model provider (opencode-go) cannot be resolved by isolated cron sessions, even though openclaw models lists it correctly and session_status model=default resolves it for existing sessions.; no longer open. |
| [#95496](https://github.com/openclaw/openclaw/pull/95496) | Closed in local gitcrawl | fix(agents): classify generic external run failure text as fallback-eligible (fixes #95489); no longer open. |
| [#95495](https://github.com/openclaw/openclaw/issues/95495) | Closed in local gitcrawl | [Bug]: 2026.6.9 silently relocates memory store with no migration, forcing a full re-embed (1499 files) with zero upgrade-time warning; no longer open. |
| [#95494](https://github.com/openclaw/openclaw/pull/95494) | Closed in local gitcrawl | fix(agents): prevent missing_tool_result from triggering cross-provider model fallback (#95474); no longer open. |
| [#95491](https://github.com/openclaw/openclaw/pull/95491) | Closed in local gitcrawl | fix(ui): reconcile model dropdown cache with server-resolved model after sessions.patch; no longer open. |
| [#95489](https://github.com/openclaw/openclaw/issues/95489) | Closed in local gitcrawl | [Bug]: claude-cli out-of-credits error bypasses model fallback chain — error text delivered as final response; no longer open. |
| [#95488](https://github.com/openclaw/openclaw/pull/95488) | Closed in local gitcrawl | fix(agents): classify missing_tool_result as tool_error to prevent cross-provider failover; no longer open. |
| [#95487](https://github.com/openclaw/openclaw/pull/95487) | Closed in local gitcrawl | feat(tts): strip emoji characters before speech synthesis (fixes #95478); no longer open. |
| [#95486](https://github.com/openclaw/openclaw/pull/95486) | Closed in local gitcrawl | feat(speech-core): filter emoji before TTS synthesis; no longer open. |
| [#95478](https://github.com/openclaw/openclaw/issues/95478) | Closed in local gitcrawl | [Feature]: 希望在文本转语音前将表情符号过滤掉; no longer open. |
| [#95474](https://github.com/openclaw/openclaw/issues/95474) | Closed in local gitcrawl | [Bug]: missing_tool_result (local tool-execution failure) is classified unclassified and triggers cross-provider model fallback; no longer open. |
| [#95458](https://github.com/openclaw/openclaw/pull/95458) | Closed in local gitcrawl | fix(cron): trim whitespace from object keys to handle malformed model outputs; no longer open. |
| [#95455](https://github.com/openclaw/openclaw/pull/95455) | Closed in local gitcrawl | fix(agents): forward resolved sub-agent model to gateway call (#91171); no longer open. |
| [#95453](https://github.com/openclaw/openclaw/pull/95453) | Closed in local gitcrawl | fix #95407: [Bug]: `cron` tool `add` action mangles certain key names in `job` parameter; no longer open. |
| [#95452](https://github.com/openclaw/openclaw/pull/95452) | Closed in local gitcrawl | fix(memory): align session file counter denominator with indexer filter (fixes #77338); no longer open. |
| [#95447](https://github.com/openclaw/openclaw/pull/95447) | Closed in local gitcrawl | fix(agents): use CJK-aware token estimation for tool results; no longer open. |
| [#95442](https://github.com/openclaw/openclaw/pull/95442) | Closed in local gitcrawl | fix(cron): recover whitespace-padded job keys from local model parsers; no longer open. |
| [#95434](https://github.com/openclaw/openclaw/pull/95434) | Closed in local gitcrawl | fix: persist modelOverride/providerOverride in subagent spawn (#91171); no longer open. |
| [#95427](https://github.com/openclaw/openclaw/pull/95427) | Closed in local gitcrawl | fix(cron): recover whitespace-padded tool keys before validation; no longer open. |
| [#95424](https://github.com/openclaw/openclaw/pull/95424) | Closed in local gitcrawl | fix(cron): trim whitespace-padded keys in job canonicalization; no longer open. |
| [#95421](https://github.com/openclaw/openclaw/pull/95421) | Closed in local gitcrawl | fix(cron): trim trailing whitespace from cron tool job keys in canonicalization (fixes #95407); no longer open. |
| [#95420](https://github.com/openclaw/openclaw/pull/95420) | Closed in local gitcrawl | fix(agents): bound OpenRouter model catalog response reads; no longer open. |
| [#95418](https://github.com/openclaw/openclaw/pull/95418) | Closed in local gitcrawl | fix(agents): bound OpenRouter model-scan catalog success body; no longer open. |
| [#95416](https://github.com/openclaw/openclaw/pull/95416) | Closed in local gitcrawl | fix(inworld): bound TTS audio and error response body reads to prevent OOM; no longer open. |
| [#95414](https://github.com/openclaw/openclaw/pull/95414) | Closed in local gitcrawl | fix(llm): strip trailing spaces from JSON keys in tool-call parsing (fixes #95407); no longer open. |
| [#95408](https://github.com/openclaw/openclaw/issues/95408) | Closed in local gitcrawl | [Feature]: Per-agent model.requestTimeoutSeconds to handle complex cron payloads in fallback chain; no longer open. |
| [#95407](https://github.com/openclaw/openclaw/issues/95407) | Closed in local gitcrawl | [Bug]: `cron` tool `add` action mangles certain key names in `job` parameter; no longer open. |
| [#95401](https://github.com/openclaw/openclaw/pull/95401) | Closed in local gitcrawl | fix(lmstudio): canonicalize variant model keys; no longer open. |
| [#95400](https://github.com/openclaw/openclaw/pull/95400) | Closed in local gitcrawl | fix(model-fallback): classify Codex usage-limit payloads; no longer open. |
| [#95394](https://github.com/openclaw/openclaw/issues/95394) | Closed in local gitcrawl | [Bug]: LM Studio model identifier gets @q4_k_m/@q8_0 quant suffix appended on retry path — assistant turn falsely marked as error; no longer open. |
| [#95393](https://github.com/openclaw/openclaw/pull/95393) | Closed in local gitcrawl | fix #92582: Bug: doctor falsely warns local memory embeddings are not ready; no longer open. |
| [#95392](https://github.com/openclaw/openclaw/pull/95392) | Closed in local gitcrawl | fix(doctor): suppress local memory embedding warning when probe was skipped; no longer open. |
| [#95375](https://github.com/openclaw/openclaw/pull/95375) | Closed in local gitcrawl | feat(requesty): add Requesty as a bundled provider plugin; no longer open. |
| [#95372](https://github.com/openclaw/openclaw/pull/95372) | Closed in local gitcrawl | fix(cli): sync infer capability inspect metadata flags with registered options; no longer open. |
| [#95365](https://github.com/openclaw/openclaw/pull/95365) | Closed in local gitcrawl | fix: preserve user text that looks like inbound metadata; no longer open. |
| [#95358](https://github.com/openclaw/openclaw/pull/95358) | Closed in local gitcrawl | fix(streaming): flush visible text immediately after reasoning close tag; no longer open. |
| [#95347](https://github.com/openclaw/openclaw/pull/95347) | Closed in local gitcrawl | fix(memory): honor qmd search timeout and bound one-shot CLI cleanup; no longer open. |
| [#95345](https://github.com/openclaw/openclaw/pull/95345) | Closed in local gitcrawl | fix(telegram): deliver reasoning as durable block when /reasoning on; no longer open. |
| [#95342](https://github.com/openclaw/openclaw/pull/95342) | Closed in local gitcrawl | fix(agents): skip pre-prompt precheck when context engine owns compaction; no longer open. |
| [#95341](https://github.com/openclaw/openclaw/pull/95341) | Closed in local gitcrawl | fix(ui): show cron job model selection; no longer open. |
| [#95327](https://github.com/openclaw/openclaw/pull/95327) | Closed in local gitcrawl | fix(agents): use context engine token estimate for precheck overflow detection [AI]; no longer open. |
| [#95314](https://github.com/openclaw/openclaw/issues/95314) | Closed in local gitcrawl | Bug: reasoning→content transition text buffered until stream flush; leading newlines swallowed; no longer open. |
| [#95305](https://github.com/openclaw/openclaw/pull/95305) | Closed in local gitcrawl | fix #95219: [Bug]: Historical tool results are re-truncated between turns, breaking prompt cache prefix stability; no longer open. |
| [#95300](https://github.com/openclaw/openclaw/pull/95300) | Closed in local gitcrawl | fix(cli): expose --count on infer image edit, matching image generate; no longer open. |
| [#95298](https://github.com/openclaw/openclaw/pull/95298) | Closed in local gitcrawl | fix(agents): seal deepseek reasoning before the answer (no discrete thinking_end); no longer open. |
| [#95296](https://github.com/openclaw/openclaw/pull/95296) | Closed in local gitcrawl | fix(anthropic): send current claude-cli user-agent on OAuth path; no longer open. |
| [#95294](https://github.com/openclaw/openclaw/pull/95294) | Closed in local gitcrawl | feat(ui): add model selector to cron quick-create wizard (fixes #93507); no longer open. |
| [#95287](https://github.com/openclaw/openclaw/pull/95287) | Closed in local gitcrawl | fix(failover): detect provider transport timeout in AbortError with 'This operation was aborted' message; no longer open. |
| [#95286](https://github.com/openclaw/openclaw/pull/95286) | Closed in local gitcrawl | fix(agents): forward resolved model to sub-agent gateway agent call; no longer open. |
| [#95284](https://github.com/openclaw/openclaw/pull/95284) | Closed in local gitcrawl | fix(openai-completions): close thinking block at reasoning→content transition for providers without discrete thinking_end; no longer open. |
| [#95283](https://github.com/openclaw/openclaw/pull/95283) | Closed in local gitcrawl | fix(openai-completions): seal native reasoning before the answer under /reasoning on; no longer open. |
| [#95281](https://github.com/openclaw/openclaw/pull/95281) | Closed in local gitcrawl | fix(llm): close reasoning stream on text-lane transition for DeepSeek (fixes #95280); no longer open. |
| [#95280](https://github.com/openclaw/openclaw/issues/95280) | Closed in local gitcrawl | deepseek reasoning: final answer merges into the thinking block under /reasoning on (no discrete thinking_end at the reasoning→content transition); no longer open. |
| [#95274](https://github.com/openclaw/openclaw/pull/95274) | Closed in local gitcrawl | fix(memory): preserve Windows QMD command paths; no longer open. |
| [#95268](https://github.com/openclaw/openclaw/pull/95268) | Closed in local gitcrawl | fix(openrouter): expand short canonical model IDs to upstream API slugs (fixes #95198); no longer open. |
| [#95267](https://github.com/openclaw/openclaw/pull/95267) | Closed in local gitcrawl | fix(memory): repair Windows QMD paths whose backslashes were stripped by JSON parsing; no longer open. |
| [#95258](https://github.com/openclaw/openclaw/pull/95258) | Closed in local gitcrawl | fix(openrouter): prevent model prefix duplication for short canonical IDs; no longer open. |
| [#95252](https://github.com/openclaw/openclaw/pull/95252) | Closed in local gitcrawl | fix(memory-host-sdk): preserve Windows backslash paths in QMD command resolution (#92302); no longer open. |
| [#95247](https://github.com/openclaw/openclaw/pull/95247) | Closed in local gitcrawl | fix(context-engine): read allowModelOverride from plugin config instead of hardcoding false; no longer open. |
| [#95246](https://github.com/openclaw/openclaw/pull/95246) | Closed in local gitcrawl | fix(plugin-sdk): bound live model catalog success body; no longer open. |
| [#95244](https://github.com/openclaw/openclaw/pull/95244) | Closed in local gitcrawl | fix(providers): bound self-hosted provider discovery JSON reads; no longer open. |
| [#95224](https://github.com/openclaw/openclaw/issues/95224) | Closed in local gitcrawl | OpenAI Codex gpt-5.5 catalog reports 272k context while OpenClaw can run 1M via override; no longer open. |
| [#95223](https://github.com/openclaw/openclaw/pull/95223) | Closed in local gitcrawl | fix(openai): bound ChatGPT Responses error body reads to prevent OOM; no longer open. |
| [#95214](https://github.com/openclaw/openclaw/pull/95214) | Closed in local gitcrawl | fix(openrouter): expand short DeepSeek V4 aliases in API model normalizer; no longer open. |
| [#95213](https://github.com/openclaw/openclaw/pull/95213) | Closed in local gitcrawl | fix(plugins): infer LLM override policy from config.summaryModel at runtime; no longer open. |
| [#95212](https://github.com/openclaw/openclaw/pull/95212) | Closed in local gitcrawl | fix(memory): preserve Windows absolute paths in QMD command parsing (#92302); no longer open. |
| [#95208](https://github.com/openclaw/openclaw/pull/95208) | Closed in local gitcrawl | fix(openrouter): strip provider prefix from short model refs in API model ID normalization; no longer open. |
| [#95202](https://github.com/openclaw/openclaw/pull/95202) | Closed in local gitcrawl | fix(openrouter): expand short DeepSeek V4 aliases to upstream slug in API normalizer (#95198); no longer open. |
| [#95198](https://github.com/openclaw/openclaw/issues/95198) | Closed in local gitcrawl | Bug: OpenRouter model prefix duplicated when using short model IDs (openrouter/deepseek-v4-flash → openrouter/openrouter/deepseek-v4-flash); no longer open. |
| [#95177](https://github.com/openclaw/openclaw/pull/95177) | Closed in local gitcrawl | fix(doctor): suppress false-positive local embedding warning when gateway probe skipped [AI-assisted]; no longer open. |
| [#95176](https://github.com/openclaw/openclaw/pull/95176) | Closed in local gitcrawl | fix(anthropic): retry on UND_ERR_SOCKET keep-alive failures (#87407); no longer open. |
| [#95165](https://github.com/openclaw/openclaw/issues/95165) | Closed in local gitcrawl | embedded_run watchdog kills sessions during slow Anthropic responses (no progress signal before first token); no longer open. |
| [#95162](https://github.com/openclaw/openclaw/pull/95162) | Closed in local gitcrawl | fix(memory): align session file counter denominator with indexer filter (fixes #77338); no longer open. |
| [#95151](https://github.com/openclaw/openclaw/pull/95151) | Closed in local gitcrawl | fix(ollama): support remote Ollama hosts with extended timeouts; no longer open. |
| [#95149](https://github.com/openclaw/openclaw/pull/95149) | Closed in local gitcrawl | fix(memory-wiki): resolve bridge zero-artifact report in CLI snapshot mode; no longer open. |
| [#95140](https://github.com/openclaw/openclaw/pull/95140) | Closed in local gitcrawl | fix: auto-populate lossless-claw llm policy from summaryModel at config load; no longer open. |
| [#95139](https://github.com/openclaw/openclaw/pull/95139) | Closed in local gitcrawl | fix(ollama): show full thinking levels for live-discovered models in /think menu; no longer open. |
| [#95138](https://github.com/openclaw/openclaw/pull/95138) | Closed in local gitcrawl | fix(doctor): add OAuth re-auth hint to openai-codex provider migration; no longer open. |
| [#95136](https://github.com/openclaw/openclaw/issues/95136) | Closed in local gitcrawl | No migration path or warning when a model provider id is removed/renamed (openai-codex -> openai): OAuth profiles silently orphaned; no longer open. |
| [#95131](https://github.com/openclaw/openclaw/issues/95131) | Closed in local gitcrawl | Official openai/* model selection auto-enables Codex plugin despite disabled/opt-out intent; no longer open. |
| [#95120](https://github.com/openclaw/openclaw/pull/95120) | Closed in local gitcrawl | feat(channels): add directUserId support for per-DM model override; no longer open. |
| [#95101](https://github.com/openclaw/openclaw/pull/95101) | Closed in local gitcrawl | perf(memory-lancedb): cache query embeddings per embeddings instance; no longer open. |
| [#95099](https://github.com/openclaw/openclaw/pull/95099) | Closed in local gitcrawl | fix(memory): align session file counter denominator with indexer filter (fixes #77338); no longer open. |
| [#95091](https://github.com/openclaw/openclaw/pull/95091) | Closed in local gitcrawl | fix(doctor): probe memory embeddings on --deep and skip false warning on local provider; no longer open. |
| [#95087](https://github.com/openclaw/openclaw/pull/95087) | Closed in local gitcrawl | refactor: add memory and QMD session identity mapping; no longer open. |
| [#95067](https://github.com/openclaw/openclaw/pull/95067) | Closed in local gitcrawl | fix(doctor): suppress false-positive local embedding warning when probe is skipped (fixes #92582); no longer open. |
| [#95064](https://github.com/openclaw/openclaw/pull/95064) | Closed in local gitcrawl | fix(doctor): suppress false-positive local embedding warning when probe was skipped (fixes #92582); no longer open. |
| [#95062](https://github.com/openclaw/openclaw/pull/95062) | Closed in local gitcrawl | fix(telegram): fall back to agent default model in /think menu when session model context is empty; no longer open. |
| [#95050](https://github.com/openclaw/openclaw/pull/95050) | Closed in local gitcrawl | fix(auto-reply): surface preserved fallback notices; no longer open. |
| [#95049](https://github.com/openclaw/openclaw/pull/95049) | Closed in local gitcrawl | fix: respect hook config model override in session-memory slug generation (#89551); no longer open. |
| [#95047](https://github.com/openclaw/openclaw/pull/95047) | Closed in local gitcrawl | fix(dreaming): increase narrative timeout from 60s to 120s for ARM devices (fixes #92494); no longer open. |
| [#95045](https://github.com/openclaw/openclaw/pull/95045) | Closed in local gitcrawl 2026-06-20 | fix(utils): handle Windows absolute paths in splitShellArgs (#92302); no longer open. |
| [#95036](https://github.com/openclaw/openclaw/pull/95036) | Closed in local gitcrawl | fix(memory): preserve Windows backslashes in qmd command paths [AI-assisted]; no longer open. |
| [#95022](https://github.com/openclaw/openclaw/pull/95022) | Closed in local gitcrawl | fix(memory-qmd): preserve unquoted Windows absolute paths in qmd command [AI-assisted]; no longer open. |
| [#95003](https://github.com/openclaw/openclaw/issues/95003) | Closed in local gitcrawl | [Bug]: [Regression] [LOCALLY HOTFIXED] Memory search fails with "index metadata is missing" after Node.js 22.22.2 → 22.22.3 upgrade (apt); no longer open. |
| [#94998](https://github.com/openclaw/openclaw/issues/94998) | Closed in local gitcrawl | AbortError timeout not detected — fallback not triggered on provider transport timeout; no longer open. |
| [#94992](https://github.com/openclaw/openclaw/issues/94992) | Closed in local gitcrawl | [Bug]: Invalid signature in thinking block on every agent — persists on v2026.6.1; no longer open. |
| [#94988](https://github.com/openclaw/openclaw/pull/94988) | Closed in local gitcrawl | Codex/fix 94979 kimi web search baseurl; no longer open. |
| [#94985](https://github.com/openclaw/openclaw/pull/94985) | Closed in local gitcrawl | fix(memory-core): skip markdown placeholder snippets in short-term promotion (#80582) [AI-assisted]; no longer open. |
| [#94982](https://github.com/openclaw/openclaw/pull/94982) | Closed in local gitcrawl | fix: preserve Windows path separators in splitShellArgs (#92302); no longer open. |
| [#94979](https://github.com/openclaw/openclaw/issues/94979) | Closed in local gitcrawl | [Bug]: web_search (kimi) returns 401 Invalid Authentication despite valid API key; no longer open. |
| [#94961](https://github.com/openclaw/openclaw/pull/94961) | Closed in local gitcrawl | fix: propagate lossless-claw allowModelOverride at config normalization (#94289); no longer open. |
| [#94960](https://github.com/openclaw/openclaw/pull/94960) | Closed in local gitcrawl | fix: add MiniMax M3/M2.7 to reasoning content replay allowlist (#92769); no longer open. |
| [#94958](https://github.com/openclaw/openclaw/pull/94958) | Closed in local gitcrawl | fix(memory): preserve Windows backslash paths in QMD command resolution; no longer open. |
| [#94954](https://github.com/openclaw/openclaw/pull/94954) | Closed in local gitcrawl | fix(dreaming): increase narrative timeout from 60s to 120s for ARM workloads (fixes #92494); no longer open. |
| [#94941](https://github.com/openclaw/openclaw/pull/94941) | Closed in local gitcrawl | fix(memory-qmd): preserve Windows absolute paths in memory.qmd.command; no longer open. |
| [#94918](https://github.com/openclaw/openclaw/pull/94918) | Closed in local gitcrawl | feat(cron): expose --fallbacks option on cron create and edit commands; no longer open. |
| [#94914](https://github.com/openclaw/openclaw/pull/94914) | Closed in local gitcrawl | fix(models): filter models list by configured providers in replace mode [AI-assisted]; no longer open. |
| [#94911](https://github.com/openclaw/openclaw/pull/94911) | Closed in local gitcrawl | fix(byteplus): add missing cacheRead/cacheWrite pricing for BytePlus models; no longer open. |
| [#94908](https://github.com/openclaw/openclaw/issues/94908) | Closed in local gitcrawl | [Bug]: /v1/responses does not retain conversation context when using the same user value; no longer open. |
| [#94890](https://github.com/openclaw/openclaw/pull/94890) | Closed in local gitcrawl | fix(diagnostic): add hasActiveModelCall to activity snapshot for CLI session recovery; no longer open. |
| [#94884](https://github.com/openclaw/openclaw/pull/94884) | Closed in local gitcrawl | fix(feishu): replace empty Type.Any() with non-empty FlexibleValue in bitable schemas; no longer open. |
| [#94882](https://github.com/openclaw/openclaw/pull/94882) | Closed in local gitcrawl | fix(ollama): treat undefined reasoning as potentially reasoning-capable; no longer open. |
| [#94875](https://github.com/openclaw/openclaw/pull/94875) | Closed in local gitcrawl | fix(dreaming): increase narrative timeout from 60s to 120s for ARM devices (fixes #92494); no longer open. |
| [#94841](https://github.com/openclaw/openclaw/pull/94841) | Closed in local gitcrawl | fix(qmd): preserve Windows absolute paths in command resolution; no longer open. |
| [#94839](https://github.com/openclaw/openclaw/pull/94839) | Closed in local gitcrawl | fix(feishu): replace Type.Record(Type.String(), Type.Any()) with Type.Object({}, {additionalProperties: true}) in bitable tools; no longer open. |
| [#94825](https://github.com/openclaw/openclaw/pull/94825) | Closed in local gitcrawl | fix: respect replace mode in default models list; no longer open. |
| [#94817](https://github.com/openclaw/openclaw/pull/94817) | Closed in local gitcrawl | fix(ollama): treat undefined reasoning as potentially reasoning-capable; no longer open. |
| [#94811](https://github.com/openclaw/openclaw/pull/94811) | Closed in local gitcrawl | fix(ollama): honor memory embedding output dimensionality; no longer open. |
| [#94783](https://github.com/openclaw/openclaw/pull/94783) | Closed in local gitcrawl | fix(memory-core): lower default promotion minScore for Gemini embedding compatibility; no longer open. |
| [#94780](https://github.com/openclaw/openclaw/issues/94780) | Closed in local gitcrawl | [Feature]: Per-cron model selection independent of agent default — run cheap/free models on automation jobs while keeping main agent on premium LLM; no longer open. |
| [#94773](https://github.com/openclaw/openclaw/pull/94773) | Closed in local gitcrawl | refactor(memory): add LEARNINGS.md to workspace memory artifact discovery; no longer open. |
| [#94770](https://github.com/openclaw/openclaw/pull/94770) | Closed in local gitcrawl | fix(memory): align session file counter denominator with indexer filter (fixes #77338); no longer open. |
| [#94763](https://github.com/openclaw/openclaw/pull/94763) | Closed in local gitcrawl | fix(embedding): resilient dimensions retry with availability/compatibility/session safeguards; no longer open. |
| [#94758](https://github.com/openclaw/openclaw/pull/94758) | Closed in local gitcrawl | fix(gateway): propagate allowModelOverride policies from auto-enabled config at startup; no longer open. |
| [#94752](https://github.com/openclaw/openclaw/pull/94752) | Closed in local gitcrawl | fix(reply): clarify stale model override resets; no longer open. |
| [#94745](https://github.com/openclaw/openclaw/pull/94745) | Closed in local gitcrawl | fix(session): avoid misleading rejection message for stale auto overrides in allowlist; no longer open. |
| [#94732](https://github.com/openclaw/openclaw/pull/94732) | Closed in local gitcrawl | fix(memory): add batch completed log after embedding batch finishes; no longer open. |
| [#94728](https://github.com/openclaw/openclaw/pull/94728) | Closed in local gitcrawl | fix(sessions): skip inherited modelOverride when parent model is not in allowlist; no longer open. |
| [#94726](https://github.com/openclaw/openclaw/pull/94726) | Closed in local gitcrawl | fix(google): add gemini-3.5-flash model catalog entry; no longer open. |
| [#94722](https://github.com/openclaw/openclaw/pull/94722) | Closed in local gitcrawl | fix(models): respect models.mode: "replace" in models list output; no longer open. |
| [#94713](https://github.com/openclaw/openclaw/issues/94713) | Closed in local gitcrawl | [Bug]: Dashboard child-session rollover can reject allowed openai/gpt-5.5 and revert to stale gpt-5.4; no longer open. |
| [#94706](https://github.com/openclaw/openclaw/pull/94706) | Closed in local gitcrawl | fix(dreaming): increase narrative timeout from 60s to 120s for ARM workloads (fixes #92494); no longer open. |
| [#94700](https://github.com/openclaw/openclaw/pull/94700) | Closed in local gitcrawl | test: fold HTTP API script proof into QA Lab; no longer open. |
| [#94671](https://github.com/openclaw/openclaw/pull/94671) | Closed in local gitcrawl | feat(memory): support global baselines and agent overrides; no longer open. |
| [#94665](https://github.com/openclaw/openclaw/pull/94665) | Closed in local gitcrawl | fix: #92302 preserve Windows absolute paths in QMD command resolution; no longer open. |
| [#94662](https://github.com/openclaw/openclaw/pull/94662) | Closed in local gitcrawl | fix(xai): allow private self-hosted Responses endpoints; no longer open. |
| [#94653](https://github.com/openclaw/openclaw/pull/94653) | Closed in local gitcrawl | feat(cron): expose --fallbacks flag on cron add/create and edit commands (fixes #90302); no longer open. |
| [#94650](https://github.com/openclaw/openclaw/issues/94650) | Closed in local gitcrawl | Gateway watchdog fails to kill stuck model calls; stall recovery is none; no longer open. |
| [#94646](https://github.com/openclaw/openclaw/pull/94646) | Closed in local gitcrawl | refactor(sqlite): land database-first memory and proxy alignment; no longer open. |
| [#94636](https://github.com/openclaw/openclaw/pull/94636) | Closed in local gitcrawl | fix(memory): skip raw snippets during promotion; no longer open. |
| [#94633](https://github.com/openclaw/openclaw/pull/94633) | Closed in local gitcrawl | fix(feishu): replace empty bitable record value schema rejected by strict validators; no longer open. |
| [#94628](https://github.com/openclaw/openclaw/pull/94628) | Closed in local gitcrawl | Forward run context request headers; no longer open. |
| [#94623](https://github.com/openclaw/openclaw/issues/94623) | Closed in local gitcrawl | [Bug]: Rate-limit quota suspension blocks model fallback — session freezes 30min despite available fallback chain; no longer open. |
| [#94621](https://github.com/openclaw/openclaw/issues/94621) | Closed in local gitcrawl | [Bug]: Rate-limit quota suspension blocks model fallback — session freezes 30min despite available fallback chain; no longer open. |
| [#94590](https://github.com/openclaw/openclaw/pull/94590) | Closed in local gitcrawl | feat(config): allow modelIdNormalization in models.providers config; no longer open. |
| [#94585](https://github.com/openclaw/openclaw/pull/94585) | Closed in local gitcrawl | feat(xiaomi): add MiMo V2.5 models to the pay-as-you-go provider; no longer open. |
| [#94582](https://github.com/openclaw/openclaw/pull/94582) | Closed in local gitcrawl | fix(openai-completions): add disableBoundaryAwareCache compat option for prefix-matching cache providers; no longer open. |
| [#94581](https://github.com/openclaw/openclaw/issues/94581) | Closed in local gitcrawl | Feature Request: memsearch agent_id filtering for multi-agent memory isolation; no longer open. |
| [#94579](https://github.com/openclaw/openclaw/pull/94579) | Closed in local gitcrawl | feat(xmemo-memory): add bundled XMemo cloud memory plugin; no longer open. |
| [#94564](https://github.com/openclaw/openclaw/pull/94564) | Closed in local gitcrawl | fix(memory-core): bound zero-hit forced sync so memory_search can't hang the whole deadline; no longer open. |
| [#94547](https://github.com/openclaw/openclaw/issues/94547) | Closed in local gitcrawl | [Bug]: @openclaw/feishu bitable write tools emit invalid JSON Schema (empty patternProperties sub-schema) — breaks Anthropic via AWS Bedrock; no longer open. |
| [#94540](https://github.com/openclaw/openclaw/pull/94540) | Closed in local gitcrawl | fix: LCM compaction fails: allowModelOverride not propagated to plugin runtime client until config hot-reload; no longer open. |
| [#94537](https://github.com/openclaw/openclaw/pull/94537) | Closed in local gitcrawl | fix(memory-core): harden dreaming daily-file writes and drain dangling recall refs; no longer open. |
| [#94534](https://github.com/openclaw/openclaw/issues/94534) | Closed in local gitcrawl | Recurring "Invalid signature in thinking block" poisons sessions across agents; no longer open. |
| [#94520](https://github.com/openclaw/openclaw/pull/94520) | Closed in local gitcrawl | fix(xai): normalize grok web search tools; no longer open. |
| [#94518](https://github.com/openclaw/openclaw/issues/94518) | Closed in local gitcrawl | DeepSeek cache hit rate <10% after 6.x upgrade - boundary-aware caching breaks prefix matching; no longer open. |
| [#94509](https://github.com/openclaw/openclaw/pull/94509) | Closed in local gitcrawl | fix(memory-wiki): honor durable: true frontmatter in stale pages report; no longer open. |
| [#94503](https://github.com/openclaw/openclaw/pull/94503) | Closed in local gitcrawl | fix(compaction): emit after_compaction hook even when compacted:false; no longer open. |
| [#94500](https://github.com/openclaw/openclaw/issues/94500) | Closed in local gitcrawl | memory_search tool reports "index metadata is missing" in-gateway while CLI reads the same store as healthy (identity resolved before provider init, never recomputed); no longer open. |
| [#94495](https://github.com/openclaw/openclaw/pull/94495) | Closed in local gitcrawl | fix(ollama): add request timeout fallback for remote hosts; no longer open. |
| [#94494](https://github.com/openclaw/openclaw/pull/94494) | Closed in local gitcrawl | fix(agents): map cacheRetention 'standard' to 'short' for Bedrock Claude models; no longer open. |
| [#94493](https://github.com/openclaw/openclaw/pull/94493) | Closed in local gitcrawl | fix(anthropic): strip thinking blocks from completed prior assistant turns; no longer open. |
| [#94490](https://github.com/openclaw/openclaw/pull/94490) | Closed in local gitcrawl | fix(compaction): wire aggregate retry timeout through compaction.timeoutSeconds; no longer open. |
| [#94487](https://github.com/openclaw/openclaw/pull/94487) | Closed in local gitcrawl | fix: #94482 normalize cacheRetention 'standard' to 'short'; no longer open. |
| [#94482](https://github.com/openclaw/openclaw/issues/94482) | Closed in local gitcrawl | Bedrock Claude cacheRetention='standard' is silently ignored; no longer open. |
| [#94481](https://github.com/openclaw/openclaw/pull/94481) | Closed in local gitcrawl | fix(edit): unwrap XML-RPC {item: {oldText, newText}} edit transport shape; no longer open. |
| [#94478](https://github.com/openclaw/openclaw/pull/94478) | Closed in local gitcrawl | fix(doctor): repair legacy Codex route persistence; no longer open. |
| [#94477](https://github.com/openclaw/openclaw/pull/94477) | Closed in local gitcrawl | [AI] fix(session): add session.restartContinuation config to preserve sessionId across Gateway restart; no longer open. |
| [#94461](https://github.com/openclaw/openclaw/pull/94461) | Closed in local gitcrawl | fix(zai): fall back to manifest baseUrl for synthesized GLM-5 models; no longer open. |
| [#94458](https://github.com/openclaw/openclaw/issues/94458) | Closed in local gitcrawl | lossless-claw bootstraps into quarantine after every Gateway restart due to new sessionId generating fresh JSONL file; no longer open. |
| [#94446](https://github.com/openclaw/openclaw/pull/94446) | Closed in local gitcrawl | fix(context-engine): eagerly resolve plugin LLM policy from config for model override authority; no longer open. |
| [#94443](https://github.com/openclaw/openclaw/pull/94443) | Closed in local gitcrawl | fix(memory-wiki): retry transient source-page rewrite race instead of aborting wiki_status; no longer open. |
| [#94440](https://github.com/openclaw/openclaw/pull/94440) | Closed in local gitcrawl | fix: #94432 classify Cloudflare challenge 403 as upstream_html instead of auth_html; no longer open. |
| [#94432](https://github.com/openclaw/openclaw/issues/94432) | Closed in local gitcrawl | OpenAI/Codex OAuth provider fails with Cloudflare HTML 403 from chatgpt.com/backend-api; no longer open. |
| [#94429](https://github.com/openclaw/openclaw/pull/94429) | Closed in local gitcrawl | fix: #94391 将 compaction aggregate timeout 从硬编码 60s 改为读取 compaction.timeoutSeconds 配置; no longer open. |
| [#94419](https://github.com/openclaw/openclaw/pull/94419) | Closed in local gitcrawl | feat(qwen): add Token Plan (Team Edition) provider; no longer open. |
| [#94418](https://github.com/openclaw/openclaw/issues/94418) | Closed in local gitcrawl | [Feature]: Alibaba Model Studio Token Plan (Team Edition) provider; no longer open. |
| [#94404](https://github.com/openclaw/openclaw/pull/94404) | Closed in local gitcrawl | fix(zai): fall back to default baseUrl when template lacks one for catalog models; no longer open. |
| [#94402](https://github.com/openclaw/openclaw/pull/94402) | Closed in local gitcrawl | fix: handle object-format data and URL-safe base64 from OpenAI-compatible proxy responses; no longer open. |
| [#94401](https://github.com/openclaw/openclaw/pull/94401) | Closed in local gitcrawl | fix(session-memory): skip transcript-only assistant messages in getRecentSessionContent; no longer open. |
| [#94378](https://github.com/openclaw/openclaw/pull/94378) | Closed in local gitcrawl | fix(image-gen): skip invalid entries in OpenAI-compatible image response parsing; no longer open. |
| [#94372](https://github.com/openclaw/openclaw/pull/94372) | Closed in local gitcrawl | fix(cli): resolve context window from context.ts to ensure cache is loaded; no longer open. |
| [#94367](https://github.com/openclaw/openclaw/issues/94367) | Closed in local gitcrawl | [Bug]: Image generation "response malformed" when using OpenAI-compatible proxy with valid b64_json response; no longer open. |
| [#94362](https://github.com/openclaw/openclaw/pull/94362) | Closed in local gitcrawl | fix: improve Ollama thinking profile resolution for live-discovered reasoning models using name heuristic; no longer open. |
| [#94355](https://github.com/openclaw/openclaw/pull/94355) | Closed in local gitcrawl | fix(agents): fall back to generic embedding provider registry in memory-search config resolution; no longer open. |
| [#94350](https://github.com/openclaw/openclaw/pull/94350) | Closed in local gitcrawl | feat: externalize GMI provider plugin; no longer open. |
| [#94333](https://github.com/openclaw/openclaw/pull/94333) | Closed in local gitcrawl | fix(agents): read allowModelOverride from plugin config in context-engine capabilities; no longer open. |
| [#94331](https://github.com/openclaw/openclaw/pull/94331) | Closed in local gitcrawl | fix: merge llm policy into plugin subagent override authorization; no longer open. |
| [#94330](https://github.com/openclaw/openclaw/issues/94330) | Closed in local gitcrawl | replay_invalid (stale thinking-block signature) surfaces a hard error + drops the user message instead of self-recovering; no longer open. |
| [#94316](https://github.com/openclaw/openclaw/issues/94316) | Closed in local gitcrawl | Memory search tool cannot find local embedding provider even though CLI shows it as ready; no longer open. |
| [#94311](https://github.com/openclaw/openclaw/pull/94311) | Closed in local gitcrawl | fix: auto-grant lossless-claw model override from summaryModel config; no longer open. |
| [#94297](https://github.com/openclaw/openclaw/pull/94297) | Closed in local gitcrawl | fix(plugins): propagate llm.allowModelOverride to plugin subagent override policies (fixes #94289); no longer open. |
| [#94288](https://github.com/openclaw/openclaw/pull/94288) | Closed in local gitcrawl | fix(memory): refresh stale index handles after cli reindex; no longer open. |
| [#94275](https://github.com/openclaw/openclaw/issues/94275) | Closed in local gitcrawl | Google provider: AQ. format API keys rejected by OpenAI-compatible endpoint (HTTP 401); no longer open. |
| [#94269](https://github.com/openclaw/openclaw/issues/94269) | Closed in local gitcrawl | Z.ai static catalog models resolve without baseUrl and fall through to OpenAI API; no longer open. |
| [#94261](https://github.com/openclaw/openclaw/pull/94261) | Closed in local gitcrawl | [Feature]: [FEAT]: Add Adorbis AI as a bundled provider plugin; no longer open. |
| [#94258](https://github.com/openclaw/openclaw/issues/94258) | Closed in local gitcrawl | Bug: Tier routing not resolving tier-* aliases to actual models in v2026.6.8; no longer open. |
| [#94244](https://github.com/openclaw/openclaw/pull/94244) | Closed in local gitcrawl | fix: strip plain-text reasoning from GLM-5.x models; no longer open. |
| [#94242](https://github.com/openclaw/openclaw/issues/94242) | Closed in local gitcrawl | [Feature]: [FEAT]: Add Adorbis AI as a bundled provider plugin; no longer open. |
| [#94240](https://github.com/openclaw/openclaw/pull/94240) | Closed in local gitcrawl | fix(memory-core): degrade non-local embedding provider on persistent failure; no longer open. |
| [#94239](https://github.com/openclaw/openclaw/pull/94239) | Closed in local gitcrawl | fix(memory): align session file counter denominator with indexer filter; no longer open. |
| [#94234](https://github.com/openclaw/openclaw/pull/94234) | Closed in local gitcrawl | fix(anthropic): allow failover for thinking signature replay errors; no longer open. |
| [#94214](https://github.com/openclaw/openclaw/pull/94214) | Closed in local gitcrawl | fix(ollama): resolve thinking profile for live-discovered models; no longer open. |
| [#94210](https://github.com/openclaw/openclaw/pull/94210) | Closed in local gitcrawl | fix(cli): resolve 200K context window fallback in status command; no longer open. |
| [#94209](https://github.com/openclaw/openclaw/pull/94209) | Closed in local gitcrawl | fix(model): cap contextWindow at native runtime catalog limit when user config exceeds it; no longer open. |
| [#94184](https://github.com/openclaw/openclaw/issues/94184) | Closed in local gitcrawl | Externalised @openclaw/codex (openai-codex OAuth) provider fails to register catalog on 2026.6.x (works on 2026.5.27); no longer open. |
| [#94180](https://github.com/openclaw/openclaw/pull/94180) | Closed in local gitcrawl | feat(memory-core): allow private network endpoints for memory embeddi…; no longer open. |
| [#94165](https://github.com/openclaw/openclaw/pull/94165) | Closed in local gitcrawl | fix(control-ui): recognize namespaced reasoning tags in thinking extraction; no longer open. |
| [#94136](https://github.com/openclaw/openclaw/pull/94136) | Closed in local gitcrawl | fix(zai): expose GLM-5.2 reasoning levels [AI-assisted]; no longer open. |
| [#94135](https://github.com/openclaw/openclaw/pull/94135) | Closed in local gitcrawl | fix(memory-core): index memory path in FTS text for filename queries (fixes #94102); no longer open. |
| [#94114](https://github.com/openclaw/openclaw/pull/94114) | Closed in local gitcrawl | fix(memory-core): include path in FTS indexed text so filename tokens are searchable; no longer open. |
| [#94106](https://github.com/openclaw/openclaw/pull/94106) | Closed in local gitcrawl | fix(secrets): scope env scrub to migrated providers' vars; no longer open. |
| [#94102](https://github.com/openclaw/openclaw/issues/94102) | Closed in local gitcrawl | memory_search ranks filename/date-token queries poorly despite clean index and working content search; no longer open. |
| [#94071](https://github.com/openclaw/openclaw/pull/94071) | Closed in local gitcrawl | fix(memory-lancedb): stop forwarding embedding dimensions upstream; no longer open. |
| [#94067](https://github.com/openclaw/openclaw/pull/94067) | Closed in local gitcrawl | fix(channels): resolve native /think menu levels via runtime catalog for live-discovered models; no longer open. |
| [#94066](https://github.com/openclaw/openclaw/pull/94066) | Closed in local gitcrawl | fix(qwen): enable qwen3.6-plus on Coding Plan CN, correct reasoning flag; no longer open. |
| [#94064](https://github.com/openclaw/openclaw/pull/94064) | Closed in local gitcrawl | feat(huggingface): add text-to-image generation via hf-inference Inference Providers route; no longer open. |
| [#94062](https://github.com/openclaw/openclaw/pull/94062) | Closed in local gitcrawl | fix(agents): classify generic "LLM request failed." as transient time…; no longer open. |
| [#94038](https://github.com/openclaw/openclaw/pull/94038) | Closed in local gitcrawl | fix(matrix): recognize MiniMax mm: namespaced reasoning tags in monitor replies; no longer open. |
| [#94021](https://github.com/openclaw/openclaw/pull/94021) | Closed in local gitcrawl | fix(agents): classify local model not loaded/ready as overloaded for model fallback; no longer open. |
| [#94017](https://github.com/openclaw/openclaw/pull/94017) | Closed in local gitcrawl | fix(think): skip provider profile when model not in catalog; no longer open. |
| [#94012](https://github.com/openclaw/openclaw/pull/94012) | Closed in local gitcrawl | feat: route canonical provider models through ClawRouter; no longer open. |
| [#94011](https://github.com/openclaw/openclaw/pull/94011) | Closed in local gitcrawl | fix(cron): treat generic 'LLM request failed' error as transient server_error; no longer open. |
| [#94004](https://github.com/openclaw/openclaw/pull/94004) | Closed in local gitcrawl | refactor(sqlite): canonicalize memory and proxy storage; no longer open. |
| [#93969](https://github.com/openclaw/openclaw/pull/93969) | Closed in local gitcrawl | fix(xai): reject unsupported multi-agent model refs before runtime fallback; no longer open. |
| [#93965](https://github.com/openclaw/openclaw/pull/93965) | Closed in local gitcrawl | [Bug]: opencode-go provider streaming — API calls complete on provider side but gateway never receives stream termination signal; no longer open. |
| [#93956](https://github.com/openclaw/openclaw/pull/93956) | Closed in local gitcrawl | fix(ollama): skip auto-discovery for remote/cloud base URLs; no longer open. |
| [#93946](https://github.com/openclaw/openclaw/pull/93946) | Closed in local gitcrawl | fix(ollama): show full thinking levels for discovered reasoning models; no longer open. |
| [#93931](https://github.com/openclaw/openclaw/issues/93931) | Closed in local gitcrawl | Configured model fallbacks (payload.fallbacks) never engage on generic 'LLM request failed.' errors — fallbackUsed: false on every cron failure; no longer open. |
| [#93926](https://github.com/openclaw/openclaw/pull/93926) | Closed in local gitcrawl | fix(matrix): recognize MiniMax mm: namespaced reasoning tags in monitor suppression; no longer open. |
| [#93897](https://github.com/openclaw/openclaw/pull/93897) | Closed in local gitcrawl | fix(doctor): deep-merge openai-codex plugin entry when openai already exists; no longer open. |
| [#93891](https://github.com/openclaw/openclaw/issues/93891) | Closed in local gitcrawl | Bug: rewritePluginEntries silently drops openai-codex config when openai entry already present; no longer open. |
| [#93882](https://github.com/openclaw/openclaw/pull/93882) | Closed in local gitcrawl | fix(telegram): show full think levels for live-discovered Ollama models; no longer open. |
| [#93874](https://github.com/openclaw/openclaw/pull/93874) | Closed in local gitcrawl | fix(slack): recognize MiniMax mm: namespaced reasoning tags in monitor preview; no longer open. |
| [#93872](https://github.com/openclaw/openclaw/pull/93872) | Closed in local gitcrawl | fix(ollama): show full thinking levels for live-discovered models in /think menu; no longer open. |
| [#93864](https://github.com/openclaw/openclaw/pull/93864) | Closed in local gitcrawl | fix(ollama): show all thinking levels in /think menu for dynamically-discovered models; no longer open. |
| [#93853](https://github.com/openclaw/openclaw/pull/93853) | Closed in local gitcrawl | [AI] fix(agents): route memory embedding through generic resolution when provider has custom baseUrl; no longer open. |
| [#93844](https://github.com/openclaw/openclaw/pull/93844) | Closed in local gitcrawl | fix(ollama): resolve thinking profile for live-discovered models; no longer open. |
| [#93835](https://github.com/openclaw/openclaw/issues/93835) | Closed in local gitcrawl | [Bug]: Telegram /think menu shows only off for live-discovered Ollama thinking models, but /think <level> accepts them; no longer open. |
| [#93833](https://github.com/openclaw/openclaw/pull/93833) | Closed in local gitcrawl | fix(azure): responses model aliases route correctly; no longer open. |
| [#93832](https://github.com/openclaw/openclaw/pull/93832) | Closed in local gitcrawl | feat(providers): add ClawRouter managed proxy; no longer open. |
| [#93829](https://github.com/openclaw/openclaw/pull/93829) | Closed in local gitcrawl | fix: /status usage follows session /model override instead of stale runtime provider; no longer open. |
| [#93821](https://github.com/openclaw/openclaw/pull/93821) | Closed in local gitcrawl | fix(qmd): strip mcporter daemon startup logs from stdout before JSON.parse (fixes #59808); no longer open. |
| [#93820](https://github.com/openclaw/openclaw/pull/93820) | Closed in local gitcrawl | fix(imessage): recognize MiniMax mm: reasoning tags in reflection guard (completes #93767); no longer open. |
| [#93806](https://github.com/openclaw/openclaw/pull/93806) | Closed in local gitcrawl | fix(reasoning-tags): strip MiniMax mm: tags on silent-reply and streaming paths missed by #93767; no longer open. |
| [#93801](https://github.com/openclaw/openclaw/issues/93801) | Closed in local gitcrawl | [Feature]: Per-task model-router hook in agent dispatch (external policy command, fail-open); no longer open. |
| [#93791](https://github.com/openclaw/openclaw/pull/93791) | Closed in local gitcrawl | fix(memory): await search-sync before returning results to prevent stale index (fixes #52115); no longer open. |
| [#93789](https://github.com/openclaw/openclaw/pull/93789) | Closed in local gitcrawl | fix(agents): make lane suspension consistent across cooldown-precheck and embedded-runner paths; no longer open. |
| [#93786](https://github.com/openclaw/openclaw/pull/93786) | Closed in local gitcrawl | fix(plugins): treat refreshable catalogs as requiring runtime discovery (fixes #93775); no longer open. |
| [#93785](https://github.com/openclaw/openclaw/pull/93785) | Closed in local gitcrawl | fix(reasoning-tags): strip MiniMax `mm:` namespaced reasoning tags; no longer open. |
| [#93783](https://github.com/openclaw/openclaw/pull/93783) | Closed in local gitcrawl | fix(qmd): strip mcporter daemon startup logs from stdout before JSON.parse (fixes #59808); no longer open. |
| [#93781](https://github.com/openclaw/openclaw/issues/93781) | Closed in local gitcrawl | azure-openai-responses probe/agent route uses OpenAI auth profile instead of Azure credentials; no longer open. |
| [#93775](https://github.com/openclaw/openclaw/issues/93775) | Closed in local gitcrawl | [Bug]: Refreshable provider catalogs can skip runtime discovery; no longer open. |
| [#93774](https://github.com/openclaw/openclaw/pull/93774) | Closed in local gitcrawl | fix(codex): provision app-server model catalog metadata; no longer open. |
| [#93768](https://github.com/openclaw/openclaw/pull/93768) | Closed in local gitcrawl | [codex] Forward opt-in run context headers; no longer open. |
| [#93767](https://github.com/openclaw/openclaw/pull/93767) | Closed in local gitcrawl | fix(reasoning-tags): strip MiniMax `mm:` namespaced reasoning tags; no longer open. |
| [#93766](https://github.com/openclaw/openclaw/pull/93766) | Closed in local gitcrawl | feat: add MegaBrain provider; no longer open. |
| [#93765](https://github.com/openclaw/openclaw/issues/93765) | Closed in local gitcrawl | Codex isolated app-server homes do not receive configured custom-model catalog metadata; no longer open. |
| [#93764](https://github.com/openclaw/openclaw/issues/93764) | Closed in local gitcrawl | Codex OAuth gpt-5.5: config reports 1M/950k but native runtime caps turns at 258400; no longer open. |
| [#93759](https://github.com/openclaw/openclaw/pull/93759) | Closed in local gitcrawl | fix(minimax): surface TTS envelope errors so fallback fires (#76904) [AI]; no longer open. |
| [#93758](https://github.com/openclaw/openclaw/pull/93758) | Closed in local gitcrawl | feat(memory): apply outputDimensionality truncation to local GGUF embeddings (fixes #58765); no longer open. |
| [#93757](https://github.com/openclaw/openclaw/issues/93757) | Closed in local gitcrawl | v2026.5.28: Bedrock thinking-signature errors surface as unclassified/no-failover (fixed on main); no longer open. |
| [#93756](https://github.com/openclaw/openclaw/pull/93756) | Closed in local gitcrawl | fix(dreaming): increase narrative timeout from 60s to 120s for ARM cold-load (fixes #92494); no longer open. |
| [#93747](https://github.com/openclaw/openclaw/pull/93747) | Closed in local gitcrawl | fix(memory): await search-sync before returning results to prevent stale index (fixes #52115); no longer open. |
| [#93746](https://github.com/openclaw/openclaw/pull/93746) | Closed in local gitcrawl | fix(ui): populate realtime talk provider and transport options from talk.catalog; no longer open. |
| [#93730](https://github.com/openclaw/openclaw/pull/93730) | Closed in local gitcrawl | fix: preserve fallback chain when primary model hits rate-limit lane suspension; no longer open. |
| [#93729](https://github.com/openclaw/openclaw/pull/93729) | Closed in local gitcrawl | Preserve configured Ollama API during discovery; no longer open. |
| [#93723](https://github.com/openclaw/openclaw/pull/93723) | Closed in local gitcrawl | fix(dreaming): increase narrative timeout from 60s to 120s for ARM cold-load (fixes #92494); no longer open. |
| [#93721](https://github.com/openclaw/openclaw/pull/93721) | Closed in local gitcrawl | fix(agents): notify no-op compaction hooks; no longer open. |
| [#93710](https://github.com/openclaw/openclaw/issues/93710) | Closed in local gitcrawl | ollama plugin overrides api to native protocol ignoring config api setting; no longer open. |
| [#93708](https://github.com/openclaw/openclaw/pull/93708) | Closed in local gitcrawl | [Bug]: opencode-go provider streaming — API calls complete on provider side but gateway never receives stream termination signal; no longer open. |
| [#93688](https://github.com/openclaw/openclaw/pull/93688) | Closed in local gitcrawl | fix(minimax): check base_resp envelope errors in TTS provider; no longer open. |
| [#93683](https://github.com/openclaw/openclaw/pull/93683) | Closed in local gitcrawl | fix(memory): await search-sync before returning results to prevent stale index (fixes #52115); no longer open. |
| [#93681](https://github.com/openclaw/openclaw/pull/93681) | Closed in local gitcrawl | fix(llm): handle string assistant content on the OpenAI-compatible completion path; no longer open. |
| [#93676](https://github.com/openclaw/openclaw/pull/93676) | Closed in local gitcrawl | fix(agent-runner): retry same model on Gemini per-minute rate-limit 429s; no longer open. |
| [#93669](https://github.com/openclaw/openclaw/pull/93669) | Closed in local gitcrawl | fix(agents): classify Zhipu GLM error 1305 / 访问量过大 as overloaded for model fallback; no longer open. |
| [#93660](https://github.com/openclaw/openclaw/pull/93660) | Closed in local gitcrawl | feat(gateway): 添加 streaming 输出配置块到 HTTP 端点; no longer open. |
| [#93658](https://github.com/openclaw/openclaw/pull/93658) | Closed in local gitcrawl | fix(wizard): preserve existing default model during setup auth choice [AI-assisted]; no longer open. |
| [#93651](https://github.com/openclaw/openclaw/pull/93651) | Closed in local gitcrawl | fix(dreaming): increase narrative timeout from 60s to 120s for ARM cold-load (fixes #92494); no longer open. |
| [#93640](https://github.com/openclaw/openclaw/pull/93640) | Closed in local gitcrawl | fix: add stream stall guard for lost stream termination signal (opencode-go); no longer open. |
| [#93627](https://github.com/openclaw/openclaw/pull/93627) | Closed in local gitcrawl | fix(dreaming): filter already-emitted entries in light phase to prevent verbatim repeats (fixes #72096); no longer open. |
| [#93624](https://github.com/openclaw/openclaw/pull/93624) | Closed in local gitcrawl | feat(gateway): add configurable streaming chunk size for HTTP endpoints; no longer open. |
| [#93623](https://github.com/openclaw/openclaw/pull/93623) | Closed in local gitcrawl | fix(chat): prefer server session row over stale cache in model dropdown; no longer open. |
| [#93620](https://github.com/openclaw/openclaw/pull/93620) | Closed in local gitcrawl | [AI] fix(openai-completions): preserve reasoning_content on assistant messages for OpenRouter providers; no longer open. |
| [#93613](https://github.com/openclaw/openclaw/pull/93613) | Closed in local gitcrawl | feat(llm): forward run context to model as opt-in request headers; no longer open. |
| [#93611](https://github.com/openclaw/openclaw/pull/93611) | Closed in local gitcrawl | fix(dreaming): filter already-emitted entries in light phase to prevent verbatim repeats (fixes #72096); no longer open. |
| [#93610](https://github.com/openclaw/openclaw/issues/93610) | Closed in local gitcrawl | [Bug]: opencode-go provider streaming — API calls complete on provider side but gateway never receives stream termination signal; no longer open. |
| [#93608](https://github.com/openclaw/openclaw/pull/93608) | Closed in local gitcrawl | chore: update glm-5.2 model cost pricing for input, output, and cache; no longer open. |
| [#93602](https://github.com/openclaw/openclaw/pull/93602) | Closed in local gitcrawl | fix(memory): align session file counter denominator with indexer filter; no longer open. |
| [#93596](https://github.com/openclaw/openclaw/pull/93596) | Closed in local gitcrawl | fix(plugins): activate dreaming engine sidecar under restrictive allowlist; no longer open. |
| [#93586](https://github.com/openclaw/openclaw/pull/93586) | Closed in local gitcrawl | fix(qmd): strip XDG env vars from mcporter spawn env to fix mcporter ≥ 0.10 config resolution (fixes #79847); no longer open. |
| [#93533](https://github.com/openclaw/openclaw/pull/93533) | Closed in local gitcrawl | fix: support baseURL config for remote embedding providers; no longer open. |
| [#93523](https://github.com/openclaw/openclaw/pull/93523) | Closed in local gitcrawl | feat(ui): add model selector to cron quick-create wizard and job list; no longer open. |
| [#93508](https://github.com/openclaw/openclaw/pull/93508) | Closed in local gitcrawl | fix(session-memory): deduplicate assistant messages when thinking is stripped; no longer open. |
| [#93507](https://github.com/openclaw/openclaw/issues/93507) | Closed in local gitcrawl | [Feature]: Allow selecting cron job models and clearly displaying them in the Web UI; no longer open. |
| [#93505](https://github.com/openclaw/openclaw/pull/93505) | Closed in local gitcrawl | fix: support baseURL alias in memory embedding provider config resolution; no longer open. |
| [#93503](https://github.com/openclaw/openclaw/pull/93503) | Closed in local gitcrawl | fix(cli): resolve 200K context window fallback in status command; no longer open. |
| [#93473](https://github.com/openclaw/openclaw/pull/93473) | Closed in local gitcrawl | [codex] Fix QMD lexical memory status; no longer open. |
| [#93469](https://github.com/openclaw/openclaw/pull/93469) | Closed in local gitcrawl | fix(agents): drop partialJson streaming artifacts from session history repair; no longer open. |
| [#93452](https://github.com/openclaw/openclaw/pull/93452) | Closed in local gitcrawl | fix(bedrock): strip inference profile prefix from model ID in embedding adapter; no longer open. |
| [#93451](https://github.com/openclaw/openclaw/pull/93451) | Closed in local gitcrawl | #93436: Forward run context to the model as opt-in request headers; no longer open. |
| [#93443](https://github.com/openclaw/openclaw/pull/93443) | Closed in local gitcrawl | fix(gateway): block internal HTTP session overrides; no longer open. |
| [#93439](https://github.com/openclaw/openclaw/pull/93439) | Closed in local gitcrawl | fix(agents): honor embedded run default model; no longer open. |
| [#93430](https://github.com/openclaw/openclaw/pull/93430) | Closed in local gitcrawl | fix: honor configured default model for embedded agents; no longer open. |
| [#93428](https://github.com/openclaw/openclaw/pull/93428) | Closed in local gitcrawl | fix(agents): resolve configured default model in runEmbeddedAgent (fixes #93419); no longer open. |
| [#93426](https://github.com/openclaw/openclaw/issues/93426) | Closed in local gitcrawl | Feature request: Mimir as persistent memory backend; no longer open. |
| [#93419](https://github.com/openclaw/openclaw/issues/93419) | Closed in local gitcrawl | [Bug]: runEmbeddedAgent ignores agents.defaults.model and hardcodes openai/gpt-5.5; no longer open. |
| [#93397](https://github.com/openclaw/openclaw/pull/93397) | Closed in local gitcrawl | fix(minimax): correct volume range warning to match inclusive max; no longer open. |
| [#93394](https://github.com/openclaw/openclaw/pull/93394) | Closed in local gitcrawl | fix(memory): abort orphaned qmd search subprocess when memory_search times out; no longer open. |
| [#93393](https://github.com/openclaw/openclaw/issues/93393) | Closed in local gitcrawl | [Feature]: Model-agnostic advisor tool via api.runtime.llm.complete; no longer open. |
| [#93389](https://github.com/openclaw/openclaw/pull/93389) | Closed in local gitcrawl | fix(memory-core): clear daily-ingestion sqlite namespace on dreaming repair; no longer open. |
| [#93384](https://github.com/openclaw/openclaw/pull/93384) | Closed in local gitcrawl | fix(status): usage follows session model after switch; no longer open. |
| [#93371](https://github.com/openclaw/openclaw/pull/93371) | Closed in local gitcrawl | fix(memory): keep recalled memory out of user prompts; no longer open. |
| [#93369](https://github.com/openclaw/openclaw/pull/93369) | Closed in local gitcrawl | fix(cron): expose per-job fallbacks in CLI; no longer open. |
| [#93365](https://github.com/openclaw/openclaw/pull/93365) | Closed in local gitcrawl | fix(memory-core): EPERM fallback for atomic reindex on Windows (#78640); no longer open. |
| [#93356](https://github.com/openclaw/openclaw/pull/93356) | Closed in local gitcrawl | fix(plugins): cache plugin setup registry to kill the /models CPU storm; no longer open. |
| [#93350](https://github.com/openclaw/openclaw/pull/93350) | Closed in local gitcrawl | #93346: fix(ui): show effective runtime model in dropdown after fallback; no longer open. |
| [#93348](https://github.com/openclaw/openclaw/pull/93348) | Closed in local gitcrawl | fix(status): use selected model for usage; no longer open. |
| [#93342](https://github.com/openclaw/openclaw/pull/93342) | Closed in local gitcrawl | pipeline: normalized provider→channel stream grammar (core); no longer open. |
| [#93335](https://github.com/openclaw/openclaw/pull/93335) | Closed in local gitcrawl | fix(thinking): clamp below-range requests down to the cheapest level,…; no longer open. |
| [#93331](https://github.com/openclaw/openclaw/pull/93331) | Closed in local gitcrawl | feat(compaction): add embedded fallback models; no longer open. |
| [#93322](https://github.com/openclaw/openclaw/issues/93322) | Closed in local gitcrawl | [Bug]: /status usage should follow session-selected model after /model switch; no longer open. |
| [#93306](https://github.com/openclaw/openclaw/pull/93306) | Closed in local gitcrawl | fix(status): ignore stale context after model switch; no longer open. |
| [#93295](https://github.com/openclaw/openclaw/pull/93295) | Closed in local gitcrawl | fix(memory): swap rollback-journal sidecar during atomic reindex; no longer open. |
| [#93276](https://github.com/openclaw/openclaw/pull/93276) | Closed in local gitcrawl | fix(plugins): stop tool-discovery loads from clearing active providers; no longer open. |
| [#93275](https://github.com/openclaw/openclaw/pull/93275) | Closed in local gitcrawl | #92776: fix(agents): prevent indefinite session model pinning from polluted fallback origin; no longer open. |
| [#93268](https://github.com/openclaw/openclaw/pull/93268) | Closed in local gitcrawl | fix(status): resolve "Vector store: unknown" on memory status fast path; no longer open. |
| [#93267](https://github.com/openclaw/openclaw/pull/93267) | Closed in local gitcrawl | fix(session-memory): skip delivery-mirror entries and dedup consecutive identical assistant messages (#92563); no longer open. |
| [#93261](https://github.com/openclaw/openclaw/pull/93261) | Closed in local gitcrawl | fix(plugins): resolve provider policy surface for plugin-owned CLI backends; no longer open. |
| [#93260](https://github.com/openclaw/openclaw/pull/93260) | Closed in local gitcrawl | fix(memory): fall back to keyword search without sqlite; no longer open. |
| [#93259](https://github.com/openclaw/openclaw/issues/93259) | Closed in local gitcrawl | claude-cli subagents silently cap thinking at "high" — provider-policy surface not resolved for plugin CLI backends; no longer open. |
| [#93253](https://github.com/openclaw/openclaw/pull/93253) | Closed in local gitcrawl | fix(openai-completions): preserve reasoning replay for MiniMax M3 via OpenRouter; no longer open. |
| [#93241](https://github.com/openclaw/openclaw/pull/93241) | Closed in local gitcrawl | fix(agents): classify Zhipu GLM overload as overloaded for failover; no longer open. |
| [#93238](https://github.com/openclaw/openclaw/pull/93238) | Closed in local gitcrawl | fix(agents): honor disabled envelope timestamps at model boundary; no longer open. |
| [#93235](https://github.com/openclaw/openclaw/pull/93235) | Closed in local gitcrawl | fix(qmd): strip XDG env vars from mcporter spawn env to fix mcporter ≥ 0.10 config resolution (fixes #79847); no longer open. |
| [#93231](https://github.com/openclaw/openclaw/pull/93231) | Closed in local gitcrawl | fix(status): correct pinned model clear hint; no longer open. |
| [#93220](https://github.com/openclaw/openclaw/pull/93220) | Closed in local gitcrawl | fix(status): avoid stale session context windows; no longer open. |
| [#93215](https://github.com/openclaw/openclaw/pull/93215) | Closed in local gitcrawl | fix(memory): derive agentId from sessionKey fallback in resolveMemoryToolOptions; no longer open. |
| [#93212](https://github.com/openclaw/openclaw/pull/93212) | Closed in local gitcrawl | fix(failover): classify Zhipu (GLM) error [1305] as overloaded; no longer open. |
| [#93211](https://github.com/openclaw/openclaw/issues/93211) | Closed in local gitcrawl | Model fallback not triggered for Zhipu (GLM) error code 1305 — overloaded pattern mismatch; no longer open. |
| [#93198](https://github.com/openclaw/openclaw/pull/93198) | Closed in local gitcrawl | fix(agents): honor claude-cli contextTokens setting; no longer open. |
| [#93196](https://github.com/openclaw/openclaw/pull/93196) | Closed in local gitcrawl | fix(auth): inherit config auth.profiles when default agent store is empty; no longer open. |
| [#93192](https://github.com/openclaw/openclaw/pull/93192) | Closed in local gitcrawl | fix(dreaming): filter already-emitted entries in light phase to prevent verbatim repeats (fixes #72096); no longer open. |
| [#93187](https://github.com/openclaw/openclaw/pull/93187) | Closed in local gitcrawl | fix(memory-core): exclude archive transcripts from dreaming corpus and propagate cron parentage to subagents; no longer open. |
| [#93183](https://github.com/openclaw/openclaw/pull/93183) | Closed in local gitcrawl | [codex] Fix /btw Codex runtime side-question routing; no longer open. |
| [#93182](https://github.com/openclaw/openclaw/pull/93182) | Closed in local gitcrawl | fix(memory): clean rollback-journal reindex temp sidecar on NFS stores; no longer open. |
| [#93180](https://github.com/openclaw/openclaw/pull/93180) | Closed in local gitcrawl | fix(doctor): gate legacy Codex canonicalization on a migration plan; no longer open. |
| [#93170](https://github.com/openclaw/openclaw/pull/93170) | Closed in local gitcrawl | fix(qmd): strip XDG env vars from mcporter spawn env to fix mcporter ≥ 0.10 config resolution (fixes #79847); no longer open. |
| [#93168](https://github.com/openclaw/openclaw/pull/93168) | Closed in local gitcrawl | fix(active-memory): exclude dreaming-narrative session keys from interactive eligibility gate; no longer open. |
| [#93156](https://github.com/openclaw/openclaw/pull/93156) | Closed in local gitcrawl | fix(doctor): import default-agent auth profiles into sqlite; no longer open. |
| [#93154](https://github.com/openclaw/openclaw/issues/93154) | Closed in local gitcrawl | memory_search tool reports 'index provider settings changed' with OAuth-based OpenAI profile; no longer open. |
| [#93145](https://github.com/openclaw/openclaw/issues/93145) | Closed in local gitcrawl | Agent auth migration to SQLite leaves default agent with empty auth store (v2026.6.6); no longer open. |
| [#93136](https://github.com/openclaw/openclaw/pull/93136) | Closed in local gitcrawl | feat(attribution): parameterize OpenRouter `X-OpenRouter-Title` per deployment; no longer open. |
| [#93125](https://github.com/openclaw/openclaw/pull/93125) | Closed in local gitcrawl | feat(compaction): add compaction.fallbacks: string[] for ordered model fallback chain; no longer open. |
| [#93122](https://github.com/openclaw/openclaw/pull/93122) | Closed in local gitcrawl | #93120: feat(auth): make maxSameModelRateLimitRetries configurable; no longer open. |
| [#93113](https://github.com/openclaw/openclaw/pull/93113) | Closed in local gitcrawl | fix(memory-core): report active dreaming phases in status; no longer open. |
| [#93106](https://github.com/openclaw/openclaw/pull/93106) | Closed in local gitcrawl | docs(gateway): add cloud-orchestrator plus local-text-workers pattern; no longer open. |
| [#93097](https://github.com/openclaw/openclaw/pull/93097) | Closed in local gitcrawl | fix(qmd): strip XDG env vars from mcporter spawn env to fix mcporter ≥ 0.10 integration (fixes #79847); no longer open. |
| [#93093](https://github.com/openclaw/openclaw/pull/93093) | Closed in local gitcrawl | docs(memory): warn about session memory overlap; no longer open. |
| [#93064](https://github.com/openclaw/openclaw/pull/93064) | Closed in local gitcrawl | fix(memory): align session file counter denominator with indexer filter (fixes #77338); no longer open. |
| [#93050](https://github.com/openclaw/openclaw/issues/93050) | Closed in local gitcrawl | [Feature]: Add compaction.fallbacks: string[] for ordered model fallback chain on summarization failure; no longer open. |
| [#93039](https://github.com/openclaw/openclaw/pull/93039) | Closed in local gitcrawl | fix(dreaming): increase narrative timeout from 60s to 120s for ARM cold-load (fixes #92494); no longer open. |
| [#93036](https://github.com/openclaw/openclaw/issues/93036) | Closed in local gitcrawl | suspendSession locks entire lane, prevents fallback models from running on rate-limit; no longer open. |
| [#93017](https://github.com/openclaw/openclaw/pull/93017) | Closed in local gitcrawl | fix(agents): null-guard baseUrl in getAttributionHeaders; no longer open. |
| [#93013](https://github.com/openclaw/openclaw/pull/93013) | Closed in local gitcrawl | fix(agents): null-guard baseUrl in getAttributionHeaders; no longer open. |
| [#93011](https://github.com/openclaw/openclaw/pull/93011) | Closed in local gitcrawl | fix(gateway): accept file-only input on /v1/responses (parity with image-only); no longer open. |
| [#93008](https://github.com/openclaw/openclaw/pull/93008) | Closed in local gitcrawl | fix(dreaming): filter already-emitted entries in light phase to prevent verbatim repeats (fixes #72096); no longer open. |
| [#93005](https://github.com/openclaw/openclaw/pull/93005) | Closed in local gitcrawl | [codex] Add OpenRouter Fusion guidance and prompt context; no longer open. |
| [#93003](https://github.com/openclaw/openclaw/pull/93003) | Closed in local gitcrawl | fix(sdk): null-guard model.baseUrl in getAttributionHeaders; no longer open. |
| [#92993](https://github.com/openclaw/openclaw/pull/92993) | Closed in local gitcrawl | [codex] openai proxy compat for compatible providers; no longer open. |
| [#92991](https://github.com/openclaw/openclaw/pull/92991) | Closed in local gitcrawl | fix(agents): tolerate missing attribution baseUrl; no longer open. |
| [#92988](https://github.com/openclaw/openclaw/pull/92988) | Closed in local gitcrawl | fix(memory-core): cleanup orphaned *.sqlite.tmp-* reindex files on startup; no longer open. |
| [#92984](https://github.com/openclaw/openclaw/issues/92984) | Closed in local gitcrawl | Docs: add OpenRouter Fusion model guidance; no longer open. |
| [#92979](https://github.com/openclaw/openclaw/pull/92979) | Closed in local gitcrawl | fix(memory): show per-phase dreaming status when only light phase is enabled (fixes #67868); no longer open. |
| [#92977](https://github.com/openclaw/openclaw/pull/92977) | Closed in local gitcrawl | #92974: Bug: v2026.6.6 getAttributionHeaders() crashes on Bedrock models — baseUrl undefined (null-guard missing); no longer open. |
| [#92974](https://github.com/openclaw/openclaw/issues/92974) | Closed in local gitcrawl | Bug: v2026.6.6 getAttributionHeaders() crashes on Bedrock models — baseUrl undefined (null-guard missing); no longer open. |
| [#92972](https://github.com/openclaw/openclaw/pull/92972) | Closed in local gitcrawl | fix(memory): sweep orphaned reindex temp files; no longer open. |
| [#92968](https://github.com/openclaw/openclaw/pull/92968) | Closed in local gitcrawl | fix(status): warm context-window cache at gateway startup for correct /status on first call; no longer open. |
| [#92967](https://github.com/openclaw/openclaw/issues/92967) | Closed in local gitcrawl | fix(status): warm context-window cache at gateway startup for correct /status on first call; no longer open. |
| [#92966](https://github.com/openclaw/openclaw/pull/92966) | Closed in local gitcrawl | fix(session-memory): deduplicate consecutive assistant messages with identical text; no longer open. |
| [#92959](https://github.com/openclaw/openclaw/pull/92959) | Closed in local gitcrawl | fix(model-fallback): coalesce repeated auth-class fallback decision logs to prevent auth expiry spam (fixes #56979); no longer open. |
| [#92955](https://github.com/openclaw/openclaw/pull/92955) | Closed in local gitcrawl | fix(opencode-go): load context windows from bundled catalog; no longer open. |
| [#92954](https://github.com/openclaw/openclaw/pull/92954) | Closed in local gitcrawl | fix(memory): accept local default model path migration; no longer open. |
| [#92952](https://github.com/openclaw/openclaw/pull/92952) | Closed in local gitcrawl | fix(memory-core): sweep orphaned sqlite reindex temp files on startup (#92874); no longer open. |
| [#92943](https://github.com/openclaw/openclaw/pull/92943) | Closed in local gitcrawl | Refresh memory index state after external reindex; no longer open. |
| [#92940](https://github.com/openclaw/openclaw/pull/92940) | Closed in local gitcrawl | fix(model-fallback): throttle duplicate decision logs to prevent auth expiry spam (fixes #56979); no longer open. |
| [#92938](https://github.com/openclaw/openclaw/pull/92938) | Closed in local gitcrawl | gateway hangs at `[gateway] starting...` when a declared provider lacks credentials (regression v2026.4.8 → v2026.4.26); no longer open. |
| [#92932](https://github.com/openclaw/openclaw/pull/92932) | Closed in local gitcrawl | #92931: Bug: catalog.json caches API key in plaintext after auth migration to encrypted SQLite; no longer open. |
| [#92930](https://github.com/openclaw/openclaw/pull/92930) | Closed in local gitcrawl | fix(status): warm model context-window cache before /status reads it; no longer open. |
| [#92914](https://github.com/openclaw/openclaw/pull/92914) | Closed in local gitcrawl | fix(agents): clamp unsupported thinking for subagent spawns instead of hard-failing; no longer open. |
| [#92913](https://github.com/openclaw/openclaw/pull/92913) | Closed in local gitcrawl | fix(opencode-go): register model catalog to fix context window detection; no longer open. |
| [#92912](https://github.com/openclaw/openclaw/issues/92912) | Closed in local gitcrawl | opencode-go plugin: model contextWindow not loaded, all models fall back to 200K; no longer open. |
| [#92910](https://github.com/openclaw/openclaw/pull/92910) | Closed in local gitcrawl | fix(memory-core): safely refresh qmd index during collection repair; no longer open. |
| [#92908](https://github.com/openclaw/openclaw/pull/92908) | Closed in local gitcrawl | fix(providers): quarantine unreadable Anthropic payload tools; no longer open. |
| [#92905](https://github.com/openclaw/openclaw/pull/92905) | Closed in local gitcrawl | fix(status): warm model context-window cache before /status reads it; no longer open. |
| [#92904](https://github.com/openclaw/openclaw/pull/92904) | Closed in local gitcrawl | fix(elevenlabs): use current TTS model ids; no longer open. |
| [#92897](https://github.com/openclaw/openclaw/pull/92897) | Closed in local gitcrawl | fix(memory-wiki): tolerate public artifacts without agent ids; no longer open. |
| [#92891](https://github.com/openclaw/openclaw/pull/92891) | Closed in local gitcrawl | fix(memory): clean stale reindex temp files; no longer open. |
| [#92890](https://github.com/openclaw/openclaw/pull/92890) | Closed in local gitcrawl | fix(lmstudio): honor binary reasoning maps in completions; no longer open. |
| [#92887](https://github.com/openclaw/openclaw/pull/92887) | Closed in local gitcrawl | fix(memory): sweep stale reindex temp sqlite files; no longer open. |
| [#92885](https://github.com/openclaw/openclaw/pull/92885) | Closed in local gitcrawl | #92207 fix(memory-wiki): guard against missing agentIds in public artifacts; no longer open. |
| [#92881](https://github.com/openclaw/openclaw/pull/92881) | Closed in local gitcrawl | fix(memory): preserve reindex rollback recovery; no longer open. |
| [#92876](https://github.com/openclaw/openclaw/pull/92876) | Closed in local gitcrawl | fix(memory-wiki): stop flagging raw source pages as malformed; no longer open. |
| [#92874](https://github.com/openclaw/openclaw/issues/92874) | Closed in local gitcrawl | Builtin memory backend leaks orphaned *.sqlite.tmp-<uuid> reindex files on hard restart (no startup sweep); no longer open. |
| [#92867](https://github.com/openclaw/openclaw/pull/92867) | Closed in local gitcrawl | fix(memory-qmd): preserve Windows absolute paths in QMD command resolution; no longer open. |
| [#92864](https://github.com/openclaw/openclaw/issues/92864) | Closed in local gitcrawl | Session model override (/model) silently survives context compaction — cost $300usd  in one day; no longer open. |
| [#92863](https://github.com/openclaw/openclaw/pull/92863) | Closed in local gitcrawl | docs(logging): document exact model.usage event field names in diagnostic catalog (fixes #49046); no longer open. |
| [#92857](https://github.com/openclaw/openclaw/pull/92857) | Closed in local gitcrawl | fix(openai): drop encrypted reasoning from history for Responses-family APIs (fixes #90093); no longer open. |
| [#92854](https://github.com/openclaw/openclaw/pull/92854) | Closed in local gitcrawl | fix(hooks): reject slug-generator error payloads; no longer open. |
| [#92850](https://github.com/openclaw/openclaw/pull/92850) | Closed in local gitcrawl | fix(memory-core): reset lastMetaSerialized in runSafeReindex so a byte-identical reindex still writes __meta; no longer open. |
| [#92848](https://github.com/openclaw/openclaw/issues/92848) | Closed in local gitcrawl | Memory vector search pauses permanently when legacy index has empty `meta` (no identity backfill); no longer open. |
| [#92839](https://github.com/openclaw/openclaw/pull/92839) | Closed in local gitcrawl | fix(doctor): preserve legacy codex OAuth provider when no models are mergeable; no longer open. |
| [#92833](https://github.com/openclaw/openclaw/pull/92833) | Closed in local gitcrawl | fix(memory): search memory and wiki concurrently for corpus=all (#92633); no longer open. |
| [#92824](https://github.com/openclaw/openclaw/pull/92824) | Closed in local gitcrawl | [codex] Fix OpenAI OAuth media routing; no longer open. |
| [#92821](https://github.com/openclaw/openclaw/pull/92821) | Closed in local gitcrawl | fix(agents): use configured primary as fallback origin to prevent indefinite session pinning (#92776); no longer open. |
| [#92808](https://github.com/openclaw/openclaw/issues/92808) | Closed in local gitcrawl | [Bug]: Title: Local embedding provider breaks on upgrade (two consecutive releases) — no migration path, misleading error; no longer open. |
| [#92803](https://github.com/openclaw/openclaw/pull/92803) | Closed in local gitcrawl | fix(thinking): avoid adaptive fallback for budget requests; no longer open. |
| [#92790](https://github.com/openclaw/openclaw/pull/92790) | Closed in local gitcrawl | fix(session): clear stale auto fallback origins; no longer open. |
| [#92782](https://github.com/openclaw/openclaw/pull/92782) | Closed in local gitcrawl | fix #92688: [Bug]: Qwen vision models fail with 400 "Unexpected item type in content" on DashScope; no longer open. |
| [#92775](https://github.com/openclaw/openclaw/pull/92775) | Closed in local gitcrawl | fix(status): warm context window cache at startup for correct /status on first call; no longer open. |
| [#92773](https://github.com/openclaw/openclaw/pull/92773) | Closed in local gitcrawl 2026-06-15 | fix(tui): show resolved canonical model ref in /model confirmation; no longer open. |
| [#92770](https://github.com/openclaw/openclaw/pull/92770) | Closed in local gitcrawl | fix(media-understanding): place Qwen/DashScope image prompts in user content (#92688); no longer open. |
| [#92763](https://github.com/openclaw/openclaw/pull/92763) | Closed in local gitcrawl | fix(gateway): add google-gemini-cli image capability fallback for stale catalog rows; no longer open. |
| [#92760](https://github.com/openclaw/openclaw/issues/92760) | Closed in local gitcrawl | CLI openclaw status shows 200K context window due to standalone resolution copy in status.summary.runtime.ts; no longer open. |
| [#92759](https://github.com/openclaw/openclaw/pull/92759) | Closed in local gitcrawl | fix(memory): guard against missing agentIds in wiki artifact clone and sort; no longer open. |
| [#92745](https://github.com/openclaw/openclaw/pull/92745) | Closed in local gitcrawl | fix(memory): explain skipped short-term recall hits; no longer open. |
| [#92743](https://github.com/openclaw/openclaw/issues/92743) | Closed in local gitcrawl 2026-06-15 | [hy-memory] AutoRecall should use current user request, not full OpenClaw envelope; no longer open. |
| [#92739](https://github.com/openclaw/openclaw/pull/92739) | Closed in local gitcrawl 2026-06-15 | fix(doctor): probe memory embeddings when --deep flag is used; no longer open. |
| [#92725](https://github.com/openclaw/openclaw/pull/92725) | Closed in local gitcrawl | External reranker; no longer open. |
| [#92709](https://github.com/openclaw/openclaw/pull/92709) | Closed in local gitcrawl 2026-06-15 | fix(agents): resolve context window for proxy models with slash in ID; no longer open. |
| [#92706](https://github.com/openclaw/openclaw/issues/92706) | Closed in local gitcrawl | Dreaming deep-sleep promotes 0 — short-term recall store only populated by session-corpus ingestion (recallCount stays 0); is live memory_search supposed to feed recall?; no longer open. |
| [#92704](https://github.com/openclaw/openclaw/pull/92704) | Closed in local gitcrawl | #92688: fix(qwen): use DashScope native image format for Qwen vision models; no longer open. |
| [#92698](https://github.com/openclaw/openclaw/pull/92698) | Closed in local gitcrawl | fix #80582: Memory: skip markdown placeholder snippets during short-term promotion; no longer open. |
| [#92688](https://github.com/openclaw/openclaw/issues/92688) | Closed in local gitcrawl | [Bug]: Qwen vision models fail with 400 "Unexpected item type in content" on DashScope; no longer open. |
| [#92675](https://github.com/openclaw/openclaw/issues/92675) | Closed in local gitcrawl | GitHub Copilot recurring HTTP 401 after 2026.6.6 — incomplete SQLite auth migration leaves stale auth-profiles.json / auth-state.json; no longer open. |
| [#92665](https://github.com/openclaw/openclaw/pull/92665) | Closed in local gitcrawl | fix(llm): honor cacheRetention for LiteLLM-proxied Anthropic models; no longer open. |
| [#92663](https://github.com/openclaw/openclaw/pull/92663) | Closed in local gitcrawl | fix(dreaming): unwrap message envelope in extractNarrativeText for cron context (fixes #90292); no longer open. |
| [#92650](https://github.com/openclaw/openclaw/pull/92650) | Closed in local gitcrawl 2026-06-15 | fix #92465: split OpenAI 431 embedding batches; no longer open. |
| [#92644](https://github.com/openclaw/openclaw/pull/92644) | Closed in local gitcrawl 2026-06-15 | fix(openrouter): strip openrouter/ prefix from model IDs before API calls; no longer open. |
| [#92641](https://github.com/openclaw/openclaw/pull/92641) | Closed in local gitcrawl 2026-06-15 | fix(memory): run memory+supplement searches in parallel for corpus=all (fixes #92633); no longer open. |
| [#92639](https://github.com/openclaw/openclaw/pull/92639) | Closed in local gitcrawl 2026-06-15 | fix(memory): keep memory_search in transient qmd mode; no longer open. |
| [#92638](https://github.com/openclaw/openclaw/issues/92638) | Closed in local gitcrawl | [Bug]: Memory index meta table not populated; index --force and status --index hang; no longer open. |
| [#92632](https://github.com/openclaw/openclaw/pull/92632) | Closed in local gitcrawl | fix(memory-core): clarify memory_search tool timeouts; no longer open. |
| [#92629](https://github.com/openclaw/openclaw/issues/92629) | Closed in local gitcrawl 2026-06-15 | [Bug]: Gateway re-reads and deep-clones the entire subagent registry on every transcript-update broadcast, stalling the event loop ~4s per tool call (scales with registry size); no longer open. |
| [#92628](https://github.com/openclaw/openclaw/pull/92628) | Closed in local gitcrawl 2026-06-15 | fix #73713: surface nested embedding fetch failures; no longer open. |
| [#92627](https://github.com/openclaw/openclaw/pull/92627) | Closed in local gitcrawl 2026-06-15 | fix(openrouter): strip openrouter/ prefix from model ID in normalizeResolvedModel hook (fixes #92611); no longer open. |
| [#92624](https://github.com/openclaw/openclaw/pull/92624) | Closed in local gitcrawl | fix(memory-core): honor qmd search timeouts; no longer open. |
| [#92623](https://github.com/openclaw/openclaw/pull/92623) | Closed in local gitcrawl | fix(dreaming): increase narrative timeout from 60s to 120s for ARM devices (fixes #92494); no longer open. |
| [#92618](https://github.com/openclaw/openclaw/pull/92618) | Closed in local gitcrawl 2026-06-15 | fix #92218: memory_search tool disabled with QMD backend; no longer open. |
| [#92614](https://github.com/openclaw/openclaw/pull/92614) | Closed in local gitcrawl 2026-06-15 | fix(openrouter): strip openrouter/ prefix from model ID before API call (fixes #92611); no longer open. |
| [#92611](https://github.com/openclaw/openclaw/issues/92611) | Closed in local gitcrawl 2026-06-15 | [Bug]: OpenRouter: Anthropic models send wrong model ID to API (includes openrouter/ prefix); no longer open. |
| [#92599](https://github.com/openclaw/openclaw/issues/92599) | Closed in local gitcrawl 2026-06-15 | Model calls to a stalled provider connection hang to the job timeout — fetch timeout doesn't fire and fallback never triggers; no longer open. |
| [#92598](https://github.com/openclaw/openclaw/issues/92598) | Closed in local gitcrawl | Discord compaction still fails with provider_error_4xx after #90496 closure on 2026.6.5; no longer open. |
| [#92594](https://github.com/openclaw/openclaw/pull/92594) | Closed in local gitcrawl | [Bug]: ollama-cloud runtime fails DNS lookup for ai.ollama.com, while ollama/<model>:cloud works; no longer open. |
| [#92585](https://github.com/openclaw/openclaw/pull/92585) | Closed in local gitcrawl 2026-06-15 | fix(model-registry): skip invalid plugin catalog shards instead of aborting the whole load; no longer open. |
| [#92583](https://github.com/openclaw/openclaw/pull/92583) | Closed in local gitcrawl 2026-06-15 | fix(doctor): pass --deep flag to memory embedding probe (fixes #92582); no longer open. |
| [#92582](https://github.com/openclaw/openclaw/issues/92582) | Closed in local gitcrawl | Bug: doctor falsely warns local memory embeddings are not ready; no longer open. |
| [#92577](https://github.com/openclaw/openclaw/pull/92577) | 0 | Local memory/embedding |
| [#92575](https://github.com/openclaw/openclaw/pull/92575) | 0 | Model routing/config |
| [#92573](https://github.com/openclaw/openclaw/pull/92573) | 0 | Model routing/config |
| [#92572](https://github.com/openclaw/openclaw/issues/92572) | 0 | Model routing/config |
| [#92571](https://github.com/openclaw/openclaw/pull/92571) | 0 | Local memory/embedding |
| [#92565](https://github.com/openclaw/openclaw/pull/92565) | 0 | OpenAI-compatible/proxy |
| [#92564](https://github.com/openclaw/openclaw/pull/92564) | 0 | Model routing/config |
| [#92563](https://github.com/openclaw/openclaw/issues/92563) | 0 | Local memory/embedding |
| [#92562](https://github.com/openclaw/openclaw/issues/92562) | 0 | Model routing/config |
| [#92560](https://github.com/openclaw/openclaw/pull/92560) | Closed in local gitcrawl | fix(memory-qmd): preserve Windows absolute paths in QMD command resolution; no longer open. |
| [#92554](https://github.com/openclaw/openclaw/pull/92554) | Closed in local gitcrawl 2026-06-15 | feat(moonshot): add Kimi K2.7 Code support; no longer open. |
| [#92553](https://github.com/openclaw/openclaw/issues/92553) | Closed in local gitcrawl 2026-06-15 | ModelRegistry: a single invalid plugin catalog aborts the entire custom-models load, leaving zero models and an unlogged error; no longer open. |
| [#92544](https://github.com/openclaw/openclaw/pull/92544) | Closed in local gitcrawl | Add TrustedRouter setup docs; no longer open. |
| [#92541](https://github.com/openclaw/openclaw/pull/92541) | Closed in local gitcrawl | fix(plugins): load dreaming engine when memory slot plugin omitted from allowlist; no longer open. |
| [#92539](https://github.com/openclaw/openclaw/issues/92539) | Closed in local gitcrawl 2026-06-15 | ModelRegistry: a single invalid plugin catalog aborts the entire custom-models load, leaving zero models and an unlogged error; no longer open. |
| [#92538](https://github.com/openclaw/openclaw/pull/92538) | Closed in local gitcrawl 2026-06-15 | fix(memory): persist metadata during safe reindex; no longer open. |
| [#92536](https://github.com/openclaw/openclaw/issues/92536) | 0 | Local memory/embedding |
| [#92531](https://github.com/openclaw/openclaw/pull/92531) | 0 | Local memory/embedding |
| [#92529](https://github.com/openclaw/openclaw/pull/92529) | 0 | Model routing/config |
| [#92526](https://github.com/openclaw/openclaw/pull/92526) | 0 | Model routing/config |
| [#92524](https://github.com/openclaw/openclaw/pull/92524) | 0 | Local memory/embedding |
| [#92515](https://github.com/openclaw/openclaw/pull/92515) | 0 | Local memory/embedding |
| [#92510](https://github.com/openclaw/openclaw/pull/92510) | 0 | OpenAI-compatible/proxy |
| [#92509](https://github.com/openclaw/openclaw/pull/92509) | 0 | Local memory/embedding |
| [#92507](https://github.com/openclaw/openclaw/pull/92507) | Closed in local gitcrawl 2026-06-15 | fix(memory): persist metadata after atomic reindex; no longer open. |
| [#92505](https://github.com/openclaw/openclaw/pull/92505) | Closed in local gitcrawl | fix(gateway): validate agent roster in resolveAgentIdForRequest (fixes #92504); no longer open. |
| [#92504](https://github.com/openclaw/openclaw/issues/92504) | Closed in local gitcrawl 2026-06-15 | Gateway runs well-formed-but-unknown agent slug under agents.defaults instead of 4xx (no roster validation in resolveAgentIdForRequest; x-openclaw-agent-id header never roster-validated); no longer open. |
| [#92502](https://github.com/openclaw/openclaw/pull/92502) | Closed in local gitcrawl | Add Telegram voice STT telemetry and cron payload audit; no longer open. |
| [#92496](https://github.com/openclaw/openclaw/pull/92496) | Closed in local gitcrawl | fix(agents): set origin fields for config-driven subagent model overrides (fixes #92486); no longer open. |
| [#92495](https://github.com/openclaw/openclaw/pull/92495) | Closed in local gitcrawl | fix(opencode): restore Zen model catalog; no longer open. |
| [#92494](https://github.com/openclaw/openclaw/issues/92494) | Closed in local gitcrawl | Dreaming narrative timeout on ARM devices with many skills (600+); no longer open. |
| [#92493](https://github.com/openclaw/openclaw/pull/92493) | Closed in local gitcrawl 2026-06-15 | fix(gateway): clear provider auth prewarm on stop; no longer open. |
| [#92488](https://github.com/openclaw/openclaw/pull/92488) | Closed in local gitcrawl | fix(gateway): forward image-only input on /v1/responses (parity with chat completions); no longer open. |
| [#92486](https://github.com/openclaw/openclaw/issues/92486) | Closed in local gitcrawl | Subagent model override from agents.defaults.subagents.model is silently discarded (modelOverrideSource:"auto" matches legacy-cleanup heuristic); no longer open. |
| [#92479](https://github.com/openclaw/openclaw/issues/92479) | Closed in local gitcrawl | bug(opencode): Zen provider ships no model catalog — every Zen model must be hand-registered (opencode-go discovers, opencode does not); no longer open. |
| [#92476](https://github.com/openclaw/openclaw/pull/92476) | Closed in local gitcrawl | fix(agents): preserve compatible CLI session runtime pins; no longer open. |
| [#92466](https://github.com/openclaw/openclaw/pull/92466) | Closed in local gitcrawl | Add EvoLink provider integration; no longer open. |
| [#92465](https://github.com/openclaw/openclaw/issues/92465) | Closed in local gitcrawl 2026-06-15 | Bulk memory import can hit OpenAI 431; chunked indexing avoids it; no longer open. |
| [#92458](https://github.com/openclaw/openclaw/issues/92458) | Closed in local gitcrawl 2026-06-15 | 2026.6 openai-provider-unification migration removes openai-codex:default profile, breaking every Codex-backed agent at launch (root cause + concrete fix); no longer open. |
| [#92451](https://github.com/openclaw/openclaw/issues/92451) | Closed in local gitcrawl | v2026.6.x system prompt bloat causes instruction following degradation on smaller models; no longer open. |
| [#92447](https://github.com/openclaw/openclaw/pull/92447) | Closed in local gitcrawl 2026-06-15 | fix(memory-search): increase tool timeout from 15s to 60s; no longer open. |
| [#92446](https://github.com/openclaw/openclaw/pull/92446) | Closed in local gitcrawl | feat(cli): add --file option to image generate command (fixes #91734); no longer open. |
| [#92444](https://github.com/openclaw/openclaw/issues/92444) | Closed in local gitcrawl | Provider disabled:billing cooldown deadlocks for full 5h after credits restored — no early-clear path; no longer open. |
| [#92442](https://github.com/openclaw/openclaw/pull/92442) | Closed in local gitcrawl 2026-06-15 | fix(memory-search): increase tool timeout from 15s to 60s; no longer open. |
| [#92439](https://github.com/openclaw/openclaw/pull/92439) | Closed in local gitcrawl | fix/92327 openai responses fix; no longer open. |
| [#92437](https://github.com/openclaw/openclaw/pull/92437) | Closed in local gitcrawl | fix/92327 webchat inter session ui regression final; no longer open. |
| [#92436](https://github.com/openclaw/openclaw/pull/92436) | Closed in local gitcrawl | fix: openai-responses adapter sends system prompt in instructions; no longer open. |
| [#92431](https://github.com/openclaw/openclaw/pull/92431) | Closed in local gitcrawl | fix(agents): use thinking-level fallback for programmatic spawn instead of hard throw (fixes #92412); no longer open. |
| [#92424](https://github.com/openclaw/openclaw/pull/92424) | Closed in local gitcrawl | fix(agents): resolve fresh model from registry for post-turn reads after /model switch (fixes #92415); no longer open. |
| [#92415](https://github.com/openclaw/openclaw/issues/92415) | Closed in local gitcrawl 2026-06-15 | Session-level AgentSession.this.model snapshot is never refreshed after /model switch (affects contextWindow, reasoning, thinkingLevelMap, branch summary); no longer open. |
| [#92412](https://github.com/openclaw/openclaw/issues/92412) | Closed in local gitcrawl | BUG: sessions_spawn silently half-fails when thinking level is unsupported — fan-out spawns produce non-deterministic survivors, no signal to orchestrator (fix: symmetrize CLI-launch fallback with embedded path); no longer open. |
| [#92404](https://github.com/openclaw/openclaw/pull/92404) | Closed in local gitcrawl | fix(openai-responses): use instructions parameter for system prompt instead of input array; no longer open. |
| [#92400](https://github.com/openclaw/openclaw/issues/92400) | Closed in local gitcrawl | [Bug]: `openai-responses` adapter sends system prompt in `input` instead of `instructions`; no longer open. |
| [#92399](https://github.com/openclaw/openclaw/pull/92399) | Closed in local gitcrawl | fix(llm): collapse cumulative openai-responses message snapshots instead of concatenating [AI-assisted]; no longer open. |
| [#92396](https://github.com/openclaw/openclaw/pull/92396) | Closed in local gitcrawl 2026-06-15 | fix(moonshot): backfill reasoning_content on assistant tool-call replay messages; no longer open. |
| [#92391](https://github.com/openclaw/openclaw/issues/92391) | Closed in local gitcrawl | [Bug]: ollama-cloud runtime fails DNS lookup for ai.ollama.com, while ollama/<model>:cloud works; no longer open. |
| [#92388](https://github.com/openclaw/openclaw/pull/92388) | Closed in local gitcrawl | #92379: fix(session): refresh stale model before reading contextWindow in checkCompaction; no longer open. |
| [#92379](https://github.com/openclaw/openclaw/issues/92379) | Closed in local gitcrawl 2026-06-15 | [Bug]: Session this.model not refreshed after /model switch — auto-compaction uses stale contextWindow; no longer open. |
| [#92378](https://github.com/openclaw/openclaw/pull/92378) | Closed in local gitcrawl | fix(plugins): guard against missing agentIds in memory-wiki public artifacts (#92207); no longer open. |
| [#92375](https://github.com/openclaw/openclaw/pull/92375) | Closed in local gitcrawl | #92134: fix(memory-wiki): retry transient path-alias errors during source page write; no longer open. |
| [#92363](https://github.com/openclaw/openclaw/pull/92363) | Closed in local gitcrawl | #92224: fix(models): report local models as available in CLI list output; no longer open. |
| [#92357](https://github.com/openclaw/openclaw/pull/92357) | Closed in local gitcrawl 2026-06-15 | fix(memory): preserve keyword-only results in hybrid search when chunk IDs don't overlap (fixes #92337); no longer open. |
| [#92350](https://github.com/openclaw/openclaw/pull/92350) | Closed in local gitcrawl 2026-06-15 | [codex] Fix memory recall prompt registration; no longer open. |
| [#92337](https://github.com/openclaw/openclaw/issues/92337) | Closed in local gitcrawl | memory-core: mergeHybridResults ignores textScore when keyword/vector chunk IDs don't overlap; no longer open. |
| [#92333](https://github.com/openclaw/openclaw/issues/92333) | Closed in local gitcrawl 2026-06-15 | Bug: model.fallbacks gets wiped when desktop app switches primary model; no longer open. |
| [#92320](https://github.com/openclaw/openclaw/issues/92320) | Closed in local gitcrawl | Provider-level retry configuration for rate-limit errors (403/429); no longer open. |
| [#92308](https://github.com/openclaw/openclaw/pull/92308) | Closed in local gitcrawl 2026-06-15 | fix(memory): preserve Windows absolute paths in QMD command resolution (fixes #92302); no longer open. |
| [#92306](https://github.com/openclaw/openclaw/issues/92306) | Closed in local gitcrawl 2026-06-15 | [Bug]: cron jobs fails with "LLM request failed"; no longer open. |
| [#92302](https://github.com/openclaw/openclaw/issues/92302) | Closed in local gitcrawl | memory.qmd.command path mangled on Windows — QMD memory backend unusable despite working CLI (CommonJS path concatenation strips separators); no longer open. |
| [#92300](https://github.com/openclaw/openclaw/pull/92300) | Closed in local gitcrawl 2026-06-15 | fix(openai-responses): collapse cumulative message snapshots; no longer open. |
| [#92293](https://github.com/openclaw/openclaw/pull/92293) | Closed in local gitcrawl 2026-06-15 | Fix provider static model fallback resolution; no longer open. |
| [#92292](https://github.com/openclaw/openclaw/pull/92292) | Closed in local gitcrawl 2026-06-15 | fix(doctor): warn when resolved default model is not in the catalog (fixes #92009); no longer open. |
| [#92280](https://github.com/openclaw/openclaw/pull/92280) | Closed in local gitcrawl 2026-06-15 | fix(agents): classify structured unsupported model errors; no longer open. |
| [#92273](https://github.com/openclaw/openclaw/issues/92273) | Closed in local gitcrawl | Tool Search (mode: "tools") silently breaks the pre-compaction memory flush: model calls tool_call with a guessed name, gets an unrecoverable error, durable memories are lost; no longer open. |
| [#92271](https://github.com/openclaw/openclaw/issues/92271) | Closed in local gitcrawl | Fallback turns can re-execute work already reported as completed (semantic recursive task execution); no longer open. |
| [#92266](https://github.com/openclaw/openclaw/pull/92266) | Closed in local gitcrawl 2026-06-12 | fix(memory): report vector store ready when indexed chunks exist but probe was skipped; no longer open. |
| [#92265](https://github.com/openclaw/openclaw/pull/92265) | Closed in local gitcrawl 2026-06-15 | Fix configured DeepSeek model transport inheritance; no longer open. |
| [#92264](https://github.com/openclaw/openclaw/pull/92264) | Closed in local gitcrawl 2026-06-15 | fix(btw): resolve agentRuntime alias models in /btw side questions (fixes #92168); no longer open. |
| [#92263](https://github.com/openclaw/openclaw/pull/92263) | Closed in local gitcrawl | Fix heartbeat reasoning payload selection; no longer open. |
| [#92260](https://github.com/openclaw/openclaw/issues/92260) | Closed in local gitcrawl | [Bug]: Heartbeat delivers reasoning payload as main reply when includeReasoning is false (resolveHeartbeatReplyPayload ignores isReasoning); no longer open. |
| [#92253](https://github.com/openclaw/openclaw/pull/92253) | Closed in local gitcrawl | [codex] active-memory default to configured agents; no longer open. |
| [#92247](https://github.com/openclaw/openclaw/pull/92247) | Closed in local gitcrawl 2026-06-15 | fix(models): bound /models and models list catalog loading; no longer open. |
| [#92243](https://github.com/openclaw/openclaw/pull/92243) | Closed in local gitcrawl | feat(coreweave): add CoreWeave Serverless Inference model provider; no longer open. |
| [#92235](https://github.com/openclaw/openclaw/pull/92235) | Closed in local gitcrawl 2026-06-15 | fix: resolve managed SecretRef provider auth; no longer open. |
| [#92232](https://github.com/openclaw/openclaw/issues/92232) | Closed in local gitcrawl | [Feature]: Add CoreWeave Serverless Inference (formerly Weights & Biases) model provider; no longer open. |
| [#92228](https://github.com/openclaw/openclaw/pull/92228) | Closed in local gitcrawl 2026-06-12 | fix(cli): mark local models (Ollama) available in models list without auth; no longer open. |
| [#92226](https://github.com/openclaw/openclaw/pull/92226) | Closed in local gitcrawl 2026-06-15 | Fail closed for CLI-backed /btw fallback; no longer open. |
| [#92224](https://github.com/openclaw/openclaw/issues/92224) | Closed in local gitcrawl | Bug: CLI shows available: false for local Ollama models that are running and working; no longer open. |
| [#92218](https://github.com/openclaw/openclaw/issues/92218) | Closed in local gitcrawl 2026-06-15 | memory_search tool disabled with QMD backend; no longer open. |
| [#92208](https://github.com/openclaw/openclaw/pull/92208) | Closed in local gitcrawl 2026-06-15 | fix(model-auth): resolve secretref-managed custom provider keys from runtime config snapshot; no longer open. |
| [#92200](https://github.com/openclaw/openclaw/pull/92200) | Closed in local gitcrawl | fix(openai-completions): fallback to compat.reasoningEffortMap when thinkingLevelMap is unset (fixes #91913); no longer open. |
| [#92192](https://github.com/openclaw/openclaw/pull/92192) | Closed in local gitcrawl 2026-06-12 | fix(model-auth): resolve secretref-managed custom provider keys from runtime config snapshot; no longer open. |
| [#92191](https://github.com/openclaw/openclaw/pull/92191) | Closed in local gitcrawl | fix(agents): retry thinking-only errored turns; no longer open. |
| [#92187](https://github.com/openclaw/openclaw/issues/92187) | Closed in local gitcrawl | Memory Index Repeatedly Broken After Gateway Restart (OOM during Rebuild); no longer open. |
| [#92181](https://github.com/openclaw/openclaw/pull/92181) | Closed in local gitcrawl 2026-06-15 | fix(agents): align /btw model resolution with runtime aliases; no longer open. |
| [#92177](https://github.com/openclaw/openclaw/pull/92177) | Closed in local gitcrawl 2026-06-15 | fix(agents): treat NO_REPLY-only turns as silent regardless of silence flag (#92038); no longer open. |
| [#92176](https://github.com/openclaw/openclaw/pull/92176) | Closed in local gitcrawl | fix(media-understanding): resolve image model input from catalog, preserve explicit text-only (#92104); no longer open. |
| [#92174](https://github.com/openclaw/openclaw/pull/92174) | Closed in local gitcrawl | feat(aigateway): add AIgateway as a bundled model provider; no longer open. |
| [#92168](https://github.com/openclaw/openclaw/issues/92168) | Closed in local gitcrawl 2026-06-15 | [Bug]: /btw fails with "Unknown model" for anthropic/* aliases routed via agentRuntime: claude-cli (resolver path divergence from main agent loop); no longer open. |
| [#92166](https://github.com/openclaw/openclaw/pull/92166) | Closed in local gitcrawl 2026-06-12 | fix(media-understanding): resolve image model input from catalog, preserve explicit text-only (#92104); no longer open. |
| [#92165](https://github.com/openclaw/openclaw/pull/92165) | Closed in local gitcrawl | fix(memory): show dreaming status without search; no longer open. |
| [#92164](https://github.com/openclaw/openclaw/pull/92164) | Closed in local gitcrawl | fix(memory-core): score CJK keyword search instead of textScore=0 with trigram FTS5; no longer open. |
| [#92159](https://github.com/openclaw/openclaw/pull/92159) | Closed in local gitcrawl 2026-06-12 | fix(media-understanding): resolve image model input from bundled catalog for inline providers (#92104); no longer open. |
| [#92148](https://github.com/openclaw/openclaw/issues/92148) | Closed in local gitcrawl 2026-06-15 | [Bug]: 2026.6.5 routes DeepSeek (custom OpenAI-compatible provider) to the OpenAI Responses API → 401, now affecting non-reasoning deepseek-v4-pro; no longer open. |
| [#92147](https://github.com/openclaw/openclaw/pull/92147) | Closed in local gitcrawl | [codex] support Responses system prompts in instructions; no longer open. |
| [#92145](https://github.com/openclaw/openclaw/pull/92145) | Closed in local gitcrawl 2026-06-12 | fix(model-auth): resolve secretref-managed apiKey from runtime config snapshot (#92097); no longer open. |
| [#92135](https://github.com/openclaw/openclaw/pull/92135) | Closed in local gitcrawl | fix(openai-embedding): preserve openai/ prefix for non-native base URLs; no longer open. |
| [#92133](https://github.com/openclaw/openclaw/pull/92133) | Closed in local gitcrawl 2026-06-15 | fix(agents): handle "Not supported model" error format in isModelNotFoundErrorMessage; no longer open. |
| [#92131](https://github.com/openclaw/openclaw/pull/92131) | Closed in local gitcrawl 2026-06-15 | [codex] fix(agents): detect not supported model errors; no longer open. |
| [#92127](https://github.com/openclaw/openclaw/pull/92127) | Closed in local gitcrawl 2026-06-12 | fix(plugins): stop derived metadata snapshot rescan storm in /models (regression shipped since v2026.5.18); no longer open. |
| [#92124](https://github.com/openclaw/openclaw/issues/92124) | Closed in local gitcrawl | Memory search breaks with Requesty/OpenAI embedding model prefix mismatch; no longer open. |
| [#92121](https://github.com/openclaw/openclaw/pull/92121) | Closed in local gitcrawl 2026-06-12 | [AI] fix(memory): eliminate absent-window race in index swap + prevent auto-create empty DB; no longer open. |
| [#92118](https://github.com/openclaw/openclaw/issues/92118) | Closed in local gitcrawl 2026-06-15 | isModelNotFoundErrorMessage does not match "Not supported model" error format; no longer open. |
| [#92117](https://github.com/openclaw/openclaw/issues/92117) | Closed in local gitcrawl | Flaky / failing: simple-completion-runtime > can preserve asynchronous provider model discovery (introduced 25ca39e876); no longer open. |
| [#92113](https://github.com/openclaw/openclaw/pull/92113) | Closed in local gitcrawl 2026-06-15 | fix(auth): resolve custom provider secretref-managed apiKey from runtime snapshot; no longer open. |
| [#92104](https://github.com/openclaw/openclaw/issues/92104) | Closed in local gitcrawl 2026-06-15 | image/pdf tool: 'Unknown model' for every provider, while the same models work as agent models (2026.5.28 and 2026.6.5); no longer open. |
| [#92099](https://github.com/openclaw/openclaw/pull/92099) | Closed in local gitcrawl | feat(active-memory): add messageMaxChars config to cap latest user message in message mode; no longer open. |
| [#92097](https://github.com/openclaw/openclaw/issues/92097) | Closed in local gitcrawl 2026-06-15 | [Bug] Custom providers with secretref-managed apiKey fail with 503 auth_unavailable after update to 2026.6.5; no longer open. |
| [#92079](https://github.com/openclaw/openclaw/pull/92079) | Closed in local gitcrawl | [AI] fix(memory): auto-fix providerKey mismatch from CLI index --force; no longer open. |
| [#92072](https://github.com/openclaw/openclaw/pull/92072) | Closed in local gitcrawl | fix(gateway): treat `google-gemini-cli` Gemini models as image-capable; no longer open. |
| [#92071](https://github.com/openclaw/openclaw/pull/92071) | Closed in local gitcrawl 2026-06-12 | fix(anthropic): resolve thinking profile for custom Anthropic-compatible providers; no longer open. |
| [#92065](https://github.com/openclaw/openclaw/pull/92065) | Closed in local gitcrawl | fix(memory): honor configured qmd search timeouts; no longer open. |
| [#92061](https://github.com/openclaw/openclaw/issues/92061) | Closed in local gitcrawl | memory-core: CJK text FTS5 search returns textScore=0 with trigram tokenizer; no longer open. |
| [#92057](https://github.com/openclaw/openclaw/issues/92057) | Closed in local gitcrawl | Gateway becomes slow or times out under multi-session / multi-agent load; no longer open. |
| [#92054](https://github.com/openclaw/openclaw/issues/92054) | Closed in local gitcrawl | [Bug]: Windows 11 - Claude CLI provider fails with spawn claude ENOENT; no longer open. |
| [#92053](https://github.com/openclaw/openclaw/pull/92053) | Closed in local gitcrawl 2026-06-12 | fix(thinking): apply Claude profile to anthropic-messages catalog rows; no longer open. |
| [#92050](https://github.com/openclaw/openclaw/issues/92050) | Closed in local gitcrawl 2026-06-15 | memory-core: short-term-recall.json grows without rotation → permanent dreaming promotion deadlock once it crosses the 16MiB read limit; no longer open. |
| [#92038](https://github.com/openclaw/openclaw/issues/92038) | Closed in local gitcrawl 2026-06-12 | NO_REPLY silence reply counted as empty turn - retry + candidate_failed(format) + full fallback cascade on heartbeats (2026.6.5); no longer open. |
| [#92034](https://github.com/openclaw/openclaw/pull/92034) | Closed in local gitcrawl 2026-06-12 | perf(agents): memoize XML attribute regex in DSML stream parser; no longer open. |
| [#92020](https://github.com/openclaw/openclaw/pull/92020) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): check SQLite plugin state for dreaming ingestion audit after JSON migration (fixes #92017); no longer open. |
| [#92019](https://github.com/openclaw/openclaw/issues/92019) | Closed in local gitcrawl 2026-06-15 | anthropic-messages replay: preserved thinking-block signatures hard-fail (400 Invalid signature) on proxied endpoints / model-switch; no longer open. |
| [#92018](https://github.com/openclaw/openclaw/issues/92018) | Closed in local gitcrawl 2026-06-12 | [Bug]: Builtin semantic memory index loses memory_index_meta_v1 after live memory_search; no longer open. |
| [#92017](https://github.com/openclaw/openclaw/issues/92017) | Closed in local gitcrawl 2026-06-12 | [Bug]: memory status reports "ingestion state absent" after dreaming JSON→SQLite migration; no longer open. |
| [#92012](https://github.com/openclaw/openclaw/pull/92012) | Closed in local gitcrawl | docs(providers): add LLMBase setup guide; no longer open. |
| [#92011](https://github.com/openclaw/openclaw/pull/92011) | Closed in local gitcrawl | fix(agents): prevent recursive task execution during model fallback; no longer open. |
| [#92010](https://github.com/openclaw/openclaw/issues/92010) | Closed in local gitcrawl 2026-06-15 | [Feature]: Add CloudSigma TaaS as a model provider (OpenAI-compatible multi-model gateway); no longer open. |
| [#92009](https://github.com/openclaw/openclaw/issues/92009) | Closed in local gitcrawl 2026-06-15 | [Bug]: Resolved default model google/gemini-3.1-pro-preview cannot be inspected or executed in 2026.6.5; no longer open. |
| [#92002](https://github.com/openclaw/openclaw/pull/92002) | Closed in local gitcrawl | fix(lmstudio): deliver thinking "off" to binary-thinking models; no longer open. |
| [#91999](https://github.com/openclaw/openclaw/issues/91999) | Closed in local gitcrawl | Bug: Main agent model reverts to Gemini in terminal sessions; no longer open. |
| [#91982](https://github.com/openclaw/openclaw/issues/91982) | Closed in local gitcrawl 2026-06-15 | [Bug]: anthropic-vertex-provider adds cache_control to active-memory system block — triggers "Found 5" error when active-memory is enabled; no longer open. |
| [#91975](https://github.com/openclaw/openclaw/issues/91975) | Closed in local gitcrawl 2026-06-12 | Native Anthropic adapter silently drops `thinking` to `off` for custom provider ids (resolveThinkingProfile only matches exact `anthropic`/`claude-cli`); no longer open. |
| [#91971](https://github.com/openclaw/openclaw/issues/91971) | Closed in local gitcrawl | [Bug]: @openclaw/llama-cpp-provider documented but not published to npm/ClawHub; no longer open. |
| [#91965](https://github.com/openclaw/openclaw/issues/91965) | Closed in local gitcrawl 2026-06-15 | [Bug]: memory_search permanently fails with "index metadata is missing" — cached indexIdentityState not refreshed after meta fix; no longer open. |
| [#91961](https://github.com/openclaw/openclaw/issues/91961) | Closed in local gitcrawl 2026-06-15 | Memory status shows 'paused' after index rebuild despite vector search working (v2026.6.5); no longer open. |
| [#91959](https://github.com/openclaw/openclaw/issues/91959) | Closed in local gitcrawl | Bedrock Mantle (openai-responses) cumulatively duplicates reply text with reasoning enabled (GPT-5.x); no longer open. |
| [#91958](https://github.com/openclaw/openclaw/pull/91958) | Closed in local gitcrawl | fix(memory): align memory_search tool deadline with configured QMD timeout (fixes #91947); no longer open. |
| [#91956](https://github.com/openclaw/openclaw/issues/91956) | Closed in local gitcrawl | bug: 飞书流式回复重复显示思考过程和工具调用信息; no longer open. |
| [#91953](https://github.com/openclaw/openclaw/issues/91953) | Closed in local gitcrawl | [Bug]: empty-error-retry skipped when stop_reason="error" turn contains a thinking block or non-zero output, causing silent mid-turn abort on multi-step tasks; no longer open. |
| [#91949](https://github.com/openclaw/openclaw/issues/91949) | Closed in local gitcrawl | invalid_request_error from Anthropic kills session instead of triggering fallback; no longer open. |
| [#91947](https://github.com/openclaw/openclaw/issues/91947) | Closed in local gitcrawl | memory_search 工具硬编码 15s timeout 不够 qmd query 跑完，建议可配置; no longer open. |
| [#91942](https://github.com/openclaw/openclaw/issues/91942) | Closed in local gitcrawl 2026-06-15 | [Bug] l1-extractor 临时 workspace 上下文注入缺失，LLM 返回空字符串; no longer open. |
| [#91930](https://github.com/openclaw/openclaw/issues/91930) | Closed in local gitcrawl 2026-06-15 | Docs feedback: /providers/opencode; no longer open. |
| [#91929](https://github.com/openclaw/openclaw/issues/91929) | Closed in local gitcrawl | [Bug]: model provider config custom proxy url, image generation error; no longer open. |
| [#91928](https://github.com/openclaw/openclaw/issues/91928) | Closed in local gitcrawl | DeepSeek 模型在长上下文中注意力偏移（attention inertia）—— 倾向回应上一轮而非最新消息; no longer open. |
| [#91913](https://github.com/openclaw/openclaw/issues/91913) | Closed in local gitcrawl | openai-completions legacy path drops `compat.reasoningEffortMap` and `thinkLevel`; LM Studio binary-thinking models silently fall back to thinking-on; no longer open. |
| [#91912](https://github.com/openclaw/openclaw/issues/91912) | Closed in local gitcrawl 2026-06-15 | Feature request: per-session suppressFallbackNotice config option; no longer open. |
| [#91911](https://github.com/openclaw/openclaw/pull/91911) | Closed in local gitcrawl 2026-06-12 | fix(agents): retry same model across short rate-limit windows; no longer open. |
| [#91902](https://github.com/openclaw/openclaw/issues/91902) | Closed in local gitcrawl | [BUG] memory index --force CLI writes incompatible meta providerKey, breaks runtime memory_search; no longer open. |
| [#91897](https://github.com/openclaw/openclaw/pull/91897) | Closed in local gitcrawl 2026-06-12 | fix(memory): self-heal missing index identity by initializing provider during sync; no longer open. |
| [#91895](https://github.com/openclaw/openclaw/pull/91895) | Closed in local gitcrawl 2026-06-12 | fix(webchat): finalize provider failure lifecycle; no longer open. |
| [#91884](https://github.com/openclaw/openclaw/pull/91884) | Closed in local gitcrawl 2026-06-12 | fix(memory): keep QMD background refreshes armed; no longer open. |
| [#91882](https://github.com/openclaw/openclaw/pull/91882) | Closed in local gitcrawl 2026-06-12 | feat(anthropic): support Claude Fable 5 adaptive thinking; no longer open. |
| [#91881](https://github.com/openclaw/openclaw/issues/91881) | Closed in local gitcrawl | v2026.6.5 - DeepSeek 401 auth error después de actualizar; no longer open. |
| [#91875](https://github.com/openclaw/openclaw/pull/91875) | Closed in local gitcrawl | fix(github-copilot): claude-opus-4.8 context window to 1M with reasoning support; no longer open. |
| [#91870](https://github.com/openclaw/openclaw/pull/91870) | Closed in local gitcrawl | fix(github-copilot): claude-opus-4.8 is native 1M context + thinking (not 128K); no longer open. |
| [#91869](https://github.com/openclaw/openclaw/issues/91869) | Closed in local gitcrawl | GitHub Copilot: claude-opus-4.8 hard-coded to 128K context (native 1M) + missing thinking support; no longer open. |
| [#91864](https://github.com/openclaw/openclaw/pull/91864) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): force exit after memory search --json output; no longer open. |
| [#91862](https://github.com/openclaw/openclaw/pull/91862) | Closed in local gitcrawl | fix(memory): gracefully degrade when embedding provider is unregistered; no longer open. |
| [#91854](https://github.com/openclaw/openclaw/issues/91854) | Closed in local gitcrawl | [Bug]: Memory dreaming narrative/REM lane is given apply_patch and misuses it; no longer open. |
| [#91839](https://github.com/openclaw/openclaw/issues/91839) | Closed in local gitcrawl | [Bug]: Terminal provider model_not_available in subagent announce path can trigger chat.history storm and gateway event-loop starvation; no longer open. |
| [#91837](https://github.com/openclaw/openclaw/pull/91837) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): settle json search cleanup; no longer open. |
| [#91830](https://github.com/openclaw/openclaw/pull/91830) | Closed in local gitcrawl 2026-06-12 | feat: add OpenRouter OAuth to onboarding; no longer open. |
| [#91827](https://github.com/openclaw/openclaw/issues/91827) | Closed in local gitcrawl 2026-06-15 | [P1] Structural fix: content-based dedup + delivery-mirror model-hiding for kimi-code message loops; no longer open. |
| [#91821](https://github.com/openclaw/openclaw/issues/91821) | Closed in local gitcrawl 2026-06-12 | memory search --json prints results but does not exit with QMD backend; no longer open. |
| [#91813](https://github.com/openclaw/openclaw/pull/91813) | Closed in local gitcrawl 2026-06-12 | fix(codex): restore memory recall from plugin tools; no longer open. |
| [#91809](https://github.com/openclaw/openclaw/issues/91809) | Closed in local gitcrawl 2026-06-15 | [Performance] /models command slow in v2026.6.1 — catalog loading regression; no longer open. |
| [#91796](https://github.com/openclaw/openclaw/pull/91796) | Closed in local gitcrawl 2026-06-15 | fix(anthropic): add Claude Haiku 4.5 to static model catalog; no longer open. |
| [#91790](https://github.com/openclaw/openclaw/pull/91790) | Closed in local gitcrawl 2026-06-12 | fix(gateway): add google-gemini-cli image capability shim (fixes #91739); no longer open. |
| [#91778](https://github.com/openclaw/openclaw/issues/91778) | Closed in local gitcrawl 2026-06-15 | [P0] memory_search cassé — index metadata is missing depuis v2026.6.1, reproduit sur v2026.6.5; no longer open. |
| [#91767](https://github.com/openclaw/openclaw/pull/91767) | Closed in local gitcrawl | Fix one-shot Codex app-server teardown; no longer open. |
| [#91742](https://github.com/openclaw/openclaw/pull/91742) | Closed in local gitcrawl 2026-06-12 | fix(memory): abort orphaned embedding work when memory_search times out; no longer open. |
| [#91740](https://github.com/openclaw/openclaw/pull/91740) | Closed in local gitcrawl 2026-06-12 | fix(auth): verify SQLite auth migration before cleanup; no longer open. |
| [#91730](https://github.com/openclaw/openclaw/issues/91730) | Closed in local gitcrawl 2026-06-12 | [Bug]: OpenClaw-native provider failure leaves web chat session stuck in progress; no longer open. |
| [#91728](https://github.com/openclaw/openclaw/pull/91728) | Closed in local gitcrawl | test(github-copilot): cover live xhigh reasoning for non-Claude mini models (#59416); no longer open. |
| [#91724](https://github.com/openclaw/openclaw/pull/91724) | Closed in local gitcrawl | fix(agents): infer runtime provider from qualified model ids; no longer open. |
| [#91720](https://github.com/openclaw/openclaw/pull/91720) | Closed in local gitcrawl 2026-06-12 | :bug: fix(openai): remove chatgpt-responses transport override from gpt-5.3-codex catalog entry; no longer open. |
| [#91718](https://github.com/openclaw/openclaw/issues/91718) | Closed in local gitcrawl 2026-06-12 | memory_search tool-level timeout orphans background embedding work; no longer open. |
| [#91714](https://github.com/openclaw/openclaw/pull/91714) | Closed in local gitcrawl | fix(agents): apply Gemini schema cleaning for Gemini models via OpenAI-compat providers; no longer open. |
| [#91711](https://github.com/openclaw/openclaw/pull/91711) | Closed in local gitcrawl 2026-06-12 | :bug: fix(agents): classify harness provider mismatch as format error (#91710); no longer open. |
| [#91710](https://github.com/openclaw/openclaw/issues/91710) | Closed in local gitcrawl 2026-06-12 | [Bug]: v2026.6.1 regression: openai/gpt-5.3-codex silently falls back to Sonnet — Codex harness rejects "openai" provider due to stale npm plugin; no longer open. |
| [#91708](https://github.com/openclaw/openclaw/pull/91708) | Closed in local gitcrawl 2026-06-12 | fix(agents): preserve legacy openai-codex context overrides after provider unification (fixes #90448); no longer open. |
| [#91706](https://github.com/openclaw/openclaw/pull/91706) | Closed in local gitcrawl | fix(memory): keep local embedding indexes clean when only local.modelPath is set; no longer open. |
| [#91696](https://github.com/openclaw/openclaw/pull/91696) | Closed in local gitcrawl 2026-06-12 | fix(agents): preserve reasoning_content replay for Gemma 4 openai-completions models; no longer open. |
| [#91691](https://github.com/openclaw/openclaw/pull/91691) | Closed in local gitcrawl | [AI] fix(memory): prevent empty-string expectedModel in resolveMemory…; no longer open. |
| [#91660](https://github.com/openclaw/openclaw/pull/91660) | Closed in local gitcrawl | [AI] fix(memory): backfill provider.model with resolved model name in…; no longer open. |
| [#91657](https://github.com/openclaw/openclaw/pull/91657) | Closed in local gitcrawl 2026-06-12 | fix(ollama): use provider thinking default in SDK session factory; no longer open. |
| [#91651](https://github.com/openclaw/openclaw/issues/91651) | Closed in local gitcrawl 2026-06-12 | bug(tools): web_fetch fails with 'Invalid URL' when LLM generates a space in the protocol scheme; no longer open. |
| [#91645](https://github.com/openclaw/openclaw/issues/91645) | Closed in local gitcrawl 2026-06-12 | [Bug]: In-turn reasoning dropped on multi-turn tool replay for non-400 openai models (gemma4/vLLM) — silent agentic-quality regression; no longer open. |
| [#91644](https://github.com/openclaw/openclaw/pull/91644) | Closed in local gitcrawl | feat(gateway): add OpenAI-compatible /v1/audio/speech endpoint; no longer open. |
| [#91640](https://github.com/openclaw/openclaw/pull/91640) | Closed in local gitcrawl | docs(compaction): warn that compaction.model breaks native compaction on claude-cli/OAuth; no longer open. |
| [#91634](https://github.com/openclaw/openclaw/issues/91634) | Closed in local gitcrawl 2026-06-15 | memory-tdai: ByteString encoding fails on fullwidth ellipsis (U+2026) in vec indexer; no longer open. |
| [#91625](https://github.com/openclaw/openclaw/pull/91625) | Closed in local gitcrawl | fix(cron): add cron edit --clear-model to clear a job's model override; no longer open. |
| [#91622](https://github.com/openclaw/openclaw/issues/91622) | Closed in local gitcrawl | gpt-5.4-mini via Responses API: incomplete turn false positive + claude eager_input_streaming schema rejection; no longer open. |
| [#91596](https://github.com/openclaw/openclaw/pull/91596) | Closed in local gitcrawl | fix(memory): use local modelPath for status identity so custom local models aren't always dirty (fixes #91001); no longer open. |
| [#91592](https://github.com/openclaw/openclaw/issues/91592) | Closed in local gitcrawl | memory_search broken with "index scope changed" after --force rebuild — scopeHash mismatch persists; no longer open. |
| [#91589](https://github.com/openclaw/openclaw/pull/91589) | Closed in local gitcrawl 2026-06-11 | Harden external CLI auth sync diagnostics; no longer open. |
| [#91580](https://github.com/openclaw/openclaw/pull/91580) | Closed in local gitcrawl 2026-06-11 | fix(agents): trim dense text delta snapshots; no longer open. |
| [#91579](https://github.com/openclaw/openclaw/pull/91579) | Closed in local gitcrawl 2026-06-11 | fix(agents): bootstrap OpenClaw auth for codex harness when provider is codex; no longer open. |
| [#91575](https://github.com/openclaw/openclaw/issues/91575) | Closed in local gitcrawl 2026-06-15 | [Feature]: Feature Request: Pre-request budget/cost check to prevent runaway spending on free tier accounts; no longer open. |
| [#91567](https://github.com/openclaw/openclaw/pull/91567) | Closed in local gitcrawl 2026-06-11 | fix(openai): require api-key auth for realtime voice; no longer open. |
| [#91560](https://github.com/openclaw/openclaw/issues/91560) | Closed in local gitcrawl 2026-06-15 | [Bug]: Codex ACP native route fails with "Authentication required" when host Codex uses OAuth (ChatGPT login); no longer open. |
| [#91559](https://github.com/openclaw/openclaw/pull/91559) | Closed in local gitcrawl | fix(agents): clean Gemini tool schemas by model id; no longer open. |
| [#91552](https://github.com/openclaw/openclaw/issues/91552) | Closed in local gitcrawl | Codex app-server binding sidecar can retain stale GPT model across provider switches, causing embedded runs to dispatch zai/gpt-5.5; no longer open. |
| [#91546](https://github.com/openclaw/openclaw/pull/91546) | Closed in local gitcrawl | fix: add gemini-3.5-flash to the Google provider catalog; no longer open. |
| [#91542](https://github.com/openclaw/openclaw/issues/91542) | Closed in local gitcrawl | [Bug] Gemini (jjcc/openai-compat) rejects cron tool schema: anyOf properties missing type field in v2026.6.1; no longer open. |
| [#91538](https://github.com/openclaw/openclaw/pull/91538) | Closed in local gitcrawl 2026-06-11 | perf(control-ui): avoid startup catalog wait; no longer open. |
| [#91537](https://github.com/openclaw/openclaw/issues/91537) | Closed in local gitcrawl | [Bug]: Codex yolo mode leaks app-server processes and binding files; no longer open. |
| [#91531](https://github.com/openclaw/openclaw/pull/91531) | Closed in local gitcrawl 2026-06-11 | perf(control-ui): reuse startup model metadata; no longer open. |
| [#91513](https://github.com/openclaw/openclaw/issues/91513) | Closed in local gitcrawl 2026-06-11 | ACP: model prefix not stripped when dispatching to Claude ACP adapter — Cannot replay saved model "anthropic/claude-sonnet-4-6"; no longer open. |
| [#91459](https://github.com/openclaw/openclaw/pull/91459) | Closed in local gitcrawl | fix(memory-wiki): include workspace in bridge artifact hash to prevent collisions; no longer open. |
| [#91444](https://github.com/openclaw/openclaw/pull/91444) | Closed in local gitcrawl | fix(google): register 'google' alias for memory embedding provider; no longer open. |
| [#91430](https://github.com/openclaw/openclaw/pull/91430) | Closed in local gitcrawl 2026-06-11 | fix(openai): honor configured embedding model input limits; no longer open. |
| [#91428](https://github.com/openclaw/openclaw/issues/91428) | Closed in local gitcrawl 2026-06-12 | Gemma4/Qwen3.6 via local Ollama: only first token/word? rendered, while Ollama streams clean content-only output; no longer open. |
| [#91427](https://github.com/openclaw/openclaw/pull/91427) | Closed in local gitcrawl | fix(openai-completions): reject provider empty stop replies; no longer open. |
| [#91425](https://github.com/openclaw/openclaw/pull/91425) | Closed in local gitcrawl 2026-06-11 | fix(memory-lancedb): guard memory recall output [AI]; no longer open. |
| [#91421](https://github.com/openclaw/openclaw/pull/91421) | Closed in local gitcrawl 2026-06-11 | fix(cron): clear payload model overrides; no longer open. |
| [#91414](https://github.com/openclaw/openclaw/pull/91414) | Closed in local gitcrawl | fix(agent): agents.defaults.model.fallbacks not inherited by isolated cron sessions; no longer open. |
| [#91405](https://github.com/openclaw/openclaw/pull/91405) | Closed in local gitcrawl 2026-06-11 | fix(cli): thread silent-empty policy to CLI runner to stop duplicate group reply (fixes #91302); no longer open. |
| [#91403](https://github.com/openclaw/openclaw/pull/91403) | Closed in local gitcrawl | fix(openai-completions): route empty stop with no content into error path; no longer open. |
| [#91397](https://github.com/openclaw/openclaw/pull/91397) | Closed in local gitcrawl | feat(neosantara): add Neosantara gateway provider and responses API alias; no longer open. |
| [#91395](https://github.com/openclaw/openclaw/pull/91395) | Closed in local gitcrawl 2026-06-11 | fix(cron): inherit default model fallbacks for plain-string agent models (fixes #91362); no longer open. |
| [#91388](https://github.com/openclaw/openclaw/pull/91388) | Closed in local gitcrawl 2026-06-11 | [codex] Fix Claude tool-only empty response fallback; no longer open. |
| [#91387](https://github.com/openclaw/openclaw/pull/91387) | Closed in local gitcrawl 2026-06-11 | fix(cron): clear payload model overrides; no longer open. |
| [#91380](https://github.com/openclaw/openclaw/pull/91380) | Closed in local gitcrawl 2026-06-11 | fix(cron): inherit default fallbacks for cron string models; no longer open. |
| [#91379](https://github.com/openclaw/openclaw/pull/91379) | Closed in local gitcrawl 2026-06-11 | fix(cron): inherit default fallbacks for string agent jobs; no longer open. |
| [#91373](https://github.com/openclaw/openclaw/pull/91373) | Closed in local gitcrawl 2026-06-11 | fix(agent): string model configs inherit default fallbacks for cron sessions; no longer open. |
| [#91360](https://github.com/openclaw/openclaw/pull/91360) | Closed in local gitcrawl 2026-06-11 | fix(cron): allow clearing payload.model via update (fixes #91298); no longer open. |
| [#91352](https://github.com/openclaw/openclaw/issues/91352) | Closed in local gitcrawl | [Bug]: OpenAI Codex OAuth migration leaves stale default profile and codexPlugins app inventory can fail Codex harness; no longer open. |
| [#91351](https://github.com/openclaw/openclaw/pull/91351) | Closed in local gitcrawl 2026-06-12 | fix(opencode-go): add qwen plus tiered pricing; no longer open. |
| [#91338](https://github.com/openclaw/openclaw/pull/91338) | Closed in local gitcrawl 2026-06-11 | fix(cron): allow payload.model and other optional fields to be cleared via null in update API; no longer open. |
| [#91329](https://github.com/openclaw/openclaw/pull/91329) | Closed in local gitcrawl 2026-06-11 | fix(reply): pass silent-empty policy to CLI fallback runs; no longer open. |
| [#91324](https://github.com/openclaw/openclaw/pull/91324) | Closed in local gitcrawl 2026-06-11 | fix(memory): move local llama.cpp runtime to provider plugin; no longer open. |
| [#91323](https://github.com/openclaw/openclaw/pull/91323) | Closed in local gitcrawl | fix(gateway): keep dense stream updates incremental and preserve replacement stream deltas; no longer open. |
| [#91319](https://github.com/openclaw/openclaw/pull/91319) | Closed in local gitcrawl 2026-06-11 | Fix CLI silent reply fallback policy; no longer open. |
| [#91318](https://github.com/openclaw/openclaw/pull/91318) | Closed in local gitcrawl 2026-06-11 | fix(cron): allow update patches to clear payload.model back to inherit; no longer open. |
| [#91313](https://github.com/openclaw/openclaw/pull/91313) | Closed in local gitcrawl 2026-06-11 | fix(cron): allow null model/fallbacks in payload patch to clear overrides (fixes #91298); no longer open. |
| [#91310](https://github.com/openclaw/openclaw/pull/91310) | Closed in local gitcrawl | fix(memory): resolve embedding provider by authProviderId fallback; no longer open. |
| [#91308](https://github.com/openclaw/openclaw/pull/91308) | Closed in local gitcrawl | feat(xai): add realtime voice provider; no longer open. |
| [#91299](https://github.com/openclaw/openclaw/pull/91299) | Closed in local gitcrawl 2026-06-15 | fix(memory-core): write ## Deep Sleep summary into DREAMS.md after deep dreaming sweep; no longer open. |
| [#91297](https://github.com/openclaw/openclaw/pull/91297) | Closed in local gitcrawl 2026-06-11 | fix(memory): rebind qmd collection when root path drifts despite list missing path (#91251); no longer open. |
| [#91292](https://github.com/openclaw/openclaw/pull/91292) | Closed in local gitcrawl 2026-06-12 | fix(models): keep bundled provider catalog when configured base URL is blank (#91270); no longer open. |
| [#91275](https://github.com/openclaw/openclaw/pull/91275) | Closed in local gitcrawl 2026-06-11 | fix(memory-qmd): enrich collection list with path from 'qmd collection show' so rebind detects changed roots; no longer open. |
| [#91274](https://github.com/openclaw/openclaw/pull/91274) | Closed in local gitcrawl | refactor(memory): drop redundant agent-id scoping from qmd collection names; no longer open. |
| [#91270](https://github.com/openclaw/openclaw/issues/91270) | Closed in local gitcrawl 2026-06-12 | [Bug]: Gemini can't resolve on embedded runtime; no longer open. |
| [#91267](https://github.com/openclaw/openclaw/pull/91267) | Closed in local gitcrawl | fix(memory-core): skip session archive artifacts during dreaming corpus collection (fixes #90313); no longer open. |
| [#91265](https://github.com/openclaw/openclaw/pull/91265) | Closed in local gitcrawl 2026-06-15 | fix(memory): drop redundant agent-id scoping from QMD collection names; no longer open. |
| [#91260](https://github.com/openclaw/openclaw/issues/91260) | Closed in local gitcrawl 2026-06-11 | opencode-go: bundled models from provider-catalog.ts (glm-5, glm-5.1, kimi-k2.5, mimo-v2.5-pro, minimax-m2.5, minimax-m2.7, qwen3.5-plus) are silently dropped at runtime — only 5 of 12 surface; no longer open. |
| [#91255](https://github.com/openclaw/openclaw/pull/91255) | Closed in local gitcrawl 2026-06-11 | fix(memory-core): enrich collection paths from qmd collection show to enable rebind (fixes #91251); no longer open. |
| [#91253](https://github.com/openclaw/openclaw/pull/91253) | Closed in local gitcrawl 2026-06-11 | fix(memory): rebind qmd collections when a collection root changes; no longer open. |
| [#91251](https://github.com/openclaw/openclaw/issues/91251) | Closed in local gitcrawl 2026-06-11 | memory(qmd): collections never rebind when a collection's root path changes; no longer open. |
| [#91239](https://github.com/openclaw/openclaw/pull/91239) | Closed in local gitcrawl | fix(opencode-go): complete catalog, onboarding, and tiered pricing; no longer open. |
| [#91238](https://github.com/openclaw/openclaw/issues/91238) | Closed in local gitcrawl 2026-06-12 | opencode-go provider: qwen3.7-max, qwen3.7-plus, minimax-m3 missing from static model catalog → "Unknown model" (model_not_found); no longer open. |
| [#91231](https://github.com/openclaw/openclaw/pull/91231) | Closed in local gitcrawl 2026-06-11 | fix(anthropic): drop reasoning_content replay signatures; no longer open. |
| [#91227](https://github.com/openclaw/openclaw/pull/91227) | Closed in local gitcrawl 2026-06-15 | fix #91216: [Bug]: gateway opens an empty memory database when main.sqlite is absent during the index swap, leaving memory_search paused with "index metadata is missing" until restart; no longer open. |
| [#91225](https://github.com/openclaw/openclaw/pull/91225) | Closed in local gitcrawl | fix #83830: [Bug]: Dreaming diary repeats "first day" narrative every sweep — same early memories dominate snippets; no longer open. |
| [#91218](https://github.com/openclaw/openclaw/pull/91218) | Closed in local gitcrawl 2026-06-15 | fix(google): strip provider prefix from Vertex model path; no longer open. |
| [#91216](https://github.com/openclaw/openclaw/issues/91216) | Closed in local gitcrawl 2026-06-12 | [Bug]: gateway opens an empty memory database when main.sqlite is absent during the index swap, leaving memory_search paused with "index metadata is missing" until restart; no longer open. |
| [#91214](https://github.com/openclaw/openclaw/issues/91214) | Closed in local gitcrawl | [Bug]: Active memory injection breaks prompt_cache_key for OpenAI-compatible providers (compat.supportsPromptCacheKey=true); no longer open. |
| [#91206](https://github.com/openclaw/openclaw/pull/91206) | Closed in local gitcrawl | fix(agents/subagent-spawn): pass resolved model to gateway agent call; no longer open. |
| [#91205](https://github.com/openclaw/openclaw/issues/91205) | Closed in local gitcrawl 2026-06-11 | Cross-provider thinking block signature poisoning bricks sessions when switching between non-Anthropic and Anthropic models; no longer open. |
| [#91188](https://github.com/openclaw/openclaw/pull/91188) | Closed in local gitcrawl 2026-06-11 | fix(memory-core): write ## Deep Sleep summary to DREAMS.md; no longer open. |
| [#91187](https://github.com/openclaw/openclaw/pull/91187) | Closed in local gitcrawl | fix(cron): isolate auth profile failure policy so cron runs don't pollute shared cooldowns; no longer open. |
| [#91183](https://github.com/openclaw/openclaw/issues/91183) | Closed in local gitcrawl | [Bug]: memorySearch index metadata lost after upgrade to 2026.6.5-beta.2, vector search paused despite 2272 cache entries; no longer open. |
| [#91182](https://github.com/openclaw/openclaw/pull/91182) | Closed in local gitcrawl | fix(memory-core): exclude archive transcripts from dreaming session corpus collection; no longer open. |
| [#91177](https://github.com/openclaw/openclaw/pull/91177) | Closed in local gitcrawl | fix(tui): persist canonical provider in session modelProvider; no longer open. |
| [#91175](https://github.com/openclaw/openclaw/pull/91175) | Closed in local gitcrawl 2026-06-11 | fix(memory-core): write Deep Sleep summary into DREAMS.md after deep dreaming phase (fixes #91051); no longer open. |
| [#91173](https://github.com/openclaw/openclaw/pull/91173) | Closed in local gitcrawl 2026-06-12 | fix(memory): self-heal missing index identity during sync; no longer open. |
| [#91170](https://github.com/openclaw/openclaw/pull/91170) | Closed in local gitcrawl | fix(memory): align local modelPath index identity on status; no longer open. |
| [#91168](https://github.com/openclaw/openclaw/pull/91168) | Closed in local gitcrawl | feat(tui,gateway): show CLI-routing label in /model picker; no longer open. |
| [#91167](https://github.com/openclaw/openclaw/issues/91167) | Closed in local gitcrawl | bug(memory): gateway cannot self-heal a missing index identity when chunks are already indexed; no longer open. |
| [#91154](https://github.com/openclaw/openclaw/issues/91154) | Closed in local gitcrawl | memory-wiki: wiki.palace fails with (path-mismatch) and wiki.importInsights takes 100s+ under load; no longer open. |
| [#91153](https://github.com/openclaw/openclaw/pull/91153) | Closed in local gitcrawl 2026-06-12 | fix(agents): resolve model aliases in compaction model override (fixes #90340); no longer open. |
| [#91118](https://github.com/openclaw/openclaw/pull/91118) | Closed in local gitcrawl 2026-06-11 | fix: preserve Foundry Responses reasoning replay ids; no longer open. |
| [#91113](https://github.com/openclaw/openclaw/pull/91113) | Closed in local gitcrawl 2026-06-11 | fix: align Xiaomi completions replay compat; no longer open. |
| [#91112](https://github.com/openclaw/openclaw/pull/91112) | Closed in local gitcrawl 2026-06-11 | fix(openai-completions): add Xiaomi endpoint detection to detectCompat (fixes #91106); no longer open. |
| [#91111](https://github.com/openclaw/openclaw/pull/91111) | Closed in local gitcrawl 2026-06-11 | fix(media-understanding): preserve native vision skip with imageModel…; no longer open. |
| [#91109](https://github.com/openclaw/openclaw/pull/91109) | Closed in local gitcrawl 2026-06-11 | fix(openai-completions): add Xiaomi to detectCompat requiresReasoningContentOnAssistantMessages; no longer open. |
| [#91106](https://github.com/openclaw/openclaw/issues/91106) | Closed in local gitcrawl 2026-06-11 | [Bug]: detectCompat in openai-completions.ts misses Xiaomi endpoints for requiresReasoningContentOnAssistantMessages — diverges from openai-completions-compat.ts; no longer open. |
| [#91094](https://github.com/openclaw/openclaw/pull/91094) | Closed in local gitcrawl 2026-06-11 | fix(media-understanding): skip image understanding when primary model supports vision, regardless of imageModel config (fixes #91084); no longer open. |
| [#91084](https://github.com/openclaw/openclaw/issues/91084) | Closed in local gitcrawl 2026-06-11 | [Bug]: vision-skip guard bypassed when agents.defaults.imageModel is set, even with vision-capable primary model; no longer open. |
| [#91081](https://github.com/openclaw/openclaw/pull/91081) | Closed in local gitcrawl 2026-06-12 | perf(memory): coalesce + cache session-file listings to cut NFS READDIR load; no longer open. |
| [#91077](https://github.com/openclaw/openclaw/issues/91077) | Closed in local gitcrawl | [Bug] cacheRetention has no effect on Discord direct-message sessions; subagent/cron/channel sessions cache normally; no longer open. |
| [#91073](https://github.com/openclaw/openclaw/pull/91073) | Closed in local gitcrawl 2026-06-11 | fix(openrouter): reconcile streamed generation cost; no longer open. |
| [#91072](https://github.com/openclaw/openclaw/pull/91072) | Closed in local gitcrawl 2026-06-11 | refactor(memory-wiki): store source sync state in sqlite; no longer open. |
| [#91071](https://github.com/openclaw/openclaw/pull/91071) | Closed in local gitcrawl 2026-06-11 | fix(memory-core): write Deep Sleep summary to DREAMS.md with managed markers; no longer open. |
| [#91068](https://github.com/openclaw/openclaw/pull/91068) | Closed in local gitcrawl 2026-06-11 | Refactor core fetch paths off guarded fetch; no longer open. |
| [#91063](https://github.com/openclaw/openclaw/pull/91063) | Closed in local gitcrawl | fix(memory): write deep summaries into DREAMS.md; no longer open. |
| [#91060](https://github.com/openclaw/openclaw/issues/91060) | Closed in local gitcrawl 2026-06-15 | Feature Request: Per-task or Per-capability Model Routing; no longer open. |
| [#91057](https://github.com/openclaw/openclaw/pull/91057) | Closed in local gitcrawl | fix(sessions): prune stale gateway model-run sessions; no longer open. |
| [#91050](https://github.com/openclaw/openclaw/pull/91050) | Closed in local gitcrawl | fix(active-memory): keep a runnable iMessage channel so memory thread key builds; no longer open. |
| [#91046](https://github.com/openclaw/openclaw/pull/91046) | Closed in local gitcrawl 2026-06-11 | fix(microsoft-foundry): exclude alias providers from DeepSeek V4 thinking wrapper (fixes #90520); no longer open. |
| [#91045](https://github.com/openclaw/openclaw/pull/91045) | Closed in local gitcrawl 2026-06-11 | fix(config): accept model thinkingLevelMap in provider config schema (#91011) [AI-assisted]; no longer open. |
| [#91037](https://github.com/openclaw/openclaw/pull/91037) | Closed in local gitcrawl 2026-06-11 | fix(config): allow thinkingLevelMap in persisted model schema; no longer open. |
| [#91033](https://github.com/openclaw/openclaw/issues/91033) | Closed in local gitcrawl 2026-06-11 | [Bug]: microsoft-foundry reasoning models return 400 invalid_encrypted_content when continuing a thread; no longer open. |
| [#91031](https://github.com/openclaw/openclaw/pull/91031) | Closed in local gitcrawl 2026-06-12 | [codex] Add OpenRouter OAuth login; no longer open. |
| [#91018](https://github.com/openclaw/openclaw/issues/91018) | Closed in local gitcrawl 2026-06-15 | ⚠️ Upgrade 2026.6.1 broke DeepSeek prompt cache - $6 burned in one hour; no longer open. |
| [#91016](https://github.com/openclaw/openclaw/issues/91016) | Closed in local gitcrawl | ⚠️ 升级 2026.6.1 后 DeepSeek Prompt Cache 完全失效，一小时烧掉约 $6; no longer open. |
| [#91011](https://github.com/openclaw/openclaw/issues/91011) | Closed in local gitcrawl 2026-06-11 | [Bug]: Foundry Entra ID onboarding fails to save with "Unrecognized key: thinkingLevelMap"; no longer open. |
| [#91010](https://github.com/openclaw/openclaw/pull/91010) | Closed in local gitcrawl | fix(memory): honor local model path in index identity; no longer open. |
| [#91008](https://github.com/openclaw/openclaw/pull/91008) | Closed in local gitcrawl 2026-06-11 | fix: address P2 cleanup items in model picker UI (PR #68927); no longer open. |
| [#91001](https://github.com/openclaw/openclaw/issues/91001) | Closed in local gitcrawl | [Bug]: local embeedings provider fail; no longer open. |
| [#90991](https://github.com/openclaw/openclaw/issues/90991) | Closed in local gitcrawl | Cron scheduled trigger contaminates global runtime state causing transient system-wide overload failures; no longer open. |
| [#90990](https://github.com/openclaw/openclaw/pull/90990) | Closed in local gitcrawl | fix(agents): use appropriate log levels in model-resolver fallback paths; no longer open. |
| [#90982](https://github.com/openclaw/openclaw/issues/90982) | Closed in local gitcrawl | [Bug]: TUI hides tool-call validation errors behind "run aborted" — root cause only visible in gateway log; no longer open. |
| [#90959](https://github.com/openclaw/openclaw/pull/90959) | Closed in local gitcrawl 2026-06-15 | fix(agents): apply default provider catalog timeout in all environments; no longer open. |
| [#90925](https://github.com/openclaw/openclaw/issues/90925) | Closed in local gitcrawl | [Bug]: Subagent announce compaction for Codex/OAuth falls into openai-responses API-key route; no longer open. |
| [#90908](https://github.com/openclaw/openclaw/pull/90908) | Closed in local gitcrawl | fix(model-fallback): don't rethrow provider-side AbortErrors as user cancellations; no longer open. |
| [#90904](https://github.com/openclaw/openclaw/pull/90904) | Closed in local gitcrawl 2026-06-11 | fix(doctor): match short-term memory files with -HHMM timestamp suffixes; no longer open. |
| [#90896](https://github.com/openclaw/openclaw/issues/90896) | Closed in local gitcrawl 2026-06-07 | Bug: isShortTermMemoryPath regex skips daily memory files with timestamp suffixes (e.g. YYYY-MM-DD-HHMM.md); no longer open. |
| [#90889](https://github.com/openclaw/openclaw/pull/90889) | Closed in local gitcrawl | fix: cap session context overrides by model window; no longer open. |
| [#90886](https://github.com/openclaw/openclaw/issues/90886) | Closed in local gitcrawl | gateway hangs at `[gateway] starting...` when a declared provider lacks credentials (regression v2026.4.8 → v2026.4.26); no longer open. |
| [#90885](https://github.com/openclaw/openclaw/pull/90885) | Closed in local gitcrawl | fix(agent): resolve compaction model alias to canonical model ref; no longer open. |
| [#90884](https://github.com/openclaw/openclaw/pull/90884) | Closed in local gitcrawl 2026-06-11 | fix(agent): exclude Microsoft Foundry alias providers from DeepSeek V4 thinking wrapper; no longer open. |
| [#90881](https://github.com/openclaw/openclaw/issues/90881) | Closed in local gitcrawl | doctor --fix migrates codex/gpt-5.5 to openai/gpt-5.5, then Codex app-server startup times out on 2026.6.1; no longer open. |
| [#90878](https://github.com/openclaw/openclaw/issues/90878) | Closed in local gitcrawl 2026-06-07 | OAuth Codex profile falls back after openai-codex to openai namespace mismatch; no longer open. |
| [#90877](https://github.com/openclaw/openclaw/issues/90877) | Closed in local gitcrawl 2026-06-07 | Issue on memory-lancedb; no longer open. |
| [#90876](https://github.com/openclaw/openclaw/pull/90876) | Closed in local gitcrawl | docs: add ForAI provider setup guide; no longer open. |
| [#90870](https://github.com/openclaw/openclaw/pull/90870) | Closed in local gitcrawl | [AI] fix(memory-wiki): index wiki pages in query-dir subfolders; no longer open. |
| [#90869](https://github.com/openclaw/openclaw/issues/90869) | Closed in local gitcrawl | wiki_search silently drops pages in subfolders of the wiki query dirs (data loss); no longer open. |
| [#90863](https://github.com/openclaw/openclaw/pull/90863) | Closed in local gitcrawl 2026-06-11 | fix(minimax): expose xhigh and max thinking levels for MiniMax-M3; no longer open. |
| [#90839](https://github.com/openclaw/openclaw/pull/90839) | Closed in local gitcrawl | fix(memory-core): exclude soft-deleted .jsonl.deleted paths from dreaming corpus (#90466); no longer open. |
| [#90830](https://github.com/openclaw/openclaw/pull/90830) | Closed in local gitcrawl 2026-06-11 | fix(microsoft-foundry): suppress DeepSeek V4 thinking on alias provider ids (#90520); no longer open. |
| [#90826](https://github.com/openclaw/openclaw/pull/90826) | Closed in local gitcrawl | fix(tui): render /models loading feedback before listing resolves (#90720); no longer open. |
| [#90825](https://github.com/openclaw/openclaw/pull/90825) | Closed in local gitcrawl 2026-06-12 | fix(llm): warn on unknown model pricing; no longer open. |
| [#90811](https://github.com/openclaw/openclaw/pull/90811) | Closed in local gitcrawl 2026-06-11 | fix(agents): stabilize user-turn serialization across turns to preserve prompt cache; no longer open. |
| [#90810](https://github.com/openclaw/openclaw/issues/90810) | Closed in local gitcrawl 2026-06-07 | [Bug]: Prompt cache invalidated on every user turn on full-resend transports — transient timestamp + content-form decoration on the current user message (regression from #3658); no longer open. |
| [#90799](https://github.com/openclaw/openclaw/pull/90799) | Closed in local gitcrawl | fix: handle Claude CLI synthetic placeholders; no longer open. |
| [#90793](https://github.com/openclaw/openclaw/pull/90793) | Closed in local gitcrawl 2026-06-11 | Fix OpenAI audio auth to use API keys; no longer open. |
| [#90761](https://github.com/openclaw/openclaw/pull/90761) | Closed in local gitcrawl | fix(android): resolve UI bugs and add SSH tunnelling; no longer open. |
| [#90758](https://github.com/openclaw/openclaw/issues/90758) | Closed in local gitcrawl 2026-06-06 | Channel-level agentId for iMessage, WhatsApp, and Telegram DMs (escape-hatch routing); no longer open. |
| [#90748](https://github.com/openclaw/openclaw/pull/90748) | Closed in local gitcrawl 2026-06-11 | fix(memory): resolve adapter default model in plain status identity check; no longer open. |
| [#90741](https://github.com/openclaw/openclaw/pull/90741) | Closed in local gitcrawl | perf(models-config): unify auth-profile fingerprint cache + targetProvider short-circuit; no longer open. |
| [#90739](https://github.com/openclaw/openclaw/pull/90739) | Closed in local gitcrawl | fix(active-memory): preserve verbose recall summaries; no longer open. |
| [#90731](https://github.com/openclaw/openclaw/pull/90731) | Closed in local gitcrawl | fix(agents): hydrate allowlisted dynamic model metadata; no longer open. |
| [#90727](https://github.com/openclaw/openclaw/pull/90727) | Closed in local gitcrawl | fix(memory): refresh rebuilt index handles; no longer open. |
| [#90726](https://github.com/openclaw/openclaw/issues/90726) | Closed in local gitcrawl 2026-06-06 | [Bug] Cron jobs terminate immediately on HTTP 500 errors without triggering configured fallback mechanism / Cron 任务在遇到 HTTP 500 错误时直接中止，未能触发配置的 Fallback 机制; no longer open. |
| [#90717](https://github.com/openclaw/openclaw/pull/90717) | Closed in local gitcrawl 2026-06-06 | fix(agents): re-probe single-provider primary during cooldown; no longer open. |
| [#90706](https://github.com/openclaw/openclaw/pull/90706) | Closed in local gitcrawl 2026-06-15 | fix(OpenAI Responses): disable item id replay for storeless providers; no longer open. |
| [#90705](https://github.com/openclaw/openclaw/pull/90705) | Closed in local gitcrawl 2026-06-11 | fix(llm): preserve streamed tool args when Responses done omits arguments; no longer open. |
| [#90702](https://github.com/openclaw/openclaw/issues/90702) | Closed in local gitcrawl 2026-06-06 | [Bug]: blockedUntil for subscription_limit set far in the future never re-probes when no fallback is configured; no longer open. |
| [#90686](https://github.com/openclaw/openclaw/pull/90686) | Closed in local gitcrawl 2026-06-15 | fix(gateway): honor profile auth for SecretRef model entries; no longer open. |
| [#90685](https://github.com/openclaw/openclaw/issues/90685) | Closed in local gitcrawl 2026-06-15 | models.list marks auth-profile-backed SecretRef providers unavailable; no longer open. |
| [#90683](https://github.com/openclaw/openclaw/pull/90683) | Closed in local gitcrawl | fix: retry safe post-tool continuation turns; no longer open. |
| [#90675](https://github.com/openclaw/openclaw/issues/90675) | Closed in local gitcrawl | [Bug]: Dashboard/agent fake tool calls with dmxapi model; native claude route returns incomplete terminal response; no longer open. |
| [#90657](https://github.com/openclaw/openclaw/issues/90657) | Closed in local gitcrawl 2026-06-11 | tracking(OpenAI Responses): reproduce storeless replay and strict state/stream regressions in GitHub Actions; no longer open. |
| [#90642](https://github.com/openclaw/openclaw/issues/90642) | Closed in local gitcrawl | [Feature]: Gemma4-12b (and other models) audio not supported yet; no longer open. |
| [#90613](https://github.com/openclaw/openclaw/pull/90613) | Closed in local gitcrawl 2026-06-06 | fix(agents): propagate ADC credential marker so google-vertex passes isWritableProviderConfig; no longer open. |
| [#90609](https://github.com/openclaw/openclaw/pull/90609) | Closed in local gitcrawl 2026-06-11 | fix(google): preserve Vertex ADC catalog auth; no longer open. |
| [#90594](https://github.com/openclaw/openclaw/pull/90594) | Closed in local gitcrawl 2026-06-06 | fix(android): align provider readiness with available models; no longer open. |
| [#90593](https://github.com/openclaw/openclaw/pull/90593) | Closed in local gitcrawl 2026-06-11 | fix: preserve LM Studio Responses tool arguments; no longer open. |
| [#90585](https://github.com/openclaw/openclaw/issues/90585) | Closed in local gitcrawl 2026-06-11 | [Bug]: [REGRESSION] Tool calls with arguments arrive as empty objects when using LM Studio (openai-responses API).; no longer open. |
| [#90574](https://github.com/openclaw/openclaw/pull/90574) | Closed in local gitcrawl | fix(openai): omit gpt-5.5 tool reasoning effort; no longer open. |
| [#90570](https://github.com/openclaw/openclaw/issues/90570) | Closed in local gitcrawl 2026-06-11 | Azure AI Foundry models (/openai/v1/responses) fail with 400 Invalid value and 400 schema mismatch across all GPT-5.x deployments; no longer open. |
| [#90567](https://github.com/openclaw/openclaw/issues/90567) | Closed in local gitcrawl 2026-06-15 | Bug: pdf tool fails with 401 on xiaomi token-plan provider; no longer open. |
| [#90539](https://github.com/openclaw/openclaw/pull/90539) | Closed in local gitcrawl 2026-06-06 | fix(agents): skip foundry aliases for deepseek thinking; no longer open. |
| [#90538](https://github.com/openclaw/openclaw/issues/90538) | Closed in local gitcrawl 2026-06-06 | [Bug] Memory Dreaming Promotion silently no-ops: cron isolated sessions get trigger=user instead of cron; no longer open. |
| [#90533](https://github.com/openclaw/openclaw/pull/90533) | Closed in local gitcrawl 2026-06-06 | fix(openai): accept missing content-type on ChatGPT Responses SSE stream; no longer open. |
| [#90528](https://github.com/openclaw/openclaw/issues/90528) | Closed in local gitcrawl | [Bug]: OpenAI/Codex OAuth Profile Not Attached to Inference Requests; no longer open. |
| [#90520](https://github.com/openclaw/openclaw/issues/90520) | Closed in local gitcrawl 2026-06-11 | Microsoft Foundry DeepSeek V4 alias providers still inject `thinking` after #87737 fix; no longer open. |
| [#90513](https://github.com/openclaw/openclaw/pull/90513) | Closed in local gitcrawl 2026-06-15 | fix(anthropic): add haiku catalog entry; no longer open. |
| [#90507](https://github.com/openclaw/openclaw/pull/90507) | Closed in local gitcrawl 2026-06-11 | fix(doctor): preserve codex context metadata; no longer open. |
| [#90506](https://github.com/openclaw/openclaw/issues/90506) | Closed in local gitcrawl 2026-06-06 | [Bug]: [Bug]: google-vertex models fail with model_not_found at runtime on 2026.5.28 and 2026.6.1 — direct Vertex API calls succeed with same credentials; no longer open. |
| [#90496](https://github.com/openclaw/openclaw/issues/90496) | Closed in local gitcrawl 2026-06-12 | Discord channel remains trapped in oversized session after /new; compaction fails provider_error_4xx and model drifts from codex/gpt-5.5 to gpt-5.4; no longer open. |
| [#90466](https://github.com/openclaw/openclaw/issues/90466) | Closed in local gitcrawl | [Bug]:memory-core dreaming on 2026.6.1: session-corpus contains .jsonl.deleted.* paths; narrative phase writes fallback despite valid prose responses; no longer open. |
| [#90465](https://github.com/openclaw/openclaw/issues/90465) | Closed in local gitcrawl | Auto-discover models for the generic openai-completions provider from /v1/models; no longer open. |
| [#90462](https://github.com/openclaw/openclaw/issues/90462) | Closed in local gitcrawl | Fallback provider can become pinned in session metadata and trap a chat on unavailable LM Studio model; no longer open. |
| [#90457](https://github.com/openclaw/openclaw/pull/90457) | Closed in local gitcrawl 2026-06-11 | fix(models): persist agent catalog cache; no longer open. |
| [#90454](https://github.com/openclaw/openclaw/issues/90454) | Closed in local gitcrawl | active-memory plugin discards verbose sub-agent responses as status=unavailable, surface_error reason=none; no longer open. |
| [#90451](https://github.com/openclaw/openclaw/pull/90451) | Closed in local gitcrawl | fix(doctor): consolidate legacy Codex migration cleanup; no longer open. |
| [#90447](https://github.com/openclaw/openclaw/pull/90447) | Closed in local gitcrawl | fix(memory-core): resolve adapter default model for index identity state; no longer open. |
| [#90436](https://github.com/openclaw/openclaw/pull/90436) | Closed in local gitcrawl 2026-06-06 | Add NVIDIA Nemotron 3 Ultra default; no longer open. |
| [#90433](https://github.com/openclaw/openclaw/pull/90433) | Closed in local gitcrawl | fix(memory-core): exclude archived transcripts from Dreaming session corpus; no longer open. |
| [#90429](https://github.com/openclaw/openclaw/pull/90429) | Closed in local gitcrawl 2026-06-11 | Fix LM Studio wizard prompter binding; no longer open. |
| [#90425](https://github.com/openclaw/openclaw/pull/90425) | Closed in local gitcrawl 2026-06-06 | fix(openai): preserve encrypted reasoning replay ids; no longer open. |
| [#90422](https://github.com/openclaw/openclaw/pull/90422) | Closed in local gitcrawl 2026-06-06 | fix(memory-core): keep durable index identity visible during safe reindex; no longer open. |
| [#90420](https://github.com/openclaw/openclaw/issues/90420) | Closed in local gitcrawl | Codex runtime route is hard to verify after the 2026.6.1 openai-codex migration; no longer open. |
| [#90413](https://github.com/openclaw/openclaw/issues/90413) | Closed in local gitcrawl 2026-06-07 | memory status always reports "Vector search: paused" with blank expected model (2026.6.1); no longer open. |
| [#90407](https://github.com/openclaw/openclaw/pull/90407) | Closed in local gitcrawl | fix(memory-lancedb): align apache arrow peer dependency; no longer open. |
| [#90403](https://github.com/openclaw/openclaw/issues/90403) | Closed in local gitcrawl 2026-06-15 | [Performance] Model Picker UI very slow in v2026.5.28; no longer open. |
| [#90399](https://github.com/openclaw/openclaw/pull/90399) | Closed in local gitcrawl 2026-06-06 | fix(openai): accept missing content-type on ChatGPT Responses SSE stream; no longer open. |
| [#90397](https://github.com/openclaw/openclaw/pull/90397) | Closed in local gitcrawl | fix(openai): skip unreadable responses tool schemas; no longer open. |
| [#90395](https://github.com/openclaw/openclaw/pull/90395) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): write meta after sync when identity is missing with existing chunks; no longer open. |
| [#90383](https://github.com/openclaw/openclaw/pull/90383) | Closed in local gitcrawl | fix(ollama): skip unreadable tool schemas; no longer open. |
| [#90382](https://github.com/openclaw/openclaw/issues/90382) | Closed in local gitcrawl 2026-06-06 | [Bug]: ChatGPT-OAuth gpt-5.5 fails with invalid_provider_content_type after 2026.6.1 (SDK Responses stream missing Accept: text/event-stream); no longer open. |
| [#90372](https://github.com/openclaw/openclaw/issues/90372) | Closed in local gitcrawl | [Bug]: Ollama cloud model received a 14M-token prompt before OpenClaw detected context overflow; no longer open. |
| [#90368](https://github.com/openclaw/openclaw/issues/90368) | Closed in local gitcrawl 2026-06-15 | 2026.6.1: agent_model_catalogs / model_capability_cache tables defined but never written; models list takes 25–53s; no longer open. |
| [#90357](https://github.com/openclaw/openclaw/pull/90357) | Closed in local gitcrawl | fix(agents): resolve compaction model alias before dispatch; no longer open. |
| [#90342](https://github.com/openclaw/openclaw/issues/90342) | Closed in local gitcrawl | Feature: Model Cookbook — hardware-aware model recommendations with one-click download/serve; no longer open. |
| [#90340](https://github.com/openclaw/openclaw/issues/90340) | Closed in local gitcrawl | [Bug]: Auto-compaction does not resolve compaction model aliases before dispatch; no longer open. |
| [#90338](https://github.com/openclaw/openclaw/issues/90338) | Closed in local gitcrawl 2026-06-11 | Memory index meta never written when gateway auto-sync finds identity missing with existing chunks; no longer open. |
| [#90337](https://github.com/openclaw/openclaw/pull/90337) | Closed in local gitcrawl 2026-06-11 | fix(anthropic): add Claude Haiku 4.5 to static model catalog; no longer open. |
| [#90336](https://github.com/openclaw/openclaw/pull/90336) | Closed in local gitcrawl 2026-06-11 | fix(memory): fail fast when embeddings provider is unavailable; no longer open. |
| [#90330](https://github.com/openclaw/openclaw/pull/90330) | Closed in local gitcrawl | Fix ChatGPT Codex streams without content-type; no longer open. |
| [#90328](https://github.com/openclaw/openclaw/pull/90328) | Closed in local gitcrawl | Expose model picker agent runtimes; no longer open. |
| [#90327](https://github.com/openclaw/openclaw/pull/90327) | Closed in local gitcrawl 2026-06-11 | fix(openai): tolerate missing content-type on streamed Codex responses; no longer open. |
| [#90326](https://github.com/openclaw/openclaw/pull/90326) | Closed in local gitcrawl 2026-06-15 | fix(fireworks): resolve catalog model params from plugin.json via core; no longer open. |
| [#90323](https://github.com/openclaw/openclaw/pull/90323) | Closed in local gitcrawl | fix(memory): replace node:sqlite with better-sqlite3 to enable sqlite-vec on macOS; no longer open. |
| [#90321](https://github.com/openclaw/openclaw/pull/90321) | Closed in local gitcrawl 2026-06-06 | Normalize legacy Codex session runtime state; no longer open. |
| [#90319](https://github.com/openclaw/openclaw/pull/90319) | Closed in local gitcrawl 2026-06-06 | Add Codex session route migration coverage; no longer open. |
| [#90317](https://github.com/openclaw/openclaw/pull/90317) | Closed in local gitcrawl 2026-06-06 | Add Codex multi-agent config migration coverage; no longer open. |
| [#90315](https://github.com/openclaw/openclaw/issues/90315) | Closed in local gitcrawl 2026-06-11 | [Bug]: Ollama Cloud live-discovered model loses capability metadata in gateway catalog; no longer open. |
| [#90313](https://github.com/openclaw/openclaw/issues/90313) | Closed in local gitcrawl | Dreaming session-corpus: cron classification doesn't follow subagent parentage; archived (`.deleted`/`.reset`) transcripts re-ingested; no longer open. |
| [#90310](https://github.com/openclaw/openclaw/pull/90310) | Closed in local gitcrawl 2026-06-12 | fix(openai-responses): sanitize null content before SDK serialization (#90094); no longer open. |
| [#90304](https://github.com/openclaw/openclaw/pull/90304) | Closed in local gitcrawl 2026-06-06 | feat(memory): support qmd query rerank toggle; no longer open. |
| [#90302](https://github.com/openclaw/openclaw/issues/90302) | Closed in local gitcrawl | [Feature]: Expose --fallbacks on openclaw cron create/edit; no longer open. |
| [#90295](https://github.com/openclaw/openclaw/issues/90295) | Closed in local gitcrawl | memory-lancedb 2026.6.1 fails to install: apache-arrow 21.1.0 conflicts with @lancedb/lancedb 0.30.0 peer range; no longer open. |
| [#90292](https://github.com/openclaw/openclaw/issues/90292) | Closed in local gitcrawl | [Bug] Dreaming narrative writes fallback snippets despite subagent generating valid poems; no longer open. |
| [#90291](https://github.com/openclaw/openclaw/pull/90291) | Closed in local gitcrawl | fix(providers): guard OpenAI web search tool detection; no longer open. |
| [#90289](https://github.com/openclaw/openclaw/pull/90289) | Closed in local gitcrawl | fix(providers): skip unreadable Anthropic payload tool schemas; no longer open. |
| [#90288](https://github.com/openclaw/openclaw/issues/90288) | Closed in local gitcrawl | [Bug]: Non-Anthropic models output tool calls as plain text '[tool: exec]' instead of tool_use blocks; no longer open. |
| [#90286](https://github.com/openclaw/openclaw/pull/90286) | Closed in local gitcrawl | fix(providers): skip unreadable OpenAI responses tool schemas; no longer open. |
| [#90283](https://github.com/openclaw/openclaw/pull/90283) | Closed in local gitcrawl | fix(providers): skip unreadable OpenAI completion tool schemas; no longer open. |
| [#90278](https://github.com/openclaw/openclaw/pull/90278) | Closed in local gitcrawl | fix(providers): skip unreadable Anthropic tool schemas; no longer open. |
| [#90277](https://github.com/openclaw/openclaw/issues/90277) | Closed in local gitcrawl | gateway install --force drops MINIMAX_API_KEY from service-env despite managed keys list; no longer open. |
| [#90264](https://github.com/openclaw/openclaw/pull/90264) | Closed in local gitcrawl 2026-06-06 | fix(memory): move local embeddings to llama.cpp provider; no longer open. |
| [#90260](https://github.com/openclaw/openclaw/pull/90260) | Closed in local gitcrawl 2026-06-11 | fix(agents): decode xai and venice tool-call arguments exactly once; no longer open. |
| [#90249](https://github.com/openclaw/openclaw/pull/90249) | Closed in local gitcrawl | fix(providers): skip unreadable Google tool schemas; no longer open. |
| [#90242](https://github.com/openclaw/openclaw/pull/90242) | Closed in local gitcrawl 2026-06-15 | fix(providers): skip unreadable Mistral tool schemas; no longer open. |
| [#90235](https://github.com/openclaw/openclaw/pull/90235) | Closed in local gitcrawl 2026-06-15 | fix(gateway): repair Ollama dense stream — preserve replacement stream deltas and rich tool call deltas; no longer open. |
| [#90234](https://github.com/openclaw/openclaw/pull/90234) | Closed in local gitcrawl | fix(agents): filter unresolved model registry rows; no longer open. |
| [#90221](https://github.com/openclaw/openclaw/pull/90221) | Closed in local gitcrawl 2026-06-06 | fix(compaction): allow compaction with aws-sdk auth without apiKey or headers; no longer open. |
| [#90210](https://github.com/openclaw/openclaw/pull/90210) | Closed in local gitcrawl 2026-06-15 | fix(anthropic): add claude-haiku-4-5 to static model catalog; no longer open. |
| [#90206](https://github.com/openclaw/openclaw/pull/90206) | Closed in local gitcrawl | Fix Bedrock aws-sdk compaction auth; no longer open. |
| [#90205](https://github.com/openclaw/openclaw/pull/90205) | Closed in local gitcrawl 2026-06-06 | fix: tolerate missing streamed response content type; no longer open. |
| [#90200](https://github.com/openclaw/openclaw/pull/90200) | Closed in local gitcrawl | fix(agents): guard OpenAI strict tool diagnostics; no longer open. |
| [#90196](https://github.com/openclaw/openclaw/pull/90196) | Closed in local gitcrawl | feat(ios): Add Piper TTS as on-device voice engine option; no longer open. |
| [#90170](https://github.com/openclaw/openclaw/issues/90170) | Closed in local gitcrawl | [Bug]: Possible token/cost regression after OpenClaw v2026.5.28 with DeepSeek v4-pro; no longer open. |
| [#90165](https://github.com/openclaw/openclaw/pull/90165) | Closed in local gitcrawl 2026-06-11 | fix(memory): do not filter FTS keyword search by embedding model (#48300); no longer open. |
| [#90149](https://github.com/openclaw/openclaw/pull/90149) | Closed in local gitcrawl 2026-06-11 | fix: preserve user model on stale rollover; no longer open. |
| [#90146](https://github.com/openclaw/openclaw/issues/90146) | Closed in local gitcrawl 2026-06-06 | google-vertex: Missing gemini-3.1-flash-lite in provider catalog causes silent failure instead of error; no longer open. |
| [#90145](https://github.com/openclaw/openclaw/pull/90145) | Closed in local gitcrawl 2026-06-06 | fix: protect global agent config defaults [AI]; no longer open. |
| [#90139](https://github.com/openclaw/openclaw/issues/90139) | Closed in local gitcrawl | dropThinkingBlocks sanitizer: short text replies shown as [assistant reasoning omitted] in TUI/webchat/WeChat; no longer open. |
| [#90138](https://github.com/openclaw/openclaw/pull/90138) | Closed in local gitcrawl 2026-06-11 | fix(minimax): exempt M3 from thinking-disabled wrapper; no longer open. |
| [#90137](https://github.com/openclaw/openclaw/pull/90137) | Closed in local gitcrawl 2026-06-06 | fix: strip thinking signatures from entries after compaction; no longer open. |
| [#90130](https://github.com/openclaw/openclaw/pull/90130) | Closed in local gitcrawl | fix(auth): guard preferred provider metadata; no longer open. |
| [#90128](https://github.com/openclaw/openclaw/pull/90128) | Closed in local gitcrawl 2026-06-12 | fix(sessions): preserve user /model override across daily/idle session rollover (#90119); no longer open. |
| [#90125](https://github.com/openclaw/openclaw/pull/90125) | Closed in local gitcrawl | fix(embedded-runner): distinguish model initialization errors from assistant execution errors; no longer open. |
| [#90124](https://github.com/openclaw/openclaw/pull/90124) | Closed in local gitcrawl 2026-06-06 | fix(agents): harden tool-call handling against A2A/model tool-call poisoning; no longer open. |
| [#90119](https://github.com/openclaw/openclaw/issues/90119) | Closed in local gitcrawl 2026-06-12 | [Bug]: User /model override silently dropped on daily/idle session rollover (survives /new but not the 4AM reset); no longer open. |
| [#90117](https://github.com/openclaw/openclaw/pull/90117) | Closed in local gitcrawl | fix: skip qmd zero-hit sync retry in memory_search; no longer open. |
| [#90116](https://github.com/openclaw/openclaw/pull/90116) | Closed in local gitcrawl 2026-06-15 | fix: add Claude Haiku 4.5 static catalog entries; no longer open. |
| [#90112](https://github.com/openclaw/openclaw/pull/90112) | Closed in local gitcrawl | fix(commands): guard provider catalog aliases; no longer open. |
| [#90110](https://github.com/openclaw/openclaw/pull/90110) | Closed in local gitcrawl 2026-06-15 | fix(anthropic): resolve Claude Haiku 4.5 static catalog refs; no longer open. |
| [#90109](https://github.com/openclaw/openclaw/pull/90109) | Closed in local gitcrawl | fix(commands): guard manifest catalog filters; no longer open. |
| [#90107](https://github.com/openclaw/openclaw/pull/90107) | Closed in local gitcrawl | fix(commands): guard model provider aliases; no longer open. |
| [#90106](https://github.com/openclaw/openclaw/pull/90106) | Closed in local gitcrawl 2026-06-15 | fix: add Claude Haiku 4.5 to static model catalog; no longer open. |
| [#90094](https://github.com/openclaw/openclaw/issues/90094) | Closed in local gitcrawl | openai-responses transport sends null content, rejected by strict providers (400 schema error); no longer open. |
| [#90093](https://github.com/openclaw/openclaw/issues/90093) | Closed in local gitcrawl | openai-chatgpt-responses native replay sends encrypted reasoning and breaks next turn with invalid_encrypted_content; no longer open. |
| [#90088](https://github.com/openclaw/openclaw/issues/90088) | Closed in local gitcrawl 2026-06-15 | anthropic (api_key) provider: Claude Haiku 4.5 missing from static model catalog → "Unknown model" (model_not_found); no longer open. |
| [#90086](https://github.com/openclaw/openclaw/issues/90086) | Closed in local gitcrawl 2026-06-15 | Pi/native runtime routes openai-chatgpt-responses to boundary-aware transport and fails on ChatGPT Codex endpoint; no longer open. |
| [#90085](https://github.com/openclaw/openclaw/pull/90085) | Closed in local gitcrawl | fix(gateway): guard model pricing metadata; no longer open. |
| [#90083](https://github.com/openclaw/openclaw/issues/90083) | Closed in local gitcrawl 2026-06-12 | [Bug]: 2026.6.1 OpenAI ChatGPT Responses transport fails with invalid_provider_content_type for gpt-5.4/gpt-5.5; no longer open. |
| [#90077](https://github.com/openclaw/openclaw/pull/90077) | Closed in local gitcrawl | fix(plugins): guard provider discovery credential metadata; no longer open. |
| [#90075](https://github.com/openclaw/openclaw/pull/90075) | Closed in local gitcrawl 2026-06-06 | fix(agents): detect unsigned thinking-only stall when reasoning payload inflates payloadCount; no longer open. |
| [#90073](https://github.com/openclaw/openclaw/pull/90073) | Closed in local gitcrawl | fix(plugins): guard metadata snapshot owner rows; no longer open. |
| [#90056](https://github.com/openclaw/openclaw/pull/90056) | Closed in local gitcrawl 2026-06-11 | fix(doctor): merge disjoint openai-codex model entries into canonical openai provider; no longer open. |
| [#90051](https://github.com/openclaw/openclaw/pull/90051) | Closed in local gitcrawl 2026-06-11 | fix(agents): strip reasoning tags from chat replies; no longer open. |
| [#90049](https://github.com/openclaw/openclaw/issues/90049) | Closed in local gitcrawl | Heartbeat sessions report 'assistant turn failed before producing content' on model initialization failure; no longer open. |
| [#90047](https://github.com/openclaw/openclaw/issues/90047) | Closed in local gitcrawl 2026-06-11 | Codex migration (2026.6.1) drops the gpt-5.5 model when a canonical `openai` provider exists for embeddings — agents go silent; no longer open. |
| [#90036](https://github.com/openclaw/openclaw/issues/90036) | Closed in local gitcrawl | Session model route drifts from openai/gpt-5.5 to openai-codex/gpt-5.5 with native Codex runtime; no longer open. |
| [#90030](https://github.com/openclaw/openclaw/pull/90030) | Closed in local gitcrawl | fix(memory-core): skip qmd zero-hit search sync; no longer open. |
| [#90029](https://github.com/openclaw/openclaw/pull/90029) | Closed in local gitcrawl 2026-06-11 | feat: add live provider model catalog helper; no longer open. |
| [#90028](https://github.com/openclaw/openclaw/pull/90028) | Closed in local gitcrawl 2026-06-06 | docs: clarify legacy openai-codex auth; no longer open. |
| [#90023](https://github.com/openclaw/openclaw/issues/90023) | Closed in local gitcrawl | QMD memory_search zero-hit queries trigger synchronous force sync and stall interactive turns; no longer open. |
| [#90021](https://github.com/openclaw/openclaw/issues/90021) | Closed in local gitcrawl 2026-06-12 | OpenAI model with agentRuntime.id "openclaw" appears to switch to OpenAI Codex runtime after first Telegram message; no longer open. |
| [#89983](https://github.com/openclaw/openclaw/pull/89983) | Closed in local gitcrawl | fix(agents): isolate provider attribution manifest rows; no longer open. |
| [#89981](https://github.com/openclaw/openclaw/pull/89981) | Closed in local gitcrawl | fix(diagnostics-otel): keep full model id on spans instead of collapsing to "unknown"; no longer open. |
| [#89979](https://github.com/openclaw/openclaw/pull/89979) | Closed in local gitcrawl | fix(config): isolate provider auto-enable rows; no longer open. |
| [#89976](https://github.com/openclaw/openclaw/issues/89976) | Closed in local gitcrawl 2026-06-04 | [Bug]: Manual /compact on Codex OAuth sessions resolves to direct openai auth instead of Codex runtime; no longer open. |
| [#89972](https://github.com/openclaw/openclaw/pull/89972) | Closed in local gitcrawl | feat(watch): replace chokidar dep with in-repo chokidar-slim + async add API; no longer open. |
| [#89961](https://github.com/openclaw/openclaw/pull/89961) | Closed in local gitcrawl | fix(plugins): guard manifest suppression metadata; no longer open. |
| [#89957](https://github.com/openclaw/openclaw/pull/89957) | Closed in local gitcrawl 2026-06-12 | docs: add section on extending memory with corpus supplements; no longer open. |
| [#89952](https://github.com/openclaw/openclaw/pull/89952) | Closed in local gitcrawl 2026-06-11 | fix(plugins): guard provider auth choice metadata; no longer open. |
| [#89948](https://github.com/openclaw/openclaw/pull/89948) | Closed in local gitcrawl | fix(plugins): guard plugin id alias metadata; no longer open. |
| [#89946](https://github.com/openclaw/openclaw/pull/89946) | Closed in local gitcrawl | fix(plugins): guard provider policy metadata; no longer open. |
| [#89945](https://github.com/openclaw/openclaw/pull/89945) | Closed in local gitcrawl | fix(plugins): guard provider discovery metadata; no longer open. |
| [#89941](https://github.com/openclaw/openclaw/pull/89941) | Closed in local gitcrawl 2026-06-04 | fix(issue): resolve #89425 [Bug]: Missing extensions/speech-core/ in npm tarball (v2026; no longer open. |
| [#89940](https://github.com/openclaw/openclaw/pull/89940) | Closed in local gitcrawl | fix(models): guard manifest model id metadata; no longer open. |
| [#89937](https://github.com/openclaw/openclaw/issues/89937) | Closed in local gitcrawl 2026-06-06 | [Bug] before_prompt_build hook not triggered in agent-runner / embedded-agent path (chat user messages); no longer open. |
| [#89936](https://github.com/openclaw/openclaw/pull/89936) | Closed in local gitcrawl | fix(plugins): guard model suppression metadata; no longer open. |
| [#89933](https://github.com/openclaw/openclaw/pull/89933) | Closed in local gitcrawl | fix(plugins): guard synthetic auth metadata; no longer open. |
| [#89918](https://github.com/openclaw/openclaw/pull/89918) | Closed in local gitcrawl 2026-06-11 | fix(vertex): route eu/us multi-region to .rep.googleapis.com host; no longer open. |
| [#89917](https://github.com/openclaw/openclaw/pull/89917) | Closed in local gitcrawl | fix(agents): guard provider auth alias metadata; no longer open. |
| [#89910](https://github.com/openclaw/openclaw/pull/89910) | Closed in local gitcrawl 2026-06-11 | fix(plugins): guard provider auth choice metadata; no longer open. |
| [#89905](https://github.com/openclaw/openclaw/pull/89905) | Closed in local gitcrawl | fix(hooks): honor hook-level model override for session-memory slug generation; no longer open. |
| [#89901](https://github.com/openclaw/openclaw/pull/89901) | Closed in local gitcrawl 2026-06-11 | fix(vertex): support eu and us multi-region endpoints; no longer open. |
| [#89899](https://github.com/openclaw/openclaw/pull/89899) | Closed in local gitcrawl | fix(package): include speech-core in npm tarball; no longer open. |
| [#89891](https://github.com/openclaw/openclaw/issues/89891) | Closed in local gitcrawl 2026-06-11 | [Bug]: Vertex AI eu multi-region unreachable — host prefix is hardcoded; no longer open. |
| [#89880](https://github.com/openclaw/openclaw/pull/89880) | Closed in local gitcrawl | fix(plugins): guard model catalog registration metadata; no longer open. |
| [#89874](https://github.com/openclaw/openclaw/pull/89874) | Closed in local gitcrawl 2026-06-06 | fix(agents): detect unsigned thinking-only stall when reasoning payload inflates payloadCount; no longer open. |
| [#89845](https://github.com/openclaw/openclaw/pull/89845) | Closed in local gitcrawl 2026-06-04 | fix(fireworks): optimize caching with x-session-affinity; no longer open. |
| [#89832](https://github.com/openclaw/openclaw/pull/89832) | Closed in local gitcrawl 2026-06-11 | fix(config): allow requiresReasoningContentOnAssistantMessages in ModelCompatSchema; no longer open. |
| [#89787](https://github.com/openclaw/openclaw/issues/89787) | Closed in local gitcrawl 2026-06-06 | [Bug]: Agent stalls indefinitely when model emits stopReason="stop" with no toolCall — only thinking block generated; no longer open. |
| [#89758](https://github.com/openclaw/openclaw/issues/89758) | Closed in local gitcrawl | [Bug] overloaded_error triggers immediate rotate_profile without retry, causing cascade fallback on transient provider overload; no longer open. |
| [#89741](https://github.com/openclaw/openclaw/pull/89741) | Closed in local gitcrawl 2026-06-15 | fix(memory): add EPERM fallback for atomic reindex; no longer open. |
| [#89730](https://github.com/openclaw/openclaw/pull/89730) | Closed in local gitcrawl | fix(agents): guard lean tool name reads; no longer open. |
| [#89729](https://github.com/openclaw/openclaw/pull/89729) | Closed in local gitcrawl 2026-06-11 | fix（OpenAI Responses/provider）: skip Responses item id replay when store support is stripped; no longer open. |
| [#89728](https://github.com/openclaw/openclaw/issues/89728) | Closed in local gitcrawl 2026-06-15 | Custom OpenAI Responses-compatible providers still replay item ids when store support is stripped; no longer open. |
| [#89716](https://github.com/openclaw/openclaw/pull/89716) | Closed in local gitcrawl | fix(providers): strip cache-boundary marker from non-Anthropic prompts; no longer open. |
| [#89706](https://github.com/openclaw/openclaw/issues/89706) | Closed in local gitcrawl 2026-06-06 | github-copilot: gemini-3.1-pro appears in models list but fails silently when selected; no longer open. |
| [#89703](https://github.com/openclaw/openclaw/pull/89703) | Closed in local gitcrawl | fix(openai): guard responses tool payload names; no longer open. |
| [#89692](https://github.com/openclaw/openclaw/pull/89692) | Closed in local gitcrawl 2026-06-11 | fix(config): allow compat.requiresReasoningContentOnAssistantMessages in model config; no longer open. |
| [#89691](https://github.com/openclaw/openclaw/issues/89691) | Closed in local gitcrawl 2026-06-07 | Active-memory embedded memory_search intermittently loses embedding provider and falls back to FTS-only; no longer open. |
| [#89685](https://github.com/openclaw/openclaw/pull/89685) | Closed in local gitcrawl 2026-06-04 | fix(acpx): handle Claude ACP model startup options; no longer open. |
| [#89669](https://github.com/openclaw/openclaw/pull/89669) | Closed in local gitcrawl | fix(agents): contain provider schema hook failures; no longer open. |
| [#89667](https://github.com/openclaw/openclaw/pull/89667) | Closed in local gitcrawl 2026-06-11 | fix(config): allow requiresReasoningContentOnAssistantMessages in ModelCompatSchema [AI-assisted]; no longer open. |
| [#89665](https://github.com/openclaw/openclaw/pull/89665) | Closed in local gitcrawl | fix(plugin-sdk): guard provider tool schema walks; no longer open. |
| [#89660](https://github.com/openclaw/openclaw/issues/89660) | Closed in local gitcrawl 2026-06-11 | [Bug]: requiresReasoningContentOnAssistantMessages missing from ModelCompatSchema — can't replicate native DeepSeek behavior on custom providers; no longer open. |
| [#89657](https://github.com/openclaw/openclaw/pull/89657) | Closed in local gitcrawl | fix(plugins): harden installed index stale metadata; no longer open. |
| [#89655](https://github.com/openclaw/openclaw/issues/89655) | Closed in local gitcrawl | [Bug]: `NODE_USE_SYSTEM_CA=1` breaks `openai-codex` auth/keychain paths on macOS and can fail fresh runtime launch with `SecItemCopyMatching failed -50`; no longer open. |
| [#89652](https://github.com/openclaw/openclaw/pull/89652) | Closed in local gitcrawl 2026-06-11 | fix(plugins): load owning plugin for configured memory embedding provider at startup; no longer open. |
| [#89651](https://github.com/openclaw/openclaw/issues/89651) | Closed in local gitcrawl 2026-06-07 | Gateway startup does not load the plugin owning a configured memory embedding provider (memorySearch.provider); no longer open. |
| [#89647](https://github.com/openclaw/openclaw/pull/89647) | Closed in local gitcrawl | fix(plugins): guard startup manifest channels; no longer open. |
| [#89646](https://github.com/openclaw/openclaw/pull/89646) | Closed in local gitcrawl | fix(model-catalog): guard model id policies; no longer open. |
| [#89644](https://github.com/openclaw/openclaw/pull/89644) | Closed in local gitcrawl | fix(model-catalog): skip unreadable catalog records; no longer open. |
| [#89633](https://github.com/openclaw/openclaw/issues/89633) | Closed in local gitcrawl | Codex turn fails with generic Telegram fallback when invalid image tool model is configured, leaving child agent orphaned on full stdout pipe; no longer open. |
| [#89629](https://github.com/openclaw/openclaw/pull/89629) | Closed in local gitcrawl 2026-06-15 | feat(hooks): per-turn usageState (provider limits + rich atoms) on reply_payload_sending; no longer open. |
| [#89624](https://github.com/openclaw/openclaw/pull/89624) | Closed in local gitcrawl | fix(ollama): guard tool schema normalization; no longer open. |
| [#89617](https://github.com/openclaw/openclaw/issues/89617) | Closed in local gitcrawl | Add Atomic Chat as a bundled local provider (OpenAI-compatible, 127.0.0.1:1337); no longer open. |
| [#89613](https://github.com/openclaw/openclaw/pull/89613) | Closed in local gitcrawl 2026-06-06 | docs: document auth profile failure policy contract; no longer open. |
| [#89610](https://github.com/openclaw/openclaw/pull/89610) | Closed in local gitcrawl 2026-06-03 | Add channel-scoped memory search filters; no longer open. |
| [#89571](https://github.com/openclaw/openclaw/pull/89571) | Closed in local gitcrawl | fix(provider): harden provider tool schema hooks; no longer open. |
| [#89561](https://github.com/openclaw/openclaw/pull/89561) | Closed in local gitcrawl 2026-06-11 | fix(hooks): honor session-memory hook model override for LLM slug generation [AI-assisted]; no longer open. |
| [#89560](https://github.com/openclaw/openclaw/pull/89560) | Closed in local gitcrawl 2026-06-04 | fix(telegram): isolate verbose status after streamed finals; no longer open. |
| [#89558](https://github.com/openclaw/openclaw/pull/89558) | Closed in local gitcrawl | docs: document embedded compaction context contracts; no longer open. |
| [#89551](https://github.com/openclaw/openclaw/issues/89551) | Closed in local gitcrawl | [Bug]: session-memory hook model config ignored for LLM slug generation; no longer open. |
| [#89549](https://github.com/openclaw/openclaw/issues/89549) | Closed in local gitcrawl | [Bug]: sessions_spawn child runs fail after acceptance with HTTP 401 Missing scopes api.responses.write; no longer open. |
| [#89543](https://github.com/openclaw/openclaw/pull/89543) | Closed in local gitcrawl | fix(agents): harden OpenAI strict schema inspection; no longer open. |
| [#89540](https://github.com/openclaw/openclaw/issues/89540) | Closed in local gitcrawl 2026-06-04 | [Bug]: Telegram /v Active Memory status can overwrite short streamed replies; no longer open. |
| [#89535](https://github.com/openclaw/openclaw/pull/89535) | Closed in local gitcrawl | test(codex): cover binds without model overrides; no longer open. |
| [#89534](https://github.com/openclaw/openclaw/issues/89534) | Closed in local gitcrawl | [Bug]: /codex bind without --model can fail with defaultModel ReferenceError; no longer open. |
| [#89531](https://github.com/openclaw/openclaw/issues/89531) | Closed in local gitcrawl | [Bug] amazon-bedrock-openai / openai-responses: streaming emits multiple incremental final_answer phases, causing duplicate channel messages; no longer open. |
| [#89509](https://github.com/openclaw/openclaw/issues/89509) | Closed in local gitcrawl | Bug: [[tts:text]] tag content not passed to TTS engine — surrounding text sent instead; no longer open. |
| [#89508](https://github.com/openclaw/openclaw/pull/89508) | Closed in local gitcrawl 2026-06-12 | fix(models): clarify provider model registration hint; no longer open. |
| [#89479](https://github.com/openclaw/openclaw/pull/89479) | Closed in local gitcrawl 2026-06-03 | fix: auto-fix for issue #89431; no longer open. |
| [#89476](https://github.com/openclaw/openclaw/issues/89476) | Closed in local gitcrawl | feat(onboard): ? install-daemon UI ???????? custom provider ???; no longer open. |
| [#89460](https://github.com/openclaw/openclaw/pull/89460) | Closed in local gitcrawl 2026-06-03 | fix(models): preserve provider prompt cache boundaries; no longer open. |
| [#89453](https://github.com/openclaw/openclaw/pull/89453) | Closed in local gitcrawl | fix(android): filter thinking and reasoning blocks from chat message display; no longer open. |
| [#89451](https://github.com/openclaw/openclaw/pull/89451) | Closed in local gitcrawl | fix(google): quarantine invalid extension tool schemas; no longer open. |
| [#89443](https://github.com/openclaw/openclaw/pull/89443) | Closed in local gitcrawl | fix(active-memory): drop assistant chitchat boilerplate from recall summaries; no longer open. |
| [#89441](https://github.com/openclaw/openclaw/pull/89441) | Closed in local gitcrawl 2026-06-03 | fix: add missing extensions/speech-core/ source files for npm tarball; no longer open. |
| [#89440](https://github.com/openclaw/openclaw/pull/89440) | Closed in local gitcrawl 2026-06-03 | fix(llm): keep OpenAI-compatible reasoning streams active; no longer open. |
| [#89437](https://github.com/openclaw/openclaw/pull/89437) | Closed in local gitcrawl | fix(google): quarantine invalid tool declarations; no longer open. |
| [#89431](https://github.com/openclaw/openclaw/issues/89431) | Closed in local gitcrawl | [Bug]: macos say command in daemon not output to speakers; no longer open. |
| [#89429](https://github.com/openclaw/openclaw/pull/89429) | Closed in local gitcrawl | fix(plugin-sdk): quarantine invalid provider tool schemas; no longer open. |
| [#89427](https://github.com/openclaw/openclaw/pull/89427) | Closed in local gitcrawl 2026-06-03 | fix: add missing extensions/speech-core/ source files for npm tarball; no longer open. |
| [#89425](https://github.com/openclaw/openclaw/issues/89425) | Closed in local gitcrawl | [Bug]: Missing extensions/speech-core/ in npm tarball (v2026.5.28) — "Unable to resolve bundled plugin public surface speech-core/runtime-api.js"; no longer open. |
| [#89420](https://github.com/openclaw/openclaw/pull/89420) | Closed in local gitcrawl 2026-06-03 | fix(llm): filter out reasoning_content from streaming output when reasoning is disabled; no longer open. |
| [#89413](https://github.com/openclaw/openclaw/pull/89413) | Closed in local gitcrawl | fix(openai): quarantine unreadable projected tools; no longer open. |
| [#89400](https://github.com/openclaw/openclaw/pull/89400) | Closed in local gitcrawl 2026-06-03 | fix(google): add missing gemini-3.1-flash-lite to google-vertex catalog; no longer open. |
| [#89392](https://github.com/openclaw/openclaw/issues/89392) | Closed in local gitcrawl | Long streaming model responses cause event loop starvation; no longer open. |
| [#89390](https://github.com/openclaw/openclaw/issues/89390) | Closed in local gitcrawl 2026-06-03 | google-vertex: gemini-3.1-flash-lite missing from pi-ai model catalog, causes silent failure with no fallback; no longer open. |
| [#89389](https://github.com/openclaw/openclaw/issues/89389) | Closed in local gitcrawl 2026-06-03 | [Bug]: MiniMax Global OAuth fails with Connect Timeout (api.minimax.io/oauth/code now redirects); no longer open. |
| [#89386](https://github.com/openclaw/openclaw/issues/89386) | Closed in local gitcrawl 2026-06-03 | Bug: 5.28 transport refactor regressed prompt caching for Anthropic and OpenAI-compatible providers; no longer open. |
| [#89382](https://github.com/openclaw/openclaw/issues/89382) | Closed in local gitcrawl 2026-06-03 | GitHub Copilot timeout marks auth profile in cooldown and blocks same-provider fallback models; no longer open. |
| [#89381](https://github.com/openclaw/openclaw/pull/89381) | Closed in local gitcrawl | fix(plugin-sdk): guard provider tool schema traversal; no longer open. |
| [#89379](https://github.com/openclaw/openclaw/pull/89379) | Closed in local gitcrawl 2026-06-03 | fix(providers): use native reasoning mode for Gemini instead of tagged; no longer open. |
| [#89378](https://github.com/openclaw/openclaw/pull/89378) | Closed in local gitcrawl | fix(agents): guard OpenAI tool schema conversion; no longer open. |
| [#89371](https://github.com/openclaw/openclaw/pull/89371) | Closed in local gitcrawl | fix(memory): clean stale short-term temp files; no longer open. |
| [#89360](https://github.com/openclaw/openclaw/pull/89360) | Closed in local gitcrawl | refactor: add QMD session artifact identity mapping; no longer open. |
| [#89353](https://github.com/openclaw/openclaw/pull/89353) | Closed in local gitcrawl | fix(plugin-sdk): guard provider schema inspection; no longer open. |
| [#89348](https://github.com/openclaw/openclaw/pull/89348) | Closed in local gitcrawl | refactor: add memory session sync identity API; no longer open. |
| [#89347](https://github.com/openclaw/openclaw/pull/89347) | Closed in local gitcrawl 2026-06-03 | fix: repair model provider edge cases; no longer open. |
| [#89343](https://github.com/openclaw/openclaw/pull/89343) | Closed in local gitcrawl 2026-06-03 | fix(llm): prevent reasoning_content leak when reasoning is disabled; no longer open. |
| [#89330](https://github.com/openclaw/openclaw/issues/89330) | Closed in local gitcrawl 2026-06-03 | Bug: non-persistent Responses routes replay stale item ids; no longer open. |
| [#89324](https://github.com/openclaw/openclaw/pull/89324) | Closed in local gitcrawl | fix(xai): skip unreadable tool payload entries; no longer open. |
| [#89322](https://github.com/openclaw/openclaw/pull/89322) | Closed in local gitcrawl | fix(ollama): skip unreadable tool descriptors; no longer open. |
| [#89317](https://github.com/openclaw/openclaw/pull/89317) | Closed in local gitcrawl | fix(bedrock): guard tool config projection; no longer open. |
| [#89305](https://github.com/openclaw/openclaw/pull/89305) | Closed in local gitcrawl 2026-06-03 | fix(agents): bypass stale auth for plugin harnesses; no longer open. |
| [#89300](https://github.com/openclaw/openclaw/issues/89300) | Closed in local gitcrawl | model-fetch logs lost in v2026.5.28 — degraded from log.info to log.debug behind env flag; no longer open. |
| [#89298](https://github.com/openclaw/openclaw/pull/89298) | Closed in local gitcrawl 2026-06-03 | fix(diagnostics): re-queue pending messages after stuck-session recovery aborts ghost run; no longer open. |
| [#89293](https://github.com/openclaw/openclaw/pull/89293) | Closed in local gitcrawl 2026-06-03 | fix(logging): requeue stuck session lane after abort; no longer open. |
| [#89290](https://github.com/openclaw/openclaw/pull/89290) | Closed in local gitcrawl 2026-06-11 | [codex] Keep Codex waiting after raw reasoning progress; no longer open. |
| [#89273](https://github.com/openclaw/openclaw/pull/89273) | Closed in local gitcrawl | fix(doctor): sanitize provider catalog findings; no longer open. |
| [#89265](https://github.com/openclaw/openclaw/issues/89265) | Closed in local gitcrawl | [Feature]: More local providers; no longer open. |
| [#89264](https://github.com/openclaw/openclaw/issues/89264) | Closed in local gitcrawl | [Bug]: Dreaming deep promotion biased to stale 3-5 day old content; REM produces repetitive meta-themes; promotion gates bypassed via phase-signal boost; no longer open. |
| [#89259](https://github.com/openclaw/openclaw/issues/89259) | Closed in local gitcrawl | EmbeddedAttemptSessionTakeoverError fires at ~120s on long Bedrock streams (fence whitelist too narrow?); no longer open. |
| [#89251](https://github.com/openclaw/openclaw/pull/89251) | Closed in local gitcrawl 2026-06-12 | fix: deliver tts tool audio on whatsapp; no longer open. |
| [#89248](https://github.com/openclaw/openclaw/pull/89248) | Closed in local gitcrawl 2026-06-03 | feat(context-engine): context-capsule plugin — 99.3% token reduction with recovery-score gate; no longer open. |
| [#89244](https://github.com/openclaw/openclaw/pull/89244) | Closed in local gitcrawl 2026-06-04 | fix(memory): warn on high runtime watcher pressure; no longer open. |
| [#89233](https://github.com/openclaw/openclaw/issues/89233) | Closed in local gitcrawl | [Bug]: Default models.providers.lmstudio.apiKey ships as plaintext placeholder 'lm-studio' — triggers false-positive security audit warning; no longer open. |
| [#89229](https://github.com/openclaw/openclaw/pull/89229) | Closed in local gitcrawl | fix(llm): guard Anthropic provider tool descriptors; no longer open. |
| [#89221](https://github.com/openclaw/openclaw/pull/89221) | Closed in local gitcrawl | fix(agents): guard Anthropic tool descriptors; no longer open. |
| [#89208](https://github.com/openclaw/openclaw/issues/89208) | Closed in local gitcrawl 2026-06-03 | Stuck-session recovery discards queued user messages after aborting ghost run; no longer open. |
| [#89202](https://github.com/openclaw/openclaw/issues/89202) | Closed in local gitcrawl | [Bug]: Telegram heavy turns can cause incomplete  codex-app server turn around compaction, including under OpenClaw runtime.; no longer open. |
| [#89198](https://github.com/openclaw/openclaw/issues/89198) | Closed in local gitcrawl | Feature Request: Support Gateway TTS/STT in iOS App; no longer open. |
| [#89197](https://github.com/openclaw/openclaw/issues/89197) | Closed in local gitcrawl | Gateway agent run failure with no model reachable: chat.history returns incomplete state, Control UI clears conversation history; no longer open. |
| [#89196](https://github.com/openclaw/openclaw/issues/89196) | Closed in local gitcrawl | Dreaming REM: sub-session visible in session switcher + narrative diary fails to write to DREAMS.md; no longer open. |
| [#89194](https://github.com/openclaw/openclaw/pull/89194) | Closed in local gitcrawl | fix: include name field in model_not_found remediation hint; no longer open. |
| [#89192](https://github.com/openclaw/openclaw/issues/89192) | Closed in local gitcrawl 2026-06-12 | bug(models): model_not_found remediation message is incomplete — suggests `{ "id": ... }` but `name` is required and `api`/`baseUrl` are silently needed (misroutes to OpenAI); no longer open. |
| [#89190](https://github.com/openclaw/openclaw/pull/89190) | Closed in local gitcrawl | feat(xai): add grok-composer-2.5-fast model; no longer open. |
| [#89188](https://github.com/openclaw/openclaw/pull/89188) | Closed in local gitcrawl 2026-06-02 | fix(memory-core): reduce Linux watcher fan-out; no longer open. |
| [#89185](https://github.com/openclaw/openclaw/pull/89185) | Closed in local gitcrawl 2026-06-02 | fix(memory): default gateway memory watch off; no longer open. |
| [#89183](https://github.com/openclaw/openclaw/pull/89183) | Closed in local gitcrawl | fix(tui): keep local slash commands out of model prompts; no longer open. |
| [#89181](https://github.com/openclaw/openclaw/pull/89181) | Closed in local gitcrawl 2026-06-02 | fix(agents): dispatch auth failures by type; no longer open. |
| [#89173](https://github.com/openclaw/openclaw/issues/89173) | Closed in local gitcrawl | External plugin tools (memory_store, memory_recall, etc.) not routed/exposed to the Agent in v2026.5.27+; no longer open. |
| [#89167](https://github.com/openclaw/openclaw/issues/89167) | Closed in local gitcrawl | Session in status:failed remains bound as agent:main:main, crashing next TUI launch; no longer open. |
| [#89165](https://github.com/openclaw/openclaw/issues/89165) | Closed in local gitcrawl 2026-06-02 | HTTP 400 quota/usage_limit errors do not trigger provider fallback chain; no longer open. |
| [#89164](https://github.com/openclaw/openclaw/issues/89164) | Closed in local gitcrawl | Completed model responses occasionally do not persist to session jsonl despite trajectory recording success; no longer open. |
| [#89160](https://github.com/openclaw/openclaw/pull/89160) | Closed in local gitcrawl | fix(agents): detect truncated API responses to prevent silent session hang; no longer open. |
| [#89150](https://github.com/openclaw/openclaw/pull/89150) | Closed in local gitcrawl 2026-06-15 | obs(model-fallback): emit `model.fallback.exhausted` counter on chain exhaustion; no longer open. |
| [#89139](https://github.com/openclaw/openclaw/issues/89139) | Closed in local gitcrawl 2026-06-04 | webchat creates new agent run per message, destroying prompt cache (93% → 29% hit rate); no longer open. |
| [#89138](https://github.com/openclaw/openclaw/pull/89138) | Closed in local gitcrawl 2026-06-11 | fix #88009: [Feature]: batched memory embedding should batch over files; no longer open. |
| [#89133](https://github.com/openclaw/openclaw/pull/89133) | Closed in local gitcrawl | Restore GPT-5.3 Codex Spark OAuth routing; no longer open. |
| [#89128](https://github.com/openclaw/openclaw/pull/89128) | Closed in local gitcrawl 2026-06-03 | fix: skip Responses item id replay without store; no longer open. |
| [#89118](https://github.com/openclaw/openclaw/pull/89118) | Closed in local gitcrawl | fix(outbound): sanitize message.send arguments to prevent runtime scaffolding leaks; no longer open. |
| [#89112](https://github.com/openclaw/openclaw/issues/89112) | Closed in local gitcrawl 2026-06-02 | chore: OpenAI API key update requires manual edits in multiple agent auth.json files; no longer open. |
| [#89109](https://github.com/openclaw/openclaw/pull/89109) | Closed in local gitcrawl 2026-06-11 | fix(agents): block message-tool spam loops defeated by volatile message ids; no longer open. |
| [#89102](https://github.com/openclaw/openclaw/pull/89102) | Closed in local gitcrawl 2026-06-06 | refactor(auth): store auth profiles in SQLite; no longer open. |
| [#89091](https://github.com/openclaw/openclaw/pull/89091) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): retry narrative message reads; no longer open. |
| [#89090](https://github.com/openclaw/openclaw/issues/89090) | Closed in local gitcrawl 2026-06-11 | Bug: loopDetection cannot block message tool loops — volatile messageId in result defeats all critical-level detection paths; no longer open. |
| [#89088](https://github.com/openclaw/openclaw/pull/89088) | Closed in local gitcrawl | test(gateway): cover rollover model override preservation; no longer open. |
| [#89087](https://github.com/openclaw/openclaw/issues/89087) | Closed in local gitcrawl | Bug: Session model override lost on UTC midnight rollover; no longer open. |
| [#89070](https://github.com/openclaw/openclaw/pull/89070) | Closed in local gitcrawl 2026-06-04 | fix(stream): handle cumulative JSON chunks from local llama.cpp tool calls; no longer open. |
| [#89051](https://github.com/openclaw/openclaw/issues/89051) | Closed in local gitcrawl | [Bug]: Embedded agent session silently hangs after auto-compaction with no error logging or recovery; no longer open. |
| [#89049](https://github.com/openclaw/openclaw/pull/89049) | Closed in local gitcrawl 2026-06-03 | fix(idle-timeout): honor provider timeout for no-timeout runs; no longer open. |
| [#89032](https://github.com/openclaw/openclaw/issues/89032) | Closed in local gitcrawl 2026-06-02 | MiMo v2.5: reasoning_content not preserved for custom xiaomi-coding provider (400 in multi-turn tool calls); no longer open. |
| [#89029](https://github.com/openclaw/openclaw/pull/89029) | Closed in local gitcrawl | fix(cli): accept empty Claude end turns; no longer open. |
| [#89027](https://github.com/openclaw/openclaw/pull/89027) | Closed in local gitcrawl 2026-06-11 | fix(cli): prevent empty_response failover for completed thinking-only turns; no longer open. |
| [#89016](https://github.com/openclaw/openclaw/pull/89016) | Closed in local gitcrawl | fix(agents): guard OpenAI transport tool descriptors; no longer open. |
| [#89013](https://github.com/openclaw/openclaw/pull/89013) | Closed in local gitcrawl | fix(agents): materialize OpenAI tool schemas; no longer open. |
| [#89008](https://github.com/openclaw/openclaw/issues/89008) | Closed in local gitcrawl 2026-06-03 | claude-cli thinking-only (end_turn, empty text) turns trigger empty_response model-fallback re-run on a different model; no longer open. |
| [#89001](https://github.com/openclaw/openclaw/pull/89001) | Closed in local gitcrawl 2026-06-11 | fix: support Azure Responses text stream events; no longer open. |
| [#88999](https://github.com/openclaw/openclaw/pull/88999) | Closed in local gitcrawl 2026-06-11 | fix(cron): repair concatenated JSON keys from local-model tool-call parsers; no longer open. |
| [#88994](https://github.com/openclaw/openclaw/pull/88994) | Closed in local gitcrawl 2026-06-11 | fix(agents): quarantine normalized runtime tools; no longer open. |
| [#88977](https://github.com/openclaw/openclaw/pull/88977) | Closed in local gitcrawl | fix(agents): tolerate provider tool schema hook failures; no longer open. |
| [#88976](https://github.com/openclaw/openclaw/pull/88976) | Closed in local gitcrawl 2026-06-03 | fix(mistral): enable prompt cache key compat; no longer open. |
| [#88964](https://github.com/openclaw/openclaw/pull/88964) | Closed in local gitcrawl 2026-06-06 | fix(agents): repair context-engine tool-result pairing; no longer open. |
| [#88959](https://github.com/openclaw/openclaw/pull/88959) | Closed in local gitcrawl | fix(plugins): ignore throwing provider runtime hooks; no longer open. |
| [#88958](https://github.com/openclaw/openclaw/pull/88958) | Closed in local gitcrawl 2026-06-12 | Fix BTW OAuth side-question routing; no longer open. |
| [#88956](https://github.com/openclaw/openclaw/pull/88956) | Closed in local gitcrawl 2026-06-12 | Repair compacted tool-result chains; no longer open. |
| [#88950](https://github.com/openclaw/openclaw/pull/88950) | Closed in local gitcrawl | fix(plugins): ignore throwing provider policy hooks; no longer open. |
| [#88946](https://github.com/openclaw/openclaw/pull/88946) | Closed in local gitcrawl 2026-06-03 | Fix live model inference edge cases; no longer open. |
| [#88940](https://github.com/openclaw/openclaw/pull/88940) | Closed in local gitcrawl 2026-06-06 | fix(llm): repairJson injects control chars for backslash b/f/n/r/t into Windows paths; no longer open. |
| [#88938](https://github.com/openclaw/openclaw/issues/88938) | Closed in local gitcrawl 2026-06-02 | [Feature]: know what model is used by the image tool; no longer open. |
| [#88931](https://github.com/openclaw/openclaw/pull/88931) | Closed in local gitcrawl | fix(agents): cap tool search fanout in lean mode; no longer open. |
| [#88928](https://github.com/openclaw/openclaw/pull/88928) | Closed in local gitcrawl 2026-06-02 | fix(llm): preserve Windows path control escapes; no longer open. |
| [#88926](https://github.com/openclaw/openclaw/pull/88926) | Closed in local gitcrawl 2026-06-03 | fix(llm): preserve Windows path escapes in streamed args; no longer open. |
| [#88924](https://github.com/openclaw/openclaw/pull/88924) | Closed in local gitcrawl 2026-06-02 | fix(agents): strip streamed reasoning tags; no longer open. |
| [#88922](https://github.com/openclaw/openclaw/pull/88922) | Closed in local gitcrawl 2026-06-03 | fix(google): forward stop sequences to Gemini generationConfig; no longer open. |
| [#88918](https://github.com/openclaw/openclaw/issues/88918) | Closed in local gitcrawl 2026-06-03 | [Bug]: Streaming repairJson injects control chars into unescaped Windows paths in tool-call arguments; no longer open. |
| [#88917](https://github.com/openclaw/openclaw/pull/88917) | Closed in local gitcrawl 2026-06-12 | fix: retry stale Responses reasoning replay safely; no longer open. |
| [#88907](https://github.com/openclaw/openclaw/issues/88907) | Closed in local gitcrawl | Chronic agent failures on Telegram — LLM timeouts before configured timeout + silent incomplete turns + dead fallbacks (OpenRouter/DeepSeek+V4-Flash, v2026.5.28); no longer open. |
| [#88906](https://github.com/openclaw/openclaw/pull/88906) | Closed in local gitcrawl | fix(openai): allow Codex Spark via harness; no longer open. |
| [#88902](https://github.com/openclaw/openclaw/issues/88902) | Closed in local gitcrawl | [Bug]: Codex OAuth /btw still falls back to OpenAI Responses after /new; no longer open. |
| [#88896](https://github.com/openclaw/openclaw/pull/88896) | Closed in local gitcrawl 2026-06-02 | fix: harden CLI and plugin edge cases; no longer open. |
| [#88893](https://github.com/openclaw/openclaw/pull/88893) | Closed in local gitcrawl 2026-06-11 | fix: support Azure Responses API text content type; no longer open. |
| [#88890](https://github.com/openclaw/openclaw/pull/88890) | Closed in local gitcrawl 2026-06-06 | fix #87768: [Bug]: push to talk mac os companion app hard codes thinking low; no longer open. |
| [#88887](https://github.com/openclaw/openclaw/pull/88887) | Closed in local gitcrawl | fix(memory-core): don't run the LLM reranker in vsearch/search modes; no longer open. |
| [#88884](https://github.com/openclaw/openclaw/pull/88884) | Closed in local gitcrawl | fix(agents): trim web tools in lean mode; no longer open. |
| [#88882](https://github.com/openclaw/openclaw/pull/88882) | Closed in local gitcrawl 2026-06-11 | test(gateway): add small model live profile; no longer open. |
| [#88881](https://github.com/openclaw/openclaw/pull/88881) | Closed in local gitcrawl | fix(agents): trim media tools in lean mode; no longer open. |
| [#88880](https://github.com/openclaw/openclaw/pull/88880) | Closed in local gitcrawl | fix(agents): project nullable tool schemas for providers; no longer open. |
| [#88878](https://github.com/openclaw/openclaw/pull/88878) | Closed in local gitcrawl | fix(agents): project cron tool schemas for providers; no longer open. |
| [#88874](https://github.com/openclaw/openclaw/issues/88874) | Closed in local gitcrawl 2026-06-02 | [Bug]: cron openai/gpt-5.4-mini ignores agentRuntime=openclaw/pi and routes to openai-codex with zero tools; no longer open. |
| [#88873](https://github.com/openclaw/openclaw/pull/88873) | Closed in local gitcrawl 2026-06-02 | fix(agent-os): harden full-local substrate; no longer open. |
| [#88869](https://github.com/openclaw/openclaw/pull/88869) | Closed in local gitcrawl | Follow up MiniMax M3 pricing and PDF extraction defaults; no longer open. |
| [#88864](https://github.com/openclaw/openclaw/issues/88864) | Closed in local gitcrawl | [Bug]: `memory-wiki` bridge imports all workspace artifacts into shared vault, causing `path-mismatch` error; no longer open. |
| [#88861](https://github.com/openclaw/openclaw/pull/88861) | Closed in local gitcrawl 2026-06-02 | Fix OpenResponses callback message context; no longer open. |
| [#88851](https://github.com/openclaw/openclaw/pull/88851) | Closed in local gitcrawl 2026-06-02 | Persist OpenRouter model cache in SQLite; no longer open. |
| [#88837](https://github.com/openclaw/openclaw/pull/88837) | Closed in local gitcrawl | fix(agent): use static catalog for skip-agent model resolution; no longer open. |
| [#88833](https://github.com/openclaw/openclaw/issues/88833) | Closed in local gitcrawl 2026-06-03 | Bug: azure-openai-responses can return non_deliverable_terminal_turn with assistantTexts=[] even when direct Azure /responses succeeds; no longer open. |
| [#88830](https://github.com/openclaw/openclaw/pull/88830) | Closed in local gitcrawl 2026-06-02 | feat(dreaming): score candidates with shadow trial results; no longer open. |
| [#88827](https://github.com/openclaw/openclaw/pull/88827) | Closed in local gitcrawl 2026-06-02 | Add Vertex API key model config regression coverage; no longer open. |
| [#88822](https://github.com/openclaw/openclaw/pull/88822) | Closed in local gitcrawl 2026-06-11 | fix(agents): compact lean local tool catalogs; no longer open. |
| [#88816](https://github.com/openclaw/openclaw/issues/88816) | Closed in local gitcrawl 2026-06-02 | [Bug]: v2026.05.28 breaks Google Vertex Express API Key; no longer open. |
| [#88806](https://github.com/openclaw/openclaw/pull/88806) | Closed in local gitcrawl 2026-06-02 | fix(memory-lancedb): reject envelope metadata sludge (incl. marker-free shapes); no longer open. |
| [#88804](https://github.com/openclaw/openclaw/pull/88804) | Closed in local gitcrawl 2026-06-02 | fix(openai): keep stop-finished tool calls; no longer open. |
| [#88800](https://github.com/openclaw/openclaw/pull/88800) | Closed in local gitcrawl 2026-06-12 | fix(models): keep generated secret refs out of plaintext; no longer open. |
| [#88799](https://github.com/openclaw/openclaw/pull/88799) | Closed in local gitcrawl 2026-06-02 | fix(openai): honor streamed tool calls with stop finish; no longer open. |
| [#88791](https://github.com/openclaw/openclaw/issues/88791) | Closed in local gitcrawl 2026-06-02 | Bug: structured tool_calls with finish_reason stop are dropped as non_deliverable_terminal_turn; no longer open. |
| [#88789](https://github.com/openclaw/openclaw/pull/88789) | Closed in local gitcrawl | feat(agents): auto-trim lean local tools; no longer open. |
| [#88787](https://github.com/openclaw/openclaw/pull/88787) | Closed in local gitcrawl 2026-06-02 | feat(openai): support gpt-5.5 azure routing and reasoning, restrict telegram bot access; no longer open. |
| [#88781](https://github.com/openclaw/openclaw/pull/88781) | Closed in local gitcrawl 2026-06-01 | fix(models): strip remaining provider self prefixes; no longer open. |
| [#88771](https://github.com/openclaw/openclaw/pull/88771) | Closed in local gitcrawl 2026-06-11 | fix(agents): stream phased text deltas incrementally; no longer open. |
| [#88770](https://github.com/openclaw/openclaw/issues/88770) | Closed in local gitcrawl 2026-06-01 | [Bug]: Self-prefix normalization gap remaining in google/xai/openai providers after #88587; no longer open. |
| [#88769](https://github.com/openclaw/openclaw/pull/88769) | Closed in local gitcrawl 2026-06-03 | fix(agents): keep inline <think> reasoning out of OpenAI-compatible visible text; no longer open. |
| [#88767](https://github.com/openclaw/openclaw/pull/88767) | Closed in local gitcrawl 2026-06-02 | fix(plugin-sdk): isolate provider catalog projection failures; no longer open. |
| [#88761](https://github.com/openclaw/openclaw/pull/88761) | Closed in local gitcrawl 2026-06-01 | [codex] Surface disabled Codex plugin routes in doctor lint; no longer open. |
| [#88759](https://github.com/openclaw/openclaw/pull/88759) | Closed in local gitcrawl 2026-06-01 | fix: repair providerless Codex session overrides; no longer open. |
| [#88751](https://github.com/openclaw/openclaw/issues/88751) | Closed in local gitcrawl 2026-06-01 | [Bug]: doctor lint misses disabled codex plugin required by native codex runtime; no longer open. |
| [#88748](https://github.com/openclaw/openclaw/pull/88748) | Closed in local gitcrawl | fix(gemini): bridge OAuth profiles into CLI runtime; no longer open. |
| [#88746](https://github.com/openclaw/openclaw/pull/88746) | Closed in local gitcrawl 2026-06-02 | feat: add Agent OS full-local substrate; no longer open. |
| [#88745](https://github.com/openclaw/openclaw/pull/88745) | Closed in local gitcrawl 2026-06-01 | fix: preserve explicit provider in resolveConfiguredProviderFallback (v2); no longer open. |
| [#88741](https://github.com/openclaw/openclaw/issues/88741) | Closed in local gitcrawl 2026-06-02 | Stream parser duplicates &lt;think&gt; content into both text and thinking parts (CoT leaks to chat channels with minimax/MiniMax-M2.7); no longer open. |
| [#88723](https://github.com/openclaw/openclaw/pull/88723) | Closed in local gitcrawl 2026-06-02 | fix(doctor): respect explicit PI runtime policy; no longer open. |
| [#88719](https://github.com/openclaw/openclaw/pull/88719) | Closed in local gitcrawl 2026-06-01 | fix(auth): enforce canonical openai-codex OAuth owner; no longer open. |
| [#88715](https://github.com/openclaw/openclaw/pull/88715) | Closed in local gitcrawl 2026-06-01 | perf(plugins): avoid duplicate provider hook load probes; no longer open. |
| [#88711](https://github.com/openclaw/openclaw/pull/88711) | Closed in local gitcrawl 2026-06-01 | fix: preserve explicit provider in resolveConfiguredProviderFallback; no longer open. |
| [#88710](https://github.com/openclaw/openclaw/issues/88710) | Closed in local gitcrawl 2026-06-01 | Bug: resolveConfiguredProviderFallback replaces explicit provider/model with wrong provider when default provider is unconfigured; no longer open. |
| [#88708](https://github.com/openclaw/openclaw/issues/88708) | Closed in local gitcrawl 2026-06-01 | memory-tencentdb OpenAI-compatible prompt cache regression; no longer open. |
| [#88705](https://github.com/openclaw/openclaw/issues/88705) | Closed in local gitcrawl 2026-06-11 | Bug: npm updates drop node-llama-cpp, breaking local memory_search after every OpenClaw update; no longer open. |
| [#88704](https://github.com/openclaw/openclaw/pull/88704) | Closed in local gitcrawl 2026-06-02 | fix(memory): rehydrate daily list promotions; no longer open. |
| [#88696](https://github.com/openclaw/openclaw/pull/88696) | Closed in local gitcrawl 2026-06-11 | fix #70559: runUnsafeReindex crashes with "no such table: chunks_vec" when sqlite-vec is enabled; no longer open. |
| [#88693](https://github.com/openclaw/openclaw/pull/88693) | Closed in local gitcrawl 2026-06-01 | docs(openai): clarify openai-codex auth profile mismatch; no longer open. |
| [#88679](https://github.com/openclaw/openclaw/issues/88679) | Closed in local gitcrawl | [Feature]: Per-Tool Model Routing — route specific tool calls to different models; no longer open. |
| [#88672](https://github.com/openclaw/openclaw/pull/88672) | Closed in local gitcrawl 2026-06-01 | fix(plugins): reuse current metadata snapshot in provider hot paths; no longer open. |
| [#88671](https://github.com/openclaw/openclaw/issues/88671) | Closed in local gitcrawl 2026-06-02 | [Bug]: [assistant reasoning omitted] appears with reasoningDefault off on Ollama models; no longer open. |
| [#88669](https://github.com/openclaw/openclaw/pull/88669) | Closed in local gitcrawl 2026-06-01 | fix(auth): skip no-op auth-profile disk writes on success; no longer open. |
| [#88667](https://github.com/openclaw/openclaw/pull/88667) | Closed in local gitcrawl 2026-06-01 | fix #81214: OpenClaw 2026.5.7 subagent regression; no longer open. |
| [#88654](https://github.com/openclaw/openclaw/issues/88654) | Closed in local gitcrawl 2026-06-01 | markAuthProfileSuccess rewrites auth-profiles.json on every success; no longer open. |
| [#88645](https://github.com/openclaw/openclaw/pull/88645) | Closed in local gitcrawl 2026-06-12 | fix(llm): use JSON5 as intermediate fallback in parseStreamingJson to avoid partial-json key corruption; no longer open. |
| [#88644](https://github.com/openclaw/openclaw/issues/88644) | Closed in local gitcrawl 2026-06-01 | doctor --fix breaks Codex model routing by rewriting openai-codex/ to openai/; no longer open. |
| [#88632](https://github.com/openclaw/openclaw/issues/88632) | Closed in local gitcrawl | [Bug]: gateway model-run sessions accumulate until session maxEntries cap; no longer open. |
| [#88630](https://github.com/openclaw/openclaw/pull/88630) | Closed in local gitcrawl 2026-06-12 | fix(codex): avoid guardian review for local models; no longer open. |
| [#88615](https://github.com/openclaw/openclaw/issues/88615) | Closed in local gitcrawl 2026-06-11 | [Bug]: sqlite-vec fails to load on Node 22 Linux x64 (Vector store: unknown, distinct from #64776 and #65033); no longer open. |
| [#88612](https://github.com/openclaw/openclaw/pull/88612) | Closed in local gitcrawl 2026-06-01 | fix(models): keep auth login out of main config; no longer open. |
| [#88608](https://github.com/openclaw/openclaw/pull/88608) | Closed in local gitcrawl 2026-06-02 | fix(minimax): use account OAuth device endpoints; no longer open. |
| [#88596](https://github.com/openclaw/openclaw/issues/88596) | Closed in local gitcrawl 2026-06-02 | xAI models report incorrect context window (200k instead of 1M) — long_context_threshold misinterpreted; no longer open. |
| [#88587](https://github.com/openclaw/openclaw/pull/88587) | Closed in local gitcrawl 2026-06-01 | fix(agents): normalize prefixed Anthropic fallback model ids (#88560); no longer open. |
| [#88579](https://github.com/openclaw/openclaw/issues/88579) | Closed in local gitcrawl | LLM error: Authorization Not Found - SecretRef apiKey not properly resolved in Gateway; no longer open. |
| [#88565](https://github.com/openclaw/openclaw/issues/88565) | Closed in local gitcrawl 2026-06-01 | models auth login overwrites and truncates main openclaw.json; no longer open. |
| [#88563](https://github.com/openclaw/openclaw/pull/88563) | Closed in local gitcrawl 2026-06-01 | fix(agents): resolve exact static-catalog models for plugin-harness cold start (#88510); no longer open. |
| [#88561](https://github.com/openclaw/openclaw/issues/88561) | Closed in local gitcrawl 2026-06-04 | lossless-claw compaction breaks tool_calls/tool message chain → 499 error on model switch; no longer open. |
| [#88560](https://github.com/openclaw/openclaw/issues/88560) | Closed in local gitcrawl 2026-06-01 | fallback iterator leaks one candidate modelId into subsequent provider lookup; no longer open. |
| [#88558](https://github.com/openclaw/openclaw/pull/88558) | Closed in local gitcrawl 2026-06-01 | fix(gateway): enforce OpenAI tool_choice required/function contracts; no longer open. |
| [#88553](https://github.com/openclaw/openclaw/pull/88553) | Closed in local gitcrawl | fix(agents): unblock fallback classification tests; no longer open. |
| [#88551](https://github.com/openclaw/openclaw/pull/88551) | Closed in local gitcrawl | fix(agents): skip auth gate for CLI-owned transport; no longer open. |
| [#88548](https://github.com/openclaw/openclaw/issues/88548) | Closed in local gitcrawl | GitHub Copilot: static default model list shadows live entitlement discovery; no longer open. |
| [#88547](https://github.com/openclaw/openclaw/pull/88547) | Closed in local gitcrawl 2026-06-01 | feat(github-copilot): add Claude Opus 4.8 to default model catalog; no longer open. |
| [#88525](https://github.com/openclaw/openclaw/pull/88525) | Closed in local gitcrawl 2026-06-01 | feat(deepseek): show provider balance in usage status; no longer open. |
| [#88517](https://github.com/openclaw/openclaw/issues/88517) | Closed in local gitcrawl 2026-06-01 | v2026.5.28 regression: claude-haiku-4-5 cron model override fails again; no longer open. |
| [#88516](https://github.com/openclaw/openclaw/pull/88516) | Closed in local gitcrawl 2026-06-01 | fix(doctor): preserve Codex routes in non-interactive repair; no longer open. |
| [#88514](https://github.com/openclaw/openclaw/pull/88514) | Closed in local gitcrawl | fix(gateway): avoid default provider auth startup prewarm; no longer open. |
| [#88512](https://github.com/openclaw/openclaw/pull/88512) | Closed in local gitcrawl 2026-06-02 | fix: resolve google provider default API to google-generative-ai; no longer open. |
| [#88510](https://github.com/openclaw/openclaw/issues/88510) | Closed in local gitcrawl 2026-06-01 | Codex model catalog cold-start miss for gpt-5.3-codex after gateway restart; no longer open. |
| [#88506](https://github.com/openclaw/openclaw/pull/88506) | Closed in local gitcrawl | feat: add per-agent compaction overrides; no longer open. |
| [#88499](https://github.com/openclaw/openclaw/issues/88499) | Closed in local gitcrawl 2026-06-02 | openai-responses provider: 404 on previous_response_id when store=false (default); no longer open. |
| [#88490](https://github.com/openclaw/openclaw/issues/88490) | Closed in local gitcrawl | Session model override from Codex persists in unrelated sessions (e.g. Telegram); no longer open. |
| [#88482](https://github.com/openclaw/openclaw/pull/88482) | Closed in local gitcrawl 2026-06-01 | docs: clarify auth profile provider field after openai-codex OAuth login; no longer open. |
| [#88480](https://github.com/openclaw/openclaw/issues/88480) | Closed in local gitcrawl 2026-06-01 | Google Gemini chat model routes to openai-responses transport (401), native @google/genai transport never selected; no longer open. |
| [#88470](https://github.com/openclaw/openclaw/issues/88470) | Closed in local gitcrawl 2026-06-01 | [Bug]: Title: OpenAI GPT-5.5 fails through Codex runtime after upgrade to OpenClaw 2026.5.28; no longer open. |
| [#88468](https://github.com/openclaw/openclaw/pull/88468) | Closed in local gitcrawl 2026-06-01 | fix(configure): migrate stale Codex defaults after OpenAI auth; no longer open. |
| [#88460](https://github.com/openclaw/openclaw/pull/88460) | Closed in local gitcrawl 2026-06-15 | fix(cron): recover from local-llamacpp parameter serialization bugs; no longer open. |
| [#88457](https://github.com/openclaw/openclaw/issues/88457) | Closed in local gitcrawl | [Bug]: opencode-go works via direct infer but fails in embedded agent runtime with session takeover; no longer open. |
| [#88439](https://github.com/openclaw/openclaw/issues/88439) | Closed in local gitcrawl 2026-06-03 | [Bug]: cron tool: local llamacpp model parameter serialization corrupts JSON property names (key concatenation); no longer open. |
| [#88400](https://github.com/openclaw/openclaw/pull/88400) | Closed in local gitcrawl | fix(config): accept overlays for bundled provider aliases; no longer open. |
| [#88381](https://github.com/openclaw/openclaw/pull/88381) | Closed in local gitcrawl 2026-06-01 | fix(agents): preserve runtime tools in lean mode; no longer open. |
| [#88378](https://github.com/openclaw/openclaw/pull/88378) | Closed in local gitcrawl 2026-06-01 | fix(xiaomi): support MiMo voicedesign TTS; no longer open. |
| [#88366](https://github.com/openclaw/openclaw/pull/88366) | Closed in local gitcrawl 2026-06-01 | fix(agents): preserve required replies in lean local mode; no longer open. |
| [#88357](https://github.com/openclaw/openclaw/issues/88357) | Closed in local gitcrawl 2026-06-03 | Bug: apply_patch unavailable on non-OpenAI providers due to hardcoded isOpenAIProvider gate; no longer open. |
| [#88351](https://github.com/openclaw/openclaw/pull/88351) | Closed in local gitcrawl 2026-06-01 | fix(plugin-sdk): isolate provider catalog projection failures; no longer open. |
| [#88320](https://github.com/openclaw/openclaw/pull/88320) | Closed in local gitcrawl 2026-06-01 | fix(agents): recover DeepSeek DSML tool calls; no longer open. |
| [#88289](https://github.com/openclaw/openclaw/pull/88289) | Closed in local gitcrawl 2026-06-02 | fix(microsoft-foundry): skip DeepSeek V4 thinking params on Foundry fallback; no longer open. |
| [#88275](https://github.com/openclaw/openclaw/pull/88275) | Closed in local gitcrawl 2026-05-31 | fix(models-config): allow self-hosted providers without apiKey in models.json (#88267); no longer open. |
| [#88267](https://github.com/openclaw/openclaw/issues/88267) | Closed in local gitcrawl 2026-06-01 | [Bug]:; no longer open. |
| [#88266](https://github.com/openclaw/openclaw/pull/88266) | Closed in local gitcrawl 2026-05-31 | refactor: extract model catalog core package; no longer open. |
| [#88263](https://github.com/openclaw/openclaw/pull/88263) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): use native recursive fs.watch in QMD watcher to prevent per-file FD leak; no longer open. |
| [#88247](https://github.com/openclaw/openclaw/pull/88247) | Closed in local gitcrawl 2026-05-31 | feat: add hosted model providers; no longer open. |
| [#88241](https://github.com/openclaw/openclaw/pull/88241) | Closed in local gitcrawl 2026-06-02 | test(crabbox): pin wrapper provider expectations; no longer open. |
| [#88238](https://github.com/openclaw/openclaw/pull/88238) | Closed in local gitcrawl 2026-06-02 | perf(memory): batch memory embeddings across files; no longer open. |
| [#88237](https://github.com/openclaw/openclaw/pull/88237) | Closed in local gitcrawl 2026-05-31 | fix(agents): preserve qualified model alias targets; no longer open. |
| [#88232](https://github.com/openclaw/openclaw/pull/88232) | Closed in local gitcrawl 2026-05-31 | fix(models): prefer exact configured provider refs before aliases; no longer open. |
| [#88218](https://github.com/openclaw/openclaw/issues/88218) | Closed in local gitcrawl 2026-05-31 | [Bug]: agents.defaults.models aliases silently re-resolve target refs to openai/<alias-key> on 5.x; no longer open. |
| [#88212](https://github.com/openclaw/openclaw/pull/88212) | Closed in local gitcrawl | feat(agents): auto-trim lean local model tools; no longer open. |
| [#88181](https://github.com/openclaw/openclaw/pull/88181) | Closed in local gitcrawl | feat(agents): add strict local model lean profile; no longer open. |
| [#88145](https://github.com/openclaw/openclaw/pull/88145) | Closed in local gitcrawl 2026-05-31 | feat: add Hermes provider parity for hosted models; no longer open. |
| [#88135](https://github.com/openclaw/openclaw/pull/88135) | Closed in local gitcrawl 2026-05-31 | fix(codex): refresh stale managed runtime plugin; no longer open. |
| [#88130](https://github.com/openclaw/openclaw/pull/88130) | Closed in local gitcrawl 2026-05-31 | fix(agents): preserve Codex auth for compaction fallback; no longer open. |
| [#88125](https://github.com/openclaw/openclaw/issues/88125) | Closed in local gitcrawl 2026-06-01 | [Docs] Clarify auth profile provider field after openai-codex OAuth login; no longer open. |
| [#88120](https://github.com/openclaw/openclaw/issues/88120) | Closed live 2026-05-30 | [Bug]: 2026.5.27 upgrade leaves stale Codex plugin providerIds, breaking openai/gpt-5.5 route and status usage workaround; no longer open. |
| [#88110](https://github.com/openclaw/openclaw/pull/88110) | Closed in local gitcrawl 2026-05-31 | fix(session): normalize codex oauth session routes; no longer open. |
| [#88108](https://github.com/openclaw/openclaw/pull/88108) | Closed in local gitcrawl 2026-06-11 | fix(agents): compact lean local tool catalogs; no longer open. |
| [#88102](https://github.com/openclaw/openclaw/issues/88102) | Closed in local gitcrawl 2026-05-31 | [Bug]: 2026.5.27 Codex runtime rejects openai/gpt-5.5; codex/gpt-5.5 workaround drops Telegram /status usage; no longer open. |
| [#88098](https://github.com/openclaw/openclaw/pull/88098) | Closed in local gitcrawl | feat(onboard): add --custom-context-window flag for non-interactive setup; no longer open. |
| [#88091](https://github.com/openclaw/openclaw/issues/88091) | Closed in local gitcrawl 2026-05-31 | Guard MiniMax OAuth fetches in bundled plugin runtime; no longer open. |
| [#88086](https://github.com/openclaw/openclaw/pull/88086) | Closed in local gitcrawl 2026-05-31 | fix(minimax): guard oauth fetches; no longer open. |
| [#88082](https://github.com/openclaw/openclaw/pull/88082) | Closed in local gitcrawl | feat(stepfun): add step-3.7-flash model; no longer open. |
| [#88072](https://github.com/openclaw/openclaw/pull/88072) | Closed in local gitcrawl 2026-05-31 | fix(agents): classify expired thinking signatures; no longer open. |
| [#88071](https://github.com/openclaw/openclaw/pull/88071) | Closed in local gitcrawl 2026-06-01 | fix(config): add dropReasoningFromHistory config for openai-completions providers (#88068); no longer open. |
| [#88068](https://github.com/openclaw/openclaw/issues/88068) | Closed in local gitcrawl 2026-06-01 | [Bug]: No config key to override dropReasoningFromHistory for openai-completions providers; no longer open. |
| [#88067](https://github.com/openclaw/openclaw/pull/88067) | Closed in local gitcrawl 2026-05-31 | fix(responses): drop orphaned assistant msg_* id when reasoning is dropped (#88019); no longer open. |
| [#88065](https://github.com/openclaw/openclaw/issues/88065) | Closed in local gitcrawl 2026-05-31 | Gateway crash on exit: SIGABRT in ggml_metal_rsets_free (node-llama-cpp Metal backend); no longer open. |
| [#88049](https://github.com/openclaw/openclaw/pull/88049) | Closed in local gitcrawl 2026-06-03 | fix(status): exclude session-selected model from fallback display list; no longer open. |
| [#88039](https://github.com/openclaw/openclaw/issues/88039) | Closed in local gitcrawl 2026-06-03 | [Bug]: Session-selected model incorrectly included in fallback list in v2026.5.26; no longer open. |
| [#88019](https://github.com/openclaw/openclaw/issues/88019) | Closed in local gitcrawl 2026-05-31 | [Bug]: Azure Responses session replay keeps msg id without required reasoning after fallback; no longer open. |
| [#88009](https://github.com/openclaw/openclaw/issues/88009) | Closed in local gitcrawl 2026-06-11 | [Feature]: batched memory embedding should batch over files; no longer open. |
| [#87996](https://github.com/openclaw/openclaw/issues/87996) | Closed in local gitcrawl | Vertex beta INVALID_ARGUMENT can wedge long sessions without actionable recovery; no longer open. |
| [#87963](https://github.com/openclaw/openclaw/pull/87963) | Closed in local gitcrawl 2026-05-31 | fix(agents): downgrade thinking blocks with empty signatures to text before anthropic-messages replay; no longer open. |
| [#87958](https://github.com/openclaw/openclaw/pull/87958) | Closed in local gitcrawl | fix(agents): scale read output for small contexts; no longer open. |
| [#87955](https://github.com/openclaw/openclaw/pull/87955) | Closed in local gitcrawl | fix(agents): keep lean tools behind catalog controls; no longer open. |
| [#87943](https://github.com/openclaw/openclaw/issues/87943) | Closed in local gitcrawl 2026-06-15 | feat: Add Xiaomi MiMo Web Search provider; no longer open. |
| [#87940](https://github.com/openclaw/openclaw/pull/87940) | Closed in local gitcrawl 2026-06-04 | fix(gateway): keep dense stream updates incremental; no longer open. |
| [#87935](https://github.com/openclaw/openclaw/issues/87935) | Closed in local gitcrawl 2026-05-31 | feat: Add Xiaomi MiMo Web Search provider; no longer open. |
| [#87933](https://github.com/openclaw/openclaw/pull/87933) | Closed in local gitcrawl 2026-06-11 | fix(agents): respect compat.thinkingFormat override for DeepSeek V4 models; no longer open. |
| [#87927](https://github.com/openclaw/openclaw/pull/87927) | Closed in local gitcrawl | fix(agents): cap compaction budgets for small contexts; no longer open. |
| [#87923](https://github.com/openclaw/openclaw/pull/87923) | Closed in local gitcrawl | fix(thinking): keep explicit session thinkingLevel when runtime downgrades (#87740); no longer open. |
| [#87920](https://github.com/openclaw/openclaw/pull/87920) | Closed in local gitcrawl 2026-05-31 | feat(gateway): forward OpenAI stop sequences through chat completions; no longer open. |
| [#87907](https://github.com/openclaw/openclaw/pull/87907) | Closed in local gitcrawl 2026-06-03 | fix(memory): validate memory index identity; no longer open. |
| [#87895](https://github.com/openclaw/openclaw/pull/87895) | Closed in local gitcrawl | test(agents): broaden small live hosted model matrix; no longer open. |
| [#87893](https://github.com/openclaw/openclaw/pull/87893) | Closed in local gitcrawl 2026-06-15 | fix(auth-profiles): repair stale auto runtime auth selection; no longer open. |
| [#87881](https://github.com/openclaw/openclaw/issues/87881) | Closed in local gitcrawl 2026-06-11 | Gap Analysis: v2026.5.27 config keys rejected as unknown by schema; no longer open. |
| [#87877](https://github.com/openclaw/openclaw/issues/87877) | Closed in local gitcrawl 2026-05-31 | Codex runtime persists openai-codex as session modelProvider, causing recurring legacy route doctor warning; no longer open. |
| [#87876](https://github.com/openclaw/openclaw/issues/87876) | Closed in local gitcrawl | Bug: Bedrock Converse Streaming silently aborts on long-context agent sessions (~6 min timeout, no retry, no fallback); no longer open. |
| [#87874](https://github.com/openclaw/openclaw/pull/87874) | Closed in local gitcrawl 2026-06-02 | fix(macos): inherit thinking for voice wake forwarding; no longer open. |
| [#87862](https://github.com/openclaw/openclaw/pull/87862) | Closed in local gitcrawl 2026-05-31 | Add Claude Opus 4.8 defaults; no longer open. |
| [#87856](https://github.com/openclaw/openclaw/pull/87856) | Closed in local gitcrawl 2026-06-11 | fix(agents): count streamed model deltas incrementally; no longer open. |
| [#87854](https://github.com/openclaw/openclaw/issues/87854) | Closed in local gitcrawl 2026-06-02 | Memory Dreaming Promotion: candidates found but applied=0 (rehydratePromotionCandidate returns null for all); no longer open. |
| [#87851](https://github.com/openclaw/openclaw/pull/87851) | Closed in local gitcrawl 2026-05-31 | fix(agents): preserve logical OpenAI session routes; no longer open. |
| [#87850](https://github.com/openclaw/openclaw/pull/87850) | Closed in local gitcrawl | fix(agents): avoid constructing lean local model tools; no longer open. |
| [#87838](https://github.com/openclaw/openclaw/pull/87838) | Closed in local gitcrawl 2026-06-02 | test(agents): include Ollama in small live model matrix; no longer open. |
| [#87835](https://github.com/openclaw/openclaw/pull/87835) | Closed in local gitcrawl 2026-05-31 | fix(agents): add opus-4-8 to adaptive thinking allowlist; no longer open. |
| [#87833](https://github.com/openclaw/openclaw/pull/87833) | Closed in local gitcrawl 2026-05-31 | fix: probe stale rate-limit cooldown primaries; no longer open. |
| [#87819](https://github.com/openclaw/openclaw/pull/87819) | Closed in local gitcrawl 2026-05-31 | fix: remove reset hint from pinned model status; no longer open. |
| [#87818](https://github.com/openclaw/openclaw/pull/87818) | Closed in local gitcrawl 2026-06-01 | fix(ollama): yield during dense stream processing; no longer open. |
| [#87802](https://github.com/openclaw/openclaw/pull/87802) | Closed in local gitcrawl 2026-05-31 | feat(opencode): add resolveDynamicModel and augmentModelCatalog hooks to Zen plugin; no longer open. |
| [#87801](https://github.com/openclaw/openclaw/issues/87801) | Closed in local gitcrawl 2026-06-01 | supportsAdaptiveThinking() omits opus-4-8 → reasoning-enabled requests send thinking.type.enabled → 400 + silent fallback; no longer open. |
| [#87794](https://github.com/openclaw/openclaw/pull/87794) | Closed in local gitcrawl 2026-05-31 | refactor(tts): catalog voice models through providers; no longer open. |
| [#87768](https://github.com/openclaw/openclaw/issues/87768) | Closed in local gitcrawl 2026-06-03 | [Bug]: push to talk mac os companion app hard codes thinking low; no longer open. |
| [#87766](https://github.com/openclaw/openclaw/issues/87766) | Closed in local gitcrawl 2026-06-11 | [Bug] Kimi web_search always returns "ungrounded" error — Moonshot API no longer returns search_results field[Bug]:; no longer open. |
| [#87762](https://github.com/openclaw/openclaw/pull/87762) | Closed in local gitcrawl 2026-05-31 | feat(opencode): support separate Zen and Go API key env vars; no longer open. |
| [#87752](https://github.com/openclaw/openclaw/issues/87752) | Closed in local gitcrawl | [Bug]: Failover selects unconfigured model MiniMax-M2.7-highspeed causing complete session failure; no longer open. |
| [#87746](https://github.com/openclaw/openclaw/issues/87746) | Closed in local gitcrawl 2026-06-03 | Add Claude Opus 4.8 (`claude-opus-4-8`) to the model catalog; no longer open. |
| [#87740](https://github.com/openclaw/openclaw/issues/87740) | Closed in local gitcrawl 2026-06-03 | Bug: Explicit thinkingLevel session override permanently reset to 'off' after each agent turn; no longer open. |
| [#87737](https://github.com/openclaw/openclaw/issues/87737) | Closed in local gitcrawl 2026-06-02 | DeepSeek V4 thinking wrapper ignores thinkingFormat compat override, breaks Azure Foundry deployments; no longer open. |
| [#87719](https://github.com/openclaw/openclaw/pull/87719) | Closed in local gitcrawl 2026-05-29 | fix(anthropic): stop migrating current claude-haiku-4-5 to sonnet; no longer open. |
| [#87705](https://github.com/openclaw/openclaw/pull/87705) | Closed in local gitcrawl 2026-06-06 | fix(agents): make subagent-control timeout configurable; no longer open. |
| [#87697](https://github.com/openclaw/openclaw/pull/87697) | Closed in local gitcrawl | fix(auth): clear stale provider cooldowns after reauth; no longer open. |
| [#87675](https://github.com/openclaw/openclaw/pull/87675) | Closed in local gitcrawl 2026-05-29 | fix(ollama): promote plain text tool calls; no longer open. |
| [#87642](https://github.com/openclaw/openclaw/issues/87642) | Closed in local gitcrawl | Expose subagent-control waitForRun timeout as a config knob (hardcoded 30s blocks slow local LLMs); no longer open. |
| [#87641](https://github.com/openclaw/openclaw/issues/87641) | Closed in local gitcrawl 2026-05-31 | `opencode-go/kimi-k2.6`: every multi-turn task rejected with opaque 400 "Provider returned error" (reason=format), rotates to fallback (2026.5.26+5.27); no longer open. |
| [#87638](https://github.com/openclaw/openclaw/pull/87638) | Closed in local gitcrawl 2026-05-29 | test(agents): add small model live profile; no longer open. |
| [#87628](https://github.com/openclaw/openclaw/pull/87628) | Closed in local gitcrawl 2026-06-03 | feat(agents): inherit requester model for subagents; no longer open. |
| [#87621](https://github.com/openclaw/openclaw/pull/87621) | Closed in local gitcrawl 2026-05-29 | fix(ollama): yield during dense ndjson bursts; no longer open. |
| [#87619](https://github.com/openclaw/openclaw/pull/87619) | Closed in local gitcrawl 2026-06-11 | fix(diagnostics): account stream deltas incrementally; no longer open. |
| [#87617](https://github.com/openclaw/openclaw/pull/87617) | Closed in local gitcrawl | fix(agents): broaden local model lean profile; no longer open. |
| [#87616](https://github.com/openclaw/openclaw/issues/87616) | Closed in local gitcrawl 2026-06-02 | [Bug]: GatewayClientRequestError: FailoverError: LLM request timed out.; no longer open. |
| [#87608](https://github.com/openclaw/openclaw/issues/87608) | Closed in local gitcrawl 2026-05-31 | [Bug] Ollama Cloud rate-limit cooldown permanently blocks agents — not released after API recovery; no longer open. |
| [#87606](https://github.com/openclaw/openclaw/pull/87606) | Closed in local gitcrawl 2026-05-29 | fix(active-memory): raise recall timeout ceiling; no longer open. |
| [#87603](https://github.com/openclaw/openclaw/issues/87603) | Closed in local gitcrawl 2026-06-06 | lossless-claw contextThreshold does not adapt to actual model context window after fallback; no longer open. |
| [#87596](https://github.com/openclaw/openclaw/pull/87596) | Closed in local gitcrawl 2026-06-15 | fix(moonshot): rewrite duplicate native Kimi tool_call ids on replay; no longer open. |
| [#87594](https://github.com/openclaw/openclaw/pull/87594) | Closed in local gitcrawl 2026-05-29 | fix(openrouter): apply strict9 tool_call_id sanitisation for Mistral routes; no longer open. |
| [#87593](https://github.com/openclaw/openclaw/pull/87593) | Closed in local gitcrawl 2026-05-29 | fix(agents): preserve reasoning_content replay across DeepSeek tier suffixes; no longer open. |
| [#87587](https://github.com/openclaw/openclaw/pull/87587) | Closed in local gitcrawl | fix(agents): keep exec visible for lean local models; no longer open. |
| [#87586](https://github.com/openclaw/openclaw/issues/87586) | Closed in local gitcrawl | [Feature]: Unixsocket Provider plugin; no longer open. |
| [#87575](https://github.com/openclaw/openclaw/issues/87575) | Closed in local gitcrawl 2026-05-29 | Bug: DeepSeek V4 Flash Free via OpenCode Zen provider fails with 400 on follow-up API calls; no longer open. |
| [#87572](https://github.com/openclaw/openclaw/pull/87572) | Closed in local gitcrawl | fix(memory): increase QMD embedTimeoutMs default to 600s for local GG…; no longer open. |
| [#87562](https://github.com/openclaw/openclaw/pull/87562) | Closed in local gitcrawl 2026-06-12 | fix(openrouter): reconcile streamed cost with /generation total_cost; no longer open. |
| [#87558](https://github.com/openclaw/openclaw/pull/87558) | Closed in local gitcrawl 2026-06-02 | fix(gateway): keep dense stream updates incremental; no longer open. |
| [#87538](https://github.com/openclaw/openclaw/pull/87538) | Closed in local gitcrawl 2026-06-01 | fix(agents): model-scope cooldown for transport timeout (#87462); no longer open. |
| [#87484](https://github.com/openclaw/openclaw/pull/87484) | Closed in local gitcrawl 2026-06-02 | fix(agents): clear legacy auto fallback pins; no longer open. |
| [#87480](https://github.com/openclaw/openclaw/pull/87480) | Closed in local gitcrawl | fix(anthropic): configure undici Agent with extended keep-alive to prevent socket failures; no longer open. |
| [#87467](https://github.com/openclaw/openclaw/issues/87467) | Closed in local gitcrawl 2026-06-02 | [Bug]: Auto rate-limit fallback override still pins Discord session to fallback after primary recovers; no longer open. |
| [#87463](https://github.com/openclaw/openclaw/pull/87463) | Closed in local gitcrawl 2026-05-31 | fix(session): normalize openai-codex provider to openai for session route persistence; no longer open. |
| [#87462](https://github.com/openclaw/openclaw/issues/87462) | Closed in local gitcrawl 2026-06-01 | [Bug]: Auth profile cooldown triggers chain exhaustion without actual Google API errors in v2026.5.26; no longer open. |
| [#87456](https://github.com/openclaw/openclaw/pull/87456) | Closed in local gitcrawl 2026-05-29 | Restore Codex Spark OAuth routes; no longer open. |
| [#87436](https://github.com/openclaw/openclaw/issues/87436) | Closed in local gitcrawl 2026-05-31 | Codex harness runs recreate legacy openai-codex session route state after doctor --fix; no longer open. |
| [#87416](https://github.com/openclaw/openclaw/pull/87416) | Closed in local gitcrawl 2026-05-29 | fix(agents): resolve Codex runtime models first; no longer open. |
| [#87404](https://github.com/openclaw/openclaw/pull/87404) | Closed in local gitcrawl | fix(agents): honor ACP alias model.primary overrides (Fixes #87381); no longer open. |
| [#87393](https://github.com/openclaw/openclaw/pull/87393) | Closed in local gitcrawl | fix(media): suppress local whisper progress transcripts; no longer open. |
| [#87384](https://github.com/openclaw/openclaw/issues/87384) | Closed in local gitcrawl | Bug: CLI audio transcription can use progress stdout when transcript file is empty; no longer open. |
| [#87381](https://github.com/openclaw/openclaw/issues/87381) | Closed in local gitcrawl 2026-06-03 | ACP runtime ignores per-agent model.primary override; no longer open. |
| [#87296](https://github.com/openclaw/openclaw/pull/87296) | Closed in local gitcrawl | feat: group model select with collapsible panel in Control UI; no longer open. |
| [#87285](https://github.com/openclaw/openclaw/issues/87285) | Closed in local gitcrawl | Gateway frequent restarts: config reload too aggressive + auth pre-warm blocks event loop; no longer open. |
| [#87274](https://github.com/openclaw/openclaw/pull/87274) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor OpenAI-compatible cache retention; no longer open. |
| [#87262](https://github.com/openclaw/openclaw/issues/87262) | Closed in local gitcrawl | [Bug]: qqbot + ollama + local model: qwen3.5:27b report: error Embedded agent failed before reply: LLM request failed: network connection was interrupted; no longer open. |
| [#87252](https://github.com/openclaw/openclaw/pull/87252) | Closed in local gitcrawl 2026-05-28 | fix(agents): use runtime alias equivalence in live model switch comparison; no longer open. |
| [#87225](https://github.com/openclaw/openclaw/pull/87225) | Closed in local gitcrawl 2026-05-28 | fix(memory): salvage qmd search JSON after nonzero exit; no longer open. |
| [#87170](https://github.com/openclaw/openclaw/issues/87170) | Closed in local gitcrawl | Agent always returns "Provider returned error" with auto model after gateway restart; no longer open. |
| [#87168](https://github.com/openclaw/openclaw/issues/87168) | Closed in local gitcrawl | Codex-authenticated installs can auto-select direct OpenAI for image media understanding without OPENAI_API_KEY; no longer open. |
| [#87110](https://github.com/openclaw/openclaw/issues/87110) | Closed in local gitcrawl | When calling a VLLM model, the usage page statistics show no data. How can I calculate usage and cost when using VLLM?; no longer open. |
| [#86880](https://github.com/openclaw/openclaw/issues/86880) | Closed in local gitcrawl 2026-06-01 | [Bug]: Context Overflow Bug With OpenRouter Models (Latest Version 2026.05.22); no longer open. |
| [#86868](https://github.com/openclaw/openclaw/issues/86868) | Closed in local gitcrawl | Embedded runtime: model fallback chain breaks at intermediate candidates instead of walking to the last entry; no longer open. |
| [#86813](https://github.com/openclaw/openclaw/issues/86813) | Closed in local gitcrawl | `/new` does not clear persisted model override in channel-bound sessions; no longer open. |
| [#86773](https://github.com/openclaw/openclaw/issues/86773) | Closed in local gitcrawl | Provider auth prewarm can starve gateway event loop and cause sessions.list timeouts after restart; no longer open. |
| [#86765](https://github.com/openclaw/openclaw/pull/86765) | Closed in local gitcrawl 2026-05-28 | [codex] Fix memory close sync race; no longer open. |
| [#86752](https://github.com/openclaw/openclaw/issues/86752) | Closed in local gitcrawl | [Bug]: 2026.5.22 Docker/WSL2 gateway event-loop starvation, 284s provider-auth prewarm, slow Telegram turn, and local RPC timeouts; no longer open. |
| [#86748](https://github.com/openclaw/openclaw/pull/86748) | Closed in local gitcrawl 2026-05-28 | perf(plugins): resolve provider policy from current snapshot first; no longer open. |
| [#86702](https://github.com/openclaw/openclaw/issues/86702) | Closed in local gitcrawl 2026-05-28 | MemoryIndexManager.close() races with in-flight sync — provider/DB closed before sync settles; no longer open. |
| [#86690](https://github.com/openclaw/openclaw/pull/86690) | Closed in local gitcrawl 2026-05-28 | fix(plugin-sdk): preserve string-const unions as flat enum for deepseek tool schemas; no longer open. |
| [#86689](https://github.com/openclaw/openclaw/pull/86689) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor per-agent thinking defaults for ingress runs; no longer open. |
| [#86669](https://github.com/openclaw/openclaw/issues/86669) | Closed in local gitcrawl 2026-05-28 | [Bug]: openclaw openai-compat /v1/chat/completions strips chat_template_kwargs entirely on vLLM/Nemotron — causes reasoning-only death-spiral; no longer open. |
| [#86644](https://github.com/openclaw/openclaw/pull/86644) | Closed in local gitcrawl 2026-05-28 | fix(models): skip wildcard catalog aliases; no longer open. |
| [#86637](https://github.com/openclaw/openclaw/pull/86637) | Closed in local gitcrawl | fix(agents): cap DSML recovery buffer to prevent unbounded memory growth; no longer open. |
| [#86633](https://github.com/openclaw/openclaw/pull/86633) | Closed in local gitcrawl 2026-05-31 | fix(ollama): yield during dense stream processing; no longer open. |
| [#86613](https://github.com/openclaw/openclaw/issues/86613) | Closed in local gitcrawl 2026-05-28 | [Bug]: Every memory_search call leaks ~N FDs (one per .md file in workspace memory tree) on macOS; long-lived gateways degrade toward FD exhaustion; no longer open. |
| [#86599](https://github.com/openclaw/openclaw/issues/86599) | Closed in local gitcrawl 2026-06-11 | [Bug]: Local model provider calls thread block gateway event loop on Windows beta; trivial infer run takes ~4 minutes; no longer open. |
| [#86564](https://github.com/openclaw/openclaw/pull/86564) | Closed in local gitcrawl | fix(gateway): disable provider auth prewarm by default; no longer open. |
| [#86554](https://github.com/openclaw/openclaw/pull/86554) | Closed in local gitcrawl | fix(agents): add missing DeepSeek V4 proxy models to reasoning_content replay set; no longer open. |
| [#86552](https://github.com/openclaw/openclaw/pull/86552) | Closed in local gitcrawl 2026-05-28 | perf(agents): reuse manifest metadata during model resolution; no longer open. |
| [#86551](https://github.com/openclaw/openclaw/pull/86551) | Closed in local gitcrawl | fix(agents): add missing DeepSeek V4 proxy models to reasoning_content replay set; no longer open. |
| [#86521](https://github.com/openclaw/openclaw/issues/86521) | Closed in local gitcrawl | fix: preserve reasoning_content for DeepSeek models through proxy providers (opencode-native); no longer open. |
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
| [#86090](https://github.com/openclaw/openclaw/issues/86090) | Closed in local gitcrawl | runHeartbeatOnce returns {status: "ran"} in 78ms on idle agent — phantom run, no model turn executed; no longer open. |
| [#86065](https://github.com/openclaw/openclaw/issues/86065) | Closed in local gitcrawl 2026-05-29 | [Enhancement]: Increase or make configurable the Active Memory timeoutMs hard cap; no longer open. |
| [#86048](https://github.com/openclaw/openclaw/issues/86048) | Closed in local gitcrawl 2026-06-03 | WSL2 GPU-PV driver lockup: nvidia-smi hangs after llama-server D-state crash; no longer open. |
| [#86044](https://github.com/openclaw/openclaw/issues/86044) | Closed in local gitcrawl 2026-06-03 | 2026.5.22: CLI hangs on Windows — provider auth-state pre-warm blocks all CLI commands; no longer open. |
| [#86032](https://github.com/openclaw/openclaw/pull/86032) | Closed in local gitcrawl 2026-05-31 | fix(agents): recover DeepSeek DSML tool markup into synthetic tool calls; no longer open. |
| [#86003](https://github.com/openclaw/openclaw/pull/86003) | Closed in local gitcrawl 2026-05-28 | fix(gateway): add provider auth prewarm operator controls; no longer open. |
| [#85931](https://github.com/openclaw/openclaw/pull/85931) | Closed in local gitcrawl 2026-06-01 | fix(memory): serialize qmd update writes across processes to stop SQLITE_BUSY; no longer open. |
| [#85918](https://github.com/openclaw/openclaw/issues/85918) | Closed in local gitcrawl 2026-06-03 | Bug: Foundry DeepSeek V4 tool turns surface DSML text instead of executable tool calls; no longer open. |
| [#85883](https://github.com/openclaw/openclaw/issues/85883) | Closed in local gitcrawl 2026-05-31 | openai-completions provider leaks channel-output JSON to channel (works correctly on ollama provider); no longer open. |
| [#85826](https://github.com/openclaw/openclaw/issues/85826) | Closed in local gitcrawl | [Bug]: Agent stall detector hard-coded 120s threshold kills legitimate long model calls on local vLLM; no longer open. |
| [#85773](https://github.com/openclaw/openclaw/issues/85773) | Closed in local gitcrawl | [Bug]: After reinstalling (v2026.5.20), agents only provide generic replies, completely ignoring workspace files content and skills; no longer open. |
| [#85715](https://github.com/openclaw/openclaw/pull/85715) | Closed in local gitcrawl 2026-05-31 | feat(deepseek): parse leaked DSML tags into synthetic tool calls instead of dropping them; no longer open. |
| [#85382](https://github.com/openclaw/openclaw/issues/85382) | Closed in local gitcrawl | [Bug] post-compaction embedding sync fails with 500 when memorySearch.remote.baseUrl points to non-OpenAI host; no longer open. |
| [#85321](https://github.com/openclaw/openclaw/issues/85321) | Closed in local gitcrawl 2026-06-15 | `wrapStreamRepairMalformedToolCallArguments` clears valid tool call arguments for Moonshot/Kimi provider; no longer open. |
| [#85269](https://github.com/openclaw/openclaw/pull/85269) | Closed in local gitcrawl 2026-05-28 | feat(openai): add generic OpenAI-compatible embeddings; no longer open. |
| [#85267](https://github.com/openclaw/openclaw/issues/85267) | Closed 2026-05-25 | Assigned to osolmaz before close. |
| [#85217](https://github.com/openclaw/openclaw/issues/85217) | Closed in local gitcrawl 2026-05-28 | [Bug]: QMD query mode unusable on macOS Apple Silicon — Metal GPU cleanup crash discards valid search results; no longer open. |
| [#85192](https://github.com/openclaw/openclaw/issues/85192) | Closed in local gitcrawl | DeepSeek V4: isSignedThinkingBlock misses unsigned thinking blocks — reasoning-only retry fails; no longer open. |
| [#85161](https://github.com/openclaw/openclaw/issues/85161) | Closed in local gitcrawl 2026-05-31 | [Bug]: valid tool call XML in LLM reasoning block is sometimes executed by gateway; no longer open. |
| [#85072](https://github.com/openclaw/openclaw/pull/85072) | Closed in local gitcrawl 2026-05-28 | Deprecate memory-specific embedding provider registration; no longer open. |
| [#84998](https://github.com/openclaw/openclaw/pull/84998) | Closed in local gitcrawl 2026-05-28 | feat(plugins): add OpenAI-compatible embedding provider; no longer open. |
| [#84991](https://github.com/openclaw/openclaw/pull/84991) | Closed in local gitcrawl 2026-05-28 | feat(memory-core): consume generic embedding providers; no longer open. |
| [#84697](https://github.com/openclaw/openclaw/issues/84697) | Closed in local gitcrawl 2026-06-03 | Custom OpenAI-compatible provider with baseUrl without /v1 fails with cryptic 'incomplete terminal response' error; no longer open. |
| [#84621](https://github.com/openclaw/openclaw/pull/84621) | Closed in local gitcrawl 2026-05-29 | Fix Kimi tool-call rewriting stop reason handling; no longer open. |
| [#84581](https://github.com/openclaw/openclaw/pull/84581) | Closed in local gitcrawl | fix(agents): strip plaintext model provider keys; no longer open. |
| [#84384](https://github.com/openclaw/openclaw/issues/84384) | Closed in local gitcrawl 2026-06-03 | [Bug]: Gemini 2.5 Flash via vertex-ai (OpenAI-compatible) streaming times out — thinking tokens not handled; no longer open. |
| [#84228](https://github.com/openclaw/openclaw/pull/84228) | Closed in local gitcrawl 2026-06-15 | fix(nvidia): update Nemotron 3 Super contextWindow to 1M per NVIDIA spec; no longer open. |
| [#84070](https://github.com/openclaw/openclaw/issues/84070) | Closed in local gitcrawl | Active Memory embedded runner fails to expose plugin tools when hidden runner is on the DeepSeek provider path; no longer open. |
| [#83709](https://github.com/openclaw/openclaw/issues/83709) | Closed in local gitcrawl 2026-06-03 | [Feature]: Add `supportsPromptCacheKey` to Mistral transport compat patch; no longer open. |
| [#83461](https://github.com/openclaw/openclaw/issues/83461) | Not resolvable as live issue | Earlier notes referenced it, but live GitHub issue view did not resolve it as an open issue. |
| [#83436](https://github.com/openclaw/openclaw/pull/83436) | Closed in local gitcrawl | fix(agents): rethrow EmbeddedAttemptSessionTakeoverError before model fallback; no longer open. |
| [#83333](https://github.com/openclaw/openclaw/issues/83333) | Closed in local gitcrawl 2026-06-03 | [Bug]: Memory provider cutover to Ollama leaves production index in mixed OpenAI/Ollama vector state after live sync/reload; no longer open. |
| [#83227](https://github.com/openclaw/openclaw/pull/83227) | Closed in local gitcrawl | fix(openai): mark mp3 TTS voice output compatible; no longer open. |
| [#83213](https://github.com/openclaw/openclaw/pull/83213) | Closed in local gitcrawl | [codex] fix(gateway): clear live model switch on reset; no longer open. |
| [#83107](https://github.com/openclaw/openclaw/issues/83107) | Closed in local gitcrawl 2026-05-31 | Model registry name matching is load-bearing — silent fallback to picker selection on registry miss (2026.5.12); no longer open. |
| [#82973](https://github.com/openclaw/openclaw/pull/82973) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor explicit cacheRetention for openai-completions providers; no longer open. |
| [#82887](https://github.com/openclaw/openclaw/pull/82887) | Closed in local gitcrawl 2026-05-31 | fix(cron): preflight model fallbacks before skip; no longer open. |
| [#82594](https://github.com/openclaw/openclaw/issues/82594) | Closed in local gitcrawl 2026-06-06 | [Bug]: openclaw onboard extremely slow on Windows during model loading; no longer open. |
| [#82557](https://github.com/openclaw/openclaw/pull/82557) | Closed in local gitcrawl 2026-06-11 | Allow onboarding to configure multiple model providers; no longer open. |
| [#82145](https://github.com/openclaw/openclaw/pull/82145) | Closed in local gitcrawl | cron: allow retries for local model preflight; no longer open. |
| [#81961](https://github.com/openclaw/openclaw/issues/81961) | Closed in local gitcrawl | [Feature]: Add a simple Dashboard UX to manage multiple model providers; no longer open. |
| [#81530](https://github.com/openclaw/openclaw/issues/81530) | Closed in local gitcrawl 2026-06-03 | [Bug]: [5.12-beta.8] Telegram Supergroup Forum Topics — Inbound Messages Not Processed; no longer open. |
| [#81525](https://github.com/openclaw/openclaw/issues/81525) | Closed in local gitcrawl | [Bug]: media-understanding silently routes images to user-declared vision models without validating declared capabilities; no longer open. |
| [#81443](https://github.com/openclaw/openclaw/pull/81443) | Closed in local gitcrawl | fix: resolve QMD Windows shims and guard image URL downloads; no longer open. |
| [#81281](https://github.com/openclaw/openclaw/issues/81281) | Closed in local gitcrawl 2026-05-28 | [Bug]: OpenAI-completions prompt_cache_key regression — caching worked in 2026.3.x, broken in 2026.5.x; no longer open. |
| [#81249](https://github.com/openclaw/openclaw/issues/81249) | Closed 2026-05-24 | No longer counted as live-open. |
| [#81214](https://github.com/openclaw/openclaw/issues/81214) | Closed in local gitcrawl 2026-06-01 | [Bug]: OpenClaw 2026.5.7 subagent regression; no longer open. |
| [#81170](https://github.com/openclaw/openclaw/pull/81170) | Closed in local gitcrawl 2026-06-01 | fix(openai): preserve custom provider id through memory embedding adapter; no longer open. |
| [#80947](https://github.com/openclaw/openclaw/pull/80947) | Closed in local gitcrawl | fix(doctor): warn and document QMD session recall gates; no longer open. |
| [#80722](https://github.com/openclaw/openclaw/issues/80722) | Closed in local gitcrawl | config set "Restart the gateway to apply" warning is misleading for active agents without agentRuntime override; no longer open. |
| [#80495](https://github.com/openclaw/openclaw/issues/80495) | Closed in local gitcrawl 2026-05-31 | [Bug]: LM Studio Provider Fails: Environment Variable Expansion + API Endpoint Mismatch; no longer open. |
| [#80476](https://github.com/openclaw/openclaw/issues/80476) | Closed in local gitcrawl 2026-05-28 | [Feature]: bundled openai-compatible embedding provider for self-hosted servers (llama.cpp, Ollama, vLLM, TGI, LocalAI); no longer open. |
| [#80379](https://github.com/openclaw/openclaw/issues/80379) | Closed in local gitcrawl 2026-05-28 | [Bug]: Tool result secret redaction mutates session history, breaking KV cache prefix matching for local LLM providers; no longer open. |
| [#80317](https://github.com/openclaw/openclaw/issues/80317) | Closed in local gitcrawl | TTS OpenAI provider: MP3 responseFormat not voice-compatible for Telegram, unlike Edge TTS; no longer open. |
| [#80226](https://github.com/openclaw/openclaw/issues/80226) | Closed 2026-05-25 | No longer counted as live-open. |
| [#79897](https://github.com/openclaw/openclaw/issues/79897) | Closed in local gitcrawl | OpenAI-compatible streaming with llama.cpp saves zero usage (stream closed before final usage chunk); no longer open. |
| [#79745](https://github.com/openclaw/openclaw/pull/79745) | Closed in local gitcrawl 2026-06-12 | Memory/QMD: isolate mcporter sidecars per agent; no longer open. |
| [#79380](https://github.com/openclaw/openclaw/issues/79380) | Closed in local gitcrawl 2026-06-01 | [Bug]: Gateway CPU spin / crash loop on Raspberry Pi 4 (ARM64) — regression from 4.23 to 4.25+; no longer open. |
| [#79329](https://github.com/openclaw/openclaw/issues/79329) | Closed in local gitcrawl 2026-05-31 | Cron model preflight skips entire run when local primary is unreachable, ignoring configured cloud fallbacks [AI]; no longer open. |
| [#78897](https://github.com/openclaw/openclaw/issues/78897) | Closed in local gitcrawl | OpenAI Responses provider should allow store=true for LiteLLM gpt-5.5 continuations; no longer open. |
| [#77792](https://github.com/openclaw/openclaw/issues/77792) | Closed in local gitcrawl 2026-06-01 | fix(tts/xiaomi): support per-call voice and model overrides; no longer open. |
| [#77678](https://github.com/openclaw/openclaw/pull/77678) | Closed in local gitcrawl 2026-05-28 | fix(memory): don't report QMD embeddings as unavailable when searchMode=search; no longer open. |
| [#77655](https://github.com/openclaw/openclaw/issues/77655) | Closed in local gitcrawl 2026-05-31 | Model fallback chain interrupted by race condition — 6 fallback models configured but task terminates before all are tried; no longer open. |
| [#77645](https://github.com/openclaw/openclaw/issues/77645) | Closed in local gitcrawl | memory status --deep reports QMD embeddings unavailable when searchMode=search intentionally disables vectors; no longer open. |
| [#77339](https://github.com/openclaw/openclaw/pull/77339) | Closed in local gitcrawl | fix(auto-reply): clear runtime model cache on reset; no longer open. |
| [#77336](https://github.com/openclaw/openclaw/issues/77336) | Closed in local gitcrawl 2026-06-02 | [Feature Request]: Built-in handling of strict role alternation for Mistral / SGLang backends; no longer open. |
| [#77158](https://github.com/openclaw/openclaw/pull/77158) | Closed in local gitcrawl | perf(qmd): persistent export-state cache + stat fast path in exportSessions; no longer open. |
| [#77053](https://github.com/openclaw/openclaw/pull/77053) | Closed in local gitcrawl | feat(lmstudio): opt-in idle TTL via native load API; no longer open. |
| [#76928](https://github.com/openclaw/openclaw/pull/76928) | Closed in local gitcrawl | feat(plugins): let hooks prefer auth profiles; no longer open. |
| [#76884](https://github.com/openclaw/openclaw/issues/76884) | Closed in local gitcrawl | [Bug]: OpenClaw on native Windows getting notably slower and slower with each new version???; no longer open. |
| [#76741](https://github.com/openclaw/openclaw/pull/76741) | Closed in local gitcrawl 2026-06-03 | fix(kimi): strip anthropic cache markers; no longer open. |
| [#76654](https://github.com/openclaw/openclaw/issues/76654) | Closed in local gitcrawl 2026-05-31 | [webchat] Agent responses disappear after heartbeat tool calls (model-specific, MiMo V2 Pro); no longer open. |
| [#76612](https://github.com/openclaw/openclaw/issues/76612) | Closed in local gitcrawl 2026-06-03 | Kimi Code returns empty content when Anthropic cache_control markers are sent; no longer open. |
| [#76002](https://github.com/openclaw/openclaw/pull/76002) | Closed in local gitcrawl 2026-06-15 | fix(kimi): switch to openai-completions endpoint for image support; no longer open. |
| [#75959](https://github.com/openclaw/openclaw/issues/75959) | Closed in local gitcrawl | [Feature]: Support image analysis for Kimi Code Plan; no longer open. |
| [#75860](https://github.com/openclaw/openclaw/pull/75860) | Closed in local gitcrawl | fix(memory): improve QMD recall for channel queries; no longer open. |
| [#75811](https://github.com/openclaw/openclaw/issues/75811) | Closed in local gitcrawl | [Bug]: `exec` tool schema exposes `security`/`elevated`/`ask` fields as model-controllable; model self-imposes denial; no longer open. |
| [#75720](https://github.com/openclaw/openclaw/issues/75720) | Closed in local gitcrawl 2026-05-28 | [Bug]: Auto-onboard / plugin presets unconditionally overwrite user-set agents.defaults.model.primary; no longer open. |
| [#75657](https://github.com/openclaw/openclaw/issues/75657) | Closed in local gitcrawl 2026-05-29 | fix: local GGUF embedding model warmup blocks Node.js event loop for minutes on startup; no longer open. |
| [#75378](https://github.com/openclaw/openclaw/issues/75378) | Closed in local gitcrawl 2026-06-15 | [Bug] Gateway event loop saturation during parallel subagent spawn causes 1012 restart (v2026.4.29); no longer open. |
| [#75350](https://github.com/openclaw/openclaw/pull/75350) | Closed in local gitcrawl | fix(deepseek): strip reasoning_content from input messages when thinking is enabled; no longer open. |
| [#75312](https://github.com/openclaw/openclaw/issues/75312) | Closed in local gitcrawl | Bug: wiki_search throws 'sharedMemoryManager.search is not a function' when search.backend=shared and corpus includes memory/all; no longer open. |
| [#75301](https://github.com/openclaw/openclaw/issues/75301) | Closed in local gitcrawl | [Feature]: `openclaw caches` command to inspect and prune unbounded `~/.openclaw/` cache dirs (plugin-runtime-deps, browser, tools, orphan transcripts); no longer open. |
| [#75274](https://github.com/openclaw/openclaw/pull/75274) | Closed in local gitcrawl | fix(ollama): per-request URL routing for multi-provider setups; no longer open. |
| [#75267](https://github.com/openclaw/openclaw/pull/75267) | Closed in local gitcrawl | Fix model picker alias/provider scoped options; no longer open. |
| [#75163](https://github.com/openclaw/openclaw/issues/75163) | Closed in local gitcrawl | Bug: TUI mid-session model switch passes raw alias instead of resolved model ID; no longer open. |
| [#75105](https://github.com/openclaw/openclaw/issues/75105) | Closed in local gitcrawl | [Feature]: Allow per-model setting for Deepseek `reasoning_content` fix; no longer open. |
| [#75075](https://github.com/openclaw/openclaw/pull/75075) | Closed in local gitcrawl | feat(gateway): surface built-in tool calls as function_call output items on /v1/responses; no longer open. |
| [#75026](https://github.com/openclaw/openclaw/issues/75026) | Closed in local gitcrawl | MiniMax token usage shows 0 in Control UI Usage page (only message count works); no longer open. |
| [#74910](https://github.com/openclaw/openclaw/issues/74910) | Closed in local gitcrawl | doctor: agents.defaults.llm.idleTimeoutSeconds auto-fix discards the user value; runtime gives no signal until doctor runs; no longer open. |
| [#74900](https://github.com/openclaw/openclaw/issues/74900) | Closed in local gitcrawl | [Feature]: stable public SDK path for embedding provider API (independent of memory-core); no longer open. |
| [#74835](https://github.com/openclaw/openclaw/issues/74835) | Closed in local gitcrawl | Add global provider request proxy/default SSRF policy for model providers; no longer open. |
| [#74761](https://github.com/openclaw/openclaw/pull/74761) | Closed in local gitcrawl | docs: Document oMLX (Apple Silicon MLX) as memorySearch embedding provider; no longer open. |
| [#74644](https://github.com/openclaw/openclaw/issues/74644) | Closed in local gitcrawl 2026-05-31 | mediaUnderstandingProviders audio path hard-requires API key, breaking no-auth/local STT providers; no longer open. |
| [#74403](https://github.com/openclaw/openclaw/pull/74403) | Closed in local gitcrawl | fix(deepseek): strip reasoning_content when extra_body disables thinking; no longer open. |
| [#74315](https://github.com/openclaw/openclaw/pull/74315) | Closed in local gitcrawl 2026-05-31 | fix(agents): remove kimi-coding from normalizeProviderId alias chain; no longer open. |
| [#74310](https://github.com/openclaw/openclaw/issues/74310) | Closed in local gitcrawl 2026-06-03 | Bug Report: `normalizeProviderId` breaks provider-namespaced models like `kimi-coding/k2p5`; no longer open. |
| [#74185](https://github.com/openclaw/openclaw/pull/74185) | Closed in local gitcrawl | fix(infra): wrap provider auth resolution in timeout for status --usage --json; no longer open. |
| [#74020](https://github.com/openclaw/openclaw/issues/74020) | Closed in local gitcrawl | Gateway startup: models.mode=replace should skip pricing fetches; no longer open. |
| [#73667](https://github.com/openclaw/openclaw/pull/73667) | Closed in local gitcrawl 2026-06-11 | Bound active-memory recall latency and jitter QMD startup; no longer open. |
| [#73512](https://github.com/openclaw/openclaw/pull/73512) | Closed in local gitcrawl | fix(memory): schedule qmd embed when embedInterval is configured regardless of searchMode; no longer open. |
| [#73186](https://github.com/openclaw/openclaw/issues/73186) | Closed in local gitcrawl | [Bug]: Thinking/reasoning content leaks into cron announce delivery for Matrix/Feishu; no longer open. |
| [#73144](https://github.com/openclaw/openclaw/issues/73144) | Closed in local gitcrawl | Model switch experience: 5 issues when switching from qwen3.6-plus to deepseek-v4-pro; no longer open. |
| [#72927](https://github.com/openclaw/openclaw/issues/72927) | Closed in local gitcrawl 2026-06-01 | feat(tts): support MiMo v2.5 TTS VoiceDesign; no longer open. |
| [#72537](https://github.com/openclaw/openclaw/pull/72537) | Closed in local gitcrawl | fix(tts): honor provider timeoutMs in chat synthesis; no longer open. |
| [#71784](https://github.com/openclaw/openclaw/issues/71784) | Closed in local gitcrawl 2026-06-01 | Bug: memory search live embedding fails ~20–40% with `fetch failed \| other side closed` (provider-agnostic; upstream healthy); no longer open. |
| [#71678](https://github.com/openclaw/openclaw/pull/71678) | Closed in local gitcrawl | Fix: Issue 71522 memory embeddings; no longer open. |
| [#71491](https://github.com/openclaw/openclaw/issues/71491) | Closed in local gitcrawl 2026-06-15 | Kimi K2.6 reasoning_content 400 regression in long conversations after LCM compaction (follow-up #70392); no longer open. |
| [#71273](https://github.com/openclaw/openclaw/issues/71273) | Closed in local gitcrawl | Bug: Kimi Code model enters infinite tool call loop; no longer open. |
| [#70739](https://github.com/openclaw/openclaw/pull/70739) | Closed in local gitcrawl 2026-06-15 | fix(gateway): add SSE heartbeat to keep /v1/responses and /v1/chat/completions streams alive through idle-timeout proxies; no longer open. |
| [#70647](https://github.com/openclaw/openclaw/pull/70647) | Closed in local gitcrawl 2026-06-11 | test(agents): pin empty-turn coverage for non-strict-agentic nemotron; no longer open. |
| [#70596](https://github.com/openclaw/openclaw/pull/70596) | Closed in local gitcrawl | perf(memory): prewarm explicit local embeddings on gateway startup; no longer open. |
| [#70559](https://github.com/openclaw/openclaw/issues/70559) | Closed in local gitcrawl 2026-06-11 | runUnsafeReindex crashes with "no such table: chunks_vec" when sqlite-vec is enabled; no longer open. |
| [#69729](https://github.com/openclaw/openclaw/pull/69729) | Closed in local gitcrawl | fix(qwen): enable qwen3.6-plus on Coding Plan CN, correct reasoning flag; no longer open. |
| [#69495](https://github.com/openclaw/openclaw/pull/69495) | Closed in local gitcrawl | feat(heartbeat): support model fallbacks via {primary,fallbacks} (#69434); no longer open. |
| [#69245](https://github.com/openclaw/openclaw/pull/69245) | Closed in local gitcrawl | feat: enable cache-ttl context pruning for openai-completions providers; no longer open. |
| [#68996](https://github.com/openclaw/openclaw/pull/68996) | Closed in local gitcrawl | fix(google): route Gemma models through native Generative AI API; no longer open. |
| [#68975](https://github.com/openclaw/openclaw/pull/68975) | Closed in local gitcrawl 2026-06-15 | feat(memory): switch default local embedding model to bge-m3 Q8_0 🤖 AI-assisted; no longer open. |
| [#68812](https://github.com/openclaw/openclaw/issues/68812) | Closed in local gitcrawl 2026-06-01 | Make memory embedding retry/concurrency parameters configurable; no longer open. |
| [#68725](https://github.com/openclaw/openclaw/pull/68725) | Closed in local gitcrawl | feat(amazon-bedrock-mantle): add known context windows for open-weight Mantle models; no longer open. |
| [#68590](https://github.com/openclaw/openclaw/pull/68590) | Closed in local gitcrawl | fix(memory-core): rewrite qmd index on managed collection repair; no longer open. |
| [#68435](https://github.com/openclaw/openclaw/pull/68435) | Closed in local gitcrawl 2026-06-15 | feat(gateway): accept audio/file content blocks in /v1/chat/completions; no longer open. |
| [#68222](https://github.com/openclaw/openclaw/issues/68222) | Closed in local gitcrawl 2026-06-15 | [Bug]: Kimi Code model frequent sessions_yield tool call/output interrupts long-running tasks, requires manual intervention to resume; no longer open. |
| [#67593](https://github.com/openclaw/openclaw/issues/67593) | Closed in local gitcrawl 2026-06-15 | feat: add Kimi/Moonshot provider usage and balance display; no longer open. |
| [#67423](https://github.com/openclaw/openclaw/issues/67423) | Closed in local gitcrawl 2026-06-01 | [Bug] Auth router ignores provider entry's apiKey field, resolves via auth.order by canonical provider ID — wrong key for split provider entries; no longer open. |
| [#67379](https://github.com/openclaw/openclaw/issues/67379) | Closed in local gitcrawl 2026-06-15 | qmd scope denies subagent sessions — channel/chatType resolve to undefined; no longer open. |
| [#67035](https://github.com/openclaw/openclaw/issues/67035) | Closed in local gitcrawl 2026-06-04 | [Bug]: 2026.4.14 Windows chat UI regression: input text swallowed, streamed replies often invisible until refresh, typing indicator flashes then blanks; no longer open. |
| [#67008](https://github.com/openclaw/openclaw/pull/67008) | Closed in local gitcrawl | feat(chutes): add zai-org/GLM-5.1-TEE to static model catalog; no longer open. |
| [#66339](https://github.com/openclaw/openclaw/issues/66339) | Closed in local gitcrawl 2026-06-01 | memory search can hit QMD SQLite lock contention during normal runtime; no longer open. |
| [#65914](https://github.com/openclaw/openclaw/pull/65914) | Closed in local gitcrawl 2026-06-01 | fix(memory): respect qmd status timeout and skip checkpoint exports; no longer open. |
| [#65557](https://github.com/openclaw/openclaw/issues/65557) | Closed in local gitcrawl 2026-06-07 | Provider & model selection per session/account with admin-controlled allowlists; no longer open. |
| [#65547](https://github.com/openclaw/openclaw/pull/65547) | Closed in local gitcrawl 2026-06-15 | test(memory-qmd): verify extraCollections pattern reaches qmd collection add CLI args; no longer open. |
| [#65502](https://github.com/openclaw/openclaw/issues/65502) | Closed in local gitcrawl 2026-05-31 | feat(agents): resilient model fallback with retry + context-aware safe mode; no longer open. |
| [#65423](https://github.com/openclaw/openclaw/pull/65423) | Closed in local gitcrawl | feat(agents): shuffle auth profile candidates for subagent runs; no longer open. |
| [#65180](https://github.com/openclaw/openclaw/pull/65180) | Closed in local gitcrawl | fix(cli,sessions): make local model run stateless by default and keep transcript fallback profile-scoped; no longer open. |
| [#64335](https://github.com/openclaw/openclaw/pull/64335) | Closed in local gitcrawl | fix(zai): rotate env-backed API keys on rate limit; no longer open. |
| [#64224](https://github.com/openclaw/openclaw/issues/64224) | Closed in local gitcrawl 2026-06-15 | Billing cooldown flags entire provider instead of individual model — breaks proxy/litellm setups; no longer open. |
| [#64212](https://github.com/openclaw/openclaw/issues/64212) | Closed in local gitcrawl 2026-06-15 | [Bug]: Image tool fails with "Request was aborted" for NVIDIA Kimi K2.5; no longer open. |
| [#63685](https://github.com/openclaw/openclaw/issues/63685) | Closed in local gitcrawl 2026-06-03 | [Bug]: Cannot run gemma 4 models from google ai studio; no longer open. |
| [#62924](https://github.com/openclaw/openclaw/issues/62924) | Closed in local gitcrawl 2026-06-15 | Expose actual media-understanding chosen model in inbound body to avoid guessed media model reporting; no longer open. |
| [#62780](https://github.com/openclaw/openclaw/issues/62780) | Closed in local gitcrawl 2026-06-15 | Feature: message:before_send hook to enable content-quality fallback gating; no longer open. |
| [#62733](https://github.com/openclaw/openclaw/pull/62733) | Closed in local gitcrawl | Fix local memory embedding VRAM fallback and logging file resolution; no longer open. |
| [#62710](https://github.com/openclaw/openclaw/pull/62710) | Closed in local gitcrawl | fix(auth): stop new sessions inheriting auto-selected auth profile overrides; no longer open. |
| [#62436](https://github.com/openclaw/openclaw/issues/62436) | Closed in local gitcrawl 2026-06-12 | Feature: Lightweight LLM passthrough mode for /v1/chat/completions — skip session persistence entirely; no longer open. |
| [#62432](https://github.com/openclaw/openclaw/issues/62432) | Closed in local gitcrawl 2026-06-15 | [Bug]: Xiaomi/MiMo sessions can repeatedly relaunch exec after 'Command still running' instead of switching to process poll; no longer open. |
| [#62121](https://github.com/openclaw/openclaw/issues/62121) | Closed in local gitcrawl 2026-06-15 | DeepSeek preamble text leaks to Telegram after 3.13 → 4.5 upgrade (untagged assistant text bypasses commentary filter); no longer open. |
| [#62109](https://github.com/openclaw/openclaw/issues/62109) | Closed in local gitcrawl 2026-06-15 | Interactive runs fail with auth-style 403 when custom OpenAI-compatible provider baseUrl uses Unicode/IDN or punycode hostname, but ASCII hostname/IP works; no longer open. |
| [#61834](https://github.com/openclaw/openclaw/issues/61834) | Closed in local gitcrawl 2026-06-06 | [Feature]: expose QMD no-rerank for memory.qmd query mode; no longer open. |
| [#61187](https://github.com/openclaw/openclaw/pull/61187) | Closed in local gitcrawl 2026-06-15 | fix(kimi, moonshot): model picker shows wrong models; no longer open. |
| [#60546](https://github.com/openclaw/openclaw/issues/60546) | Closed in local gitcrawl 2026-06-11 | [Bug]: microsoft-foundry provider selects Claude deployments but routes them through OpenAI Foundry endpoints; no longer open. |
| [#60344](https://github.com/openclaw/openclaw/issues/60344) | Closed in local gitcrawl 2026-06-15 | [Bug]: Recursive output of system marker [image data removed - already processed by model] in kimi-coding/k2p; no longer open. |
| [#60078](https://github.com/openclaw/openclaw/issues/60078) | Closed in local gitcrawl 2026-06-03 | [Bug]: Announce delivery ignores modelByChannel, always uses agent default model; no longer open. |
| [#59208](https://github.com/openclaw/openclaw/pull/59208) | Closed in local gitcrawl 2026-06-02 | fix(status): honor selected usage auth profile; no longer open. |
| [#58765](https://github.com/openclaw/openclaw/issues/58765) | Closed in local gitcrawl | Feature: Support output dimensionality truncation for local GGUF embedding models; no longer open. |
| [#58434](https://github.com/openclaw/openclaw/pull/58434) | Closed in local gitcrawl | feat(openresponses): add per-request tool_deny override to /v1/responses; no longer open. |
| [#58405](https://github.com/openclaw/openclaw/pull/58405) | Closed in local gitcrawl 2026-06-12 | feat(openresponses): add per-request skills override to /v1/responses; no longer open. |
| [#58012](https://github.com/openclaw/openclaw/issues/58012) | Closed in local gitcrawl 2026-05-29 | strict9 tool-call-id regression for Mistral via proxy providers; no longer open. |
| [#57638](https://github.com/openclaw/openclaw/issues/57638) | Closed in local gitcrawl 2026-06-15 | feat: cron.defaults for model, delivery, and contextTokens; no longer open. |
| [#56674](https://github.com/openclaw/openclaw/pull/56674) | Closed in local gitcrawl | feat(openresponses): return reasoning/thinking content in /v1/responses output; no longer open. |
| [#55477](https://github.com/openclaw/openclaw/pull/55477) | Closed in local gitcrawl | feat: stamp session_key, message_channel, context_limit into LiteLLM request metadata; no longer open. |
| [#54155](https://github.com/openclaw/openclaw/issues/54155) | Closed in local gitcrawl | Gateway memory leak: 389MB → 14.7GB over 4 days with session accumulation; no longer open. |
| [#52029](https://github.com/openclaw/openclaw/issues/52029) | Closed in local gitcrawl | Feature Request: heartbeat.tools option to disable tools during heartbeat; no longer open. |
| [#51593](https://github.com/openclaw/openclaw/issues/51593) | Closed in local gitcrawl 2026-06-15 | [Bug]: Moonshot/Kimi duplicate tool-call IDs in replay, exposed by WhatsApp group chats; no longer open. |
| [#50051](https://github.com/openclaw/openclaw/pull/50051) | Closed in local gitcrawl | feat(macos): ExecuTorch Parakeet-TDT STT for Talk Mode + model-plugin runtime; no longer open. |
| [#48680](https://github.com/openclaw/openclaw/issues/48680) | Closed in local gitcrawl 2026-05-31 | [Bug] Model fallback treats HTTP 403 business rejection as 'candidate_succeeded', skipping remaining fallback models; no longer open. |
| [#48300](https://github.com/openclaw/openclaw/issues/48300) | Closed in local gitcrawl 2026-06-11 | Bug: memory_search hybrid mode not returning FTS matches; no longer open. |
| [#47884](https://github.com/openclaw/openclaw/issues/47884) | Closed in local gitcrawl 2026-06-01 | [Bug]: memory_search tool fails with "fetch failed" despite embedding provider configured; no longer open. |
| [#44870](https://github.com/openclaw/openclaw/issues/44870) | Closed in local gitcrawl 2026-06-03 | [Bug]: I have been unable to verify using the codex from the transfer station; no longer open. |
| [#33962](https://github.com/openclaw/openclaw/issues/33962) | Closed in local gitcrawl | [Feature]: slug-generator: use lightweight model instead of agent primary to prevent lane congestion; no longer open. |
| [#33329](https://github.com/openclaw/openclaw/issues/33329) | Closed in local gitcrawl 2026-06-15 | Document and add config toggles for all implicit discovery mechanisms; no longer open. |
| [#32496](https://github.com/openclaw/openclaw/issues/32496) | Closed in local gitcrawl 2026-06-01 | [Feature]:  Support frequency_penalty and presence_penalty Parameters for OpenAI-Compatible Providers; no longer open. |
| [#17925](https://github.com/openclaw/openclaw/issues/17925) | Closed in local gitcrawl 2026-06-15 | [Feature]: Support native web_search passthrough for ZAI (GLM) and Google (Gemini) providers; no longer open. |

</details>

## REGENERATION NOTES

Do not regenerate this file by dumping keyword hits. The correct workflow is:

1. Verify Gitcrawl freshness and fetch live GitHub open issue/PR state.
2. Build a broad candidate pool from local/open-weight/provider terms.
3. Review every candidate for whether the actual problem or PR change is materially about local/open-weight/model-provider behavior.
4. Keep direct/material matches, drop incidental body mentions, and preserve closed/removed notable items in the collapsed details block above.
5. Recount rows and compare against the retained issue/PR number sets before committing.
6. Run `python3 scripts/sort_openclaw_onur_inventory.py`, then `python3 scripts/export_inventory_json.py` and `python3 scripts/validate_inventory_json.py`, before committing so the Markdown table and JSON mirror stay in sync. The sorter generates `NEW OPEN THREADS` from Gitcrawl creation dates, keeps the canonical `OPEN THREADS` table collapsed with `Thread`, `Activity`, `Area`, `Creator`, and `Title` columns, fills creator handles from Gitcrawl, and sorts the canonical table by `Activity` score descending, then GitHub number descending/latest. Closed or removed rows stay newest-first by GitHub number.
7. Do not add cumulative source logs, audit-result prose, inclusion-criteria repeats, or generated highest-risk sections to this file. Keep operational notes in commit messages, PRs, or chat, not in the inventory.
- Kept open threads: 953 (491 issues, 462 PRs).
