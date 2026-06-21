# OPENCLAW ONUR INVENTORY

Updated: 2026-06-22

Review watermark:

- Last reviewed through issue: #95601.
- Last reviewed through PR: #95603.
- Meaning: all GitHub issues and PRs at or below these numbers were considered for local-model and open-weight relevance; later numbers need review on the next run.

## NEW OPEN THREADS (50)

| Thread | Created | Activity | Area | Creator | Title |
| --- | --- | --- | --- | --- | --- |
| 🔀&nbsp;[#95599](https://github.com/openclaw/openclaw/pull/95599) | 2026-06-21 | 0 | Local memory/embedding | @lsr911 | fix(memory): backfill provider.model in createWithAdapter when adapter returns empty string |
| 🔀&nbsp;[#95598](https://github.com/openclaw/openclaw/pull/95598) | 2026-06-21 | 0 | Local memory/embedding | @harjothkhara | fix(memory): skip placeholder short-term promotions |
| 🔀&nbsp;[#95596](https://github.com/openclaw/openclaw/pull/95596) | 2026-06-21 | 0 | Local/media model provider | @mcaxtr | fix: preserve steered audio for inbound TTS |
| 🔀&nbsp;[#95595](https://github.com/openclaw/openclaw/pull/95595) | 2026-06-21 | 0 | Local memory/embedding | @Lestat569769 | fix(memory-core): skip forced sync for healthy zero-hit search |
| 🔀&nbsp;[#95594](https://github.com/openclaw/openclaw/pull/95594) | 2026-06-21 | 0 | Model routing/config | @mmyzwl | fix(agent-runner): classify transient provider errors as fallback-worthy |
| 🔀&nbsp;[#95590](https://github.com/openclaw/openclaw/pull/95590) | 2026-06-21 | 0 | Local model runtime | @yu-xin-c | [codex] fix(reply): let preflight compaction use compaction timeout |
| 🔀&nbsp;[#95587](https://github.com/openclaw/openclaw/pull/95587) | 2026-06-21 | 0 | OpenAI-compatible/proxy | @fanyangCS | fix(openai-responses): recover streamed invalid_encrypted_content via drain-level retry (#95441) |
| 📝&nbsp;[#95586](https://github.com/openclaw/openclaw/issues/95586) | 2026-06-21 | 0 | Open-weight/provider behavior | @jwong-art | [Bug]: Kimi Coding auth fallback in systemd Gateway when config env is not injected |
| 🔀&nbsp;[#95584](https://github.com/openclaw/openclaw/pull/95584) | 2026-06-21 | 0 | OpenAI-compatible/proxy | @425072024 | fix(agents): null-guard baseUrl in getAttributionHeaders (fixes #92974) |
| 🔀&nbsp;[#95580](https://github.com/openclaw/openclaw/pull/95580) | 2026-06-21 | 0 | Local model runtime | @xydt-tanshanshan | fix(compaction): preflight compaction uses configured compaction timeout instead of reply operation abort signal |
| 🔀&nbsp;[#95579](https://github.com/openclaw/openclaw/pull/95579) | 2026-06-21 | 0 | Local model runtime | @ruomuxydt | fix(agents): allow model fallback on harness-owned prompt timeout |
| 🔀&nbsp;[#95576](https://github.com/openclaw/openclaw/pull/95576) | 2026-06-21 | 0 | Local model runtime | @lsr911 | fix(failover): allow model fallback on harness transport timeout |
| 📝&nbsp;[#95574](https://github.com/openclaw/openclaw/issues/95574) | 2026-06-21 | 0 | Local model runtime | @riazrahaman | [Bug]: Behavior bug (incorrect output/state without crash) |
| 🔀&nbsp;[#95564](https://github.com/openclaw/openclaw/pull/95564) | 2026-06-21 | 0 | OpenAI-compatible/proxy | @reatang | fix(openai): Codex OAuth token refresh bypasses proxy in restricted regions |
| 🔀&nbsp;[#95563](https://github.com/openclaw/openclaw/pull/95563) | 2026-06-21 | 0 | Local model runtime | @yu-xin-c | [codex] feat(mcp): share bundled runtime scope and fix preflight compaction abort |
| 📝&nbsp;[#95562](https://github.com/openclaw/openclaw/issues/95562) | 2026-06-21 | 0 | Open-weight/provider behavior | @tpanda09 | [Bug]: DeepSeek token cost spikes 15-37x after upgrading from 2026.5.27 → 2026.6.x |
| 🔀&nbsp;[#95561](https://github.com/openclaw/openclaw/pull/95561) | 2026-06-21 | 0 | Local model runtime | @maweibin | fix: preflight compaction uses reply abort signal (~60s) instead of configurable compaction timeout (#95553) |
| 📝&nbsp;[#95553](https://github.com/openclaw/openclaw/issues/95553) | 2026-06-21 | 0 | Local model runtime | @kiagentkronos-cell | Bug: preflight (budget-triggered) compaction hard-capped at ~60s, ignores compaction.timeoutSeconds |
| 📝&nbsp;[#95544](https://github.com/openclaw/openclaw/issues/95544) | 2026-06-21 | 0 | Local/media model provider | @oliver-arti | Feature: Voice Wake should optionally start a realtime Talk session instead of STT→chat→TTS |
| 🔀&nbsp;[#95543](https://github.com/openclaw/openclaw/pull/95543) | 2026-06-21 | 0 | Model routing/config | @mikasa0818 | fix #95474: [Bug]: missing_tool_result (local tool-execution failure) is classified unclassified and triggers cross-provider model fallback |
| 🔀&nbsp;[#95542](https://github.com/openclaw/openclaw/pull/95542) | 2026-06-21 | 0 | Model routing/config | @mikasa0818 | fix #95519: [Bug]: Fallback should trigger on provider upstream_error / LLM request failed |
| 🔀&nbsp;[#95537](https://github.com/openclaw/openclaw/pull/95537) | 2026-06-21 | 0 | Model routing/config | @bowenluo718 | fix(agents): expand embedded fallback classifier to accept transient provider errors |
| 📝&nbsp;[#95530](https://github.com/openclaw/openclaw/issues/95530) | 2026-06-21 | 0 | Model routing/config | @kumaxs | opencode-go streaming hangs in isolated cron sessions (model_call:stream_progress stalls) |
| 🔀&nbsp;[#95524](https://github.com/openclaw/openclaw/pull/95524) | 2026-06-21 | 0 | OpenAI-compatible/proxy | @liuhao1024 | fix(agents): classify upstream_error errorType as server_error for model fallback (fixes #95519) (AI-assisted) |
| 🔀&nbsp;[#95523](https://github.com/openclaw/openclaw/pull/95523) | 2026-06-21 | 0 | Model routing/config | @Bartok9 | fix(agents): classify provider upstream_error as fallbackable transient failure |
| 🔀&nbsp;[#95521](https://github.com/openclaw/openclaw/pull/95521) | 2026-06-21 | 0 | Model routing/config | @zhiqiang26 | fix(agents): classify 'upstream request failed' as server_error for failover |
| 🔀&nbsp;[#95520](https://github.com/openclaw/openclaw/pull/95520) | 2026-06-21 | 0 | Model routing/config | @zhangqueping | fix(agents): prevent Codex missing_tool_result from triggering cross-provider model fallback |
| 📝&nbsp;[#95519](https://github.com/openclaw/openclaw/issues/95519) | 2026-06-21 | 0 | Model routing/config | @zjx111234 | [Bug]: Fallback should trigger on provider upstream_error / LLM request failed |
| 🔀&nbsp;[#95513](https://github.com/openclaw/openclaw/pull/95513) | 2026-06-21 | 0 | Model routing/config | @jincheng-xydt | fix: treat claude-cli out-of-credits error as fallback-triggering failure (#95489) |
| 🔀&nbsp;[#95512](https://github.com/openclaw/openclaw/pull/95512) | 2026-06-21 | 0 | Model routing/config | @bowenluo718 | fix(agents): detect CLI generic failure text in fallback classifier (#95489) |
| 🔀&nbsp;[#95509](https://github.com/openclaw/openclaw/pull/95509) | 2026-06-21 | 0 | Local/media model provider | @CG-Intelligence-Agent-Cole | feat(ui): per-agent ElevenLabs Voice/TTS settings in control-ui |
| 🔀&nbsp;[#95508](https://github.com/openclaw/openclaw/pull/95508) | 2026-06-21 | 0 | Model routing/config | @mikasa0818 | fix #95489: [Bug]: claude-cli out-of-credits error bypasses model fallback chain — error text delivered as final response |
| 🔀&nbsp;[#95501](https://github.com/openclaw/openclaw/pull/95501) | 2026-06-21 | 0 | Model routing/config | @zhangqueping | fix(agents): classify CLI generic failure text as fallback-worthy |
| 📝&nbsp;[#95500](https://github.com/openclaw/openclaw/issues/95500) | 2026-06-21 | 0 | Model routing/config | @hpfan | [Bug]: Plugin model provider (opencode-go) cannot be resolved by isolated cron sessions, even though openclaw models lists it correctly and session_status model=default resolves it for existing sessions. |
| 🔀&nbsp;[#95496](https://github.com/openclaw/openclaw/pull/95496) | 2026-06-21 | 0 | Model routing/config | @liuhao1024 | fix(agents): classify generic external run failure text as fallback-eligible (fixes #95489) |
| 📝&nbsp;[#95495](https://github.com/openclaw/openclaw/issues/95495) | 2026-06-21 | 0 | Local memory/embedding | @fenglanhua | [Bug]: 2026.6.9 silently relocates memory store with no migration, forcing a full re-embed (1499 files) with zero upgrade-time warning |
| 🔀&nbsp;[#95494](https://github.com/openclaw/openclaw/pull/95494) | 2026-06-21 | 0 | Model routing/config | @Pandah97 | fix(agents): prevent missing_tool_result from triggering cross-provider model fallback (#95474) |
| 🔀&nbsp;[#95493](https://github.com/openclaw/openclaw/pull/95493) | 2026-06-21 | 0 | OpenAI-compatible/proxy | @openperf | fix(github-copilot): strip encrypted_content from reasoning replay items |
| 🔀&nbsp;[#95491](https://github.com/openclaw/openclaw/pull/95491) | 2026-06-21 | 0 | Model routing/config | @zhangqueping | fix(ui): reconcile model dropdown cache with server-resolved model after sessions.patch |
| 📝&nbsp;[#95489](https://github.com/openclaw/openclaw/issues/95489) | 2026-06-21 | 0 | Model routing/config | @riazrahaman | [Bug]: claude-cli out-of-credits error bypasses model fallback chain — error text delivered as final response |
| 🔀&nbsp;[#95488](https://github.com/openclaw/openclaw/pull/95488) | 2026-06-21 | 0 | Model routing/config | @zhiqiang26 | fix(agents): classify missing_tool_result as tool_error to prevent cross-provider failover |
| 🔀&nbsp;[#95487](https://github.com/openclaw/openclaw/pull/95487) | 2026-06-21 | 0 | Local/media model provider | @liuhao1024 | feat(tts): strip emoji characters before speech synthesis (fixes #95478) |
| 🔀&nbsp;[#95486](https://github.com/openclaw/openclaw/pull/95486) | 2026-06-21 | 0 | Local/media model provider | @Pandah97 | feat(speech-core): filter emoji before TTS synthesis |
| 📝&nbsp;[#95478](https://github.com/openclaw/openclaw/issues/95478) | 2026-06-21 | 0 | Local/media model provider | @lewiswu1209 | [Feature]: 希望在文本转语音前将表情符号过滤掉 |
| 📝&nbsp;[#95474](https://github.com/openclaw/openclaw/issues/95474) | 2026-06-21 | 0 | Model routing/config | @ElliotDrel | [Bug]: missing_tool_result (local tool-execution failure) is classified unclassified and triggers cross-provider model fallback |
| 🔀&nbsp;[#95458](https://github.com/openclaw/openclaw/pull/95458) | 2026-06-21 | 0 | Local model runtime | @Linux2010 | fix(cron): trim whitespace from object keys to handle malformed model outputs |
| 🔀&nbsp;[#95455](https://github.com/openclaw/openclaw/pull/95455) | 2026-06-21 | 0 | Model routing/config | @LiuwqGit | fix(agents): forward resolved sub-agent model to gateway call (#91171) |
| 🔀&nbsp;[#95453](https://github.com/openclaw/openclaw/pull/95453) | 2026-06-21 | 0 | Local model runtime | @mikasa0818 | fix #95407: [Bug]: `cron` tool `add` action mangles certain key names in `job` parameter |
| 🔀&nbsp;[#95452](https://github.com/openclaw/openclaw/pull/95452) | 2026-06-21 | 0 | Local memory/embedding | @liuhao1024 | fix(memory): align session file counter denominator with indexer filter (fixes #77338) |
| 🔀&nbsp;[#95447](https://github.com/openclaw/openclaw/pull/95447) | 2026-06-21 | 0 | Model routing/config | @moguangyu5-design | fix(agents): use CJK-aware token estimation for tool results |

## OPEN THREADS (1221)

| Thread | Activity | Area | Creator | Title |
| --- | --- | --- | --- | --- |
| 📝&nbsp;[#72015](https://github.com/openclaw/openclaw/issues/72015) | 29 | Local memory/embedding | @0xCNAI | Reliability: active-memory blocks replies and QMD boot initialization can overload multi-agent gateways |
| 🔀&nbsp;[#84581](https://github.com/openclaw/openclaw/pull/84581) | 17 | OpenAI-compatible/proxy | @pcdqc | fix(agents): strip plaintext model provider keys |
| 📝&nbsp;[#74586](https://github.com/openclaw/openclaw/issues/74586) | 17 | Local memory/embedding | @islandpreneur007 | AM embedded run aborts memory_search tool calls; classifies as timeout despite model completion |
| 📝&nbsp;[#62328](https://github.com/openclaw/openclaw/issues/62328) | 17 | Local memory/embedding | @TimeAground | node:sqlite missing FTS5 module - memory search keyword fallback broken |
| 🔀&nbsp;[#56674](https://github.com/openclaw/openclaw/pull/56674) | 17 | OpenAI-compatible/proxy | @tonga54 | feat(openresponses): return reasoning/thinking content in /v1/responses output |
| 📝&nbsp;[#33962](https://github.com/openclaw/openclaw/issues/33962) | 15 | Local model runtime | @zhangsensen | [Feature]: slug-generator: use lightweight model instead of agent primary to prevent lane congestion |
| 📝&nbsp;[#74986](https://github.com/openclaw/openclaw/issues/74986) | 14 | Local model runtime | @mlaihk | [Bug]: openclaw infer hangs indefinitely on 2026.4.27 - openclaw-infer child spins at 100% CPU with zero network I/O |
| 📝&nbsp;[#68920](https://github.com/openclaw/openclaw/issues/68920) | 14 | Local memory/embedding | @mehdic | HTTP /v1/chat/completions: 10-15s TTFB due to full agent context assembly - needs lightContext/voice mode |
| 📝&nbsp;[#85192](https://github.com/openclaw/openclaw/issues/85192) | 13 | OpenAI-compatible/proxy | @yxyujian98-png | DeepSeek V4: isSignedThinkingBlock misses unsigned thinking blocks - reasoning-only retry fails |
| 📝&nbsp;[#84569](https://github.com/openclaw/openclaw/issues/84569) | 13 | Local model runtime | @kiagentkronos-cell | WhatsApp session stalls on long model_call: incomplete turn with payloads=0, reply never delivered |
| 🔀&nbsp;[#81834](https://github.com/openclaw/openclaw/pull/81834) | 13 | Local/media model provider | @KLilyZ | feat(senseaudio): add SenseAudio TTS provider |
| 📝&nbsp;[#79847](https://github.com/openclaw/openclaw/issues/79847) | 13 | Local memory/embedding | @ChrisBot2026 | qmd-manager leaks XDG_CONFIG_HOME / XDG_CACHE_HOME to all child spawns, breaking mcporter >= 0.10 integration |
| 🔀&nbsp;[#87247](https://github.com/openclaw/openclaw/pull/87247) | 12 | Local memory/embedding | @airbing11 | docs: note LanceDB dreaming v0.2.3 via memory-lancedb-dreaming plugin |
| 🔀&nbsp;[#77158](https://github.com/openclaw/openclaw/pull/77158) | 12 | Local memory/embedding | @zeroaltitude | perf(qmd): persistent export-state cache + stat fast path in exportSessions |
| 📝&nbsp;[#54155](https://github.com/openclaw/openclaw/issues/54155) | 12 | Local memory/embedding | @the-lobsternaut | Gateway memory leak: 389MB -> 14.7GB over 4 days with session accumulation |
| 📝&nbsp;[#51441](https://github.com/openclaw/openclaw/issues/51441) | 12 | OpenAI-compatible/proxy | @Kyzcreig | feat: expose resolved backend model in session_status and agent runtime |
| 🔀&nbsp;[#50051](https://github.com/openclaw/openclaw/pull/50051) | 12 | Local/media model provider | @seyeong-han | feat(macos): ExecuTorch Parakeet-TDT STT for Talk Mode + model-plugin runtime |
| 📝&nbsp;[#45049](https://github.com/openclaw/openclaw/issues/45049) | 12 | OpenAI-compatible/proxy | @ArnoldJr | Agent loop allows simulated tool calls instead of enforcing real tool invocation |
| 🔀&nbsp;[#81443](https://github.com/openclaw/openclaw/pull/81443) | 11 | Local memory/embedding | @knightplat-blip | fix: resolve QMD Windows shims and guard image URL downloads |
| 🔀&nbsp;[#77339](https://github.com/openclaw/openclaw/pull/77339) | 11 | Model routing/config | @mjamiv | fix(auto-reply): clear runtime model cache on reset |
| 🔀&nbsp;[#68079](https://github.com/openclaw/openclaw/pull/68079) | 11 | OpenAI-compatible/proxy | @Frrrrrrrrank | feat(providers/zai): inject X-Session-Id header for prompt cache stickiness |
| 📝&nbsp;[#85126](https://github.com/openclaw/openclaw/issues/85126) | 10 | Local model runtime | @mlaihk | Bug: Control UI (TUI/WebChat) sessions auto-select wrong authProfileOverride (deepseek instead of minimax) at creation |
| 🔀&nbsp;[#78747](https://github.com/openclaw/openclaw/pull/78747) | 10 | Model/provider behavior | @ashvinnagarajan | fix(cache): emit `tools` before `input` in OpenAI Responses request body for prefix-cache stability |
| 📝&nbsp;[#54463](https://github.com/openclaw/openclaw/issues/54463) | 10 | Local memory/embedding | @bwjoke | QMD memory indexing can recurse into symlink loops in workspace-visible temp monorepos and fail with ENAMETOOLONG<br>Assignee: vincentkoc |
| 🔀&nbsp;[#87404](https://github.com/openclaw/openclaw/pull/87404) | 9 | Model routing/config | @deepujain | fix(agents): honor ACP alias model.primary overrides (Fixes #87381) |
| 🔀&nbsp;[#86564](https://github.com/openclaw/openclaw/pull/86564) | 9 | Model/provider behavior | @wesleysimplicio | fix(gateway): disable provider auth prewarm by default |
| 📝&nbsp;[#86090](https://github.com/openclaw/openclaw/issues/86090) | 9 | Local model runtime | @dustytext-bot | runHeartbeatOnce returns {status: "ran"} in 78ms on idle agent — phantom run, no model turn executed |
| 📝&nbsp;[#85773](https://github.com/openclaw/openclaw/issues/85773) | 9 | Local model runtime | @philippulus | [Bug]: After reinstalling (v2026.5.20), agents only provide generic replies, completely ignoring workspace files content and skills |
| 🔀&nbsp;[#84977](https://github.com/openclaw/openclaw/pull/84977) | 9 | Local model runtime | @ouchuan | feat: handle gemma 4 format tool call |
| 📝&nbsp;[#73432](https://github.com/openclaw/openclaw/issues/73432) | 9 | Local memory/embedding | @danielngn | [Bug]: qmd embedding is never triggered per memory.qmd.update.interval/embedInterval |
| 🔀&nbsp;[#71062](https://github.com/openclaw/openclaw/pull/71062) | 9 | OpenAI-compatible/proxy | @PopFlamingo | fix(/v1/responses): drop the extra phantom assistant turn on client-tool calls |
| 🔀&nbsp;[#70596](https://github.com/openclaw/openclaw/pull/70596) | 9 | Local memory/embedding | @taosiyuan163 | perf(memory): prewarm explicit local embeddings on gateway startup |
| 🔀&nbsp;[#68725](https://github.com/openclaw/openclaw/pull/68725) | 9 | OpenAI-compatible/proxy | @wirjo | feat(amazon-bedrock-mantle): add known context windows for open-weight Mantle models |
| 📝&nbsp;[#37966](https://github.com/openclaw/openclaw/issues/37966) | 9 | OpenAI-compatible/proxy | @V0v1kkkAssistant | [Bug]: cacheRetention ignored for LiteLLM-proxied Anthropic models |
| 📝&nbsp;[#10480](https://github.com/openclaw/openclaw/issues/10480) | 9 | OpenAI-compatible/proxy | @sidharthachatterjee | Support Workers AI model selection during onboard |
| 🔀&nbsp;[#87393](https://github.com/openclaw/openclaw/pull/87393) | 8 | Local/media model provider | @kesslerio | fix(media): suppress local whisper progress transcripts |
| 🔀&nbsp;[#87300](https://github.com/openclaw/openclaw/pull/87300) | 8 | Model routing/config | @newbie-yu | feat: group model select with collapsible panel in Control UI |
| 🔀&nbsp;[#86554](https://github.com/openclaw/openclaw/pull/86554) | 8 | OpenAI-compatible/proxy | @liaoyl830 | fix(agents): add missing DeepSeek V4 proxy models to reasoning_content replay set |
| 📝&nbsp;[#76665](https://github.com/openclaw/openclaw/issues/76665) | 8 | Open-weight/provider behavior | @Nelsoncongbao | Session context silently lost between consecutive turns with z.ai provider (GLM gateway) |
| 🔀&nbsp;[#75270](https://github.com/openclaw/openclaw/pull/75270) | 8 | OpenAI-compatible/proxy | @Komzpa | fix(agent): prevent sticky model fallback |
| 📝&nbsp;[#74021](https://github.com/openclaw/openclaw/issues/74021) | 8 | OpenAI-compatible/proxy | @jmystaki-create | Support reasoning-field outputs and visible final-answer handling for native reasoning models |
| 🔀&nbsp;[#73512](https://github.com/openclaw/openclaw/pull/73512) | 8 | Local memory/embedding | @SymbolStar | fix(memory): schedule qmd embed when embedInterval is configured regardless of searchMode |
| 🔀&nbsp;[#67008](https://github.com/openclaw/openclaw/pull/67008) | 8 | Open-weight/provider behavior | @tardigrde | feat(chutes): add zai-org/GLM-5.1-TEE to static model catalog |
| 📝&nbsp;[#64438](https://github.com/openclaw/openclaw/issues/64438) | 8 | Local memory/embedding | @GravenSm | Feature Request: Remote Reranker Endpoint Support |
| 📝&nbsp;[#52029](https://github.com/openclaw/openclaw/issues/52029) | 8 | Local model runtime | @andyk-ms | Feature Request: heartbeat.tools option to disable tools during heartbeat |
| 📝&nbsp;[#45508](https://github.com/openclaw/openclaw/issues/45508) | 8 | OpenAI-compatible/proxy | @mcfex | [Feature]: Self-hosted STT/TTS provider support in webchat (Route webchat TTS through the gateway instead of browser Speech API) |
| 📝&nbsp;[#41372](https://github.com/openclaw/openclaw/issues/41372) | 8 | Model/provider behavior | @e740554 | Field Report: 25 findings from 4 weeks of self-hosted production use (config crashes, CLI docs, Discord, cron) |
| 📝&nbsp;[#15073](https://github.com/openclaw/openclaw/issues/15073) | 8 | Local model runtime | @lucca-alma | Feature Request: Per-agent context/workspace on model fallback |
| 🔀&nbsp;[#77053](https://github.com/openclaw/openclaw/pull/77053) | 7 | OpenAI-compatible/proxy | @firat-elbey | feat(lmstudio): opt-in idle TTL via native load API |
| 🔀&nbsp;[#76928](https://github.com/openclaw/openclaw/pull/76928) | 7 | Model routing/config | @dorukardahan | feat(plugins): let hooks prefer auth profiles |

<details>
<summary>Remaining 1171 open threads, sorted by activity</summary>

| Thread | Activity | Area | Creator | Title |
| --- | --- | --- | --- | --- |
| 📝&nbsp;[#30381](https://github.com/openclaw/openclaw/issues/30381) | 7 | OpenAI-compatible/proxy | @mr-slurpy-wildcard | chatCompletions: ignore request model when x-openclaw-agent-id header is present |
| 📝&nbsp;[#75959](https://github.com/openclaw/openclaw/issues/75959) | 6 | OpenAI-compatible/proxy | @hpfan | [Feature]: Support image analysis for Kimi Code Plan |
| 🔀&nbsp;[#75075](https://github.com/openclaw/openclaw/pull/75075) | 6 | OpenAI-compatible/proxy | @glow1128 | feat(gateway): surface built-in tool calls as function_call output items on /v1/responses |
| 📝&nbsp;[#63990](https://github.com/openclaw/openclaw/issues/63990) | 6 | Local memory/embedding | @DIZ-admin | Feature: Multi-index embedding memory with model-aware failover (no mixed vector spaces) |
| 🔀&nbsp;[#87694](https://github.com/openclaw/openclaw/pull/87694) | 5 | Model routing/config | @sweetcornna | fix(auth): tighten billing cooldown defaults to recover from multi-hour lockouts (#70903) |
| 🔀&nbsp;[#87617](https://github.com/openclaw/openclaw/pull/87617) | 5 | Local model runtime | @vincentkoc | fix(agents): broaden local model lean profile |
| 🔀&nbsp;[#87296](https://github.com/openclaw/openclaw/pull/87296) | 5 | Model routing/config | @newbie-yu | feat: group model select with collapsible panel in Control UI |
| 📝&nbsp;[#83402](https://github.com/openclaw/openclaw/issues/83402) | 5 | OpenAI-compatible/proxy | @Guardl1n | [Bug]: Providers/Xiaomi: MiMo mimo-v2.5-pro still rejects cron embedded agent tool schema with 400 after 2026.5.12 fix |
| 📝&nbsp;[#81961](https://github.com/openclaw/openclaw/issues/81961) | 5 | OpenAI-compatible/proxy | @alexandre-leng | [Feature]: Add a simple Dashboard UX to manage multiple model providers |
| 📝&nbsp;[#81525](https://github.com/openclaw/openclaw/issues/81525) | 5 | OpenAI-compatible/proxy | @holgergruenhagen | [Bug]: media-understanding silently routes images to user-declared vision models without validating declared capabilities |
| 🔀&nbsp;[#78085](https://github.com/openclaw/openclaw/pull/78085) | 5 | OpenAI-compatible/proxy | @Beandon13 | fix(agents): parse prompt_tokens/completion_tokens in CLI usage for llama.cpp compatibility (#77992) |
| 📝&nbsp;[#76884](https://github.com/openclaw/openclaw/issues/76884) | 5 | Local model runtime | @wingraver | [Bug]: OpenClaw on native Windows getting notably slower and slower with each new version??? |
| 📝&nbsp;[#75105](https://github.com/openclaw/openclaw/issues/75105) | 5 | Open-weight/provider behavior | @flofrie | [Feature]: Allow per-model setting for Deepseek `reasoning_content` fix |
| 📝&nbsp;[#74732](https://github.com/openclaw/openclaw/issues/74732) | 5 | Local memory/embedding | @mppyes-ai | docs+feat: Document oMLX (Apple Silicon MLX) as memorySearch embedding provider |
| 🔀&nbsp;[#74403](https://github.com/openclaw/openclaw/pull/74403) | 5 | Open-weight/provider behavior | @SymbolStar | fix(deepseek): strip reasoning_content when extra_body disables thinking |
| 🔀&nbsp;[#74185](https://github.com/openclaw/openclaw/pull/74185) | 5 | Model/provider behavior | @yelog | fix(infra): wrap provider auth resolution in timeout for status --usage --json |
| 🔀&nbsp;[#73594](https://github.com/openclaw/openclaw/pull/73594) | 5 | Open-weight/provider behavior | @simpx | feat(openrouter): inject cache_control for closed-source qwen models |
| 🔀&nbsp;[#71678](https://github.com/openclaw/openclaw/pull/71678) | 5 | Local memory/embedding | @sahilsatralkar | Fix: Issue 71522 memory embeddings |
| 📝&nbsp;[#66125](https://github.com/openclaw/openclaw/issues/66125) | 5 | OpenAI-compatible/proxy | @Cybertr0n313 | [Bug]: openai-completions fallback candidate is selected, but fallback does not complete successfully through an OpenAI-compatible proxy |
| 🔀&nbsp;[#87932](https://github.com/openclaw/openclaw/pull/87932) | 4 | Model routing/config | @tanshanshan | feat(compaction): support percentage strings for token thresholds |
| 📝&nbsp;[#87756](https://github.com/openclaw/openclaw/issues/87756) | 4 | Local model runtime | @rogerallen1 | [Bug]: Regression: prompt-launched Lobster workflow hangs on nested /tools/invoke, while curl-launched workflow works |
| 📝&nbsp;[#87752](https://github.com/openclaw/openclaw/issues/87752) | 4 | Model routing/config | @jlin53882 | [Bug]: Failover selects unconfigured model MiniMax-M2.7-highspeed causing complete session failure |
| 🔀&nbsp;[#87572](https://github.com/openclaw/openclaw/pull/87572) | 4 | Local memory/embedding | @tanshanshan | fix(memory): increase QMD embedTimeoutMs default to 600s for local GGUF |
| 🔀&nbsp;[#87480](https://github.com/openclaw/openclaw/pull/87480) | 4 | Model routing/config | @bladin | fix(anthropic): configure undici Agent with extended keep-alive to prevent socket failures |
| 📝&nbsp;[#87407](https://github.com/openclaw/openclaw/issues/87407) | 4 | Model routing/config | @chrisgarcia-cpu | [Bug]: Anthropic provider: UND_ERR_SOCKET keep-alive failures trigger silent mid-turn fallback to OpenAI/Codex |
| 📝&nbsp;[#87325](https://github.com/openclaw/openclaw/issues/87325) | 4 | OpenAI-compatible/proxy | @BSG2000 | Support Azure Foundry GPT Realtime Talk via gateway relay |
| 📝&nbsp;[#87318](https://github.com/openclaw/openclaw/issues/87318) | 4 | Model routing/config | @Haderach-Ram | amazon-bedrock provider: Haiku 4.5 inference profile ARN not supported; params.modelId override ignored |
| 📝&nbsp;[#87285](https://github.com/openclaw/openclaw/issues/87285) | 4 | Local model runtime | @junxuku-byte | Gateway frequent restarts: config reload too aggressive + auth pre-warm blocks event loop |
| 📝&nbsp;[#87170](https://github.com/openclaw/openclaw/issues/87170) | 4 | Model routing/config | @phyosweet84-dev | Agent always returns "Provider returned error" with auto model after gateway restart |
| 📝&nbsp;[#87140](https://github.com/openclaw/openclaw/issues/87140) | 4 | Local/media model provider | @StephenCYL | [Feature]: Pluggable STT backend for macOS Push-to-Talk |
| 📝&nbsp;[#86868](https://github.com/openclaw/openclaw/issues/86868) | 4 | Model routing/config | @John1Tang | Embedded runtime: model fallback chain breaks at intermediate candidates instead of walking to the last entry |
| 📝&nbsp;[#86632](https://github.com/openclaw/openclaw/issues/86632) | 4 | Local model runtime | @ebelo | OpenClaw local embedded Ollama/Qwen session fails live-data request that Pi coding agent handles via shell/curl |
| 🔀&nbsp;[#86551](https://github.com/openclaw/openclaw/pull/86551) | 4 | OpenAI-compatible/proxy | @liaoyl830 | fix(agents): add missing DeepSeek V4 proxy models to reasoning_content replay set |
| 📝&nbsp;[#86034](https://github.com/openclaw/openclaw/issues/86034) | 4 | OpenAI-compatible/proxy | @tianxiaochannel-oss88 | Media generation succeeds but completion delivery fails and looks like generation failure |
| 📝&nbsp;[#85826](https://github.com/openclaw/openclaw/issues/85826) | 4 | Local model runtime | @kiagentkronos-cell | [Bug]: Agent stall detector hard-coded 120s threshold kills legitimate long model calls on local vLLM |
| 📝&nbsp;[#85382](https://github.com/openclaw/openclaw/issues/85382) | 4 | Local memory/embedding | @mmhzlrj | [Bug] post-compaction embedding sync fails with 500 when memorySearch.remote.baseUrl points to non-OpenAI host |
| 📝&nbsp;[#84575](https://github.com/openclaw/openclaw/issues/84575) | 4 | OpenAI-compatible/proxy | @juergenvh | [Bug] /v1/chat/completions: second request with same x-openclaw-session-key during in-flight turn runs in isolated session, loses memory scope |
| 📝&nbsp;[#84218](https://github.com/openclaw/openclaw/issues/84218) | 4 | Local model runtime | @reboost-openclaw-team[bot] | Heartbeat isolatedSession=true replays prior heartbeat context, causing deterministic overflow/restart loop |
| 📝&nbsp;[#83584](https://github.com/openclaw/openclaw/issues/83584) | 4 | OpenAI-compatible/proxy | @kwizzlek | [Bug]: Outbound MEDIA: directive on /v1/responses and /v1/chat/completions is passed through as raw text instead of translated to image_url / file content block |
| 🔀&nbsp;[#83227](https://github.com/openclaw/openclaw/pull/83227) | 4 | OpenAI-compatible/proxy | @HemantSudarshan | fix(openai): mark mp3 TTS voice output compatible |
| 📝&nbsp;[#81960](https://github.com/openclaw/openclaw/issues/81960) | 4 | Local model runtime | @alexandre-leng | [Feature]: Allow onboarding to configure multiple providers and models |
| 🔀&nbsp;[#80947](https://github.com/openclaw/openclaw/pull/80947) | 4 | Local memory/embedding | @anyech | fix(doctor): warn and document QMD session recall gates |
| 📝&nbsp;[#80722](https://github.com/openclaw/openclaw/issues/80722) | 4 | Local model runtime | @islandpreneur007 | config set "Restart the gateway to apply" warning is misleading for active agents without agentRuntime override |
| 📝&nbsp;[#80081](https://github.com/openclaw/openclaw/issues/80081) | 4 | OpenAI-compatible/proxy | @torbisoc | Need documented config keys for disabling plugin/tool/channel/owner-elevated surfaces for proposal-only mode |
| 📝&nbsp;[#79897](https://github.com/openclaw/openclaw/issues/79897) | 4 | OpenAI-compatible/proxy | @alexanderatkins | OpenAI-compatible streaming with llama.cpp saves zero usage (stream closed before final usage chunk) |
| 📝&nbsp;[#78897](https://github.com/openclaw/openclaw/issues/78897) | 4 | OpenAI-compatible/proxy | @Proita | OpenAI Responses provider should allow store=true for LiteLLM gpt-5.5 continuations |
| 📝&nbsp;[#77692](https://github.com/openclaw/openclaw/issues/77692) | 4 | OpenAI-compatible/proxy | @kidding1412 | fix(tts/xiaomi): Xiaomi Token Plan endpoint uses Bearer auth, not api-key header |
| 📝&nbsp;[#77675](https://github.com/openclaw/openclaw/issues/77675) | 4 | Local model runtime | @nickytonline | [Bug]: request.headers SecretRefs on model providers fail in embedded agent context with "unresolved SecretRef" error |
| 📝&nbsp;[#77142](https://github.com/openclaw/openclaw/issues/77142) | 4 | Local memory/embedding | @vuho60-byte | [Feature]: Parametric consolidation channel for dreaming pipeline (CLS Phase 4) |
| 🔀&nbsp;[#75860](https://github.com/openclaw/openclaw/pull/75860) | 4 | Local memory/embedding | @codexGW | fix(memory): improve QMD recall for channel queries |
| 🔀&nbsp;[#75350](https://github.com/openclaw/openclaw/pull/75350) | 4 | Open-weight/provider behavior | @t6am3 | fix(deepseek): strip reasoning_content from input messages when thinking is enabled |
| 📝&nbsp;[#75301](https://github.com/openclaw/openclaw/issues/75301) | 4 | Local model runtime | @mogglemoss | [Feature]: `openclaw caches` command to inspect and prune unbounded `~/.openclaw/` cache dirs (plugin-runtime-deps, browser, tools, orphan transcripts) |
| 📝&nbsp;[#75163](https://github.com/openclaw/openclaw/issues/75163) | 4 | OpenAI-compatible/proxy | @david-r-jones | Bug: TUI mid-session model switch passes raw alias instead of resolved model ID |
| 📝&nbsp;[#74910](https://github.com/openclaw/openclaw/issues/74910) | 4 | Local memory/embedding | @andhai | doctor: agents.defaults.llm.idleTimeoutSeconds auto-fix discards the user value; runtime gives no signal until doctor runs |
| 📝&nbsp;[#73801](https://github.com/openclaw/openclaw/issues/73801) | 4 | OpenAI-compatible/proxy | @iannwu | Active Memory with Cerebras gpt-oss-120b times out and can pin gateway CPU |
| 🔀&nbsp;[#72537](https://github.com/openclaw/openclaw/pull/72537) | 4 | Local memory/embedding | @masonjamie | fix(tts): honor provider timeoutMs in chat synthesis |
| 📝&nbsp;[#69943](https://github.com/openclaw/openclaw/issues/69943) | 4 | Local memory/embedding | @reidperyam | [Bug]: session-memory hook persists raw chat-template tokens and unparsed tool calls - re-injected context creates self-reinforcing poisoning loop, agents emit role tokens / NO_REPLY across all subsequent /new sessions |
| 🔀&nbsp;[#68996](https://github.com/openclaw/openclaw/pull/68996) | 4 | OpenAI-compatible/proxy | @tanjinlimkelvin-dot | fix(google): route Gemma models through native Generative AI API |
| 📝&nbsp;[#63229](https://github.com/openclaw/openclaw/issues/63229) | 4 | Local model runtime | @clawdia-lobster | Bug: Gateway falsely marks healthy local vLLM endpoints as timed out/overloaded, causing 1-23 min fallback cascades |
| 📝&nbsp;[#62599](https://github.com/openclaw/openclaw/issues/62599) | 4 | Local model runtime | @shawnpetros | [Bug]: openclaw status loads memory plugins locally and can report false vector state |
| 🔀&nbsp;[#58434](https://github.com/openclaw/openclaw/pull/58434) | 4 | OpenAI-compatible/proxy | @tonga54 | feat(openresponses): add per-request tool_deny override to /v1/responses |
| 📝&nbsp;[#57996](https://github.com/openclaw/openclaw/issues/57996) | 4 | Local memory/embedding | @Orionation | QMD per-agent SQLite caches cause extreme disk I/O on multi-agent deployments<br>Assignee: vincentkoc |
| 📝&nbsp;[#53550](https://github.com/openclaw/openclaw/issues/53550) | 4 | Local memory/embedding | @shivasymbl | experimental.sessionMemory does not surface gateway-dispatched sessions in memory_search |
| 📝&nbsp;[#49205](https://github.com/openclaw/openclaw/issues/49205) | 4 | OpenAI-compatible/proxy | @SHAREN | [Bug]: Control UI messages can reach shared context but still not appear in Open WebUI visible chat history |
| 📝&nbsp;[#46661](https://github.com/openclaw/openclaw/issues/46661) | 4 | OpenAI-compatible/proxy | @sheldon123z | [Feature]: Support Custom ASR (Speech-to-Text) Server Configuration |
| 📝&nbsp;[#22021](https://github.com/openclaw/openclaw/issues/22021) | 4 | Local model runtime | @dekaru | [Feature]: Add X-Actual-Model header to expose runtime model in HTTP responses |
| 📝&nbsp;[#13962](https://github.com/openclaw/openclaw/issues/13962) | 4 | Local model runtime | @dantaik | Feature: Per-mention model routing + context window for group mentions |
| 🔀&nbsp;[#74761](https://github.com/openclaw/openclaw/pull/74761) | 2 | Local memory/embedding | @mppyes-ai | docs: Document oMLX (Apple Silicon MLX) as memorySearch embedding provider |
| 🔀&nbsp;[#73817](https://github.com/openclaw/openclaw/pull/73817) | 2 | OpenAI-compatible/proxy | @spi3 | fix(media): allow private openai compatible audio transcription endpoints |
| 📝&nbsp;[#59168](https://github.com/openclaw/openclaw/issues/59168) | 2 | Local model runtime | @Kaspre | feat(models): use provider/name as internal key to decouple from API model ID |
| 🔀&nbsp;[#86637](https://github.com/openclaw/openclaw/pull/86637) | 1 | Open-weight/provider behavior | @SebTardif | fix(agents): recover tool calls from DeepSeek DSML text markup |
| 📝&nbsp;[#77645](https://github.com/openclaw/openclaw/issues/77645) | 1 | Local memory/embedding | @aderius | memory status --deep reports QMD embeddings unavailable when searchMode=search intentionally disables vectors |
| 📝&nbsp;[#77090](https://github.com/openclaw/openclaw/issues/77090) | 1 | Local model runtime | @djpollock | Feature: Auto-revert to primary model after image analysis |
| 📝&nbsp;[#73144](https://github.com/openclaw/openclaw/issues/73144) | 1 | Open-weight/provider behavior | @shaolin-cloud | Model switch experience: 5 issues when switching from qwen3.6-plus to deepseek-v4-pro |
| 📝&nbsp;[#41135](https://github.com/openclaw/openclaw/issues/41135) | 1 | Local model runtime | @tardis-create | [Feature]: Add provider-profile routing policies for multi-account OAuth/API pools (starting with google-gemini-cli) |
| 🔀&nbsp;[#95599](https://github.com/openclaw/openclaw/pull/95599) | 0 | Local memory/embedding | @lsr911 | fix(memory): backfill provider.model in createWithAdapter when adapter returns empty string |
| 🔀&nbsp;[#95598](https://github.com/openclaw/openclaw/pull/95598) | 0 | Local memory/embedding | @harjothkhara | fix(memory): skip placeholder short-term promotions |
| 🔀&nbsp;[#95596](https://github.com/openclaw/openclaw/pull/95596) | 0 | Local/media model provider | @mcaxtr | fix: preserve steered audio for inbound TTS |
| 🔀&nbsp;[#95595](https://github.com/openclaw/openclaw/pull/95595) | 0 | Local memory/embedding | @Lestat569769 | fix(memory-core): skip forced sync for healthy zero-hit search |
| 🔀&nbsp;[#95594](https://github.com/openclaw/openclaw/pull/95594) | 0 | Model routing/config | @mmyzwl | fix(agent-runner): classify transient provider errors as fallback-worthy |
| 🔀&nbsp;[#95590](https://github.com/openclaw/openclaw/pull/95590) | 0 | Local model runtime | @yu-xin-c | [codex] fix(reply): let preflight compaction use compaction timeout |
| 🔀&nbsp;[#95587](https://github.com/openclaw/openclaw/pull/95587) | 0 | OpenAI-compatible/proxy | @fanyangCS | fix(openai-responses): recover streamed invalid_encrypted_content via drain-level retry (#95441) |
| 📝&nbsp;[#95586](https://github.com/openclaw/openclaw/issues/95586) | 0 | Open-weight/provider behavior | @jwong-art | [Bug]: Kimi Coding auth fallback in systemd Gateway when config env is not injected |
| 🔀&nbsp;[#95584](https://github.com/openclaw/openclaw/pull/95584) | 0 | OpenAI-compatible/proxy | @425072024 | fix(agents): null-guard baseUrl in getAttributionHeaders (fixes #92974) |
| 🔀&nbsp;[#95580](https://github.com/openclaw/openclaw/pull/95580) | 0 | Local model runtime | @xydt-tanshanshan | fix(compaction): preflight compaction uses configured compaction timeout instead of reply operation abort signal |
| 🔀&nbsp;[#95579](https://github.com/openclaw/openclaw/pull/95579) | 0 | Local model runtime | @ruomuxydt | fix(agents): allow model fallback on harness-owned prompt timeout |
| 🔀&nbsp;[#95576](https://github.com/openclaw/openclaw/pull/95576) | 0 | Local model runtime | @lsr911 | fix(failover): allow model fallback on harness transport timeout |
| 📝&nbsp;[#95574](https://github.com/openclaw/openclaw/issues/95574) | 0 | Local model runtime | @riazrahaman | [Bug]: Behavior bug (incorrect output/state without crash) |
| 🔀&nbsp;[#95564](https://github.com/openclaw/openclaw/pull/95564) | 0 | OpenAI-compatible/proxy | @reatang | fix(openai): Codex OAuth token refresh bypasses proxy in restricted regions |
| 🔀&nbsp;[#95563](https://github.com/openclaw/openclaw/pull/95563) | 0 | Local model runtime | @yu-xin-c | [codex] feat(mcp): share bundled runtime scope and fix preflight compaction abort |
| 📝&nbsp;[#95562](https://github.com/openclaw/openclaw/issues/95562) | 0 | Open-weight/provider behavior | @tpanda09 | [Bug]: DeepSeek token cost spikes 15-37x after upgrading from 2026.5.27 → 2026.6.x |
| 🔀&nbsp;[#95561](https://github.com/openclaw/openclaw/pull/95561) | 0 | Local model runtime | @maweibin | fix: preflight compaction uses reply abort signal (~60s) instead of configurable compaction timeout (#95553) |
| 📝&nbsp;[#95553](https://github.com/openclaw/openclaw/issues/95553) | 0 | Local model runtime | @kiagentkronos-cell | Bug: preflight (budget-triggered) compaction hard-capped at ~60s, ignores compaction.timeoutSeconds |
| 📝&nbsp;[#95544](https://github.com/openclaw/openclaw/issues/95544) | 0 | Local/media model provider | @oliver-arti | Feature: Voice Wake should optionally start a realtime Talk session instead of STT→chat→TTS |
| 🔀&nbsp;[#95543](https://github.com/openclaw/openclaw/pull/95543) | 0 | Model routing/config | @mikasa0818 | fix #95474: [Bug]: missing_tool_result (local tool-execution failure) is classified unclassified and triggers cross-provider model fallback |
| 🔀&nbsp;[#95542](https://github.com/openclaw/openclaw/pull/95542) | 0 | Model routing/config | @mikasa0818 | fix #95519: [Bug]: Fallback should trigger on provider upstream_error / LLM request failed |
| 🔀&nbsp;[#95537](https://github.com/openclaw/openclaw/pull/95537) | 0 | Model routing/config | @bowenluo718 | fix(agents): expand embedded fallback classifier to accept transient provider errors |
| 📝&nbsp;[#95530](https://github.com/openclaw/openclaw/issues/95530) | 0 | Model routing/config | @kumaxs | opencode-go streaming hangs in isolated cron sessions (model_call:stream_progress stalls) |
| 🔀&nbsp;[#95524](https://github.com/openclaw/openclaw/pull/95524) | 0 | OpenAI-compatible/proxy | @liuhao1024 | fix(agents): classify upstream_error errorType as server_error for model fallback (fixes #95519) (AI-assisted) |
| 🔀&nbsp;[#95523](https://github.com/openclaw/openclaw/pull/95523) | 0 | Model routing/config | @Bartok9 | fix(agents): classify provider upstream_error as fallbackable transient failure |
| 🔀&nbsp;[#95521](https://github.com/openclaw/openclaw/pull/95521) | 0 | Model routing/config | @zhiqiang26 | fix(agents): classify 'upstream request failed' as server_error for failover |
| 🔀&nbsp;[#95520](https://github.com/openclaw/openclaw/pull/95520) | 0 | Model routing/config | @zhangqueping | fix(agents): prevent Codex missing_tool_result from triggering cross-provider model fallback |
| 📝&nbsp;[#95519](https://github.com/openclaw/openclaw/issues/95519) | 0 | Model routing/config | @zjx111234 | [Bug]: Fallback should trigger on provider upstream_error / LLM request failed |
| 🔀&nbsp;[#95513](https://github.com/openclaw/openclaw/pull/95513) | 0 | Model routing/config | @jincheng-xydt | fix: treat claude-cli out-of-credits error as fallback-triggering failure (#95489) |
| 🔀&nbsp;[#95512](https://github.com/openclaw/openclaw/pull/95512) | 0 | Model routing/config | @bowenluo718 | fix(agents): detect CLI generic failure text in fallback classifier (#95489) |
| 🔀&nbsp;[#95509](https://github.com/openclaw/openclaw/pull/95509) | 0 | Local/media model provider | @CG-Intelligence-Agent-Cole | feat(ui): per-agent ElevenLabs Voice/TTS settings in control-ui |
| 🔀&nbsp;[#95508](https://github.com/openclaw/openclaw/pull/95508) | 0 | Model routing/config | @mikasa0818 | fix #95489: [Bug]: claude-cli out-of-credits error bypasses model fallback chain — error text delivered as final response |
| 🔀&nbsp;[#95501](https://github.com/openclaw/openclaw/pull/95501) | 0 | Model routing/config | @zhangqueping | fix(agents): classify CLI generic failure text as fallback-worthy |
| 📝&nbsp;[#95500](https://github.com/openclaw/openclaw/issues/95500) | 0 | Model routing/config | @hpfan | [Bug]: Plugin model provider (opencode-go) cannot be resolved by isolated cron sessions, even though openclaw models lists it correctly and session_status model=default resolves it for existing sessions. |
| 🔀&nbsp;[#95496](https://github.com/openclaw/openclaw/pull/95496) | 0 | Model routing/config | @liuhao1024 | fix(agents): classify generic external run failure text as fallback-eligible (fixes #95489) |
| 📝&nbsp;[#95495](https://github.com/openclaw/openclaw/issues/95495) | 0 | Local memory/embedding | @fenglanhua | [Bug]: 2026.6.9 silently relocates memory store with no migration, forcing a full re-embed (1499 files) with zero upgrade-time warning |
| 🔀&nbsp;[#95494](https://github.com/openclaw/openclaw/pull/95494) | 0 | Model routing/config | @Pandah97 | fix(agents): prevent missing_tool_result from triggering cross-provider model fallback (#95474) |
| 🔀&nbsp;[#95493](https://github.com/openclaw/openclaw/pull/95493) | 0 | OpenAI-compatible/proxy | @openperf | fix(github-copilot): strip encrypted_content from reasoning replay items |
| 🔀&nbsp;[#95491](https://github.com/openclaw/openclaw/pull/95491) | 0 | Model routing/config | @zhangqueping | fix(ui): reconcile model dropdown cache with server-resolved model after sessions.patch |
| 📝&nbsp;[#95489](https://github.com/openclaw/openclaw/issues/95489) | 0 | Model routing/config | @riazrahaman | [Bug]: claude-cli out-of-credits error bypasses model fallback chain — error text delivered as final response |
| 🔀&nbsp;[#95488](https://github.com/openclaw/openclaw/pull/95488) | 0 | Model routing/config | @zhiqiang26 | fix(agents): classify missing_tool_result as tool_error to prevent cross-provider failover |
| 🔀&nbsp;[#95487](https://github.com/openclaw/openclaw/pull/95487) | 0 | Local/media model provider | @liuhao1024 | feat(tts): strip emoji characters before speech synthesis (fixes #95478) |
| 🔀&nbsp;[#95486](https://github.com/openclaw/openclaw/pull/95486) | 0 | Local/media model provider | @Pandah97 | feat(speech-core): filter emoji before TTS synthesis |
| 📝&nbsp;[#95478](https://github.com/openclaw/openclaw/issues/95478) | 0 | Local/media model provider | @lewiswu1209 | [Feature]: 希望在文本转语音前将表情符号过滤掉 |
| 📝&nbsp;[#95474](https://github.com/openclaw/openclaw/issues/95474) | 0 | Model routing/config | @ElliotDrel | [Bug]: missing_tool_result (local tool-execution failure) is classified unclassified and triggers cross-provider model fallback |
| 🔀&nbsp;[#95458](https://github.com/openclaw/openclaw/pull/95458) | 0 | Local model runtime | @Linux2010 | fix(cron): trim whitespace from object keys to handle malformed model outputs |
| 🔀&nbsp;[#95455](https://github.com/openclaw/openclaw/pull/95455) | 0 | Model routing/config | @LiuwqGit | fix(agents): forward resolved sub-agent model to gateway call (#91171) |
| 🔀&nbsp;[#95453](https://github.com/openclaw/openclaw/pull/95453) | 0 | Local model runtime | @mikasa0818 | fix #95407: [Bug]: `cron` tool `add` action mangles certain key names in `job` parameter |
| 🔀&nbsp;[#95452](https://github.com/openclaw/openclaw/pull/95452) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): align session file counter denominator with indexer filter (fixes #77338) |
| 🔀&nbsp;[#95447](https://github.com/openclaw/openclaw/pull/95447) | 0 | Model routing/config | @moguangyu5-design | fix(agents): use CJK-aware token estimation for tool results |
| 🔀&nbsp;[#95442](https://github.com/openclaw/openclaw/pull/95442) | 0 | Local model runtime | @lzyyzznl | fix(cron): recover whitespace-padded job keys from local model parsers |
| 📝&nbsp;[#95441](https://github.com/openclaw/openclaw/issues/95441) | 0 | OpenAI-compatible/proxy | @fanyangCS | github-copilot/gpt-5.5 still persists/replays thinkingSignature encrypted_content after #84367/#90682/#92941, causing channel/direct LLM request failed |
| 🔀&nbsp;[#95436](https://github.com/openclaw/openclaw/pull/95436) | 0 | Model routing/config | @mikasa0818 | fix #91171: [Bug]: Sub-agent model routing ignores model parameter, silently falls back to deepseek |
| 🔀&nbsp;[#95434](https://github.com/openclaw/openclaw/pull/95434) | 0 | Model routing/config | @jincheng-xydt | fix: persist modelOverride/providerOverride in subagent spawn (#91171) |
| 🔀&nbsp;[#95427](https://github.com/openclaw/openclaw/pull/95427) | 0 | Local model runtime | @ZengWen-DT | fix(cron): recover whitespace-padded tool keys before validation |
| 🔀&nbsp;[#95424](https://github.com/openclaw/openclaw/pull/95424) | 0 | Local model runtime | @zhangqueping | fix(cron): trim whitespace-padded keys in job canonicalization |
| 🔀&nbsp;[#95421](https://github.com/openclaw/openclaw/pull/95421) | 0 | Local model runtime | @zenglingbiao | fix(cron): trim trailing whitespace from cron tool job keys in canonicalization (fixes #95407) |
| 🔀&nbsp;[#95420](https://github.com/openclaw/openclaw/pull/95420) | 0 | Model routing/config | @Alix-007 | fix(agents): bound OpenRouter model catalog response reads |
| 🔀&nbsp;[#95418](https://github.com/openclaw/openclaw/pull/95418) | 0 | Model routing/config | @Alix-007 | fix(agents): bound OpenRouter model-scan catalog success body |
| 🔀&nbsp;[#95416](https://github.com/openclaw/openclaw/pull/95416) | 0 | Local/media model provider | @Alix-007 | fix(inworld): bound TTS audio and error response body reads to prevent OOM |
| 🔀&nbsp;[#95414](https://github.com/openclaw/openclaw/pull/95414) | 0 | Local model runtime | @liuhao1024 | fix(llm): strip trailing spaces from JSON keys in tool-call parsing (fixes #95407) |
| 📝&nbsp;[#95408](https://github.com/openclaw/openclaw/issues/95408) | 0 | Model routing/config | @aegis-gh-agent[bot] | [Feature]: Per-agent model.requestTimeoutSeconds to handle complex cron payloads in fallback chain |
| 📝&nbsp;[#95407](https://github.com/openclaw/openclaw/issues/95407) | 0 | Local model runtime | @Nassiel | [Bug]: `cron` tool `add` action mangles certain key names in `job` parameter |
| 🔀&nbsp;[#95401](https://github.com/openclaw/openclaw/pull/95401) | 0 | Local model runtime | @MonkeyLeeT | fix(lmstudio): canonicalize variant model keys |
| 🔀&nbsp;[#95400](https://github.com/openclaw/openclaw/pull/95400) | 0 | Model routing/config | @jason-allen-oneal | fix(model-fallback): classify Codex usage-limit payloads |
| 📝&nbsp;[#95394](https://github.com/openclaw/openclaw/issues/95394) | 0 | Local model runtime | @spacenet-Pop-OS | [Bug]: LM Studio model identifier gets @q4_k_m/@q8_0 quant suffix appended on retry path — assistant turn falsely marked as error |
| 🔀&nbsp;[#95393](https://github.com/openclaw/openclaw/pull/95393) | 0 | Local memory/embedding | @mikasa0818 | fix #92582: Bug: doctor falsely warns local memory embeddings are not ready |
| 🔀&nbsp;[#95392](https://github.com/openclaw/openclaw/pull/95392) | 0 | Local memory/embedding | @1052326311 | fix(doctor): suppress local memory embedding warning when probe was skipped |
| 🔀&nbsp;[#95391](https://github.com/openclaw/openclaw/pull/95391) | 0 | Local memory/embedding | @liuhao1024 | fix(active-memory): filter assistant chitchat from recall summary (fixes #84034) |
| 🔀&nbsp;[#95386](https://github.com/openclaw/openclaw/pull/95386) | 0 | Model routing/config | @mikasa0818 | fix #95351: [Feature]: Generic JSONL line-parsing hook for CliBackendPlugin (native tool-card support beyond claude-stream-json) |
| 🔀&nbsp;[#95375](https://github.com/openclaw/openclaw/pull/95375) | 0 | OpenAI-compatible/proxy | @Thibaultjaigu | feat(requesty): add Requesty as a bundled provider plugin |
| 🔀&nbsp;[#95372](https://github.com/openclaw/openclaw/pull/95372) | 0 | Local/media model provider | @ly-wang19 | fix(cli): sync infer capability inspect metadata flags with registered options |
| 🔀&nbsp;[#95370](https://github.com/openclaw/openclaw/pull/95370) | 0 | Open-weight/provider behavior | @mikasa0818 | fix #94919: [Bug]: Z.AI Coding-Plan: ECONNRESET triggers model fallback — fallback notice is invisible to the user in async contexts (cron jobs, sub-agents, isolated runs) |
| 🔀&nbsp;[#95365](https://github.com/openclaw/openclaw/pull/95365) | 0 | Local memory/embedding | @NianJiuZst | fix: preserve user text that looks like inbound metadata |
| 🔀&nbsp;[#95358](https://github.com/openclaw/openclaw/pull/95358) | 0 | Open-weight/provider behavior | @krpr | fix(streaming): flush visible text immediately after reasoning close tag |
| 📝&nbsp;[#95351](https://github.com/openclaw/openclaw/issues/95351) | 0 | Model routing/config | @jrluis | [Feature]: Generic JSONL line-parsing hook for CliBackendPlugin (native tool-card support beyond claude-stream-json) |
| 🔀&nbsp;[#95347](https://github.com/openclaw/openclaw/pull/95347) | 0 | Local memory/embedding | @jason-allen-oneal | fix(memory): honor qmd search timeout for memory_search |
| 🔀&nbsp;[#95345](https://github.com/openclaw/openclaw/pull/95345) | 0 | Model/provider behavior | @zhangqueping | fix(telegram): deliver reasoning as durable block when /reasoning on |
| 🔀&nbsp;[#95342](https://github.com/openclaw/openclaw/pull/95342) | 0 | Model routing/config | @mpz4life | fix(agents): skip pre-prompt precheck when context engine owns compaction [AI] |
| 🔀&nbsp;[#95341](https://github.com/openclaw/openclaw/pull/95341) | 0 | Model routing/config | @ly85206559 | fix(ui): show cron job model selection |
| 🔀&nbsp;[#95333](https://github.com/openclaw/openclaw/pull/95333) | 0 | Local memory/embedding | @mikasa0818 | fix #95279: Provide a trusted inbound-decoration contract so consumers can strip/dedup without forgeable text heuristics |
| 🔀&nbsp;[#95327](https://github.com/openclaw/openclaw/pull/95327) | 0 | Model routing/config | @mpz4life | fix(agents): use context engine token estimate for precheck overflow detection [AI] |
| 📝&nbsp;[#95314](https://github.com/openclaw/openclaw/issues/95314) | 0 | Local model runtime | @krpr | Bug: reasoning→content transition text buffered until stream flush; leading newlines swallowed |
| 🔀&nbsp;[#95311](https://github.com/openclaw/openclaw/pull/95311) | 0 | Open-weight/provider behavior | @sunlit-deng | feat: add disableBoundaryAwareCache compat option for prefix-matching prompt cache providers |
| 🔀&nbsp;[#95305](https://github.com/openclaw/openclaw/pull/95305) | 0 | Model/provider behavior | @mikasa0818 | fix #95219: [Bug]: Historical tool results are re-truncated between turns, breaking prompt cache prefix stability |
| 🔀&nbsp;[#95303](https://github.com/openclaw/openclaw/pull/95303) | 0 | Model routing/config | @liaoyl830 | [codex] fix security audit request headers |
| 🔀&nbsp;[#95300](https://github.com/openclaw/openclaw/pull/95300) | 0 | Local/media model provider | @ly-wang19 | fix(cli): expose --count on infer image edit, matching image generate |
| 🔀&nbsp;[#95298](https://github.com/openclaw/openclaw/pull/95298) | 0 | OpenAI-compatible/proxy | @Marvinthebored | fix(agents): seal deepseek reasoning before the answer (no discrete thinking_end) |
| 🔀&nbsp;[#95296](https://github.com/openclaw/openclaw/pull/95296) | 0 | Model routing/config | @Pick-cat | fix(anthropic): send current claude-cli user-agent on OAuth path |
| 🔀&nbsp;[#95294](https://github.com/openclaw/openclaw/pull/95294) | 0 | Model routing/config | @liuhao1024 | feat(ui): add model selector to cron quick-create wizard (fixes #93507) |
| 🔀&nbsp;[#95289](https://github.com/openclaw/openclaw/pull/95289) | 0 | Model routing/config | @summerview1997 | fix: bound Codex Telegram turns fail after /codex bind on OAuth refresh |
| 🔀&nbsp;[#95287](https://github.com/openclaw/openclaw/pull/95287) | 0 | Model routing/config | @crh-code | fix(failover): detect provider transport timeout in AbortError with 'This operation was aborted' message |
| 🔀&nbsp;[#95286](https://github.com/openclaw/openclaw/pull/95286) | 0 | Model routing/config | @zhangqueping | fix(agents): forward resolved model to sub-agent gateway agent call |
| 🔀&nbsp;[#95285](https://github.com/openclaw/openclaw/pull/95285) | 0 | Local memory/embedding | @mmyzwl | fix(memory-wiki): resolve bridge zero-artifact report in CLI snapshot mode |
| 🔀&nbsp;[#95284](https://github.com/openclaw/openclaw/pull/95284) | 0 | OpenAI-compatible/proxy | @lzyyzznl | fix(openai-completions): close thinking block at reasoning→content transition for providers without discrete thinking_end |
| 🔀&nbsp;[#95283](https://github.com/openclaw/openclaw/pull/95283) | 0 | OpenAI-compatible/proxy | @ZengWen-DT | fix(openai-completions): seal native reasoning before the answer under /reasoning on |
| 🔀&nbsp;[#95281](https://github.com/openclaw/openclaw/pull/95281) | 0 | OpenAI-compatible/proxy | @liuhao1024 | fix(llm): close reasoning stream on text-lane transition for DeepSeek (fixes #95280) |
| 📝&nbsp;[#95280](https://github.com/openclaw/openclaw/issues/95280) | 0 | OpenAI-compatible/proxy | @Marvinthebored | deepseek reasoning: final answer merges into the thinking block under /reasoning on (no discrete thinking_end at the reasoning→content transition) |
| 📝&nbsp;[#95279](https://github.com/openclaw/openclaw/issues/95279) | 0 | Local memory/embedding | @gorkem2020 | Provide a trusted inbound-decoration contract so consumers can strip/dedup without forgeable text heuristics |
| 🔀&nbsp;[#95274](https://github.com/openclaw/openclaw/pull/95274) | 0 | Local memory/embedding | @ly85206559 | fix(memory): preserve Windows QMD command paths |
| 🔀&nbsp;[#95268](https://github.com/openclaw/openclaw/pull/95268) | 0 | Model routing/config | @Darren2030 | fix(openrouter): expand short canonical model IDs to upstream API slugs (fixes #95198) |
| 🔀&nbsp;[#95267](https://github.com/openclaw/openclaw/pull/95267) | 0 | Local memory/embedding | @zhangqueping | fix(memory): repair Windows QMD paths whose backslashes were stripped by JSON parsing |
| 🔀&nbsp;[#95258](https://github.com/openclaw/openclaw/pull/95258) | 0 | Model routing/config | @dwc1997 | fix(openrouter): prevent model prefix duplication for short canonical IDs |
| 🔀&nbsp;[#95252](https://github.com/openclaw/openclaw/pull/95252) | 0 | Local memory/embedding | @Pandah97 | fix(memory-host-sdk): preserve Windows backslash paths in QMD command resolution (#92302) |
| 🔀&nbsp;[#95247](https://github.com/openclaw/openclaw/pull/95247) | 0 | Model routing/config | @crh-code | fix(context-engine): read allowModelOverride from plugin config instead of hardcoding false |
| 🔀&nbsp;[#95246](https://github.com/openclaw/openclaw/pull/95246) | 0 | Model routing/config | @Alix-007 | fix(plugin-sdk): bound live model catalog success body |
| 🔀&nbsp;[#95244](https://github.com/openclaw/openclaw/pull/95244) | 0 | Local model runtime | @Alix-007 | fix(providers): bound self-hosted provider discovery JSON reads |
| 📝&nbsp;[#95224](https://github.com/openclaw/openclaw/issues/95224) | 0 | Model routing/config | @guifav | OpenAI Codex gpt-5.5 catalog reports 272k context while OpenClaw can run 1M via override |
| 🔀&nbsp;[#95223](https://github.com/openclaw/openclaw/pull/95223) | 0 | OpenAI-compatible/proxy | @Alix-007 | fix(openai): bound ChatGPT Responses error body reads to prevent OOM |
| 🔀&nbsp;[#95214](https://github.com/openclaw/openclaw/pull/95214) | 0 | Model routing/config | @mmyzwl | fix(openrouter): expand short DeepSeek V4 aliases in API model normalizer |
| 🔀&nbsp;[#95213](https://github.com/openclaw/openclaw/pull/95213) | 0 | Model routing/config | @lzyyzznl | fix(plugins): infer LLM override policy from config.summaryModel at runtime |
| 🔀&nbsp;[#95212](https://github.com/openclaw/openclaw/pull/95212) | 0 | Local memory/embedding | @Pandah97 | fix(memory): preserve Windows absolute paths in QMD command parsing (#92302) |
| 🔀&nbsp;[#95208](https://github.com/openclaw/openclaw/pull/95208) | 0 | Model routing/config | @maweibin | fix(openrouter): strip provider prefix from short model refs in API model ID normalization |
| 🔀&nbsp;[#95202](https://github.com/openclaw/openclaw/pull/95202) | 0 | Model routing/config | @Sanjays2402 | fix(openrouter): expand short DeepSeek V4 aliases to upstream slug in API normalizer (#95198) |
| 📝&nbsp;[#95198](https://github.com/openclaw/openclaw/issues/95198) | 0 | Model routing/config | @daniel-alejandro-t | Bug: OpenRouter model prefix duplicated when using short model IDs (openrouter/deepseek-v4-flash → openrouter/openrouter/deepseek-v4-flash) |
| 🔀&nbsp;[#95177](https://github.com/openclaw/openclaw/pull/95177) | 0 | Local memory/embedding | @ml12580 | fix(doctor): suppress false-positive local embedding warning when gateway probe skipped [AI-assisted] |
| 🔀&nbsp;[#95176](https://github.com/openclaw/openclaw/pull/95176) | 0 | Model routing/config | @jincheng-xydt | fix(anthropic): retry on UND_ERR_SOCKET keep-alive failures (#87407) |
| 🔀&nbsp;[#95167](https://github.com/openclaw/openclaw/pull/95167) | 0 | Model routing/config | @moguangyu5-design | fix(config): allow Nix-mode doctor --fix and auth login for non-config writes |
| 📝&nbsp;[#95165](https://github.com/openclaw/openclaw/issues/95165) | 0 | Model routing/config | @ArturoArktad | embedded_run watchdog kills sessions during slow Anthropic responses (no progress signal before first token) |
| 🔀&nbsp;[#95162](https://github.com/openclaw/openclaw/pull/95162) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): align session file counter denominator with indexer filter (fixes #77338) |
| 🔀&nbsp;[#95151](https://github.com/openclaw/openclaw/pull/95151) | 0 | Local model runtime | @bowenluo718 | fix(ollama): support remote Ollama hosts with extended timeouts |
| 🔀&nbsp;[#95149](https://github.com/openclaw/openclaw/pull/95149) | 0 | Local memory/embedding | @SunnyShu0925 | fix(memory-wiki): resolve bridge zero-artifact report in CLI snapshot mode |
| 🔀&nbsp;[#95140](https://github.com/openclaw/openclaw/pull/95140) | 0 | Model routing/config | @sunlit-deng | fix: auto-populate lossless-claw llm policy from summaryModel at config load |
| 🔀&nbsp;[#95139](https://github.com/openclaw/openclaw/pull/95139) | 0 | Local model runtime | @lzyyzznl | fix(ollama): show full thinking levels for live-discovered models in /think menu |
| 🔀&nbsp;[#95138](https://github.com/openclaw/openclaw/pull/95138) | 0 | Model routing/config | @LiLan0125 | fix(doctor): add OAuth re-auth hint to openai-codex provider migration |
| 📝&nbsp;[#95136](https://github.com/openclaw/openclaw/issues/95136) | 0 | Model routing/config | @cattyclaw-bot | No migration path or warning when a model provider id is removed/renamed (openai-codex -> openai): OAuth profiles silently orphaned |
| 📝&nbsp;[#95135](https://github.com/openclaw/openclaw/issues/95135) | 0 | Model routing/config | @cattyclaw-bot | Nix-mode write guard blocks auth-profile and session-state writes that never touch openclaw.json |
| 📝&nbsp;[#95131](https://github.com/openclaw/openclaw/issues/95131) | 0 | Model routing/config | @a-m-a-r-a | Official openai/* model selection auto-enables Codex plugin despite disabled/opt-out intent |
| 🔀&nbsp;[#95127](https://github.com/openclaw/openclaw/pull/95127) | 0 | Local memory/embedding | @Nas01010101 | perf(memory-lancedb): cache query embeddings per embeddings instance |
| 🔀&nbsp;[#95120](https://github.com/openclaw/openclaw/pull/95120) | 0 | Model routing/config | @xydigit-zt | feat(channels): add directUserId support for per-DM model override |
| 🔀&nbsp;[#95113](https://github.com/openclaw/openclaw/pull/95113) | 0 | Local memory/embedding | @849261680 | fix(memory): keep cleaning reindex sidecars after lock errors |
| 🔀&nbsp;[#95101](https://github.com/openclaw/openclaw/pull/95101) | 0 | Local memory/embedding | @Nas01010101 | perf(memory-lancedb): cache query embeddings per embeddings instance |
| 🔀&nbsp;[#95099](https://github.com/openclaw/openclaw/pull/95099) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): align session file counter denominator with indexer filter (fixes #77338) |
| 🔀&nbsp;[#95091](https://github.com/openclaw/openclaw/pull/95091) | 0 | Local memory/embedding | @lzyyzznl | fix(doctor): probe memory embeddings on --deep and skip false warning on local provider |
| 🔀&nbsp;[#95088](https://github.com/openclaw/openclaw/pull/95088) | 0 | Local memory/embedding | @aniruddhaadak80 | [AI-assisted] fix(memory): close cached agent and state databases in test teardowns |
| 🔀&nbsp;[#95087](https://github.com/openclaw/openclaw/pull/95087) | 0 | Local memory/embedding | @jalehman | refactor: add memory and QMD session identity mapping |
| 🔀&nbsp;[#95070](https://github.com/openclaw/openclaw/pull/95070) | 0 | Local memory/embedding | @Nas01010101 | perf(memory-core): store embedding cache as Float32 BLOB instead of JSON TEXT [AI] |
| 🔀&nbsp;[#95067](https://github.com/openclaw/openclaw/pull/95067) | 0 | Local memory/embedding | @zenglingbiao | fix(doctor): suppress false-positive local embedding warning when probe is skipped (fixes #92582) |
| 🔀&nbsp;[#95064](https://github.com/openclaw/openclaw/pull/95064) | 0 | Local memory/embedding | @liuhao1024 | fix(doctor): suppress false-positive local embedding warning when probe was skipped (fixes #92582) |
| 🔀&nbsp;[#95062](https://github.com/openclaw/openclaw/pull/95062) | 0 | Local model runtime | @lzyyzznl | fix(telegram): fall back to agent default model in /think menu when session model context is empty |
| 🔀&nbsp;[#95050](https://github.com/openclaw/openclaw/pull/95050) | 0 | Model routing/config | @MonkeyLeeT | fix(auto-reply): surface preserved fallback notices |
| 🔀&nbsp;[#95049](https://github.com/openclaw/openclaw/pull/95049) | 0 | Model routing/config | @jincheng-xydt | fix: respect hook config model override in session-memory slug generation (#89551) |
| 🔀&nbsp;[#95047](https://github.com/openclaw/openclaw/pull/95047) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): increase narrative timeout from 60s to 120s for ARM devices (fixes #92494) |
| 📝&nbsp;[#95042](https://github.com/openclaw/openclaw/issues/95042) | 0 | Local memory/embedding | @1attila2 | [Bug]: 2026.6.x regression cascade — memory search broken, then sessions lost on every reconnect (multi-agent deployment broken) |
| 🔀&nbsp;[#95036](https://github.com/openclaw/openclaw/pull/95036) | 0 | Local memory/embedding | @aniruddhaadak80 | fix(memory): preserve Windows backslashes in qmd command paths [AI-assisted] |
| 🔀&nbsp;[#95034](https://github.com/openclaw/openclaw/pull/95034) | 0 | Model/provider behavior | @AxelHu | fix(embedded-agent): auto-recover provider-rejected image history (closes #94906) |
| 🔀&nbsp;[#95022](https://github.com/openclaw/openclaw/pull/95022) | 0 | Local memory/embedding | @ml12580 | fix(memory-qmd): preserve unquoted Windows absolute paths in qmd command [AI-assisted] |
| 🔀&nbsp;[#95006](https://github.com/openclaw/openclaw/pull/95006) | 0 | Local memory/embedding | @mmyzwl | fix(memory): default memorySearch provider to "auto" instead of "openai" |
| 📝&nbsp;[#95003](https://github.com/openclaw/openclaw/issues/95003) | 0 | Local memory/embedding | @Wagregg | [Bug]: [Regression] [LOCALLY HOTFIXED] Memory search fails with "index metadata is missing" after Node.js 22.22.2 → 22.22.3 upgrade (apt) |
| 📝&nbsp;[#94998](https://github.com/openclaw/openclaw/issues/94998) | 0 | Model routing/config | @cls3389 | AbortError timeout not detected — fallback not triggered on provider transport timeout |
| 📝&nbsp;[#94992](https://github.com/openclaw/openclaw/issues/94992) | 0 | Model/provider behavior | @911erik | [Bug]: Invalid signature in thinking block on every agent — persists on v2026.6.1 |
| 🔀&nbsp;[#94988](https://github.com/openclaw/openclaw/pull/94988) | 0 | OpenAI-compatible/proxy | @hugenshen | Codex/fix 94979 kimi web search baseurl |
| 🔀&nbsp;[#94985](https://github.com/openclaw/openclaw/pull/94985) | 0 | Local memory/embedding | @ml12580 | fix(memory-core): skip markdown placeholder snippets in short-term promotion (#80582) [AI-assisted] |
| 🔀&nbsp;[#94982](https://github.com/openclaw/openclaw/pull/94982) | 0 | Local memory/embedding | @jincheng-xydt | fix: preserve Windows path separators in splitShellArgs (#92302) |
| 📝&nbsp;[#94979](https://github.com/openclaw/openclaw/issues/94979) | 0 | Open-weight/provider behavior | @bici926434 | [Bug]: web_search (kimi) returns 401 Invalid Authentication despite valid API key |
| 🔀&nbsp;[#94961](https://github.com/openclaw/openclaw/pull/94961) | 0 | Model routing/config | @jincheng-xydt | fix: propagate lossless-claw allowModelOverride at config normalization (#94289) |
| 🔀&nbsp;[#94960](https://github.com/openclaw/openclaw/pull/94960) | 0 | Open-weight/provider behavior | @jincheng-xydt | fix: add MiniMax M3/M2.7 to reasoning content replay allowlist (#92769) |
| 🔀&nbsp;[#94958](https://github.com/openclaw/openclaw/pull/94958) | 0 | Local memory/embedding | @lzyyzznl | fix(memory): preserve Windows backslash paths in QMD command resolution |
| 🔀&nbsp;[#94954](https://github.com/openclaw/openclaw/pull/94954) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): increase narrative timeout from 60s to 120s for ARM workloads (fixes #92494) |
| 🔀&nbsp;[#94945](https://github.com/openclaw/openclaw/pull/94945) | 0 | OpenAI-compatible/proxy | @ai-hpc | fix(openai-completions): keep cache-boundary suffix out of DeepSeek's implicit prefix cache |
| 🔀&nbsp;[#94941](https://github.com/openclaw/openclaw/pull/94941) | 0 | Local memory/embedding | @lzyyzznl | fix(memory-qmd): preserve Windows absolute paths in memory.qmd.command |
| 📝&nbsp;[#94919](https://github.com/openclaw/openclaw/issues/94919) | 0 | Open-weight/provider behavior | @moccassins | [Bug]: Z.AI Coding-Plan: ECONNRESET triggers model fallback — fallback notice is invisible to the user in async contexts (cron jobs, sub-agents, isolated runs) |
| 🔀&nbsp;[#94918](https://github.com/openclaw/openclaw/pull/94918) | 0 | Model routing/config | @zhangqueping | feat(cron): expose --fallbacks option on cron create and edit commands |
| 🔀&nbsp;[#94914](https://github.com/openclaw/openclaw/pull/94914) | 0 | Model routing/config | @aniruddhaadak80 | fix(models): filter models list by configured providers in replace mode [AI-assisted] |
| 🔀&nbsp;[#94911](https://github.com/openclaw/openclaw/pull/94911) | 0 | Model/provider behavior | @zhangqueping | fix(byteplus): add missing cacheRead/cacheWrite pricing for BytePlus models |
| 📝&nbsp;[#94908](https://github.com/openclaw/openclaw/issues/94908) | 0 | OpenAI-compatible/proxy | @Naruto2018 | [Bug]: /v1/responses does not retain conversation context when using the same user value |
| 📝&nbsp;[#94906](https://github.com/openclaw/openclaw/issues/94906) | 0 | Model/provider behavior | @AxelHu | Add recovery path for provider-rejected image blocks in session history |
| 🔀&nbsp;[#94890](https://github.com/openclaw/openclaw/pull/94890) | 0 | Model/provider behavior | @zhangqueping | fix(diagnostic): lower stall abort threshold and extend model-call recovery to CLI sessions |
| 📝&nbsp;[#94888](https://github.com/openclaw/openclaw/issues/94888) | 0 | Local memory/embedding | @bizzle12368239 | Memory indexer fails to pick up files in agents that haven't been invoked in the current session |
| 🔀&nbsp;[#94884](https://github.com/openclaw/openclaw/pull/94884) | 0 | Model/provider behavior | @zhangqueping | fix(feishu): replace empty Type.Any() with non-empty FlexibleValue in bitable schemas |
| 🔀&nbsp;[#94882](https://github.com/openclaw/openclaw/pull/94882) | 0 | Local model runtime | @lzyyzznl | fix(ollama): treat undefined reasoning as potentially reasoning-capable |
| 🔀&nbsp;[#94875](https://github.com/openclaw/openclaw/pull/94875) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): increase narrative timeout from 60s to 120s for ARM devices (fixes #92494) |
| 🔀&nbsp;[#94841](https://github.com/openclaw/openclaw/pull/94841) | 0 | Local memory/embedding | @Pick-cat | fix(qmd): preserve Windows absolute paths in command resolution |
| 🔀&nbsp;[#94839](https://github.com/openclaw/openclaw/pull/94839) | 0 | Model/provider behavior | @lzyyzznl | fix(feishu): replace Type.Record(Type.String(), Type.Any()) with Type.Object({}, {additionalProperties: true}) in bitable tools |
| 🔀&nbsp;[#94825](https://github.com/openclaw/openclaw/pull/94825) | 0 | Model routing/config | @TUARAN | fix: respect replace mode in default models list |
| 🔀&nbsp;[#94817](https://github.com/openclaw/openclaw/pull/94817) | 0 | Local model runtime | @lzyyzznl | fix(ollama): treat undefined reasoning as potentially reasoning-capable |
| 🔀&nbsp;[#94811](https://github.com/openclaw/openclaw/pull/94811) | 0 | Local memory/embedding | @mushuiyu886 | fix(ollama): honor memory embedding output dimensionality |
| 🔀&nbsp;[#94783](https://github.com/openclaw/openclaw/pull/94783) | 0 | Local memory/embedding | @bowenluo718 | fix(memory-core): lower default promotion minScore for Gemini embedding compatibility |
| 📝&nbsp;[#94780](https://github.com/openclaw/openclaw/issues/94780) | 0 | Model routing/config | @Haderach-Ram | [Feature]: Per-cron model selection independent of agent default - run cheap/free models on automation jobs while keeping main agent on premium LLM |
| 🔀&nbsp;[#94773](https://github.com/openclaw/openclaw/pull/94773) | 0 | Local memory/embedding | @bowenluo718 | refactor(memory): add LEARNINGS.md to workspace memory artifact discovery |
| 🔀&nbsp;[#94770](https://github.com/openclaw/openclaw/pull/94770) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): align session file counter denominator with indexer filter (fixes #77338) |
| 📝&nbsp;[#94769](https://github.com/openclaw/openclaw/issues/94769) | 0 | Local memory/embedding | @ITHACAJASON | Memory dreaming promotion: short-term recall signals collected but never promote with Gemini embeddings (structural threshold mismatch + read/exec signal gap) |
| 🔀&nbsp;[#94763](https://github.com/openclaw/openclaw/pull/94763) | 0 | Local memory/embedding | @chenyangjun-xy | fix(embedding): restrict openai-compatible dimensions to api.openai.com to prevent connection resets on self-hosted servers |
| 🔀&nbsp;[#94758](https://github.com/openclaw/openclaw/pull/94758) | 0 | Model routing/config | @mazhuima | fix(gateway): propagate allowModelOverride policies from auto-enabled config at startup |
| 🔀&nbsp;[#94752](https://github.com/openclaw/openclaw/pull/94752) | 0 | Model routing/config | @snowzlmbot | fix(reply): clarify stale model override resets |
| 🔀&nbsp;[#94745](https://github.com/openclaw/openclaw/pull/94745) | 0 | Model routing/config | @bowenluo718 | fix(session): avoid misleading rejection message for stale auto overrides in allowlist |
| 🔀&nbsp;[#94735](https://github.com/openclaw/openclaw/pull/94735) | 0 | Model routing/config | @Monkey-wusky | fix(models): respect models.mode=replace in 'openclaw models list' output |
| 🔀&nbsp;[#94732](https://github.com/openclaw/openclaw/pull/94732) | 0 | Local memory/embedding | @xydt-tanshanshan | fix(memory): add batch completed log after embedding batch finishes |
| 🔀&nbsp;[#94728](https://github.com/openclaw/openclaw/pull/94728) | 0 | Model routing/config | @xydt-tanshanshan | fix(sessions): skip inherited modelOverride when parent model is not in allowlist |
| 🔀&nbsp;[#94726](https://github.com/openclaw/openclaw/pull/94726) | 0 | Model routing/config | @ajwan8998 | fix(google): add gemini-3.5-flash model catalog entry |
| 🔀&nbsp;[#94722](https://github.com/openclaw/openclaw/pull/94722) | 0 | Model routing/config | @ZOOWH | fix(models): respect models.mode: "replace" in models list output |
| 📝&nbsp;[#94713](https://github.com/openclaw/openclaw/issues/94713) | 0 | Model routing/config | @Gr4via | [Bug]: Dashboard child-session rollover can reject allowed openai/gpt-5.5 and revert to stale gpt-5.4 |
| 🔀&nbsp;[#94706](https://github.com/openclaw/openclaw/pull/94706) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): increase narrative timeout from 60s to 120s for ARM workloads (fixes #92494) |
| 📝&nbsp;[#94705](https://github.com/openclaw/openclaw/issues/94705) | 0 | Model routing/config | @apoapostolov | models.mode: "replace" does not filter openclaw models list output |
| 🔀&nbsp;[#94700](https://github.com/openclaw/openclaw/pull/94700) | 0 | OpenAI-compatible/proxy | @RomneyDa | test: fold HTTP API script proof into QA Lab |
| 📝&nbsp;[#94686](https://github.com/openclaw/openclaw/issues/94686) | 0 | Model/provider behavior | @CarotaWealth | Critical Fleet Stability Issues — Multi-Agent Session Crashes (thinking block corruption, session bloat, cron contention) |
| 🔀&nbsp;[#94671](https://github.com/openclaw/openclaw/pull/94671) | 0 | Local memory/embedding | @vincentkoc | feat(memory): unify agent-scoped memory configuration<br>Assignee: vincentkoc |
| 🔀&nbsp;[#94665](https://github.com/openclaw/openclaw/pull/94665) | 0 | Local memory/embedding | @lzyyzznl | fix: #92302 preserve Windows absolute paths in QMD command resolution |
| 🔀&nbsp;[#94662](https://github.com/openclaw/openclaw/pull/94662) | 0 | OpenAI-compatible/proxy | @XSIRIX | fix(xai): allow private self-hosted Responses endpoints |
| 🔀&nbsp;[#94653](https://github.com/openclaw/openclaw/pull/94653) | 0 | Model routing/config | @zenglingbiao | feat(cron): expose --fallbacks flag on cron add/create and edit commands (fixes #90302) |
| 📝&nbsp;[#94650](https://github.com/openclaw/openclaw/issues/94650) | 0 | Open-weight/provider behavior | @ArisMontclair | Gateway watchdog fails to kill stuck model calls; stall recovery is none |
| 🔀&nbsp;[#94646](https://github.com/openclaw/openclaw/pull/94646) | 0 | Local memory/embedding | @vincentkoc | refactor(sqlite): land database-first memory and proxy alignment |
| 🔀&nbsp;[#94636](https://github.com/openclaw/openclaw/pull/94636) | 0 | Local memory/embedding | @tayoun | fix(memory): skip raw snippets during promotion |
| 🔀&nbsp;[#94633](https://github.com/openclaw/openclaw/pull/94633) | 0 | Model/provider behavior | @ZOOWH | fix(feishu): replace empty bitable record value schema rejected by strict validators |
| 🔀&nbsp;[#94628](https://github.com/openclaw/openclaw/pull/94628) | 0 | OpenAI-compatible/proxy | @yu-xin-c | [codex] Forward run context request headers |
| 🔀&nbsp;[#94625](https://github.com/openclaw/openclaw/pull/94625) | 0 | Local memory/embedding | @googlerest | investigate(memory-core): root-cause for #84882 dreaming silent daily-file deletion |
| 📝&nbsp;[#94623](https://github.com/openclaw/openclaw/issues/94623) | 0 | Model routing/config | @yancankang | [Bug]: Rate-limit quota suspension blocks model fallback — session freezes 30min despite available fallback chain |
| 📝&nbsp;[#94621](https://github.com/openclaw/openclaw/issues/94621) | 0 | Model routing/config | @yancankang | [Bug]: Rate-limit quota suspension blocks model fallback — session freezes 30min despite available fallback chain |
| 🔀&nbsp;[#94590](https://github.com/openclaw/openclaw/pull/94590) | 0 | OpenAI-compatible/proxy | @bowenluo718 | feat(config): allow modelIdNormalization in models.providers config |
| 🔀&nbsp;[#94585](https://github.com/openclaw/openclaw/pull/94585) | 0 | Open-weight/provider behavior | @idootop | feat(xiaomi): add MiMo V2.5 models to the pay-as-you-go provider |
| 🔀&nbsp;[#94582](https://github.com/openclaw/openclaw/pull/94582) | 0 | OpenAI-compatible/proxy | @bowenluo718 | fix(openai-completions): add disableBoundaryAwareCache compat option for prefix-matching cache providers |
| 📝&nbsp;[#94581](https://github.com/openclaw/openclaw/issues/94581) | 0 | Local memory/embedding | @junxuku-byte | Feature Request: memsearch agent_id filtering for multi-agent memory isolation |
| 🔀&nbsp;[#94579](https://github.com/openclaw/openclaw/pull/94579) | 0 | Local memory/embedding | @yunze7373 | feat(xmemo-memory): add bundled XMemo cloud memory plugin |
| 🔀&nbsp;[#94564](https://github.com/openclaw/openclaw/pull/94564) | 0 | Local memory/embedding | @esqandil | fix(memory-core): bound zero-hit forced sync so memory_search can't hang the whole deadline |
| 📝&nbsp;[#94557](https://github.com/openclaw/openclaw/issues/94557) | 0 | OpenAI-compatible/proxy | @alexminza | [Feature]: Use any native model provider through the Cloudflare AI Gateway by allowing `modelIdNormalization` in `models.providers.<provider>` config |
| 📝&nbsp;[#94554](https://github.com/openclaw/openclaw/issues/94554) | 0 | OpenAI-compatible/proxy | @alexminza | [Feature]: `cloudflare-ai-gateway` is a single-model Anthropic passthrough, not a bridge to AI Gateway |
| 📝&nbsp;[#94547](https://github.com/openclaw/openclaw/issues/94547) | 0 | Model/provider behavior | @TwinsLee | [Bug]: @openclaw/feishu bitable write tools emit invalid JSON Schema (empty patternProperties sub-schema) — breaks Anthropic via AWS Bedrock |
| 🔀&nbsp;[#94540](https://github.com/openclaw/openclaw/pull/94540) | 0 | Model routing/config | @sunlit-deng | fix: LCM compaction fails: allowModelOverride not propagated to plugin runtime client until config hot-reload |
| 🔀&nbsp;[#94537](https://github.com/openclaw/openclaw/pull/94537) | 0 | Local memory/embedding | @SunnyShu0925 | fix(memory-core): harden dreaming daily-file writes and drain dangling recall refs |
| 📝&nbsp;[#94534](https://github.com/openclaw/openclaw/issues/94534) | 0 | Model routing/config | @davidcittadini | Recurring "Invalid signature in thinking block" poisons sessions across agents |
| 🔀&nbsp;[#94520](https://github.com/openclaw/openclaw/pull/94520) | 0 | Model/provider behavior | @pedrosbraga | fix(xai): normalize grok web search tools |
| 📝&nbsp;[#94518](https://github.com/openclaw/openclaw/issues/94518) | 0 | OpenAI-compatible/proxy | @xiep-dot | DeepSeek cache hit rate <10% after 6.x upgrade - boundary-aware caching breaks prefix matching |
| 🔀&nbsp;[#94509](https://github.com/openclaw/openclaw/pull/94509) | 0 | Local memory/embedding | @chenweicong736 | fix(memory-wiki): honor durable: true frontmatter in stale pages report |
| 🔀&nbsp;[#94503](https://github.com/openclaw/openclaw/pull/94503) | 0 | Local memory/embedding | @lsr911 | fix(compaction): emit after_compaction hook even when compacted:false |
| 📝&nbsp;[#94500](https://github.com/openclaw/openclaw/issues/94500) | 0 | Local memory/embedding | @garrytan-agents | memory_search tool reports "index metadata is missing" in-gateway while CLI reads the same store as healthy (identity resolved before provider init, never recomputed) |
| 🔀&nbsp;[#94495](https://github.com/openclaw/openclaw/pull/94495) | 0 | Local model runtime | @LZY3538 | fix(ollama): add request timeout fallback for remote hosts |
| 🔀&nbsp;[#94494](https://github.com/openclaw/openclaw/pull/94494) | 0 | Model routing/config | @xialonglee | fix(agents): map cacheRetention 'standard' to 'short' for Bedrock Claude models |
| 🔀&nbsp;[#94493](https://github.com/openclaw/openclaw/pull/94493) | 0 | Model routing/config | @LZY3538 | fix(anthropic): strip thinking blocks from completed prior assistant turns |
| 🔀&nbsp;[#94490](https://github.com/openclaw/openclaw/pull/94490) | 0 | Model routing/config | @LZY3538 | fix(compaction): wire aggregate retry timeout through compaction.timeoutSeconds |
| 🔀&nbsp;[#94487](https://github.com/openclaw/openclaw/pull/94487) | 0 | Model routing/config | @zhiqiang26 | fix: #94482 normalize cacheRetention 'standard' to 'short' |
| 📝&nbsp;[#94482](https://github.com/openclaw/openclaw/issues/94482) | 0 | Model routing/config | @aaronedell | Bedrock Claude cacheRetention='standard' is silently ignored |
| 🔀&nbsp;[#94481](https://github.com/openclaw/openclaw/pull/94481) | 0 | Open-weight/provider behavior | @lsr911 | fix(edit): unwrap XML-RPC {item: {oldText, newText}} edit transport shape |
| 🔀&nbsp;[#94478](https://github.com/openclaw/openclaw/pull/94478) | 0 | Model routing/config | @TurboTheTurtle | fix(codex): restore openai-codex catalog alias |
| 🔀&nbsp;[#94477](https://github.com/openclaw/openclaw/pull/94477) | 0 | Model routing/config | @xydt-tanshanshan | [AI] fix(session): add session.restartContinuation config to preserve sessionId across Gateway restart |
| 🔀&nbsp;[#94473](https://github.com/openclaw/openclaw/pull/94473) | 0 | OpenAI-compatible/proxy | @LiuwqGit | fix(provider-catalog): use apiKey fallback for self-hosted discovery when discoveryApiKey is undefined (fixes #83461) |
| 🔀&nbsp;[#94461](https://github.com/openclaw/openclaw/pull/94461) | 0 | OpenAI-compatible/proxy | @Pandah97 | fix(zai): fall back to manifest baseUrl for synthesized GLM-5 models |
| 📝&nbsp;[#94458](https://github.com/openclaw/openclaw/issues/94458) | 0 | Model routing/config | @hurtlovewow | lossless-claw bootstraps into quarantine after every Gateway restart due to new sessionId generating fresh JSONL file |
| 🔀&nbsp;[#94446](https://github.com/openclaw/openclaw/pull/94446) | 0 | Model routing/config | @xydttsw | fix(context-engine): eagerly resolve plugin LLM policy from config for model override authority |
| 🔀&nbsp;[#94443](https://github.com/openclaw/openclaw/pull/94443) | 0 | Local memory/embedding | @ZengWen-DT | fix(memory-wiki): retry transient source-page rewrite race instead of aborting wiki_status |
| 🔀&nbsp;[#94440](https://github.com/openclaw/openclaw/pull/94440) | 0 | Model routing/config | @lzyyzznl | fix: #94432 classify Cloudflare challenge 403 as upstream_html instead of auth_html |
| 📝&nbsp;[#94432](https://github.com/openclaw/openclaw/issues/94432) | 0 | Model routing/config | @pbm9z95m6z-hue | OpenAI/Codex OAuth provider fails with Cloudflare HTML 403 from chatgpt.com/backend-api |
| 🔀&nbsp;[#94430](https://github.com/openclaw/openclaw/pull/94430) | 0 | Model routing/config | @xiongxiaoyang-cell | fix(errors): recognize content policy / new_sensitive errors as rate_limit for fallback |
| 🔀&nbsp;[#94429](https://github.com/openclaw/openclaw/pull/94429) | 0 | Model routing/config | @zhiqiang26 | fix: #94391 将 compaction aggregate timeout 从硬编码 60s 改为读取 compaction.timeoutSeconds 配置 |
| 🔀&nbsp;[#94419](https://github.com/openclaw/openclaw/pull/94419) | 0 | Open-weight/provider behavior | @Omee11 | feat(qwen): add Token Plan (Team Edition) provider |
| 📝&nbsp;[#94418](https://github.com/openclaw/openclaw/issues/94418) | 0 | Open-weight/provider behavior | @Omee11 | [Feature]: Alibaba Model Studio Token Plan (Team Edition) provider |
| 🔀&nbsp;[#94404](https://github.com/openclaw/openclaw/pull/94404) | 0 | OpenAI-compatible/proxy | @xydttsw | fix(zai): fall back to default baseUrl when template lacks one for catalog models |
| 🔀&nbsp;[#94402](https://github.com/openclaw/openclaw/pull/94402) | 0 | OpenAI-compatible/proxy | @Jah-xy | fix: handle object-format data and URL-safe base64 from OpenAI-compatible proxy responses |
| 🔀&nbsp;[#94401](https://github.com/openclaw/openclaw/pull/94401) | 0 | Local memory/embedding | @SunnyShu0925 | fix(session-memory): skip transcript-only assistant messages in getRecentSessionContent |
| 🔀&nbsp;[#94378](https://github.com/openclaw/openclaw/pull/94378) | 0 | OpenAI-compatible/proxy | @zhiqiang26 | fix(image-gen): skip invalid entries in OpenAI-compatible image response parsing |
| 🔀&nbsp;[#94372](https://github.com/openclaw/openclaw/pull/94372) | 0 | Model routing/config | @ajwan8998 | fix(cli): resolve context window from context.ts to ensure cache is loaded |
| 📝&nbsp;[#94367](https://github.com/openclaw/openclaw/issues/94367) | 0 | OpenAI-compatible/proxy | @ff5278 | [Bug]: Image generation "response malformed" when using OpenAI-compatible proxy with valid b64_json response |
| 🔀&nbsp;[#94362](https://github.com/openclaw/openclaw/pull/94362) | 0 | Local model runtime | @lizanle521 | fix: improve Ollama thinking profile resolution for live-discovered reasoning models using name heuristic |
| 🔀&nbsp;[#94355](https://github.com/openclaw/openclaw/pull/94355) | 0 | Local memory/embedding | @SunnyShu0925 | fix(agents): fall back to generic embedding provider registry in memory-search config resolution |
| 🔀&nbsp;[#94350](https://github.com/openclaw/openclaw/pull/94350) | 0 | Model/provider behavior | @Patrick-Erichsen | feat: externalize GMI provider plugin |
| 🔀&nbsp;[#94344](https://github.com/openclaw/openclaw/pull/94344) | 0 | Local memory/embedding | @mushuiyu886 | fix #94166: memory-core OpenAI-compatible embeddings: honor provider request.allowPrivateNetwork |
| 🔀&nbsp;[#94333](https://github.com/openclaw/openclaw/pull/94333) | 0 | Model routing/config | @zhangqueping | fix(agents): read allowModelOverride from plugin config in context-engine capabilities |
| 🔀&nbsp;[#94331](https://github.com/openclaw/openclaw/pull/94331) | 0 | Model routing/config | @sheyanmin | fix: merge llm policy into plugin subagent override authorization |
| 📝&nbsp;[#94330](https://github.com/openclaw/openclaw/issues/94330) | 0 | Model routing/config | @wayrk | replay_invalid (stale thinking-block signature) surfaces a hard error + drops the user message instead of self-recovering |
| 📝&nbsp;[#94316](https://github.com/openclaw/openclaw/issues/94316) | 0 | Local memory/embedding | @rglover666 | Memory search tool cannot find local embedding provider even though CLI shows it as ready |
| 🔀&nbsp;[#94311](https://github.com/openclaw/openclaw/pull/94311) | 0 | Model routing/config | @lzyyzznl | fix: #94289 auto-grant lossless-claw model override from summaryModel config |
| 🔀&nbsp;[#94297](https://github.com/openclaw/openclaw/pull/94297) | 0 | Model routing/config | @zenglingbiao | fix(plugins): propagate llm.allowModelOverride to plugin subagent override policies (fixes #94289) |
| 📝&nbsp;[#94289](https://github.com/openclaw/openclaw/issues/94289) | 0 | Model routing/config | @Nardoa375 | [Bug]: LCM compaction fails: allowModelOverride not propagated to plugin runtime client until config hot-reload |
| 🔀&nbsp;[#94288](https://github.com/openclaw/openclaw/pull/94288) | 0 | Local memory/embedding | @khalil-omer | fix(memory): refresh stale index handles after cli reindex |
| 📝&nbsp;[#94275](https://github.com/openclaw/openclaw/issues/94275) | 0 | OpenAI-compatible/proxy | @Voltarr | Google provider: AQ. format API keys rejected by OpenAI-compatible endpoint (HTTP 401) |
| 📝&nbsp;[#94269](https://github.com/openclaw/openclaw/issues/94269) | 0 | OpenAI-compatible/proxy | @chrysb | Z.ai static catalog models resolve without baseUrl and fall through to OpenAI API |
| 🔀&nbsp;[#94261](https://github.com/openclaw/openclaw/pull/94261) | 0 | OpenAI-compatible/proxy | @natecl | [Feature]: [FEAT]: Add Adorbis AI as a bundled provider plugin |
| 📝&nbsp;[#94258](https://github.com/openclaw/openclaw/issues/94258) | 0 | Model routing/config | @GuyMayer | Bug: Tier routing not resolving tier-* aliases to actual models in v2026.6.8 |
| 🔀&nbsp;[#94252](https://github.com/openclaw/openclaw/pull/94252) | 0 | Local memory/embedding | @bennewell35 | fix(memory): scrub stale dreaming sessions on startup |
| 📝&nbsp;[#94251](https://github.com/openclaw/openclaw/issues/94251) | 0 | Local model runtime | @tborer | [Bug]: Ollama remote provider streaming not consumed — model_call:started never progresses in chat sessions |
| 🔀&nbsp;[#94244](https://github.com/openclaw/openclaw/pull/94244) | 0 | Open-weight/provider behavior | @Joel-Claw | fix: strip plain-text reasoning from GLM-5.x models |
| 📝&nbsp;[#94242](https://github.com/openclaw/openclaw/issues/94242) | 0 | OpenAI-compatible/proxy | @adorbistech | [Feature]: [FEAT]: Add Adorbis AI as a bundled provider plugin |
| 🔀&nbsp;[#94240](https://github.com/openclaw/openclaw/pull/94240) | 0 | OpenAI-compatible/proxy | @SunnyShu0925 | fix(memory-core): degrade non-local embedding provider on persistent failure |
| 🔀&nbsp;[#94239](https://github.com/openclaw/openclaw/pull/94239) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): align session file counter denominator with indexer filter |
| 🔀&nbsp;[#94234](https://github.com/openclaw/openclaw/pull/94234) | 0 | Model routing/config | @lsr911 | fix(anthropic): allow failover for thinking signature replay errors |
| 📝&nbsp;[#94228](https://github.com/openclaw/openclaw/issues/94228) | 0 | Model routing/config | @eugkhp | Native Anthropic path: replaying historical `thinking` blocks bricks long tool-use threads (`Invalid signature in thinking block` 400) |
| 🔀&nbsp;[#94214](https://github.com/openclaw/openclaw/pull/94214) | 0 | Local model runtime | @Pandah97 | fix(ollama): resolve thinking profile for live-discovered models |
| 🔀&nbsp;[#94210](https://github.com/openclaw/openclaw/pull/94210) | 0 | Model routing/config | @Pandah97 | fix(cli): resolve 200K context window fallback in status command |
| 🔀&nbsp;[#94209](https://github.com/openclaw/openclaw/pull/94209) | 0 | Model routing/config | @lsr911 | fix(model): cap contextWindow at native runtime catalog limit when user config exceeds it |
| 📝&nbsp;[#94184](https://github.com/openclaw/openclaw/issues/94184) | 0 | Model routing/config | @Sleepyarno | Externalised @openclaw/codex (openai-codex OAuth) provider fails to register catalog on 2026.6.x (works on 2026.5.27) |
| 🔀&nbsp;[#94180](https://github.com/openclaw/openclaw/pull/94180) | 0 | Local memory/embedding | @SunnyShu0925 | feat(memory-core): allow private network endpoints for memory embeddi… |
| 📝&nbsp;[#94166](https://github.com/openclaw/openclaw/issues/94166) | 0 | Local memory/embedding | @dmorn | memory-core OpenAI-compatible embeddings cannot use explicitly configured private endpoints |
| 🔀&nbsp;[#94165](https://github.com/openclaw/openclaw/pull/94165) | 0 | Open-weight/provider behavior | @Alix-007 | fix(control-ui): recognize namespaced reasoning tags in thinking extraction |
| 🔀&nbsp;[#94136](https://github.com/openclaw/openclaw/pull/94136) | 0 | Open-weight/provider behavior | @BorClaw | fix(zai): expose GLM-5.2 reasoning levels [AI-assisted] |
| 🔀&nbsp;[#94135](https://github.com/openclaw/openclaw/pull/94135) | 0 | Local memory/embedding | @Pick-cat | fix(memory-core): index memory path in FTS text for filename queries (fixes #94102) |
| 📝&nbsp;[#94125](https://github.com/openclaw/openclaw/issues/94125) | 0 | Local memory/embedding | @thedoctormes-hue | [Bug]: Memory search completely broken — FTS-only hangs, embeddings hang, --force corrupts meta (Ollama/bge-m3, Linux, 2026.6.8) |
| 🔀&nbsp;[#94114](https://github.com/openclaw/openclaw/pull/94114) | 0 | Local memory/embedding | @zhangguiping-xydt | fix(memory-core): include path in FTS indexed text so filename tokens are searchable |
| 🔀&nbsp;[#94106](https://github.com/openclaw/openclaw/pull/94106) | 0 | OpenAI-compatible/proxy | @yetval | fix(secrets): scope env scrub to migrated providers' vars |
| 📝&nbsp;[#94102](https://github.com/openclaw/openclaw/issues/94102) | 0 | Local memory/embedding | @alexph-dev | memory_search ranks filename/date-token queries poorly despite clean index and working content search |
| 🔀&nbsp;[#94071](https://github.com/openclaw/openclaw/pull/94071) | 0 | Local memory/embedding | @zhanxingxin1998 | fix(memory-lancedb): stop forwarding embedding dimensions upstream |
| 🔀&nbsp;[#94067](https://github.com/openclaw/openclaw/pull/94067) | 0 | Local model runtime | @openperf | fix(channels): resolve native /think menu levels via runtime catalog for live-discovered models |
| 🔀&nbsp;[#94066](https://github.com/openclaw/openclaw/pull/94066) | 0 | Open-weight/provider behavior | @zhanxingxin1998 | fix(qwen): enable qwen3.6-plus on Coding Plan CN, correct reasoning flag |
| 🔀&nbsp;[#94064](https://github.com/openclaw/openclaw/pull/94064) | 0 | Model/provider behavior | @zhanxingxin1998 | feat(huggingface): add text-to-image generation via hf-inference Inference Providers route |
| 🔀&nbsp;[#94062](https://github.com/openclaw/openclaw/pull/94062) | 0 | Local model runtime | @hugenshen | fix(agents): classify generic "LLM request failed." as transient time… |
| 🔀&nbsp;[#94038](https://github.com/openclaw/openclaw/pull/94038) | 0 | Open-weight/provider behavior | @zhangguiping-xydt | fix(matrix): recognize MiniMax mm: namespaced reasoning tags in monitor replies |
| 🔀&nbsp;[#94021](https://github.com/openclaw/openclaw/pull/94021) | 0 | Local model runtime | @lsr911 | fix(agents): classify local model not loaded/ready as overloaded for model fallback |
| 🔀&nbsp;[#94017](https://github.com/openclaw/openclaw/pull/94017) | 0 | Local model runtime | @mazhuima | fix(think): skip provider profile when model not in catalog |
| 🔀&nbsp;[#94012](https://github.com/openclaw/openclaw/pull/94012) | 0 | OpenAI-compatible/proxy | @vincentkoc | feat: route canonical provider models through ClawRouter |
| 🔀&nbsp;[#94011](https://github.com/openclaw/openclaw/pull/94011) | 0 | Model routing/config | @ajwan8998 | fix(cron): treat generic 'LLM request failed' error as transient server_error |
| 🔀&nbsp;[#94004](https://github.com/openclaw/openclaw/pull/94004) | 0 | Local memory/embedding | @vincentkoc | refactor(sqlite): canonicalize memory and proxy storage<br>Assignee: vincentkoc |
| 🔀&nbsp;[#93969](https://github.com/openclaw/openclaw/pull/93969) | 0 | Model routing/config | @xialonglee | fix(xai): reject unsupported multi-agent model refs before runtime fallback |
| 📝&nbsp;[#93968](https://github.com/openclaw/openclaw/issues/93968) | 0 | Local memory/embedding | @edisonxl | [Bug 6.1] Silent config auto-patch from memory-core + error-message auto-fix breaks all cron jobs on hosts without Docker |
| 🔀&nbsp;[#93965](https://github.com/openclaw/openclaw/pull/93965) | 0 | OpenAI-compatible/proxy | @zhangguiping-xydt | [Bug]: opencode-go provider streaming — API calls complete on provider side but gateway never receives stream termination signal |
| 🔀&nbsp;[#93956](https://github.com/openclaw/openclaw/pull/93956) | 0 | Local model runtime | @jason-allen-oneal | fix(ollama): skip auto-discovery for remote/cloud base URLs |
| 🔀&nbsp;[#93946](https://github.com/openclaw/openclaw/pull/93946) | 0 | Local model runtime | @Alix-007 | fix(ollama): show full thinking levels for discovered reasoning models |
| 📝&nbsp;[#93931](https://github.com/openclaw/openclaw/issues/93931) | 0 | Model routing/config | @hyphae-bot | Configured model fallbacks (payload.fallbacks) never engage on generic 'LLM request failed.' errors — fallbackUsed: false on every cron failure |
| 🔀&nbsp;[#93926](https://github.com/openclaw/openclaw/pull/93926) | 0 | Open-weight/provider behavior | @Alix-007 | fix(matrix): recognize MiniMax mm: namespaced reasoning tags in monitor suppression |
| 🔀&nbsp;[#93897](https://github.com/openclaw/openclaw/pull/93897) | 0 | OpenAI-compatible/proxy | @lsr911 | fix(doctor): deep-merge openai-codex plugin entry when openai already exists |
| 📝&nbsp;[#93891](https://github.com/openclaw/openclaw/issues/93891) | 0 | OpenAI-compatible/proxy | @Nas01010101 | Bug: rewritePluginEntries silently drops openai-codex config when openai entry already present |
| 🔀&nbsp;[#93882](https://github.com/openclaw/openclaw/pull/93882) | 0 | Local model runtime | @xydttsw | fix(telegram): show full think levels for live-discovered Ollama models |
| 🔀&nbsp;[#93878](https://github.com/openclaw/openclaw/pull/93878) | 0 | Local memory/embedding | @sheyanmin | fix: route memory embeddings to configured baseURL for openai provider |
| 🔀&nbsp;[#93874](https://github.com/openclaw/openclaw/pull/93874) | 0 | Open-weight/provider behavior | @Alix-007 | fix(slack): recognize MiniMax mm: namespaced reasoning tags in monitor preview |
| 🔀&nbsp;[#93872](https://github.com/openclaw/openclaw/pull/93872) | 0 | Local model runtime | @lzyyzznl | fix(ollama): show full thinking levels for live-discovered models in /think menu |
| 🔀&nbsp;[#93868](https://github.com/openclaw/openclaw/pull/93868) | 0 | Local/media model provider | @harjothkhara | fix(gateway): dedupe TTS status provider diagnostics [AI-assisted] |
| 🔀&nbsp;[#93864](https://github.com/openclaw/openclaw/pull/93864) | 0 | Local model runtime | @Jah-xy | fix(ollama): show all thinking levels in /think menu for dynamically-discovered models |
| 🔀&nbsp;[#93853](https://github.com/openclaw/openclaw/pull/93853) | 0 | Local memory/embedding | @xydt-tanshanshan | [AI] fix(agents): route memory embedding through generic resolution when provider has custom baseUrl |
| 🔀&nbsp;[#93844](https://github.com/openclaw/openclaw/pull/93844) | 0 | Local model runtime | @lzyyzznl | fix(ollama): resolve thinking profile for live-discovered models |
| 📝&nbsp;[#93835](https://github.com/openclaw/openclaw/issues/93835) | 0 | Local model runtime | @civiltox | [Bug]: Telegram /think menu shows only off for live-discovered Ollama thinking models, but /think &lt;level&gt; accepts them |
| 🔀&nbsp;[#93833](https://github.com/openclaw/openclaw/pull/93833) | 0 | OpenAI-compatible/proxy | @zhangguiping-xydt | Fix Azure Responses model alias routing |
| 🔀&nbsp;[#93832](https://github.com/openclaw/openclaw/pull/93832) | 0 | OpenAI-compatible/proxy | @vincentkoc | feat(providers): add ClawRouter managed proxy<br>Assignee: vincentkoc |
| 🔀&nbsp;[#93829](https://github.com/openclaw/openclaw/pull/93829) | 0 | Model routing/config | @sunlit-deng | fix: /status usage follows session /model override instead of stale runtime provider |
| 🔀&nbsp;[#93821](https://github.com/openclaw/openclaw/pull/93821) | 0 | Local memory/embedding | @liuhao1024 | fix(qmd): strip mcporter daemon startup logs from stdout before JSON.parse (fixes #59808) |
| 🔀&nbsp;[#93820](https://github.com/openclaw/openclaw/pull/93820) | 0 | Open-weight/provider behavior | @Alix-007 | fix(imessage): recognize MiniMax mm: reasoning tags in reflection guard (completes #93767) |
| 🔀&nbsp;[#93806](https://github.com/openclaw/openclaw/pull/93806) | 0 | Open-weight/provider behavior | @Alix-007 | fix(reasoning-tags): strip MiniMax mm: tags on silent-reply and streaming paths missed by #93767 |
| 📝&nbsp;[#93801](https://github.com/openclaw/openclaw/issues/93801) | 0 | Model routing/config | @anguslogan01 | [Feature]: Per-task model-router hook in agent dispatch (external policy command, fail-open) |
| 🔀&nbsp;[#93791](https://github.com/openclaw/openclaw/pull/93791) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): await search-sync before returning results to prevent stale index (fixes #52115) |
| 🔀&nbsp;[#93789](https://github.com/openclaw/openclaw/pull/93789) | 0 | Model routing/config | @joelnishanth | fix(agents): make lane suspension consistent across cooldown-precheck and embedded-runner paths |
| 🔀&nbsp;[#93786](https://github.com/openclaw/openclaw/pull/93786) | 0 | Model routing/config | @liuhao1024 | fix(plugins): treat refreshable catalogs as requiring runtime discovery (fixes #93775) |
| 🔀&nbsp;[#93785](https://github.com/openclaw/openclaw/pull/93785) | 0 | Open-weight/provider behavior | @manus-use | fix(reasoning-tags): strip MiniMax `mm:` namespaced reasoning tags |
| 🔀&nbsp;[#93783](https://github.com/openclaw/openclaw/pull/93783) | 0 | Local memory/embedding | @liuhao1024 | fix(qmd): strip mcporter daemon startup logs from stdout before JSON.parse (fixes #59808) |
| 📝&nbsp;[#93781](https://github.com/openclaw/openclaw/issues/93781) | 0 | OpenAI-compatible/proxy | @BSG2000 | azure-openai-responses probe/agent route uses OpenAI auth profile instead of Azure credentials |
| 📝&nbsp;[#93775](https://github.com/openclaw/openclaw/issues/93775) | 0 | Model routing/config | @St0rmz1 | [Bug]: Refreshable provider catalogs can skip runtime discovery |
| 🔀&nbsp;[#93774](https://github.com/openclaw/openclaw/pull/93774) | 0 | Model routing/config | @TurboTheTurtle | fix(codex): provision app-server model catalog metadata |
| 🔀&nbsp;[#93768](https://github.com/openclaw/openclaw/pull/93768) | 0 | OpenAI-compatible/proxy | @yu-xin-c | [codex] Forward opt-in run context headers |
| 🔀&nbsp;[#93767](https://github.com/openclaw/openclaw/pull/93767) | 0 | Model/provider behavior | @DrHack1 | fix(reasoning-tags): strip MiniMax `mm:` namespaced reasoning tags |
| 🔀&nbsp;[#93766](https://github.com/openclaw/openclaw/pull/93766) | 0 | OpenAI-compatible/proxy | @sha367 | feat: add MegaBrain provider |
| 📝&nbsp;[#93765](https://github.com/openclaw/openclaw/issues/93765) | 0 | OpenAI-compatible/proxy | @hannesrudolph | Codex isolated app-server homes do not receive configured custom-model catalog metadata |
| 📝&nbsp;[#93764](https://github.com/openclaw/openclaw/issues/93764) | 0 | Model routing/config | @Fuma2013 | Codex OAuth gpt-5.5: config reports 1M/950k but native runtime caps turns at 258400 |
| 🔀&nbsp;[#93759](https://github.com/openclaw/openclaw/pull/93759) | 0 | Local/media model provider | @harjothkhara | fix(minimax): surface TTS envelope errors so fallback fires (#76904) [AI] |
| 🔀&nbsp;[#93758](https://github.com/openclaw/openclaw/pull/93758) | 0 | Local memory/embedding | @liuhao1024 | feat(memory): apply outputDimensionality truncation to local GGUF embeddings (fixes #58765) |
| 📝&nbsp;[#93757](https://github.com/openclaw/openclaw/issues/93757) | 0 | Model routing/config | @ffluk3 | v2026.5.28: Bedrock thinking-signature errors surface as unclassified/no-failover (fixed on main) |
| 🔀&nbsp;[#93756](https://github.com/openclaw/openclaw/pull/93756) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): increase narrative timeout from 60s to 120s for ARM cold-load (fixes #92494) |
| 🔀&nbsp;[#93747](https://github.com/openclaw/openclaw/pull/93747) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): await search-sync before returning results to prevent stale index (fixes #52115) |
| 🔀&nbsp;[#93746](https://github.com/openclaw/openclaw/pull/93746) | 0 | Model routing/config | @shushushv | fix(ui): populate realtime talk provider and transport options from talk.catalog |
| 📝&nbsp;[#93741](https://github.com/openclaw/openclaw/issues/93741) | 0 | Model routing/config | @clemenshelm | Allow the `agent` RPC to offload images to `imageModel` for text-only models (opt-in) |
| 🔀&nbsp;[#93730](https://github.com/openclaw/openclaw/pull/93730) | 0 | Model routing/config | @joelnishanth | fix: preserve fallback chain when primary model hits rate-limit lane suspension |
| 🔀&nbsp;[#93729](https://github.com/openclaw/openclaw/pull/93729) | 0 | Local model runtime | @zhangguiping-xydt | Preserve configured Ollama API during discovery |
| 🔀&nbsp;[#93723](https://github.com/openclaw/openclaw/pull/93723) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): increase narrative timeout from 60s to 120s for ARM cold-load (fixes #92494) |
| 🔀&nbsp;[#93721](https://github.com/openclaw/openclaw/pull/93721) | 0 | Local memory/embedding | @yu-xin-c | fix(agents): notify no-op compaction hooks |
| 📝&nbsp;[#93710](https://github.com/openclaw/openclaw/issues/93710) | 0 | Local model runtime | @obnoxious2011-cmd | ollama plugin overrides api to native protocol ignoring config api setting |
| 🔀&nbsp;[#93708](https://github.com/openclaw/openclaw/pull/93708) | 0 | OpenAI-compatible/proxy | @zhangguiping-xydt | [Bug]: opencode-go provider streaming — API calls complete on provider side but gateway never receives stream termination signal |
| 🔀&nbsp;[#93688](https://github.com/openclaw/openclaw/pull/93688) | 0 | Local/media model provider | @dwc1997 | fix(minimax): check base_resp envelope errors in TTS provider |
| 🔀&nbsp;[#93683](https://github.com/openclaw/openclaw/pull/93683) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): await search-sync before returning results to prevent stale index (fixes #52115) |
| 🔀&nbsp;[#93681](https://github.com/openclaw/openclaw/pull/93681) | 0 | OpenAI-compatible/proxy | @Alix-007 | fix(llm): handle string assistant content on the OpenAI-compatible completion path |
| 🔀&nbsp;[#93676](https://github.com/openclaw/openclaw/pull/93676) | 0 | Model routing/config | @Pick-cat | fix(agent-runner): retry same model on Gemini per-minute rate-limit 429s |
| 🔀&nbsp;[#93669](https://github.com/openclaw/openclaw/pull/93669) | 0 | Open-weight/provider behavior | @lzyyzznl | fix(agents): classify Zhipu GLM error 1305 / 访问量过大 as overloaded for model fallback |
| 🔀&nbsp;[#93660](https://github.com/openclaw/openclaw/pull/93660) | 0 | OpenAI-compatible/proxy | @lzyyzznl | feat(gateway): 添加 streaming 输出配置块到 HTTP 端点 |
| 🔀&nbsp;[#93658](https://github.com/openclaw/openclaw/pull/93658) | 0 | Model routing/config | @ml12580 | fix(wizard): preserve existing default model during setup auth choice [AI-assisted] |
| 🔀&nbsp;[#93655](https://github.com/openclaw/openclaw/pull/93655) | 0 | OpenAI-compatible/proxy | @mushuiyu886 | fix(agent): classify stuck recovery as idle timeout |
| 🔀&nbsp;[#93651](https://github.com/openclaw/openclaw/pull/93651) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): increase narrative timeout from 60s to 120s for ARM cold-load (fixes #92494) |
| 🔀&nbsp;[#93640](https://github.com/openclaw/openclaw/pull/93640) | 0 | OpenAI-compatible/proxy | @blindjoy23 | fix: add stream stall guard for lost stream termination signal (opencode-go) |
| 🔀&nbsp;[#93627](https://github.com/openclaw/openclaw/pull/93627) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): filter already-emitted entries in light phase to prevent verbatim repeats (fixes #72096)<br>Assignee: vincentkoc |
| 🔀&nbsp;[#93624](https://github.com/openclaw/openclaw/pull/93624) | 0 | OpenAI-compatible/proxy | @Jah-xy | feat(gateway): add configurable streaming chunk size for HTTP endpoints |
| 🔀&nbsp;[#93623](https://github.com/openclaw/openclaw/pull/93623) | 0 | Model routing/config | @sunlit-deng | fix(chat): prefer server session row over stale cache in model dropdown |
| 🔀&nbsp;[#93620](https://github.com/openclaw/openclaw/pull/93620) | 0 | OpenAI-compatible/proxy | @xydt-tanshanshan | [AI] fix(openai-completions): preserve reasoning_content on assistant messages for OpenRouter providers |
| 🔀&nbsp;[#93613](https://github.com/openclaw/openclaw/pull/93613) | 0 | OpenAI-compatible/proxy | @Jah-xy | feat(llm): forward run context to model as opt-in request headers<br>Assignee: vincentkoc |
| 🔀&nbsp;[#93611](https://github.com/openclaw/openclaw/pull/93611) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): filter already-emitted entries in light phase to prevent verbatim repeats (fixes #72096) |
| 📝&nbsp;[#93610](https://github.com/openclaw/openclaw/issues/93610) | 0 | Model/provider behavior | @ForceConstant | [Bug]: opencode-go provider streaming — API calls complete on provider side but gateway never receives stream termination signal |
| 🔀&nbsp;[#93608](https://github.com/openclaw/openclaw/pull/93608) | 0 | Open-weight/provider behavior | @tomsun28 | chore: update glm-5.2 model cost pricing for input, output, and cache |
| 🔀&nbsp;[#93602](https://github.com/openclaw/openclaw/pull/93602) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): align session file counter denominator with indexer filter |
| 📝&nbsp;[#93598](https://github.com/openclaw/openclaw/issues/93598) | 0 | OpenAI-compatible/proxy | @ikaijian | [Feature]: Can the streaming output increase the size of the configuration control block? |
| 🔀&nbsp;[#93596](https://github.com/openclaw/openclaw/pull/93596) | 0 | Local memory/embedding | @Alix-007 | fix(plugins): activate dreaming engine sidecar under restrictive allowlist |
| 🔀&nbsp;[#93586](https://github.com/openclaw/openclaw/pull/93586) | 0 | Local memory/embedding | @liuhao1024 | fix(qmd): strip XDG env vars from mcporter spawn env to fix mcporter ≥ 0.10 config resolution (fixes #79847) |
| 🔀&nbsp;[#93533](https://github.com/openclaw/openclaw/pull/93533) | 0 | Local memory/embedding | @bowenluo718 | fix: support baseURL config for remote embedding providers |
| 🔀&nbsp;[#93523](https://github.com/openclaw/openclaw/pull/93523) | 0 | Model routing/config | @lzyyzznl | feat(ui): add model selector to cron quick-create wizard and job list |
| 🔀&nbsp;[#93508](https://github.com/openclaw/openclaw/pull/93508) | 0 | Local memory/embedding | @lzyyzznl | fix(session-memory): deduplicate assistant messages when thinking is stripped |
| 📝&nbsp;[#93507](https://github.com/openclaw/openclaw/issues/93507) | 0 | Model routing/config | @psdjc | [Feature]: Allow selecting cron job models and clearly displaying them in the Web UI |
| 🔀&nbsp;[#93505](https://github.com/openclaw/openclaw/pull/93505) | 0 | Local memory/embedding | @sunlit-deng | fix: support baseURL alias in memory embedding provider config resolution |
| 🔀&nbsp;[#93503](https://github.com/openclaw/openclaw/pull/93503) | 0 | Model routing/config | @lzyyzznl | fix(cli): resolve 200K context window fallback in status command |
| 📝&nbsp;[#93485](https://github.com/openclaw/openclaw/issues/93485) | 0 | Local memory/embedding | @A1fred-AI | memory-wiki: Stale Pages report flags intentionally durable references (concepts, syntheses) as aging |
| 🔀&nbsp;[#93473](https://github.com/openclaw/openclaw/pull/93473) | 0 | Local memory/embedding | @TurboTheTurtle | [codex] Fix QMD lexical memory status |
| 🔀&nbsp;[#93469](https://github.com/openclaw/openclaw/pull/93469) | 0 | OpenAI-compatible/proxy | @drvoss | fix(agents): drop partialJson streaming artifacts from session history repair |
| 🔀&nbsp;[#93452](https://github.com/openclaw/openclaw/pull/93452) | 0 | Local memory/embedding | @LiuwqGit | fix(bedrock): strip inference profile prefix from model ID in embedding adapter |
| 🔀&nbsp;[#93451](https://github.com/openclaw/openclaw/pull/93451) | 0 | OpenAI-compatible/proxy | @lzyyzznl | #93436: Forward run context to the model as opt-in request headers |
| 🔀&nbsp;[#93443](https://github.com/openclaw/openclaw/pull/93443) | 0 | OpenAI-compatible/proxy | @openclaw-clownfish[bot] | fix(gateway): block internal HTTP session overrides |
| 🔀&nbsp;[#93439](https://github.com/openclaw/openclaw/pull/93439) | 0 | Model routing/config | @harjothkhara | fix(agents): honor embedded run default model |
| 📝&nbsp;[#93436](https://github.com/openclaw/openclaw/issues/93436) | 0 | OpenAI-compatible/proxy | @asupian | [Feature]: Forward run context to the model as opt-in request headers (cost attribution behind a proxy) |
| 🔀&nbsp;[#93430](https://github.com/openclaw/openclaw/pull/93430) | 0 | Model routing/config | @kingrubic | fix: honor configured default model for embedded agents |
| 🔀&nbsp;[#93428](https://github.com/openclaw/openclaw/pull/93428) | 0 | Model routing/config | @zenglingbiao | fix(agents): resolve configured default model in runEmbeddedAgent (fixes #93419)<br>Assignee: vincentkoc |
| 📝&nbsp;[#93426](https://github.com/openclaw/openclaw/issues/93426) | 0 | Local memory/embedding | @tcconnally | Feature request: Mimir as persistent memory backend |
| 📝&nbsp;[#93419](https://github.com/openclaw/openclaw/issues/93419) | 0 | Model routing/config | @danielgerlag | [Bug]: runEmbeddedAgent ignores agents.defaults.model and hardcodes openai/gpt-5.5 |
| 🔀&nbsp;[#93397](https://github.com/openclaw/openclaw/pull/93397) | 0 | Local/media model provider | @Quratulain-bilal | fix(minimax): correct volume range warning to match inclusive max |
| 📝&nbsp;[#93396](https://github.com/openclaw/openclaw/issues/93396) | 0 | Local model runtime | @pineapple82 | [Bug]:  Provider name "openai" misleading when using local Ollama – causes fallback to real OpenAI API for embeddings |
| 🔀&nbsp;[#93394](https://github.com/openclaw/openclaw/pull/93394) | 0 | Local memory/embedding | @Alix-007 | fix(memory): abort orphaned qmd search subprocess when memory_search times out |
| 📝&nbsp;[#93393](https://github.com/openclaw/openclaw/issues/93393) | 0 | Local model runtime | @turururu | [Feature]: Model-agnostic advisor tool via api.runtime.llm.complete |
| 🔀&nbsp;[#93389](https://github.com/openclaw/openclaw/pull/93389) | 0 | Local memory/embedding | @Alix-007 | fix(memory-core): clear daily-ingestion sqlite namespace on dreaming repair |
| 🔀&nbsp;[#93388](https://github.com/openclaw/openclaw/pull/93388) | 0 | Model/provider behavior | @vortexopenclaw | fix(google): use stable Gemini image model |
| 🔀&nbsp;[#93384](https://github.com/openclaw/openclaw/pull/93384) | 0 | Model routing/config | @zhangguiping-xydt | [Bug]: /status usage should follow session-selected model after /model switch |
| 🔀&nbsp;[#93377](https://github.com/openclaw/openclaw/pull/93377) | 0 | Model routing/config | @pandaAIGC | fix(model-fallback): classify Codex/OpenAI auth failures |
| 🔀&nbsp;[#93371](https://github.com/openclaw/openclaw/pull/93371) | 0 | Local memory/embedding | @mushuiyu886 | fix(memory): keep recalled memory out of user prompts |
| 🔀&nbsp;[#93369](https://github.com/openclaw/openclaw/pull/93369) | 0 | Model routing/config | @849261680 | fix(cron): expose per-job fallbacks in CLI |
| 🔀&nbsp;[#93365](https://github.com/openclaw/openclaw/pull/93365) | 0 | Local memory/embedding | @xydigit-sj | fix(memory-core): EPERM fallback for atomic reindex on Windows (#78640) |
| 🔀&nbsp;[#93356](https://github.com/openclaw/openclaw/pull/93356) | 0 | Model routing/config | @obuchowski | fix(plugins): cache plugin setup registry to kill the /models CPU storm |
| 🔀&nbsp;[#93352](https://github.com/openclaw/openclaw/pull/93352) | 0 | Model routing/config | @jailbirt | fix(auth-profiles): import legacy auth-profiles.json into SQLite store on load |
| 🔀&nbsp;[#93350](https://github.com/openclaw/openclaw/pull/93350) | 0 | Model routing/config | @mmyzwl | #93346: fix(ui): show effective runtime model in dropdown after fallback |
| 🔀&nbsp;[#93348](https://github.com/openclaw/openclaw/pull/93348) | 0 | Model routing/config | @MonkeyLeeT | fix(status): use selected model for usage |
| 📝&nbsp;[#93346](https://github.com/openclaw/openclaw/issues/93346) | 0 | Model routing/config | @davidstoll | [Bug]: Model dropdown does not reflect effective runtime model after fallback/default drift |
| 🔀&nbsp;[#93342](https://github.com/openclaw/openclaw/pull/93342) | 0 | Model/provider behavior | @Marvinthebored | pipeline: normalized provider→channel stream grammar (core) |
| 🔀&nbsp;[#93335](https://github.com/openclaw/openclaw/pull/93335) | 0 | Model routing/config | @obuchowski | fix(thinking): clamp below-range requests down to the cheapest level,… |
| 🔀&nbsp;[#93331](https://github.com/openclaw/openclaw/pull/93331) | 0 | Model routing/config | @ferminquant | feat(compaction): add embedded fallback models |
| 📝&nbsp;[#93322](https://github.com/openclaw/openclaw/issues/93322) | 0 | Model routing/config | @rollingshmily | [Bug]: /status usage should follow session-selected model after /model switch |
| 📝&nbsp;[#93312](https://github.com/openclaw/openclaw/issues/93312) | 0 | Local memory/embedding | @doubleji817-lang | [Bug]: memory] openai-compatible embedding batch hangs on "batch start" - never produces "batch completed" |
| 🔀&nbsp;[#93306](https://github.com/openclaw/openclaw/pull/93306) | 0 | Model routing/config | @hxy91819 | fix(status): ignore stale context after model switch |
| 🔀&nbsp;[#93295](https://github.com/openclaw/openclaw/pull/93295) | 0 | Local memory/embedding | @Alix-007 | fix(memory): swap rollback-journal sidecar during atomic reindex |
| 🔀&nbsp;[#93276](https://github.com/openclaw/openclaw/pull/93276) | 0 | Model routing/config | @medns | fix(plugins): stop tool-discovery loads from clearing active providers |
| 🔀&nbsp;[#93275](https://github.com/openclaw/openclaw/pull/93275) | 0 | Model routing/config | @zhiqiang26 | #92776: fix(agents): prevent indefinite session model pinning from polluted fallback origin |
| 📝&nbsp;[#93272](https://github.com/openclaw/openclaw/issues/93272) | 0 | Model routing/config | @pandaAIGC | Model fallback does not trigger for Codex/OpenAI auth and zero-output assistant failures |
| 🔀&nbsp;[#93268](https://github.com/openclaw/openclaw/pull/93268) | 0 | Local memory/embedding | @lzyyzznl | fix(status): resolve "Vector store: unknown" on memory status fast path |
| 🔀&nbsp;[#93267](https://github.com/openclaw/openclaw/pull/93267) | 0 | Local memory/embedding | @fsdwen | fix(session-memory): skip delivery-mirror entries and dedup consecutive identical assistant messages (#92563) |
| 🔀&nbsp;[#93261](https://github.com/openclaw/openclaw/pull/93261) | 0 | Model routing/config | @BitmapAsset | fix(plugins): resolve provider policy surface for plugin-owned CLI backends |
| 🔀&nbsp;[#93260](https://github.com/openclaw/openclaw/pull/93260) | 0 | Local memory/embedding | @mushuiyu886 | fix(memory): fall back to keyword search without sqlite |
| 📝&nbsp;[#93259](https://github.com/openclaw/openclaw/issues/93259) | 0 | Model routing/config | @BitmapAsset | claude-cli subagents silently cap thinking at "high" — provider-policy surface not resolved for plugin CLI backends |
| 🔀&nbsp;[#93253](https://github.com/openclaw/openclaw/pull/93253) | 0 | OpenAI-compatible/proxy | @XuZehan-iCenter | fix(openai-completions): preserve reasoning replay for MiniMax M3 via OpenRouter |
| 🔀&nbsp;[#93241](https://github.com/openclaw/openclaw/pull/93241) | 0 | Model routing/config | @0xghost42 | fix(agents): classify Zhipu GLM overload as overloaded for failover |
| 🔀&nbsp;[#93238](https://github.com/openclaw/openclaw/pull/93238) | 0 | Local model runtime | @osolmaz | fix(agents): honor disabled envelope timestamps at model boundary |
| 🔀&nbsp;[#93235](https://github.com/openclaw/openclaw/pull/93235) | 0 | Local memory/embedding | @liuhao1024 | fix(qmd): strip XDG env vars from mcporter spawn env to fix mcporter ≥ 0.10 config resolution (fixes #79847) |
| 🔀&nbsp;[#93231](https://github.com/openclaw/openclaw/pull/93231) | 0 | Model routing/config | @hxy91819 | fix(status): correct pinned model clear hint<br>Assignee: steipete |
| 🔀&nbsp;[#93226](https://github.com/openclaw/openclaw/pull/93226) | 0 | Model routing/config | @mmyzwl | fix(auth-health): prefer usable OAuth over expired inventory in provider status |
| 🔀&nbsp;[#93220](https://github.com/openclaw/openclaw/pull/93220) | 0 | Model routing/config | @hxy91819 | fix(status): avoid stale session context windows |
| 🔀&nbsp;[#93215](https://github.com/openclaw/openclaw/pull/93215) | 0 | Local memory/embedding | @xydt-tanshanshan | fix(memory): derive agentId from sessionKey fallback in resolveMemoryToolOptions |
| 🔀&nbsp;[#93212](https://github.com/openclaw/openclaw/pull/93212) | 0 | Model routing/config | @mmyzwl | fix(failover): classify Zhipu (GLM) error [1305] as overloaded |
| 📝&nbsp;[#93211](https://github.com/openclaw/openclaw/issues/93211) | 0 | Model routing/config | @zhengli0922 | Model fallback not triggered for Zhipu (GLM) error code 1305 — overloaded pattern mismatch |
| 🔀&nbsp;[#93206](https://github.com/openclaw/openclaw/pull/93206) | 0 | Open-weight/provider behavior | @extrasmall0 | fix(minimax): wrap simple completion requests |
| 📝&nbsp;[#93199](https://github.com/openclaw/openclaw/issues/93199) | 0 | Local memory/embedding | @chaboncarpentier-blip | memory_search fails in non-default agent session while CLI --agent search works; current session resolves inconsistently |
| 🔀&nbsp;[#93198](https://github.com/openclaw/openclaw/pull/93198) | 0 | Model routing/config | @mushuiyu886 | fix #80933: honor claude-cli contextTokens |
| 🔀&nbsp;[#93196](https://github.com/openclaw/openclaw/pull/93196) | 0 | Model routing/config | @mmyzwl | fix(auth): inherit config auth.profiles when default agent store is empty |
| 🔀&nbsp;[#93192](https://github.com/openclaw/openclaw/pull/93192) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): filter already-emitted entries in light phase to prevent verbatim repeats (fixes #72096) |
| 🔀&nbsp;[#93187](https://github.com/openclaw/openclaw/pull/93187) | 0 | Local memory/embedding | @xialonglee | fix(memory-core): exclude archive transcripts from dreaming corpus and propagate cron parentage to subagents |
| 🔀&nbsp;[#93183](https://github.com/openclaw/openclaw/pull/93183) | 0 | Model routing/config | @TurboTheTurtle | [codex] Fix /btw Codex runtime side-question routing |
| 🔀&nbsp;[#93182](https://github.com/openclaw/openclaw/pull/93182) | 0 | Local memory/embedding | @Alix-007 | fix(memory): clean rollback-journal reindex temp sidecar on NFS stores |
| 🔀&nbsp;[#93180](https://github.com/openclaw/openclaw/pull/93180) | 0 | Model routing/config | @ooiuuii | fix(doctor): gate legacy Codex canonicalization on a migration plan |
| 🔀&nbsp;[#93170](https://github.com/openclaw/openclaw/pull/93170) | 0 | Local memory/embedding | @liuhao1024 | fix(qmd): strip XDG env vars from mcporter spawn env to fix mcporter ≥ 0.10 config resolution (fixes #79847) |
| 🔀&nbsp;[#93168](https://github.com/openclaw/openclaw/pull/93168) | 0 | Local memory/embedding | @xialonglee | fix(active-memory): exclude dreaming-narrative session keys from interactive eligibility gate |
| 🔀&nbsp;[#93156](https://github.com/openclaw/openclaw/pull/93156) | 0 | Model routing/config | @Pick-cat | fix(doctor): import default-agent auth profiles into sqlite |
| 📝&nbsp;[#93154](https://github.com/openclaw/openclaw/issues/93154) | 0 | Local memory/embedding | @1818TusculumSt | memory_search tool reports 'index provider settings changed' with OAuth-based OpenAI profile |
| 📝&nbsp;[#93150](https://github.com/openclaw/openclaw/issues/93150) | 0 | Local memory/embedding | @rrrrrredy | [Feature]: Add keyword fallback for memory_search when node:sqlite is unavailable |
| 📝&nbsp;[#93145](https://github.com/openclaw/openclaw/issues/93145) | 0 | Model routing/config | @Tazio7 | Agent auth migration to SQLite leaves default agent with empty auth store (v2026.6.6) |
| 🔀&nbsp;[#93136](https://github.com/openclaw/openclaw/pull/93136) | 0 | OpenAI-compatible/proxy | @patelmm79 | feat(attribution): parameterize OpenRouter `X-OpenRouter-Title` per deployment |
| 🔀&nbsp;[#93125](https://github.com/openclaw/openclaw/pull/93125) | 0 | Model routing/config | @ferminquant | feat(compaction): add compaction.fallbacks: string[] for ordered model fallback chain |
| 🔀&nbsp;[#93122](https://github.com/openclaw/openclaw/pull/93122) | 0 | Model routing/config | @zhangqueping | #93120: feat(auth): make maxSameModelRateLimitRetries configurable |
| 📝&nbsp;[#93120](https://github.com/openclaw/openclaw/issues/93120) | 0 | Model routing/config | @shichuzhu | [Feature]: Expose MAX_SAME_MODEL_RATE_LIMIT_RETRIES as configurable (currently hardcoded to 3) |
| 🔀&nbsp;[#93116](https://github.com/openclaw/openclaw/pull/93116) | 0 | OpenAI-compatible/proxy | @xydt-tanshanshan | fix(xai): respect ssrfPolicy and request.allowPrivateNetwork in image_generate |
| 🔀&nbsp;[#93113](https://github.com/openclaw/openclaw/pull/93113) | 0 | Local memory/embedding | @AgentArcLab | fix(memory-core): report active dreaming phases in status |
| 🔀&nbsp;[#93106](https://github.com/openclaw/openclaw/pull/93106) | 0 | Local model runtime | @ZengWen-DT | docs(gateway): add cloud-orchestrator plus local-text-workers pattern |
| 🔀&nbsp;[#93100](https://github.com/openclaw/openclaw/pull/93100) | 0 | Local memory/embedding | @yetval | fix(compaction): emit after_compaction on no-op and use JSON-safe validator delimiters (#81925) |
| 🔀&nbsp;[#93097](https://github.com/openclaw/openclaw/pull/93097) | 0 | Local memory/embedding | @liuhao1024 | fix(qmd): strip XDG env vars from mcporter spawn env to fix mcporter ≥ 0.10 integration (fixes #79847) |
| 🔀&nbsp;[#93093](https://github.com/openclaw/openclaw/pull/93093) | 0 | Local memory/embedding | @ZengWen-DT | docs(memory): warn about session memory overlap |
| 🔀&nbsp;[#93064](https://github.com/openclaw/openclaw/pull/93064) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): align session file counter denominator with indexer filter (fixes #77338) |
| 🔀&nbsp;[#93056](https://github.com/openclaw/openclaw/pull/93056) | 0 | Model routing/config | @samson910022 | fix(agents): sync stale this.model snapshot after /model switch |
| 📝&nbsp;[#93050](https://github.com/openclaw/openclaw/issues/93050) | 0 | Model routing/config | @ferminquant | [Feature]: Add compaction.fallbacks: string[] for ordered model fallback chain on summarization failure |
| 🔀&nbsp;[#93039](https://github.com/openclaw/openclaw/pull/93039) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): increase narrative timeout from 60s to 120s for ARM cold-load (fixes #92494) |
| 📝&nbsp;[#93036](https://github.com/openclaw/openclaw/issues/93036) | 0 | Model routing/config | @kumaxs | suspendSession locks entire lane, prevents fallback models from running on rate-limit |
| 🔀&nbsp;[#93017](https://github.com/openclaw/openclaw/pull/93017) | 0 | Model/provider behavior | @dwc1997 | fix(agents): null-guard baseUrl in getAttributionHeaders |
| 🔀&nbsp;[#93013](https://github.com/openclaw/openclaw/pull/93013) | 0 | Model/provider behavior | @425072024 | fix(agents): null-guard baseUrl in getAttributionHeaders |
| 🔀&nbsp;[#93011](https://github.com/openclaw/openclaw/pull/93011) | 0 | OpenAI-compatible/proxy | @yetval | fix(gateway): accept file-only input on /v1/responses (parity with image-only) |
| 🔀&nbsp;[#93008](https://github.com/openclaw/openclaw/pull/93008) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): filter already-emitted entries in light phase to prevent verbatim repeats (fixes #72096) |
| 🔀&nbsp;[#93007](https://github.com/openclaw/openclaw/pull/93007) | 0 | OpenAI-compatible/proxy | @Lellansin | feat(gateway): forward web_search_options through OpenAI-compatible chat completions |
| 🔀&nbsp;[#93005](https://github.com/openclaw/openclaw/pull/93005) | 0 | OpenAI-compatible/proxy | @sallyom | [codex] Add OpenRouter Fusion guidance and prompt context |
| 🔀&nbsp;[#93003](https://github.com/openclaw/openclaw/pull/93003) | 0 | Model/provider behavior | @whiteyzy | fix(sdk): null-guard model.baseUrl in getAttributionHeaders |
| 🔀&nbsp;[#92993](https://github.com/openclaw/openclaw/pull/92993) | 0 | OpenAI-compatible/proxy | @luoluo-xue-ops | [codex] openai proxy compat for compatible providers |
| 🔀&nbsp;[#92991](https://github.com/openclaw/openclaw/pull/92991) | 0 | Model/provider behavior | @samrusani | fix(agents): tolerate missing attribution baseUrl |
| 🔀&nbsp;[#92988](https://github.com/openclaw/openclaw/pull/92988) | 0 | Local memory/embedding | @chengzhichao-xydt | fix(memory-core): cleanup orphaned *.sqlite.tmp-* reindex files on startup |
| 📝&nbsp;[#92984](https://github.com/openclaw/openclaw/issues/92984) | 0 | OpenAI-compatible/proxy | @sallyom | Docs: add OpenRouter Fusion model guidance<br>Assignee: sallyom |
| 🔀&nbsp;[#92979](https://github.com/openclaw/openclaw/pull/92979) | 0 | Local memory/embedding | @liuhao1024 | fix(memory): show per-phase dreaming status when only light phase is enabled (fixes #67868) |
| 🔀&nbsp;[#92977](https://github.com/openclaw/openclaw/pull/92977) | 0 | Model/provider behavior | @zhiqiang26 | #92974: Bug: v2026.6.6 getAttributionHeaders() crashes on Bedrock models — baseUrl undefined (null-guard missing) |
| 📝&nbsp;[#92974](https://github.com/openclaw/openclaw/issues/92974) | 0 | Model/provider behavior | @Haderach-Ram | Bug: v2026.6.6 getAttributionHeaders() crashes on Bedrock models — baseUrl undefined (null-guard missing) |
| 🔀&nbsp;[#92972](https://github.com/openclaw/openclaw/pull/92972) | 0 | Local memory/embedding | @pony-maggie | fix(memory): sweep orphaned reindex temp files |
| 🔀&nbsp;[#92968](https://github.com/openclaw/openclaw/pull/92968) | 0 | Model routing/config | @samson910022 | fix(status): warm context-window cache at gateway startup for correct /status on first call |
| 📝&nbsp;[#92967](https://github.com/openclaw/openclaw/issues/92967) | 0 | Model routing/config | @samson910022 | fix(status): warm context-window cache at gateway startup for correct /status on first call |
| 🔀&nbsp;[#92966](https://github.com/openclaw/openclaw/pull/92966) | 0 | Local memory/embedding | @hnlqt666 | fix(session-memory): deduplicate consecutive assistant messages with identical text |
| 🔀&nbsp;[#92959](https://github.com/openclaw/openclaw/pull/92959) | 0 | Model routing/config | @zenglingbiao | fix(model-fallback): coalesce repeated auth-class fallback decision logs to prevent auth expiry spam (fixes #56979) |
| 🔀&nbsp;[#92955](https://github.com/openclaw/openclaw/pull/92955) | 0 | Model routing/config | @NianJiuZst | fix(opencode-go): load context windows from bundled catalog |
| 🔀&nbsp;[#92954](https://github.com/openclaw/openclaw/pull/92954) | 0 | Local memory/embedding | @mushuiyu886 | fix(memory): accept local default model path migration |
| 🔀&nbsp;[#92952](https://github.com/openclaw/openclaw/pull/92952) | 0 | Local memory/embedding | @Alix-007 | fix(memory-core): sweep orphaned sqlite reindex temp files on startup (#92874) |
| 🔀&nbsp;[#92943](https://github.com/openclaw/openclaw/pull/92943) | 0 | Local memory/embedding | @mushuiyu886 | Refresh memory index state after external reindex |
| 🔀&nbsp;[#92940](https://github.com/openclaw/openclaw/pull/92940) | 0 | Model routing/config | @liuhao1024 | fix(model-fallback): throttle duplicate decision logs to prevent auth expiry spam (fixes #56979) |
| 🔀&nbsp;[#92938](https://github.com/openclaw/openclaw/pull/92938) | 0 | Model routing/config | @zhangguiping-xydt | gateway hangs at `[gateway] starting...` when a declared provider lacks credentials (regression v2026.4.8 → v2026.4.26) |
| 🔀&nbsp;[#92932](https://github.com/openclaw/openclaw/pull/92932) | 0 | Model routing/config | @zhiqiang26 | #92931: Bug: catalog.json caches API key in plaintext after auth migration to encrypted SQLite |
| 🔀&nbsp;[#92930](https://github.com/openclaw/openclaw/pull/92930) | 0 | Model routing/config | @samson910022 | fix(status): warm model context-window cache before /status reads it |
| 🔀&nbsp;[#92914](https://github.com/openclaw/openclaw/pull/92914) | 0 | Model routing/config | @openperf | fix(agents): clamp unsupported thinking for subagent spawns instead of hard-failing |
| 🔀&nbsp;[#92913](https://github.com/openclaw/openclaw/pull/92913) | 0 | Model routing/config | @kumaxs | fix(opencode-go): register model catalog to fix context window detection |
| 📝&nbsp;[#92912](https://github.com/openclaw/openclaw/issues/92912) | 0 | Model routing/config | @kumaxs | opencode-go plugin: model contextWindow not loaded, all models fall back to 200K |
| 🔀&nbsp;[#92910](https://github.com/openclaw/openclaw/pull/92910) | 0 | Local memory/embedding | @openclaw-clownfish[bot] | fix(memory-core): safely refresh qmd index during collection repair |
| 🔀&nbsp;[#92908](https://github.com/openclaw/openclaw/pull/92908) | 0 | OpenAI-compatible/proxy | @steipete | fix(providers): quarantine unreadable Anthropic payload tools |
| 🔀&nbsp;[#92905](https://github.com/openclaw/openclaw/pull/92905) | 0 | Model routing/config | @samson910022 | fix(status): warm model context-window cache before /status reads it |
| 🔀&nbsp;[#92904](https://github.com/openclaw/openclaw/pull/92904) | 0 | Model/provider behavior | @vortexopenclaw | fix(elevenlabs): use current TTS model ids |
| 🔀&nbsp;[#92900](https://github.com/openclaw/openclaw/pull/92900) | 0 | Model routing/config | @YonganZhang | fix(ui): refresh overview model auth status on demand |
| 🔀&nbsp;[#92897](https://github.com/openclaw/openclaw/pull/92897) | 0 | Local memory/embedding | @yu-xin-c | fix(memory-wiki): tolerate public artifacts without agent ids |
| 🔀&nbsp;[#92892](https://github.com/openclaw/openclaw/pull/92892) | 0 | Model routing/config | @YonganZhang | fix(gateway): allow Gemini CLI image-capable models |
| 🔀&nbsp;[#92891](https://github.com/openclaw/openclaw/pull/92891) | 0 | Local memory/embedding | @ZengWen-DT | fix(memory): clean stale reindex temp files |
| 🔀&nbsp;[#92890](https://github.com/openclaw/openclaw/pull/92890) | 0 | Local model runtime | @YonganZhang | fix(lmstudio): honor binary reasoning maps in completions |
| 📝&nbsp;[#92888](https://github.com/openclaw/openclaw/issues/92888) | 0 | Model routing/config | @buyuangtampan | Control UI model auth badge still shows expired on 2026.6.6 while runtime auth is usable |
| 🔀&nbsp;[#92887](https://github.com/openclaw/openclaw/pull/92887) | 0 | Local memory/embedding | @YonganZhang | fix(memory): sweep stale reindex temp sqlite files |
| 🔀&nbsp;[#92885](https://github.com/openclaw/openclaw/pull/92885) | 0 | Local memory/embedding | @Pandah97 | #92207 fix(memory-wiki): guard against missing agentIds in public artifacts |
| 🔀&nbsp;[#92881](https://github.com/openclaw/openclaw/pull/92881) | 0 | Local memory/embedding | @openclaw-clownfish[bot] | fix(memory): preserve reindex rollback recovery |
| 🔀&nbsp;[#92876](https://github.com/openclaw/openclaw/pull/92876) | 0 | Local memory/embedding | @openclaw-clownfish[bot] | fix(memory-wiki): stop flagging raw source pages as malformed |
| 📝&nbsp;[#92874](https://github.com/openclaw/openclaw/issues/92874) | 0 | Local memory/embedding | @potterdigital | Builtin memory backend leaks orphaned *.sqlite.tmp-<uuid> reindex files on hard restart (no startup sweep) |
| 🔀&nbsp;[#92867](https://github.com/openclaw/openclaw/pull/92867) | 0 | Local memory/embedding | @XuZehan-iCenter | fix(memory-qmd): preserve Windows absolute paths in QMD command resolution |
| 📝&nbsp;[#92866](https://github.com/openclaw/openclaw/issues/92866) | 0 | OpenAI-compatible/proxy | @Kambrian | Feature: image_generate should support custom/third-party providers, not only built-in ones |
| 📝&nbsp;[#92864](https://github.com/openclaw/openclaw/issues/92864) | 0 | Model routing/config | @cedricdesgagne-falcon | Session model override (/model) silently survives context compaction — cost $300usd  in one day |
| 🔀&nbsp;[#92863](https://github.com/openclaw/openclaw/pull/92863) | 0 | Model/provider behavior | @liuhao1024 | docs(logging): document exact model.usage event field names in diagnostic catalog (fixes #49046) |
| 🔀&nbsp;[#92857](https://github.com/openclaw/openclaw/pull/92857) | 0 | OpenAI-compatible/proxy | @liuhao1024 | fix(openai): drop encrypted reasoning from history for Responses-family APIs (fixes #90093) |
| 🔀&nbsp;[#92854](https://github.com/openclaw/openclaw/pull/92854) | 0 | Model/provider behavior | @openclaw-clownfish[bot] | fix(hooks): reject slug-generator error payloads |
| 🔀&nbsp;[#92850](https://github.com/openclaw/openclaw/pull/92850) | 0 | Local memory/embedding | @yarikv8 | fix(memory-core): reset lastMetaSerialized in runSafeReindex so a byte-identical reindex still writes __meta |
| 📝&nbsp;[#92848](https://github.com/openclaw/openclaw/issues/92848) | 0 | Local memory/embedding | @garrytan-agents | Memory vector search pauses permanently when legacy index has empty `meta` (no identity backfill) |
| 🔀&nbsp;[#92839](https://github.com/openclaw/openclaw/pull/92839) | 0 | OpenAI-compatible/proxy | @yetval | fix(doctor): preserve legacy codex OAuth provider when no models are mergeable |
| 🔀&nbsp;[#92833](https://github.com/openclaw/openclaw/pull/92833) | 0 | Local memory/embedding | @openperf | fix(memory): search memory and wiki concurrently for corpus=all (#92633) |
| 🔀&nbsp;[#92824](https://github.com/openclaw/openclaw/pull/92824) | 0 | Model routing/config | @bek91 | [codex] Fix OpenAI OAuth media routing |
| 🔀&nbsp;[#92821](https://github.com/openclaw/openclaw/pull/92821) | 0 | Model routing/config | @liuhao1024 | fix(agents): use configured primary as fallback origin to prevent indefinite session pinning (#92776) |
| 🔀&nbsp;[#92819](https://github.com/openclaw/openclaw/pull/92819) | 0 | Model routing/config | @TurboTheTurtle | Fix stale auto-fallback origin model selection |
| 📝&nbsp;[#92808](https://github.com/openclaw/openclaw/issues/92808) | 0 | Local memory/embedding | @Alyx-Learbott | [Bug]: Title: Local embedding provider breaks on upgrade (two consecutive releases) — no migration path, misleading error |
| 🔀&nbsp;[#92803](https://github.com/openclaw/openclaw/pull/92803) | 0 | Model/provider behavior | @MonkeyLeeT | fix(thinking): avoid adaptive fallback for budget requests |
| 🔀&nbsp;[#92790](https://github.com/openclaw/openclaw/pull/92790) | 0 | Model routing/config | @TurboTheTurtle | fix(session): clear stale auto fallback origins |
| 🔀&nbsp;[#92782](https://github.com/openclaw/openclaw/pull/92782) | 0 | OpenAI-compatible/proxy | @zhangguiping-xydt | fix #92688: [Bug]: Qwen vision models fail with 400 "Unexpected item type in content" on DashScope |
| 📝&nbsp;[#92776](https://github.com/openclaw/openclaw/issues/92776) | 0 | Model routing/config | @falonrozfatemi | Session model pinning persists indefinitely: snap-back probe (PR #82676) defeated by origin-field pollution upstream — repros on 2026.5.28 through 2026.6.7-beta.1, byte-identical paths |
| 🔀&nbsp;[#92775](https://github.com/openclaw/openclaw/pull/92775) | 0 | Model routing/config | @samson910022 | fix(status): delegate CLI status context resolution and fix slash-model 200K bug (closes #92760) |
| 🔀&nbsp;[#92770](https://github.com/openclaw/openclaw/pull/92770) | 0 | OpenAI-compatible/proxy | @XuZehan-iCenter | fix(media-understanding): place Qwen/DashScope image prompts in user content (#92688) |
| 📝&nbsp;[#92769](https://github.com/openclaw/openclaw/issues/92769) | 0 | OpenAI-compatible/proxy | @Wizongod | [Bug]: Regression of #65533 — reasoning/reasoning_details completely dropped from message history for MiniMax M3 via OpenRouter (both plain-text and tool-call turns) |
| 🔀&nbsp;[#92763](https://github.com/openclaw/openclaw/pull/92763) | 0 | Model routing/config | @1052326311 | fix(gateway): add google-gemini-cli image capability fallback for stale catalog rows |
| 📝&nbsp;[#92760](https://github.com/openclaw/openclaw/issues/92760) | 0 | Model routing/config | @samson910022 | CLI openclaw status shows 200K context window due to standalone resolution copy in status.summary.runtime.ts |
| 🔀&nbsp;[#92759](https://github.com/openclaw/openclaw/pull/92759) | 0 | Local memory/embedding | @1052326311 | fix(memory): guard against missing agentIds in wiki artifact clone and sort |
| 🔀&nbsp;[#92745](https://github.com/openclaw/openclaw/pull/92745) | 0 | Local memory/embedding | @mushuiyu886 | fix(memory): explain skipped short-term recall hits |
| 📝&nbsp;[#92728](https://github.com/openclaw/openclaw/issues/92728) | 0 | Local memory/embedding | @rrriiiccckkk | memory-core: CJK LIKE fallback returns wrong results for multi-character queries |
| 🔀&nbsp;[#92725](https://github.com/openclaw/openclaw/pull/92725) | 0 | Local memory/embedding | @michmill1970 | External reranker |
| 📝&nbsp;[#92706](https://github.com/openclaw/openclaw/issues/92706) | 0 | Local memory/embedding | @armarinho | Dreaming deep-sleep promotes 0 — short-term recall store only populated by session-corpus ingestion (recallCount stays 0); is live memory_search supposed to feed recall? |
| 🔀&nbsp;[#92704](https://github.com/openclaw/openclaw/pull/92704) | 0 | OpenAI-compatible/proxy | @sheyanmin | #92688: fix(qwen): use DashScope native image format for Qwen vision models |
| 🔀&nbsp;[#92698](https://github.com/openclaw/openclaw/pull/92698) | 0 | Local memory/embedding | @mushuiyu886 | fix #80582: Memory: skip markdown placeholder snippets during short-term promotion |
| 📝&nbsp;[#92688](https://github.com/openclaw/openclaw/issues/92688) | 0 | OpenAI-compatible/proxy | @Yachiyo404 | [Bug]: Qwen vision models fail with 400 "Unexpected item type in content" on DashScope |
| 🔀&nbsp;[#92676](https://github.com/openclaw/openclaw/pull/92676) | 0 | Model routing/config | @kumaxs | feat: Rate-limit fallback user-visible error notification (message-lifecycle Phase 2 extension) |
| 📝&nbsp;[#92675](https://github.com/openclaw/openclaw/issues/92675) | 0 | Model/provider behavior | @Robin9plus1 | GitHub Copilot recurring HTTP 401 after 2026.6.6 — incomplete SQLite auth migration leaves stale auth-profiles.json / auth-state.json |
| 📝&nbsp;[#92674](https://github.com/openclaw/openclaw/issues/92674) | 0 | Model routing/config | @xxtyyq | [Bug] Thinking level fallback to "adaptive" silently increases token usage 4-5x when user requests "medium" on models that only support [off, adaptive] |
| 📝&nbsp;[#92672](https://github.com/openclaw/openclaw/issues/92672) | 0 | Model routing/config | @kumaxs | [RFC] Rate-limit fallback: user-visible error + immediate switch notification (message-lifecycle Phase 2 extension) |
| 🔀&nbsp;[#92665](https://github.com/openclaw/openclaw/pull/92665) | 0 | OpenAI-compatible/proxy | @kagura-agent | fix(llm): honor cacheRetention for LiteLLM-proxied Anthropic models |
| 🔀&nbsp;[#92663](https://github.com/openclaw/openclaw/pull/92663) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): unwrap message envelope in extractNarrativeText for cron context (fixes #90292) |
| 📝&nbsp;[#92655](https://github.com/openclaw/openclaw/issues/92655) | 0 | Model routing/config | @renaudcerrato | [Bug]: Telegram: /models provider buttons do nothing when clicked in a forum topic group |
| 🔀&nbsp;[#92649](https://github.com/openclaw/openclaw/pull/92649) | 0 | Open-weight/provider behavior | @litang9 | feat(kimi): show code quota in usage status |
| 🔀&nbsp;[#92647](https://github.com/openclaw/openclaw/pull/92647) | 0 | Local memory/embedding | @Bartok9 | fix(memory): attribute corpus=all timeouts to the slow branch instead of the provider |
| 📝&nbsp;[#92638](https://github.com/openclaw/openclaw/issues/92638) | 0 | Local memory/embedding | @djtitov-netizen | [Bug]: Memory index meta table not populated; index --force and status --index hang |
| 📝&nbsp;[#92633](https://github.com/openclaw/openclaw/issues/92633) | 0 | Local memory/embedding | @desksk | memory_search corpus=all times out while individual corpora succeed |
| 🔀&nbsp;[#92632](https://github.com/openclaw/openclaw/pull/92632) | 0 | Local memory/embedding | @anyech | fix(memory-core): clarify memory_search tool timeouts |
| 🔀&nbsp;[#92624](https://github.com/openclaw/openclaw/pull/92624) | 0 | Local memory/embedding | @yu-xin-c | fix(memory-core): honor qmd search timeouts |
| 🔀&nbsp;[#92623](https://github.com/openclaw/openclaw/pull/92623) | 0 | Local memory/embedding | @liuhao1024 | fix(dreaming): increase narrative timeout from 60s to 120s for ARM devices (fixes #92494) |
| 📝&nbsp;[#92598](https://github.com/openclaw/openclaw/issues/92598) | 0 | Model routing/config | @nguyenjustin214-lab | Discord compaction still fails with provider_error_4xx after #90496 closure on 2026.6.5 |
| 🔀&nbsp;[#92594](https://github.com/openclaw/openclaw/pull/92594) | 0 | Local model runtime | @zhangguiping-xydt | [Bug]: ollama-cloud runtime fails DNS lookup for ai.ollama.com, while ollama/&lt;model&gt;:cloud works |
| 📝&nbsp;[#92582](https://github.com/openclaw/openclaw/issues/92582) | 0 | Local memory/embedding | @neekolascmd | Bug: doctor falsely warns local memory embeddings are not ready |
| 🔀&nbsp;[#92560](https://github.com/openclaw/openclaw/pull/92560) | 0 | Local memory/embedding | @XuZehan-iCenter | fix(memory-qmd): preserve Windows absolute paths in QMD command resolution |
| 📝&nbsp;[#92559](https://github.com/openclaw/openclaw/issues/92559) | 0 | OpenAI-compatible/proxy | @fmsonic | Feature: Session-aware template variables in extra_body (e.g. {{session.channel}}) |
| 🔀&nbsp;[#92557](https://github.com/openclaw/openclaw/pull/92557) | 0 | Local model runtime | @Patrick-Erichsen | Validate ClawHub plugin metadata in PRs |
| 🔀&nbsp;[#92556](https://github.com/openclaw/openclaw/pull/92556) | 0 | OpenAI-compatible/proxy | @smolskayanastassia | feat(llm): add Inworld as built-in llm provider |
| 🔀&nbsp;[#92544](https://github.com/openclaw/openclaw/pull/92544) | 0 | OpenAI-compatible/proxy | @jperla | Add TrustedRouter setup docs |
| 🔀&nbsp;[#92541](https://github.com/openclaw/openclaw/pull/92541) | 0 | Local memory/embedding | @yxshee | fix(plugins): load dreaming engine when memory slot plugin omitted from allowlist |
| 🔀&nbsp;[#92505](https://github.com/openclaw/openclaw/pull/92505) | 0 | OpenAI-compatible/proxy | @zenglingbiao | fix(gateway): validate agent roster in resolveAgentIdForRequest (fixes #92504) |
| 🔀&nbsp;[#92502](https://github.com/openclaw/openclaw/pull/92502) | 0 | Local/media model provider | @100yenadmin | Add Telegram voice STT telemetry and cron payload audit |
| 📝&nbsp;[#92500](https://github.com/openclaw/openclaw/issues/92500) | 0 | Local/media model provider | @100yenadmin | Add Telegram voice/STT handoff telemetry into agent context |
| 🔀&nbsp;[#92499](https://github.com/openclaw/openclaw/pull/92499) | 0 | Local memory/embedding | @SYU8384 | Memory/QMD: isolate mcporter sidecars per agent |
| 🔀&nbsp;[#92496](https://github.com/openclaw/openclaw/pull/92496) | 0 | Model routing/config | @liuhao1024 | fix(agents): set origin fields for config-driven subagent model overrides (fixes #92486) |
| 🔀&nbsp;[#92495](https://github.com/openclaw/openclaw/pull/92495) | 0 | OpenAI-compatible/proxy | @mushuiyu886 | fix(opencode): restore Zen model catalog |
| 📝&nbsp;[#92494](https://github.com/openclaw/openclaw/issues/92494) | 0 | Local memory/embedding | @KingYiKa | Dreaming narrative timeout on ARM devices with many skills (600+) |
| 🔀&nbsp;[#92488](https://github.com/openclaw/openclaw/pull/92488) | 0 | OpenAI-compatible/proxy | @s554097550 | fix(gateway): accept image-only input on /v1/responses |
| 📝&nbsp;[#92486](https://github.com/openclaw/openclaw/issues/92486) | 0 | Model routing/config | @PatrickTrent | Subagent model override from agents.defaults.subagents.model is silently discarded (modelOverrideSource:"auto" matches legacy-cleanup heuristic) |
| 📝&nbsp;[#92479](https://github.com/openclaw/openclaw/issues/92479) | 0 | Model routing/config | @aaajiao | feat(opencode): Zen provider ships no model catalog — every Zen model must be hand-registered (opencode-go discovers, opencode does not) |
| 📝&nbsp;[#92478](https://github.com/openclaw/openclaw/issues/92478) | 0 | Local/media model provider | @novaagentia-cpu | [Bug]: Native Talk button triggers OpenAI Realtime WebRTC call and fails with 500 when Realtime is not configured |
| 🔀&nbsp;[#92476](https://github.com/openclaw/openclaw/pull/92476) | 0 | Model routing/config | @yu-xin-c | fix(agents): preserve compatible CLI session runtime pins |
| 📝&nbsp;[#92473](https://github.com/openclaw/openclaw/issues/92473) | 0 | Model routing/config | @guscamara | Model fallback notice leaks to external user-facing channels |
| 🔀&nbsp;[#92466](https://github.com/openclaw/openclaw/pull/92466) | 0 | OpenAI-compatible/proxy | @EvoLinkAI | Add EvoLink provider integration |
| 📝&nbsp;[#92451](https://github.com/openclaw/openclaw/issues/92451) | 0 | Open-weight/provider behavior | @syfvb | v2026.6.x system prompt bloat causes instruction following degradation on smaller models |
| 🔀&nbsp;[#92446](https://github.com/openclaw/openclaw/pull/92446) | 0 | Local/media model provider | @zenglingbiao | feat(cli): add --file option to image generate command (fixes #91734) |
| 📝&nbsp;[#92444](https://github.com/openclaw/openclaw/issues/92444) | 0 | Model routing/config | @xThe-Dude | Provider disabled:billing cooldown deadlocks for full 5h after credits restored — no early-clear path |
| 🔀&nbsp;[#92439](https://github.com/openclaw/openclaw/pull/92439) | 0 | OpenAI-compatible/proxy | @bladin | fix/92327 openai responses fix |
| 🔀&nbsp;[#92437](https://github.com/openclaw/openclaw/pull/92437) | 0 | OpenAI-compatible/proxy | @bladin | fix/92327 webchat inter session ui regression final |
| 🔀&nbsp;[#92436](https://github.com/openclaw/openclaw/pull/92436) | 0 | OpenAI-compatible/proxy | @bladin | fix: openai-responses adapter sends system prompt in instructions |
| 🔀&nbsp;[#92431](https://github.com/openclaw/openclaw/pull/92431) | 0 | Model routing/config | @liuhao1024 | fix(agents): use thinking-level fallback for programmatic spawn instead of hard throw (fixes #92412) |
| 🔀&nbsp;[#92424](https://github.com/openclaw/openclaw/pull/92424) | 0 | Model routing/config | @liuhao1024 | fix(agents): resolve fresh model from registry for post-turn reads after /model switch (fixes #92415) |
| 📝&nbsp;[#92412](https://github.com/openclaw/openclaw/issues/92412) | 0 | Model routing/config | @oiGaDio | BUG: sessions_spawn silently half-fails when thinking level is unsupported — fan-out spawns produce non-deterministic survivors, no signal to orchestrator (fix: symmetrize CLI-launch fallback with embedded path) |
| 📝&nbsp;[#92405](https://github.com/openclaw/openclaw/issues/92405) | 0 | Model routing/config | @oiGaDio | subagent spawn persists raw provider instead of CLI runtime — depth-2 cold spawns silently die with 'lost execution context' (two unpatched #57326 call sites, fix included) |
| 🔀&nbsp;[#92404](https://github.com/openclaw/openclaw/pull/92404) | 0 | OpenAI-compatible/proxy | @liuhao1024 | fix(openai-responses): use instructions parameter for system prompt instead of input array |
| 📝&nbsp;[#92400](https://github.com/openclaw/openclaw/issues/92400) | 0 | OpenAI-compatible/proxy | @chenpeimin2 | [Bug]: `openai-responses` adapter sends system prompt in `input` instead of `instructions` |
| 🔀&nbsp;[#92399](https://github.com/openclaw/openclaw/pull/92399) | 0 | OpenAI-compatible/proxy | @amersheeny | fix(llm): collapse cumulative openai-responses message snapshots instead of concatenating [AI-assisted] |
| 📝&nbsp;[#92391](https://github.com/openclaw/openclaw/issues/92391) | 0 | Model routing/config | @kvzsolt | [Bug]: ollama-cloud runtime fails DNS lookup for ai.ollama.com, while ollama/&lt;model&gt;:cloud works |
| 🔀&nbsp;[#92388](https://github.com/openclaw/openclaw/pull/92388) | 0 | Model routing/config | @sheyanmin | #92379: fix(session): refresh stale model before reading contextWindow in checkCompaction |
| 🔀&nbsp;[#92378](https://github.com/openclaw/openclaw/pull/92378) | 0 | Local memory/embedding | @xydigit-sj | fix(plugins): guard against missing agentIds in memory-wiki public artifacts (#92207) |
| 🔀&nbsp;[#92375](https://github.com/openclaw/openclaw/pull/92375) | 0 | Local memory/embedding | @zhangqueping | #92134: fix(memory-wiki): retry transient path-alias errors during source page write |
| 🔀&nbsp;[#92363](https://github.com/openclaw/openclaw/pull/92363) | 0 | Local model runtime | @zhangqueping | #92224: fix(models): report local models as available in CLI list output |
| 🔀&nbsp;[#92359](https://github.com/openclaw/openclaw/pull/92359) | 0 | OpenAI-compatible/proxy | @jiewent1-cmyk | fix(config): allow model.compat.sendSessionAffinityHeaders in ModelCompatSchema |
| 🔀&nbsp;[#92341](https://github.com/openclaw/openclaw/pull/92341) | 0 | Local memory/embedding | @rrriiiccckkk | fix(memory-core): remove CJK length threshold for trigram LIKE matching |
| 📝&nbsp;[#92337](https://github.com/openclaw/openclaw/issues/92337) | 0 | Local memory/embedding | @rrriiiccckkk | memory-core: mergeHybridResults ignores textScore when keyword/vector chunk IDs don't overlap |
| 📝&nbsp;[#92320](https://github.com/openclaw/openclaw/issues/92320) | 0 | Model routing/config | @reallyleelee | Provider-level retry configuration for rate-limit errors (403/429) |
| 📝&nbsp;[#92302](https://github.com/openclaw/openclaw/issues/92302) | 0 | Local memory/embedding | @Ardooken | memory.qmd.command path mangled on Windows — QMD memory backend unusable despite working CLI (CommonJS path concatenation strips separators) |
| 🔀&nbsp;[#92288](https://github.com/openclaw/openclaw/pull/92288) | 0 | OpenAI-compatible/proxy | @ai-hpc | fix(agents): quiet extra_body tuning-key collisions |
| 📝&nbsp;[#92273](https://github.com/openclaw/openclaw/issues/92273) | 0 | Local memory/embedding | @poison | Tool Search (mode: "tools") silently breaks the pre-compaction memory flush: model calls tool_call with a guessed name, gets an unrecoverable error, durable memories are lost |
| 📝&nbsp;[#92271](https://github.com/openclaw/openclaw/issues/92271) | 0 | Model routing/config | @MertBasar0 | Fallback turns can re-execute work already reported as completed (semantic recursive task execution) |
| 🔀&nbsp;[#92263](https://github.com/openclaw/openclaw/pull/92263) | 0 | Model/provider behavior | @harjothkhara | Fix heartbeat reasoning payload selection |
| 🔀&nbsp;[#92261](https://github.com/openclaw/openclaw/pull/92261) | 0 | Local memory/embedding | @skocher | Fix live orphan session transcript visibility |
| 📝&nbsp;[#92260](https://github.com/openclaw/openclaw/issues/92260) | 0 | Model/provider behavior | @jmpei | [Bug]: Heartbeat delivers reasoning payload as main reply when includeReasoning is false (resolveHeartbeatReplyPayload ignores isReasoning) |
| 🔀&nbsp;[#92254](https://github.com/openclaw/openclaw/pull/92254) | 0 | Model routing/config | @jbetala7 | fix(model-picker): preserve auth profile override when selecting a model |
| 🔀&nbsp;[#92253](https://github.com/openclaw/openclaw/pull/92253) | 0 | Local memory/embedding | @Glucksberg | [codex] active-memory default to configured agents |
| 📝&nbsp;[#92244](https://github.com/openclaw/openclaw/issues/92244) | 0 | Model routing/config | @saphoroth | [bug] Telegram model picker call to applyModelOverrideToSessionEntry doesn't pass preserveAuthProfileOverride, causing silent destruction of auth profile overrides set by non-picker sources |
| 🔀&nbsp;[#92243](https://github.com/openclaw/openclaw/pull/92243) | 0 | OpenAI-compatible/proxy | @juan-lee | feat(coreweave): add CoreWeave Serverless Inference model provider |
| 📝&nbsp;[#92232](https://github.com/openclaw/openclaw/issues/92232) | 0 | OpenAI-compatible/proxy | @juan-lee | [Feature]: Add CoreWeave Serverless Inference (formerly Weights & Biases) model provider |
| 🔀&nbsp;[#92230](https://github.com/openclaw/openclaw/pull/92230) | 0 | Model routing/config | @clawSean | feat: add model switch choices to /model |
| 📝&nbsp;[#92224](https://github.com/openclaw/openclaw/issues/92224) | 0 | Local model runtime | @lingfeizi | Bug: CLI shows available: false for local Ollama models that are running and working |
| 🔀&nbsp;[#92217](https://github.com/openclaw/openclaw/pull/92217) | 0 | Open-weight/provider behavior | @obuchowski | feat(fireworks): catalog DeepSeek V4 Pro, MiniMax M2.7, GLM-5.1, GPT-OSS 120B reasoning models |
| 🔀&nbsp;[#92200](https://github.com/openclaw/openclaw/pull/92200) | 0 | Local model runtime | @zenglingbiao | fix(openai-completions): fallback to compat.reasoningEffortMap when thinkingLevelMap is unset (fixes #91913) |
| 🔀&nbsp;[#92196](https://github.com/openclaw/openclaw/pull/92196) | 0 | Local memory/embedding | @yetval | fix(memory-search): stop hybrid fusion from discounting vector-only multimodal results |
| 🔀&nbsp;[#92191](https://github.com/openclaw/openclaw/pull/92191) | 0 | Model/provider behavior | @ai-hpc | fix(agents): retry thinking-only errored turns |
| 📝&nbsp;[#92187](https://github.com/openclaw/openclaw/issues/92187) | 0 | Local memory/embedding | @yaorenliang | Memory Index Repeatedly Broken After Gateway Restart (OOM during Rebuild) |
| 🔀&nbsp;[#92176](https://github.com/openclaw/openclaw/pull/92176) | 0 | Model routing/config | @zhangqueping | fix(media-understanding): resolve image model input from catalog, preserve explicit text-only (#92104) |
| 🔀&nbsp;[#92174](https://github.com/openclaw/openclaw/pull/92174) | 0 | OpenAI-compatible/proxy | @RishiP2006 | feat(aigateway): add AIgateway as a bundled model provider |
| 🔀&nbsp;[#92165](https://github.com/openclaw/openclaw/pull/92165) | 0 | Local memory/embedding | @bennewell35 | fix(memory): show dreaming status without search |
| 🔀&nbsp;[#92164](https://github.com/openclaw/openclaw/pull/92164) | 0 | Local memory/embedding | @draix | fix(memory-core): score CJK keyword search instead of textScore=0 with trigram FTS5 |
| 🔀&nbsp;[#92147](https://github.com/openclaw/openclaw/pull/92147) | 0 | OpenAI-compatible/proxy | @skingford | [codex] support Responses system prompts in instructions |
| 🔀&nbsp;[#92135](https://github.com/openclaw/openclaw/pull/92135) | 0 | Local memory/embedding | @xialonglee | fix(openai-embedding): preserve openai/ prefix for non-native base URLs |
| 📝&nbsp;[#92124](https://github.com/openclaw/openclaw/issues/92124) | 0 | OpenAI-compatible/proxy | @Kambrian | Memory search breaks with Requesty/OpenAI embedding model prefix mismatch |
| 📝&nbsp;[#92117](https://github.com/openclaw/openclaw/issues/92117) | 0 | Model routing/config | @wangwllu | Flaky / failing: simple-completion-runtime > can preserve asynchronous provider model discovery (introduced 25ca39e876) |
| 🔀&nbsp;[#92114](https://github.com/openclaw/openclaw/pull/92114) | 0 | Local memory/embedding | @TurboTheTurtle | fix(memory): report indexed vector store in status |
| 📝&nbsp;[#92105](https://github.com/openclaw/openclaw/issues/92105) | 0 | Local memory/embedding | @qiaokuan1992 | [Feature]: Configurable page groups for memory-wiki with custom index directories and recursive scanning |
| 📝&nbsp;[#92102](https://github.com/openclaw/openclaw/issues/92102) | 0 | Local memory/embedding | @pepe-hern | [Bug]: openclaw memory status shows "Vector store: unknown" despite working vectors (sqlite-vec lazy init in CLI fast path) |
| 🔀&nbsp;[#92099](https://github.com/openclaw/openclaw/pull/92099) | 0 | Local memory/embedding | @bladin | feat(active-memory): add messageMaxChars config to cap latest user message in message mode |
| 🔀&nbsp;[#92079](https://github.com/openclaw/openclaw/pull/92079) | 0 | Local memory/embedding | @xydt-tanshanshan | [AI] fix(memory): auto-fix providerKey mismatch from CLI index --force |
| 🔀&nbsp;[#92072](https://github.com/openclaw/openclaw/pull/92072) | 0 | Model routing/config | @HaozheZhang6 | fix(gateway): treat `google-gemini-cli` Gemini models as image-capable |
| 🔀&nbsp;[#92065](https://github.com/openclaw/openclaw/pull/92065) | 0 | Local memory/embedding | @arkyu2077 | fix(memory): honor configured qmd search timeouts |
| 📝&nbsp;[#92061](https://github.com/openclaw/openclaw/issues/92061) | 0 | Local memory/embedding | @rrriiiccckkk | memory-core: CJK text FTS5 search returns textScore=0 with trigram tokenizer |
| 📝&nbsp;[#92057](https://github.com/openclaw/openclaw/issues/92057) | 0 | Local model runtime | @xiaopings | Gateway becomes slow or times out under multi-session / multi-agent load |
| 📝&nbsp;[#92054](https://github.com/openclaw/openclaw/issues/92054) | 0 | Model routing/config | @arturomagdiel | [Bug]: Windows 11 - Claude CLI provider fails with spawn claude ENOENT |
| 📝&nbsp;[#92043](https://github.com/openclaw/openclaw/issues/92043) | 0 | Model routing/config | @yetval | Bug: 180s compaction timeout is a single wall clock over the whole chunk pipeline with no partial-progress reuse, so a legitimately-long compaction fails identically every turn |
| 🔀&nbsp;[#92040](https://github.com/openclaw/openclaw/pull/92040) | 0 | OpenAI-compatible/proxy | @849261680 | fix(provider): route thinking profiles by model API |
| 🔀&nbsp;[#92035](https://github.com/openclaw/openclaw/pull/92035) | 0 | Local memory/embedding | @fall4knight | feat(memory): apply temporal decay to QMD search results |
| 📝&nbsp;[#92013](https://github.com/openclaw/openclaw/issues/92013) | 0 | Local memory/embedding | @islandpreneur007 | Active Memory `queryMode: "message"` can receive full assembled request envelopes; needs latest-message cap or slim-intent field |
| 🔀&nbsp;[#92012](https://github.com/openclaw/openclaw/pull/92012) | 0 | OpenAI-compatible/proxy | @mariusbolik | docs(providers): add LLMBase setup guide |
| 🔀&nbsp;[#92011](https://github.com/openclaw/openclaw/pull/92011) | 0 | Model routing/config | @MertBasar0 | fix(agents): prevent recursive task execution during model fallback |
| 🔀&nbsp;[#92002](https://github.com/openclaw/openclaw/pull/92002) | 0 | Local model runtime | @nxmxbbd | fix(lmstudio): deliver thinking "off" to binary-thinking models |
| 📝&nbsp;[#91999](https://github.com/openclaw/openclaw/issues/91999) | 0 | Model routing/config | @andresparilli | Bug: Main agent model reverts to Gemini in terminal sessions |
| 📝&nbsp;[#91971](https://github.com/openclaw/openclaw/issues/91971) | 0 | Local model runtime | @nikosml | [Bug]: @openclaw/llama-cpp-provider documented but not published to npm/ClawHub |
| 📝&nbsp;[#91959](https://github.com/openclaw/openclaw/issues/91959) | 0 | OpenAI-compatible/proxy | @phoenixyy | Bedrock Mantle (openai-responses) cumulatively duplicates reply text with reasoning enabled (GPT-5.x) |
| 🔀&nbsp;[#91958](https://github.com/openclaw/openclaw/pull/91958) | 0 | Local memory/embedding | @zenglingbiao | fix(memory): align memory_search tool deadline with configured QMD timeout (fixes #91947) |
| 📝&nbsp;[#91956](https://github.com/openclaw/openclaw/issues/91956) | 0 | Open-weight/provider behavior | @xunx33 | bug: 飞书流式回复重复显示思考过程和工具调用信息 |
| 📝&nbsp;[#91953](https://github.com/openclaw/openclaw/issues/91953) | 0 | Model routing/config | @lml2468 | [Bug]: empty-error-retry skipped when stop_reason="error" turn contains a thinking block or non-zero output, causing silent mid-turn abort on multi-step tasks |
| 📝&nbsp;[#91951](https://github.com/openclaw/openclaw/issues/91951) | 0 | Local memory/embedding | @workingpleasewait | [Feature]: memory index: support maxAgeDays config to limit indexed window |
| 📝&nbsp;[#91949](https://github.com/openclaw/openclaw/issues/91949) | 0 | Model routing/config | @philipmisner63-ux | invalid_request_error from Anthropic kills session instead of triggering fallback |
| 📝&nbsp;[#91947](https://github.com/openclaw/openclaw/issues/91947) | 0 | Local memory/embedding | @guojiongming | memory_search 工具硬编码 15s timeout 不够 qmd query 跑完，建议可配置 |
| 📝&nbsp;[#91945](https://github.com/openclaw/openclaw/issues/91945) | 0 | OpenAI-compatible/proxy | @alexminza | [Feature]: Upgrade Cloudflare AI Gateway provider to the REST API |
| 📝&nbsp;[#91929](https://github.com/openclaw/openclaw/issues/91929) | 0 | OpenAI-compatible/proxy | @ofpay-code | [Bug]: model provider config custom proxy url, image generation error |
| 📝&nbsp;[#91928](https://github.com/openclaw/openclaw/issues/91928) | 0 | Open-weight/provider behavior | @34262315716 | DeepSeek 模型在长上下文中注意力偏移（attention inertia）—— 倾向回应上一轮而非最新消息 |
| 📝&nbsp;[#91913](https://github.com/openclaw/openclaw/issues/91913) | 0 | Local model runtime | @mlaihk | openai-completions legacy path drops `compat.reasoningEffortMap` and `thinkLevel`; LM Studio binary-thinking models silently fall back to thinking-on |
| 📝&nbsp;[#91902](https://github.com/openclaw/openclaw/issues/91902) | 0 | Local memory/embedding | @charles717-art | [BUG] memory index --force CLI writes incompatible meta providerKey, breaks runtime memory_search |
| 📝&nbsp;[#91892](https://github.com/openclaw/openclaw/issues/91892) | 0 | Open-weight/provider behavior | @luciaski | Cron jobs stall during AI model calls (model_call:stream_progress never completes) |
| 📝&nbsp;[#91881](https://github.com/openclaw/openclaw/issues/91881) | 0 | OpenAI-compatible/proxy | @denisneuf | v2026.6.5 - DeepSeek 401 auth error después de actualizar |
| 🔀&nbsp;[#91875](https://github.com/openclaw/openclaw/pull/91875) | 0 | Model routing/config | @yichu10c | fix(github-copilot): claude-opus-4.8 context window to 1M with reasoning support |
| 🔀&nbsp;[#91870](https://github.com/openclaw/openclaw/pull/91870) | 0 | Model routing/config | @wyhgoodjob | fix(github-copilot): claude-opus-4.8 is native 1M context + thinking (not 128K) |
| 📝&nbsp;[#91869](https://github.com/openclaw/openclaw/issues/91869) | 0 | Model routing/config | @wyhgoodjob | GitHub Copilot: claude-opus-4.8 hard-coded to 128K context (native 1M) + missing thinking support |
| 🔀&nbsp;[#91862](https://github.com/openclaw/openclaw/pull/91862) | 0 | Local memory/embedding | @xydt-tanshanshan | fix(memory): gracefully degrade when embedding provider is unregistered |
| 📝&nbsp;[#91854](https://github.com/openclaw/openclaw/issues/91854) | 0 | Local memory/embedding | @MahmutDehhan | [Bug]: Memory dreaming narrative/REM lane is given apply_patch and misuses it |
| 📝&nbsp;[#91839](https://github.com/openclaw/openclaw/issues/91839) | 0 | Model routing/config | @aspalagin | [Bug]: Terminal provider model_not_available in subagent announce path can trigger chat.history storm and gateway event-loop starvation |
| 📝&nbsp;[#91806](https://github.com/openclaw/openclaw/issues/91806) | 0 | Model routing/config | @Cornil79 | [Bug]: Session shows openai/gpt-5.5 in UI, but new turns execute via DeepSeek and chat history collapses into new leaf sessions |
| 🔀&nbsp;[#91770](https://github.com/openclaw/openclaw/pull/91770) | 0 | Local memory/embedding | @ai-hpc | fix(memory): abort search embeddings on tool timeout |
| 🔀&nbsp;[#91767](https://github.com/openclaw/openclaw/pull/91767) | 0 | Model/provider behavior | @aliahnaf2013-max | Fix one-shot Codex app-server teardown |
| 📝&nbsp;[#91739](https://github.com/openclaw/openclaw/issues/91739) | 0 | Model routing/config | @ruben2000de | google-gemini-cli rejects image attachments before CLI image prestage |
| 🔀&nbsp;[#91728](https://github.com/openclaw/openclaw/pull/91728) | 0 | Model routing/config | @saju01 | fix(github-copilot): prefer live model catalog |
| 🔀&nbsp;[#91724](https://github.com/openclaw/openclaw/pull/91724) | 0 | Model routing/config | @yu-xin-c | fix(agents): infer runtime provider from qualified model ids |
| 🔀&nbsp;[#91714](https://github.com/openclaw/openclaw/pull/91714) | 0 | OpenAI-compatible/proxy | @dwc1997 | fix(agents): apply Gemini schema cleaning for Gemini models via OpenAI-compat providers |
| 🔀&nbsp;[#91706](https://github.com/openclaw/openclaw/pull/91706) | 0 | Local memory/embedding | @tiffanychum | fix(memory): keep local embedding indexes clean when only local.modelPath is set |
| 🔀&nbsp;[#91691](https://github.com/openclaw/openclaw/pull/91691) | 0 | Local memory/embedding | @xydt-tanshanshan | [AI] fix(memory): prevent empty-string expectedModel in resolveMemory… |
| 📝&nbsp;[#91683](https://github.com/openclaw/openclaw/issues/91683) | 0 | Model/provider behavior | @GabeMillikan | [Feature]: Add provider-native file/document forwarding for non-image attachments |
| 🔀&nbsp;[#91660](https://github.com/openclaw/openclaw/pull/91660) | 0 | Local memory/embedding | @xydt-tanshanshan | [AI] fix(memory): backfill provider.model with resolved model name in… |
| 🔀&nbsp;[#91644](https://github.com/openclaw/openclaw/pull/91644) | 0 | OpenAI-compatible/proxy | @tracy-e | feat(gateway): add OpenAI-compatible /v1/audio/speech endpoint |
| 🔀&nbsp;[#91640](https://github.com/openclaw/openclaw/pull/91640) | 0 | Model routing/config | @z1pp090 | docs(compaction): warn that compaction.model breaks native compaction on claude-cli/OAuth |
| 🔀&nbsp;[#91625](https://github.com/openclaw/openclaw/pull/91625) | 0 | Model routing/config | @ly-wang19 | fix(cron): add cron edit --clear-model to clear a job's model override |
| 📝&nbsp;[#91622](https://github.com/openclaw/openclaw/issues/91622) | 0 | Model/provider behavior | @beerygaz | gpt-5.4-mini via Responses API: incomplete turn false positive + claude eager_input_streaming schema rejection |
| 🔀&nbsp;[#91596](https://github.com/openclaw/openclaw/pull/91596) | 0 | Local memory/embedding | @ly-wang19 | fix(memory): use local modelPath for status identity so custom local models aren't always dirty (fixes #91001) |
| 📝&nbsp;[#91592](https://github.com/openclaw/openclaw/issues/91592) | 0 | Local memory/embedding | @StarbloomConsultingHub | memory_search broken with "index scope changed" after --force rebuild — scopeHash mismatch persists |
| 📝&nbsp;[#91572](https://github.com/openclaw/openclaw/issues/91572) | 0 | Local memory/embedding | @Orionation | Dreaming light phase should ingest workspace file creation events, not just memory/*.md |
| 📝&nbsp;[#91563](https://github.com/openclaw/openclaw/issues/91563) | 0 | Local memory/embedding | @Orionation | Dreaming deep phase: minUniqueQueries gate bypassed by day-diversity counting |
| 🔀&nbsp;[#91559](https://github.com/openclaw/openclaw/pull/91559) | 0 | OpenAI-compatible/proxy | @Huangting-xy | fix(agents): clean Gemini tool schemas by model id |
| 📝&nbsp;[#91552](https://github.com/openclaw/openclaw/issues/91552) | 0 | Model routing/config | @rmichelena | Codex app-server binding sidecar can retain stale GPT model across provider switches, causing embedded runs to dispatch zai/gpt-5.5 |
| 🔀&nbsp;[#91549](https://github.com/openclaw/openclaw/pull/91549) | 0 | OpenAI-compatible/proxy | @studentzhou-svg | fix: enable DeepSeek DSML filtering for proxy providers via model id detection |
| 🔀&nbsp;[#91546](https://github.com/openclaw/openclaw/pull/91546) | 0 | Model/provider behavior | @arkyu2077 | fix: add gemini-3.5-flash to the Google provider catalog |
| 📝&nbsp;[#91542](https://github.com/openclaw/openclaw/issues/91542) | 0 | OpenAI-compatible/proxy | @qiukui666 | [Bug] Gemini (jjcc/openai-compat) rejects cron tool schema: anyOf properties missing type field in v2026.6.1 |
| 📝&nbsp;[#91537](https://github.com/openclaw/openclaw/issues/91537) | 0 | Model/provider behavior | @mikealford-kuon | [Bug]: Codex yolo mode leaks app-server processes and binding files |
| 📝&nbsp;[#91504](https://github.com/openclaw/openclaw/issues/91504) | 0 | Model/provider behavior | @resYuto | [Feature]: Support another Image generation models on OpenRouter |
| 📝&nbsp;[#91498](https://github.com/openclaw/openclaw/issues/91498) | 0 | Model routing/config | @medikoo | [Feature]: Allow model aliases or runtimes to select different auth profiles for the same provider |
| 🔀&nbsp;[#91459](https://github.com/openclaw/openclaw/pull/91459) | 0 | Local memory/embedding | @dwc1997 | fix(memory-wiki): include workspace in bridge artifact hash to prevent collisions |
| 🔀&nbsp;[#91444](https://github.com/openclaw/openclaw/pull/91444) | 0 | Local memory/embedding | @dwc1997 | fix(google): register 'google' alias for memory embedding provider |
| 📝&nbsp;[#91434](https://github.com/openclaw/openclaw/issues/91434) | 0 | Local model runtime | @lily-oc | [Bug]: LM Studio sessions start without tools |
| 🔀&nbsp;[#91427](https://github.com/openclaw/openclaw/pull/91427) | 0 | OpenAI-compatible/proxy | @849261680 | fix(openai-completions): reject provider empty stop replies |
| 🔀&nbsp;[#91414](https://github.com/openclaw/openclaw/pull/91414) | 0 | Model routing/config | @Linux2010 | fix(agent): agents.defaults.model.fallbacks not inherited by isolated cron sessions |
| 🔀&nbsp;[#91403](https://github.com/openclaw/openclaw/pull/91403) | 0 | OpenAI-compatible/proxy | @ZengWen-DT | fix(openai-completions): route empty stop with no content into error path |
| 🔀&nbsp;[#91397](https://github.com/openclaw/openclaw/pull/91397) | 0 | OpenAI-compatible/proxy | @ErRickow | feat(neosantara): add Neosantara gateway provider and responses API alias |
| 📝&nbsp;[#91396](https://github.com/openclaw/openclaw/issues/91396) | 0 | Local memory/embedding | @xiangcaoni | Memory embedding fails with HTTP 400 when using SiliconFlow (fetchWithSsrFGuard incompatibility) |
| 📝&nbsp;[#91354](https://github.com/openclaw/openclaw/issues/91354) | 0 | Local memory/embedding | @Louisone1 | memory: Gemini embeddings still use inline batch requests after remote.batch.enabled=false, causing 429 on low quota |
| 📝&nbsp;[#91352](https://github.com/openclaw/openclaw/issues/91352) | 0 | Model routing/config | @chac4l | [Bug]: OpenAI Codex OAuth migration leaves stale default profile and codexPlugins app inventory can fail Codex harness |
| 🔀&nbsp;[#91323](https://github.com/openclaw/openclaw/pull/91323) | 0 | Local model runtime | @deepshekhardas | fix(gateway): keep dense stream updates incremental and preserve replacement stream deltas |
| 🔀&nbsp;[#91310](https://github.com/openclaw/openclaw/pull/91310) | 0 | Local memory/embedding | @LiLan0125 | fix(memory): resolve embedding provider by authProviderId fallback |
| 🔀&nbsp;[#91308](https://github.com/openclaw/openclaw/pull/91308) | 0 | OpenAI-compatible/proxy | @jsi-tross | feat(xai): add realtime voice provider |
| 🔀&nbsp;[#91274](https://github.com/openclaw/openclaw/pull/91274) | 0 | Local memory/embedding | @sasan1200 | refactor(memory): drop redundant agent-id scoping from qmd collection names |
| 🔀&nbsp;[#91267](https://github.com/openclaw/openclaw/pull/91267) | 0 | Local memory/embedding | @zenglingbiao | fix(memory-core): skip session archive artifacts during dreaming corpus collection (fixes #90313) |
| 📝&nbsp;[#91259](https://github.com/openclaw/openclaw/issues/91259) | 0 | Local memory/embedding | @sasan1200 | memory(qmd): drop redundant agent-id scoping from collection names |
| 🔀&nbsp;[#91239](https://github.com/openclaw/openclaw/pull/91239) | 0 | Open-weight/provider behavior | @samson910022 | fix(opencode-go): add qwen3.7-max, qwen3.7-plus, minimax-m3 to provider catalog |
| 🔀&nbsp;[#91237](https://github.com/openclaw/openclaw/pull/91237) | 0 | OpenAI-compatible/proxy | @Bartok9 | fix(providers/openrouter): treat openrouter.ai as long-TTL-eligible for Anthropic cache_control |
| 🔀&nbsp;[#91225](https://github.com/openclaw/openclaw/pull/91225) | 0 | Local memory/embedding | @mushuiyu886 | fix #83830: [Bug]: Dreaming diary repeats "first day" narrative every sweep — same early memories dominate snippets |
| 📝&nbsp;[#91223](https://github.com/openclaw/openclaw/issues/91223) | 0 | Local memory/embedding | @Enominera | [Bug]: Active memory injection breaks prompt cache hit rate (99.9% → 22%) |
| 🔀&nbsp;[#91222](https://github.com/openclaw/openclaw/pull/91222) | 0 | Model/provider behavior | @damianFelixPago | fix(google-vertex): retry transient pre-stream failures and stale ADC |
| 🔀&nbsp;[#91217](https://github.com/openclaw/openclaw/pull/91217) | 0 | Model routing/config | @safrano9999 | feat(gateway): add deterministic dummy model (AI-assisted) |
| 📝&nbsp;[#91214](https://github.com/openclaw/openclaw/issues/91214) | 0 | OpenAI-compatible/proxy | @Enominera | [Bug]: Active memory injection breaks prompt_cache_key for OpenAI-compatible providers (compat.supportsPromptCacheKey=true) |
| 🔀&nbsp;[#91211](https://github.com/openclaw/openclaw/pull/91211) | 0 | Model routing/config | @Kirchlive | feat(tui): classify every model as CLI / OAuth / API in /model picker |
| 🔀&nbsp;[#91206](https://github.com/openclaw/openclaw/pull/91206) | 0 | Model routing/config | @tanshanshan | fix(agents/subagent-spawn): Sub-agent model routing ignores model parameter |
| 🔀&nbsp;[#91187](https://github.com/openclaw/openclaw/pull/91187) | 0 | Model routing/config | @openperf | fix(cron): isolate auth profile failure policy so cron runs don't pollute shared cooldowns |
| 📝&nbsp;[#91183](https://github.com/openclaw/openclaw/issues/91183) | 0 | Local memory/embedding | @zhong18804784882 | [Bug]: memorySearch index metadata lost after upgrade to 2026.6.5-beta.2, vector search paused despite 2272 cache entries |
| 🔀&nbsp;[#91182](https://github.com/openclaw/openclaw/pull/91182) | 0 | Local memory/embedding | @Huangting-xy | fix(memory-core): exclude archive transcripts from dreaming session corpus collection |
| 🔀&nbsp;[#91177](https://github.com/openclaw/openclaw/pull/91177) | 0 | Model routing/config | @Kirchlive | fix(tui): persist canonical provider in session modelProvider |
| 📝&nbsp;[#91171](https://github.com/openclaw/openclaw/issues/91171) | 0 | Model routing/config | @wolfeee | [Bug]: Sub-agent model routing ignores model parameter, silently falls back to deepseek |
| 🔀&nbsp;[#91170](https://github.com/openclaw/openclaw/pull/91170) | 0 | Local memory/embedding | @LiuwqGit | fix(memory): align local modelPath index identity on status |
| 🔀&nbsp;[#91168](https://github.com/openclaw/openclaw/pull/91168) | 0 | Model routing/config | @Kirchlive | feat(tui,gateway): show CLI-routing label in /model picker |
| 📝&nbsp;[#91167](https://github.com/openclaw/openclaw/issues/91167) | 0 | Local memory/embedding | @kiagentkronos-cell | bug(memory): gateway cannot self-heal a missing index identity when chunks are already indexed |
| 📝&nbsp;[#91154](https://github.com/openclaw/openclaw/issues/91154) | 0 | Local memory/embedding | @mlaihk | memory-wiki: wiki.palace fails with (path-mismatch) and wiki.importInsights takes 100s+ under load |
| 🔀&nbsp;[#91091](https://github.com/openclaw/openclaw/pull/91091) | 0 | Local memory/embedding | @amknight | fix(memory): do not prune session index from a failed directory scan |
| 📝&nbsp;[#91077](https://github.com/openclaw/openclaw/issues/91077) | 0 | OpenAI-compatible/proxy | @Schnup03 | [Bug] cacheRetention has no effect on Discord direct-message sessions; subagent/cron/channel sessions cache normally |
| 🔀&nbsp;[#91063](https://github.com/openclaw/openclaw/pull/91063) | 0 | Local memory/embedding | @arkyu2077 | fix(memory): write deep summaries into DREAMS.md |
| 🔀&nbsp;[#91057](https://github.com/openclaw/openclaw/pull/91057) | 0 | Local model runtime | @wangwllu | fix(sessions): prune stale gateway model-run sessions |
| 📝&nbsp;[#91052](https://github.com/openclaw/openclaw/issues/91052) | 0 | Local/media model provider | @xueqingli1 | [Feature]: make voice-call realtime barge-in detection configurable |
| 🔀&nbsp;[#91050](https://github.com/openclaw/openclaw/pull/91050) | 0 | Local memory/embedding | @7thfloorindustries | fix(active-memory): keep a runnable iMessage channel so memory thread key builds |
| 🔀&nbsp;[#91028](https://github.com/openclaw/openclaw/pull/91028) | 0 | Model routing/config | @bosszukung | feat(lobster): in-process LLM adapters for embedded runner (#90909) |
| 📝&nbsp;[#91016](https://github.com/openclaw/openclaw/issues/91016) | 0 | OpenAI-compatible/proxy | @RavenSS213 | ⚠️ 升级 2026.6.1 后 DeepSeek Prompt Cache 完全失效，一小时烧掉约 $6 |
| 🔀&nbsp;[#91010](https://github.com/openclaw/openclaw/pull/91010) | 0 | Local memory/embedding | @stevenepalmer | fix(memory): honor local model path in index identity |
| 📝&nbsp;[#91009](https://github.com/openclaw/openclaw/issues/91009) | 0 | Local model runtime | @aspalagin | Codex PreToolUse native hook relay spawns CPU-bound openclaw-hooks processes and stalls gateway RPC |
| 📝&nbsp;[#91007](https://github.com/openclaw/openclaw/issues/91007) | 0 | Local/media model provider | @Countermarch | [Bug]: iOS Talk realtime session closes before audio append and ignores server stt-tts routing |
| 📝&nbsp;[#91001](https://github.com/openclaw/openclaw/issues/91001) | 0 | Local memory/embedding | @samrrr | [Bug]: local embeedings provider fail |
| 📝&nbsp;[#90991](https://github.com/openclaw/openclaw/issues/90991) | 0 | Model routing/config | @cx306806112 | Cron scheduled trigger contaminates global runtime state causing transient system-wide overload failures |
| 🔀&nbsp;[#90990](https://github.com/openclaw/openclaw/pull/90990) | 0 | Model routing/config | @Kailigithub | fix(agents): use appropriate log levels in model-resolver fallback paths |
| 📝&nbsp;[#90982](https://github.com/openclaw/openclaw/issues/90982) | 0 | Open-weight/provider behavior | @taerlandsen | [Bug]: TUI hides tool-call validation errors behind "run aborted" — root cause only visible in gateway log |
| 🔀&nbsp;[#90975](https://github.com/openclaw/openclaw/pull/90975) | 0 | Model/provider behavior | @Kirchlive | feat(google): add Antigravity CLI backend |
| 📝&nbsp;[#90974](https://github.com/openclaw/openclaw/issues/90974) | 0 | Model routing/config | @itanyplus | [Feedback] Stop shipping features. Start shipping a product that works. |
| 🔀&nbsp;[#90968](https://github.com/openclaw/openclaw/pull/90968) | 0 | Model routing/config | @moeedahmed | fix: avoid reapplying ACP startup runtime options |
| 📝&nbsp;[#90925](https://github.com/openclaw/openclaw/issues/90925) | 0 | Model routing/config | @DolencLuka | [Bug]: Subagent announce compaction for Codex/OAuth falls into openai-responses API-key route |
| 📝&nbsp;[#90909](https://github.com/openclaw/openclaw/issues/90909) | 0 | Model routing/config | @bosszukung | [Feature]: Host-provided in-process LLM adapters for the embedded Lobster runner (#76101 bridge) |
| 🔀&nbsp;[#90908](https://github.com/openclaw/openclaw/pull/90908) | 0 | Model routing/config | @shengting | fix(model-fallback): don't rethrow provider-side AbortErrors as user cancellations |
| 🔀&nbsp;[#90903](https://github.com/openclaw/openclaw/pull/90903) | 0 | Model routing/config | @thinhkhang97 | fix(agents): inherit default agent model catalog for secondary agents |
| 🔀&nbsp;[#90889](https://github.com/openclaw/openclaw/pull/90889) | 0 | Model routing/config | @clawsweeper[bot] | fix: cap session context overrides by model window |
| 📝&nbsp;[#90886](https://github.com/openclaw/openclaw/issues/90886) | 0 | Model routing/config | @smisy-system-design[bot] | gateway hangs at `[gateway] starting...` when a declared provider lacks credentials (regression v2026.4.8 -> v2026.4.26) |
| 🔀&nbsp;[#90885](https://github.com/openclaw/openclaw/pull/90885) | 0 | Model routing/config | @Huangting-xy | fix(agent): resolve compaction model alias to canonical model ref |
| 📝&nbsp;[#90881](https://github.com/openclaw/openclaw/issues/90881) | 0 | Model routing/config | @abdulla2010 | doctor --fix migrates codex/gpt-5.5 to openai/gpt-5.5, then Codex app-server startup times out on 2026.6.1 |
| 🔀&nbsp;[#90876](https://github.com/openclaw/openclaw/pull/90876) | 0 | OpenAI-compatible/proxy | @qianwu007 | docs: add ForAI provider setup guide |
| 🔀&nbsp;[#90870](https://github.com/openclaw/openclaw/pull/90870) | 0 | Local memory/embedding | @Agent-Aurelius | [AI] fix(memory-wiki): index wiki pages in query-dir subfolders |
| 📝&nbsp;[#90869](https://github.com/openclaw/openclaw/issues/90869) | 0 | Local memory/embedding | @Agent-Aurelius | wiki_search silently drops pages in subfolders of the wiki query dirs (data loss) |
| 🔀&nbsp;[#90839](https://github.com/openclaw/openclaw/pull/90839) | 0 | Local memory/embedding | @lonexreb | fix(memory-core): exclude soft-deleted .jsonl.deleted paths from dreaming corpus (#90466) |
| 🔀&nbsp;[#90827](https://github.com/openclaw/openclaw/pull/90827) | 0 | Local memory/embedding | @lonexreb | fix(memory-core): surface empty narrative generation instead of silent fallback (#90781) |
| 🔀&nbsp;[#90826](https://github.com/openclaw/openclaw/pull/90826) | 0 | Model routing/config | @lonexreb | fix(tui): render /models loading feedback before listing resolves (#90720) |
| 📝&nbsp;[#90801](https://github.com/openclaw/openclaw/issues/90801) | 0 | Local memory/embedding | @fenglanhua | [Bug]: memory status shows inconsistent Dirty state, watcher stops auto-indexing, and --deep required to confirm health on 2026.6.1 |
| 🔀&nbsp;[#90799](https://github.com/openclaw/openclaw/pull/90799) | 0 | Model routing/config | @wangwllu | fix: handle Claude CLI synthetic placeholders |
| 📝&nbsp;[#90787](https://github.com/openclaw/openclaw/issues/90787) | 0 | Local memory/embedding | @fenglanhua | [Bug]: memorySearch provider silently resets to "openai" after upgrade to 2026.6.1, causing permanent Dirty index and vector search outage |
| 📝&nbsp;[#90786](https://github.com/openclaw/openclaw/issues/90786) | 0 | Local memory/embedding | @fenglanhua | [Bug]: memory status --index and --deep fail with "Unknown memory embedding provider: google" on 2026.6.1 |
| 📝&nbsp;[#90781](https://github.com/openclaw/openclaw/issues/90781) | 0 | Local memory/embedding | @xdengli | [Bug]: memory-core narrative generation silently produces no text and writes fallback diary entries (light/rem/deep phases) |
| 📝&nbsp;[#90763](https://github.com/openclaw/openclaw/issues/90763) | 0 | Model routing/config | @A1fred-AI | [Feature]: Add agents.list[].subagents.allowedModels to restrict model overrides in sessions_spawn |
| 🔀&nbsp;[#90761](https://github.com/openclaw/openclaw/pull/90761) | 0 | Model routing/config | @TeALO36 | fix(android): resolve UI bugs and add SSH tunnelling |
| 📝&nbsp;[#90746](https://github.com/openclaw/openclaw/issues/90746) | 0 | Local memory/embedding | @holgergruenhagen | Document practical requirements for QMD memory backend on CPU-only VPS deployments |
| 🔀&nbsp;[#90741](https://github.com/openclaw/openclaw/pull/90741) | 0 | Model routing/config | @zeroaltitude | perf(models-config): unify auth-profile fingerprint cache + targetProvider short-circuit |
| 🔀&nbsp;[#90739](https://github.com/openclaw/openclaw/pull/90739) | 0 | Local memory/embedding | @brokemac79 | fix(active-memory): preserve verbose recall summaries |
| 🔀&nbsp;[#90731](https://github.com/openclaw/openclaw/pull/90731) | 0 | Model routing/config | @849261680 | fix(agents): hydrate allowlisted dynamic model metadata |
| 🔀&nbsp;[#90727](https://github.com/openclaw/openclaw/pull/90727) | 0 | Local memory/embedding | @dr00-eth | fix(memory): refresh rebuilt index handles |
| 🔀&nbsp;[#90703](https://github.com/openclaw/openclaw/pull/90703) | 0 | OpenAI-compatible/proxy | @Alex-Govorov | Support compat reasoning levels for thinking xhigh |
| 🔀&nbsp;[#90689](https://github.com/openclaw/openclaw/pull/90689) | 0 | OpenAI-compatible/proxy | @ly85206559 | fix(agents): align custom provider auth labels with runtime (#82020) |
| 📝&nbsp;[#90684](https://github.com/openclaw/openclaw/issues/90684) | 0 | Open-weight/provider behavior | @studentzhou-svg | Feishu (and non-Discord channels) should apply sanitizeAssistantVisibleText() on outbound text |
| 🔀&nbsp;[#90683](https://github.com/openclaw/openclaw/pull/90683) | 0 | Local model runtime | @JuanHuaXu | fix: retry safe post-tool continuation turns |
| 📝&nbsp;[#90675](https://github.com/openclaw/openclaw/issues/90675) | 0 | OpenAI-compatible/proxy | @JohnnyBlack123 | [Bug]: Dashboard/agent fake tool calls with dmxapi model; native claude route returns incomplete terminal response |
| 📝&nbsp;[#90674](https://github.com/openclaw/openclaw/issues/90674) | 0 | Model/provider behavior | @motteman | Gateway writes usage.cost: 0 for model strings absent from its internal price table (silent cost under-reporting) |
| 📝&nbsp;[#90642](https://github.com/openclaw/openclaw/issues/90642) | 0 | Local/media model provider | @ruizcrp | [Feature]: Gemma4-12b (and other models) audio not supported yet |
| 🔀&nbsp;[#90603](https://github.com/openclaw/openclaw/pull/90603) | 0 | Model routing/config | @Bartok9 | fix(secrets): use configured default agent ID in auth/model path discovery (#90573) |
| 🔀&nbsp;[#90574](https://github.com/openclaw/openclaw/pull/90574) | 0 | OpenAI-compatible/proxy | @BSG2000 | fix(openai): omit gpt-5.5 tool reasoning effort |
| 📝&nbsp;[#90556](https://github.com/openclaw/openclaw/issues/90556) | 0 | Local model runtime | @Wsq-159 | Chat UI: Display response latency under each message |
| 📝&nbsp;[#90536](https://github.com/openclaw/openclaw/issues/90536) | 0 | Model routing/config | @ozp | OpenAI OAuth missing 'model.request' scope — GPT-5.5 falls back silently |
| 📝&nbsp;[#90528](https://github.com/openclaw/openclaw/issues/90528) | 0 | Model routing/config | @amoni094 | [Bug]: OpenAI/Codex OAuth Profile Not Attached to Inference Requests |
| 🔀&nbsp;[#90514](https://github.com/openclaw/openclaw/pull/90514) | 0 | Model routing/config | @baskduf | fix(session): clear stale fallback model state on reset |
| 📝&nbsp;[#90508](https://github.com/openclaw/openclaw/issues/90508) | 0 | Local memory/embedding | @joeykrug | memory-core main reindex thrashes, leaks main.sqlite.tmp files, and leaves memory_search paused after repair |
| 🔀&nbsp;[#90500](https://github.com/openclaw/openclaw/pull/90500) | 0 | Model routing/config | @TurboTheTurtle | Fix stale session routes for removed providers |
| 📝&nbsp;[#90471](https://github.com/openclaw/openclaw/issues/90471) | 0 | Model routing/config | @centralpc | [Bug]: Deleted provider session overrides persist in sessions.json — silent financial damage risk |
| 📝&nbsp;[#90466](https://github.com/openclaw/openclaw/issues/90466) | 0 | Local memory/embedding | @mrizzo123 | [Bug]:memory-core dreaming on 2026.6.1: session-corpus contains .jsonl.deleted.* paths; narrative phase writes fallback despite valid prose responses |
| 📝&nbsp;[#90465](https://github.com/openclaw/openclaw/issues/90465) | 0 | OpenAI-compatible/proxy | @jaylfc | Auto-discover models for the generic openai-completions provider from /v1/models |
| 📝&nbsp;[#90462](https://github.com/openclaw/openclaw/issues/90462) | 0 | Local model runtime | @al-osokin | Fallback provider can become pinned in session metadata and trap a chat on unavailable LM Studio model |
| 📝&nbsp;[#90454](https://github.com/openclaw/openclaw/issues/90454) | 0 | Local memory/embedding | @nocode-ananas | active-memory plugin discards verbose sub-agent responses as status=unavailable, surface_error reason=none |
| 🔀&nbsp;[#90453](https://github.com/openclaw/openclaw/pull/90453) | 0 | Local memory/embedding | @849261680 | fix(memory-core): guard searches during safe reindex |
| 🔀&nbsp;[#90451](https://github.com/openclaw/openclaw/pull/90451) | 0 | Model routing/config | @ooiuuii | fix(codex): honor legacy context overrides after OpenAI unification |
| 📝&nbsp;[#90448](https://github.com/openclaw/openclaw/issues/90448) | 0 | Model routing/config | @ooiuuii | Codex context override can fall back to 272k after 2026.6.1 OpenAI route unification |
| 🔀&nbsp;[#90447](https://github.com/openclaw/openclaw/pull/90447) | 0 | Local memory/embedding | @Kailigithub | fix(memory-core): resolve adapter default model for index identity state |
| 📝&nbsp;[#90445](https://github.com/openclaw/openclaw/issues/90445) | 0 | Model routing/config | @openkralle | Control Panel: Add tooltips/clarifying labels for Reasoning and Thinking dropdowns (Config↔UI naming collision) |
| 🔀&nbsp;[#90433](https://github.com/openclaw/openclaw/pull/90433) | 0 | Local memory/embedding | @xiaobao-k8s | fix(memory-core): exclude archived transcripts from Dreaming session corpus |
| 📝&nbsp;[#90420](https://github.com/openclaw/openclaw/issues/90420) | 0 | Model routing/config | @ooiuuii | Codex runtime route is hard to verify after the 2026.6.1 openai-codex migration |
| 📝&nbsp;[#90414](https://github.com/openclaw/openclaw/issues/90414) | 0 | Local memory/embedding | @AS76 | agentmemory__memory_search returns "index metadata is missing" persistently (memory-core manager state cache) |
| 🔀&nbsp;[#90407](https://github.com/openclaw/openclaw/pull/90407) | 0 | Local memory/embedding | @sahibzada-allahyar | fix(memory-lancedb): align apache arrow peer dependency |
| 🔀&nbsp;[#90401](https://github.com/openclaw/openclaw/pull/90401) | 0 | OpenAI-compatible/proxy | @danyurkin | docs(local-models): add Atomic Chat as an OpenAI-compatible local server |
| 🔀&nbsp;[#90397](https://github.com/openclaw/openclaw/pull/90397) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(openai): skip unreadable responses tool schemas<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90383](https://github.com/openclaw/openclaw/pull/90383) | 0 | Local model runtime | @vincentkoc | fix(ollama): skip unreadable tool schemas<br>Assignee: vincentkoc |
| 📝&nbsp;[#90372](https://github.com/openclaw/openclaw/issues/90372) | 0 | Local model runtime | @JsuHod | [Bug]: Ollama cloud model received a 14M-token prompt before OpenClaw detected context overflow |
| 📝&nbsp;[#90361](https://github.com/openclaw/openclaw/issues/90361) | 0 | Local memory/embedding | @AyitLabs | [Bug]:Intermittent memory_search "index metadata is missing" despite valid builtin memory index; likely search/reindex race. Locally hotfixed. |
| 🔀&nbsp;[#90357](https://github.com/openclaw/openclaw/pull/90357) | 0 | Model routing/config | @alkor2000 | fix(agents): resolve compaction model alias before dispatch |
| 🔀&nbsp;[#90356](https://github.com/openclaw/openclaw/pull/90356) | 0 | Model routing/config | @sovushik | fix(status): use legacy Codex OAuth profiles for OpenAI usage |
| 📝&nbsp;[#90349](https://github.com/openclaw/openclaw/issues/90349) | 0 | Model routing/config | @AungMyoKyaw | Feature: Context Budget/Compactor — intelligent prompt slimming for small-context models |
| 📝&nbsp;[#90342](https://github.com/openclaw/openclaw/issues/90342) | 0 | Local model runtime | @AungMyoKyaw | Feature: Model Cookbook — hardware-aware model recommendations with one-click download/serve |
| 📝&nbsp;[#90340](https://github.com/openclaw/openclaw/issues/90340) | 0 | Model routing/config | @toruvieI | [Bug]: Auto-compaction does not resolve compaction model aliases before dispatch |
| 🔀&nbsp;[#90331](https://github.com/openclaw/openclaw/pull/90331) | 0 | Model routing/config | @Daozheyuanxi | fix(agents): harden gateway config self-edits |
| 🔀&nbsp;[#90330](https://github.com/openclaw/openclaw/pull/90330) | 0 | OpenAI-compatible/proxy | @sercada | Fix ChatGPT Codex streams without content-type |
| 🔀&nbsp;[#90328](https://github.com/openclaw/openclaw/pull/90328) | 0 | Model routing/config | @ooiuuii | Expose model picker agent runtimes |
| 🔀&nbsp;[#90323](https://github.com/openclaw/openclaw/pull/90323) | 0 | Local memory/embedding | @googlerest | fix(memory): replace node:sqlite with better-sqlite3 to enable sqlite-vec on macOS |
| 📝&nbsp;[#90313](https://github.com/openclaw/openclaw/issues/90313) | 0 | Local memory/embedding | @Adam-Researchh | Dreaming session-corpus: cron classification doesn't follow subagent parentage; archived (`.deleted`/`.reset`) transcripts re-ingested |
| 📝&nbsp;[#90302](https://github.com/openclaw/openclaw/issues/90302) | 0 | Model routing/config | @Walliiee | [Feature]: Expose --fallbacks on openclaw cron create/edit |
| 📝&nbsp;[#90295](https://github.com/openclaw/openclaw/issues/90295) | 0 | Local memory/embedding | @allenhurff | memory-lancedb 2026.6.1 fails to install: apache-arrow 21.1.0 conflicts with @lancedb/lancedb 0.30.0 peer range |
| 📝&nbsp;[#90292](https://github.com/openclaw/openclaw/issues/90292) | 0 | Local memory/embedding | @FerrumLogic | [Bug] Dreaming narrative writes fallback snippets despite subagent generating valid poems |
| 🔀&nbsp;[#90291](https://github.com/openclaw/openclaw/pull/90291) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(providers): guard OpenAI web search tool detection<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90289](https://github.com/openclaw/openclaw/pull/90289) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(providers): skip unreadable Anthropic payload tool schemas<br>Assignee: vincentkoc |
| 📝&nbsp;[#90288](https://github.com/openclaw/openclaw/issues/90288) | 0 | OpenAI-compatible/proxy | @Lvan185 | [Bug]: Non-Anthropic models output tool calls as plain text '[tool: exec]' instead of tool_use blocks |
| 🔀&nbsp;[#90286](https://github.com/openclaw/openclaw/pull/90286) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(providers): skip unreadable OpenAI responses tool schemas<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90283](https://github.com/openclaw/openclaw/pull/90283) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(providers): skip unreadable OpenAI completion tool schemas<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90278](https://github.com/openclaw/openclaw/pull/90278) | 0 | Model/provider behavior | @vincentkoc | fix(providers): skip unreadable Anthropic tool schemas<br>Assignee: vincentkoc |
| 📝&nbsp;[#90277](https://github.com/openclaw/openclaw/issues/90277) | 0 | Model routing/config | @Kvikkulf | gateway install --force drops MINIMAX_API_KEY from service-env despite managed keys list |
| 📝&nbsp;[#90276](https://github.com/openclaw/openclaw/issues/90276) | 0 | Local/media model provider | @WilhelminaVonHunt | TTS timeoutMs hard cap of 120000ms (120s) too low for local TTS models — silent fallback to default provider |
| 🔀&nbsp;[#90249](https://github.com/openclaw/openclaw/pull/90249) | 0 | Model/provider behavior | @vincentkoc | fix(providers): skip unreadable Google tool schemas<br>Assignee: vincentkoc |
| 📝&nbsp;[#90243](https://github.com/openclaw/openclaw/issues/90243) | 0 | Model routing/config | @silvesterxm | feat(llm/google-vertex): Support physical model mapping/aliasing to support Google's Priority and Flex PayGo tiers |
| 🔀&nbsp;[#90234](https://github.com/openclaw/openclaw/pull/90234) | 0 | Model routing/config | @ferminquant | fix(agents): filter unresolved model registry rows |
| 🔀&nbsp;[#90206](https://github.com/openclaw/openclaw/pull/90206) | 0 | Model routing/config | @mushuiyu886 | Fix Bedrock aws-sdk compaction auth |
| 🔀&nbsp;[#90200](https://github.com/openclaw/openclaw/pull/90200) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(agents): guard OpenAI strict tool diagnostics<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90196](https://github.com/openclaw/openclaw/pull/90196) | 0 | Local/media model provider | @theashbhat | feat(ios): Add Piper TTS as on-device voice engine option |
| 📝&nbsp;[#90193](https://github.com/openclaw/openclaw/issues/90193) | 0 | OpenAI-compatible/proxy | @jalehman | Refactor duplicate Codex Responses paths for agent turns and llm.complete |
| 📝&nbsp;[#90170](https://github.com/openclaw/openclaw/issues/90170) | 0 | Open-weight/provider behavior | @1240981163-lab | [Bug]: Possible token/cost regression after OpenClaw v2026.5.28 with DeepSeek v4-pro |
| 📝&nbsp;[#90139](https://github.com/openclaw/openclaw/issues/90139) | 0 | Model/provider behavior | @PriceNing | dropThinkingBlocks sanitizer: short text replies shown as [assistant reasoning omitted] in TUI/webchat/WeChat |
| 🔀&nbsp;[#90130](https://github.com/openclaw/openclaw/pull/90130) | 0 | Model routing/config | @vincentkoc | fix(auth): guard preferred provider metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90125](https://github.com/openclaw/openclaw/pull/90125) | 0 | Model routing/config | @bladin | fix(embedded-runner): distinguish model initialization errors from assistant execution errors |
| 🔀&nbsp;[#90117](https://github.com/openclaw/openclaw/pull/90117) | 0 | Local memory/embedding | @arkyu2077 | fix: skip qmd zero-hit sync retry in memory_search |
| 🔀&nbsp;[#90112](https://github.com/openclaw/openclaw/pull/90112) | 0 | Model routing/config | @vincentkoc | fix(commands): guard provider catalog aliases<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90109](https://github.com/openclaw/openclaw/pull/90109) | 0 | Model routing/config | @vincentkoc | fix(commands): guard manifest catalog filters<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90107](https://github.com/openclaw/openclaw/pull/90107) | 0 | Model routing/config | @vincentkoc | fix(commands): guard model provider aliases<br>Assignee: vincentkoc |
| 📝&nbsp;[#90094](https://github.com/openclaw/openclaw/issues/90094) | 0 | OpenAI-compatible/proxy | @xneone | openai-responses transport sends null content, rejected by strict providers (400 schema error) |
| 📝&nbsp;[#90093](https://github.com/openclaw/openclaw/issues/90093) | 0 | OpenAI-compatible/proxy | @richardmqq | openai-chatgpt-responses native replay sends encrypted reasoning and breaks next turn with invalid_encrypted_content |
| 🔀&nbsp;[#90085](https://github.com/openclaw/openclaw/pull/90085) | 0 | Model routing/config | @vincentkoc | fix(gateway): guard model pricing metadata<br>Assignee: vincentkoc |
| 📝&nbsp;[#90082](https://github.com/openclaw/openclaw/issues/90082) | 0 | Local memory/embedding | @ryswork1993 | [Bug] active-memory circuit breaker too aggressive; fallback prompt pollutes main session (v2026.6.1) |
| 🔀&nbsp;[#90077](https://github.com/openclaw/openclaw/pull/90077) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard provider discovery credential metadata<br>Assignee: vincentkoc |
| 📝&nbsp;[#90074](https://github.com/openclaw/openclaw/issues/90074) | 0 | Model routing/config | @holgergruenhagen | OpenAI image generation uses direct API-key route instead of Codex OAuth when explicit provider config exists |
| 🔀&nbsp;[#90073](https://github.com/openclaw/openclaw/pull/90073) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard metadata snapshot owner rows<br>Assignee: vincentkoc |
| 📝&nbsp;[#90049](https://github.com/openclaw/openclaw/issues/90049) | 0 | Local model runtime | @zenassist26-create | Heartbeat sessions report 'assistant turn failed before producing content' on model initialization failure |
| 📝&nbsp;[#90042](https://github.com/openclaw/openclaw/issues/90042) | 0 | Local memory/embedding | @Bizman365 | Gateway memory_search index stuck dirty: provider.model empty during boot overwrites correct index identity |
| 📝&nbsp;[#90036](https://github.com/openclaw/openclaw/issues/90036) | 0 | Model routing/config | @nexic-hh | Session model route drifts from openai/gpt-5.5 to openai-codex/gpt-5.5 with native Codex runtime |
| 🔀&nbsp;[#90033](https://github.com/openclaw/openclaw/pull/90033) | 0 | OpenAI-compatible/proxy | @obuchowski | fix(llm): apply model.compat.sendSessionAffinityHeaders at openai-transport-stream |
| 🔀&nbsp;[#90030](https://github.com/openclaw/openclaw/pull/90030) | 0 | Local memory/embedding | @sahibzada-allahyar | fix(memory-core): skip qmd zero-hit search sync |
| 📝&nbsp;[#90023](https://github.com/openclaw/openclaw/issues/90023) | 0 | Local memory/embedding | @ruben2000de | QMD memory_search zero-hit queries trigger synchronous force sync and stall interactive turns |
| 🔀&nbsp;[#90019](https://github.com/openclaw/openclaw/pull/90019) | 0 | Local memory/embedding | @sahibzada-allahyar | fix(memory-search): default periodic sync fallback |
| 📝&nbsp;[#90015](https://github.com/openclaw/openclaw/issues/90015) | 0 | Open-weight/provider behavior | @SebTardif | DSML recovery buffer grows without bound on unclosed DSML blocks |
| 🔀&nbsp;[#89983](https://github.com/openclaw/openclaw/pull/89983) | 0 | Model/provider behavior | @vincentkoc | fix(agents): isolate provider attribution manifest rows<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89981](https://github.com/openclaw/openclaw/pull/89981) | 0 | Model/provider behavior | @mycarrysun | fix(diagnostics-otel): keep full model id on spans instead of collapsing to "unknown" |
| 🔀&nbsp;[#89979](https://github.com/openclaw/openclaw/pull/89979) | 0 | Model routing/config | @vincentkoc | fix(config): isolate provider auto-enable rows<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89972](https://github.com/openclaw/openclaw/pull/89972) | 0 | Local memory/embedding | @RomneyDa | feat(watch): replace chokidar dep with in-repo chokidar-slim + async add API |
| 🔀&nbsp;[#89961](https://github.com/openclaw/openclaw/pull/89961) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard manifest suppression metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89948](https://github.com/openclaw/openclaw/pull/89948) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard plugin id alias metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89946](https://github.com/openclaw/openclaw/pull/89946) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard provider policy metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89945](https://github.com/openclaw/openclaw/pull/89945) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard provider discovery metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89940](https://github.com/openclaw/openclaw/pull/89940) | 0 | Model routing/config | @vincentkoc | fix(models): guard manifest model id metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89936](https://github.com/openclaw/openclaw/pull/89936) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard model suppression metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89933](https://github.com/openclaw/openclaw/pull/89933) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard synthetic auth metadata<br>Assignee: vincentkoc |
| 📝&nbsp;[#89927](https://github.com/openclaw/openclaw/issues/89927) | 0 | Model routing/config | @A1fred-AI | Fallback sessions don't terminate parent lane → concurrent orchestrator lanes, duplicate billed subagent dispatches, and wedged sessions |
| 🔀&nbsp;[#89917](https://github.com/openclaw/openclaw/pull/89917) | 0 | Model routing/config | @vincentkoc | fix(agents): guard provider auth alias metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89905](https://github.com/openclaw/openclaw/pull/89905) | 0 | Model routing/config | @dwc1997 | fix(hooks): honor hook-level model override for session-memory slug generation |
| 🔀&nbsp;[#89899](https://github.com/openclaw/openclaw/pull/89899) | 0 | Local/media model provider | @zhangguiping-xydt | fix #89425: [Bug]: Missing extensions/speech-core/ in npm tarball (v2026.5.28) — "Unable to resolve bundled plugin public surface speech-core/runtime-api.js" |
| 🔀&nbsp;[#89880](https://github.com/openclaw/openclaw/pull/89880) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard model catalog registration metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89818](https://github.com/openclaw/openclaw/pull/89818) | 0 | Model/provider behavior | @masatohoshino | fix(providers): forward stop sequences in bundled Anthropic transports |
| 📝&nbsp;[#89758](https://github.com/openclaw/openclaw/issues/89758) | 0 | Model routing/config | @Enominera | [Bug] overloaded_error triggers immediate rotate_profile without retry, causing cascade fallback on transient provider overload |
| 🔀&nbsp;[#89730](https://github.com/openclaw/openclaw/pull/89730) | 0 | Local model runtime | @vincentkoc | fix(agents): guard lean tool name reads<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89716](https://github.com/openclaw/openclaw/pull/89716) | 0 | OpenAI-compatible/proxy | @masatohoshino | fix(providers): strip cache-boundary marker from non-Anthropic prompts |
| 🔀&nbsp;[#89703](https://github.com/openclaw/openclaw/pull/89703) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(openai): guard responses tool payload names<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89669](https://github.com/openclaw/openclaw/pull/89669) | 0 | Model/provider behavior | @vincentkoc | fix(agents): contain provider schema hook failures<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89665](https://github.com/openclaw/openclaw/pull/89665) | 0 | Open-weight/provider behavior | @vincentkoc | fix(plugin-sdk): guard provider tool schema walks<br>Assignee: vincentkoc |
| 📝&nbsp;[#89664](https://github.com/openclaw/openclaw/issues/89664) | 0 | Model routing/config | @Stache73 | [Bug] secrets audit / doctor falsely flags static routing header as plaintext secret |
| 🔀&nbsp;[#89657](https://github.com/openclaw/openclaw/pull/89657) | 0 | Model routing/config | @vincentkoc | fix(plugins): harden installed index stale metadata<br>Assignee: vincentkoc |
| 📝&nbsp;[#89655](https://github.com/openclaw/openclaw/issues/89655) | 0 | Model routing/config | @kasanuowa | [Bug]: `NODE_USE_SYSTEM_CA=1` breaks `openai-codex` auth/keychain paths on macOS and can fail fresh runtime launch with `SecItemCopyMatching failed -50` |
| 🔀&nbsp;[#89647](https://github.com/openclaw/openclaw/pull/89647) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard startup manifest channels<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89646](https://github.com/openclaw/openclaw/pull/89646) | 0 | Model routing/config | @vincentkoc | fix(model-catalog): guard model id policies<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89644](https://github.com/openclaw/openclaw/pull/89644) | 0 | Model routing/config | @vincentkoc | fix(model-catalog): skip unreadable catalog records<br>Assignee: vincentkoc |
| 📝&nbsp;[#89633](https://github.com/openclaw/openclaw/issues/89633) | 0 | Model routing/config | @goslingmanagment | Codex turn fails with generic Telegram fallback when invalid image tool model is configured, leaving child agent orphaned on full stdout pipe |
| 🔀&nbsp;[#89624](https://github.com/openclaw/openclaw/pull/89624) | 0 | Local model runtime | @vincentkoc | fix(ollama): guard tool schema normalization<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89618](https://github.com/openclaw/openclaw/pull/89618) | 0 | Local model runtime | @danyurkin | feat(atomicchat): add Atomic Chat as a bundled local provider |
| 📝&nbsp;[#89617](https://github.com/openclaw/openclaw/issues/89617) | 0 | Local model runtime | @danyurkin | Add Atomic Chat as a bundled local provider (OpenAI-compatible, 127.0.0.1:1337) |
| 🔀&nbsp;[#89602](https://github.com/openclaw/openclaw/pull/89602) | 0 | Model routing/config | @zerone0x | fix(status): show effective channel model override |
| 🔀&nbsp;[#89584](https://github.com/openclaw/openclaw/pull/89584) | 0 | Local memory/embedding | @ubehera | feat(memory-core): optional cross-encoder rerank stage for memory search |
| 🔀&nbsp;[#89571](https://github.com/openclaw/openclaw/pull/89571) | 0 | Open-weight/provider behavior | @vincentkoc | fix(provider): harden provider tool schema hooks<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89558](https://github.com/openclaw/openclaw/pull/89558) | 0 | Model routing/config | @steipete | docs: document embedded compaction context contracts |
| 📝&nbsp;[#89551](https://github.com/openclaw/openclaw/issues/89551) | 0 | Model routing/config | @syncword | [Bug]: session-memory hook model config ignored for LLM slug generation |
| 📝&nbsp;[#89549](https://github.com/openclaw/openclaw/issues/89549) | 0 | Model routing/config | @himynameisluna | [Bug]: sessions_spawn accepts subagent runs that later fail on a different auth/provider path than the healthy main session |
| 🔀&nbsp;[#89543](https://github.com/openclaw/openclaw/pull/89543) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(agents): harden OpenAI strict schema inspection<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89535](https://github.com/openclaw/openclaw/pull/89535) | 0 | Model routing/config | @kesslerio | test(codex): cover binds without model overrides |
| 📝&nbsp;[#89534](https://github.com/openclaw/openclaw/issues/89534) | 0 | Model routing/config | @kesslerio | [Bug]: /codex bind without --model can fail with defaultModel ReferenceError |
| 📝&nbsp;[#89532](https://github.com/openclaw/openclaw/issues/89532) | 0 | Model routing/config | @tess020126-cmyk | Bug: /status does not show effective model from channels.modelByChannel |
| 📝&nbsp;[#89531](https://github.com/openclaw/openclaw/issues/89531) | 0 | OpenAI-compatible/proxy | @pigfoot | [Bug] amazon-bedrock-openai / openai-responses: streaming emits multiple incremental final_answer phases, causing duplicate channel messages |
| 📝&nbsp;[#89522](https://github.com/openclaw/openclaw/issues/89522) | 0 | Model routing/config | @Gausons | [Feature]: Inherit requester session model for native subagents |
| 📝&nbsp;[#89509](https://github.com/openclaw/openclaw/issues/89509) | 0 | Local/media model provider | @WilhelminaVonHunt | Bug: [[tts:text]] tag content not passed to TTS engine — surrounding text sent instead |
| 📝&nbsp;[#89477](https://github.com/openclaw/openclaw/issues/89477) | 0 | Local memory/embedding | @ubehera | [Feature]: optional cross-encoder rerank stage for memory search |
| 📝&nbsp;[#89476](https://github.com/openclaw/openclaw/issues/89476) | 0 | OpenAI-compatible/proxy | @simon998888 | feat(onboard): install-daemon UI support for custom provider setup |
| 📝&nbsp;[#89473](https://github.com/openclaw/openclaw/issues/89473) | 0 | Model/provider behavior | @zax0rz | [Bug]: Reasoning tokens leak to chat channels when models stream interleaved text/thinking blocks |
| 🔀&nbsp;[#89469](https://github.com/openclaw/openclaw/pull/89469) | 0 | Model routing/config | @Gausons | feat(agents): inherit requester model for subagents |
| 🔀&nbsp;[#89453](https://github.com/openclaw/openclaw/pull/89453) | 0 | Model/provider behavior | @xianshishan | fix(android): filter thinking and reasoning blocks from chat message display |
| 🔀&nbsp;[#89451](https://github.com/openclaw/openclaw/pull/89451) | 0 | Model/provider behavior | @vincentkoc | fix(google): quarantine invalid extension tool schemas |
| 📝&nbsp;[#89444](https://github.com/openclaw/openclaw/issues/89444) | 0 | Local memory/embedding | @Josephur | Dreaming promotion still writes raw/junk data into MEMORY.md (regression from #67580) |
| 🔀&nbsp;[#89443](https://github.com/openclaw/openclaw/pull/89443) | 0 | Local memory/embedding | @Alix-007 | fix(active-memory): drop assistant chitchat boilerplate from recall summaries |
| 🔀&nbsp;[#89437](https://github.com/openclaw/openclaw/pull/89437) | 0 | Model/provider behavior | @vincentkoc | fix(google): quarantine invalid tool declarations |
| 📝&nbsp;[#89431](https://github.com/openclaw/openclaw/issues/89431) | 0 | Local/media model provider | @guzzijones | [Bug]: macos say command in daemon not output to speakers |
| 🔀&nbsp;[#89429](https://github.com/openclaw/openclaw/pull/89429) | 0 | Open-weight/provider behavior | @vincentkoc | fix(plugin-sdk): quarantine invalid provider tool schemas<br>Assignee: vincentkoc |
| 📝&nbsp;[#89425](https://github.com/openclaw/openclaw/issues/89425) | 0 | Local/media model provider | @ant1b0t | [Bug]: Missing extensions/speech-core/ in npm tarball (v2026.5.28) — "Unable to resolve bundled plugin public surface speech-core/runtime-api.js" |
| 🔀&nbsp;[#89413](https://github.com/openclaw/openclaw/pull/89413) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(openai): quarantine unreadable projected tools<br>Assignee: vincentkoc |
| 📝&nbsp;[#89392](https://github.com/openclaw/openclaw/issues/89392) | 0 | Open-weight/provider behavior | @xiaoyaolanyun | Long streaming model responses cause event loop starvation |
| 🔀&nbsp;[#89381](https://github.com/openclaw/openclaw/pull/89381) | 0 | Model/provider behavior | @vincentkoc | fix(plugin-sdk): guard provider tool schema traversal<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89378](https://github.com/openclaw/openclaw/pull/89378) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(agents): guard OpenAI tool schema conversion<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89371](https://github.com/openclaw/openclaw/pull/89371) | 0 | Local memory/embedding | @yelog | fix(memory): clean stale short-term temp files |
| 📝&nbsp;[#89362](https://github.com/openclaw/openclaw/issues/89362) | 0 | Local memory/embedding | @BomBastikDE | Expose batchEmbed from the Ollama memory adapter so batch indexing can be enabled |
| 🔀&nbsp;[#89360](https://github.com/openclaw/openclaw/pull/89360) | 0 | Local memory/embedding | @jalehman | refactor: add QMD session artifact identity mapping |
| 🔀&nbsp;[#89353](https://github.com/openclaw/openclaw/pull/89353) | 0 | Model/provider behavior | @vincentkoc | fix(plugin-sdk): guard provider schema inspection<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89348](https://github.com/openclaw/openclaw/pull/89348) | 0 | Local memory/embedding | @jalehman | refactor: add memory session sync identity API |
| 🔀&nbsp;[#89334](https://github.com/openclaw/openclaw/pull/89334) | 0 | Local memory/embedding | @AdrianIp0204 | docs: note active memory timeout circuit breaker |
| 🔀&nbsp;[#89324](https://github.com/openclaw/openclaw/pull/89324) | 0 | Model/provider behavior | @vincentkoc | fix(xai): skip unreadable tool payload entries |
| 🔀&nbsp;[#89322](https://github.com/openclaw/openclaw/pull/89322) | 0 | Local model runtime | @vincentkoc | fix(ollama): skip unreadable tool descriptors |
| 🔀&nbsp;[#89317](https://github.com/openclaw/openclaw/pull/89317) | 0 | Model/provider behavior | @vincentkoc | fix(bedrock): guard tool config projection |
| 📝&nbsp;[#89300](https://github.com/openclaw/openclaw/issues/89300) | 0 | Model/provider behavior | @Enominera | model-fetch logs lost in v2026.5.28 - degraded from log.info to log.debug behind env flag |
| 📝&nbsp;[#89278](https://github.com/openclaw/openclaw/issues/89278) | 0 | Model routing/config | @kopl-blip | [Bug]: Codex OAuth refresh succeeds but cron/heartbeat fail with 10s auth refresh timeout |
| 🔀&nbsp;[#89273](https://github.com/openclaw/openclaw/pull/89273) | 0 | Model/provider behavior | @vincentkoc | fix(doctor): sanitize provider catalog findings |
| 📝&nbsp;[#89265](https://github.com/openclaw/openclaw/issues/89265) | 0 | Local model runtime | @CobraSoftware | [Feature]: More local providers |
| 📝&nbsp;[#89264](https://github.com/openclaw/openclaw/issues/89264) | 0 | Local memory/embedding | @C1-BA-B1-F3 | [Bug]: Dreaming deep promotion biased to stale 3-5 day old content; REM produces repetitive meta-themes; promotion gates bypassed via phase-signal boost |
| 📝&nbsp;[#89259](https://github.com/openclaw/openclaw/issues/89259) | 0 | Model/provider behavior | @swiser-nexa | EmbeddedAttemptSessionTakeoverError fires at ~120s on long Bedrock streams (fence whitelist too narrow?) |
| 📝&nbsp;[#89233](https://github.com/openclaw/openclaw/issues/89233) | 0 | Local model runtime | @CameronWeller | [Bug]: Default models.providers.lmstudio.apiKey ships as plaintext placeholder 'lm-studio' - triggers false-positive security audit warning |
| 🔀&nbsp;[#89229](https://github.com/openclaw/openclaw/pull/89229) | 0 | Model/provider behavior | @vincentkoc | fix(llm): guard Anthropic provider tool descriptors |
| 🔀&nbsp;[#89221](https://github.com/openclaw/openclaw/pull/89221) | 0 | Model/provider behavior | @vincentkoc | fix(agents): guard Anthropic tool descriptors |
| 📝&nbsp;[#89202](https://github.com/openclaw/openclaw/issues/89202) | 0 | Model/provider behavior | @aaronescobar09 | [Bug]: Telegram heavy turns can cause incomplete codex-app server turn around compaction, including under OpenClaw runtime. |
| 📝&nbsp;[#89198](https://github.com/openclaw/openclaw/issues/89198) | 0 | Local/media model provider | @talentshf | Feature Request: Support Gateway TTS/STT in iOS App |
| 📝&nbsp;[#89197](https://github.com/openclaw/openclaw/issues/89197) | 0 | Model routing/config | @yangiit | Gateway agent run failure with no model reachable: chat.history returns incomplete state, Control UI clears conversation history |
| 📝&nbsp;[#89196](https://github.com/openclaw/openclaw/issues/89196) | 0 | Local memory/embedding | @yangiit | Dreaming REM: sub-session visible in session switcher + narrative diary fails to write to DREAMS.md |
| 🔀&nbsp;[#89194](https://github.com/openclaw/openclaw/pull/89194) | 0 | Model routing/config | @Kailigithub | fix: include name field in model_not_found remediation hint |
| 🔀&nbsp;[#89190](https://github.com/openclaw/openclaw/pull/89190) | 0 | Model/provider behavior | @lidge-jun | feat(xai): add grok-composer-2.5-fast model |
| 🔀&nbsp;[#89183](https://github.com/openclaw/openclaw/pull/89183) | 0 | Local model runtime | @ferminquant | fix(tui): keep local slash commands out of model prompts |
| 📝&nbsp;[#89173](https://github.com/openclaw/openclaw/issues/89173) | 0 | Local memory/embedding | @DerekEXS | External plugin tools (memory_store, memory_recall, etc.) not routed/exposed to the Agent in v2026.5.27+ |
| 📝&nbsp;[#89167](https://github.com/openclaw/openclaw/issues/89167) | 0 | Model routing/config | @devin-ai-integration[bot] | Session in status:failed remains bound as agent:main:main, crashing next TUI launch |
| 📝&nbsp;[#89164](https://github.com/openclaw/openclaw/issues/89164) | 0 | Model/provider behavior | @devin-ai-integration[bot] | Completed model responses occasionally do not persist to session jsonl despite trajectory recording success |
| 🔀&nbsp;[#89160](https://github.com/openclaw/openclaw/pull/89160) | 0 | Model/provider behavior | @joelnishanth | fix(agents): detect truncated API responses to prevent silent session hang |
| 🔀&nbsp;[#89155](https://github.com/openclaw/openclaw/pull/89155) | 0 | Open-weight/provider behavior | @Alex-vonAllmen | feat(openrouter): forward OpenClaw session id as session_id |
| 📝&nbsp;[#89147](https://github.com/openclaw/openclaw/issues/89147) | 0 | Model/provider behavior | @scipher888 | Native hook relay starves mid-turn after long model-thinking gap (renewal loop tool-call-driven) |
| 🔀&nbsp;[#89133](https://github.com/openclaw/openclaw/pull/89133) | 0 | Model routing/config | @VACInc | Restore GPT-5.3 Codex Spark OAuth routing |
| 🔀&nbsp;[#89118](https://github.com/openclaw/openclaw/pull/89118) | 0 | Open-weight/provider behavior | @LiLan0125 | fix(outbound): sanitize message.send arguments to prevent runtime scaffolding leaks |
| 🔀&nbsp;[#89117](https://github.com/openclaw/openclaw/pull/89117) | 0 | Local memory/embedding | @abel-zer0 | Support Gemini Embedding 2 GA |
| 📝&nbsp;[#89114](https://github.com/openclaw/openclaw/issues/89114) | 0 | Open-weight/provider behavior | @superandylin | Minimax M3: /think menu missing xhigh, adaptive, max levels (provider profile limitation) |
| 📝&nbsp;[#89100](https://github.com/openclaw/openclaw/issues/89100) | 0 | Open-weight/provider behavior | @bobgitmcgrath | Sanitise outbound message.send tool arguments to prevent runtime scaffolding leak (FM-3) and chat_id routing bleed (FM-2) on weaker models |
| 🔀&nbsp;[#89088](https://github.com/openclaw/openclaw/pull/89088) | 0 | Model routing/config | @charles-openclaw | test(gateway): cover rollover model override preservation |
| 📝&nbsp;[#89087](https://github.com/openclaw/openclaw/issues/89087) | 0 | Model routing/config | @pitbuild | Bug: Session model override lost on UTC midnight rollover |
| 📝&nbsp;[#89051](https://github.com/openclaw/openclaw/issues/89051) | 0 | Local model runtime | @ArthurusDent | [Bug]: Embedded agent session silently hangs after auto-compaction with no error logging or recovery |
| 🔀&nbsp;[#89040](https://github.com/openclaw/openclaw/pull/89040) | 0 | Local model runtime | @Jerry-Xin | perf: avoid event-loop stall during embedded_run bootstrap-context |
| 🔀&nbsp;[#89039](https://github.com/openclaw/openclaw/pull/89039) | 0 | OpenAI-compatible/proxy | @Jerry-Xin | fix: prevent silent message loss from EmbeddedAttemptSessionTakeoverError |
| 🔀&nbsp;[#89029](https://github.com/openclaw/openclaw/pull/89029) | 0 | Model routing/config | @charles-openclaw | fix(cli): accept empty Claude end turns |
| 🔀&nbsp;[#89016](https://github.com/openclaw/openclaw/pull/89016) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(agents): guard OpenAI transport tool descriptors |
| 🔀&nbsp;[#89013](https://github.com/openclaw/openclaw/pull/89013) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(agents): materialize OpenAI tool schemas |
| 🔀&nbsp;[#88977](https://github.com/openclaw/openclaw/pull/88977) | 0 | Model routing/config | @vincentkoc | fix(agents): tolerate provider tool schema hook failures |
| 🔀&nbsp;[#88959](https://github.com/openclaw/openclaw/pull/88959) | 0 | Model routing/config | @vincentkoc | fix(plugins): ignore throwing provider runtime hooks |
| 🔀&nbsp;[#88950](https://github.com/openclaw/openclaw/pull/88950) | 0 | Model routing/config | @vincentkoc | fix(plugins): ignore throwing provider policy hooks |
| 🔀&nbsp;[#88931](https://github.com/openclaw/openclaw/pull/88931) | 0 | Local model runtime | @vincentkoc | fix(agents): cap tool search fanout in lean mode |
| 📝&nbsp;[#88907](https://github.com/openclaw/openclaw/issues/88907) | 0 | Open-weight/provider behavior | @ivannin | Chronic agent failures on Telegram - LLM timeouts before configured timeout + silent incomplete turns + dead fallbacks (OpenRouter/DeepSeek+V4-Flash, v2026.5.28) |
| 🔀&nbsp;[#88906](https://github.com/openclaw/openclaw/pull/88906) | 0 | Model routing/config | @keshavbotagent | fix(openai): allow Codex Spark via harness |
| 🔀&nbsp;[#88905](https://github.com/openclaw/openclaw/pull/88905) | 0 | Local memory/embedding | @iFiras-Max1 | feat(dreaming): expose shadow-trial scoring in reports |
| 📝&nbsp;[#88902](https://github.com/openclaw/openclaw/issues/88902) | 0 | Model routing/config | @khalil-omer | [Bug]: Codex OAuth /btw still falls back to OpenAI Responses after /new |
| 🔀&nbsp;[#88887](https://github.com/openclaw/openclaw/pull/88887) | 0 | Local memory/embedding | @potterdigital | fix(memory-core): don't run the LLM reranker in vsearch/search modes |
| 🔀&nbsp;[#88884](https://github.com/openclaw/openclaw/pull/88884) | 0 | Local model runtime | @vincentkoc | fix(agents): trim web tools in lean mode |
| 🔀&nbsp;[#88881](https://github.com/openclaw/openclaw/pull/88881) | 0 | Local model runtime | @vincentkoc | fix(agents): trim media tools in lean mode |
| 🔀&nbsp;[#88880](https://github.com/openclaw/openclaw/pull/88880) | 0 | Model routing/config | @vincentkoc | fix(agents): project nullable tool schemas for providers |
| 🔀&nbsp;[#88878](https://github.com/openclaw/openclaw/pull/88878) | 0 | Model routing/config | @vincentkoc | fix(agents): project cron tool schemas for providers |
| 🔀&nbsp;[#88869](https://github.com/openclaw/openclaw/pull/88869) | 0 | Open-weight/provider behavior | @NianJiuZst | Add MiniMax M3 support to the bundled MiniMax provider |
| 📝&nbsp;[#88868](https://github.com/openclaw/openclaw/issues/88868) | 0 | Open-weight/provider behavior | @NianJiuZst | Add MiniMax M3 support to the bundled MiniMax provider |
| 📝&nbsp;[#88864](https://github.com/openclaw/openclaw/issues/88864) | 0 | Local memory/embedding | @MarsCNS | [Bug]: `memory-wiki` bridge imports all workspace artifacts into shared vault, causing `path-mismatch` error |
| 🔀&nbsp;[#88837](https://github.com/openclaw/openclaw/pull/88837) | 0 | Model routing/config | @charles-openclaw | fix(agent): use static catalog for skip-agent model resolution |
| 🔀&nbsp;[#88789](https://github.com/openclaw/openclaw/pull/88789) | 0 | Local model runtime | @vincentkoc | feat(agents): auto-trim lean local tools |
| 🔀&nbsp;[#88754](https://github.com/openclaw/openclaw/pull/88754) | 0 | Open-weight/provider behavior | @Kailigithub | fix(text): normalize CJK/fullwidth quotes in reasoning tag delimiters |
| 🔀&nbsp;[#88748](https://github.com/openclaw/openclaw/pull/88748) | 0 | Model routing/config | @jason-allen-oneal | fix(gemini): bridge OAuth profiles into CLI runtime |
| 🔀&nbsp;[#88709](https://github.com/openclaw/openclaw/pull/88709) | 0 | Model routing/config | @MertBasar0 | fix(auth): cooldown inline api key billing failures |
| 📝&nbsp;[#88707](https://github.com/openclaw/openclaw/issues/88707) | 0 | Model routing/config | @podulator | [Bug] Regression 2026.5.27→2026.5.28: "No API provider registered for api: bedrock-converse-stream" — pi-ai removal breaks Bedrock provider registration; bearer token auth broken |
| 📝&nbsp;[#88679](https://github.com/openclaw/openclaw/issues/88679) | 0 | Model routing/config | @junxuku-byte | [Feature]: Per-Tool Model Routing — route specific tool calls to different models |
| 📝&nbsp;[#88657](https://github.com/openclaw/openclaw/issues/88657) | 0 | Open-weight/provider behavior | @mikefaierberg-byte | Bug: DeepSeek V4 Flash incomplete turn (payloads=0, tools=2, replaySafe=no, stopReason=stop) in 2026.5.27/28 |
| 📝&nbsp;[#88632](https://github.com/openclaw/openclaw/issues/88632) | 0 | Local model runtime | @wangwllu | [Bug]: gateway model-run sessions accumulate until session maxEntries cap |
| 📝&nbsp;[#88616](https://github.com/openclaw/openclaw/issues/88616) | 0 | Model routing/config | @Alex-vonAllmen | [Feature]: Forward session_id to OpenRouter for sticky routing & prompt caching |
| 📝&nbsp;[#88579](https://github.com/openclaw/openclaw/issues/88579) | 0 | Model routing/config | @Goron01 | LLM error: Authorization Not Found - SecretRef apiKey not properly resolved in Gateway |
| 📝&nbsp;[#88562](https://github.com/openclaw/openclaw/issues/88562) | 0 | Model routing/config | @mnowrot | [Bug]: models.json generator writes apiKey as plain string instead of secret-ref object |
| 🔀&nbsp;[#88553](https://github.com/openclaw/openclaw/pull/88553) | 0 | Model routing/config | @yu-xin-c | fix(agents): unblock fallback classification tests |
| 🔀&nbsp;[#88551](https://github.com/openclaw/openclaw/pull/88551) | 0 | Model routing/config | @yu-xin-c | fix(agents): skip auth gate for CLI-owned transport |
| 📝&nbsp;[#88548](https://github.com/openclaw/openclaw/issues/88548) | 0 | Model routing/config | @saju01 | GitHub Copilot: static default model list shadows live entitlement discovery |
| 🔀&nbsp;[#88514](https://github.com/openclaw/openclaw/pull/88514) | 0 | Local model runtime | @vincentkoc | fix(gateway): avoid default provider auth startup prewarm |
| 🔀&nbsp;[#88506](https://github.com/openclaw/openclaw/pull/88506) | 0 | Model routing/config | @kklouzal | feat: add per-agent compaction overrides |
| 📝&nbsp;[#88490](https://github.com/openclaw/openclaw/issues/88490) | 0 | Model routing/config | @edgardoalvarez100 | Session model override from Codex persists in unrelated sessions (e.g. Telegram) |
| 📝&nbsp;[#88457](https://github.com/openclaw/openclaw/issues/88457) | 0 | Open-weight/provider behavior | @ReyesAdrian | [Bug]: opencode-go works via direct infer but fails in embedded agent runtime with session takeover |
| 🔀&nbsp;[#88400](https://github.com/openclaw/openclaw/pull/88400) | 0 | Model routing/config | @Pluviobyte | fix(config): accept overlays for bundled provider aliases |
| 🔀&nbsp;[#88329](https://github.com/openclaw/openclaw/pull/88329) | 0 | Model routing/config | @Knowcheng | fix: user-pinned model falls back to global chain on quota exhaustion |
| 🔀&nbsp;[#88249](https://github.com/openclaw/openclaw/pull/88249) | 0 | Model routing/config | @Darclindy | feat(desktop): add Tauri model setup app |
| 🔀&nbsp;[#88212](https://github.com/openclaw/openclaw/pull/88212) | 0 | Local model runtime | @vincentkoc | feat(agents): auto-trim lean local model tools |
| 📝&nbsp;[#88201](https://github.com/openclaw/openclaw/issues/88201) | 0 | Local model runtime | @adamdksaad-ops | [Bug]: OpenClaw 5.22: ~10 sec per-call inference overhead in infer model run (both --gateway and --local) vs ~1.3 sec direct provider call |
| 🔀&nbsp;[#88181](https://github.com/openclaw/openclaw/pull/88181) | 0 | Local model runtime | @vincentkoc | feat(agents): add strict local model lean profile |
| 🔀&nbsp;[#88098](https://github.com/openclaw/openclaw/pull/88098) | 0 | OpenAI-compatible/proxy | @ericlevine | feat(onboard): add --custom-context-window flag for non-interactive setup |
| 🔀&nbsp;[#88082](https://github.com/openclaw/openclaw/pull/88082) | 0 | Model routing/config | @lit26 | feat(stepfun): add step-3.7-flash model |
| 📝&nbsp;[#88079](https://github.com/openclaw/openclaw/issues/88079) | 0 | Open-weight/provider behavior | @xx1170822819 | [Regression] WebChat: reasoning_content not streamed for Kimi Code & DeepSeek Reasoner — only MiniMax works |
| 🔀&nbsp;[#88078](https://github.com/openclaw/openclaw/pull/88078) | 0 | Local memory/embedding | @gisk0 | fix(active-memory): trim recall prompt envelope |
| 📝&nbsp;[#88077](https://github.com/openclaw/openclaw/issues/88077) | 0 | Local memory/embedding | @gisk0 | [Bug]: Active Memory recall context uses full OpenClaw prompt envelope |
| 📝&nbsp;[#87996](https://github.com/openclaw/openclaw/issues/87996) | 0 | OpenAI-compatible/proxy | @liaoandi | Vertex beta INVALID_ARGUMENT can wedge long Enterprise sessions without actionable recovery |
| 🔀&nbsp;[#87958](https://github.com/openclaw/openclaw/pull/87958) | 0 | Model routing/config | @vincentkoc | fix(agents): scale read output for small contexts |
| 📝&nbsp;[#87957](https://github.com/openclaw/openclaw/issues/87957) | 0 | Model routing/config | @osolmaz | Refactor session model/auth state resolution |
| 🔀&nbsp;[#87955](https://github.com/openclaw/openclaw/pull/87955) | 0 | Local model runtime | @vincentkoc | fix(agents): keep lean tools behind catalog controls |
| 🔀&nbsp;[#87927](https://github.com/openclaw/openclaw/pull/87927) | 0 | Model routing/config | @vincentkoc | fix(agents): cap compaction budgets for small contexts |
| 📝&nbsp;[#87925](https://github.com/openclaw/openclaw/issues/87925) | 0 | Model routing/config | @hoobnn | thinkingLevel: model switch silently downgrades and persists an inherited explicit override |
| 🔀&nbsp;[#87923](https://github.com/openclaw/openclaw/pull/87923) | 0 | Model routing/config | @hoobnn | fix(thinking): keep explicit session thinkingLevel when runtime downgrades (#87740) |
| 🔀&nbsp;[#87895](https://github.com/openclaw/openclaw/pull/87895) | 0 | Open-weight/provider behavior | @vincentkoc | test(agents): broaden small live hosted model matrix |
| 📝&nbsp;[#87876](https://github.com/openclaw/openclaw/issues/87876) | 0 | Model routing/config | @Haderach-Ram | Bug: Bedrock Converse Streaming silently aborts on long-context agent sessions (~6 min timeout, no retry, no fallback) |
| 🔀&nbsp;[#87850](https://github.com/openclaw/openclaw/pull/87850) | 0 | Local model runtime | @vincentkoc | fix(agents): avoid constructing lean local model tools<br>Assignee: vincentkoc |
| 📝&nbsp;[#87816](https://github.com/openclaw/openclaw/issues/87816) | 0 | Local/media model provider | @DoiiarX | feat(tts): xiaomi voicedesign/voiceclone model support |
| 📝&nbsp;[#87763](https://github.com/openclaw/openclaw/issues/87763) | 0 | OpenAI-compatible/proxy | @georgenaz | SSRF guard pinned DNS dispatcher causes model fetch timeouts when autoSelectFamily is enabled |
| 🔀&nbsp;[#87697](https://github.com/openclaw/openclaw/pull/87697) | 0 | Model routing/config | @ferminquant | fix(auth): clear stale provider cooldowns after reauth |
| 📝&nbsp;[#87689](https://github.com/openclaw/openclaw/issues/87689) | 0 | Local memory/embedding | @Countermarch | Dreaming needs supported guard to disable session transcript ingestion during QMD migrations |
| 📝&nbsp;[#87687](https://github.com/openclaw/openclaw/issues/87687) | 0 | Local model runtime | @sonofanton44 | vllm openai-completions streaming parser drops tool_calls when reasoning_content streams first for gpt-oss-120b at large systemPrompt |
| 📝&nbsp;[#87642](https://github.com/openclaw/openclaw/issues/87642) | 0 | Local model runtime | @chrisslee | Expose subagent-control waitForRun timeout as a config knob (hardcoded 30s blocks slow local LLMs) |
| 🔀&nbsp;[#87587](https://github.com/openclaw/openclaw/pull/87587) | 0 | Local model runtime | @vincentkoc | fix(agents): keep exec visible for lean local models |
| 📝&nbsp;[#87586](https://github.com/openclaw/openclaw/issues/87586) | 0 | Local model runtime | @taocwal | [Feature]: Unixsocket Provider plugin |
| 📝&nbsp;[#87466](https://github.com/openclaw/openclaw/issues/87466) | 0 | Local/media model provider | @UrsineBear | [Bug]:Telegram voice delivery is unstable across model runtimes because voice generation depends on model-generated media tags |
| 📝&nbsp;[#87443](https://github.com/openclaw/openclaw/issues/87443) | 0 | Local memory/embedding | @bxf471494973 | sqlite-vec vector search fails on musl-based systems |
| 🔀&nbsp;[#87414](https://github.com/openclaw/openclaw/pull/87414) | 0 | Local model runtime | @ezcoder | [codex] Key llama.cpp sessions for local reuse |
| 📝&nbsp;[#87384](https://github.com/openclaw/openclaw/issues/87384) | 0 | Local/media model provider | @kesslerio | Bug: CLI audio transcription can use progress stdout when transcript file is empty |
| 🔀&nbsp;[#87343](https://github.com/openclaw/openclaw/pull/87343) | 0 | Model routing/config | @riosbotchen-source | feat(cron): surface fallback progress |
| 📝&nbsp;[#87277](https://github.com/openclaw/openclaw/issues/87277) | 0 | Open-weight/provider behavior | @0mlkrizzz655335v | [Feature] Add MiMo-V2.5 to Xiaomi catalog + automatic multimodal routing when DeepSeek V4-Pro is primary model |
| 📝&nbsp;[#87267](https://github.com/openclaw/openclaw/issues/87267) | 0 | Local model runtime | @rogerallen1 | [Bug]: Dream Diary narrative needs separate config for timeout/concurrency or disablement, while keeping dreaming enabled. |
| 📝&nbsp;[#87262](https://github.com/openclaw/openclaw/issues/87262) | 0 | Local model runtime | @huangzeqi | [Bug]: qqbot + ollama + local model: qwen3.5:27b report: error Embedded agent failed before reply: LLM request failed: network connection was interrupted |
| 📝&nbsp;[#87168](https://github.com/openclaw/openclaw/issues/87168) | 0 | Model routing/config | @bek91 | `image` media-understanding tool can bypass configured Codex image route via model overrides and direct OpenAI auto-selection |
| 📝&nbsp;[#87110](https://github.com/openclaw/openclaw/issues/87110) | 0 | Local model runtime | @knight-666 | When calling a VLLM model, the usage page statistics show no data. How can I calculate usage and cost when using VLLM? |
| 📝&nbsp;[#86813](https://github.com/openclaw/openclaw/issues/86813) | 0 | Model routing/config | @pppetertao | `/new` does not clear persisted model override in channel-bound sessions |
| 🔀&nbsp;[#86776](https://github.com/openclaw/openclaw/pull/86776) | 0 | Model routing/config | @kierandotai | fix(models): apply provider policy defaults to inline models |
| 📝&nbsp;[#86773](https://github.com/openclaw/openclaw/issues/86773) | 0 | Local model runtime | @chac4l | Provider auth prewarm can starve gateway event loop and cause sessions.list timeouts after restart |
| 📝&nbsp;[#86752](https://github.com/openclaw/openclaw/issues/86752) | 0 | Local model runtime | @balaji1968-kingler | [Bug]: 2026.5.22 Docker/WSL2 gateway event-loop starvation, 284s provider-auth prewarm, slow Telegram turn, and local RPC timeouts |
| 📝&nbsp;[#86521](https://github.com/openclaw/openclaw/issues/86521) | 0 | OpenAI-compatible/proxy | @mindflarevortx-maker | fix: preserve reasoning_content for DeepSeek models through proxy providers (opencode-native) |
| 📝&nbsp;[#86182](https://github.com/openclaw/openclaw/issues/86182) | 0 | Local model runtime | @rendrag-git | discord/picker: structural 25-option / 5-row / 100-char limits constrain large wildcard configs |
| 📝&nbsp;[#86174](https://github.com/openclaw/openclaw/issues/86174) | 0 | Model routing/config | @rqlangley | [Bug]: WebChat + New Session displays default model but inherits parent's model override |
| 📝&nbsp;[#85684](https://github.com/openclaw/openclaw/issues/85684) | 0 | OpenAI-compatible/proxy | @iFwu | pi-embedded-runner: reasoning-only retry short-circuited in group chats by silentReplyPolicy default |
| 📝&nbsp;[#84918](https://github.com/openclaw/openclaw/issues/84918) | 0 | OpenAI-compatible/proxy | @killo3967 | OpenWebUI image uploads reach image tool as empty image via /v1/chat/completions on 2026.5.18 |
| 📝&nbsp;[#84865](https://github.com/openclaw/openclaw/issues/84865) | 0 | Open-weight/provider behavior | @njuboy11 | user-switched model has no fallback chain, causing session deadlock on provider outage |
| 🔀&nbsp;[#84554](https://github.com/openclaw/openclaw/pull/84554) | 0 | Local memory/embedding | @jetd1 | fix(memory-core): guard builtin fallback after qmd failures |
| 📝&nbsp;[#84217](https://github.com/openclaw/openclaw/issues/84217) | 0 | Local model runtime | @fanispoulinakisai-boop | [Bug]: Heartbeat dispatch delivers free text block alongside message-tool call (chatty non-Codex providers, v2026.5.18) |
| 🔀&nbsp;[#84072](https://github.com/openclaw/openclaw/pull/84072) | 0 | Model routing/config | @wiatrM | Add model fallback circuit breaker |
| 📝&nbsp;[#84070](https://github.com/openclaw/openclaw/issues/84070) | 0 | Local model runtime | @islandpreneur007 | Active Memory embedded runner fails to expose plugin tools when hidden runner is on the DeepSeek provider path |
| 🔀&nbsp;[#83436](https://github.com/openclaw/openclaw/pull/83436) | 0 | Model routing/config | @cael-dandelion-cult | fix(agents): rethrow EmbeddedAttemptSessionTakeoverError before model fallback |
| 📝&nbsp;[#83399](https://github.com/openclaw/openclaw/issues/83399) | 0 | OpenAI-compatible/proxy | @yuzhihui886 | Bug: Tool call loop when assistant generates text + toolCall with openai-completions API |
| 🔀&nbsp;[#83213](https://github.com/openclaw/openclaw/pull/83213) | 0 | Model routing/config | @Derekko-web | fix(gateway): clear live model switch on reset |
| 🔀&nbsp;[#82145](https://github.com/openclaw/openclaw/pull/82145) | 0 | Local model runtime | @cthornsburg | cron: allow retries for local model preflight |
| 📝&nbsp;[#81925](https://github.com/openclaw/openclaw/issues/81925) | 0 | Local memory/embedding | @castigiova | Compaction: `after_compaction` not emitted when `result.compacted:false`; validation: single-quote delimiter trips tool-caller retries |
| 📝&nbsp;[#81835](https://github.com/openclaw/openclaw/issues/81835) | 0 | OpenAI-compatible/proxy | @STLI69 | Bug: thinking parameter format incompatible with Volcengine CodingPlan v3 API |
| 🔀&nbsp;[#80957](https://github.com/openclaw/openclaw/pull/80957) | 0 | OpenAI-compatible/proxy | @chenyanchen | fix: refresh status context window after model switch |
| 📝&nbsp;[#80521](https://github.com/openclaw/openclaw/issues/80521) | 0 | Local model runtime | @wherewolf87 | UI feature request: model picker + drag-to-reorder for primary/fallback model selection in Agents > Overview |
| 🔀&nbsp;[#80418](https://github.com/openclaw/openclaw/pull/80418) | 0 | OpenAI-compatible/proxy | @logicbridgedev | fix(/v1/responses): accept text field on requests for OpenAI SDK 6.x parity |
| 📝&nbsp;[#80336](https://github.com/openclaw/openclaw/issues/80336) | 0 | Local model runtime | @kinerliu | [Bug]: placeholder.openclaw.cloud unreachable on WSL2 with custom gateway port |
| 📝&nbsp;[#80317](https://github.com/openclaw/openclaw/issues/80317) | 0 | OpenAI-compatible/proxy | @vokasug | TTS OpenAI provider: MP3 responseFormat not voice-compatible for Telegram, unlike Edge TTS |
| 🔀&nbsp;[#80033](https://github.com/openclaw/openclaw/pull/80033) | 0 | Open-weight/provider behavior | @wrcno1 | fix(opencode-go): add supportedReasoningEfforts to DeepSeek V4 model entries |
| 📝&nbsp;[#79437](https://github.com/openclaw/openclaw/issues/79437) | 0 | Local memory/embedding | @bp2u | Prebuilt `node-llama-cpp` Windows binaries crash (0xC0000005) on Intel Alder Lake-N (N95) - qmd LLM half unusable |
| 🔀&nbsp;[#79185](https://github.com/openclaw/openclaw/pull/79185) | 0 | Open-weight/provider behavior | @kidding1412 | fix(tts/xiaomi): support Token Plan TTS endpoint |
| 📝&nbsp;[#78091](https://github.com/openclaw/openclaw/issues/78091) | 0 | OpenAI-compatible/proxy | @wurdzy | [Bug]: Open-WebUI creates new session per message instead of reusing persistent session |
| 📝&nbsp;[#75811](https://github.com/openclaw/openclaw/issues/75811) | 0 | Local model runtime | @camerono | [Bug]: `exec` tool schema exposes `security`/`elevated`/`ask` fields as model-controllable; model self-imposes denial |
| 📝&nbsp;[#75312](https://github.com/openclaw/openclaw/issues/75312) | 0 | Local memory/embedding | @xuanmingguo | Bug: wiki_search throws 'sharedMemoryManager.search is not a function' when search.backend=shared and corpus includes memory/all |
| 🔀&nbsp;[#75274](https://github.com/openclaw/openclaw/pull/75274) | 0 | Local model runtime | @davidvv | fix(ollama): per-request URL routing for multi-provider setups |
| 🔀&nbsp;[#75267](https://github.com/openclaw/openclaw/pull/75267) | 0 | Model routing/config | @fancymatt | Fix model picker alias/provider scoped options |
| 📝&nbsp;[#75189](https://github.com/openclaw/openclaw/issues/75189) | 0 | Local model runtime | @camerono | [Bug]: Default `bootstrapMaxChars=20000` + verbose auto-generated bootstrap content degrades tool dispatch on small/mid models |
| 📝&nbsp;[#75187](https://github.com/openclaw/openclaw/issues/75187) | 0 | Local model runtime | @camerono | [Bug]: Auto-generated `AGENTS.md` puts load-bearing tool-use rules at the bottom; head-truncation by `bootstrapMaxChars` strips them |
| 📝&nbsp;[#75040](https://github.com/openclaw/openclaw/issues/75040) | 0 | Local model runtime | @kingkong9817 | [Bug]: extra_body overwriting request payload keys: thinking - framework-level thinking field collision affecting all providers |
| 📝&nbsp;[#75026](https://github.com/openclaw/openclaw/issues/75026) | 0 | OpenAI-compatible/proxy | @mmhzlrj | MiniMax token usage shows 0 in Control UI Usage page (only message count works) |
| 📝&nbsp;[#74900](https://github.com/openclaw/openclaw/issues/74900) | 0 | Local memory/embedding | @jarimustonen | [Feature]: stable public SDK path for embedding provider API (independent of memory-core) |
| 📝&nbsp;[#74835](https://github.com/openclaw/openclaw/issues/74835) | 0 | OpenAI-compatible/proxy | @abnershang | Add global provider request proxy/default SSRF policy for model providers |
| 📝&nbsp;[#74481](https://github.com/openclaw/openclaw/issues/74481) | 0 | OpenAI-compatible/proxy | @sunapi386 | feat: dynamic catalog refresh from configured provider /v1/models |
| 📝&nbsp;[#74204](https://github.com/openclaw/openclaw/issues/74204) | 0 | Local memory/embedding | @Skeptomenos | memory.qmd.update.embedTimeoutMs default (120 s) is too low for local GGUF; error message doesn't surface the fix |
| 📝&nbsp;[#74020](https://github.com/openclaw/openclaw/issues/74020) | 0 | OpenAI-compatible/proxy | @CassidyTTWD-bot | Gateway startup: models.mode=replace should skip pricing fetches |
| 📝&nbsp;[#73186](https://github.com/openclaw/openclaw/issues/73186) | 0 | OpenAI-compatible/proxy | @fryccerGit | [Bug]: Thinking/reasoning content leaks into cron announce delivery for Matrix/Feishu |
| 📝&nbsp;[#72359](https://github.com/openclaw/openclaw/issues/72359) | 0 | Local memory/embedding | @thecolormaroun | Active Memory: add single-shot mode (no embedded agent loop) for low-latency preflight injection |
| 📝&nbsp;[#71273](https://github.com/openclaw/openclaw/issues/71273) | 0 | Open-weight/provider behavior | @y9c | Bug: Kimi Code model enters infinite tool call loop |
| 🔀&nbsp;[#69729](https://github.com/openclaw/openclaw/pull/69729) | 0 | OpenAI-compatible/proxy | @wAnyBug-Com | fix(qwen): enable qwen3.6-plus on Coding Plan CN, correct reasoning flag |
| 🔀&nbsp;[#69495](https://github.com/openclaw/openclaw/pull/69495) | 0 | Model routing/config | @zote | feat(heartbeat): support model fallbacks via {primary,fallbacks} (#69434) |
| 🔀&nbsp;[#69245](https://github.com/openclaw/openclaw/pull/69245) | 0 | OpenAI-compatible/proxy | @g18166599417-svg | feat: enable cache-ttl context pruning for openai-completions providers |
| 🔀&nbsp;[#68590](https://github.com/openclaw/openclaw/pull/68590) | 0 | Local memory/embedding | @imadal1n | fix(memory-core): rewrite qmd index on managed collection repair |
| 🔀&nbsp;[#65423](https://github.com/openclaw/openclaw/pull/65423) | 0 | Model routing/config | @ryanngit | feat(agents): shuffle auth profile candidates for subagent runs |
| 🔀&nbsp;[#65180](https://github.com/openclaw/openclaw/pull/65180) | 0 | Local model runtime | @jnk0423 | fix(cli,sessions): make local model run stateless by default and keep transcript fallback profile-scoped |
| 🔀&nbsp;[#64335](https://github.com/openclaw/openclaw/pull/64335) | 0 | Open-weight/provider behavior | @serg0x | fix(zai): rotate env-backed API keys on rate limit |
| 📝&nbsp;[#63531](https://github.com/openclaw/openclaw/issues/63531) | 0 | Local memory/embedding | @ImLukeF | [Feature]: Add MLX Talk provider MVP for local macOS TTS |
| 🔀&nbsp;[#62733](https://github.com/openclaw/openclaw/pull/62733) | 0 | Local memory/embedding | @nSPIR3D | Fix local memory embedding VRAM fallback and logging file resolution |
| 🔀&nbsp;[#62710](https://github.com/openclaw/openclaw/pull/62710) | 0 | Model routing/config | @zeynalnia | fix(auth): stop new sessions inheriting auto-selected auth profile overrides |
| 📝&nbsp;[#61716](https://github.com/openclaw/openclaw/issues/61716) | 0 | OpenAI-compatible/proxy | @Andy-Xie-1145 | [Feature]: Add model parameter prompts (context window, max_tokens, modalities) during OpenAI-compatible provider onboarding CLI flow |
| 📝&nbsp;[#58765](https://github.com/openclaw/openclaw/issues/58765) | 0 | Local memory/embedding | @losz5000 | Feature: Support output dimensionality truncation for local GGUF embedding models |
| 📝&nbsp;[#57443](https://github.com/openclaw/openclaw/issues/57443) | 0 | OpenAI-compatible/proxy | @wujiaming88 | [Bug]: Tool JSON Schema patternProperties causes 400 errors on BytePlus Ark (doubao) - schema cleaning should be universal, not provider-specific |
| 🔀&nbsp;[#55477](https://github.com/openclaw/openclaw/pull/55477) | 0 | OpenAI-compatible/proxy | @Kyzcreig | feat: stamp session_key, message_channel, context_limit into LiteLLM request metadata |
| 📝&nbsp;[#54128](https://github.com/openclaw/openclaw/issues/54128) | 0 | Local memory/embedding | @hsuaaron | Add maxThreads config for local embedding (node-llama-cpp) |
| 📝&nbsp;[#53810](https://github.com/openclaw/openclaw/issues/53810) | 0 | OpenAI-compatible/proxy | @FiredMosquito831 | Subagent Premature Announce Bug - Model-Specific Tool Call Handling Issues |
| 📝&nbsp;[#44789](https://github.com/openclaw/openclaw/issues/44789) | 0 | OpenAI-compatible/proxy | @Hylance | [Bug]: openclaw 2026.03.11 partially config litellm |
| 📝&nbsp;[#43432](https://github.com/openclaw/openclaw/issues/43432) | 0 | Local memory/embedding | @omegabyte-ai | [Feature]: Memory durability config - hard flush threshold, priority-aware compaction, cache TTL |
| 📝&nbsp;[#42408](https://github.com/openclaw/openclaw/issues/42408) | 0 | Local memory/embedding | @1sexywoo8 | [Bug/Docs]: local+hybrid memory_search quality can appear unstable due to extraPaths path drift + benchmark-file contamination |

</details>

## RECENTLY CLOSED OR REMOVED FROM OPEN INVENTORY

These were in earlier local-model notes or candidate pools but are not counted as live-open retained threads now.

| [#95045](https://github.com/openclaw/openclaw/pull/95045) | Closed in local gitcrawl 2026-06-20 | fix(utils): handle Windows absolute paths in splitShellArgs (#92302); no longer open. |
| [#92773](https://github.com/openclaw/openclaw/pull/92773) | Closed in local gitcrawl 2026-06-15 | fix(tui): show resolved canonical model ref in /model confirmation; no longer open. |
| [#92743](https://github.com/openclaw/openclaw/issues/92743) | Closed in local gitcrawl 2026-06-15 | [hy-memory] AutoRecall should use current user request, not full OpenClaw envelope; no longer open. |
| [#92739](https://github.com/openclaw/openclaw/pull/92739) | Closed in local gitcrawl 2026-06-15 | fix(doctor): probe memory embeddings when --deep flag is used; no longer open. |
| [#92709](https://github.com/openclaw/openclaw/pull/92709) | Closed in local gitcrawl 2026-06-15 | fix(agents): resolve context window for proxy models with slash in ID; no longer open. |
| [#92650](https://github.com/openclaw/openclaw/pull/92650) | Closed in local gitcrawl 2026-06-15 | fix #92465: split OpenAI 431 embedding batches; no longer open. |
| [#92644](https://github.com/openclaw/openclaw/pull/92644) | Closed in local gitcrawl 2026-06-15 | fix(openrouter): strip openrouter/ prefix from model IDs before API calls; no longer open. |
| [#92641](https://github.com/openclaw/openclaw/pull/92641) | Closed in local gitcrawl 2026-06-15 | fix(memory): run memory+supplement searches in parallel for corpus=all (fixes #92633); no longer open. |

| [#92639](https://github.com/openclaw/openclaw/pull/92639) | Closed in local gitcrawl 2026-06-15 | fix(memory): keep memory_search in transient qmd mode; no longer open. |

| [#92629](https://github.com/openclaw/openclaw/issues/92629) | Closed in local gitcrawl 2026-06-15 | [Bug]: Gateway re-reads and deep-clones the entire subagent registry on every transcript-update broadcast, stalling the event loop ~4s per tool call (scales with registry size); no longer open. |

| [#92628](https://github.com/openclaw/openclaw/pull/92628) | Closed in local gitcrawl 2026-06-15 | fix #73713: surface nested embedding fetch failures; no longer open. |

| [#92627](https://github.com/openclaw/openclaw/pull/92627) | Closed in local gitcrawl 2026-06-15 | fix(openrouter): strip openrouter/ prefix from model ID in normalizeResolvedModel hook (fixes #92611); no longer open. |

| [#92618](https://github.com/openclaw/openclaw/pull/92618) | Closed in local gitcrawl 2026-06-15 | fix #92218: memory_search tool disabled with QMD backend; no longer open. |

| [#92614](https://github.com/openclaw/openclaw/pull/92614) | Closed in local gitcrawl 2026-06-15 | fix(openrouter): strip openrouter/ prefix from model ID before API call (fixes #92611); no longer open. |

| [#92611](https://github.com/openclaw/openclaw/issues/92611) | Closed in local gitcrawl 2026-06-15 | [Bug]: OpenRouter: Anthropic models send wrong model ID to API (includes openrouter/ prefix); no longer open. |

| [#92599](https://github.com/openclaw/openclaw/issues/92599) | Closed in local gitcrawl 2026-06-15 | Model calls to a stalled provider connection hang to the job timeout — fetch timeout doesn't fire and fallback never triggers; no longer open. |

| [#92585](https://github.com/openclaw/openclaw/pull/92585) | Closed in local gitcrawl 2026-06-15 | fix(model-registry): skip invalid plugin catalog shards instead of aborting the whole load; no longer open. |

<details>
<summary>Recently closed or removed threads (527)</summary>

| Thread | Status checked | Note |
| --- | --- | --- |
| [#92583](https://github.com/openclaw/openclaw/pull/92583) | Closed in local gitcrawl 2026-06-15 | fix(doctor): pass --deep flag to memory embedding probe (fixes #92582); no longer open. |
| 🔀&nbsp;[#92577](https://github.com/openclaw/openclaw/pull/92577) | 0 | Local memory/embedding | @xydt-tanshanshan | fix: deduplicate consecutive assistant messages in session-memory hook |
| 🔀&nbsp;[#92575](https://github.com/openclaw/openclaw/pull/92575) | 0 | Model routing/config | @harjothkhara | fix(sessions): preserve user behavior overrides across daily/idle rollover (#92562) [AI-assisted] |
| 🔀&nbsp;[#92573](https://github.com/openclaw/openclaw/pull/92573) | 0 | Model routing/config | @arkyu2077 | fix: preserve config-selected subagent model overrides |
| 📝&nbsp;[#92572](https://github.com/openclaw/openclaw/issues/92572) | 0 | Model routing/config | @sweetrice-stack | [Bug]: Claude Opus 4.6 via `agy` CLI returns 404 in web UI despite working in terminal |
| 🔀&nbsp;[#92571](https://github.com/openclaw/openclaw/pull/92571) | 0 | Local memory/embedding | @arkyu2077 | fix: dedupe cleaned assistant transcript entries for session-memory |
| 🔀&nbsp;[#92565](https://github.com/openclaw/openclaw/pull/92565) | 0 | OpenAI-compatible/proxy | @fsdwen | fix(deepseek): enable prompt cache key in model catalog |
| 🔀&nbsp;[#92564](https://github.com/openclaw/openclaw/pull/92564) | 0 | Model routing/config | @tangtaizong666 | fix(agents): isolate invalid plugin model catalogs [AI-assisted] |
| 📝&nbsp;[#92563](https://github.com/openclaw/openclaw/issues/92563) | 0 | Local memory/embedding | @redcrowst2-afk | session-memory hook duplicates assistant messages when thinking is stripped |
| 📝&nbsp;[#92562](https://github.com/openclaw/openclaw/issues/92562) | 0 | Model routing/config | @civiltox | [Bug]: Implicit daily/idle session rollover does not preserve user-set behavior overrides |
| [#92554](https://github.com/openclaw/openclaw/pull/92554) | Closed in local gitcrawl 2026-06-15 | feat(moonshot): add Kimi K2.7 Code support; no longer open. |
| [#92553](https://github.com/openclaw/openclaw/issues/92553) | Closed in local gitcrawl 2026-06-15 | ModelRegistry: a single invalid plugin catalog aborts the entire custom-models load, leaving zero models and an unlogged error; no longer open. |
| [#92539](https://github.com/openclaw/openclaw/issues/92539) | Closed in local gitcrawl 2026-06-15 | ModelRegistry: a single invalid plugin catalog aborts the entire custom-models load, leaving zero models and an unlogged error; no longer open. |
| [#92538](https://github.com/openclaw/openclaw/pull/92538) | Closed in local gitcrawl 2026-06-15 | fix(memory): persist metadata during safe reindex; no longer open. |
| 📝&nbsp;[#92536](https://github.com/openclaw/openclaw/issues/92536) | 0 | Local memory/embedding | @resYuto | [Bug]: Dreaming sweeps not working if use Dreaming-compatible memory plugin |
| 🔀&nbsp;[#92531](https://github.com/openclaw/openclaw/pull/92531) | 0 | Local memory/embedding | @leonmuellerfijucha | feat: implement shadow-logger plugin for memory system |
| 🔀&nbsp;[#92529](https://github.com/openclaw/openclaw/pull/92529) | 0 | Model routing/config | @jml001 | fix(agents): prevent local exec policy errors from triggering model fallback |
| 🔀&nbsp;[#92526](https://github.com/openclaw/openclaw/pull/92526) | 0 | Model routing/config | @zenglingbiao | fix(gateway): treat google-gemini-cli Gemini models as image-capable (fixes #91739) |
| 🔀&nbsp;[#92524](https://github.com/openclaw/openclaw/pull/92524) | 0 | Local memory/embedding | @yu-xin-c | fix(memory-core): preserve overlapping hybrid keyword scores |
| 🔀&nbsp;[#92515](https://github.com/openclaw/openclaw/pull/92515) | 0 | Local memory/embedding | @EleutheroiEdge | Recover memory search from transient missing metadata |
| 🔀&nbsp;[#92510](https://github.com/openclaw/openclaw/pull/92510) | 0 | OpenAI-compatible/proxy | @zhangguiping-xydt | fix(gateway): reject unknown OpenAI agent selectors |
| 🔀&nbsp;[#92509](https://github.com/openclaw/openclaw/pull/92509) | 0 | Local memory/embedding | @Dazlarus | fix(memory-core): WAL checkpoint after writeMeta + stale index file cleanup |
| [#92507](https://github.com/openclaw/openclaw/pull/92507) | Closed in local gitcrawl 2026-06-15 | fix(memory): persist metadata after atomic reindex; no longer open. |
| [#92504](https://github.com/openclaw/openclaw/issues/92504) | Closed in local gitcrawl 2026-06-15 | Gateway runs well-formed-but-unknown agent slug under agents.defaults instead of 4xx (no roster validation in resolveAgentIdForRequest; x-openclaw-agent-id header never roster-validated); no longer open. |
| [#92493](https://github.com/openclaw/openclaw/pull/92493) | Closed in local gitcrawl 2026-06-15 | fix(gateway): clear provider auth prewarm on stop; no longer open. |
| [#92465](https://github.com/openclaw/openclaw/issues/92465) | Closed in local gitcrawl 2026-06-15 | Bulk memory import can hit OpenAI 431; chunked indexing avoids it; no longer open. |
| [#92458](https://github.com/openclaw/openclaw/issues/92458) | Closed in local gitcrawl 2026-06-15 | 2026.6 openai-provider-unification migration removes openai-codex:default profile, breaking every Codex-backed agent at launch (root cause + concrete fix); no longer open. |
| [#92447](https://github.com/openclaw/openclaw/pull/92447) | Closed in local gitcrawl 2026-06-15 | fix(memory-search): increase tool timeout from 15s to 60s; no longer open. |
| [#92442](https://github.com/openclaw/openclaw/pull/92442) | Closed in local gitcrawl 2026-06-15 | fix(memory-search): increase tool timeout from 15s to 60s; no longer open. |
| [#92415](https://github.com/openclaw/openclaw/issues/92415) | Closed in local gitcrawl 2026-06-15 | Session-level AgentSession.this.model snapshot is never refreshed after /model switch (affects contextWindow, reasoning, thinkingLevelMap, branch summary); no longer open. |
| [#92396](https://github.com/openclaw/openclaw/pull/92396) | Closed in local gitcrawl 2026-06-15 | fix(moonshot): backfill reasoning_content on assistant tool-call replay messages; no longer open. |
| [#92379](https://github.com/openclaw/openclaw/issues/92379) | Closed in local gitcrawl 2026-06-15 | [Bug]: Session this.model not refreshed after /model switch — auto-compaction uses stale contextWindow; no longer open. |
| [#92357](https://github.com/openclaw/openclaw/pull/92357) | Closed in local gitcrawl 2026-06-15 | fix(memory): preserve keyword-only results in hybrid search when chunk IDs don't overlap (fixes #92337); no longer open. |
| [#92350](https://github.com/openclaw/openclaw/pull/92350) | Closed in local gitcrawl 2026-06-15 | [codex] Fix memory recall prompt registration; no longer open. |
| [#92333](https://github.com/openclaw/openclaw/issues/92333) | Closed in local gitcrawl 2026-06-15 | Bug: model.fallbacks gets wiped when desktop app switches primary model; no longer open. |
| [#92308](https://github.com/openclaw/openclaw/pull/92308) | Closed in local gitcrawl 2026-06-15 | fix(memory): preserve Windows absolute paths in QMD command resolution (fixes #92302); no longer open. |
| [#92306](https://github.com/openclaw/openclaw/issues/92306) | Closed in local gitcrawl 2026-06-15 | [Bug]: cron jobs fails with "LLM request failed"; no longer open. |
| [#92300](https://github.com/openclaw/openclaw/pull/92300) | Closed in local gitcrawl 2026-06-15 | fix(openai-responses): collapse cumulative message snapshots; no longer open. |
| [#92293](https://github.com/openclaw/openclaw/pull/92293) | Closed in local gitcrawl 2026-06-15 | Fix provider static model fallback resolution; no longer open. |
| [#92292](https://github.com/openclaw/openclaw/pull/92292) | Closed in local gitcrawl 2026-06-15 | fix(doctor): warn when resolved default model is not in the catalog (fixes #92009); no longer open. |
| [#92280](https://github.com/openclaw/openclaw/pull/92280) | Closed in local gitcrawl 2026-06-15 | fix(agents): classify structured unsupported model errors; no longer open. |
| [#92266](https://github.com/openclaw/openclaw/pull/92266) | Closed in local gitcrawl 2026-06-12 | fix(memory): report vector store ready when indexed chunks exist but probe was skipped; no longer open. |
| [#92265](https://github.com/openclaw/openclaw/pull/92265) | Closed in local gitcrawl 2026-06-15 | Fix configured DeepSeek model transport inheritance; no longer open. |
| [#92264](https://github.com/openclaw/openclaw/pull/92264) | Closed in local gitcrawl 2026-06-15 | fix(btw): resolve agentRuntime alias models in /btw side questions (fixes #92168); no longer open. |
| [#92247](https://github.com/openclaw/openclaw/pull/92247) | Closed in local gitcrawl 2026-06-15 | fix(models): bound /models and models list catalog loading; no longer open. |
| [#92235](https://github.com/openclaw/openclaw/pull/92235) | Closed in local gitcrawl 2026-06-15 | fix: resolve managed SecretRef provider auth; no longer open. |
| [#92228](https://github.com/openclaw/openclaw/pull/92228) | Closed in local gitcrawl 2026-06-12 | fix(cli): mark local models (Ollama) available in models list without auth; no longer open. |
| [#92226](https://github.com/openclaw/openclaw/pull/92226) | Closed in local gitcrawl 2026-06-15 | Fail closed for CLI-backed /btw fallback; no longer open. |
| [#92218](https://github.com/openclaw/openclaw/issues/92218) | Closed in local gitcrawl 2026-06-15 | memory_search tool disabled with QMD backend; no longer open. |
| [#92208](https://github.com/openclaw/openclaw/pull/92208) | Closed in local gitcrawl 2026-06-15 | fix(model-auth): resolve secretref-managed custom provider keys from runtime config snapshot; no longer open. |
| [#92192](https://github.com/openclaw/openclaw/pull/92192) | Closed in local gitcrawl 2026-06-12 | fix(model-auth): resolve secretref-managed custom provider keys from runtime config snapshot; no longer open. |
| [#92181](https://github.com/openclaw/openclaw/pull/92181) | Closed in local gitcrawl 2026-06-15 | fix(agents): align /btw model resolution with runtime aliases; no longer open. |
| [#92177](https://github.com/openclaw/openclaw/pull/92177) | Closed in local gitcrawl 2026-06-15 | fix(agents): treat NO_REPLY-only turns as silent regardless of silence flag (#92038); no longer open. |
| [#92168](https://github.com/openclaw/openclaw/issues/92168) | Closed in local gitcrawl 2026-06-15 | [Bug]: /btw fails with "Unknown model" for anthropic/* aliases routed via agentRuntime: claude-cli (resolver path divergence from main agent loop); no longer open. |
| [#92166](https://github.com/openclaw/openclaw/pull/92166) | Closed in local gitcrawl 2026-06-12 | fix(media-understanding): resolve image model input from catalog, preserve explicit text-only (#92104); no longer open. |
| [#92159](https://github.com/openclaw/openclaw/pull/92159) | Closed in local gitcrawl 2026-06-12 | fix(media-understanding): resolve image model input from bundled catalog for inline providers (#92104); no longer open. |
| [#92148](https://github.com/openclaw/openclaw/issues/92148) | Closed in local gitcrawl 2026-06-15 | [Bug]: 2026.6.5 routes DeepSeek (custom OpenAI-compatible provider) to the OpenAI Responses API → 401, now affecting non-reasoning deepseek-v4-pro; no longer open. |
| [#92145](https://github.com/openclaw/openclaw/pull/92145) | Closed in local gitcrawl 2026-06-12 | fix(model-auth): resolve secretref-managed apiKey from runtime config snapshot (#92097); no longer open. |
| [#92133](https://github.com/openclaw/openclaw/pull/92133) | Closed in local gitcrawl 2026-06-15 | fix(agents): handle "Not supported model" error format in isModelNotFoundErrorMessage; no longer open. |
| [#92131](https://github.com/openclaw/openclaw/pull/92131) | Closed in local gitcrawl 2026-06-15 | [codex] fix(agents): detect not supported model errors; no longer open. |
| [#92127](https://github.com/openclaw/openclaw/pull/92127) | Closed in local gitcrawl 2026-06-12 | fix(plugins): stop derived metadata snapshot rescan storm in /models (regression shipped since v2026.5.18); no longer open. |
| [#92121](https://github.com/openclaw/openclaw/pull/92121) | Closed in local gitcrawl 2026-06-12 | [AI] fix(memory): eliminate absent-window race in index swap + prevent auto-create empty DB; no longer open. |
| [#92118](https://github.com/openclaw/openclaw/issues/92118) | Closed in local gitcrawl 2026-06-15 | isModelNotFoundErrorMessage does not match "Not supported model" error format; no longer open. |
| [#92113](https://github.com/openclaw/openclaw/pull/92113) | Closed in local gitcrawl 2026-06-15 | fix(auth): resolve custom provider secretref-managed apiKey from runtime snapshot; no longer open. |
| [#92104](https://github.com/openclaw/openclaw/issues/92104) | Closed in local gitcrawl 2026-06-15 | image/pdf tool: 'Unknown model' for every provider, while the same models work as agent models (2026.5.28 and 2026.6.5); no longer open. |
| [#92097](https://github.com/openclaw/openclaw/issues/92097) | Closed in local gitcrawl 2026-06-15 | [Bug] Custom providers with secretref-managed apiKey fail with 503 auth_unavailable after update to 2026.6.5; no longer open. |
| [#92071](https://github.com/openclaw/openclaw/pull/92071) | Closed in local gitcrawl 2026-06-12 | fix(anthropic): resolve thinking profile for custom Anthropic-compatible providers; no longer open. |
| [#92053](https://github.com/openclaw/openclaw/pull/92053) | Closed in local gitcrawl 2026-06-12 | fix(thinking): apply Claude profile to anthropic-messages catalog rows; no longer open. |
| [#92050](https://github.com/openclaw/openclaw/issues/92050) | Closed in local gitcrawl 2026-06-15 | memory-core: short-term-recall.json grows without rotation → permanent dreaming promotion deadlock once it crosses the 16MiB read limit; no longer open. |
| [#92038](https://github.com/openclaw/openclaw/issues/92038) | Closed in local gitcrawl 2026-06-12 | NO_REPLY silence reply counted as empty turn - retry + candidate_failed(format) + full fallback cascade on heartbeats (2026.6.5); no longer open. |
| [#92034](https://github.com/openclaw/openclaw/pull/92034) | Closed in local gitcrawl 2026-06-12 | perf(agents): memoize XML attribute regex in DSML stream parser; no longer open. |
| [#92020](https://github.com/openclaw/openclaw/pull/92020) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): check SQLite plugin state for dreaming ingestion audit after JSON migration (fixes #92017); no longer open. |
| [#92019](https://github.com/openclaw/openclaw/issues/92019) | Closed in local gitcrawl 2026-06-15 | anthropic-messages replay: preserved thinking-block signatures hard-fail (400 Invalid signature) on proxied endpoints / model-switch; no longer open. |
| [#92018](https://github.com/openclaw/openclaw/issues/92018) | Closed in local gitcrawl 2026-06-12 | [Bug]: Builtin semantic memory index loses memory_index_meta_v1 after live memory_search; no longer open. |
| [#92017](https://github.com/openclaw/openclaw/issues/92017) | Closed in local gitcrawl 2026-06-12 | [Bug]: memory status reports "ingestion state absent" after dreaming JSON→SQLite migration; no longer open. |
| [#92010](https://github.com/openclaw/openclaw/issues/92010) | Closed in local gitcrawl 2026-06-15 | [Feature]: Add CloudSigma TaaS as a model provider (OpenAI-compatible multi-model gateway); no longer open. |
| [#92009](https://github.com/openclaw/openclaw/issues/92009) | Closed in local gitcrawl 2026-06-15 | [Bug]: Resolved default model google/gemini-3.1-pro-preview cannot be inspected or executed in 2026.6.5; no longer open. |
| [#91982](https://github.com/openclaw/openclaw/issues/91982) | Closed in local gitcrawl 2026-06-15 | [Bug]: anthropic-vertex-provider adds cache_control to active-memory system block — triggers "Found 5" error when active-memory is enabled; no longer open. |
| [#91975](https://github.com/openclaw/openclaw/issues/91975) | Closed in local gitcrawl 2026-06-12 | Native Anthropic adapter silently drops `thinking` to `off` for custom provider ids (resolveThinkingProfile only matches exact `anthropic`/`claude-cli`); no longer open. |
| [#91965](https://github.com/openclaw/openclaw/issues/91965) | Closed in local gitcrawl 2026-06-15 | [Bug]: memory_search permanently fails with "index metadata is missing" — cached indexIdentityState not refreshed after meta fix; no longer open. |
| [#91961](https://github.com/openclaw/openclaw/issues/91961) | Closed in local gitcrawl 2026-06-15 | Memory status shows 'paused' after index rebuild despite vector search working (v2026.6.5); no longer open. |
| [#91942](https://github.com/openclaw/openclaw/issues/91942) | Closed in local gitcrawl 2026-06-15 | [Bug] l1-extractor 临时 workspace 上下文注入缺失，LLM 返回空字符串; no longer open. |
| [#91930](https://github.com/openclaw/openclaw/issues/91930) | Closed in local gitcrawl 2026-06-15 | Docs feedback: /providers/opencode; no longer open. |
| [#91912](https://github.com/openclaw/openclaw/issues/91912) | Closed in local gitcrawl 2026-06-15 | Feature request: per-session suppressFallbackNotice config option; no longer open. |
| [#91911](https://github.com/openclaw/openclaw/pull/91911) | Closed in local gitcrawl 2026-06-12 | fix(agents): retry same model across short rate-limit windows; no longer open. |
| [#91897](https://github.com/openclaw/openclaw/pull/91897) | Closed in local gitcrawl 2026-06-12 | fix(memory): self-heal missing index identity by initializing provider during sync; no longer open. |
| [#91895](https://github.com/openclaw/openclaw/pull/91895) | Closed in local gitcrawl 2026-06-12 | fix(webchat): finalize provider failure lifecycle; no longer open. |
| [#91884](https://github.com/openclaw/openclaw/pull/91884) | Closed in local gitcrawl 2026-06-12 | fix(memory): keep QMD background refreshes armed; no longer open. |
| [#91882](https://github.com/openclaw/openclaw/pull/91882) | Closed in local gitcrawl 2026-06-12 | feat(anthropic): support Claude Fable 5 adaptive thinking; no longer open. |
| [#91864](https://github.com/openclaw/openclaw/pull/91864) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): force exit after memory search --json output; no longer open. |
| [#91837](https://github.com/openclaw/openclaw/pull/91837) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): settle json search cleanup; no longer open. |
| [#91830](https://github.com/openclaw/openclaw/pull/91830) | Closed in local gitcrawl 2026-06-12 | feat: add OpenRouter OAuth to onboarding; no longer open. |
| [#91827](https://github.com/openclaw/openclaw/issues/91827) | Closed in local gitcrawl 2026-06-15 | [P1] Structural fix: content-based dedup + delivery-mirror model-hiding for kimi-code message loops; no longer open. |
| [#91821](https://github.com/openclaw/openclaw/issues/91821) | Closed in local gitcrawl 2026-06-12 | memory search --json prints results but does not exit with QMD backend; no longer open. |
| [#91813](https://github.com/openclaw/openclaw/pull/91813) | Closed in local gitcrawl 2026-06-12 | fix(codex): restore memory recall from plugin tools; no longer open. |
| [#91809](https://github.com/openclaw/openclaw/issues/91809) | Closed in local gitcrawl 2026-06-15 | [Performance] /models command slow in v2026.6.1 — catalog loading regression; no longer open. |
| [#91796](https://github.com/openclaw/openclaw/pull/91796) | Closed in local gitcrawl 2026-06-15 | fix(anthropic): add Claude Haiku 4.5 to static model catalog; no longer open. |
| [#91790](https://github.com/openclaw/openclaw/pull/91790) | Closed in local gitcrawl 2026-06-12 | fix(gateway): add google-gemini-cli image capability shim (fixes #91739); no longer open. |
| [#91778](https://github.com/openclaw/openclaw/issues/91778) | Closed in local gitcrawl 2026-06-15 | [P0] memory_search cassé — index metadata is missing depuis v2026.6.1, reproduit sur v2026.6.5; no longer open. |
| [#91742](https://github.com/openclaw/openclaw/pull/91742) | Closed in local gitcrawl 2026-06-12 | fix(memory): abort orphaned embedding work when memory_search times out; no longer open. |
| [#91740](https://github.com/openclaw/openclaw/pull/91740) | Closed in local gitcrawl 2026-06-12 | fix(auth): verify SQLite auth migration before cleanup; no longer open. |
| [#91730](https://github.com/openclaw/openclaw/issues/91730) | Closed in local gitcrawl 2026-06-12 | [Bug]: OpenClaw-native provider failure leaves web chat session stuck in progress; no longer open. |
| [#91720](https://github.com/openclaw/openclaw/pull/91720) | Closed in local gitcrawl 2026-06-12 | :bug: fix(openai): remove chatgpt-responses transport override from gpt-5.3-codex catalog entry; no longer open. |
| [#91718](https://github.com/openclaw/openclaw/issues/91718) | Closed in local gitcrawl 2026-06-12 | memory_search tool-level timeout orphans background embedding work; no longer open. |
| [#91711](https://github.com/openclaw/openclaw/pull/91711) | Closed in local gitcrawl 2026-06-12 | :bug: fix(agents): classify harness provider mismatch as format error (#91710); no longer open. |
| [#91710](https://github.com/openclaw/openclaw/issues/91710) | Closed in local gitcrawl 2026-06-12 | [Bug]: v2026.6.1 regression: openai/gpt-5.3-codex silently falls back to Sonnet — Codex harness rejects "openai" provider due to stale npm plugin; no longer open. |
| [#91708](https://github.com/openclaw/openclaw/pull/91708) | Closed in local gitcrawl 2026-06-12 | fix(agents): preserve legacy openai-codex context overrides after provider unification (fixes #90448); no longer open. |
| [#91696](https://github.com/openclaw/openclaw/pull/91696) | Closed in local gitcrawl 2026-06-12 | fix(agents): preserve reasoning_content replay for Gemma 4 openai-completions models; no longer open. |
| [#91657](https://github.com/openclaw/openclaw/pull/91657) | Closed in local gitcrawl 2026-06-12 | fix(ollama): use provider thinking default in SDK session factory; no longer open. |
| [#91651](https://github.com/openclaw/openclaw/issues/91651) | Closed in local gitcrawl 2026-06-12 | bug(tools): web_fetch fails with 'Invalid URL' when LLM generates a space in the protocol scheme; no longer open. |
| [#91645](https://github.com/openclaw/openclaw/issues/91645) | Closed in local gitcrawl 2026-06-12 | [Bug]: In-turn reasoning dropped on multi-turn tool replay for non-400 openai models (gemma4/vLLM) — silent agentic-quality regression; no longer open. |
| [#91634](https://github.com/openclaw/openclaw/issues/91634) | Closed in local gitcrawl 2026-06-15 | memory-tdai: ByteString encoding fails on fullwidth ellipsis (U+2026) in vec indexer; no longer open. |
| [#91589](https://github.com/openclaw/openclaw/pull/91589) | Closed in local gitcrawl 2026-06-11 | Harden external CLI auth sync diagnostics; no longer open. |
| [#91580](https://github.com/openclaw/openclaw/pull/91580) | Closed in local gitcrawl 2026-06-11 | fix(agents): trim dense text delta snapshots; no longer open. |
| [#91579](https://github.com/openclaw/openclaw/pull/91579) | Closed in local gitcrawl 2026-06-11 | fix(agents): bootstrap OpenClaw auth for codex harness when provider is codex; no longer open. |
| [#91575](https://github.com/openclaw/openclaw/issues/91575) | Closed in local gitcrawl 2026-06-15 | [Feature]: Feature Request: Pre-request budget/cost check to prevent runaway spending on free tier accounts; no longer open. |
| [#91567](https://github.com/openclaw/openclaw/pull/91567) | Closed in local gitcrawl 2026-06-11 | fix(openai): require api-key auth for realtime voice; no longer open. |
| [#91560](https://github.com/openclaw/openclaw/issues/91560) | Closed in local gitcrawl 2026-06-15 | [Bug]: Codex ACP native route fails with "Authentication required" when host Codex uses OAuth (ChatGPT login); no longer open. |
| [#91538](https://github.com/openclaw/openclaw/pull/91538) | Closed in local gitcrawl 2026-06-11 | perf(control-ui): avoid startup catalog wait; no longer open. |
| [#91531](https://github.com/openclaw/openclaw/pull/91531) | Closed in local gitcrawl 2026-06-11 | perf(control-ui): reuse startup model metadata; no longer open. |
| [#91513](https://github.com/openclaw/openclaw/issues/91513) | Closed in local gitcrawl 2026-06-11 | ACP: model prefix not stripped when dispatching to Claude ACP adapter — Cannot replay saved model "anthropic/claude-sonnet-4-6"; no longer open. |
| [#91430](https://github.com/openclaw/openclaw/pull/91430) | Closed in local gitcrawl 2026-06-11 | fix(openai): honor configured embedding model input limits; no longer open. |
| [#91428](https://github.com/openclaw/openclaw/issues/91428) | Closed in local gitcrawl 2026-06-12 | Gemma4/Qwen3.6 via local Ollama: only first token/word? rendered, while Ollama streams clean content-only output; no longer open. |
| [#91425](https://github.com/openclaw/openclaw/pull/91425) | Closed in local gitcrawl 2026-06-11 | fix(memory-lancedb): guard memory recall output [AI]; no longer open. |
| [#91421](https://github.com/openclaw/openclaw/pull/91421) | Closed in local gitcrawl 2026-06-11 | fix(cron): clear payload model overrides; no longer open. |
| [#91405](https://github.com/openclaw/openclaw/pull/91405) | Closed in local gitcrawl 2026-06-11 | fix(cli): thread silent-empty policy to CLI runner to stop duplicate group reply (fixes #91302); no longer open. |
| [#91395](https://github.com/openclaw/openclaw/pull/91395) | Closed in local gitcrawl 2026-06-11 | fix(cron): inherit default model fallbacks for plain-string agent models (fixes #91362); no longer open. |
| [#91388](https://github.com/openclaw/openclaw/pull/91388) | Closed in local gitcrawl 2026-06-11 | [codex] Fix Claude tool-only empty response fallback; no longer open. |
| [#91387](https://github.com/openclaw/openclaw/pull/91387) | Closed in local gitcrawl 2026-06-11 | fix(cron): clear payload model overrides; no longer open. |
| [#91380](https://github.com/openclaw/openclaw/pull/91380) | Closed in local gitcrawl 2026-06-11 | fix(cron): inherit default fallbacks for cron string models; no longer open. |
| [#91379](https://github.com/openclaw/openclaw/pull/91379) | Closed in local gitcrawl 2026-06-11 | fix(cron): inherit default fallbacks for string agent jobs; no longer open. |
| [#91373](https://github.com/openclaw/openclaw/pull/91373) | Closed in local gitcrawl 2026-06-11 | fix(agent): string model configs inherit default fallbacks for cron sessions; no longer open. |
| [#91360](https://github.com/openclaw/openclaw/pull/91360) | Closed in local gitcrawl 2026-06-11 | fix(cron): allow clearing payload.model via update (fixes #91298); no longer open. |
| [#91351](https://github.com/openclaw/openclaw/pull/91351) | Closed in local gitcrawl 2026-06-12 | fix(opencode-go): add qwen plus tiered pricing; no longer open. |
| [#91338](https://github.com/openclaw/openclaw/pull/91338) | Closed in local gitcrawl 2026-06-11 | fix(cron): allow payload.model and other optional fields to be cleared via null in update API; no longer open. |
| [#91329](https://github.com/openclaw/openclaw/pull/91329) | Closed in local gitcrawl 2026-06-11 | fix(reply): pass silent-empty policy to CLI fallback runs; no longer open. |
| [#91324](https://github.com/openclaw/openclaw/pull/91324) | Closed in local gitcrawl 2026-06-11 | fix(memory): move local llama.cpp runtime to provider plugin; no longer open. |
| [#91319](https://github.com/openclaw/openclaw/pull/91319) | Closed in local gitcrawl 2026-06-11 | Fix CLI silent reply fallback policy; no longer open. |
| [#91318](https://github.com/openclaw/openclaw/pull/91318) | Closed in local gitcrawl 2026-06-11 | fix(cron): allow update patches to clear payload.model back to inherit; no longer open. |
| [#91313](https://github.com/openclaw/openclaw/pull/91313) | Closed in local gitcrawl 2026-06-11 | fix(cron): allow null model/fallbacks in payload patch to clear overrides (fixes #91298); no longer open. |
| [#91299](https://github.com/openclaw/openclaw/pull/91299) | Closed in local gitcrawl 2026-06-15 | fix(memory-core): write ## Deep Sleep summary into DREAMS.md after deep dreaming sweep; no longer open. |
| [#91297](https://github.com/openclaw/openclaw/pull/91297) | Closed in local gitcrawl 2026-06-11 | fix(memory): rebind qmd collection when root path drifts despite list missing path (#91251); no longer open. |
| [#91292](https://github.com/openclaw/openclaw/pull/91292) | Closed in local gitcrawl 2026-06-12 | fix(models): keep bundled provider catalog when configured base URL is blank (#91270); no longer open. |
| [#91275](https://github.com/openclaw/openclaw/pull/91275) | Closed in local gitcrawl 2026-06-11 | fix(memory-qmd): enrich collection list with path from 'qmd collection show' so rebind detects changed roots; no longer open. |
| [#91270](https://github.com/openclaw/openclaw/issues/91270) | Closed in local gitcrawl 2026-06-12 | [Bug]: Gemini can't resolve on embedded runtime; no longer open. |
| [#91265](https://github.com/openclaw/openclaw/pull/91265) | Closed in local gitcrawl 2026-06-15 | fix(memory): drop redundant agent-id scoping from QMD collection names; no longer open. |
| [#91260](https://github.com/openclaw/openclaw/issues/91260) | Closed in local gitcrawl 2026-06-11 | opencode-go: bundled models from provider-catalog.ts (glm-5, glm-5.1, kimi-k2.5, mimo-v2.5-pro, minimax-m2.5, minimax-m2.7, qwen3.5-plus) are silently dropped at runtime — only 5 of 12 surface; no longer open. |
| [#91255](https://github.com/openclaw/openclaw/pull/91255) | Closed in local gitcrawl 2026-06-11 | fix(memory-core): enrich collection paths from qmd collection show to enable rebind (fixes #91251); no longer open. |
| [#91253](https://github.com/openclaw/openclaw/pull/91253) | Closed in local gitcrawl 2026-06-11 | fix(memory): rebind qmd collections when a collection root changes; no longer open. |
| [#91251](https://github.com/openclaw/openclaw/issues/91251) | Closed in local gitcrawl 2026-06-11 | memory(qmd): collections never rebind when a collection's root path changes; no longer open. |
| [#91238](https://github.com/openclaw/openclaw/issues/91238) | Closed in local gitcrawl 2026-06-12 | opencode-go provider: qwen3.7-max, qwen3.7-plus, minimax-m3 missing from static model catalog → "Unknown model" (model_not_found); no longer open. |
| [#91231](https://github.com/openclaw/openclaw/pull/91231) | Closed in local gitcrawl 2026-06-11 | fix(anthropic): drop reasoning_content replay signatures; no longer open. |
| [#91227](https://github.com/openclaw/openclaw/pull/91227) | Closed in local gitcrawl 2026-06-15 | fix #91216: [Bug]: gateway opens an empty memory database when main.sqlite is absent during the index swap, leaving memory_search paused with "index metadata is missing" until restart; no longer open. |
| [#91218](https://github.com/openclaw/openclaw/pull/91218) | Closed in local gitcrawl 2026-06-15 | fix(google): strip provider prefix from Vertex model path; no longer open. |
| [#91216](https://github.com/openclaw/openclaw/issues/91216) | Closed in local gitcrawl 2026-06-12 | [Bug]: gateway opens an empty memory database when main.sqlite is absent during the index swap, leaving memory_search paused with "index metadata is missing" until restart; no longer open. |
| [#91205](https://github.com/openclaw/openclaw/issues/91205) | Closed in local gitcrawl 2026-06-11 | Cross-provider thinking block signature poisoning bricks sessions when switching between non-Anthropic and Anthropic models; no longer open. |
| [#91188](https://github.com/openclaw/openclaw/pull/91188) | Closed in local gitcrawl 2026-06-11 | fix(memory-core): write ## Deep Sleep summary to DREAMS.md; no longer open. |
| [#91175](https://github.com/openclaw/openclaw/pull/91175) | Closed in local gitcrawl 2026-06-11 | fix(memory-core): write Deep Sleep summary into DREAMS.md after deep dreaming phase (fixes #91051); no longer open. |
| [#91173](https://github.com/openclaw/openclaw/pull/91173) | Closed in local gitcrawl 2026-06-12 | fix(memory): self-heal missing index identity during sync; no longer open. |
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
| [#91073](https://github.com/openclaw/openclaw/pull/91073) | Closed in local gitcrawl 2026-06-11 | fix(openrouter): reconcile streamed generation cost; no longer open. |
| [#91072](https://github.com/openclaw/openclaw/pull/91072) | Closed in local gitcrawl 2026-06-11 | refactor(memory-wiki): store source sync state in sqlite; no longer open. |
| [#91071](https://github.com/openclaw/openclaw/pull/91071) | Closed in local gitcrawl 2026-06-11 | fix(memory-core): write Deep Sleep summary to DREAMS.md with managed markers; no longer open. |
| [#91068](https://github.com/openclaw/openclaw/pull/91068) | Closed in local gitcrawl 2026-06-11 | Refactor core fetch paths off guarded fetch; no longer open. |
| [#91060](https://github.com/openclaw/openclaw/issues/91060) | Closed in local gitcrawl 2026-06-15 | Feature Request: Per-task or Per-capability Model Routing; no longer open. |
| [#91046](https://github.com/openclaw/openclaw/pull/91046) | Closed in local gitcrawl 2026-06-11 | fix(microsoft-foundry): exclude alias providers from DeepSeek V4 thinking wrapper (fixes #90520); no longer open. |
| [#91045](https://github.com/openclaw/openclaw/pull/91045) | Closed in local gitcrawl 2026-06-11 | fix(config): accept model thinkingLevelMap in provider config schema (#91011) [AI-assisted]; no longer open. |
| [#91037](https://github.com/openclaw/openclaw/pull/91037) | Closed in local gitcrawl 2026-06-11 | fix(config): allow thinkingLevelMap in persisted model schema; no longer open. |
| [#91033](https://github.com/openclaw/openclaw/issues/91033) | Closed in local gitcrawl 2026-06-11 | [Bug]: microsoft-foundry reasoning models return 400 invalid_encrypted_content when continuing a thread; no longer open. |
| [#91031](https://github.com/openclaw/openclaw/pull/91031) | Closed in local gitcrawl 2026-06-12 | [codex] Add OpenRouter OAuth login; no longer open. |
| [#91018](https://github.com/openclaw/openclaw/issues/91018) | Closed in local gitcrawl 2026-06-15 | ⚠️ Upgrade 2026.6.1 broke DeepSeek prompt cache - $6 burned in one hour; no longer open. |
| [#91011](https://github.com/openclaw/openclaw/issues/91011) | Closed in local gitcrawl 2026-06-11 | [Bug]: Foundry Entra ID onboarding fails to save with "Unrecognized key: thinkingLevelMap"; no longer open. |
| [#91008](https://github.com/openclaw/openclaw/pull/91008) | Closed in local gitcrawl 2026-06-11 | fix: address P2 cleanup items in model picker UI (PR #68927); no longer open. |
| [#90959](https://github.com/openclaw/openclaw/pull/90959) | Closed in local gitcrawl 2026-06-15 | fix(agents): apply default provider catalog timeout in all environments; no longer open. |
| [#90904](https://github.com/openclaw/openclaw/pull/90904) | Closed in local gitcrawl 2026-06-11 | fix(doctor): match short-term memory files with -HHMM timestamp suffixes; no longer open. |
| [#90896](https://github.com/openclaw/openclaw/issues/90896) | Closed in local gitcrawl 2026-06-07 | Bug: isShortTermMemoryPath regex skips daily memory files with timestamp suffixes (e.g. YYYY-MM-DD-HHMM.md); no longer open. |
| [#90884](https://github.com/openclaw/openclaw/pull/90884) | Closed in local gitcrawl 2026-06-11 | fix(agent): exclude Microsoft Foundry alias providers from DeepSeek V4 thinking wrapper; no longer open. |
| [#90878](https://github.com/openclaw/openclaw/issues/90878) | Closed in local gitcrawl 2026-06-07 | OAuth Codex profile falls back after openai-codex to openai namespace mismatch; no longer open. |
| [#90877](https://github.com/openclaw/openclaw/issues/90877) | Closed in local gitcrawl 2026-06-07 | Issue on memory-lancedb; no longer open. |
| [#90863](https://github.com/openclaw/openclaw/pull/90863) | Closed in local gitcrawl 2026-06-11 | fix(minimax): expose xhigh and max thinking levels for MiniMax-M3; no longer open. |
| [#90830](https://github.com/openclaw/openclaw/pull/90830) | Closed in local gitcrawl 2026-06-11 | fix(microsoft-foundry): suppress DeepSeek V4 thinking on alias provider ids (#90520); no longer open. |
| [#90825](https://github.com/openclaw/openclaw/pull/90825) | Closed in local gitcrawl 2026-06-12 | fix(llm): warn on unknown model pricing; no longer open. |
| [#90811](https://github.com/openclaw/openclaw/pull/90811) | Closed in local gitcrawl 2026-06-11 | fix(agents): stabilize user-turn serialization across turns to preserve prompt cache; no longer open. |
| [#90810](https://github.com/openclaw/openclaw/issues/90810) | Closed in local gitcrawl 2026-06-07 | [Bug]: Prompt cache invalidated on every user turn on full-resend transports — transient timestamp + content-form decoration on the current user message (regression from #3658); no longer open. |
| [#90793](https://github.com/openclaw/openclaw/pull/90793) | Closed in local gitcrawl 2026-06-11 | Fix OpenAI audio auth to use API keys; no longer open. |
| [#90758](https://github.com/openclaw/openclaw/issues/90758) | Closed in local gitcrawl 2026-06-06 | Channel-level agentId for iMessage, WhatsApp, and Telegram DMs (escape-hatch routing); no longer open. |
| [#90748](https://github.com/openclaw/openclaw/pull/90748) | Closed in local gitcrawl 2026-06-11 | fix(memory): resolve adapter default model in plain status identity check; no longer open. |
| [#90726](https://github.com/openclaw/openclaw/issues/90726) | Closed in local gitcrawl 2026-06-06 | [Bug] Cron jobs terminate immediately on HTTP 500 errors without triggering configured fallback mechanism / Cron 任务在遇到 HTTP 500 错误时直接中止，未能触发配置的 Fallback 机制; no longer open. |
| [#90717](https://github.com/openclaw/openclaw/pull/90717) | Closed in local gitcrawl 2026-06-06 | fix(agents): re-probe single-provider primary during cooldown; no longer open. |
| [#90706](https://github.com/openclaw/openclaw/pull/90706) | Closed in local gitcrawl 2026-06-15 | fix(OpenAI Responses): disable item id replay for storeless providers; no longer open. |
| [#90705](https://github.com/openclaw/openclaw/pull/90705) | Closed in local gitcrawl 2026-06-11 | fix(llm): preserve streamed tool args when Responses done omits arguments; no longer open. |
| [#90702](https://github.com/openclaw/openclaw/issues/90702) | Closed in local gitcrawl 2026-06-06 | [Bug]: blockedUntil for subscription_limit set far in the future never re-probes when no fallback is configured; no longer open. |
| [#90686](https://github.com/openclaw/openclaw/pull/90686) | Closed in local gitcrawl 2026-06-15 | fix(gateway): honor profile auth for SecretRef model entries; no longer open. |
| [#90685](https://github.com/openclaw/openclaw/issues/90685) | Closed in local gitcrawl 2026-06-15 | models.list marks auth-profile-backed SecretRef providers unavailable; no longer open. |
| [#90657](https://github.com/openclaw/openclaw/issues/90657) | Closed in local gitcrawl 2026-06-11 | tracking(OpenAI Responses): reproduce storeless replay and strict state/stream regressions in GitHub Actions; no longer open. |
| [#90613](https://github.com/openclaw/openclaw/pull/90613) | Closed in local gitcrawl 2026-06-06 | fix(agents): propagate ADC credential marker so google-vertex passes isWritableProviderConfig; no longer open. |
| [#90609](https://github.com/openclaw/openclaw/pull/90609) | Closed in local gitcrawl 2026-06-11 | fix(google): preserve Vertex ADC catalog auth; no longer open. |
| [#90594](https://github.com/openclaw/openclaw/pull/90594) | Closed in local gitcrawl 2026-06-06 | fix(android): align provider readiness with available models; no longer open. |
| [#90593](https://github.com/openclaw/openclaw/pull/90593) | Closed in local gitcrawl 2026-06-11 | fix: preserve LM Studio Responses tool arguments; no longer open. |
| [#90585](https://github.com/openclaw/openclaw/issues/90585) | Closed in local gitcrawl 2026-06-11 | [Bug]: [REGRESSION] Tool calls with arguments arrive as empty objects when using LM Studio (openai-responses API).; no longer open. |
| [#90570](https://github.com/openclaw/openclaw/issues/90570) | Closed in local gitcrawl 2026-06-11 | Azure AI Foundry models (/openai/v1/responses) fail with 400 Invalid value and 400 schema mismatch across all GPT-5.x deployments; no longer open. |
| [#90567](https://github.com/openclaw/openclaw/issues/90567) | Closed in local gitcrawl 2026-06-15 | Bug: pdf tool fails with 401 on xiaomi token-plan provider; no longer open. |
| [#90539](https://github.com/openclaw/openclaw/pull/90539) | Closed in local gitcrawl 2026-06-06 | fix(agents): skip foundry aliases for deepseek thinking; no longer open. |
| [#90538](https://github.com/openclaw/openclaw/issues/90538) | Closed in local gitcrawl 2026-06-06 | [Bug] Memory Dreaming Promotion silently no-ops: cron isolated sessions get trigger=user instead of cron; no longer open. |
| [#90533](https://github.com/openclaw/openclaw/pull/90533) | Closed in local gitcrawl 2026-06-06 | fix(openai): accept missing content-type on ChatGPT Responses SSE stream; no longer open. |
| [#90520](https://github.com/openclaw/openclaw/issues/90520) | Closed in local gitcrawl 2026-06-11 | Microsoft Foundry DeepSeek V4 alias providers still inject `thinking` after #87737 fix; no longer open. |
| [#90513](https://github.com/openclaw/openclaw/pull/90513) | Closed in local gitcrawl 2026-06-15 | fix(anthropic): add haiku catalog entry; no longer open. |
| [#90507](https://github.com/openclaw/openclaw/pull/90507) | Closed in local gitcrawl 2026-06-11 | fix(doctor): preserve codex context metadata; no longer open. |
| [#90506](https://github.com/openclaw/openclaw/issues/90506) | Closed in local gitcrawl 2026-06-06 | [Bug]: [Bug]: google-vertex models fail with model_not_found at runtime on 2026.5.28 and 2026.6.1 — direct Vertex API calls succeed with same credentials; no longer open. |
| [#90496](https://github.com/openclaw/openclaw/issues/90496) | Closed in local gitcrawl 2026-06-12 | Discord channel remains trapped in oversized session after /new; compaction fails provider_error_4xx and model drifts from codex/gpt-5.5 to gpt-5.4; no longer open. |
| [#90457](https://github.com/openclaw/openclaw/pull/90457) | Closed in local gitcrawl 2026-06-11 | fix(models): persist agent catalog cache; no longer open. |
| [#90436](https://github.com/openclaw/openclaw/pull/90436) | Closed in local gitcrawl 2026-06-06 | Add NVIDIA Nemotron 3 Ultra default; no longer open. |
| [#90429](https://github.com/openclaw/openclaw/pull/90429) | Closed in local gitcrawl 2026-06-11 | Fix LM Studio wizard prompter binding; no longer open. |
| [#90425](https://github.com/openclaw/openclaw/pull/90425) | Closed in local gitcrawl 2026-06-06 | fix(openai): preserve encrypted reasoning replay ids; no longer open. |
| [#90422](https://github.com/openclaw/openclaw/pull/90422) | Closed in local gitcrawl 2026-06-06 | fix(memory-core): keep durable index identity visible during safe reindex; no longer open. |
| [#90413](https://github.com/openclaw/openclaw/issues/90413) | Closed in local gitcrawl 2026-06-07 | memory status always reports "Vector search: paused" with blank expected model (2026.6.1); no longer open. |
| [#90403](https://github.com/openclaw/openclaw/issues/90403) | Closed in local gitcrawl 2026-06-15 | [Performance] Model Picker UI very slow in v2026.5.28; no longer open. |
| [#90399](https://github.com/openclaw/openclaw/pull/90399) | Closed in local gitcrawl 2026-06-06 | fix(openai): accept missing content-type on ChatGPT Responses SSE stream; no longer open. |
| [#90395](https://github.com/openclaw/openclaw/pull/90395) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): write meta after sync when identity is missing with existing chunks; no longer open. |
| [#90382](https://github.com/openclaw/openclaw/issues/90382) | Closed in local gitcrawl 2026-06-06 | [Bug]: ChatGPT-OAuth gpt-5.5 fails with invalid_provider_content_type after 2026.6.1 (SDK Responses stream missing Accept: text/event-stream); no longer open. |
| [#90368](https://github.com/openclaw/openclaw/issues/90368) | Closed in local gitcrawl 2026-06-15 | 2026.6.1: agent_model_catalogs / model_capability_cache tables defined but never written; models list takes 25–53s; no longer open. |
| [#90338](https://github.com/openclaw/openclaw/issues/90338) | Closed in local gitcrawl 2026-06-11 | Memory index meta never written when gateway auto-sync finds identity missing with existing chunks; no longer open. |
| [#90337](https://github.com/openclaw/openclaw/pull/90337) | Closed in local gitcrawl 2026-06-11 | fix(anthropic): add Claude Haiku 4.5 to static model catalog; no longer open. |
| [#90336](https://github.com/openclaw/openclaw/pull/90336) | Closed in local gitcrawl 2026-06-11 | fix(memory): fail fast when embeddings provider is unavailable; no longer open. |
| [#90327](https://github.com/openclaw/openclaw/pull/90327) | Closed in local gitcrawl 2026-06-11 | fix(openai): tolerate missing content-type on streamed Codex responses; no longer open. |
| [#90326](https://github.com/openclaw/openclaw/pull/90326) | Closed in local gitcrawl 2026-06-15 | fix(fireworks): resolve catalog model params from plugin.json via core; no longer open. |
| [#90321](https://github.com/openclaw/openclaw/pull/90321) | Closed in local gitcrawl 2026-06-06 | Normalize legacy Codex session runtime state; no longer open. |
| [#90319](https://github.com/openclaw/openclaw/pull/90319) | Closed in local gitcrawl 2026-06-06 | Add Codex session route migration coverage; no longer open. |
| [#90317](https://github.com/openclaw/openclaw/pull/90317) | Closed in local gitcrawl 2026-06-06 | Add Codex multi-agent config migration coverage; no longer open. |
| [#90315](https://github.com/openclaw/openclaw/issues/90315) | Closed in local gitcrawl 2026-06-11 | [Bug]: Ollama Cloud live-discovered model loses capability metadata in gateway catalog; no longer open. |
| [#90310](https://github.com/openclaw/openclaw/pull/90310) | Closed in local gitcrawl 2026-06-12 | fix(openai-responses): sanitize null content before SDK serialization (#90094); no longer open. |
| [#90304](https://github.com/openclaw/openclaw/pull/90304) | Closed in local gitcrawl 2026-06-06 | feat(memory): support qmd query rerank toggle; no longer open. |
| [#90264](https://github.com/openclaw/openclaw/pull/90264) | Closed in local gitcrawl 2026-06-06 | fix(memory): move local embeddings to llama.cpp provider; no longer open. |
| [#90260](https://github.com/openclaw/openclaw/pull/90260) | Closed in local gitcrawl 2026-06-11 | fix(agents): decode xai and venice tool-call arguments exactly once; no longer open. |
| [#90242](https://github.com/openclaw/openclaw/pull/90242) | Closed in local gitcrawl 2026-06-15 | fix(providers): skip unreadable Mistral tool schemas; no longer open. |
| [#90235](https://github.com/openclaw/openclaw/pull/90235) | Closed in local gitcrawl 2026-06-15 | fix(gateway): repair Ollama dense stream — preserve replacement stream deltas and rich tool call deltas; no longer open. |
| [#90221](https://github.com/openclaw/openclaw/pull/90221) | Closed in local gitcrawl 2026-06-06 | fix(compaction): allow compaction with aws-sdk auth without apiKey or headers; no longer open. |
| [#90210](https://github.com/openclaw/openclaw/pull/90210) | Closed in local gitcrawl 2026-06-15 | fix(anthropic): add claude-haiku-4-5 to static model catalog; no longer open. |
| [#90205](https://github.com/openclaw/openclaw/pull/90205) | Closed in local gitcrawl 2026-06-06 | fix: tolerate missing streamed response content type; no longer open. |
| [#90165](https://github.com/openclaw/openclaw/pull/90165) | Closed in local gitcrawl 2026-06-11 | fix(memory): do not filter FTS keyword search by embedding model (#48300); no longer open. |
| [#90149](https://github.com/openclaw/openclaw/pull/90149) | Closed in local gitcrawl 2026-06-11 | fix: preserve user model on stale rollover; no longer open. |
| [#90146](https://github.com/openclaw/openclaw/issues/90146) | Closed in local gitcrawl 2026-06-06 | google-vertex: Missing gemini-3.1-flash-lite in provider catalog causes silent failure instead of error; no longer open. |
| [#90145](https://github.com/openclaw/openclaw/pull/90145) | Closed in local gitcrawl 2026-06-06 | fix: protect global agent config defaults [AI]; no longer open. |
| [#90138](https://github.com/openclaw/openclaw/pull/90138) | Closed in local gitcrawl 2026-06-11 | fix(minimax): exempt M3 from thinking-disabled wrapper; no longer open. |
| [#90137](https://github.com/openclaw/openclaw/pull/90137) | Closed in local gitcrawl 2026-06-06 | fix: strip thinking signatures from entries after compaction; no longer open. |
| [#90128](https://github.com/openclaw/openclaw/pull/90128) | Closed in local gitcrawl 2026-06-12 | fix(sessions): preserve user /model override across daily/idle session rollover (#90119); no longer open. |
| [#90124](https://github.com/openclaw/openclaw/pull/90124) | Closed in local gitcrawl 2026-06-06 | fix(agents): harden tool-call handling against A2A/model tool-call poisoning; no longer open. |
| [#90119](https://github.com/openclaw/openclaw/issues/90119) | Closed in local gitcrawl 2026-06-12 | [Bug]: User /model override silently dropped on daily/idle session rollover (survives /new but not the 4AM reset); no longer open. |
| [#90116](https://github.com/openclaw/openclaw/pull/90116) | Closed in local gitcrawl 2026-06-15 | fix: add Claude Haiku 4.5 static catalog entries; no longer open. |
| [#90110](https://github.com/openclaw/openclaw/pull/90110) | Closed in local gitcrawl 2026-06-15 | fix(anthropic): resolve Claude Haiku 4.5 static catalog refs; no longer open. |
| [#90106](https://github.com/openclaw/openclaw/pull/90106) | Closed in local gitcrawl 2026-06-15 | fix: add Claude Haiku 4.5 to static model catalog; no longer open. |
| [#90088](https://github.com/openclaw/openclaw/issues/90088) | Closed in local gitcrawl 2026-06-15 | anthropic (api_key) provider: Claude Haiku 4.5 missing from static model catalog → "Unknown model" (model_not_found); no longer open. |
| [#90086](https://github.com/openclaw/openclaw/issues/90086) | Closed in local gitcrawl 2026-06-15 | Pi/native runtime routes openai-chatgpt-responses to boundary-aware transport and fails on ChatGPT Codex endpoint; no longer open. |
| [#90083](https://github.com/openclaw/openclaw/issues/90083) | Closed in local gitcrawl 2026-06-12 | [Bug]: 2026.6.1 OpenAI ChatGPT Responses transport fails with invalid_provider_content_type for gpt-5.4/gpt-5.5; no longer open. |
| [#90075](https://github.com/openclaw/openclaw/pull/90075) | Closed in local gitcrawl 2026-06-06 | fix(agents): detect unsigned thinking-only stall when reasoning payload inflates payloadCount; no longer open. |
| [#90056](https://github.com/openclaw/openclaw/pull/90056) | Closed in local gitcrawl 2026-06-11 | fix(doctor): merge disjoint openai-codex model entries into canonical openai provider; no longer open. |
| [#90051](https://github.com/openclaw/openclaw/pull/90051) | Closed in local gitcrawl 2026-06-11 | fix(agents): strip reasoning tags from chat replies; no longer open. |
| [#90047](https://github.com/openclaw/openclaw/issues/90047) | Closed in local gitcrawl 2026-06-11 | Codex migration (2026.6.1) drops the gpt-5.5 model when a canonical `openai` provider exists for embeddings — agents go silent; no longer open. |
| [#90029](https://github.com/openclaw/openclaw/pull/90029) | Closed in local gitcrawl 2026-06-11 | feat: add live provider model catalog helper; no longer open. |
| [#90028](https://github.com/openclaw/openclaw/pull/90028) | Closed in local gitcrawl 2026-06-06 | docs: clarify legacy openai-codex auth; no longer open. |
| [#90021](https://github.com/openclaw/openclaw/issues/90021) | Closed in local gitcrawl 2026-06-12 | OpenAI model with agentRuntime.id "openclaw" appears to switch to OpenAI Codex runtime after first Telegram message; no longer open. |
| [#89976](https://github.com/openclaw/openclaw/issues/89976) | Closed in local gitcrawl 2026-06-04 | [Bug]: Manual /compact on Codex OAuth sessions resolves to direct openai auth instead of Codex runtime; no longer open. |
| [#89957](https://github.com/openclaw/openclaw/pull/89957) | Closed in local gitcrawl 2026-06-12 | docs: add section on extending memory with corpus supplements; no longer open. |
| [#89952](https://github.com/openclaw/openclaw/pull/89952) | Closed in local gitcrawl 2026-06-11 | fix(plugins): guard provider auth choice metadata; no longer open. |
| [#89941](https://github.com/openclaw/openclaw/pull/89941) | Closed in local gitcrawl 2026-06-04 | fix(issue): resolve #89425 [Bug]: Missing extensions/speech-core/ in npm tarball (v2026; no longer open. |
| [#89937](https://github.com/openclaw/openclaw/issues/89937) | Closed in local gitcrawl 2026-06-06 | [Bug] before_prompt_build hook not triggered in agent-runner / embedded-agent path (chat user messages); no longer open. |
| [#89918](https://github.com/openclaw/openclaw/pull/89918) | Closed in local gitcrawl 2026-06-11 | fix(vertex): route eu/us multi-region to .rep.googleapis.com host; no longer open. |
| [#89910](https://github.com/openclaw/openclaw/pull/89910) | Closed in local gitcrawl 2026-06-11 | fix(plugins): guard provider auth choice metadata; no longer open. |
| [#89901](https://github.com/openclaw/openclaw/pull/89901) | Closed in local gitcrawl 2026-06-11 | fix(vertex): support eu and us multi-region endpoints; no longer open. |
| [#89891](https://github.com/openclaw/openclaw/issues/89891) | Closed in local gitcrawl 2026-06-11 | [Bug]: Vertex AI eu multi-region unreachable — host prefix is hardcoded; no longer open. |
| [#89874](https://github.com/openclaw/openclaw/pull/89874) | Closed in local gitcrawl 2026-06-06 | fix(agents): detect unsigned thinking-only stall when reasoning payload inflates payloadCount; no longer open. |
| [#89845](https://github.com/openclaw/openclaw/pull/89845) | Closed in local gitcrawl 2026-06-04 | fix(fireworks): optimize caching with x-session-affinity; no longer open. |
| [#89832](https://github.com/openclaw/openclaw/pull/89832) | Closed in local gitcrawl 2026-06-11 | fix(config): allow requiresReasoningContentOnAssistantMessages in ModelCompatSchema; no longer open. |
| [#89787](https://github.com/openclaw/openclaw/issues/89787) | Closed in local gitcrawl 2026-06-06 | [Bug]: Agent stalls indefinitely when model emits stopReason="stop" with no toolCall — only thinking block generated; no longer open. |
| [#89741](https://github.com/openclaw/openclaw/pull/89741) | Closed in local gitcrawl 2026-06-15 | fix(memory): add EPERM fallback for atomic reindex; no longer open. |
| [#89729](https://github.com/openclaw/openclaw/pull/89729) | Closed in local gitcrawl 2026-06-11 | fix（OpenAI Responses/provider）: skip Responses item id replay when store support is stripped; no longer open. |
| [#89728](https://github.com/openclaw/openclaw/issues/89728) | Closed in local gitcrawl 2026-06-15 | Custom OpenAI Responses-compatible providers still replay item ids when store support is stripped; no longer open. |
| [#89706](https://github.com/openclaw/openclaw/issues/89706) | Closed in local gitcrawl 2026-06-06 | github-copilot: gemini-3.1-pro appears in models list but fails silently when selected; no longer open. |
| [#89692](https://github.com/openclaw/openclaw/pull/89692) | Closed in local gitcrawl 2026-06-11 | fix(config): allow compat.requiresReasoningContentOnAssistantMessages in model config; no longer open. |
| [#89691](https://github.com/openclaw/openclaw/issues/89691) | Closed in local gitcrawl 2026-06-07 | Active-memory embedded memory_search intermittently loses embedding provider and falls back to FTS-only; no longer open. |
| [#89685](https://github.com/openclaw/openclaw/pull/89685) | Closed in local gitcrawl 2026-06-04 | fix(acpx): handle Claude ACP model startup options; no longer open. |
| [#89667](https://github.com/openclaw/openclaw/pull/89667) | Closed in local gitcrawl 2026-06-11 | fix(config): allow requiresReasoningContentOnAssistantMessages in ModelCompatSchema [AI-assisted]; no longer open. |
| [#89660](https://github.com/openclaw/openclaw/issues/89660) | Closed in local gitcrawl 2026-06-11 | [Bug]: requiresReasoningContentOnAssistantMessages missing from ModelCompatSchema — can't replicate native DeepSeek behavior on custom providers; no longer open. |
| [#89652](https://github.com/openclaw/openclaw/pull/89652) | Closed in local gitcrawl 2026-06-11 | fix(plugins): load owning plugin for configured memory embedding provider at startup; no longer open. |
| [#89651](https://github.com/openclaw/openclaw/issues/89651) | Closed in local gitcrawl 2026-06-07 | Gateway startup does not load the plugin owning a configured memory embedding provider (memorySearch.provider); no longer open. |
| [#89629](https://github.com/openclaw/openclaw/pull/89629) | Closed in local gitcrawl 2026-06-15 | feat(hooks): per-turn usageState (provider limits + rich atoms) on reply_payload_sending; no longer open. |
| [#89613](https://github.com/openclaw/openclaw/pull/89613) | Closed in local gitcrawl 2026-06-06 | docs: document auth profile failure policy contract; no longer open. |
| [#89610](https://github.com/openclaw/openclaw/pull/89610) | Closed in local gitcrawl 2026-06-03 | Add channel-scoped memory search filters; no longer open. |
| [#89561](https://github.com/openclaw/openclaw/pull/89561) | Closed in local gitcrawl 2026-06-11 | fix(hooks): honor session-memory hook model override for LLM slug generation [AI-assisted]; no longer open. |
| [#89560](https://github.com/openclaw/openclaw/pull/89560) | Closed in local gitcrawl 2026-06-04 | fix(telegram): isolate verbose status after streamed finals; no longer open. |
| [#89540](https://github.com/openclaw/openclaw/issues/89540) | Closed in local gitcrawl 2026-06-04 | [Bug]: Telegram /v Active Memory status can overwrite short streamed replies; no longer open. |
| [#89508](https://github.com/openclaw/openclaw/pull/89508) | Closed in local gitcrawl 2026-06-12 | fix(models): clarify provider model registration hint; no longer open. |
| [#89479](https://github.com/openclaw/openclaw/pull/89479) | Closed in local gitcrawl 2026-06-03 | fix: auto-fix for issue #89431; no longer open. |
| [#89460](https://github.com/openclaw/openclaw/pull/89460) | Closed in local gitcrawl 2026-06-03 | fix(models): preserve provider prompt cache boundaries; no longer open. |
| [#89441](https://github.com/openclaw/openclaw/pull/89441) | Closed in local gitcrawl 2026-06-03 | fix: add missing extensions/speech-core/ source files for npm tarball; no longer open. |
| [#89440](https://github.com/openclaw/openclaw/pull/89440) | Closed in local gitcrawl 2026-06-03 | fix(llm): keep OpenAI-compatible reasoning streams active; no longer open. |
| [#89427](https://github.com/openclaw/openclaw/pull/89427) | Closed in local gitcrawl 2026-06-03 | fix: add missing extensions/speech-core/ source files for npm tarball; no longer open. |
| [#89420](https://github.com/openclaw/openclaw/pull/89420) | Closed in local gitcrawl 2026-06-03 | fix(llm): filter out reasoning_content from streaming output when reasoning is disabled; no longer open. |
| [#89400](https://github.com/openclaw/openclaw/pull/89400) | Closed in local gitcrawl 2026-06-03 | fix(google): add missing gemini-3.1-flash-lite to google-vertex catalog; no longer open. |
| [#89390](https://github.com/openclaw/openclaw/issues/89390) | Closed in local gitcrawl 2026-06-03 | google-vertex: gemini-3.1-flash-lite missing from pi-ai model catalog, causes silent failure with no fallback; no longer open. |
| [#89389](https://github.com/openclaw/openclaw/issues/89389) | Closed in local gitcrawl 2026-06-03 | [Bug]: MiniMax Global OAuth fails with Connect Timeout (api.minimax.io/oauth/code now redirects); no longer open. |
| [#89386](https://github.com/openclaw/openclaw/issues/89386) | Closed in local gitcrawl 2026-06-03 | Bug: 5.28 transport refactor regressed prompt caching for Anthropic and OpenAI-compatible providers; no longer open. |
| [#89382](https://github.com/openclaw/openclaw/issues/89382) | Closed in local gitcrawl 2026-06-03 | GitHub Copilot timeout marks auth profile in cooldown and blocks same-provider fallback models; no longer open. |
| [#89379](https://github.com/openclaw/openclaw/pull/89379) | Closed in local gitcrawl 2026-06-03 | fix(providers): use native reasoning mode for Gemini instead of tagged; no longer open. |
| [#89347](https://github.com/openclaw/openclaw/pull/89347) | Closed in local gitcrawl 2026-06-03 | fix: repair model provider edge cases; no longer open. |
| [#89343](https://github.com/openclaw/openclaw/pull/89343) | Closed in local gitcrawl 2026-06-03 | fix(llm): prevent reasoning_content leak when reasoning is disabled; no longer open. |
| [#89330](https://github.com/openclaw/openclaw/issues/89330) | Closed in local gitcrawl 2026-06-03 | Bug: non-persistent Responses routes replay stale item ids; no longer open. |
| [#89305](https://github.com/openclaw/openclaw/pull/89305) | Closed in local gitcrawl 2026-06-03 | fix(agents): bypass stale auth for plugin harnesses; no longer open. |
| [#89298](https://github.com/openclaw/openclaw/pull/89298) | Closed in local gitcrawl 2026-06-03 | fix(diagnostics): re-queue pending messages after stuck-session recovery aborts ghost run; no longer open. |
| [#89293](https://github.com/openclaw/openclaw/pull/89293) | Closed in local gitcrawl 2026-06-03 | fix(logging): requeue stuck session lane after abort; no longer open. |
| [#89290](https://github.com/openclaw/openclaw/pull/89290) | Closed in local gitcrawl 2026-06-11 | [codex] Keep Codex waiting after raw reasoning progress; no longer open. |
| [#89251](https://github.com/openclaw/openclaw/pull/89251) | Closed in local gitcrawl 2026-06-12 | fix: deliver tts tool audio on whatsapp; no longer open. |
| [#89248](https://github.com/openclaw/openclaw/pull/89248) | Closed in local gitcrawl 2026-06-03 | feat(context-engine): context-capsule plugin — 99.3% token reduction with recovery-score gate; no longer open. |
| [#89244](https://github.com/openclaw/openclaw/pull/89244) | Closed in local gitcrawl 2026-06-04 | fix(memory): warn on high runtime watcher pressure; no longer open. |
| [#89208](https://github.com/openclaw/openclaw/issues/89208) | Closed in local gitcrawl 2026-06-03 | Stuck-session recovery discards queued user messages after aborting ghost run; no longer open. |
| [#89192](https://github.com/openclaw/openclaw/issues/89192) | Closed in local gitcrawl 2026-06-12 | bug(models): model_not_found remediation message is incomplete — suggests `{ "id": ... }` but `name` is required and `api`/`baseUrl` are silently needed (misroutes to OpenAI); no longer open. |
| [#89188](https://github.com/openclaw/openclaw/pull/89188) | Closed in local gitcrawl 2026-06-02 | fix(memory-core): reduce Linux watcher fan-out; no longer open. |
| [#89185](https://github.com/openclaw/openclaw/pull/89185) | Closed in local gitcrawl 2026-06-02 | fix(memory): default gateway memory watch off; no longer open. |
| [#89181](https://github.com/openclaw/openclaw/pull/89181) | Closed in local gitcrawl 2026-06-02 | fix(agents): dispatch auth failures by type; no longer open. |
| [#89165](https://github.com/openclaw/openclaw/issues/89165) | Closed in local gitcrawl 2026-06-02 | HTTP 400 quota/usage_limit errors do not trigger provider fallback chain; no longer open. |
| [#89150](https://github.com/openclaw/openclaw/pull/89150) | Closed in local gitcrawl 2026-06-15 | obs(model-fallback): emit `model.fallback.exhausted` counter on chain exhaustion; no longer open. |
| [#89139](https://github.com/openclaw/openclaw/issues/89139) | Closed in local gitcrawl 2026-06-04 | webchat creates new agent run per message, destroying prompt cache (93% → 29% hit rate); no longer open. |
| [#89138](https://github.com/openclaw/openclaw/pull/89138) | Closed in local gitcrawl 2026-06-11 | fix #88009: [Feature]: batched memory embedding should batch over files; no longer open. |
| [#89128](https://github.com/openclaw/openclaw/pull/89128) | Closed in local gitcrawl 2026-06-03 | fix: skip Responses item id replay without store; no longer open. |
| [#89112](https://github.com/openclaw/openclaw/issues/89112) | Closed in local gitcrawl 2026-06-02 | chore: OpenAI API key update requires manual edits in multiple agent auth.json files; no longer open. |
| [#89109](https://github.com/openclaw/openclaw/pull/89109) | Closed in local gitcrawl 2026-06-11 | fix(agents): block message-tool spam loops defeated by volatile message ids; no longer open. |
| [#89102](https://github.com/openclaw/openclaw/pull/89102) | Closed in local gitcrawl 2026-06-06 | refactor(auth): store auth profiles in SQLite; no longer open. |
| [#89091](https://github.com/openclaw/openclaw/pull/89091) | Closed in local gitcrawl 2026-06-12 | fix(memory-core): retry narrative message reads; no longer open. |
| [#89090](https://github.com/openclaw/openclaw/issues/89090) | Closed in local gitcrawl 2026-06-11 | Bug: loopDetection cannot block message tool loops — volatile messageId in result defeats all critical-level detection paths; no longer open. |
| [#89070](https://github.com/openclaw/openclaw/pull/89070) | Closed in local gitcrawl 2026-06-04 | fix(stream): handle cumulative JSON chunks from local llama.cpp tool calls; no longer open. |
| [#89049](https://github.com/openclaw/openclaw/pull/89049) | Closed in local gitcrawl 2026-06-03 | fix(idle-timeout): honor provider timeout for no-timeout runs; no longer open. |
| [#89032](https://github.com/openclaw/openclaw/issues/89032) | Closed in local gitcrawl 2026-06-02 | MiMo v2.5: reasoning_content not preserved for custom xiaomi-coding provider (400 in multi-turn tool calls); no longer open. |
| [#89027](https://github.com/openclaw/openclaw/pull/89027) | Closed in local gitcrawl 2026-06-11 | fix(cli): prevent empty_response failover for completed thinking-only turns; no longer open. |
| [#89008](https://github.com/openclaw/openclaw/issues/89008) | Closed in local gitcrawl 2026-06-03 | claude-cli thinking-only (end_turn, empty text) turns trigger empty_response model-fallback re-run on a different model; no longer open. |
| [#89001](https://github.com/openclaw/openclaw/pull/89001) | Closed in local gitcrawl 2026-06-11 | fix: support Azure Responses text stream events; no longer open. |
| [#88999](https://github.com/openclaw/openclaw/pull/88999) | Closed in local gitcrawl 2026-06-11 | fix(cron): repair concatenated JSON keys from local-model tool-call parsers; no longer open. |
| [#88994](https://github.com/openclaw/openclaw/pull/88994) | Closed in local gitcrawl 2026-06-11 | fix(agents): quarantine normalized runtime tools; no longer open. |
| [#88976](https://github.com/openclaw/openclaw/pull/88976) | Closed in local gitcrawl 2026-06-03 | fix(mistral): enable prompt cache key compat; no longer open. |
| [#88964](https://github.com/openclaw/openclaw/pull/88964) | Closed in local gitcrawl 2026-06-06 | fix(agents): repair context-engine tool-result pairing; no longer open. |
| [#88958](https://github.com/openclaw/openclaw/pull/88958) | Closed in local gitcrawl 2026-06-12 | Fix BTW OAuth side-question routing; no longer open. |
| [#88956](https://github.com/openclaw/openclaw/pull/88956) | Closed in local gitcrawl 2026-06-12 | Repair compacted tool-result chains; no longer open. |
| [#88946](https://github.com/openclaw/openclaw/pull/88946) | Closed in local gitcrawl 2026-06-03 | Fix live model inference edge cases; no longer open. |
| [#88940](https://github.com/openclaw/openclaw/pull/88940) | Closed in local gitcrawl 2026-06-06 | fix(llm): repairJson injects control chars for backslash b/f/n/r/t into Windows paths; no longer open. |
| [#88938](https://github.com/openclaw/openclaw/issues/88938) | Closed in local gitcrawl 2026-06-02 | [Feature]: know what model is used by the image tool; no longer open. |
| [#88928](https://github.com/openclaw/openclaw/pull/88928) | Closed in local gitcrawl 2026-06-02 | fix(llm): preserve Windows path control escapes; no longer open. |
| [#88926](https://github.com/openclaw/openclaw/pull/88926) | Closed in local gitcrawl 2026-06-03 | fix(llm): preserve Windows path escapes in streamed args; no longer open. |
| [#88924](https://github.com/openclaw/openclaw/pull/88924) | Closed in local gitcrawl 2026-06-02 | fix(agents): strip streamed reasoning tags; no longer open. |
| [#88922](https://github.com/openclaw/openclaw/pull/88922) | Closed in local gitcrawl 2026-06-03 | fix(google): forward stop sequences to Gemini generationConfig; no longer open. |
| [#88918](https://github.com/openclaw/openclaw/issues/88918) | Closed in local gitcrawl 2026-06-03 | [Bug]: Streaming repairJson injects control chars into unescaped Windows paths in tool-call arguments; no longer open. |
| [#88917](https://github.com/openclaw/openclaw/pull/88917) | Closed in local gitcrawl 2026-06-12 | fix: retry stale Responses reasoning replay safely; no longer open. |
| [#88896](https://github.com/openclaw/openclaw/pull/88896) | Closed in local gitcrawl 2026-06-02 | fix: harden CLI and plugin edge cases; no longer open. |
| [#88893](https://github.com/openclaw/openclaw/pull/88893) | Closed in local gitcrawl 2026-06-11 | fix: support Azure Responses API text content type; no longer open. |
| [#88890](https://github.com/openclaw/openclaw/pull/88890) | Closed in local gitcrawl 2026-06-06 | fix #87768: [Bug]: push to talk mac os companion app hard codes thinking low; no longer open. |
| [#88882](https://github.com/openclaw/openclaw/pull/88882) | Closed in local gitcrawl 2026-06-11 | test(gateway): add small model live profile; no longer open. |
| [#88874](https://github.com/openclaw/openclaw/issues/88874) | Closed in local gitcrawl 2026-06-02 | [Bug]: cron openai/gpt-5.4-mini ignores agentRuntime=openclaw/pi and routes to openai-codex with zero tools; no longer open. |
| [#88873](https://github.com/openclaw/openclaw/pull/88873) | Closed in local gitcrawl 2026-06-02 | fix(agent-os): harden full-local substrate; no longer open. |
| [#88861](https://github.com/openclaw/openclaw/pull/88861) | Closed in local gitcrawl 2026-06-02 | Fix OpenResponses callback message context; no longer open. |
| [#88851](https://github.com/openclaw/openclaw/pull/88851) | Closed in local gitcrawl 2026-06-02 | Persist OpenRouter model cache in SQLite; no longer open. |
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
| [#88787](https://github.com/openclaw/openclaw/pull/88787) | Closed in local gitcrawl 2026-06-02 | feat(openai): support gpt-5.5 azure routing and reasoning, restrict telegram bot access; no longer open. |
| [#88781](https://github.com/openclaw/openclaw/pull/88781) | Closed in local gitcrawl 2026-06-01 | fix(models): strip remaining provider self prefixes; no longer open. |
| [#88771](https://github.com/openclaw/openclaw/pull/88771) | Closed in local gitcrawl 2026-06-11 | fix(agents): stream phased text deltas incrementally; no longer open. |
| [#88770](https://github.com/openclaw/openclaw/issues/88770) | Closed in local gitcrawl 2026-06-01 | [Bug]: Self-prefix normalization gap remaining in google/xai/openai providers after #88587; no longer open. |
| [#88769](https://github.com/openclaw/openclaw/pull/88769) | Closed in local gitcrawl 2026-06-03 | fix(agents): keep inline <think> reasoning out of OpenAI-compatible visible text; no longer open. |
| [#88767](https://github.com/openclaw/openclaw/pull/88767) | Closed in local gitcrawl 2026-06-02 | fix(plugin-sdk): isolate provider catalog projection failures; no longer open. |
| [#88761](https://github.com/openclaw/openclaw/pull/88761) | Closed in local gitcrawl 2026-06-01 | [codex] Surface disabled Codex plugin routes in doctor lint; no longer open. |
| [#88759](https://github.com/openclaw/openclaw/pull/88759) | Closed in local gitcrawl 2026-06-01 | fix: repair providerless Codex session overrides; no longer open. |
| [#88751](https://github.com/openclaw/openclaw/issues/88751) | Closed in local gitcrawl 2026-06-01 | [Bug]: doctor lint misses disabled codex plugin required by native codex runtime; no longer open. |
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
| [#88672](https://github.com/openclaw/openclaw/pull/88672) | Closed in local gitcrawl 2026-06-01 | fix(plugins): reuse current metadata snapshot in provider hot paths; no longer open. |
| [#88671](https://github.com/openclaw/openclaw/issues/88671) | Closed in local gitcrawl 2026-06-02 | [Bug]: [assistant reasoning omitted] appears with reasoningDefault off on Ollama models; no longer open. |
| [#88669](https://github.com/openclaw/openclaw/pull/88669) | Closed in local gitcrawl 2026-06-01 | fix(auth): skip no-op auth-profile disk writes on success; no longer open. |
| [#88667](https://github.com/openclaw/openclaw/pull/88667) | Closed in local gitcrawl 2026-06-01 | fix #81214: OpenClaw 2026.5.7 subagent regression; no longer open. |
| [#88654](https://github.com/openclaw/openclaw/issues/88654) | Closed in local gitcrawl 2026-06-01 | markAuthProfileSuccess rewrites auth-profiles.json on every success; no longer open. |
| [#88645](https://github.com/openclaw/openclaw/pull/88645) | Closed in local gitcrawl 2026-06-12 | fix(llm): use JSON5 as intermediate fallback in parseStreamingJson to avoid partial-json key corruption; no longer open. |
| [#88644](https://github.com/openclaw/openclaw/issues/88644) | Closed in local gitcrawl 2026-06-01 | doctor --fix breaks Codex model routing by rewriting openai-codex/ to openai/; no longer open. |
| [#88630](https://github.com/openclaw/openclaw/pull/88630) | Closed in local gitcrawl 2026-06-12 | fix(codex): avoid guardian review for local models; no longer open. |
| [#88615](https://github.com/openclaw/openclaw/issues/88615) | Closed in local gitcrawl 2026-06-11 | [Bug]: sqlite-vec fails to load on Node 22 Linux x64 (Vector store: unknown, distinct from #64776 and #65033); no longer open. |
| [#88612](https://github.com/openclaw/openclaw/pull/88612) | Closed in local gitcrawl 2026-06-01 | fix(models): keep auth login out of main config; no longer open. |
| [#88608](https://github.com/openclaw/openclaw/pull/88608) | Closed in local gitcrawl 2026-06-02 | fix(minimax): use account OAuth device endpoints; no longer open. |
| [#88596](https://github.com/openclaw/openclaw/issues/88596) | Closed in local gitcrawl 2026-06-02 | xAI models report incorrect context window (200k instead of 1M) — long_context_threshold misinterpreted; no longer open. |
| [#88587](https://github.com/openclaw/openclaw/pull/88587) | Closed in local gitcrawl 2026-06-01 | fix(agents): normalize prefixed Anthropic fallback model ids (#88560); no longer open. |
| [#88565](https://github.com/openclaw/openclaw/issues/88565) | Closed in local gitcrawl 2026-06-01 | models auth login overwrites and truncates main openclaw.json; no longer open. |
| [#88563](https://github.com/openclaw/openclaw/pull/88563) | Closed in local gitcrawl 2026-06-01 | fix(agents): resolve exact static-catalog models for plugin-harness cold start (#88510); no longer open. |
| [#88561](https://github.com/openclaw/openclaw/issues/88561) | Closed in local gitcrawl 2026-06-04 | lossless-claw compaction breaks tool_calls/tool message chain → 499 error on model switch; no longer open. |
| [#88560](https://github.com/openclaw/openclaw/issues/88560) | Closed in local gitcrawl 2026-06-01 | fallback iterator leaks one candidate modelId into subsequent provider lookup; no longer open. |
| [#88558](https://github.com/openclaw/openclaw/pull/88558) | Closed in local gitcrawl 2026-06-01 | fix(gateway): enforce OpenAI tool_choice required/function contracts; no longer open. |
| [#88547](https://github.com/openclaw/openclaw/pull/88547) | Closed in local gitcrawl 2026-06-01 | feat(github-copilot): add Claude Opus 4.8 to default model catalog; no longer open. |
| [#88525](https://github.com/openclaw/openclaw/pull/88525) | Closed in local gitcrawl 2026-06-01 | feat(deepseek): show provider balance in usage status; no longer open. |
| [#88517](https://github.com/openclaw/openclaw/issues/88517) | Closed in local gitcrawl 2026-06-01 | v2026.5.28 regression: claude-haiku-4-5 cron model override fails again; no longer open. |
| [#88516](https://github.com/openclaw/openclaw/pull/88516) | Closed in local gitcrawl 2026-06-01 | fix(doctor): preserve Codex routes in non-interactive repair; no longer open. |
| [#88512](https://github.com/openclaw/openclaw/pull/88512) | Closed in local gitcrawl 2026-06-02 | fix: resolve google provider default API to google-generative-ai; no longer open. |
| [#88510](https://github.com/openclaw/openclaw/issues/88510) | Closed in local gitcrawl 2026-06-01 | Codex model catalog cold-start miss for gpt-5.3-codex after gateway restart; no longer open. |
| [#88499](https://github.com/openclaw/openclaw/issues/88499) | Closed in local gitcrawl 2026-06-02 | openai-responses provider: 404 on previous_response_id when store=false (default); no longer open. |
| [#88482](https://github.com/openclaw/openclaw/pull/88482) | Closed in local gitcrawl 2026-06-01 | docs: clarify auth profile provider field after openai-codex OAuth login; no longer open. |
| [#88480](https://github.com/openclaw/openclaw/issues/88480) | Closed in local gitcrawl 2026-06-01 | Google Gemini chat model routes to openai-responses transport (401), native @google/genai transport never selected; no longer open. |
| [#88470](https://github.com/openclaw/openclaw/issues/88470) | Closed in local gitcrawl 2026-06-01 | [Bug]: Title: OpenAI GPT-5.5 fails through Codex runtime after upgrade to OpenClaw 2026.5.28; no longer open. |
| [#88468](https://github.com/openclaw/openclaw/pull/88468) | Closed in local gitcrawl 2026-06-01 | fix(configure): migrate stale Codex defaults after OpenAI auth; no longer open. |
| [#88460](https://github.com/openclaw/openclaw/pull/88460) | Closed in local gitcrawl 2026-06-15 | fix(cron): recover from local-llamacpp parameter serialization bugs; no longer open. |
| [#88439](https://github.com/openclaw/openclaw/issues/88439) | Closed in local gitcrawl 2026-06-03 | [Bug]: cron tool: local llamacpp model parameter serialization corrupts JSON property names (key concatenation); no longer open. |
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
| [#88145](https://github.com/openclaw/openclaw/pull/88145) | Closed in local gitcrawl 2026-05-31 | feat: add Hermes provider parity for hosted models; no longer open. |
| [#88135](https://github.com/openclaw/openclaw/pull/88135) | Closed in local gitcrawl 2026-05-31 | fix(codex): refresh stale managed runtime plugin; no longer open. |
| [#88130](https://github.com/openclaw/openclaw/pull/88130) | Closed in local gitcrawl 2026-05-31 | fix(agents): preserve Codex auth for compaction fallback; no longer open. |
| [#88125](https://github.com/openclaw/openclaw/issues/88125) | Closed in local gitcrawl 2026-06-01 | [Docs] Clarify auth profile provider field after openai-codex OAuth login; no longer open. |
| [#88120](https://github.com/openclaw/openclaw/issues/88120) | Closed live 2026-05-30 | [Bug]: 2026.5.27 upgrade leaves stale Codex plugin providerIds, breaking openai/gpt-5.5 route and status usage workaround; no longer open. |
| [#88110](https://github.com/openclaw/openclaw/pull/88110) | Closed in local gitcrawl 2026-05-31 | fix(session): normalize codex oauth session routes; no longer open. |
| [#88108](https://github.com/openclaw/openclaw/pull/88108) | Closed in local gitcrawl 2026-06-11 | fix(agents): compact lean local tool catalogs; no longer open. |
| [#88102](https://github.com/openclaw/openclaw/issues/88102) | Closed in local gitcrawl 2026-05-31 | [Bug]: 2026.5.27 Codex runtime rejects openai/gpt-5.5; codex/gpt-5.5 workaround drops Telegram /status usage; no longer open. |
| [#88091](https://github.com/openclaw/openclaw/issues/88091) | Closed in local gitcrawl 2026-05-31 | Guard MiniMax OAuth fetches in bundled plugin runtime; no longer open. |
| [#88086](https://github.com/openclaw/openclaw/pull/88086) | Closed in local gitcrawl 2026-05-31 | fix(minimax): guard oauth fetches; no longer open. |
| [#88072](https://github.com/openclaw/openclaw/pull/88072) | Closed in local gitcrawl 2026-05-31 | fix(agents): classify expired thinking signatures; no longer open. |
| [#88071](https://github.com/openclaw/openclaw/pull/88071) | Closed in local gitcrawl 2026-06-01 | fix(config): add dropReasoningFromHistory config for openai-completions providers (#88068); no longer open. |
| [#88068](https://github.com/openclaw/openclaw/issues/88068) | Closed in local gitcrawl 2026-06-01 | [Bug]: No config key to override dropReasoningFromHistory for openai-completions providers; no longer open. |
| [#88067](https://github.com/openclaw/openclaw/pull/88067) | Closed in local gitcrawl 2026-05-31 | fix(responses): drop orphaned assistant msg_* id when reasoning is dropped (#88019); no longer open. |
| [#88065](https://github.com/openclaw/openclaw/issues/88065) | Closed in local gitcrawl 2026-05-31 | Gateway crash on exit: SIGABRT in ggml_metal_rsets_free (node-llama-cpp Metal backend); no longer open. |
| [#88049](https://github.com/openclaw/openclaw/pull/88049) | Closed in local gitcrawl 2026-06-03 | fix(status): exclude session-selected model from fallback display list; no longer open. |
| [#88039](https://github.com/openclaw/openclaw/issues/88039) | Closed in local gitcrawl 2026-06-03 | [Bug]: Session-selected model incorrectly included in fallback list in v2026.5.26; no longer open. |
| [#88019](https://github.com/openclaw/openclaw/issues/88019) | Closed in local gitcrawl 2026-05-31 | [Bug]: Azure Responses session replay keeps msg id without required reasoning after fallback; no longer open. |
| [#88009](https://github.com/openclaw/openclaw/issues/88009) | Closed in local gitcrawl 2026-06-11 | [Feature]: batched memory embedding should batch over files; no longer open. |
| [#87963](https://github.com/openclaw/openclaw/pull/87963) | Closed in local gitcrawl 2026-05-31 | fix(agents): downgrade thinking blocks with empty signatures to text before anthropic-messages replay; no longer open. |
| [#87943](https://github.com/openclaw/openclaw/issues/87943) | Closed in local gitcrawl 2026-06-15 | feat: Add Xiaomi MiMo Web Search provider; no longer open. |
| [#87940](https://github.com/openclaw/openclaw/pull/87940) | Closed in local gitcrawl 2026-06-04 | fix(gateway): keep dense stream updates incremental; no longer open. |
| [#87935](https://github.com/openclaw/openclaw/issues/87935) | Closed in local gitcrawl 2026-05-31 | feat: Add Xiaomi MiMo Web Search provider; no longer open. |
| [#87933](https://github.com/openclaw/openclaw/pull/87933) | Closed in local gitcrawl 2026-06-11 | fix(agents): respect compat.thinkingFormat override for DeepSeek V4 models; no longer open. |
| [#87920](https://github.com/openclaw/openclaw/pull/87920) | Closed in local gitcrawl 2026-05-31 | feat(gateway): forward OpenAI stop sequences through chat completions; no longer open. |
| [#87907](https://github.com/openclaw/openclaw/pull/87907) | Closed in local gitcrawl 2026-06-03 | fix(memory): validate memory index identity; no longer open. |
| [#87893](https://github.com/openclaw/openclaw/pull/87893) | Closed in local gitcrawl 2026-06-15 | fix(auth-profiles): repair stale auto runtime auth selection; no longer open. |
| [#87881](https://github.com/openclaw/openclaw/issues/87881) | Closed in local gitcrawl 2026-06-11 | Gap Analysis: v2026.5.27 config keys rejected as unknown by schema; no longer open. |
| [#87877](https://github.com/openclaw/openclaw/issues/87877) | Closed in local gitcrawl 2026-05-31 | Codex runtime persists openai-codex as session modelProvider, causing recurring legacy route doctor warning; no longer open. |
| [#87874](https://github.com/openclaw/openclaw/pull/87874) | Closed in local gitcrawl 2026-06-02 | fix(macos): inherit thinking for voice wake forwarding; no longer open. |
| [#87862](https://github.com/openclaw/openclaw/pull/87862) | Closed in local gitcrawl 2026-05-31 | Add Claude Opus 4.8 defaults; no longer open. |
| [#87856](https://github.com/openclaw/openclaw/pull/87856) | Closed in local gitcrawl 2026-06-11 | fix(agents): count streamed model deltas incrementally; no longer open. |
| [#87854](https://github.com/openclaw/openclaw/issues/87854) | Closed in local gitcrawl 2026-06-02 | Memory Dreaming Promotion: candidates found but applied=0 (rehydratePromotionCandidate returns null for all); no longer open. |
| [#87851](https://github.com/openclaw/openclaw/pull/87851) | Closed in local gitcrawl 2026-05-31 | fix(agents): preserve logical OpenAI session routes; no longer open. |
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
| [#87746](https://github.com/openclaw/openclaw/issues/87746) | Closed in local gitcrawl 2026-06-03 | Add Claude Opus 4.8 (`claude-opus-4-8`) to the model catalog; no longer open. |
| [#87740](https://github.com/openclaw/openclaw/issues/87740) | Closed in local gitcrawl 2026-06-03 | Bug: Explicit thinkingLevel session override permanently reset to 'off' after each agent turn; no longer open. |
| [#87737](https://github.com/openclaw/openclaw/issues/87737) | Closed in local gitcrawl 2026-06-02 | DeepSeek V4 thinking wrapper ignores thinkingFormat compat override, breaks Azure Foundry deployments; no longer open. |
| [#87719](https://github.com/openclaw/openclaw/pull/87719) | Closed in local gitcrawl 2026-05-29 | fix(anthropic): stop migrating current claude-haiku-4-5 to sonnet; no longer open. |
| [#87705](https://github.com/openclaw/openclaw/pull/87705) | Closed in local gitcrawl 2026-06-06 | fix(agents): make subagent-control timeout configurable; no longer open. |
| [#87675](https://github.com/openclaw/openclaw/pull/87675) | Closed in local gitcrawl 2026-05-29 | fix(ollama): promote plain text tool calls; no longer open. |
| [#87641](https://github.com/openclaw/openclaw/issues/87641) | Closed in local gitcrawl 2026-05-31 | `opencode-go/kimi-k2.6`: every multi-turn task rejected with opaque 400 "Provider returned error" (reason=format), rotates to fallback (2026.5.26+5.27); no longer open. |
| [#87638](https://github.com/openclaw/openclaw/pull/87638) | Closed in local gitcrawl 2026-05-29 | test(agents): add small model live profile; no longer open. |
| [#87628](https://github.com/openclaw/openclaw/pull/87628) | Closed in local gitcrawl 2026-06-03 | feat(agents): inherit requester model for subagents; no longer open. |
| [#87621](https://github.com/openclaw/openclaw/pull/87621) | Closed in local gitcrawl 2026-05-29 | fix(ollama): yield during dense ndjson bursts; no longer open. |
| [#87619](https://github.com/openclaw/openclaw/pull/87619) | Closed in local gitcrawl 2026-06-11 | fix(diagnostics): account stream deltas incrementally; no longer open. |
| [#87616](https://github.com/openclaw/openclaw/issues/87616) | Closed in local gitcrawl 2026-06-02 | [Bug]: GatewayClientRequestError: FailoverError: LLM request timed out.; no longer open. |
| [#87608](https://github.com/openclaw/openclaw/issues/87608) | Closed in local gitcrawl 2026-05-31 | [Bug] Ollama Cloud rate-limit cooldown permanently blocks agents — not released after API recovery; no longer open. |
| [#87606](https://github.com/openclaw/openclaw/pull/87606) | Closed in local gitcrawl 2026-05-29 | fix(active-memory): raise recall timeout ceiling; no longer open. |
| [#87603](https://github.com/openclaw/openclaw/issues/87603) | Closed in local gitcrawl 2026-06-06 | lossless-claw contextThreshold does not adapt to actual model context window after fallback; no longer open. |
| [#87596](https://github.com/openclaw/openclaw/pull/87596) | Closed in local gitcrawl 2026-06-15 | fix(moonshot): rewrite duplicate native Kimi tool_call ids on replay; no longer open. |
| [#87594](https://github.com/openclaw/openclaw/pull/87594) | Closed in local gitcrawl 2026-05-29 | fix(openrouter): apply strict9 tool_call_id sanitisation for Mistral routes; no longer open. |
| [#87593](https://github.com/openclaw/openclaw/pull/87593) | Closed in local gitcrawl 2026-05-29 | fix(agents): preserve reasoning_content replay across DeepSeek tier suffixes; no longer open. |
| [#87575](https://github.com/openclaw/openclaw/issues/87575) | Closed in local gitcrawl 2026-05-29 | Bug: DeepSeek V4 Flash Free via OpenCode Zen provider fails with 400 on follow-up API calls; no longer open. |
| [#87562](https://github.com/openclaw/openclaw/pull/87562) | Closed in local gitcrawl 2026-06-12 | fix(openrouter): reconcile streamed cost with /generation total_cost; no longer open. |
| [#87558](https://github.com/openclaw/openclaw/pull/87558) | Closed in local gitcrawl 2026-06-02 | fix(gateway): keep dense stream updates incremental; no longer open. |
| [#87538](https://github.com/openclaw/openclaw/pull/87538) | Closed in local gitcrawl 2026-06-01 | fix(agents): model-scope cooldown for transport timeout (#87462); no longer open. |
| [#87484](https://github.com/openclaw/openclaw/pull/87484) | Closed in local gitcrawl 2026-06-02 | fix(agents): clear legacy auto fallback pins; no longer open. |
| [#87467](https://github.com/openclaw/openclaw/issues/87467) | Closed in local gitcrawl 2026-06-02 | [Bug]: Auto rate-limit fallback override still pins Discord session to fallback after primary recovers; no longer open. |
| [#87463](https://github.com/openclaw/openclaw/pull/87463) | Closed in local gitcrawl 2026-05-31 | fix(session): normalize openai-codex provider to openai for session route persistence; no longer open. |
| [#87462](https://github.com/openclaw/openclaw/issues/87462) | Closed in local gitcrawl 2026-06-01 | [Bug]: Auth profile cooldown triggers chain exhaustion without actual Google API errors in v2026.5.26; no longer open. |
| [#87456](https://github.com/openclaw/openclaw/pull/87456) | Closed in local gitcrawl 2026-05-29 | Restore Codex Spark OAuth routes; no longer open. |
| [#87436](https://github.com/openclaw/openclaw/issues/87436) | Closed in local gitcrawl 2026-05-31 | Codex harness runs recreate legacy openai-codex session route state after doctor --fix; no longer open. |
| [#87416](https://github.com/openclaw/openclaw/pull/87416) | Closed in local gitcrawl 2026-05-29 | fix(agents): resolve Codex runtime models first; no longer open. |
| [#87381](https://github.com/openclaw/openclaw/issues/87381) | Closed in local gitcrawl 2026-06-03 | ACP runtime ignores per-agent model.primary override; no longer open. |
| [#87274](https://github.com/openclaw/openclaw/pull/87274) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor OpenAI-compatible cache retention; no longer open. |
| [#87252](https://github.com/openclaw/openclaw/pull/87252) | Closed in local gitcrawl 2026-05-28 | fix(agents): use runtime alias equivalence in live model switch comparison; no longer open. |
| [#87225](https://github.com/openclaw/openclaw/pull/87225) | Closed in local gitcrawl 2026-05-28 | fix(memory): salvage qmd search JSON after nonzero exit; no longer open. |
| [#86880](https://github.com/openclaw/openclaw/issues/86880) | Closed in local gitcrawl 2026-06-01 | [Bug]: Context Overflow Bug With OpenRouter Models (Latest Version 2026.05.22); no longer open. |
| [#86765](https://github.com/openclaw/openclaw/pull/86765) | Closed in local gitcrawl 2026-05-28 | [codex] Fix memory close sync race; no longer open. |
| [#86748](https://github.com/openclaw/openclaw/pull/86748) | Closed in local gitcrawl 2026-05-28 | perf(plugins): resolve provider policy from current snapshot first; no longer open. |
| [#86702](https://github.com/openclaw/openclaw/issues/86702) | Closed in local gitcrawl 2026-05-28 | MemoryIndexManager.close() races with in-flight sync — provider/DB closed before sync settles; no longer open. |
| [#86690](https://github.com/openclaw/openclaw/pull/86690) | Closed in local gitcrawl 2026-05-28 | fix(plugin-sdk): preserve string-const unions as flat enum for deepseek tool schemas; no longer open. |
| [#86689](https://github.com/openclaw/openclaw/pull/86689) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor per-agent thinking defaults for ingress runs; no longer open. |
| [#86669](https://github.com/openclaw/openclaw/issues/86669) | Closed in local gitcrawl 2026-05-28 | [Bug]: openclaw openai-compat /v1/chat/completions strips chat_template_kwargs entirely on vLLM/Nemotron — causes reasoning-only death-spiral; no longer open. |
| [#86644](https://github.com/openclaw/openclaw/pull/86644) | Closed in local gitcrawl 2026-05-28 | fix(models): skip wildcard catalog aliases; no longer open. |
| [#86633](https://github.com/openclaw/openclaw/pull/86633) | Closed in local gitcrawl 2026-05-31 | fix(ollama): yield during dense stream processing; no longer open. |
| [#86613](https://github.com/openclaw/openclaw/issues/86613) | Closed in local gitcrawl 2026-05-28 | [Bug]: Every memory_search call leaks ~N FDs (one per .md file in workspace memory tree) on macOS; long-lived gateways degrade toward FD exhaustion; no longer open. |
| [#86599](https://github.com/openclaw/openclaw/issues/86599) | Closed in local gitcrawl 2026-06-11 | [Bug]: Local model provider calls thread block gateway event loop on Windows beta; trivial infer run takes ~4 minutes; no longer open. |
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
| [#86048](https://github.com/openclaw/openclaw/issues/86048) | Closed in local gitcrawl 2026-06-03 | WSL2 GPU-PV driver lockup: nvidia-smi hangs after llama-server D-state crash; no longer open. |
| [#86044](https://github.com/openclaw/openclaw/issues/86044) | Closed in local gitcrawl 2026-06-03 | 2026.5.22: CLI hangs on Windows — provider auth-state pre-warm blocks all CLI commands; no longer open. |
| [#86032](https://github.com/openclaw/openclaw/pull/86032) | Closed in local gitcrawl 2026-05-31 | fix(agents): recover DeepSeek DSML tool markup into synthetic tool calls; no longer open. |
| [#86003](https://github.com/openclaw/openclaw/pull/86003) | Closed in local gitcrawl 2026-05-28 | fix(gateway): add provider auth prewarm operator controls; no longer open. |
| [#85931](https://github.com/openclaw/openclaw/pull/85931) | Closed in local gitcrawl 2026-06-01 | fix(memory): serialize qmd update writes across processes to stop SQLITE_BUSY; no longer open. |
| [#85918](https://github.com/openclaw/openclaw/issues/85918) | Closed in local gitcrawl 2026-06-03 | Bug: Foundry DeepSeek V4 tool turns surface DSML text instead of executable tool calls; no longer open. |
| [#85883](https://github.com/openclaw/openclaw/issues/85883) | Closed in local gitcrawl 2026-05-31 | openai-completions provider leaks channel-output JSON to channel (works correctly on ollama provider); no longer open. |
| [#85715](https://github.com/openclaw/openclaw/pull/85715) | Closed in local gitcrawl 2026-05-31 | feat(deepseek): parse leaked DSML tags into synthetic tool calls instead of dropping them; no longer open. |
| [#85321](https://github.com/openclaw/openclaw/issues/85321) | Closed in local gitcrawl 2026-06-15 | `wrapStreamRepairMalformedToolCallArguments` clears valid tool call arguments for Moonshot/Kimi provider; no longer open. |
| [#85269](https://github.com/openclaw/openclaw/pull/85269) | Closed in local gitcrawl 2026-05-28 | feat(openai): add generic OpenAI-compatible embeddings; no longer open. |
| [#85267](https://github.com/openclaw/openclaw/issues/85267) | Closed 2026-05-25 | Assigned to osolmaz before close. |
| [#85217](https://github.com/openclaw/openclaw/issues/85217) | Closed in local gitcrawl 2026-05-28 | [Bug]: QMD query mode unusable on macOS Apple Silicon — Metal GPU cleanup crash discards valid search results; no longer open. |
| [#85161](https://github.com/openclaw/openclaw/issues/85161) | Closed in local gitcrawl 2026-05-31 | [Bug]: valid tool call XML in LLM reasoning block is sometimes executed by gateway; no longer open. |
| [#85072](https://github.com/openclaw/openclaw/pull/85072) | Closed in local gitcrawl 2026-05-28 | Deprecate memory-specific embedding provider registration; no longer open. |
| [#84998](https://github.com/openclaw/openclaw/pull/84998) | Closed in local gitcrawl 2026-05-28 | feat(plugins): add OpenAI-compatible embedding provider; no longer open. |
| [#84991](https://github.com/openclaw/openclaw/pull/84991) | Closed in local gitcrawl 2026-05-28 | feat(memory-core): consume generic embedding providers; no longer open. |
| [#84697](https://github.com/openclaw/openclaw/issues/84697) | Closed in local gitcrawl 2026-06-03 | Custom OpenAI-compatible provider with baseUrl without /v1 fails with cryptic 'incomplete terminal response' error; no longer open. |
| [#84621](https://github.com/openclaw/openclaw/pull/84621) | Closed in local gitcrawl 2026-05-29 | Fix Kimi tool-call rewriting stop reason handling; no longer open. |
| [#84384](https://github.com/openclaw/openclaw/issues/84384) | Closed in local gitcrawl 2026-06-03 | [Bug]: Gemini 2.5 Flash via vertex-ai (OpenAI-compatible) streaming times out — thinking tokens not handled; no longer open. |
| [#84228](https://github.com/openclaw/openclaw/pull/84228) | Closed in local gitcrawl 2026-06-15 | fix(nvidia): update Nemotron 3 Super contextWindow to 1M per NVIDIA spec; no longer open. |
| [#83709](https://github.com/openclaw/openclaw/issues/83709) | Closed in local gitcrawl 2026-06-03 | [Feature]: Add `supportsPromptCacheKey` to Mistral transport compat patch; no longer open. |
| [#83461](https://github.com/openclaw/openclaw/issues/83461) | Not resolvable as live issue | Earlier notes referenced it, but live GitHub issue view did not resolve it as an open issue. |
| [#83333](https://github.com/openclaw/openclaw/issues/83333) | Closed in local gitcrawl 2026-06-03 | [Bug]: Memory provider cutover to Ollama leaves production index in mixed OpenAI/Ollama vector state after live sync/reload; no longer open. |
| [#83107](https://github.com/openclaw/openclaw/issues/83107) | Closed in local gitcrawl 2026-05-31 | Model registry name matching is load-bearing — silent fallback to picker selection on registry miss (2026.5.12); no longer open. |
| [#82973](https://github.com/openclaw/openclaw/pull/82973) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor explicit cacheRetention for openai-completions providers; no longer open. |
| [#82887](https://github.com/openclaw/openclaw/pull/82887) | Closed in local gitcrawl 2026-05-31 | fix(cron): preflight model fallbacks before skip; no longer open. |
| [#82594](https://github.com/openclaw/openclaw/issues/82594) | Closed in local gitcrawl 2026-06-06 | [Bug]: openclaw onboard extremely slow on Windows during model loading; no longer open. |
| [#82557](https://github.com/openclaw/openclaw/pull/82557) | Closed in local gitcrawl 2026-06-11 | Allow onboarding to configure multiple model providers; no longer open. |
| [#81530](https://github.com/openclaw/openclaw/issues/81530) | Closed in local gitcrawl 2026-06-03 | [Bug]: [5.12-beta.8] Telegram Supergroup Forum Topics — Inbound Messages Not Processed; no longer open. |
| [#81281](https://github.com/openclaw/openclaw/issues/81281) | Closed in local gitcrawl 2026-05-28 | [Bug]: OpenAI-completions prompt_cache_key regression — caching worked in 2026.3.x, broken in 2026.5.x; no longer open. |
| [#81249](https://github.com/openclaw/openclaw/issues/81249) | Closed 2026-05-24 | No longer counted as live-open. |
| [#81214](https://github.com/openclaw/openclaw/issues/81214) | Closed in local gitcrawl 2026-06-01 | [Bug]: OpenClaw 2026.5.7 subagent regression; no longer open. |
| [#81170](https://github.com/openclaw/openclaw/pull/81170) | Closed in local gitcrawl 2026-06-01 | fix(openai): preserve custom provider id through memory embedding adapter; no longer open. |
| [#80495](https://github.com/openclaw/openclaw/issues/80495) | Closed in local gitcrawl 2026-05-31 | [Bug]: LM Studio Provider Fails: Environment Variable Expansion + API Endpoint Mismatch; no longer open. |
| [#80476](https://github.com/openclaw/openclaw/issues/80476) | Closed in local gitcrawl 2026-05-28 | [Feature]: bundled openai-compatible embedding provider for self-hosted servers (llama.cpp, Ollama, vLLM, TGI, LocalAI); no longer open. |
| [#80379](https://github.com/openclaw/openclaw/issues/80379) | Closed in local gitcrawl 2026-05-28 | [Bug]: Tool result secret redaction mutates session history, breaking KV cache prefix matching for local LLM providers; no longer open. |
| [#80226](https://github.com/openclaw/openclaw/issues/80226) | Closed 2026-05-25 | No longer counted as live-open. |
| [#79745](https://github.com/openclaw/openclaw/pull/79745) | Closed in local gitcrawl 2026-06-12 | Memory/QMD: isolate mcporter sidecars per agent; no longer open. |
| [#79380](https://github.com/openclaw/openclaw/issues/79380) | Closed in local gitcrawl 2026-06-01 | [Bug]: Gateway CPU spin / crash loop on Raspberry Pi 4 (ARM64) — regression from 4.23 to 4.25+; no longer open. |
| [#79329](https://github.com/openclaw/openclaw/issues/79329) | Closed in local gitcrawl 2026-05-31 | Cron model preflight skips entire run when local primary is unreachable, ignoring configured cloud fallbacks [AI]; no longer open. |
| [#77792](https://github.com/openclaw/openclaw/issues/77792) | Closed in local gitcrawl 2026-06-01 | fix(tts/xiaomi): support per-call voice and model overrides; no longer open. |
| [#77678](https://github.com/openclaw/openclaw/pull/77678) | Closed in local gitcrawl 2026-05-28 | fix(memory): don't report QMD embeddings as unavailable when searchMode=search; no longer open. |
| [#77655](https://github.com/openclaw/openclaw/issues/77655) | Closed in local gitcrawl 2026-05-31 | Model fallback chain interrupted by race condition — 6 fallback models configured but task terminates before all are tried; no longer open. |
| [#77336](https://github.com/openclaw/openclaw/issues/77336) | Closed in local gitcrawl 2026-06-02 | [Feature Request]: Built-in handling of strict role alternation for Mistral / SGLang backends; no longer open. |
| [#76741](https://github.com/openclaw/openclaw/pull/76741) | Closed in local gitcrawl 2026-06-03 | fix(kimi): strip anthropic cache markers; no longer open. |
| [#76654](https://github.com/openclaw/openclaw/issues/76654) | Closed in local gitcrawl 2026-05-31 | [webchat] Agent responses disappear after heartbeat tool calls (model-specific, MiMo V2 Pro); no longer open. |
| [#76612](https://github.com/openclaw/openclaw/issues/76612) | Closed in local gitcrawl 2026-06-03 | Kimi Code returns empty content when Anthropic cache_control markers are sent; no longer open. |
| [#76002](https://github.com/openclaw/openclaw/pull/76002) | Closed in local gitcrawl 2026-06-15 | fix(kimi): switch to openai-completions endpoint for image support; no longer open. |
| [#75720](https://github.com/openclaw/openclaw/issues/75720) | Closed in local gitcrawl 2026-05-28 | [Bug]: Auto-onboard / plugin presets unconditionally overwrite user-set agents.defaults.model.primary; no longer open. |
| [#75657](https://github.com/openclaw/openclaw/issues/75657) | Closed in local gitcrawl 2026-05-29 | fix: local GGUF embedding model warmup blocks Node.js event loop for minutes on startup; no longer open. |
| [#75378](https://github.com/openclaw/openclaw/issues/75378) | Closed in local gitcrawl 2026-06-15 | [Bug] Gateway event loop saturation during parallel subagent spawn causes 1012 restart (v2026.4.29); no longer open. |
| [#74644](https://github.com/openclaw/openclaw/issues/74644) | Closed in local gitcrawl 2026-05-31 | mediaUnderstandingProviders audio path hard-requires API key, breaking no-auth/local STT providers; no longer open. |
| [#74315](https://github.com/openclaw/openclaw/pull/74315) | Closed in local gitcrawl 2026-05-31 | fix(agents): remove kimi-coding from normalizeProviderId alias chain; no longer open. |
| [#74310](https://github.com/openclaw/openclaw/issues/74310) | Closed in local gitcrawl 2026-06-03 | Bug Report: `normalizeProviderId` breaks provider-namespaced models like `kimi-coding/k2p5`; no longer open. |
| [#73667](https://github.com/openclaw/openclaw/pull/73667) | Closed in local gitcrawl 2026-06-11 | Bound active-memory recall latency and jitter QMD startup; no longer open. |
| [#72927](https://github.com/openclaw/openclaw/issues/72927) | Closed in local gitcrawl 2026-06-01 | feat(tts): support MiMo v2.5 TTS VoiceDesign; no longer open. |
| [#71784](https://github.com/openclaw/openclaw/issues/71784) | Closed in local gitcrawl 2026-06-01 | Bug: memory search live embedding fails ~20–40% with `fetch failed \| other side closed` (provider-agnostic; upstream healthy); no longer open. |
| [#71491](https://github.com/openclaw/openclaw/issues/71491) | Closed in local gitcrawl 2026-06-15 | Kimi K2.6 reasoning_content 400 regression in long conversations after LCM compaction (follow-up #70392); no longer open. |
| [#70739](https://github.com/openclaw/openclaw/pull/70739) | Closed in local gitcrawl 2026-06-15 | fix(gateway): add SSE heartbeat to keep /v1/responses and /v1/chat/completions streams alive through idle-timeout proxies; no longer open. |
| [#70647](https://github.com/openclaw/openclaw/pull/70647) | Closed in local gitcrawl 2026-06-11 | test(agents): pin empty-turn coverage for non-strict-agentic nemotron; no longer open. |
| [#70559](https://github.com/openclaw/openclaw/issues/70559) | Closed in local gitcrawl 2026-06-11 | runUnsafeReindex crashes with "no such table: chunks_vec" when sqlite-vec is enabled; no longer open. |
| [#68975](https://github.com/openclaw/openclaw/pull/68975) | Closed in local gitcrawl 2026-06-15 | feat(memory): switch default local embedding model to bge-m3 Q8_0 🤖 AI-assisted; no longer open. |
| [#68812](https://github.com/openclaw/openclaw/issues/68812) | Closed in local gitcrawl 2026-06-01 | Make memory embedding retry/concurrency parameters configurable; no longer open. |
| [#68435](https://github.com/openclaw/openclaw/pull/68435) | Closed in local gitcrawl 2026-06-15 | feat(gateway): accept audio/file content blocks in /v1/chat/completions; no longer open. |
| [#68222](https://github.com/openclaw/openclaw/issues/68222) | Closed in local gitcrawl 2026-06-15 | [Bug]: Kimi Code model frequent sessions_yield tool call/output interrupts long-running tasks, requires manual intervention to resume; no longer open. |
| [#67593](https://github.com/openclaw/openclaw/issues/67593) | Closed in local gitcrawl 2026-06-15 | feat: add Kimi/Moonshot provider usage and balance display; no longer open. |
| [#67423](https://github.com/openclaw/openclaw/issues/67423) | Closed in local gitcrawl 2026-06-01 | [Bug] Auth router ignores provider entry's apiKey field, resolves via auth.order by canonical provider ID — wrong key for split provider entries; no longer open. |
| [#67379](https://github.com/openclaw/openclaw/issues/67379) | Closed in local gitcrawl 2026-06-15 | qmd scope denies subagent sessions — channel/chatType resolve to undefined; no longer open. |
| [#67035](https://github.com/openclaw/openclaw/issues/67035) | Closed in local gitcrawl 2026-06-04 | [Bug]: 2026.4.14 Windows chat UI regression: input text swallowed, streamed replies often invisible until refresh, typing indicator flashes then blanks; no longer open. |
| [#66339](https://github.com/openclaw/openclaw/issues/66339) | Closed in local gitcrawl 2026-06-01 | memory search can hit QMD SQLite lock contention during normal runtime; no longer open. |
| [#65914](https://github.com/openclaw/openclaw/pull/65914) | Closed in local gitcrawl 2026-06-01 | fix(memory): respect qmd status timeout and skip checkpoint exports; no longer open. |
| [#65557](https://github.com/openclaw/openclaw/issues/65557) | Closed in local gitcrawl 2026-06-07 | Provider & model selection per session/account with admin-controlled allowlists; no longer open. |
| [#65547](https://github.com/openclaw/openclaw/pull/65547) | Closed in local gitcrawl 2026-06-15 | test(memory-qmd): verify extraCollections pattern reaches qmd collection add CLI args; no longer open. |
| [#65502](https://github.com/openclaw/openclaw/issues/65502) | Closed in local gitcrawl 2026-05-31 | feat(agents): resilient model fallback with retry + context-aware safe mode; no longer open. |
| [#64224](https://github.com/openclaw/openclaw/issues/64224) | Closed in local gitcrawl 2026-06-15 | Billing cooldown flags entire provider instead of individual model — breaks proxy/litellm setups; no longer open. |
| [#64212](https://github.com/openclaw/openclaw/issues/64212) | Closed in local gitcrawl 2026-06-15 | [Bug]: Image tool fails with "Request was aborted" for NVIDIA Kimi K2.5; no longer open. |
| [#63685](https://github.com/openclaw/openclaw/issues/63685) | Closed in local gitcrawl 2026-06-03 | [Bug]: Cannot run gemma 4 models from google ai studio; no longer open. |
| [#62924](https://github.com/openclaw/openclaw/issues/62924) | Closed in local gitcrawl 2026-06-15 | Expose actual media-understanding chosen model in inbound body to avoid guessed media model reporting; no longer open. |
| [#62780](https://github.com/openclaw/openclaw/issues/62780) | Closed in local gitcrawl 2026-06-15 | Feature: message:before_send hook to enable content-quality fallback gating; no longer open. |
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
| [#58405](https://github.com/openclaw/openclaw/pull/58405) | Closed in local gitcrawl 2026-06-12 | feat(openresponses): add per-request skills override to /v1/responses; no longer open. |
| [#58012](https://github.com/openclaw/openclaw/issues/58012) | Closed in local gitcrawl 2026-05-29 | strict9 tool-call-id regression for Mistral via proxy providers; no longer open. |
| [#57638](https://github.com/openclaw/openclaw/issues/57638) | Closed in local gitcrawl 2026-06-15 | feat: cron.defaults for model, delivery, and contextTokens; no longer open. |
| [#51593](https://github.com/openclaw/openclaw/issues/51593) | Closed in local gitcrawl 2026-06-15 | [Bug]: Moonshot/Kimi duplicate tool-call IDs in replay, exposed by WhatsApp group chats; no longer open. |
| [#48680](https://github.com/openclaw/openclaw/issues/48680) | Closed in local gitcrawl 2026-05-31 | [Bug] Model fallback treats HTTP 403 business rejection as 'candidate_succeeded', skipping remaining fallback models; no longer open. |
| [#48300](https://github.com/openclaw/openclaw/issues/48300) | Closed in local gitcrawl 2026-06-11 | Bug: memory_search hybrid mode not returning FTS matches; no longer open. |
| [#47884](https://github.com/openclaw/openclaw/issues/47884) | Closed in local gitcrawl 2026-06-01 | [Bug]: memory_search tool fails with "fetch failed" despite embedding provider configured; no longer open. |
| [#44870](https://github.com/openclaw/openclaw/issues/44870) | Closed in local gitcrawl 2026-06-03 | [Bug]: I have been unable to verify using the codex from the transfer station; no longer open. |
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
- Kept open threads: 1221 (455 issues, 766 PRs).
