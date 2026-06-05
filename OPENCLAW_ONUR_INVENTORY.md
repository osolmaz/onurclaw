# OPENCLAW ONUR INVENTORY

Updated: 2026-06-06

Review watermark:

- Last reviewed through issue: #90711.
- Last reviewed through PR: #90712.
- Meaning: all GitHub issues and PRs at or below these numbers were considered for local-model and open-weight relevance; later numbers need review on the next run.

## OPEN THREADS (632)

| Thread | Activity | Area | Creator | Title |
| --- | --- | --- | --- | --- |
| 📝&nbsp;[#72015](https://github.com/openclaw/openclaw/issues/72015) | 29 | Local memory/embedding | @0xCNAI | Reliability: active-memory blocks replies and QMD boot initialization can overload multi-agent gateways |
| 📝&nbsp;[#71491](https://github.com/openclaw/openclaw/issues/71491) | 25 | Open-weight/provider behavior | @RoseKongPS | Kimi K2.6 reasoning_content 400 regression in long conversations after LCM compaction (follow-up #70392) |
| 📝&nbsp;[#86599](https://github.com/openclaw/openclaw/issues/86599) | 23 | Local memory/embedding | @JakeBiggs | [Bug]: Local model provider calls thread block gateway event loop on Windows beta; trivial infer run takes ~4 minutes |
| 📝&nbsp;[#75378](https://github.com/openclaw/openclaw/issues/75378) | 22 | Local model runtime | @kai-the-man[bot] | [Bug] Gateway event loop saturation during parallel subagent spawn causes 1012 restart (v2026.4.29) |
| 📝&nbsp;[#17925](https://github.com/openclaw/openclaw/issues/17925) | 20 | Open-weight/provider behavior | @cedar202510-dotcom | [Feature]: Support native web_search passthrough for ZAI (GLM) and Google (Gemini) providers |
| 🔀&nbsp;[#84581](https://github.com/openclaw/openclaw/pull/84581) | 17 | OpenAI-compatible/proxy | @pcdqc | fix(agents): strip plaintext model provider keys |
| 📝&nbsp;[#74586](https://github.com/openclaw/openclaw/issues/74586) | 17 | Local memory/embedding | @islandpreneur007 | AM embedded run aborts memory_search tool calls; classifies as timeout despite model completion |
| 📝&nbsp;[#62328](https://github.com/openclaw/openclaw/issues/62328) | 17 | Local memory/embedding | @TimeAground | node:sqlite missing FTS5 module - memory search keyword fallback broken |
| 🔀&nbsp;[#56674](https://github.com/openclaw/openclaw/pull/56674) | 17 | OpenAI-compatible/proxy | @tonga54 | feat(openresponses): return reasoning/thinking content in /v1/responses output |
| 📝&nbsp;[#33962](https://github.com/openclaw/openclaw/issues/33962) | 15 | Local model runtime | @zhangsensen | [Feature]: slug-generator: use lightweight model instead of agent primary to prevent lane congestion |
| 🔀&nbsp;[#79745](https://github.com/openclaw/openclaw/pull/79745) | 14 | Local memory/embedding | @SYU8384 | Memory/QMD: isolate mcporter sidecars per agent |
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
| 📝&nbsp;[#33329](https://github.com/openclaw/openclaw/issues/33329) | 10 | Local model runtime | @bhalliburton | Document and add config toggles for all implicit discovery mechanisms |
| 🔀&nbsp;[#87404](https://github.com/openclaw/openclaw/pull/87404) | 9 | Model routing/config | @deepujain | fix(agents): honor ACP alias model.primary overrides (Fixes #87381) |
| 🔀&nbsp;[#86564](https://github.com/openclaw/openclaw/pull/86564) | 9 | Model/provider behavior | @wesleysimplicio | fix(gateway): disable provider auth prewarm by default |
| 📝&nbsp;[#86090](https://github.com/openclaw/openclaw/issues/86090) | 9 | Local model runtime | @dustytext-bot | runHeartbeatOnce returns {status: "ran"} in 78ms on idle agent — phantom run, no model turn executed |
| 📝&nbsp;[#85773](https://github.com/openclaw/openclaw/issues/85773) | 9 | Local model runtime | @philippulus | [Bug]: After reinstalling (v2026.5.20), agents only provide generic replies, completely ignoring workspace files content and skills |
| 🔀&nbsp;[#84977](https://github.com/openclaw/openclaw/pull/84977) | 9 | Local model runtime | @ouchuan | feat: handle gemma 4 format tool call |
| 📝&nbsp;[#73432](https://github.com/openclaw/openclaw/issues/73432) | 9 | Local memory/embedding | @danielngn | [Bug]: qmd embedding is never triggered per memory.qmd.update.interval/embedInterval |
| 🔀&nbsp;[#71062](https://github.com/openclaw/openclaw/pull/71062) | 9 | OpenAI-compatible/proxy | @PopFlamingo | fix(/v1/responses): drop the extra phantom assistant turn on client-tool calls |
| 🔀&nbsp;[#70739](https://github.com/openclaw/openclaw/pull/70739) | 9 | OpenAI-compatible/proxy | @tonga54 | fix(gateway): add SSE heartbeat to keep /v1/responses and /v1/chat/completions streams alive through idle-timeout proxies |
| 🔀&nbsp;[#70596](https://github.com/openclaw/openclaw/pull/70596) | 9 | Local memory/embedding | @taosiyuan163 | perf(memory): prewarm explicit local embeddings on gateway startup |
| 🔀&nbsp;[#68725](https://github.com/openclaw/openclaw/pull/68725) | 9 | OpenAI-compatible/proxy | @wirjo | feat(amazon-bedrock-mantle): add known context windows for open-weight Mantle models |
| 📝&nbsp;[#60546](https://github.com/openclaw/openclaw/issues/60546) | 9 | OpenAI-compatible/proxy | @jtgcyber | [Bug]: microsoft-foundry provider selects Claude deployments but routes them through OpenAI Foundry endpoints |
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
| 📝&nbsp;[#62121](https://github.com/openclaw/openclaw/issues/62121) | 8 | Local model runtime | @tlnini-afk | DeepSeek preamble text leaks to Telegram after 3.13 -> 4.5 upgrade (untagged assistant text bypasses commentary filter) |
| 📝&nbsp;[#52029](https://github.com/openclaw/openclaw/issues/52029) | 8 | Local model runtime | @andyk-ms | Feature Request: heartbeat.tools option to disable tools during heartbeat |
| 📝&nbsp;[#45508](https://github.com/openclaw/openclaw/issues/45508) | 8 | OpenAI-compatible/proxy | @mcfex | [Feature]: Self-hosted STT/TTS provider support in webchat (Route webchat TTS through the gateway instead of browser Speech API) |
| 📝&nbsp;[#41372](https://github.com/openclaw/openclaw/issues/41372) | 8 | Model/provider behavior | @e740554 | Field Report: 25 findings from 4 weeks of self-hosted production use (config crashes, CLI docs, Discord, cron) |
| 📝&nbsp;[#15073](https://github.com/openclaw/openclaw/issues/15073) | 8 | Local model runtime | @lucca-alma | Feature Request: Per-agent context/workspace on model fallback |
| 🔀&nbsp;[#77053](https://github.com/openclaw/openclaw/pull/77053) | 7 | OpenAI-compatible/proxy | @firat-elbey | feat(lmstudio): opt-in idle TTL via native load API |
| 🔀&nbsp;[#76928](https://github.com/openclaw/openclaw/pull/76928) | 7 | Model routing/config | @dorukardahan | feat(plugins): let hooks prefer auth profiles |
| 📝&nbsp;[#30381](https://github.com/openclaw/openclaw/issues/30381) | 7 | OpenAI-compatible/proxy | @mr-slurpy-wildcard | chatCompletions: ignore request model when x-openclaw-agent-id header is present |
| 📝&nbsp;[#75959](https://github.com/openclaw/openclaw/issues/75959) | 6 | OpenAI-compatible/proxy | @hpfan | [Feature]: Support image analysis for Kimi Code Plan |
| 🔀&nbsp;[#75075](https://github.com/openclaw/openclaw/pull/75075) | 6 | OpenAI-compatible/proxy | @glow1128 | feat(gateway): surface built-in tool calls as function_call output items on /v1/responses |
| 📝&nbsp;[#63990](https://github.com/openclaw/openclaw/issues/63990) | 6 | Local memory/embedding | @DIZ-admin | Feature: Multi-index embedding memory with model-aware failover (no mixed vector spaces) |
| 📝&nbsp;[#48300](https://github.com/openclaw/openclaw/issues/48300) | 6 | Local memory/embedding | @sabo961 | Bug: memory_search hybrid mode not returning FTS matches |
| 🔀&nbsp;[#87705](https://github.com/openclaw/openclaw/pull/87705) | 5 | Local model runtime | @EnjouZeratul | fix(agents): make subagent-control timeout configurable |
| 🔀&nbsp;[#87694](https://github.com/openclaw/openclaw/pull/87694) | 5 | Model routing/config | @sweetcornna | fix(auth): tighten billing cooldown defaults to recover from multi-hour lockouts (#70903) |
| 🔀&nbsp;[#87619](https://github.com/openclaw/openclaw/pull/87619) | 5 | Local model runtime | @vincentkoc | fix(diagnostics): account stream deltas incrementally |
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
| 🔀&nbsp;[#61187](https://github.com/openclaw/openclaw/pull/61187) | 5 | Open-weight/provider behavior | @Luckymingxuan | fix(kimi, moonshot): model picker shows wrong models |
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
| 🔀&nbsp;[#84228](https://github.com/openclaw/openclaw/pull/84228) | 4 | Open-weight/provider behavior | @nedirante | fix(nvidia): update Nemotron 3 Super contextWindow to 1M per NVIDIA spec |
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
| 🔀&nbsp;[#76002](https://github.com/openclaw/openclaw/pull/76002) | 4 | OpenAI-compatible/proxy | @symonbaikov | fix(kimi): switch to openai-completions endpoint for image support |
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
| 📝&nbsp;[#62924](https://github.com/openclaw/openclaw/issues/62924) | 4 | Local model runtime | @ulttla | Expose actual media-understanding chosen model in inbound body to avoid guessed media model reporting |
| 📝&nbsp;[#62599](https://github.com/openclaw/openclaw/issues/62599) | 4 | Local model runtime | @shawnpetros | [Bug]: openclaw status loads memory plugins locally and can report false vector state |
| 📝&nbsp;[#60344](https://github.com/openclaw/openclaw/issues/60344) | 4 | Open-weight/provider behavior | @doctorhexb163 | [Bug]: Recursive output of system marker [image data removed - already processed by model] in kimi-coding/k2p |
| 🔀&nbsp;[#58434](https://github.com/openclaw/openclaw/pull/58434) | 4 | OpenAI-compatible/proxy | @tonga54 | feat(openresponses): add per-request tool_deny override to /v1/responses |
| 📝&nbsp;[#57996](https://github.com/openclaw/openclaw/issues/57996) | 4 | Local memory/embedding | @Orionation | QMD per-agent SQLite caches cause extreme disk I/O on multi-agent deployments<br>Assignee: vincentkoc |
| 📝&nbsp;[#53550](https://github.com/openclaw/openclaw/issues/53550) | 4 | Local memory/embedding | @shivasymbl | experimental.sessionMemory does not surface gateway-dispatched sessions in memory_search |
| 📝&nbsp;[#49205](https://github.com/openclaw/openclaw/issues/49205) | 4 | OpenAI-compatible/proxy | @SHAREN | [Bug]: Control UI messages can reach shared context but still not appear in Open WebUI visible chat history |
| 📝&nbsp;[#46661](https://github.com/openclaw/openclaw/issues/46661) | 4 | OpenAI-compatible/proxy | @sheldon123z | [Feature]: Support Custom ASR (Speech-to-Text) Server Configuration |
| 📝&nbsp;[#22021](https://github.com/openclaw/openclaw/issues/22021) | 4 | Local model runtime | @dekaru | [Feature]: Add X-Actual-Model header to expose runtime model in HTTP responses |
| 📝&nbsp;[#13962](https://github.com/openclaw/openclaw/issues/13962) | 4 | Local model runtime | @dantaik | Feature: Per-mention model routing + context window for group mentions |
| 📝&nbsp;[#82594](https://github.com/openclaw/openclaw/issues/82594) | 2 | Local model runtime | @alexandre-leng | [Bug]: openclaw onboard extremely slow on Windows during model loading |
| 🔀&nbsp;[#74761](https://github.com/openclaw/openclaw/pull/74761) | 2 | Local memory/embedding | @mppyes-ai | docs: Document oMLX (Apple Silicon MLX) as memorySearch embedding provider |
| 🔀&nbsp;[#73817](https://github.com/openclaw/openclaw/pull/73817) | 2 | OpenAI-compatible/proxy | @spi3 | fix(media): allow private openai compatible audio transcription endpoints |
| 📝&nbsp;[#59168](https://github.com/openclaw/openclaw/issues/59168) | 2 | Local model runtime | @Kaspre | feat(models): use provider/name as internal key to decouple from API model ID |
| 🔀&nbsp;[#86637](https://github.com/openclaw/openclaw/pull/86637) | 1 | Open-weight/provider behavior | @SebTardif | fix(agents): recover tool calls from DeepSeek DSML text markup |
| 📝&nbsp;[#77645](https://github.com/openclaw/openclaw/issues/77645) | 1 | Local memory/embedding | @aderius | memory status --deep reports QMD embeddings unavailable when searchMode=search intentionally disables vectors |
| 📝&nbsp;[#77090](https://github.com/openclaw/openclaw/issues/77090) | 1 | Local model runtime | @djpollock | Feature: Auto-revert to primary model after image analysis |
| 🔀&nbsp;[#73667](https://github.com/openclaw/openclaw/pull/73667) | 1 | Local memory/embedding | @0xCNAI | Bound active-memory recall latency and jitter QMD startup |
| 📝&nbsp;[#73144](https://github.com/openclaw/openclaw/issues/73144) | 1 | Open-weight/provider behavior | @shaolin-cloud | Model switch experience: 5 issues when switching from qwen3.6-plus to deepseek-v4-pro |
| 📝&nbsp;[#67593](https://github.com/openclaw/openclaw/issues/67593) | 1 | Open-weight/provider behavior | @dario-github | feat: add Kimi/Moonshot provider usage and balance display |
| 📝&nbsp;[#61834](https://github.com/openclaw/openclaw/issues/61834) | 1 | Local memory/embedding | @kouka-t0yohei | [Feature]: expose QMD no-rerank for memory.qmd query mode |
| 📝&nbsp;[#41135](https://github.com/openclaw/openclaw/issues/41135) | 1 | Local model runtime | @tardis-create | [Feature]: Add provider-profile routing policies for multi-account OAuth/API pools (starting with google-gemini-cli) |
| 🔀&nbsp;[#90706](https://github.com/openclaw/openclaw/pull/90706) | 0 | OpenAI-compatible/proxy | @snowzlm | fix(OpenAI Responses): disable item id replay for storeless providers |
| 🔀&nbsp;[#90705](https://github.com/openclaw/openclaw/pull/90705) | 0 | OpenAI-compatible/proxy | @LiuwqGit | fix(llm): preserve streamed tool args when Responses done omits arguments |
| 🔀&nbsp;[#90703](https://github.com/openclaw/openclaw/pull/90703) | 0 | OpenAI-compatible/proxy | @Alex-Govorov | Support compat reasoning levels for thinking xhigh |
| 📝&nbsp;[#90702](https://github.com/openclaw/openclaw/issues/90702) | 0 | Model routing/config | @brtkwr | [Bug]: blockedUntil for subscription_limit set far in the future never re-probes when no fallback is configured |
| 🔀&nbsp;[#90689](https://github.com/openclaw/openclaw/pull/90689) | 0 | OpenAI-compatible/proxy | @ly85206559 | fix(agents): align custom provider auth labels with runtime (#82020) |
| 🔀&nbsp;[#90686](https://github.com/openclaw/openclaw/pull/90686) | 0 | Model routing/config | @rohitjavvadi | fix(gateway): honor profile auth for SecretRef model entries |
| 📝&nbsp;[#90685](https://github.com/openclaw/openclaw/issues/90685) | 0 | Model routing/config | @rohitjavvadi | models.list marks auth-profile-backed SecretRef providers unavailable |
| 📝&nbsp;[#90684](https://github.com/openclaw/openclaw/issues/90684) | 0 | Open-weight/provider behavior | @studentzhou-svg | Feishu (and non-Discord channels) should apply sanitizeAssistantVisibleText() on outbound text |
| 🔀&nbsp;[#90683](https://github.com/openclaw/openclaw/pull/90683) | 0 | Local model runtime | @JuanHuaXu | fix: retry safe post-tool continuation turns |
| 📝&nbsp;[#90675](https://github.com/openclaw/openclaw/issues/90675) | 0 | OpenAI-compatible/proxy | @JohnnyBlack123 | [Bug]: Dashboard/agent fake tool calls with dmxapi model; native claude route returns incomplete terminal response |
| 📝&nbsp;[#90674](https://github.com/openclaw/openclaw/issues/90674) | 0 | Model/provider behavior | @motteman | Gateway writes usage.cost: 0 for model strings absent from its internal price table (silent cost under-reporting) |
| 📝&nbsp;[#90657](https://github.com/openclaw/openclaw/issues/90657) | 0 | OpenAI-compatible/proxy | @snowzlm | tracking(OpenAI Responses): reproduce storeless replay and strict state/stream regressions in GitHub Actions |
| 📝&nbsp;[#90642](https://github.com/openclaw/openclaw/issues/90642) | 0 | Local/media model provider | @ruizcrp | [Feature]: Gemma4-12b (and other models) audio not supported yet |
| 🔀&nbsp;[#90613](https://github.com/openclaw/openclaw/pull/90613) | 0 | Model routing/config | @openperf | fix(agents): propagate ADC credential marker so google-vertex passes isWritableProviderConfig |
| 🔀&nbsp;[#90609](https://github.com/openclaw/openclaw/pull/90609) | 0 | Model routing/config | @849261680 | fix(google): preserve Vertex ADC catalog auth |
| 🔀&nbsp;[#90603](https://github.com/openclaw/openclaw/pull/90603) | 0 | Model routing/config | @Bartok9 | fix(secrets): use configured default agent ID in auth/model path discovery (#90573) |
| 🔀&nbsp;[#90594](https://github.com/openclaw/openclaw/pull/90594) | 0 | Model routing/config | @Tosko4 | fix(android): align provider readiness with available models |
| 🔀&nbsp;[#90593](https://github.com/openclaw/openclaw/pull/90593) | 0 | OpenAI-compatible/proxy | @849261680 | fix: preserve LM Studio Responses tool arguments |
| 📝&nbsp;[#90585](https://github.com/openclaw/openclaw/issues/90585) | 0 | Local model runtime | @ceo-nada | [Bug]: [REGRESSION] Tool calls with arguments arrive as empty objects when using LM Studio (openai-responses API). |
| 🔀&nbsp;[#90574](https://github.com/openclaw/openclaw/pull/90574) | 0 | OpenAI-compatible/proxy | @BSG2000 | fix(openai): omit gpt-5.5 tool reasoning effort |
| 📝&nbsp;[#90570](https://github.com/openclaw/openclaw/issues/90570) | 0 | OpenAI-compatible/proxy | @Osshaikh | Azure AI Foundry models (/openai/v1/responses) fail with 400 Invalid value and 400 schema mismatch across all GPT-5.x deployments |
| 📝&nbsp;[#90567](https://github.com/openclaw/openclaw/issues/90567) | 0 | OpenAI-compatible/proxy | @tinypoint-xy | Bug: pdf tool fails with 401 on xiaomi token-plan provider |
| 📝&nbsp;[#90556](https://github.com/openclaw/openclaw/issues/90556) | 0 | Local model runtime | @Wsq-159 | Chat UI: Display response latency under each message |
| 🔀&nbsp;[#90539](https://github.com/openclaw/openclaw/pull/90539) | 0 | Open-weight/provider behavior | @sahibzada-allahyar | fix(agents): skip foundry aliases for deepseek thinking |
| 📝&nbsp;[#90538](https://github.com/openclaw/openclaw/issues/90538) | 0 | Local memory/embedding | @itanyplus | [Bug] Memory Dreaming Promotion silently no-ops: cron isolated sessions get trigger=user instead of cron |
| 📝&nbsp;[#90536](https://github.com/openclaw/openclaw/issues/90536) | 0 | Model routing/config | @ozp | OpenAI OAuth missing 'model.request' scope — GPT-5.5 falls back silently |
| 🔀&nbsp;[#90533](https://github.com/openclaw/openclaw/pull/90533) | 0 | OpenAI-compatible/proxy | @clawsweeper[bot] | fix(openai): accept missing content-type on ChatGPT Responses SSE stream |
| 📝&nbsp;[#90528](https://github.com/openclaw/openclaw/issues/90528) | 0 | Model routing/config | @amoni094 | [Bug]: OpenAI/Codex OAuth Profile Not Attached to Inference Requests |
| 📝&nbsp;[#90520](https://github.com/openclaw/openclaw/issues/90520) | 0 | Open-weight/provider behavior | @wlassalle724 | Microsoft Foundry DeepSeek V4 alias providers still inject `thinking` after #87737 fix |
| 🔀&nbsp;[#90514](https://github.com/openclaw/openclaw/pull/90514) | 0 | Model routing/config | @baskduf | fix(session): clear stale fallback model state on reset |
| 🔀&nbsp;[#90513](https://github.com/openclaw/openclaw/pull/90513) | 0 | Model/provider behavior | @sahibzada-allahyar | fix(anthropic): add haiku catalog entry |
| 📝&nbsp;[#90508](https://github.com/openclaw/openclaw/issues/90508) | 0 | Local memory/embedding | @joeykrug | memory-core main reindex thrashes, leaks main.sqlite.tmp files, and leaves memory_search paused after repair |
| 🔀&nbsp;[#90507](https://github.com/openclaw/openclaw/pull/90507) | 0 | Model routing/config | @sahibzada-allahyar | fix(doctor): preserve codex context metadata |
| 📝&nbsp;[#90506](https://github.com/openclaw/openclaw/issues/90506) | 0 | Model/provider behavior | @paulogogs | [Bug]: [Bug]: google-vertex models fail with model_not_found at runtime on 2026.5.28 and 2026.6.1 — direct Vertex API calls succeed with same credentials |
| 🔀&nbsp;[#90500](https://github.com/openclaw/openclaw/pull/90500) | 0 | Model routing/config | @TurboTheTurtle | Fix stale session routes for removed providers |
| 📝&nbsp;[#90496](https://github.com/openclaw/openclaw/issues/90496) | 0 | Model routing/config | @nguyenjustin214-lab | Discord channel remains trapped in oversized session after /new; compaction fails provider_error_4xx and model drifts from codex/gpt-5.5 to gpt-5.4 |
| 📝&nbsp;[#90471](https://github.com/openclaw/openclaw/issues/90471) | 0 | Model routing/config | @centralpc | [Bug]: Deleted provider session overrides persist in sessions.json — silent financial damage risk |
| 📝&nbsp;[#90466](https://github.com/openclaw/openclaw/issues/90466) | 0 | Local memory/embedding | @mrizzo123 | [Bug]:memory-core dreaming on 2026.6.1: session-corpus contains .jsonl.deleted.* paths; narrative phase writes fallback despite valid prose responses |
| 📝&nbsp;[#90465](https://github.com/openclaw/openclaw/issues/90465) | 0 | OpenAI-compatible/proxy | @jaylfc | Auto-discover models for the generic openai-completions provider from /v1/models |
| 📝&nbsp;[#90462](https://github.com/openclaw/openclaw/issues/90462) | 0 | Local model runtime | @al-osokin | Fallback provider can become pinned in session metadata and trap a chat on unavailable LM Studio model |
| 🔀&nbsp;[#90457](https://github.com/openclaw/openclaw/pull/90457) | 0 | Model routing/config | @ai-hpc | fix(models): persist agent catalog cache |
| 📝&nbsp;[#90454](https://github.com/openclaw/openclaw/issues/90454) | 0 | Local memory/embedding | @nocode-ananas | active-memory plugin discards verbose sub-agent responses as status=unavailable, surface_error reason=none |
| 🔀&nbsp;[#90453](https://github.com/openclaw/openclaw/pull/90453) | 0 | Local memory/embedding | @849261680 | fix(memory-core): guard searches during safe reindex |
| 🔀&nbsp;[#90451](https://github.com/openclaw/openclaw/pull/90451) | 0 | Model routing/config | @ooiuuii | fix(codex): honor legacy context overrides after OpenAI unification |
| 📝&nbsp;[#90448](https://github.com/openclaw/openclaw/issues/90448) | 0 | Model routing/config | @ooiuuii | Codex context override can fall back to 272k after 2026.6.1 OpenAI route unification |
| 🔀&nbsp;[#90447](https://github.com/openclaw/openclaw/pull/90447) | 0 | Local memory/embedding | @Kailigithub | fix(memory-core): resolve adapter default model for index identity state |
| 📝&nbsp;[#90445](https://github.com/openclaw/openclaw/issues/90445) | 0 | Model routing/config | @openkralle | Control Panel: Add tooltips/clarifying labels for Reasoning and Thinking dropdowns (Config↔UI naming collision) |
| 🔀&nbsp;[#90436](https://github.com/openclaw/openclaw/pull/90436) | 0 | Open-weight/provider behavior | @jacobtomlinson | Add NVIDIA Nemotron 3 Ultra default |
| 🔀&nbsp;[#90433](https://github.com/openclaw/openclaw/pull/90433) | 0 | Local memory/embedding | @xiaobao-k8s | fix(memory-core): exclude archived transcripts from Dreaming session corpus |
| 🔀&nbsp;[#90429](https://github.com/openclaw/openclaw/pull/90429) | 0 | Local model runtime | @christineyan4 | Fix LM Studio wizard prompter binding |
| 🔀&nbsp;[#90425](https://github.com/openclaw/openclaw/pull/90425) | 0 | Model/provider behavior | @toruvieI | fix(openai): preserve encrypted reasoning replay ids |
| 🔀&nbsp;[#90422](https://github.com/openclaw/openclaw/pull/90422) | 0 | Local memory/embedding | @Alix-007 | fix(memory-core): keep durable index identity visible during safe reindex |
| 📝&nbsp;[#90420](https://github.com/openclaw/openclaw/issues/90420) | 0 | Model routing/config | @ooiuuii | Codex runtime route is hard to verify after the 2026.6.1 openai-codex migration |
| 📝&nbsp;[#90414](https://github.com/openclaw/openclaw/issues/90414) | 0 | Local memory/embedding | @AS76 | agentmemory__memory_search returns "index metadata is missing" persistently (memory-core manager state cache) |
| 📝&nbsp;[#90413](https://github.com/openclaw/openclaw/issues/90413) | 0 | Local memory/embedding | @colinmac-boop | memory status always reports "Vector search: paused" with blank expected model (2026.6.1) |
| 🔀&nbsp;[#90407](https://github.com/openclaw/openclaw/pull/90407) | 0 | Local memory/embedding | @sahibzada-allahyar | fix(memory-lancedb): align apache arrow peer dependency |
| 📝&nbsp;[#90403](https://github.com/openclaw/openclaw/issues/90403) | 0 | Model routing/config | @nerv00kaworu | [Performance] Model Picker UI very slow in v2026.5.28 |
| 🔀&nbsp;[#90401](https://github.com/openclaw/openclaw/pull/90401) | 0 | OpenAI-compatible/proxy | @danyurkin | docs(local-models): add Atomic Chat as an OpenAI-compatible local server |
| 🔀&nbsp;[#90399](https://github.com/openclaw/openclaw/pull/90399) | 0 | OpenAI-compatible/proxy | @baanish | fix(openai): send Accept: text/event-stream on ChatGPT Responses |
| 🔀&nbsp;[#90397](https://github.com/openclaw/openclaw/pull/90397) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(openai): skip unreadable responses tool schemas<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90395](https://github.com/openclaw/openclaw/pull/90395) | 0 | Local memory/embedding | @chengzhichao-xydt | fix(memory-core): write meta after sync when identity is missing with existing chunks |
| 🔀&nbsp;[#90383](https://github.com/openclaw/openclaw/pull/90383) | 0 | Local model runtime | @vincentkoc | fix(ollama): skip unreadable tool schemas<br>Assignee: vincentkoc |
| 📝&nbsp;[#90382](https://github.com/openclaw/openclaw/issues/90382) | 0 | OpenAI-compatible/proxy | @baanish | [Bug]: ChatGPT-OAuth gpt-5.5 fails with invalid_provider_content_type after 2026.6.1 (SDK Responses stream missing Accept: text/event-stream) |
| 📝&nbsp;[#90372](https://github.com/openclaw/openclaw/issues/90372) | 0 | Local model runtime | @JsuHod | [Bug]: Ollama cloud model received a 14M-token prompt before OpenClaw detected context overflow |
| 📝&nbsp;[#90368](https://github.com/openclaw/openclaw/issues/90368) | 0 | Model routing/config | @xdemocle | 2026.6.1: agent_model_catalogs / model_capability_cache tables defined but never written; models list takes 25–53s |
| 📝&nbsp;[#90361](https://github.com/openclaw/openclaw/issues/90361) | 0 | Local memory/embedding | @AyitLabs | [Bug]:Intermittent memory_search "index metadata is missing" despite valid builtin memory index; likely search/reindex race. Locally hotfixed. |
| 🔀&nbsp;[#90357](https://github.com/openclaw/openclaw/pull/90357) | 0 | Model routing/config | @alkor2000 | fix(agents): resolve compaction model alias before dispatch |
| 🔀&nbsp;[#90356](https://github.com/openclaw/openclaw/pull/90356) | 0 | Model routing/config | @sovushik | fix(status): use legacy Codex OAuth profiles for OpenAI usage |
| 📝&nbsp;[#90349](https://github.com/openclaw/openclaw/issues/90349) | 0 | Model routing/config | @AungMyoKyaw | Feature: Context Budget/Compactor — intelligent prompt slimming for small-context models |
| 📝&nbsp;[#90342](https://github.com/openclaw/openclaw/issues/90342) | 0 | Local model runtime | @AungMyoKyaw | Feature: Model Cookbook — hardware-aware model recommendations with one-click download/serve |
| 📝&nbsp;[#90340](https://github.com/openclaw/openclaw/issues/90340) | 0 | Model routing/config | @toruvieI | [Bug]: Auto-compaction does not resolve compaction model aliases before dispatch |
| 📝&nbsp;[#90338](https://github.com/openclaw/openclaw/issues/90338) | 0 | Local memory/embedding | @junxuku-byte | Memory index meta never written when gateway auto-sync finds identity missing with existing chunks |
| 🔀&nbsp;[#90337](https://github.com/openclaw/openclaw/pull/90337) | 0 | Model routing/config | @whiteyzy | fix(anthropic): add Claude Haiku 4.5 to static model catalog |
| 🔀&nbsp;[#90336](https://github.com/openclaw/openclaw/pull/90336) | 0 | Local memory/embedding | @osolmaz | fix(memory): fail fast when embeddings provider is unavailable |
| 🔀&nbsp;[#90331](https://github.com/openclaw/openclaw/pull/90331) | 0 | Model routing/config | @Daozheyuanxi | fix(agents): harden gateway config self-edits |
| 🔀&nbsp;[#90330](https://github.com/openclaw/openclaw/pull/90330) | 0 | OpenAI-compatible/proxy | @sercada | Fix ChatGPT Codex streams without content-type |
| 🔀&nbsp;[#90328](https://github.com/openclaw/openclaw/pull/90328) | 0 | Model routing/config | @ooiuuii | Expose model picker agent runtimes |
| 🔀&nbsp;[#90327](https://github.com/openclaw/openclaw/pull/90327) | 0 | OpenAI-compatible/proxy | @aaajiao | fix(openai): send Codex request contract headers on the boundary-aware transport |
| 🔀&nbsp;[#90326](https://github.com/openclaw/openclaw/pull/90326) | 0 | Model routing/config | @obuchowski | fix(fireworks): resolve catalog model limits from plugin.json via core |
| 🔀&nbsp;[#90323](https://github.com/openclaw/openclaw/pull/90323) | 0 | Local memory/embedding | @googlerest | fix(memory): replace node:sqlite with better-sqlite3 to enable sqlite-vec on macOS |
| 🔀&nbsp;[#90321](https://github.com/openclaw/openclaw/pull/90321) | 0 | Model routing/config | @ooiuuii | Normalize legacy Codex session runtime state |
| 🔀&nbsp;[#90319](https://github.com/openclaw/openclaw/pull/90319) | 0 | Model routing/config | @ooiuuii | Add Codex session route migration coverage |
| 🔀&nbsp;[#90317](https://github.com/openclaw/openclaw/pull/90317) | 0 | Model routing/config | @ooiuuii | Add Codex multi-agent config migration coverage |
| 📝&nbsp;[#90315](https://github.com/openclaw/openclaw/issues/90315) | 0 | Local model runtime | @civiltox | [Bug]: Ollama Cloud live-discovered model loses capability metadata in gateway catalog |
| 📝&nbsp;[#90313](https://github.com/openclaw/openclaw/issues/90313) | 0 | Local memory/embedding | @Adam-Researchh | Dreaming session-corpus: cron classification doesn't follow subagent parentage; archived (`.deleted`/`.reset`) transcripts re-ingested |
| 🔀&nbsp;[#90310](https://github.com/openclaw/openclaw/pull/90310) | 0 | OpenAI-compatible/proxy | @wangmiao0668000666 | fix(openai-responses): sanitize null content before SDK serialization (#90094) |
| 🔀&nbsp;[#90304](https://github.com/openclaw/openclaw/pull/90304) | 0 | Local memory/embedding | @osolmaz | feat(memory): support qmd query rerank toggle |
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
| 🔀&nbsp;[#90264](https://github.com/openclaw/openclaw/pull/90264) | 0 | Local memory/embedding | @osolmaz | fix(memory): move local embeddings to llama.cpp provider |
| 🔀&nbsp;[#90260](https://github.com/openclaw/openclaw/pull/90260) | 0 | Model/provider behavior | @yetval | fix(agents): decode xai and venice tool-call arguments exactly once |
| 🔀&nbsp;[#90249](https://github.com/openclaw/openclaw/pull/90249) | 0 | Model/provider behavior | @vincentkoc | fix(providers): skip unreadable Google tool schemas<br>Assignee: vincentkoc |
| 📝&nbsp;[#90243](https://github.com/openclaw/openclaw/issues/90243) | 0 | Model routing/config | @silvesterxm | feat(llm/google-vertex): Support physical model mapping/aliasing to support Google's Priority and Flex PayGo tiers |
| 🔀&nbsp;[#90242](https://github.com/openclaw/openclaw/pull/90242) | 0 | Open-weight/provider behavior | @vincentkoc | fix(providers): skip unreadable Mistral tool schemas<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90235](https://github.com/openclaw/openclaw/pull/90235) | 0 | Local model runtime | @deepshekhardas | fix(gateway): repair Ollama dense stream — preserve replacement stream deltas and rich tool call deltas |
| 🔀&nbsp;[#90234](https://github.com/openclaw/openclaw/pull/90234) | 0 | Model routing/config | @ferminquant | fix(agents): filter unresolved model registry rows |
| 🔀&nbsp;[#90221](https://github.com/openclaw/openclaw/pull/90221) | 0 | Model routing/config | @wangmiao0668000666 | fix(compaction): allow compaction with aws-sdk auth without apiKey or headers |
| 🔀&nbsp;[#90210](https://github.com/openclaw/openclaw/pull/90210) | 0 | Model routing/config | @yichu10c | fix(anthropic): add claude-haiku-4-5 to static model catalog |
| 🔀&nbsp;[#90206](https://github.com/openclaw/openclaw/pull/90206) | 0 | Model routing/config | @mushuiyu886 | Fix Bedrock aws-sdk compaction auth |
| 🔀&nbsp;[#90205](https://github.com/openclaw/openclaw/pull/90205) | 0 | OpenAI-compatible/proxy | @jalehman | fix: tolerate missing streamed response content type |
| 🔀&nbsp;[#90200](https://github.com/openclaw/openclaw/pull/90200) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(agents): guard OpenAI strict tool diagnostics<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90196](https://github.com/openclaw/openclaw/pull/90196) | 0 | Local/media model provider | @theashbhat | feat(ios): Add Piper TTS as on-device voice engine option |
| 📝&nbsp;[#90193](https://github.com/openclaw/openclaw/issues/90193) | 0 | OpenAI-compatible/proxy | @jalehman | Refactor duplicate Codex Responses paths for agent turns and llm.complete |
| 📝&nbsp;[#90170](https://github.com/openclaw/openclaw/issues/90170) | 0 | Open-weight/provider behavior | @1240981163-lab | [Bug]: Possible token/cost regression after OpenClaw v2026.5.28 with DeepSeek v4-pro |
| 🔀&nbsp;[#90165](https://github.com/openclaw/openclaw/pull/90165) | 0 | Local memory/embedding | @rudi193-cmd | fix(memory): do not filter FTS keyword search by embedding model (#48300) |
| 🔀&nbsp;[#90149](https://github.com/openclaw/openclaw/pull/90149) | 0 | Model routing/config | @glenn-agent | fix: preserve user model on stale rollover |
| 📝&nbsp;[#90146](https://github.com/openclaw/openclaw/issues/90146) | 0 | Model routing/config | @nyuDSA | google-vertex: Missing gemini-3.1-flash-lite in provider catalog causes silent failure instead of error |
| 🔀&nbsp;[#90145](https://github.com/openclaw/openclaw/pull/90145) | 0 | Model routing/config | @pgondhi987 | fix: protect global agent config defaults [AI] |
| 📝&nbsp;[#90139](https://github.com/openclaw/openclaw/issues/90139) | 0 | Model/provider behavior | @PriceNing | dropThinkingBlocks sanitizer: short text replies shown as [assistant reasoning omitted] in TUI/webchat/WeChat |
| 🔀&nbsp;[#90138](https://github.com/openclaw/openclaw/pull/90138) | 0 | Model/provider behavior | @IamVNIE | fix(minimax): exempt M3 from thinking-disabled wrapper |
| 🔀&nbsp;[#90137](https://github.com/openclaw/openclaw/pull/90137) | 0 | Model/provider behavior | @lgezyxr | fix: strip thinking signatures from entries after compaction |
| 🔀&nbsp;[#90130](https://github.com/openclaw/openclaw/pull/90130) | 0 | Model routing/config | @vincentkoc | fix(auth): guard preferred provider metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90128](https://github.com/openclaw/openclaw/pull/90128) | 0 | Model routing/config | @Marvinthebored | fix(sessions): preserve user /model override across daily/idle session rollover (#90119) |
| 🔀&nbsp;[#90125](https://github.com/openclaw/openclaw/pull/90125) | 0 | Model routing/config | @bladin | fix(embedded-runner): distinguish model initialization errors from assistant execution errors |
| 🔀&nbsp;[#90124](https://github.com/openclaw/openclaw/pull/90124) | 0 | Model/provider behavior | @cbire880 | fix(agents): harden tool-call handling against A2A/model tool-call poisoning |
| 📝&nbsp;[#90119](https://github.com/openclaw/openclaw/issues/90119) | 0 | Model routing/config | @Marvinthebored | [Bug]: User /model override silently dropped on daily/idle session rollover (survives /new but not the 4AM reset) |
| 🔀&nbsp;[#90117](https://github.com/openclaw/openclaw/pull/90117) | 0 | Local memory/embedding | @arkyu2077 | fix: skip qmd zero-hit sync retry in memory_search |
| 🔀&nbsp;[#90116](https://github.com/openclaw/openclaw/pull/90116) | 0 | Model routing/config | @arkyu2077 | fix: add Claude Haiku 4.5 static catalog entries |
| 🔀&nbsp;[#90112](https://github.com/openclaw/openclaw/pull/90112) | 0 | Model routing/config | @vincentkoc | fix(commands): guard provider catalog aliases<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90110](https://github.com/openclaw/openclaw/pull/90110) | 0 | Model routing/config | @harjothkhara | [codex] fix Anthropic Haiku 4.5 static catalog |
| 🔀&nbsp;[#90109](https://github.com/openclaw/openclaw/pull/90109) | 0 | Model routing/config | @vincentkoc | fix(commands): guard manifest catalog filters<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90107](https://github.com/openclaw/openclaw/pull/90107) | 0 | Model routing/config | @vincentkoc | fix(commands): guard model provider aliases<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90106](https://github.com/openclaw/openclaw/pull/90106) | 0 | Model routing/config | @comeran | fix: add Claude Haiku 4.5 to static model catalog |
| 📝&nbsp;[#90094](https://github.com/openclaw/openclaw/issues/90094) | 0 | OpenAI-compatible/proxy | @xneone | openai-responses transport sends null content, rejected by strict providers (400 schema error) |
| 📝&nbsp;[#90093](https://github.com/openclaw/openclaw/issues/90093) | 0 | OpenAI-compatible/proxy | @richardmqq | openai-chatgpt-responses native replay sends encrypted reasoning and breaks next turn with invalid_encrypted_content |
| 📝&nbsp;[#90088](https://github.com/openclaw/openclaw/issues/90088) | 0 | Model routing/config | @maaron34 | anthropic (api_key) provider: Claude Haiku 4.5 missing from static model catalog → "Unknown model" (model_not_found) |
| 📝&nbsp;[#90086](https://github.com/openclaw/openclaw/issues/90086) | 0 | OpenAI-compatible/proxy | @richardmqq | Pi/native runtime routes openai-chatgpt-responses to boundary-aware transport and fails on ChatGPT Codex endpoint |
| 🔀&nbsp;[#90085](https://github.com/openclaw/openclaw/pull/90085) | 0 | Model routing/config | @vincentkoc | fix(gateway): guard model pricing metadata<br>Assignee: vincentkoc |
| 📝&nbsp;[#90083](https://github.com/openclaw/openclaw/issues/90083) | 0 | OpenAI-compatible/proxy | @jimmielightner | [Bug]: 2026.6.1 OpenAI ChatGPT Responses transport fails with invalid_provider_content_type for gpt-5.4/gpt-5.5 |
| 📝&nbsp;[#90082](https://github.com/openclaw/openclaw/issues/90082) | 0 | Local memory/embedding | @ryswork1993 | [Bug] active-memory circuit breaker too aggressive; fallback prompt pollutes main session (v2026.6.1) |
| 🔀&nbsp;[#90077](https://github.com/openclaw/openclaw/pull/90077) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard provider discovery credential metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90075](https://github.com/openclaw/openclaw/pull/90075) | 0 | Local model runtime | @huazi-007 | fix(agents): detect unsigned thinking-only stall when reasoning payload inflates payloadCount |
| 📝&nbsp;[#90074](https://github.com/openclaw/openclaw/issues/90074) | 0 | Model routing/config | @holgergruenhagen | OpenAI image generation uses direct API-key route instead of Codex OAuth when explicit provider config exists |
| 🔀&nbsp;[#90073](https://github.com/openclaw/openclaw/pull/90073) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard metadata snapshot owner rows<br>Assignee: vincentkoc |
| 🔀&nbsp;[#90056](https://github.com/openclaw/openclaw/pull/90056) | 0 | Model routing/config | @openperf | fix(doctor): merge disjoint openai-codex model entries into canonical openai provider |
| 🔀&nbsp;[#90051](https://github.com/openclaw/openclaw/pull/90051) | 0 | OpenAI-compatible/proxy | @MonkeyLeeT | [codex] fix reasoning tag leakage |
| 📝&nbsp;[#90049](https://github.com/openclaw/openclaw/issues/90049) | 0 | Local model runtime | @zenassist26-create | Heartbeat sessions report 'assistant turn failed before producing content' on model initialization failure |
| 📝&nbsp;[#90047](https://github.com/openclaw/openclaw/issues/90047) | 0 | Model routing/config | @holgergruenhagen | Codex migration (2026.6.1) drops the gpt-5.5 model when a canonical `openai` provider exists for embeddings — agents go silent |
| 📝&nbsp;[#90042](https://github.com/openclaw/openclaw/issues/90042) | 0 | Local memory/embedding | @Bizman365 | Gateway memory_search index stuck dirty: provider.model empty during boot overwrites correct index identity |
| 📝&nbsp;[#90036](https://github.com/openclaw/openclaw/issues/90036) | 0 | Model routing/config | @nexic-hh | Session model route drifts from openai/gpt-5.5 to openai-codex/gpt-5.5 with native Codex runtime |
| 🔀&nbsp;[#90033](https://github.com/openclaw/openclaw/pull/90033) | 0 | OpenAI-compatible/proxy | @obuchowski | fix(llm): apply model.compat.sendSessionAffinityHeaders at openai-transport-stream |
| 🔀&nbsp;[#90030](https://github.com/openclaw/openclaw/pull/90030) | 0 | Local memory/embedding | @sahibzada-allahyar | fix(memory-core): skip qmd zero-hit search sync |
| 🔀&nbsp;[#90029](https://github.com/openclaw/openclaw/pull/90029) | 0 | Model routing/config | @fuller-stack-dev | feat: refresh OpenCode Go model catalog |
| 🔀&nbsp;[#90028](https://github.com/openclaw/openclaw/pull/90028) | 0 | Model routing/config | @jalehman | docs: clarify legacy openai-codex auth |
| 📝&nbsp;[#90023](https://github.com/openclaw/openclaw/issues/90023) | 0 | Local memory/embedding | @ruben2000de | QMD memory_search zero-hit queries trigger synchronous force sync and stall interactive turns |
| 📝&nbsp;[#90021](https://github.com/openclaw/openclaw/issues/90021) | 0 | Model routing/config | @claw0gang | OpenAI model with agentRuntime.id "openclaw" appears to switch to OpenAI Codex runtime after first Telegram message |
| 🔀&nbsp;[#90019](https://github.com/openclaw/openclaw/pull/90019) | 0 | Local memory/embedding | @sahibzada-allahyar | fix(memory-search): default periodic sync fallback |
| 📝&nbsp;[#90015](https://github.com/openclaw/openclaw/issues/90015) | 0 | Open-weight/provider behavior | @SebTardif | DSML recovery buffer grows without bound on unclosed DSML blocks |
| 🔀&nbsp;[#89983](https://github.com/openclaw/openclaw/pull/89983) | 0 | Model/provider behavior | @vincentkoc | fix(agents): isolate provider attribution manifest rows<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89981](https://github.com/openclaw/openclaw/pull/89981) | 0 | Model/provider behavior | @mycarrysun | fix(diagnostics-otel): keep full model id on spans instead of collapsing to "unknown" |
| 🔀&nbsp;[#89979](https://github.com/openclaw/openclaw/pull/89979) | 0 | Model routing/config | @vincentkoc | fix(config): isolate provider auto-enable rows<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89972](https://github.com/openclaw/openclaw/pull/89972) | 0 | Local memory/embedding | @RomneyDa | feat(watch): replace chokidar dep with in-repo chokidar-slim + async add API |
| 🔀&nbsp;[#89961](https://github.com/openclaw/openclaw/pull/89961) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard manifest suppression metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89957](https://github.com/openclaw/openclaw/pull/89957) | 0 | Local memory/embedding | @kiagentkronos-cell | docs: add section on extending memory with corpus supplements |
| 🔀&nbsp;[#89952](https://github.com/openclaw/openclaw/pull/89952) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard provider auth choice metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89948](https://github.com/openclaw/openclaw/pull/89948) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard plugin id alias metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89946](https://github.com/openclaw/openclaw/pull/89946) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard provider policy metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89945](https://github.com/openclaw/openclaw/pull/89945) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard provider discovery metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89940](https://github.com/openclaw/openclaw/pull/89940) | 0 | Model routing/config | @vincentkoc | fix(models): guard manifest model id metadata<br>Assignee: vincentkoc |
| 📝&nbsp;[#89937](https://github.com/openclaw/openclaw/issues/89937) | 0 | Local memory/embedding | @Enominera | [Bug] before_prompt_build hook not triggered in agent-runner / embedded-agent path (chat user messages) |
| 🔀&nbsp;[#89936](https://github.com/openclaw/openclaw/pull/89936) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard model suppression metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89933](https://github.com/openclaw/openclaw/pull/89933) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard synthetic auth metadata<br>Assignee: vincentkoc |
| 📝&nbsp;[#89927](https://github.com/openclaw/openclaw/issues/89927) | 0 | Model routing/config | @A1fred-AI | Fallback sessions don't terminate parent lane → concurrent orchestrator lanes, duplicate billed subagent dispatches, and wedged sessions |
| 🔀&nbsp;[#89918](https://github.com/openclaw/openclaw/pull/89918) | 0 | Model/provider behavior | @alkor2000 | fix(vertex): route eu/us multi-region to .rep.googleapis.com host |
| 🔀&nbsp;[#89917](https://github.com/openclaw/openclaw/pull/89917) | 0 | Model routing/config | @vincentkoc | fix(agents): guard provider auth alias metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89910](https://github.com/openclaw/openclaw/pull/89910) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard provider auth choice metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89905](https://github.com/openclaw/openclaw/pull/89905) | 0 | Model routing/config | @dwc1997 | fix(hooks): honor hook-level model override for session-memory slug generation |
| 🔀&nbsp;[#89901](https://github.com/openclaw/openclaw/pull/89901) | 0 | Model/provider behavior | @dwc1997 | fix(vertex): support eu and us multi-region endpoints |
| 🔀&nbsp;[#89899](https://github.com/openclaw/openclaw/pull/89899) | 0 | Local/media model provider | @zhangguiping-xydt | fix #89425: [Bug]: Missing extensions/speech-core/ in npm tarball (v2026.5.28) — "Unable to resolve bundled plugin public surface speech-core/runtime-api.js" |
| 📝&nbsp;[#89891](https://github.com/openclaw/openclaw/issues/89891) | 0 | Model/provider behavior | @Wimcomander | [Bug]: Vertex AI eu multi-region unreachable — host prefix is hardcoded |
| 🔀&nbsp;[#89880](https://github.com/openclaw/openclaw/pull/89880) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard model catalog registration metadata<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89874](https://github.com/openclaw/openclaw/pull/89874) | 0 | Local model runtime | @openperf | fix(agents): detect unsigned thinking-only stall when reasoning payload inflates payloadCount |
| 🔀&nbsp;[#89832](https://github.com/openclaw/openclaw/pull/89832) | 0 | OpenAI-compatible/proxy | @KrasimirKralev | fix(config): allow requiresReasoningContentOnAssistantMessages in ModelCompatSchema |
| 🔀&nbsp;[#89818](https://github.com/openclaw/openclaw/pull/89818) | 0 | Model/provider behavior | @masatohoshino | fix(providers): forward stop sequences in bundled Anthropic transports |
| 📝&nbsp;[#89787](https://github.com/openclaw/openclaw/issues/89787) | 0 | Open-weight/provider behavior | @ArthurusDent | [Bug]: Agent stalls indefinitely when model emits stopReason="stop" with no toolCall - only thinking block generated |
| 📝&nbsp;[#89758](https://github.com/openclaw/openclaw/issues/89758) | 0 | Model routing/config | @Enominera | [Bug] overloaded_error triggers immediate rotate_profile without retry, causing cascade fallback on transient provider overload |
| 🔀&nbsp;[#89741](https://github.com/openclaw/openclaw/pull/89741) | 0 | Local memory/embedding | @TurboTheTurtle | fix(memory): add EPERM fallback for atomic reindex |
| 🔀&nbsp;[#89730](https://github.com/openclaw/openclaw/pull/89730) | 0 | Local model runtime | @vincentkoc | fix(agents): guard lean tool name reads<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89729](https://github.com/openclaw/openclaw/pull/89729) | 0 | OpenAI-compatible/proxy | @snowzlm | fix: skip Responses item id replay when store support is stripped |
| 📝&nbsp;[#89728](https://github.com/openclaw/openclaw/issues/89728) | 0 | OpenAI-compatible/proxy | @snowzlm | Custom OpenAI Responses-compatible providers still replay item ids when store support is stripped |
| 🔀&nbsp;[#89716](https://github.com/openclaw/openclaw/pull/89716) | 0 | OpenAI-compatible/proxy | @masatohoshino | fix(providers): strip cache-boundary marker from non-Anthropic prompts |
| 📝&nbsp;[#89706](https://github.com/openclaw/openclaw/issues/89706) | 0 | Model routing/config | @nyuDSA | github-copilot: gemini-3.1-pro appears in models list but fails silently when selected |
| 🔀&nbsp;[#89703](https://github.com/openclaw/openclaw/pull/89703) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(openai): guard responses tool payload names<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89692](https://github.com/openclaw/openclaw/pull/89692) | 0 | OpenAI-compatible/proxy | @draix | fix(config): allow compat.requiresReasoningContentOnAssistantMessages in model config |
| 📝&nbsp;[#89691](https://github.com/openclaw/openclaw/issues/89691) | 0 | Local memory/embedding | @joeykrug | Active-memory embedded memory_search intermittently loses embedding provider and falls back to FTS-only |
| 🔀&nbsp;[#89669](https://github.com/openclaw/openclaw/pull/89669) | 0 | Model/provider behavior | @vincentkoc | fix(agents): contain provider schema hook failures<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89667](https://github.com/openclaw/openclaw/pull/89667) | 0 | OpenAI-compatible/proxy | @luyao618 | fix(config): allow requiresReasoningContentOnAssistantMessages in ModelCompatSchema [AI-assisted] |
| 🔀&nbsp;[#89665](https://github.com/openclaw/openclaw/pull/89665) | 0 | Open-weight/provider behavior | @vincentkoc | fix(plugin-sdk): guard provider tool schema walks<br>Assignee: vincentkoc |
| 📝&nbsp;[#89664](https://github.com/openclaw/openclaw/issues/89664) | 0 | Model routing/config | @Stache73 | [Bug] secrets audit / doctor falsely flags static routing header as plaintext secret |
| 📝&nbsp;[#89660](https://github.com/openclaw/openclaw/issues/89660) | 0 | OpenAI-compatible/proxy | @kyKKK | [Bug]: requiresReasoningContentOnAssistantMessages missing from ModelCompatSchema — can't replicate native DeepSeek behavior on custom providers |
| 🔀&nbsp;[#89657](https://github.com/openclaw/openclaw/pull/89657) | 0 | Model routing/config | @vincentkoc | fix(plugins): harden installed index stale metadata<br>Assignee: vincentkoc |
| 📝&nbsp;[#89655](https://github.com/openclaw/openclaw/issues/89655) | 0 | Model routing/config | @kasanuowa | [Bug]: `NODE_USE_SYSTEM_CA=1` breaks `openai-codex` auth/keychain paths on macOS and can fail fresh runtime launch with `SecItemCopyMatching failed -50` |
| 🔀&nbsp;[#89652](https://github.com/openclaw/openclaw/pull/89652) | 0 | Local memory/embedding | @joeykrug | fix(plugins): load owning plugin for configured memory embedding provider at startup |
| 📝&nbsp;[#89651](https://github.com/openclaw/openclaw/issues/89651) | 0 | Local memory/embedding | @joeykrug | Gateway startup does not load the plugin owning a configured memory embedding provider (memorySearch.provider) |
| 🔀&nbsp;[#89647](https://github.com/openclaw/openclaw/pull/89647) | 0 | Model routing/config | @vincentkoc | fix(plugins): guard startup manifest channels<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89646](https://github.com/openclaw/openclaw/pull/89646) | 0 | Model routing/config | @vincentkoc | fix(model-catalog): guard model id policies<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89644](https://github.com/openclaw/openclaw/pull/89644) | 0 | Model routing/config | @vincentkoc | fix(model-catalog): skip unreadable catalog records<br>Assignee: vincentkoc |
| 📝&nbsp;[#89633](https://github.com/openclaw/openclaw/issues/89633) | 0 | Model routing/config | @goslingmanagment | Codex turn fails with generic Telegram fallback when invalid image tool model is configured, leaving child agent orphaned on full stdout pipe |
| 🔀&nbsp;[#89629](https://github.com/openclaw/openclaw/pull/89629) | 0 | Model routing/config | @Marvinthebored | feat(hooks): expose per-turn usageState on reply_payload_sending |
| 🔀&nbsp;[#89624](https://github.com/openclaw/openclaw/pull/89624) | 0 | Local model runtime | @vincentkoc | fix(ollama): guard tool schema normalization<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89618](https://github.com/openclaw/openclaw/pull/89618) | 0 | Local model runtime | @danyurkin | feat(atomicchat): add Atomic Chat as a bundled local provider |
| 📝&nbsp;[#89617](https://github.com/openclaw/openclaw/issues/89617) | 0 | Local model runtime | @danyurkin | Add Atomic Chat as a bundled local provider (OpenAI-compatible, 127.0.0.1:1337) |
| 🔀&nbsp;[#89613](https://github.com/openclaw/openclaw/pull/89613) | 0 | Model routing/config | @steipete | docs: document auth profile failure policy contract |
| 🔀&nbsp;[#89602](https://github.com/openclaw/openclaw/pull/89602) | 0 | Model routing/config | @zerone0x | fix(status): show effective channel model override |
| 🔀&nbsp;[#89584](https://github.com/openclaw/openclaw/pull/89584) | 0 | Local memory/embedding | @ubehera | feat(memory-core): optional cross-encoder rerank stage for memory search |
| 🔀&nbsp;[#89571](https://github.com/openclaw/openclaw/pull/89571) | 0 | Open-weight/provider behavior | @vincentkoc | fix(provider): harden provider tool schema hooks<br>Assignee: vincentkoc |
| 🔀&nbsp;[#89561](https://github.com/openclaw/openclaw/pull/89561) | 0 | Model routing/config | @luyao618 | fix(hooks): honor session-memory hook model override for LLM slug generation [AI-assisted] |
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
| 🔀&nbsp;[#89508](https://github.com/openclaw/openclaw/pull/89508) | 0 | OpenAI-compatible/proxy | @sweetcornna | fix(models): clarify provider model registration hint |
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
| 🔀&nbsp;[#89290](https://github.com/openclaw/openclaw/pull/89290) | 0 | Model/provider behavior | @amittell | [codex] Keep Codex waiting after raw reasoning progress |
| 📝&nbsp;[#89278](https://github.com/openclaw/openclaw/issues/89278) | 0 | Model routing/config | @kopl-blip | [Bug]: Codex OAuth refresh succeeds but cron/heartbeat fail with 10s auth refresh timeout |
| 🔀&nbsp;[#89273](https://github.com/openclaw/openclaw/pull/89273) | 0 | Model/provider behavior | @vincentkoc | fix(doctor): sanitize provider catalog findings |
| 📝&nbsp;[#89265](https://github.com/openclaw/openclaw/issues/89265) | 0 | Local model runtime | @CobraSoftware | [Feature]: More local providers |
| 📝&nbsp;[#89264](https://github.com/openclaw/openclaw/issues/89264) | 0 | Local memory/embedding | @C1-BA-B1-F3 | [Bug]: Dreaming deep promotion biased to stale 3-5 day old content; REM produces repetitive meta-themes; promotion gates bypassed via phase-signal boost |
| 📝&nbsp;[#89259](https://github.com/openclaw/openclaw/issues/89259) | 0 | Model/provider behavior | @swiser-nexa | EmbeddedAttemptSessionTakeoverError fires at ~120s on long Bedrock streams (fence whitelist too narrow?) |
| 🔀&nbsp;[#89251](https://github.com/openclaw/openclaw/pull/89251) | 0 | Local/media model provider | @mcaxtr | fix: deliver tts tool audio on whatsapp |
| 📝&nbsp;[#89233](https://github.com/openclaw/openclaw/issues/89233) | 0 | Local model runtime | @CameronWeller | [Bug]: Default models.providers.lmstudio.apiKey ships as plaintext placeholder 'lm-studio' - triggers false-positive security audit warning |
| 🔀&nbsp;[#89229](https://github.com/openclaw/openclaw/pull/89229) | 0 | Model/provider behavior | @vincentkoc | fix(llm): guard Anthropic provider tool descriptors |
| 🔀&nbsp;[#89221](https://github.com/openclaw/openclaw/pull/89221) | 0 | Model/provider behavior | @vincentkoc | fix(agents): guard Anthropic tool descriptors |
| 📝&nbsp;[#89202](https://github.com/openclaw/openclaw/issues/89202) | 0 | Model/provider behavior | @aaronescobar09 | [Bug]: Telegram heavy turns can cause incomplete codex-app server turn around compaction, including under OpenClaw runtime. |
| 📝&nbsp;[#89198](https://github.com/openclaw/openclaw/issues/89198) | 0 | Local/media model provider | @talentshf | Feature Request: Support Gateway TTS/STT in iOS App |
| 📝&nbsp;[#89197](https://github.com/openclaw/openclaw/issues/89197) | 0 | Model routing/config | @yangiit | Gateway agent run failure with no model reachable: chat.history returns incomplete state, Control UI clears conversation history |
| 📝&nbsp;[#89196](https://github.com/openclaw/openclaw/issues/89196) | 0 | Local memory/embedding | @yangiit | Dreaming REM: sub-session visible in session switcher + narrative diary fails to write to DREAMS.md |
| 🔀&nbsp;[#89194](https://github.com/openclaw/openclaw/pull/89194) | 0 | Model routing/config | @Kailigithub | fix: include name field in model_not_found remediation hint |
| 📝&nbsp;[#89192](https://github.com/openclaw/openclaw/issues/89192) | 0 | Model routing/config | @aaajiao | bug(models): model_not_found remediation message is incomplete - suggests `{ "id": ... }` but `name` is required and `api`/`baseUrl` are silently needed (misroutes to OpenAI) |
| 🔀&nbsp;[#89190](https://github.com/openclaw/openclaw/pull/89190) | 0 | Model/provider behavior | @lidge-jun | feat(xai): add grok-composer-2.5-fast model |
| 🔀&nbsp;[#89183](https://github.com/openclaw/openclaw/pull/89183) | 0 | Local model runtime | @ferminquant | fix(tui): keep local slash commands out of model prompts |
| 📝&nbsp;[#89173](https://github.com/openclaw/openclaw/issues/89173) | 0 | Local memory/embedding | @DerekEXS | External plugin tools (memory_store, memory_recall, etc.) not routed/exposed to the Agent in v2026.5.27+ |
| 📝&nbsp;[#89167](https://github.com/openclaw/openclaw/issues/89167) | 0 | Model routing/config | @devin-ai-integration[bot] | Session in status:failed remains bound as agent:main:main, crashing next TUI launch |
| 📝&nbsp;[#89164](https://github.com/openclaw/openclaw/issues/89164) | 0 | Model/provider behavior | @devin-ai-integration[bot] | Completed model responses occasionally do not persist to session jsonl despite trajectory recording success |
| 🔀&nbsp;[#89160](https://github.com/openclaw/openclaw/pull/89160) | 0 | Model/provider behavior | @joelnishanth | fix(agents): detect truncated API responses to prevent silent session hang |
| 🔀&nbsp;[#89155](https://github.com/openclaw/openclaw/pull/89155) | 0 | Open-weight/provider behavior | @Alex-vonAllmen | feat(openrouter): forward OpenClaw session id as session_id |
| 🔀&nbsp;[#89150](https://github.com/openclaw/openclaw/pull/89150) | 0 | Model routing/config | @ttruongatl | obs(model-fallback): emit `model.fallback.exhausted` counter on chain exhaustion |
| 📝&nbsp;[#89147](https://github.com/openclaw/openclaw/issues/89147) | 0 | Model/provider behavior | @scipher888 | Native hook relay starves mid-turn after long model-thinking gap (renewal loop tool-call-driven) |
| 🔀&nbsp;[#89138](https://github.com/openclaw/openclaw/pull/89138) | 0 | Local memory/embedding | @mushuiyu886 | fix #88009: [Feature]: batched memory embedding should batch over files |
| 🔀&nbsp;[#89133](https://github.com/openclaw/openclaw/pull/89133) | 0 | Model routing/config | @VACInc | Restore GPT-5.3 Codex Spark OAuth routing |
| 🔀&nbsp;[#89118](https://github.com/openclaw/openclaw/pull/89118) | 0 | Open-weight/provider behavior | @LiLan0125 | fix(outbound): sanitize message.send arguments to prevent runtime scaffolding leaks |
| 🔀&nbsp;[#89117](https://github.com/openclaw/openclaw/pull/89117) | 0 | Local memory/embedding | @abel-zer0 | Support Gemini Embedding 2 GA |
| 📝&nbsp;[#89114](https://github.com/openclaw/openclaw/issues/89114) | 0 | Open-weight/provider behavior | @superandylin | Minimax M3: /think menu missing xhigh, adaptive, max levels (provider profile limitation) |
| 🔀&nbsp;[#89109](https://github.com/openclaw/openclaw/pull/89109) | 0 | Open-weight/provider behavior | @openperf | fix(agents): block message-tool spam loops defeated by volatile message ids |
| 🔀&nbsp;[#89102](https://github.com/openclaw/openclaw/pull/89102) | 0 | Model routing/config | @steipete | refactor(auth): store auth profiles in SQLite |
| 📝&nbsp;[#89100](https://github.com/openclaw/openclaw/issues/89100) | 0 | Open-weight/provider behavior | @bobgitmcgrath | Sanitise outbound message.send tool arguments to prevent runtime scaffolding leak (FM-3) and chat_id routing bleed (FM-2) on weaker models |
| 🔀&nbsp;[#89091](https://github.com/openclaw/openclaw/pull/89091) | 0 | Local memory/embedding | @bennewell35 | fix(memory-core): retry narrative message reads |
| 📝&nbsp;[#89090](https://github.com/openclaw/openclaw/issues/89090) | 0 | OpenAI-compatible/proxy | @wujiaming88 | Bug: loopDetection cannot block message tool loops — volatile messageId in result defeats all critical-level detection paths |
| 🔀&nbsp;[#89088](https://github.com/openclaw/openclaw/pull/89088) | 0 | Model routing/config | @charles-openclaw | test(gateway): cover rollover model override preservation |
| 📝&nbsp;[#89087](https://github.com/openclaw/openclaw/issues/89087) | 0 | Model routing/config | @pitbuild | Bug: Session model override lost on UTC midnight rollover |
| 📝&nbsp;[#89051](https://github.com/openclaw/openclaw/issues/89051) | 0 | Local model runtime | @ArthurusDent | [Bug]: Embedded agent session silently hangs after auto-compaction with no error logging or recovery |
| 🔀&nbsp;[#89040](https://github.com/openclaw/openclaw/pull/89040) | 0 | Local model runtime | @Jerry-Xin | perf: avoid event-loop stall during embedded_run bootstrap-context |
| 🔀&nbsp;[#89039](https://github.com/openclaw/openclaw/pull/89039) | 0 | OpenAI-compatible/proxy | @Jerry-Xin | fix: prevent silent message loss from EmbeddedAttemptSessionTakeoverError |
| 🔀&nbsp;[#89029](https://github.com/openclaw/openclaw/pull/89029) | 0 | Model routing/config | @charles-openclaw | fix(cli): accept empty Claude end turns |
| 🔀&nbsp;[#89027](https://github.com/openclaw/openclaw/pull/89027) | 0 | Model routing/config | @Huangting-xy | fix(cli): prevent empty_response failover for completed thinking-only turns |
| 🔀&nbsp;[#89016](https://github.com/openclaw/openclaw/pull/89016) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(agents): guard OpenAI transport tool descriptors |
| 🔀&nbsp;[#89013](https://github.com/openclaw/openclaw/pull/89013) | 0 | OpenAI-compatible/proxy | @vincentkoc | fix(agents): materialize OpenAI tool schemas |
| 🔀&nbsp;[#89001](https://github.com/openclaw/openclaw/pull/89001) | 0 | OpenAI-compatible/proxy | @BSG2000 | fix: support Azure Responses text stream events |
| 🔀&nbsp;[#88999](https://github.com/openclaw/openclaw/pull/88999) | 0 | Local model runtime | @Huangting-xy | fix(cron): repair concatenated JSON keys from local-model tool-call parsers |
| 🔀&nbsp;[#88994](https://github.com/openclaw/openclaw/pull/88994) | 0 | Model routing/config | @vincentkoc | fix(agents): quarantine normalized runtime tools |
| 🔀&nbsp;[#88977](https://github.com/openclaw/openclaw/pull/88977) | 0 | Model routing/config | @vincentkoc | fix(agents): tolerate provider tool schema hook failures |
| 🔀&nbsp;[#88964](https://github.com/openclaw/openclaw/pull/88964) | 0 | OpenAI-compatible/proxy | @MonkeyLeeT | [codex] Repair context-engine tool-result pairing |
| 🔀&nbsp;[#88959](https://github.com/openclaw/openclaw/pull/88959) | 0 | Model routing/config | @vincentkoc | fix(plugins): ignore throwing provider runtime hooks |
| 🔀&nbsp;[#88958](https://github.com/openclaw/openclaw/pull/88958) | 0 | Model routing/config | @TurboTheTurtle | Fix BTW OAuth side-question routing |
| 🔀&nbsp;[#88956](https://github.com/openclaw/openclaw/pull/88956) | 0 | Model routing/config | @TurboTheTurtle | Repair compacted tool-result chains |
| 🔀&nbsp;[#88950](https://github.com/openclaw/openclaw/pull/88950) | 0 | Model routing/config | @vincentkoc | fix(plugins): ignore throwing provider policy hooks |
| 🔀&nbsp;[#88940](https://github.com/openclaw/openclaw/pull/88940) | 0 | OpenAI-compatible/proxy | @deepshekhardas | fix(llm): repairJson injects control chars for backslash b/f/n/r/t into Windows paths |
| 🔀&nbsp;[#88931](https://github.com/openclaw/openclaw/pull/88931) | 0 | Local model runtime | @vincentkoc | fix(agents): cap tool search fanout in lean mode |
| 🔀&nbsp;[#88917](https://github.com/openclaw/openclaw/pull/88917) | 0 | OpenAI-compatible/proxy | @physicswolf | fix: retry stale Responses reasoning replay safely |
| 📝&nbsp;[#88907](https://github.com/openclaw/openclaw/issues/88907) | 0 | Open-weight/provider behavior | @ivannin | Chronic agent failures on Telegram - LLM timeouts before configured timeout + silent incomplete turns + dead fallbacks (OpenRouter/DeepSeek+V4-Flash, v2026.5.28) |
| 🔀&nbsp;[#88906](https://github.com/openclaw/openclaw/pull/88906) | 0 | Model routing/config | @keshavbotagent | fix(openai): allow Codex Spark via harness |
| 🔀&nbsp;[#88905](https://github.com/openclaw/openclaw/pull/88905) | 0 | Local memory/embedding | @iFiras-Max1 | feat(dreaming): expose shadow-trial scoring in reports |
| 📝&nbsp;[#88902](https://github.com/openclaw/openclaw/issues/88902) | 0 | Model routing/config | @khalil-omer | [Bug]: Codex OAuth /btw still falls back to OpenAI Responses after /new |
| 🔀&nbsp;[#88893](https://github.com/openclaw/openclaw/pull/88893) | 0 | OpenAI-compatible/proxy | @bladin | fix: support Azure Responses API text content type |
| 🔀&nbsp;[#88890](https://github.com/openclaw/openclaw/pull/88890) | 0 | Local model runtime | @zhangguiping-xydt | fix #87768: [Bug]: push to talk mac os companion app hard codes thinking low |
| 🔀&nbsp;[#88887](https://github.com/openclaw/openclaw/pull/88887) | 0 | Local memory/embedding | @potterdigital | fix(memory-core): don't run the LLM reranker in vsearch/search modes |
| 🔀&nbsp;[#88884](https://github.com/openclaw/openclaw/pull/88884) | 0 | Local model runtime | @vincentkoc | fix(agents): trim web tools in lean mode |
| 🔀&nbsp;[#88882](https://github.com/openclaw/openclaw/pull/88882) | 0 | Local model runtime | @vincentkoc | test(gateway): add small model live profile |
| 🔀&nbsp;[#88881](https://github.com/openclaw/openclaw/pull/88881) | 0 | Local model runtime | @vincentkoc | fix(agents): trim media tools in lean mode |
| 🔀&nbsp;[#88880](https://github.com/openclaw/openclaw/pull/88880) | 0 | Model routing/config | @vincentkoc | fix(agents): project nullable tool schemas for providers |
| 🔀&nbsp;[#88878](https://github.com/openclaw/openclaw/pull/88878) | 0 | Model routing/config | @vincentkoc | fix(agents): project cron tool schemas for providers |
| 🔀&nbsp;[#88869](https://github.com/openclaw/openclaw/pull/88869) | 0 | Open-weight/provider behavior | @NianJiuZst | Add MiniMax M3 support to the bundled MiniMax provider |
| 📝&nbsp;[#88868](https://github.com/openclaw/openclaw/issues/88868) | 0 | Open-weight/provider behavior | @NianJiuZst | Add MiniMax M3 support to the bundled MiniMax provider |
| 📝&nbsp;[#88864](https://github.com/openclaw/openclaw/issues/88864) | 0 | Local memory/embedding | @MarsCNS | [Bug]: `memory-wiki` bridge imports all workspace artifacts into shared vault, causing `path-mismatch` error |
| 🔀&nbsp;[#88837](https://github.com/openclaw/openclaw/pull/88837) | 0 | Model routing/config | @charles-openclaw | fix(agent): use static catalog for skip-agent model resolution |
| 🔀&nbsp;[#88822](https://github.com/openclaw/openclaw/pull/88822) | 0 | Local model runtime | @vincentkoc | fix(agents): compact lean local tool catalogs |
| 🔀&nbsp;[#88800](https://github.com/openclaw/openclaw/pull/88800) | 0 | Model routing/config | @TurboTheTurtle | fix(models): keep generated secret refs out of plaintext |
| 🔀&nbsp;[#88789](https://github.com/openclaw/openclaw/pull/88789) | 0 | Local model runtime | @vincentkoc | feat(agents): auto-trim lean local tools |
| 🔀&nbsp;[#88771](https://github.com/openclaw/openclaw/pull/88771) | 0 | Local model runtime | @vincentkoc | fix(agents): stream phased text deltas incrementally |
| 🔀&nbsp;[#88754](https://github.com/openclaw/openclaw/pull/88754) | 0 | Open-weight/provider behavior | @Kailigithub | fix(text): normalize CJK/fullwidth quotes in reasoning tag delimiters |
| 🔀&nbsp;[#88748](https://github.com/openclaw/openclaw/pull/88748) | 0 | Model routing/config | @jason-allen-oneal | fix(gemini): bridge OAuth profiles into CLI runtime |
| 🔀&nbsp;[#88709](https://github.com/openclaw/openclaw/pull/88709) | 0 | Model routing/config | @MertBasar0 | fix(auth): cooldown inline api key billing failures |
| 📝&nbsp;[#88707](https://github.com/openclaw/openclaw/issues/88707) | 0 | Model routing/config | @podulator | [Bug] Regression 2026.5.27→2026.5.28: "No API provider registered for api: bedrock-converse-stream" — pi-ai removal breaks Bedrock provider registration; bearer token auth broken |
| 📝&nbsp;[#88705](https://github.com/openclaw/openclaw/issues/88705) | 0 | Local memory/embedding | @Peilsender | Bug: npm updates drop node-llama-cpp, breaking local memory_search after every OpenClaw update |
| 🔀&nbsp;[#88696](https://github.com/openclaw/openclaw/pull/88696) | 0 | Local memory/embedding | @zhangguiping-xydt | fix #70559: runUnsafeReindex crashes with "no such table: chunks_vec" when sqlite-vec is enabled |
| 📝&nbsp;[#88679](https://github.com/openclaw/openclaw/issues/88679) | 0 | Model routing/config | @junxuku-byte | [Feature]: Per-Tool Model Routing — route specific tool calls to different models |
| 📝&nbsp;[#88657](https://github.com/openclaw/openclaw/issues/88657) | 0 | Open-weight/provider behavior | @mikefaierberg-byte | Bug: DeepSeek V4 Flash incomplete turn (payloads=0, tools=2, replaySafe=no, stopReason=stop) in 2026.5.27/28 |
| 🔀&nbsp;[#88645](https://github.com/openclaw/openclaw/pull/88645) | 0 | Local model runtime | @whiteyzy | fix(llm): use JSON5 as intermediate fallback in parseStreamingJson to avoid partial-json key corruption |
| 📝&nbsp;[#88632](https://github.com/openclaw/openclaw/issues/88632) | 0 | Local model runtime | @wangwllu | [Bug]: gateway model-run sessions accumulate until session maxEntries cap |
| 🔀&nbsp;[#88630](https://github.com/openclaw/openclaw/pull/88630) | 0 | Model routing/config | @vincentkoc | fix(codex): avoid guardian review for local models |
| 📝&nbsp;[#88616](https://github.com/openclaw/openclaw/issues/88616) | 0 | Model routing/config | @Alex-vonAllmen | [Feature]: Forward session_id to OpenRouter for sticky routing & prompt caching |
| 📝&nbsp;[#88615](https://github.com/openclaw/openclaw/issues/88615) | 0 | Local memory/embedding | @Joelincn | [Bug]: sqlite-vec fails to load on Node 22 Linux x64 (Vector store: unknown, distinct from #64776 and #65033) |
| 📝&nbsp;[#88579](https://github.com/openclaw/openclaw/issues/88579) | 0 | Model routing/config | @Goron01 | LLM error: Authorization Not Found - SecretRef apiKey not properly resolved in Gateway |
| 📝&nbsp;[#88562](https://github.com/openclaw/openclaw/issues/88562) | 0 | Model routing/config | @mnowrot | [Bug]: models.json generator writes apiKey as plain string instead of secret-ref object |
| 🔀&nbsp;[#88553](https://github.com/openclaw/openclaw/pull/88553) | 0 | Model routing/config | @yu-xin-c | fix(agents): unblock fallback classification tests |
| 🔀&nbsp;[#88551](https://github.com/openclaw/openclaw/pull/88551) | 0 | Model routing/config | @yu-xin-c | fix(agents): skip auth gate for CLI-owned transport |
| 📝&nbsp;[#88548](https://github.com/openclaw/openclaw/issues/88548) | 0 | Model routing/config | @saju01 | GitHub Copilot: static default model list shadows live entitlement discovery |
| 🔀&nbsp;[#88514](https://github.com/openclaw/openclaw/pull/88514) | 0 | Local model runtime | @vincentkoc | fix(gateway): avoid default provider auth startup prewarm |
| 🔀&nbsp;[#88506](https://github.com/openclaw/openclaw/pull/88506) | 0 | Model routing/config | @kklouzal | feat: add per-agent compaction overrides |
| 📝&nbsp;[#88490](https://github.com/openclaw/openclaw/issues/88490) | 0 | Model routing/config | @edgardoalvarez100 | Session model override from Codex persists in unrelated sessions (e.g. Telegram) |
| 🔀&nbsp;[#88460](https://github.com/openclaw/openclaw/pull/88460) | 0 | Local model runtime | @Linux2010 | fix(cron): recover from local-llamacpp parameter serialization bugs |
| 📝&nbsp;[#88457](https://github.com/openclaw/openclaw/issues/88457) | 0 | Open-weight/provider behavior | @ReyesAdrian | [Bug]: opencode-go works via direct infer but fails in embedded agent runtime with session takeover |
| 🔀&nbsp;[#88400](https://github.com/openclaw/openclaw/pull/88400) | 0 | Model routing/config | @Pluviobyte | fix(config): accept overlays for bundled provider aliases |
| 🔀&nbsp;[#88329](https://github.com/openclaw/openclaw/pull/88329) | 0 | Model routing/config | @Knowcheng | fix: user-pinned model falls back to global chain on quota exhaustion |
| 🔀&nbsp;[#88263](https://github.com/openclaw/openclaw/pull/88263) | 0 | Local memory/embedding | @whiteyzy | fix(memory-core): use native recursive fs.watch in QMD watcher to prevent per-file FD leak |
| 🔀&nbsp;[#88249](https://github.com/openclaw/openclaw/pull/88249) | 0 | Model routing/config | @Darclindy | feat(desktop): add Tauri model setup app |
| 🔀&nbsp;[#88212](https://github.com/openclaw/openclaw/pull/88212) | 0 | Local model runtime | @vincentkoc | feat(agents): auto-trim lean local model tools |
| 📝&nbsp;[#88201](https://github.com/openclaw/openclaw/issues/88201) | 0 | Local model runtime | @adamdksaad-ops | [Bug]: OpenClaw 5.22: ~10 sec per-call inference overhead in infer model run (both --gateway and --local) vs ~1.3 sec direct provider call |
| 🔀&nbsp;[#88181](https://github.com/openclaw/openclaw/pull/88181) | 0 | Local model runtime | @vincentkoc | feat(agents): add strict local model lean profile |
| 🔀&nbsp;[#88108](https://github.com/openclaw/openclaw/pull/88108) | 0 | Local model runtime | @vincentkoc | fix(agents): compact lean local tool catalogs |
| 🔀&nbsp;[#88098](https://github.com/openclaw/openclaw/pull/88098) | 0 | OpenAI-compatible/proxy | @ericlevine | feat(onboard): add --custom-context-window flag for non-interactive setup |
| 🔀&nbsp;[#88082](https://github.com/openclaw/openclaw/pull/88082) | 0 | Model routing/config | @lit26 | feat(stepfun): add step-3.7-flash model |
| 📝&nbsp;[#88079](https://github.com/openclaw/openclaw/issues/88079) | 0 | Open-weight/provider behavior | @xx1170822819 | [Regression] WebChat: reasoning_content not streamed for Kimi Code & DeepSeek Reasoner — only MiniMax works |
| 🔀&nbsp;[#88078](https://github.com/openclaw/openclaw/pull/88078) | 0 | Local memory/embedding | @gisk0 | fix(active-memory): trim recall prompt envelope |
| 📝&nbsp;[#88077](https://github.com/openclaw/openclaw/issues/88077) | 0 | Local memory/embedding | @gisk0 | [Bug]: Active Memory recall context uses full OpenClaw prompt envelope |
| 📝&nbsp;[#88009](https://github.com/openclaw/openclaw/issues/88009) | 0 | Local memory/embedding | @hartmark | [Feature]: batched memory embedding should batch over files |
| 📝&nbsp;[#87996](https://github.com/openclaw/openclaw/issues/87996) | 0 | OpenAI-compatible/proxy | @liaoandi | Vertex beta INVALID_ARGUMENT can wedge long Enterprise sessions without actionable recovery |
| 🔀&nbsp;[#87958](https://github.com/openclaw/openclaw/pull/87958) | 0 | Model routing/config | @vincentkoc | fix(agents): scale read output for small contexts |
| 📝&nbsp;[#87957](https://github.com/openclaw/openclaw/issues/87957) | 0 | Model routing/config | @osolmaz | Refactor session model/auth state resolution |
| 🔀&nbsp;[#87955](https://github.com/openclaw/openclaw/pull/87955) | 0 | Local model runtime | @vincentkoc | fix(agents): keep lean tools behind catalog controls |
| 📝&nbsp;[#87943](https://github.com/openclaw/openclaw/issues/87943) | 0 | Open-weight/provider behavior | @Xel-tik | feat: Add Xiaomi MiMo Web Search provider |
| 🔀&nbsp;[#87933](https://github.com/openclaw/openclaw/pull/87933) | 0 | OpenAI-compatible/proxy | @MukundaKatta | fix(agents): respect compat.thinkingFormat override for DeepSeek V4 models |
| 🔀&nbsp;[#87927](https://github.com/openclaw/openclaw/pull/87927) | 0 | Model routing/config | @vincentkoc | fix(agents): cap compaction budgets for small contexts |
| 📝&nbsp;[#87925](https://github.com/openclaw/openclaw/issues/87925) | 0 | Model routing/config | @hoobnn | thinkingLevel: model switch silently downgrades and persists an inherited explicit override |
| 🔀&nbsp;[#87923](https://github.com/openclaw/openclaw/pull/87923) | 0 | Model routing/config | @hoobnn | fix(thinking): keep explicit session thinkingLevel when runtime downgrades (#87740) |
| 🔀&nbsp;[#87895](https://github.com/openclaw/openclaw/pull/87895) | 0 | Open-weight/provider behavior | @vincentkoc | test(agents): broaden small live hosted model matrix |
| 🔀&nbsp;[#87893](https://github.com/openclaw/openclaw/pull/87893) | 0 | Model routing/config | @osolmaz | fix(auth-profiles): repair stale auto runtime auth selection |
| 📝&nbsp;[#87881](https://github.com/openclaw/openclaw/issues/87881) | 0 | Local memory/embedding | @slideshow-dingo | Gap Analysis: v2026.5.27 config keys rejected as unknown by schema |
| 📝&nbsp;[#87876](https://github.com/openclaw/openclaw/issues/87876) | 0 | Model routing/config | @Haderach-Ram | Bug: Bedrock Converse Streaming silently aborts on long-context agent sessions (~6 min timeout, no retry, no fallback) |
| 🔀&nbsp;[#87856](https://github.com/openclaw/openclaw/pull/87856) | 0 | Local model runtime | @vincentkoc | fix(agents): count streamed model deltas incrementally |
| 🔀&nbsp;[#87850](https://github.com/openclaw/openclaw/pull/87850) | 0 | Local model runtime | @vincentkoc | fix(agents): avoid constructing lean local model tools<br>Assignee: vincentkoc |
| 📝&nbsp;[#87816](https://github.com/openclaw/openclaw/issues/87816) | 0 | Local/media model provider | @DoiiarX | feat(tts): xiaomi voicedesign/voiceclone model support |
| 📝&nbsp;[#87766](https://github.com/openclaw/openclaw/issues/87766) | 0 | Open-weight/provider behavior | @hccc1203 | [Bug] Kimi web_search always returns "ungrounded" error - Moonshot API no longer returns search_results field[Bug]: |
| 📝&nbsp;[#87763](https://github.com/openclaw/openclaw/issues/87763) | 0 | OpenAI-compatible/proxy | @georgenaz | SSRF guard pinned DNS dispatcher causes model fetch timeouts when autoSelectFamily is enabled |
| 🔀&nbsp;[#87697](https://github.com/openclaw/openclaw/pull/87697) | 0 | Model routing/config | @ferminquant | fix(auth): clear stale provider cooldowns after reauth |
| 📝&nbsp;[#87689](https://github.com/openclaw/openclaw/issues/87689) | 0 | Local memory/embedding | @Countermarch | Dreaming needs supported guard to disable session transcript ingestion during QMD migrations |
| 📝&nbsp;[#87687](https://github.com/openclaw/openclaw/issues/87687) | 0 | Local model runtime | @sonofanton44 | vllm openai-completions streaming parser drops tool_calls when reasoning_content streams first for gpt-oss-120b at large systemPrompt |
| 📝&nbsp;[#87642](https://github.com/openclaw/openclaw/issues/87642) | 0 | Local model runtime | @chrisslee | Expose subagent-control waitForRun timeout as a config knob (hardcoded 30s blocks slow local LLMs) |
| 📝&nbsp;[#87603](https://github.com/openclaw/openclaw/issues/87603) | 0 | Model routing/config | @luzhidong | lossless-claw contextThreshold does not adapt to actual model context window after fallback |
| 🔀&nbsp;[#87596](https://github.com/openclaw/openclaw/pull/87596) | 0 | Open-weight/provider behavior | @Pluviobyte | fix(moonshot): rewrite duplicate native Kimi tool_call ids on replay |
| 🔀&nbsp;[#87587](https://github.com/openclaw/openclaw/pull/87587) | 0 | Local model runtime | @vincentkoc | fix(agents): keep exec visible for lean local models |
| 📝&nbsp;[#87586](https://github.com/openclaw/openclaw/issues/87586) | 0 | Local model runtime | @taocwal | [Feature]: Unixsocket Provider plugin |
| 🔀&nbsp;[#87562](https://github.com/openclaw/openclaw/pull/87562) | 0 | Open-weight/provider behavior | @Pluviobyte | fix(openrouter): reconcile streamed cost with /generation total_cost |
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
| 📝&nbsp;[#85321](https://github.com/openclaw/openclaw/issues/85321) | 0 | Open-weight/provider behavior | @Galaxy-Chen | `wrapStreamRepairMalformedToolCallArguments` clears valid tool call arguments for Moonshot/Kimi provider |
| 📝&nbsp;[#84918](https://github.com/openclaw/openclaw/issues/84918) | 0 | OpenAI-compatible/proxy | @killo3967 | OpenWebUI image uploads reach image tool as empty image via /v1/chat/completions on 2026.5.18 |
| 📝&nbsp;[#84865](https://github.com/openclaw/openclaw/issues/84865) | 0 | Open-weight/provider behavior | @njuboy11 | user-switched model has no fallback chain, causing session deadlock on provider outage |
| 🔀&nbsp;[#84554](https://github.com/openclaw/openclaw/pull/84554) | 0 | Local memory/embedding | @jetd1 | fix(memory-core): guard builtin fallback after qmd failures |
| 📝&nbsp;[#84217](https://github.com/openclaw/openclaw/issues/84217) | 0 | Local model runtime | @fanispoulinakisai-boop | [Bug]: Heartbeat dispatch delivers free text block alongside message-tool call (chatty non-Codex providers, v2026.5.18) |
| 🔀&nbsp;[#84072](https://github.com/openclaw/openclaw/pull/84072) | 0 | Model routing/config | @wiatrM | Add model fallback circuit breaker |
| 📝&nbsp;[#84070](https://github.com/openclaw/openclaw/issues/84070) | 0 | Local model runtime | @islandpreneur007 | Active Memory embedded runner fails to expose plugin tools when hidden runner is on the DeepSeek provider path |
| 🔀&nbsp;[#83436](https://github.com/openclaw/openclaw/pull/83436) | 0 | Model routing/config | @cael-dandelion-cult | fix(agents): rethrow EmbeddedAttemptSessionTakeoverError before model fallback |
| 📝&nbsp;[#83399](https://github.com/openclaw/openclaw/issues/83399) | 0 | OpenAI-compatible/proxy | @yuzhihui886 | Bug: Tool call loop when assistant generates text + toolCall with openai-completions API |
| 🔀&nbsp;[#83213](https://github.com/openclaw/openclaw/pull/83213) | 0 | Model routing/config | @Derekko-web | fix(gateway): clear live model switch on reset |
| 🔀&nbsp;[#82557](https://github.com/openclaw/openclaw/pull/82557) | 0 | Model routing/config | @alexandre-leng | Allow onboarding to configure multiple model providers |
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
| 🔀&nbsp;[#70647](https://github.com/openclaw/openclaw/pull/70647) | 0 | Open-weight/provider behavior | @chengjiew | test(agents): pin empty-turn coverage for non-strict-agentic nemotron |
| 📝&nbsp;[#70559](https://github.com/openclaw/openclaw/issues/70559) | 0 | Local memory/embedding | @Gaia39rus | runUnsafeReindex crashes with "no such table: chunks_vec" when sqlite-vec is enabled |
| 🔀&nbsp;[#69729](https://github.com/openclaw/openclaw/pull/69729) | 0 | OpenAI-compatible/proxy | @wAnyBug-Com | fix(qwen): enable qwen3.6-plus on Coding Plan CN, correct reasoning flag |
| 🔀&nbsp;[#69495](https://github.com/openclaw/openclaw/pull/69495) | 0 | Model routing/config | @zote | feat(heartbeat): support model fallbacks via {primary,fallbacks} (#69434) |
| 🔀&nbsp;[#69245](https://github.com/openclaw/openclaw/pull/69245) | 0 | OpenAI-compatible/proxy | @g18166599417-svg | feat: enable cache-ttl context pruning for openai-completions providers |
| 🔀&nbsp;[#68975](https://github.com/openclaw/openclaw/pull/68975) | 0 | Local memory/embedding | @kami-saia | feat(memory): switch default local embedding model to bge-m3 Q8_0 AI-assisted |
| 🔀&nbsp;[#68590](https://github.com/openclaw/openclaw/pull/68590) | 0 | Local memory/embedding | @imadal1n | fix(memory-core): rewrite qmd index on managed collection repair |
| 🔀&nbsp;[#68435](https://github.com/openclaw/openclaw/pull/68435) | 0 | OpenAI-compatible/proxy | @foxer0952 | feat(gateway): accept audio/file content blocks in /v1/chat/completions |
| 📝&nbsp;[#68222](https://github.com/openclaw/openclaw/issues/68222) | 0 | Open-weight/provider behavior | @huangjk1103 | [Bug]: Kimi Code model frequent sessions_yield tool call/output interrupts long-running tasks, requires manual intervention to resume |
| 📝&nbsp;[#67379](https://github.com/openclaw/openclaw/issues/67379) | 0 | Local memory/embedding | @colakang | qmd scope denies subagent sessions - channel/chatType resolve to undefined |
| 📝&nbsp;[#65557](https://github.com/openclaw/openclaw/issues/65557) | 0 | Local model runtime | @alexanderatkins | Provider & model selection per session/account with admin-controlled allowlists |
| 🔀&nbsp;[#65547](https://github.com/openclaw/openclaw/pull/65547) | 0 | Local memory/embedding | @jochenfrey | test(memory-qmd): verify extraCollections pattern reaches qmd collection add CLI args |
| 🔀&nbsp;[#65423](https://github.com/openclaw/openclaw/pull/65423) | 0 | Model routing/config | @ryanngit | feat(agents): shuffle auth profile candidates for subagent runs |
| 🔀&nbsp;[#65180](https://github.com/openclaw/openclaw/pull/65180) | 0 | Local model runtime | @jnk0423 | fix(cli,sessions): make local model run stateless by default and keep transcript fallback profile-scoped |
| 🔀&nbsp;[#64335](https://github.com/openclaw/openclaw/pull/64335) | 0 | Open-weight/provider behavior | @serg0x | fix(zai): rotate env-backed API keys on rate limit |
| 📝&nbsp;[#64224](https://github.com/openclaw/openclaw/issues/64224) | 0 | OpenAI-compatible/proxy | @hugalafutro | Billing cooldown flags entire provider instead of individual model - breaks proxy/litellm setups |
| 📝&nbsp;[#64212](https://github.com/openclaw/openclaw/issues/64212) | 0 | Open-weight/provider behavior | @Iderty | [Bug]: Image tool fails with "Request was aborted" for NVIDIA Kimi K2.5 |
| 📝&nbsp;[#63531](https://github.com/openclaw/openclaw/issues/63531) | 0 | Local memory/embedding | @ImLukeF | [Feature]: Add MLX Talk provider MVP for local macOS TTS |
| 📝&nbsp;[#62780](https://github.com/openclaw/openclaw/issues/62780) | 0 | Local model runtime | @jeremyf327 | Feature: message:before_send hook to enable content-quality fallback gating |
| 🔀&nbsp;[#62733](https://github.com/openclaw/openclaw/pull/62733) | 0 | Local memory/embedding | @nSPIR3D | Fix local memory embedding VRAM fallback and logging file resolution |
| 🔀&nbsp;[#62710](https://github.com/openclaw/openclaw/pull/62710) | 0 | Model routing/config | @zeynalnia | fix(auth): stop new sessions inheriting auto-selected auth profile overrides |
| 📝&nbsp;[#62436](https://github.com/openclaw/openclaw/issues/62436) | 0 | OpenAI-compatible/proxy | @gucasbrg | Feature: Lightweight LLM passthrough mode for /v1/chat/completions - skip session persistence entirely |
| 📝&nbsp;[#62432](https://github.com/openclaw/openclaw/issues/62432) | 0 | Open-weight/provider behavior | @NikolaFC | [Bug]: Xiaomi/MiMo sessions can repeatedly relaunch exec after 'Command still running' instead of switching to process poll |
| 📝&nbsp;[#62109](https://github.com/openclaw/openclaw/issues/62109) | 0 | OpenAI-compatible/proxy | @nboody | Interactive runs fail with auth-style 403 when custom OpenAI-compatible provider baseUrl uses Unicode/IDN or punycode hostname, but ASCII hostname/IP works |
| 📝&nbsp;[#61716](https://github.com/openclaw/openclaw/issues/61716) | 0 | OpenAI-compatible/proxy | @Andy-Xie-1145 | [Feature]: Add model parameter prompts (context window, max_tokens, modalities) during OpenAI-compatible provider onboarding CLI flow |
| 📝&nbsp;[#58765](https://github.com/openclaw/openclaw/issues/58765) | 0 | Local memory/embedding | @losz5000 | Feature: Support output dimensionality truncation for local GGUF embedding models |
| 🔀&nbsp;[#58405](https://github.com/openclaw/openclaw/pull/58405) | 0 | OpenAI-compatible/proxy | @tonga54 | feat(openresponses): add per-request skills override to /v1/responses |
| 📝&nbsp;[#57638](https://github.com/openclaw/openclaw/issues/57638) | 0 | OpenAI-compatible/proxy | @Kyzcreig | feat: cron.defaults for model, delivery, and contextTokens |
| 📝&nbsp;[#57443](https://github.com/openclaw/openclaw/issues/57443) | 0 | OpenAI-compatible/proxy | @wujiaming88 | [Bug]: Tool JSON Schema patternProperties causes 400 errors on BytePlus Ark (doubao) - schema cleaning should be universal, not provider-specific |
| 🔀&nbsp;[#55477](https://github.com/openclaw/openclaw/pull/55477) | 0 | OpenAI-compatible/proxy | @Kyzcreig | feat: stamp session_key, message_channel, context_limit into LiteLLM request metadata |
| 📝&nbsp;[#54128](https://github.com/openclaw/openclaw/issues/54128) | 0 | Local memory/embedding | @hsuaaron | Add maxThreads config for local embedding (node-llama-cpp) |
| 📝&nbsp;[#53810](https://github.com/openclaw/openclaw/issues/53810) | 0 | OpenAI-compatible/proxy | @FiredMosquito831 | Subagent Premature Announce Bug - Model-Specific Tool Call Handling Issues |
| 📝&nbsp;[#51593](https://github.com/openclaw/openclaw/issues/51593) | 0 | Open-weight/provider behavior | @Faaab84 | [Bug]: HTTP 400: "tool call id exec:26 is duplicated" with moonshot/kimi-k2.5 in WhatsApp group chats |
| 📝&nbsp;[#44789](https://github.com/openclaw/openclaw/issues/44789) | 0 | OpenAI-compatible/proxy | @Hylance | [Bug]: openclaw 2026.03.11 partially config litellm |
| 📝&nbsp;[#43432](https://github.com/openclaw/openclaw/issues/43432) | 0 | Local memory/embedding | @omegabyte-ai | [Feature]: Memory durability config - hard flush threshold, priority-aware compaction, cache TTL |
| 📝&nbsp;[#42408](https://github.com/openclaw/openclaw/issues/42408) | 0 | Local memory/embedding | @1sexywoo8 | [Bug/Docs]: local+hybrid memory_search quality can appear unstable due to extraPaths path drift + benchmark-file contamination |

## RECENTLY CLOSED OR REMOVED FROM OPEN INVENTORY

These were in earlier local-model notes or candidate pools but are not counted as live-open retained threads now.

<details>
<summary>Recently closed or removed threads (282)</summary>

| Thread | Status checked | Note |
| --- | --- | --- |
| [#89976](https://github.com/openclaw/openclaw/issues/89976) | Closed in local gitcrawl 2026-06-04 | [Bug]: Manual /compact on Codex OAuth sessions resolves to direct openai auth instead of Codex runtime; no longer open. |
| [#89941](https://github.com/openclaw/openclaw/pull/89941) | Closed in local gitcrawl 2026-06-04 | fix(issue): resolve #89425 [Bug]: Missing extensions/speech-core/ in npm tarball (v2026; no longer open. |
| [#89845](https://github.com/openclaw/openclaw/pull/89845) | Closed in local gitcrawl 2026-06-04 | fix(fireworks): optimize caching with x-session-affinity; no longer open. |
| [#89685](https://github.com/openclaw/openclaw/pull/89685) | Closed in local gitcrawl 2026-06-04 | fix(acpx): handle Claude ACP model startup options; no longer open. |
| [#89610](https://github.com/openclaw/openclaw/pull/89610) | Closed in local gitcrawl 2026-06-03 | Add channel-scoped memory search filters; no longer open. |
| [#89560](https://github.com/openclaw/openclaw/pull/89560) | Closed in local gitcrawl 2026-06-04 | fix(telegram): isolate verbose status after streamed finals; no longer open. |
| [#89540](https://github.com/openclaw/openclaw/issues/89540) | Closed in local gitcrawl 2026-06-04 | [Bug]: Telegram /v Active Memory status can overwrite short streamed replies; no longer open. |
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
| [#89248](https://github.com/openclaw/openclaw/pull/89248) | Closed in local gitcrawl 2026-06-03 | feat(context-engine): context-capsule plugin — 99.3% token reduction with recovery-score gate; no longer open. |
| [#89244](https://github.com/openclaw/openclaw/pull/89244) | Closed in local gitcrawl 2026-06-04 | fix(memory): warn on high runtime watcher pressure; no longer open. |
| [#89208](https://github.com/openclaw/openclaw/issues/89208) | Closed in local gitcrawl 2026-06-03 | Stuck-session recovery discards queued user messages after aborting ghost run; no longer open. |
| [#89188](https://github.com/openclaw/openclaw/pull/89188) | Closed in local gitcrawl 2026-06-02 | fix(memory-core): reduce Linux watcher fan-out; no longer open. |
| [#89185](https://github.com/openclaw/openclaw/pull/89185) | Closed in local gitcrawl 2026-06-02 | fix(memory): default gateway memory watch off; no longer open. |
| [#89181](https://github.com/openclaw/openclaw/pull/89181) | Closed in local gitcrawl 2026-06-02 | fix(agents): dispatch auth failures by type; no longer open. |
| [#89165](https://github.com/openclaw/openclaw/issues/89165) | Closed in local gitcrawl 2026-06-02 | HTTP 400 quota/usage_limit errors do not trigger provider fallback chain; no longer open. |
| [#89139](https://github.com/openclaw/openclaw/issues/89139) | Closed in local gitcrawl 2026-06-04 | webchat creates new agent run per message, destroying prompt cache (93% → 29% hit rate); no longer open. |
| [#89128](https://github.com/openclaw/openclaw/pull/89128) | Closed in local gitcrawl 2026-06-03 | fix: skip Responses item id replay without store; no longer open. |
| [#89112](https://github.com/openclaw/openclaw/issues/89112) | Closed in local gitcrawl 2026-06-02 | chore: OpenAI API key update requires manual edits in multiple agent auth.json files; no longer open. |
| [#89070](https://github.com/openclaw/openclaw/pull/89070) | Closed in local gitcrawl 2026-06-04 | fix(stream): handle cumulative JSON chunks from local llama.cpp tool calls; no longer open. |
| [#89049](https://github.com/openclaw/openclaw/pull/89049) | Closed in local gitcrawl 2026-06-03 | fix(idle-timeout): honor provider timeout for no-timeout runs; no longer open. |
| [#89032](https://github.com/openclaw/openclaw/issues/89032) | Closed in local gitcrawl 2026-06-02 | MiMo v2.5: reasoning_content not preserved for custom xiaomi-coding provider (400 in multi-turn tool calls); no longer open. |
| [#89008](https://github.com/openclaw/openclaw/issues/89008) | Closed in local gitcrawl 2026-06-03 | claude-cli thinking-only (end_turn, empty text) turns trigger empty_response model-fallback re-run on a different model; no longer open. |
| [#88976](https://github.com/openclaw/openclaw/pull/88976) | Closed in local gitcrawl 2026-06-03 | fix(mistral): enable prompt cache key compat; no longer open. |
| [#88946](https://github.com/openclaw/openclaw/pull/88946) | Closed in local gitcrawl 2026-06-03 | Fix live model inference edge cases; no longer open. |
| [#88938](https://github.com/openclaw/openclaw/issues/88938) | Closed in local gitcrawl 2026-06-02 | [Feature]: know what model is used by the image tool; no longer open. |
| [#88928](https://github.com/openclaw/openclaw/pull/88928) | Closed in local gitcrawl 2026-06-02 | fix(llm): preserve Windows path control escapes; no longer open. |
| [#88926](https://github.com/openclaw/openclaw/pull/88926) | Closed in local gitcrawl 2026-06-03 | fix(llm): preserve Windows path escapes in streamed args; no longer open. |
| [#88924](https://github.com/openclaw/openclaw/pull/88924) | Closed in local gitcrawl 2026-06-02 | fix(agents): strip streamed reasoning tags; no longer open. |
| [#88922](https://github.com/openclaw/openclaw/pull/88922) | Closed in local gitcrawl 2026-06-03 | fix(google): forward stop sequences to Gemini generationConfig; no longer open. |
| [#88918](https://github.com/openclaw/openclaw/issues/88918) | Closed in local gitcrawl 2026-06-03 | [Bug]: Streaming repairJson injects control chars into unescaped Windows paths in tool-call arguments; no longer open. |
| [#88896](https://github.com/openclaw/openclaw/pull/88896) | Closed in local gitcrawl 2026-06-02 | fix: harden CLI and plugin edge cases; no longer open. |
| [#88874](https://github.com/openclaw/openclaw/issues/88874) | Closed in local gitcrawl 2026-06-02 | [Bug]: cron openai/gpt-5.4-mini ignores agentRuntime=openclaw/pi and routes to openai-codex with zero tools; no longer open. |
| [#88873](https://github.com/openclaw/openclaw/pull/88873) | Closed in local gitcrawl 2026-06-02 | fix(agent-os): harden full-local substrate; no longer open. |
| [#88861](https://github.com/openclaw/openclaw/pull/88861) | Closed in local gitcrawl 2026-06-02 | Fix OpenResponses callback message context; no longer open. |
| [#88851](https://github.com/openclaw/openclaw/pull/88851) | Closed in local gitcrawl 2026-06-02 | Persist OpenRouter model cache in SQLite; no longer open. |
| [#88833](https://github.com/openclaw/openclaw/issues/88833) | Closed in local gitcrawl 2026-06-03 | Bug: azure-openai-responses can return non_deliverable_terminal_turn with assistantTexts=[] even when direct Azure /responses succeeds; no longer open. |
| [#88830](https://github.com/openclaw/openclaw/pull/88830) | Closed in local gitcrawl 2026-06-02 | feat(dreaming): score candidates with shadow trial results; no longer open. |
| [#88827](https://github.com/openclaw/openclaw/pull/88827) | Closed in local gitcrawl 2026-06-02 | Add Vertex API key model config regression coverage; no longer open. |
| [#88816](https://github.com/openclaw/openclaw/issues/88816) | Closed in local gitcrawl 2026-06-02 | [Bug]: v2026.05.28 breaks Google Vertex Express API Key; no longer open. |
| [#88806](https://github.com/openclaw/openclaw/pull/88806) | Closed in local gitcrawl 2026-06-02 | fix(memory-lancedb): reject envelope metadata sludge (incl. marker-free shapes); no longer open. |
| [#88804](https://github.com/openclaw/openclaw/pull/88804) | Closed in local gitcrawl 2026-06-02 | fix(openai): keep stop-finished tool calls; no longer open. |
| [#88799](https://github.com/openclaw/openclaw/pull/88799) | Closed in local gitcrawl 2026-06-02 | fix(openai): honor streamed tool calls with stop finish; no longer open. |
| [#88791](https://github.com/openclaw/openclaw/issues/88791) | Closed in local gitcrawl 2026-06-02 | Bug: structured tool_calls with finish_reason stop are dropped as non_deliverable_terminal_turn; no longer open. |
| [#88787](https://github.com/openclaw/openclaw/pull/88787) | Closed in local gitcrawl 2026-06-02 | feat(openai): support gpt-5.5 azure routing and reasoning, restrict telegram bot access; no longer open. |
| [#88781](https://github.com/openclaw/openclaw/pull/88781) | Closed in local gitcrawl 2026-06-01 | fix(models): strip remaining provider self prefixes; no longer open. |
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
| [#88704](https://github.com/openclaw/openclaw/pull/88704) | Closed in local gitcrawl 2026-06-02 | fix(memory): rehydrate daily list promotions; no longer open. |
| [#88693](https://github.com/openclaw/openclaw/pull/88693) | Closed in local gitcrawl 2026-06-01 | docs(openai): clarify openai-codex auth profile mismatch; no longer open. |
| [#88672](https://github.com/openclaw/openclaw/pull/88672) | Closed in local gitcrawl 2026-06-01 | fix(plugins): reuse current metadata snapshot in provider hot paths; no longer open. |
| [#88671](https://github.com/openclaw/openclaw/issues/88671) | Closed in local gitcrawl 2026-06-02 | [Bug]: [assistant reasoning omitted] appears with reasoningDefault off on Ollama models; no longer open. |
| [#88669](https://github.com/openclaw/openclaw/pull/88669) | Closed in local gitcrawl 2026-06-01 | fix(auth): skip no-op auth-profile disk writes on success; no longer open. |
| [#88667](https://github.com/openclaw/openclaw/pull/88667) | Closed in local gitcrawl 2026-06-01 | fix #81214: OpenClaw 2026.5.7 subagent regression; no longer open. |
| [#88654](https://github.com/openclaw/openclaw/issues/88654) | Closed in local gitcrawl 2026-06-01 | markAuthProfileSuccess rewrites auth-profiles.json on every success; no longer open. |
| [#88644](https://github.com/openclaw/openclaw/issues/88644) | Closed in local gitcrawl 2026-06-01 | doctor --fix breaks Codex model routing by rewriting openai-codex/ to openai/; no longer open. |
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
| [#87963](https://github.com/openclaw/openclaw/pull/87963) | Closed in local gitcrawl 2026-05-31 | fix(agents): downgrade thinking blocks with empty signatures to text before anthropic-messages replay; no longer open. |
| [#87940](https://github.com/openclaw/openclaw/pull/87940) | Closed in local gitcrawl 2026-06-04 | fix(gateway): keep dense stream updates incremental; no longer open. |
| [#87935](https://github.com/openclaw/openclaw/issues/87935) | Closed in local gitcrawl 2026-05-31 | feat: Add Xiaomi MiMo Web Search provider; no longer open. |
| [#87920](https://github.com/openclaw/openclaw/pull/87920) | Closed in local gitcrawl 2026-05-31 | feat(gateway): forward OpenAI stop sequences through chat completions; no longer open. |
| [#87907](https://github.com/openclaw/openclaw/pull/87907) | Closed in local gitcrawl 2026-06-03 | fix(memory): validate memory index identity; no longer open. |
| [#87877](https://github.com/openclaw/openclaw/issues/87877) | Closed in local gitcrawl 2026-05-31 | Codex runtime persists openai-codex as session modelProvider, causing recurring legacy route doctor warning; no longer open. |
| [#87874](https://github.com/openclaw/openclaw/pull/87874) | Closed in local gitcrawl 2026-06-02 | fix(macos): inherit thinking for voice wake forwarding; no longer open. |
| [#87862](https://github.com/openclaw/openclaw/pull/87862) | Closed in local gitcrawl 2026-05-31 | Add Claude Opus 4.8 defaults; no longer open. |
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
| [#87762](https://github.com/openclaw/openclaw/pull/87762) | Closed in local gitcrawl 2026-05-31 | feat(opencode): support separate Zen and Go API key env vars; no longer open. |
| [#87746](https://github.com/openclaw/openclaw/issues/87746) | Closed in local gitcrawl 2026-06-03 | Add Claude Opus 4.8 (`claude-opus-4-8`) to the model catalog; no longer open. |
| [#87740](https://github.com/openclaw/openclaw/issues/87740) | Closed in local gitcrawl 2026-06-03 | Bug: Explicit thinkingLevel session override permanently reset to 'off' after each agent turn; no longer open. |
| [#87737](https://github.com/openclaw/openclaw/issues/87737) | Closed in local gitcrawl 2026-06-02 | DeepSeek V4 thinking wrapper ignores thinkingFormat compat override, breaks Azure Foundry deployments; no longer open. |
| [#87719](https://github.com/openclaw/openclaw/pull/87719) | Closed in local gitcrawl 2026-05-29 | fix(anthropic): stop migrating current claude-haiku-4-5 to sonnet; no longer open. |
| [#87675](https://github.com/openclaw/openclaw/pull/87675) | Closed in local gitcrawl 2026-05-29 | fix(ollama): promote plain text tool calls; no longer open. |
| [#87641](https://github.com/openclaw/openclaw/issues/87641) | Closed in local gitcrawl 2026-05-31 | `opencode-go/kimi-k2.6`: every multi-turn task rejected with opaque 400 "Provider returned error" (reason=format), rotates to fallback (2026.5.26+5.27); no longer open. |
| [#87638](https://github.com/openclaw/openclaw/pull/87638) | Closed in local gitcrawl 2026-05-29 | test(agents): add small model live profile; no longer open. |
| [#87628](https://github.com/openclaw/openclaw/pull/87628) | Closed in local gitcrawl 2026-06-03 | feat(agents): inherit requester model for subagents; no longer open. |
| [#87621](https://github.com/openclaw/openclaw/pull/87621) | Closed in local gitcrawl 2026-05-29 | fix(ollama): yield during dense ndjson bursts; no longer open. |
| [#87616](https://github.com/openclaw/openclaw/issues/87616) | Closed in local gitcrawl 2026-06-02 | [Bug]: GatewayClientRequestError: FailoverError: LLM request timed out.; no longer open. |
| [#87608](https://github.com/openclaw/openclaw/issues/87608) | Closed in local gitcrawl 2026-05-31 | [Bug] Ollama Cloud rate-limit cooldown permanently blocks agents — not released after API recovery; no longer open. |
| [#87606](https://github.com/openclaw/openclaw/pull/87606) | Closed in local gitcrawl 2026-05-29 | fix(active-memory): raise recall timeout ceiling; no longer open. |
| [#87594](https://github.com/openclaw/openclaw/pull/87594) | Closed in local gitcrawl 2026-05-29 | fix(openrouter): apply strict9 tool_call_id sanitisation for Mistral routes; no longer open. |
| [#87593](https://github.com/openclaw/openclaw/pull/87593) | Closed in local gitcrawl 2026-05-29 | fix(agents): preserve reasoning_content replay across DeepSeek tier suffixes; no longer open. |
| [#87575](https://github.com/openclaw/openclaw/issues/87575) | Closed in local gitcrawl 2026-05-29 | Bug: DeepSeek V4 Flash Free via OpenCode Zen provider fails with 400 on follow-up API calls; no longer open. |
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
| [#83709](https://github.com/openclaw/openclaw/issues/83709) | Closed in local gitcrawl 2026-06-03 | [Feature]: Add `supportsPromptCacheKey` to Mistral transport compat patch; no longer open. |
| [#83461](https://github.com/openclaw/openclaw/issues/83461) | Not resolvable as live issue | Earlier notes referenced it, but live GitHub issue view did not resolve it as an open issue. |
| [#83333](https://github.com/openclaw/openclaw/issues/83333) | Closed in local gitcrawl 2026-06-03 | [Bug]: Memory provider cutover to Ollama leaves production index in mixed OpenAI/Ollama vector state after live sync/reload; no longer open. |
| [#83107](https://github.com/openclaw/openclaw/issues/83107) | Closed in local gitcrawl 2026-05-31 | Model registry name matching is load-bearing — silent fallback to picker selection on registry miss (2026.5.12); no longer open. |
| [#82973](https://github.com/openclaw/openclaw/pull/82973) | Closed in local gitcrawl 2026-05-28 | fix(agents): honor explicit cacheRetention for openai-completions providers; no longer open. |
| [#82887](https://github.com/openclaw/openclaw/pull/82887) | Closed in local gitcrawl 2026-05-31 | fix(cron): preflight model fallbacks before skip; no longer open. |
| [#81530](https://github.com/openclaw/openclaw/issues/81530) | Closed in local gitcrawl 2026-06-03 | [Bug]: [5.12-beta.8] Telegram Supergroup Forum Topics — Inbound Messages Not Processed; no longer open. |
| [#81281](https://github.com/openclaw/openclaw/issues/81281) | Closed in local gitcrawl 2026-05-28 | [Bug]: OpenAI-completions prompt_cache_key regression — caching worked in 2026.3.x, broken in 2026.5.x; no longer open. |
| [#81249](https://github.com/openclaw/openclaw/issues/81249) | Closed 2026-05-24 | No longer counted as live-open. |
| [#81214](https://github.com/openclaw/openclaw/issues/81214) | Closed in local gitcrawl 2026-06-01 | [Bug]: OpenClaw 2026.5.7 subagent regression; no longer open. |
| [#81170](https://github.com/openclaw/openclaw/pull/81170) | Closed in local gitcrawl 2026-06-01 | fix(openai): preserve custom provider id through memory embedding adapter; no longer open. |
| [#80495](https://github.com/openclaw/openclaw/issues/80495) | Closed in local gitcrawl 2026-05-31 | [Bug]: LM Studio Provider Fails: Environment Variable Expansion + API Endpoint Mismatch; no longer open. |
| [#80476](https://github.com/openclaw/openclaw/issues/80476) | Closed in local gitcrawl 2026-05-28 | [Feature]: bundled openai-compatible embedding provider for self-hosted servers (llama.cpp, Ollama, vLLM, TGI, LocalAI); no longer open. |
| [#80379](https://github.com/openclaw/openclaw/issues/80379) | Closed in local gitcrawl 2026-05-28 | [Bug]: Tool result secret redaction mutates session history, breaking KV cache prefix matching for local LLM providers; no longer open. |
| [#80226](https://github.com/openclaw/openclaw/issues/80226) | Closed 2026-05-25 | No longer counted as live-open. |
| [#79380](https://github.com/openclaw/openclaw/issues/79380) | Closed in local gitcrawl 2026-06-01 | [Bug]: Gateway CPU spin / crash loop on Raspberry Pi 4 (ARM64) — regression from 4.23 to 4.25+; no longer open. |
| [#79329](https://github.com/openclaw/openclaw/issues/79329) | Closed in local gitcrawl 2026-05-31 | Cron model preflight skips entire run when local primary is unreachable, ignoring configured cloud fallbacks [AI]; no longer open. |
| [#77792](https://github.com/openclaw/openclaw/issues/77792) | Closed in local gitcrawl 2026-06-01 | fix(tts/xiaomi): support per-call voice and model overrides; no longer open. |
| [#77678](https://github.com/openclaw/openclaw/pull/77678) | Closed in local gitcrawl 2026-05-28 | fix(memory): don't report QMD embeddings as unavailable when searchMode=search; no longer open. |
| [#77655](https://github.com/openclaw/openclaw/issues/77655) | Closed in local gitcrawl 2026-05-31 | Model fallback chain interrupted by race condition — 6 fallback models configured but task terminates before all are tried; no longer open. |
| [#77336](https://github.com/openclaw/openclaw/issues/77336) | Closed in local gitcrawl 2026-06-02 | [Feature Request]: Built-in handling of strict role alternation for Mistral / SGLang backends; no longer open. |
| [#76741](https://github.com/openclaw/openclaw/pull/76741) | Closed in local gitcrawl 2026-06-03 | fix(kimi): strip anthropic cache markers; no longer open. |
| [#76654](https://github.com/openclaw/openclaw/issues/76654) | Closed in local gitcrawl 2026-05-31 | [webchat] Agent responses disappear after heartbeat tool calls (model-specific, MiMo V2 Pro); no longer open. |
| [#76612](https://github.com/openclaw/openclaw/issues/76612) | Closed in local gitcrawl 2026-06-03 | Kimi Code returns empty content when Anthropic cache_control markers are sent; no longer open. |
| [#75720](https://github.com/openclaw/openclaw/issues/75720) | Closed in local gitcrawl 2026-05-28 | [Bug]: Auto-onboard / plugin presets unconditionally overwrite user-set agents.defaults.model.primary; no longer open. |
| [#75657](https://github.com/openclaw/openclaw/issues/75657) | Closed in local gitcrawl 2026-05-29 | fix: local GGUF embedding model warmup blocks Node.js event loop for minutes on startup; no longer open. |
| [#74644](https://github.com/openclaw/openclaw/issues/74644) | Closed in local gitcrawl 2026-05-31 | mediaUnderstandingProviders audio path hard-requires API key, breaking no-auth/local STT providers; no longer open. |
| [#74315](https://github.com/openclaw/openclaw/pull/74315) | Closed in local gitcrawl 2026-05-31 | fix(agents): remove kimi-coding from normalizeProviderId alias chain; no longer open. |
| [#74310](https://github.com/openclaw/openclaw/issues/74310) | Closed in local gitcrawl 2026-06-03 | Bug Report: `normalizeProviderId` breaks provider-namespaced models like `kimi-coding/k2p5`; no longer open. |
| [#72927](https://github.com/openclaw/openclaw/issues/72927) | Closed in local gitcrawl 2026-06-01 | feat(tts): support MiMo v2.5 TTS VoiceDesign; no longer open. |
| [#71784](https://github.com/openclaw/openclaw/issues/71784) | Closed in local gitcrawl 2026-06-01 | Bug: memory search live embedding fails ~20–40% with `fetch failed \| other side closed` (provider-agnostic; upstream healthy); no longer open. |
| [#68812](https://github.com/openclaw/openclaw/issues/68812) | Closed in local gitcrawl 2026-06-01 | Make memory embedding retry/concurrency parameters configurable; no longer open. |
| [#67423](https://github.com/openclaw/openclaw/issues/67423) | Closed in local gitcrawl 2026-06-01 | [Bug] Auth router ignores provider entry's apiKey field, resolves via auth.order by canonical provider ID — wrong key for split provider entries; no longer open. |
| [#67035](https://github.com/openclaw/openclaw/issues/67035) | Closed in local gitcrawl 2026-06-04 | [Bug]: 2026.4.14 Windows chat UI regression: input text swallowed, streamed replies often invisible until refresh, typing indicator flashes then blanks; no longer open. |
| [#66339](https://github.com/openclaw/openclaw/issues/66339) | Closed in local gitcrawl 2026-06-01 | memory search can hit QMD SQLite lock contention during normal runtime; no longer open. |
| [#65914](https://github.com/openclaw/openclaw/pull/65914) | Closed in local gitcrawl 2026-06-01 | fix(memory): respect qmd status timeout and skip checkpoint exports; no longer open. |
| [#65502](https://github.com/openclaw/openclaw/issues/65502) | Closed in local gitcrawl 2026-05-31 | feat(agents): resilient model fallback with retry + context-aware safe mode; no longer open. |
| [#63685](https://github.com/openclaw/openclaw/issues/63685) | Closed in local gitcrawl 2026-06-03 | [Bug]: Cannot run gemma 4 models from google ai studio; no longer open. |
| [#60078](https://github.com/openclaw/openclaw/issues/60078) | Closed in local gitcrawl 2026-06-03 | [Bug]: Announce delivery ignores modelByChannel, always uses agent default model; no longer open. |
| [#59208](https://github.com/openclaw/openclaw/pull/59208) | Closed in local gitcrawl 2026-06-02 | fix(status): honor selected usage auth profile; no longer open. |
| [#58012](https://github.com/openclaw/openclaw/issues/58012) | Closed in local gitcrawl 2026-05-29 | strict9 tool-call-id regression for Mistral via proxy providers; no longer open. |
| [#48680](https://github.com/openclaw/openclaw/issues/48680) | Closed in local gitcrawl 2026-05-31 | [Bug] Model fallback treats HTTP 403 business rejection as 'candidate_succeeded', skipping remaining fallback models; no longer open. |
| [#47884](https://github.com/openclaw/openclaw/issues/47884) | Closed in local gitcrawl 2026-06-01 | [Bug]: memory_search tool fails with "fetch failed" despite embedding provider configured; no longer open. |
| [#44870](https://github.com/openclaw/openclaw/issues/44870) | Closed in local gitcrawl 2026-06-03 | [Bug]: I have been unable to verify using the codex from the transfer station; no longer open. |
| [#32496](https://github.com/openclaw/openclaw/issues/32496) | Closed in local gitcrawl 2026-06-01 | [Feature]:  Support frequency_penalty and presence_penalty Parameters for OpenAI-Compatible Providers; no longer open. |

</details>

## REGENERATION NOTES

Do not regenerate this file by dumping keyword hits. The correct workflow is:

1. Verify Gitcrawl freshness and fetch live GitHub open issue/PR state.
2. Build a broad candidate pool from local/open-weight/provider terms.
3. Review every candidate for whether the actual problem or PR change is materially about local/open-weight/model-provider behavior.
4. Keep direct/material matches, drop incidental body mentions, and preserve closed/removed notable items in the collapsed details block above.
5. Recount rows and compare against the retained issue/PR number sets before committing.
6. Run `python3 scripts/sort_openclaw_onur_inventory.py`, then `python3 scripts/export_inventory_json.py` and `python3 scripts/validate_inventory_json.py`, before committing so the Markdown table and JSON mirror stay in sync. The merged open thread table has `Thread`, `Activity`, `Area`, `Creator`, and `Title` columns, fills creator handles from Gitcrawl, and sorts by `Activity` score descending, then GitHub number descending/latest. Closed or removed rows stay newest-first by GitHub number.
7. Do not add cumulative source logs, audit-result prose, inclusion-criteria repeats, or generated highest-risk sections to this file. Keep operational notes in commit messages, PRs, or chat, not in the inventory.
- Kept open threads: 632 (302 issues, 330 PRs).
