# OpenClaw Local Runtime Stall Repro Findings

Started: 2026-05-28

Workspace:

- Source checkout: `/Users/onur/oc/openclaw-worktrees/local-runtime-stalls`
- Scratch report: `/Users/onur/scratch/openclaw-local-runtime-stall-repro-findings.md`
- Base commit for first source/test pass: `d84cbfa50ea53a73a6b4626dca1c4c1e57db4e31`
- Current live-repro commit: `d1577a2ff2830bb151cb820af5ebbb9323ef685e`

Scope:

Try to reproduce, sequentially, the local-runtime stalls/gateway-blocking issue and PR set from the scratch inventory. Use a local worktree or Crabbox/Testbox/targeted remote proof as appropriate. Record findings even when a real repro is blocked by missing external hardware, credentials, or services.

Status legend:

- `pending`: not started.
- `in-progress`: currently under investigation.
- `reproduced`: behavior reproduced directly.
- `source-confirmed`: source/tests confirm the implicated path but direct environment is unavailable.
- `not-reproduced`: attempted and did not reproduce.
- `blocked`: requires external state not available in this run.

## Queue

1. [#86599](https://github.com/openclaw/openclaw/issues/86599) (issue): Local model provider calls can block the gateway event loop on Windows beta, making even trivial inference take several minutes.
2. [#85826](https://github.com/openclaw/openclaw/issues/85826) (issue): The hard-coded 120s agent stall detector kills legitimate long-running local vLLM calls.
3. [#84569](https://github.com/openclaw/openclaw/issues/84569) (issue): Long vLLM-backed WhatsApp model calls can stall a session and end with `payloads=0`, so the user never receives a reply.
4. [#75657](https://github.com/openclaw/openclaw/issues/75657) (issue): Local GGUF embedding warmup via `node-llama-cpp` can block the Node event loop for minutes during gateway startup.
5. [#72015](https://github.com/openclaw/openclaw/issues/72015) (issue): Active Memory and QMD boot initialization can block reply paths and overload multi-agent gateways.
6. [#63229](https://github.com/openclaw/openclaw/issues/63229) (issue): Healthy local vLLM endpoints can be falsely marked timed out or overloaded, causing 1-23 minute fallback cascades.
7. [#54155](https://github.com/openclaw/openclaw/issues/54155) (issue): Gateway memory can grow massively over days with session accumulation, eventually reaching OOM-level RSS.
8. [#86065](https://github.com/openclaw/openclaw/issues/86065) (issue): Active Memory's internal 120s timeout cap is too low for slower local vLLM recall models.
9. [#86048](https://github.com/openclaw/openclaw/issues/86048) (issue): A WSL2 GPU-PV/llama-server D-state lockup can stall local inference and force a full WSL restart.
10. [#73801](https://github.com/openclaw/openclaw/issues/73801) (issue): Active Memory with `cerebras/gpt-oss-120b` can time out and leave the gateway CPU-bound.
11. [#86633](https://github.com/openclaw/openclaw/pull/86633) (PR): Adds cooperative yielding to dense Ollama stream processing so native streams do not monopolize the event loop.
12. [#85788](https://github.com/openclaw/openclaw/pull/85788) (PR): Fixes a `spawnedByCache` lifecycle leak that contributes to long-running gateway memory growth.
13. [#78435](https://github.com/openclaw/openclaw/issues/78435) (issue): Slack `start-account` can block the event loop while a model call is in flight, but the issue is channel-startup centered rather than local-model centered.
14. [#77443](https://github.com/openclaw/openclaw/issues/77443) (issue): WhatsApp on Windows can block the event loop after the first inbound message, but the evidence points to channel/Baileys behavior rather than a local/open-weight model path.

## Findings

## Live Repro Addendum - 2026-05-28

Current repro worktree: `d1577a2ff2830bb151cb820af5ebbb9323ef685e` (`fix(perf): reject invalid startup bench counts`).

### #86599 (issue) - Live Ollama gateway pass on current main

Summary: This issue is about local Ollama/native model streaming blocking the gateway event loop on Windows.
Live repro result: a real local Ollama run through OpenClaw on this Mac stayed responsive, so the reported Windows/heavier-model stall was not reproduced here.

- Status: live-tested on macOS with real local Ollama; reported Windows severity not reproduced in this available environment.
- Environment:
  - macOS local worktree, Node `v24.16.0`, pnpm `11.2.2`, OpenClaw `2026.5.28 (d1577a2)`.
  - Isolated OpenClaw profile: `live-repro-86599`, config under `~/.openclaw-live-repro-86599`.
  - Gateway port `19099`, auth disabled for loopback-only repro, Ollama provider enabled, default model `ollama/smollm2:135m`.
  - Ollama client `0.24.0`, local model `smollm2:135m` present.
- Live direct-backend baseline:
  - Command: `/usr/bin/time -p ollama run smollm2:135m "hi"`.
  - Result: `real 0.26s`; response was a short greeting.
  - Command: `/usr/bin/time -p ollama run smollm2:135m "Write a 1000 word story about calendar math. Keep going until complete."`.
  - Result: `real 1.47s`; output file size `2737` bytes.
- Live OpenClaw local transport:
  - Command: `/usr/bin/time -p env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-86599 infer model run --local --model ollama/smollm2:135m --prompt "hi" --json`.
  - Result: `real 2.94s`; output succeeded through provider `ollama`, model `smollm2:135m`.
- Live OpenClaw gateway transport:
  - Gateway startup command: `env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-86599 gateway run --force`.
  - Startup result: gateway ready in `0.7s`; provider auth prewarm completed in `455ms` with `eventLoopMax=45.4ms`.
  - Command: `/usr/bin/time -p env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-86599 infer model run --gateway --model ollama/smollm2:135m --prompt "hi" --json`.
  - Result: `real 3.07s`; output succeeded through gateway transport.
  - Longer live command: `/usr/bin/time -p env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-86599 infer model run --gateway --model ollama/smollm2:135m --prompt "Write a 1000 word story about calendar math. Keep going until complete." --json`.
  - Result: `real 5.08s`; output succeeded through gateway transport.
- Concurrent live gateway health probes during the longer model call:
  - Probe command loop: `pnpm openclaw --profile live-repro-86599 health` repeated while the gateway model call was active.
  - Probe results: each CLI health invocation took about `2.18s` to `2.62s` end-to-end, but the gateway-reported event loop remained `ok`.
  - Reported gateway loop samples included `max=156ms p99=21ms util=0.021 cpu=0.036`, `max=68ms p99=66ms util=0.214 cpu=0.273`, and later steady samples around `max=39-70ms p99=21-44ms util=0.033-0.06`.
  - No liveness warnings appeared in the gateway log during this pass.
- Finding: this is a real local Ollama/OpenClaw gateway run and it does **not** reproduce the Windows beta symptom or multi-minute stall on current main with the available small model. It does show OpenClaw overhead versus direct Ollama (`0.26s` direct vs `2.94s` local transport vs `3.07s` gateway for `hi`), but gateway timers stayed responsive under the longer stream. A faithful #86599 reproduction still requires the reported Windows environment and larger/faster local model path such as `qwen3.5:9b` or llama.cpp/OpenAI-compatible local routing.

### #85826 (issue) - Live vLLM host attempts

Summary: This issue is about long silent local vLLM calls being treated as stalled and possibly aborted.
Live repro result: no real vLLM server or usable GPU remote was available, so the live repro is blocked rather than proven or disproven.

- Status: live vLLM reproduction not yet possible with the currently available infrastructure.
- Required live shape: OpenClaw gateway connected to a real vLLM-compatible local/self-hosted model call that stays silent beyond the diagnostics thresholds, ideally matching the reporter's ARM64/DGX Spark + Qwen3.6-27B-FP8 setup or at least a real GPU vLLM server.
- Local environment check:
  - `vllm` is not installed locally.
  - Docker CLI is present, but Docker/OrbStack is not running: `failed to connect to the docker API at unix:///Users/onur/.orbstack/run/docker.sock`.
  - Local Ollama is available, but using Ollama as a fake stand-in would not be a faithful vLLM live repro for this issue.
- Crabbox/Testbox environment attempts:
  - RunPod GPU attempt: `node scripts/crabbox-wrapper.mjs run --provider runpod --target linux --ttl 60m --idle-timeout 30m --no-sync --preflight --timing-json --shell -- "nvidia-smi && python3 --version"`.
  - Result: failed before allocation with `provider=runpod requires RUNPOD_API_KEY`.
  - AWS Crabbox attempt: `node scripts/crabbox-wrapper.mjs run --provider aws --target linux --ttl 90m --idle-timeout 30m --no-sync --preflight --timing-json --shell -- "python3 --version && uname -a"`.
  - Result: failed before allocation with `RulesPerSecurityGroupLimitExceeded: The maximum number of rules per security group has been reached`.
- Finding: I have not done the requested live vLLM repro for #85826 yet. The next faithful path needs either RunPod credentials, an AWS Crabbox security-group cleanup/fix, a running local Docker/OrbStack environment that can host vLLM, or a static GPU/Windows/WSL target. Until one of those exists, any local slow HTTP server or Ollama substitution would be a shortcut rather than live proof for this item.

### #84569 (issue) - Live WhatsApp + vLLM environment check

Summary: This issue is about long vLLM-backed WhatsApp turns ending without a delivered reply.
Live repro result: the faithful WhatsApp plus vLLM case is blocked because there is no isolated linked WhatsApp account and no real vLLM endpoint.

- Status: live reproduction not yet possible with the currently available isolated environment.
- Required live shape: a real linked WhatsApp account receiving inbound messages while OpenClaw is connected to a real long-running vLLM model call, with a second inbound message queued behind the active turn.
- Live issue state checked: open P1 issue with `clawsweeper:source-repro`, `clawsweeper:linked-pr-open`, `impact:message-loss`, and `impact:session-state`.
- Local environment check:
  - Created/checked isolated profile `live-repro-84569`; it has no linked WhatsApp account.
  - Command: `pnpm openclaw --profile live-repro-84569 channels status`.
  - Result: gateway not running for the fresh isolated profile; config-only status showed local mode and no live channel connection.
  - Existing user OpenClaw state exists under `~/.openclaw`, but I did not inspect or use production WhatsApp credentials because using a real personal/channel account would send or receive live messages and is not safe without an explicitly isolated test account.
  - The vLLM host blocker from #85826 also applies here: no local vLLM, Docker unavailable, RunPod blocked by missing `RUNPOD_API_KEY`, and AWS Crabbox allocation blocked by security-group rule limit.
- Finding: I have not done the requested live WhatsApp/vLLM repro for #84569. A faithful repro needs an isolated linked WhatsApp test account plus a real long-running vLLM endpoint; using a mocked WhatsApp monitor or fake slow provider would be a shortcut and would not satisfy the requested live proof.

### #75657 (issue) - Live local GGUF embedding attempt on current main

Summary: This issue is about local GGUF embedding warmup blocking gateway startup for minutes.
Live repro result: current main reaches a worker-process boundary before native GGUF loading, but the actual model load could not run because `node-llama-cpp` is not installed.

- Status: live-tested up to the optional native runtime boundary; actual GGUF load not completed because `node-llama-cpp` is not installed in this checkout.
- Current source shape:
  - `packages/memory-host-sdk/src/host/embeddings.ts` now makes `createLocalEmbeddingProvider()` delegate to `createLocalEmbeddingWorkerProvider()`.
  - `packages/memory-host-sdk/src/host/embeddings-worker.ts` forks `embeddings-worker-child` and communicates over IPC.
  - `packages/memory-host-sdk/src/host/embeddings-worker-child.ts` is the only path that calls `createLocalEmbeddingProviderInProcess()`, so current main has a process boundary before native GGUF load.
- Live command:
  - Command: `node --import tsx -` with a script importing `createLocalEmbeddingProvider` from `packages/memory-host-sdk/src/host/embeddings.ts`, then calling `provider.embedQuery("ping")` while a 100ms parent-process interval measured max timer delay.
  - Model target: default `hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf`.
- Live result:
  - The provider attempted the worker path and failed from the worker with `ERR_MODULE_NOT_FOUND: Cannot find package 'node-llama-cpp' imported from packages/memory-host-sdk/src/host/node-llama.ts`.
  - `pnpm why node-llama-cpp` and `pnpm list node-llama-cpp --depth 10` returned no installed package.
  - Docs say source checkouts still require native build approval and rebuild for this runtime: `pnpm approve-builds` then `pnpm rebuild node-llama-cpp`.
- Finding: current main no longer appears to put the local GGUF embedding provider on the gateway main thread by default; the live attempt reached the child-process worker boundary before failing on the missing optional native dependency. A faithful live #75657 timing repro still needs `node-llama-cpp` installed/rebuilt plus the GGUF model, ideally on ARM64/Pi-class hardware. Installing that optional native dependency into this repo without explicit dependency-surface approval would be a shortcut and would dirty the checkout.

### #72015 (issue) - Live Active Memory/QMD gateway canary on current main

Summary: This issue is about Active Memory and QMD work blocking reply paths and overloading gateways.
Live repro result: Active Memory still ran in the reply path with a real local Ollama model, but this local canary showed only a short delay and not the reported multi-minute overload.

- Status: live-tested the Active Memory reply hook on macOS/current main with a real local Ollama model; tested QMD startup wiring up to the missing local `qmd` binary boundary.
- Environment:
  - macOS local worktree, Node `v24.16.0`, pnpm `11.2.2`, OpenClaw `2026.5.28 (d1577a2)`.
  - Isolated Active Memory profile: `live-repro-72015`, gateway port `19120`, auth disabled for loopback-only repro, `memory-core` and `active-memory` enabled.
  - Pulled local Ollama model `qwen2.5:0.5b`; `ollama show qwen2.5:0.5b` reports context length `32768` and capabilities `completion` + `tools`.
  - Active Memory config used `model: "ollama/qwen2.5:0.5b"`, `agents: ["main"]`, `allowedChatTypes: ["direct"]`, `queryMode: "recent"`, `timeoutMs: 15000`, and `logging: true`.
- Control attempt with the only pre-existing local model:
  - Initial profile used `smollm2:135m` because it was the only local Ollama model present before this repro.
  - Result: Active Memory did hit the live hook, but the sub-agent failed fast because Ollama rejected tools for `smollm2:135m`: `registry.ollama.ai/library/smollm2:135m does not support tools`; Active Memory logged `done status=failed elapsedMs=316 summaryChars=0`.
  - The main run then hit context overflow on the 8k model after tool schemas loaded, so this control was real but not a faithful Active Memory recall pass.
- Live Active Memory gateway run with a tool-capable local model:
  - Gateway startup command: `env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-72015 gateway run --force`.
  - Startup result: gateway ready in about `1.1s`; provider auth prewarm completed in `521ms` with `eventLoopMax=12.6ms`.
  - Command: `/usr/bin/time -p env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-72015 agent --agent main --session-key agent:main:active-memory-qwen-live --message "Please answer in two short paragraphs: what should I check if a local model gateway feels stuck, and mention whether memory can slow the reply path." --json --timeout 180 --verbose on`.
  - Active Memory log: `active-memory: agent=main session=agent:main:active-memory-qwen-live activeProvider=ollama activeModel=qwen2.5:0.5b start timeoutMs=15000 queryChars=177 searchQueryChars=177`.
  - Active Memory result: `done status=no_relevant_memory elapsedMs=1514 summaryChars=0`.
  - Agent result: command succeeded with one visible assistant payload; CLI `real 9.71s`; run metadata reported `durationMs=7191`, provider `ollama`, model `qwen2.5:0.5b`, `input=9844`, `output=350`, `total=10194`, no fallback, `livenessState=working`.
- Concurrent live gateway health during the Active Memory run:
  - Probe command loop: `pnpm openclaw --profile live-repro-72015 health` repeated while the gateway agent call was active.
  - Baseline samples before the turn: `ok max=40ms p99=22ms util=0.029 cpu=0.103` and `ok max=70ms p99=24ms util=0.039 cpu=0.072`.
  - During the turn, one sample degraded: `degraded reasons=event_loop_delay,event_loop_utilization,cpu max=1518ms p99=1518ms util=0.993 cpu=1.114`; the same run's Active Memory span was `1514ms`.
  - Later samples recovered to `ok`, including `max=105ms p99=91ms util=0.152`, then steady `max=39-44ms p99=22-40ms`.
  - No multi-minute stall or timeout reproduced on this Mac with the small tool-capable local model, but the live run did show a short event-loop degradation aligned with the blocking Active Memory stage.
- Live QMD startup attempt:
  - Isolated QMD profile: `live-repro-72015-qmd`, gateway port `19121`, agents `main`, `ops`, `research`, `memory.backend: "qmd"`, `memory.qmd.update.onBoot: true`, `startup: "immediate"`, and `waitForBootSync: true`.
  - `pnpm openclaw --profile live-repro-72015-qmd memory status --deep --json` first reported `qmd binary unavailable (qmd); falling back to builtin: spawn qmd ENOENT`, then failed because the fallback embedding provider wanted an OpenAI API key in the isolated profile.
  - Gateway startup with that QMD profile reached `ready`, then attempted boot sync for all three configured agents and logged one failure per agent after the missing `qmd` binary fallback: `qmd memory startup boot sync failed for agent "main"`, then `ops`, then `research`.
  - Provider auth prewarm completed in `616ms` with `eventLoopMax=118.3ms`; a post-start health probe reported `ok max=46ms p99=22ms util=0.027 cpu=0.1`.
- Finding: current main's Active Memory hook is live and still blocks the reply path while recall runs; in the available local environment it completed in `1514ms` and did not reproduce the historical multi-minute overload, but it did create a measurable short event-loop degradation during a real gateway turn. The QMD boot path is also live and, when startup sync is explicitly opted in with defaults-enabled memory search, still attempts each configured agent sequentially; a faithful QMD overload repro needs the actual `qmd` binary, indexed corpus, and embedding auth/provider instead of the missing-binary fallback seen here.

### #63229 (issue) - Live vLLM infrastructure attempts on current main

Summary: This issue is about healthy local vLLM endpoints being falsely timed out or treated as overloaded.
Live repro result: the remaining vLLM timeout behavior could not be reproduced because no real vLLM server was available; fake backends were intentionally avoided.

- Status: live vLLM reproduction not possible with the currently available local or Crabbox infrastructure; no fake vLLM substitute used.
- Live issue state checked:
  - Issue remains open.
  - Maintainer comment says `3da4b28d1b` partially fixed the `LiveSessionModelSwitchError` -> `overloaded` misclassification, but intentionally left direct vLLM timeout and `sessions_spawn` latency symptoms open.
  - ClawSweeper comment says the remaining bug still needs current-main gateway/provider traces around a healthy local vLLM false timeout, including fallback decisions, fetch timing, idle/run timeout attribution, and gateway RPC timing.
- Required live shape:
  - Real OpenClaw gateway on current main.
  - Real local/private vLLM-compatible endpoints that respond directly in under about a second.
  - Multiple model fallbacks or agents/cron jobs so OpenClaw can misclassify timeout/overload and show fallback cascade behavior.
  - Concurrent gateway RPC timing, especially `sessions_spawn` or equivalent CLI/RPC calls during the model run.
- Local environment check:
  - `vllm` is not installed in local Python.
  - Docker/OrbStack is still unavailable: Docker reports it cannot connect to `/Users/onur/.orbstack/run/docker.sock`.
  - Local Ollama is available with `qwen2.5:0.5b` and `smollm2:135m`, but using Ollama or a synthetic OpenAI-compatible slow server would not be faithful to this vLLM-specific issue.
- Crabbox attempts:
  - RunPod GPU preflight command: `node scripts/crabbox-wrapper.mjs run --provider runpod --target linux --ttl 60m --idle-timeout 30m --no-sync --preflight --timing-json --shell -- "nvidia-smi && python3 --version"`.
  - RunPod result: Crabbox `0.15.0` refused before allocation with `provider=runpod requires RUNPOD_API_KEY`.
  - AWS preflight command: `node scripts/crabbox-wrapper.mjs run --provider aws --target linux --ttl 60m --idle-timeout 30m --no-sync --preflight --timing-json --shell -- "python3 --version && uname -a"`.
  - AWS result: Crabbox recorded `run_776e4f608239`, attempted `eu-west-1`, then failed before host access with `RulesPerSecurityGroupLimitExceeded: The maximum number of rules per security group has been reached`.
- Finding: I have not reproduced the remaining healthy-vLLM false-timeout cascade for #63229. The current live blockers are concrete: no local vLLM install, no running local container runtime, missing RunPod credentials, and AWS Crabbox security-group exhaustion. A faithful next pass needs either the reporter's vLLM endpoint, a GPU host with vLLM installed, a fixed Crabbox AWS allocation, or RunPod credentials; an Ollama/fake slow-server replay would be a shortcut.

### #54155 (issue) - Bounded live gateway/session accumulation canary on current main

Summary: This issue is about gateway memory and session state growing over long-running workloads.
Live repro result: a short real gateway run did not show RSS growth, but it did show session files growing with each turn, so the full multi-day memory issue remains unproven.

- Status: live-tested a bounded current-main gateway/session accumulation pass; did not reproduce the reported multi-day RSS growth in this short local run.
- Environment:
  - macOS local worktree, Node `v24.16.0`, pnpm `11.2.2`, OpenClaw `2026.5.28 (d1577a2)`.
  - Isolated profile: `live-repro-54155`, gateway port `19155`, auth disabled for loopback-only repro.
  - Real local Ollama model: `ollama/qwen2.5:0.5b`, context window `32768`, `maxTokens: 64`.
  - `active-memory` and `memory-core` were disabled for this bounded pass, so this specifically probes gateway/session-store accumulation from real agent turns rather than local embedding or QMD behavior.
- Live commands:
  - Gateway startup command: `env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-54155 gateway run --force`.
  - Startup result: gateway ready in about `0.7s`; provider auth prewarm completed in `440ms` with `eventLoopMax=36.4ms`.
  - Agent loop: 24 sequential real gateway turns using unique session keys `agent:main:mem-live-1` through `agent:main:mem-live-24`; each command used `pnpm openclaw --profile live-repro-54155 agent --agent main --session-key ... --message "Reply exactly: OK <n>" --json --timeout 90`.
- First measurement pass:
  - The first loop accidentally measured the outer `pnpm` wrapper process only, so I treated it as wrapper evidence and reran a process-tree measurement before writing conclusions.
  - Even in that wrapper-only pass, the store grew monotonically: baseline `0` bytes / `0` JSONL files; after 12 turns `260001` bytes / `24` JSONL files.
- Process-tree measurement pass:
  - Process tree after the first 12 turns: root wrapper PID `16732`, pnpm child PID `16741`, leaf gateway runner PID `16757`.
  - Before second pass: root RSS `194480 KB`, pnpm RSS `142336 KB`, leaf RSS `77488 KB`, store `260001` bytes, sessions `12`, JSONL files `24`.
  - After 24 total turns: root RSS `194480 KB`, pnpm RSS `141328 KB`, leaf RSS `76448 KB`, store `520015` bytes, sessions `24`, JSONL files `48`.
  - Per-turn CLI times in the second pass stayed around `2.70s` to `3.06s`; all 12 second-pass runs returned `ok`.
  - Store growth was roughly linear at about `21668` bytes per session entry pair in this profile.
- Post-run checks:
  - `pnpm openclaw --profile live-repro-54155 health` reported `Gateway event loop: ok max=103ms p99=23ms util=0.03 cpu=0.046` with 12 entries after the first pass, and later `ok max=105ms p99=23ms util=0.032 cpu=0.042` with 24 entries.
  - `pnpm openclaw --profile live-repro-54155 sessions --json --limit all` reported `count: 12` after the first pass; final store inspection reported `24` entries and `48` JSONL files.
  - `pnpm openclaw --profile live-repro-54155 sessions cleanup` applied maintenance and left `Current entries: 24`; RSS after cleanup remained root `194480 KB`, pnpm `141328 KB`, leaf `76448 KB`.
- Finding: this short live canary did not reproduce #54155's reported multi-day RSS climb; the actual leaf gateway runner RSS was flat/slightly down from `77488 KB` to `76448 KB` while session files and `sessions.json` grew linearly. It does prove current-main still accumulates persistent session artifacts from ordinary gateway turns, but faithful RSS proof still requires the reported multi-day workload shape: real channel traffic, cron/subagents, local embeddings or failed embedding-provider retries, larger transcripts, and soak/profile measurement.

### #86065 (issue) - Live Active Memory timeout ceiling config-path repro on current main

Summary: This issue is about Active Memory's 120-second timeout ceiling being too low for slow local recall models.
Live repro result: current main rejects `timeoutMs` values above 120 seconds in the real config/gateway path, but the slow vLLM latency need was not tested because no vLLM target was available.

- Status: live-tested the actual config validation and gateway startup paths; did not run the reported slow 27B/FP8 vLLM recall workload.
- Live issue state checked:
  - Issue remains open with `P2`, `clawsweeper:source-repro`, `clawsweeper:needs-maintainer-review`, and `clawsweeper:needs-product-decision`.
  - The issue report and ClawSweeper comment both identify the remaining behavior as the plugin-owned `timeoutMs` ceiling, not the already separate outer hook-runner timeout work.
- Environment:
  - macOS local worktree, Node `v24.16.0`, pnpm `11.2.2`, OpenClaw `2026.5.28 (d1577a2)`.
  - Isolated profile: `live-repro-86065`, gateway port `19165`, auth disabled for loopback-only repro.
  - Real local Ollama model: `ollama/qwen2.5:0.5b`; `memory-core` and `active-memory` enabled.
- Accepted ceiling proof:
  - Config used `plugins.entries.active-memory.config.timeoutMs: 120000` and `setupGraceTimeoutMs: 30000`.
  - Command: `pnpm openclaw --profile live-repro-86065 config validate`.
  - Result: `Config valid: ~/.openclaw-live-repro-86065/openclaw.json`.
  - Gateway command: `env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-86065 gateway run --force`.
  - Result: gateway started successfully; provider auth prewarm completed in `452ms` with `eventLoopMax=14.5ms`.
- Rejected-above-ceiling proof:
  - Changed the same isolated profile to `plugins.entries.active-memory.config.timeoutMs: 120001`.
  - Command: `pnpm openclaw --profile live-repro-86065 config validate`.
  - Result: exited `1` with `plugins.entries.active-memory.config.timeoutMs: invalid config: must be <= 120000`.
  - Gateway startup with the same invalid config also exited `1` after writing a stability bundle and reported: `Gateway failed to start: Invalid config ... timeoutMs: invalid config: must be <= 120000`.
- Local vLLM blocker:
  - `vllm` is not installed locally.
  - Docker/OrbStack is unavailable.
  - RunPod/AWS Crabbox blockers from #63229 still apply.
  - Local Ollama can prove the config ceiling but cannot faithfully reproduce the reported ARM64/DGX Spark + vLLM Qwen3.6-27B-FP8 recall latency.
- Finding: #86065 is live-reproduced at the config/gateway boundary: current main accepts the documented maximum `120000` ms and rejects `120001` before the gateway can start, so operators cannot set a larger Active Memory recall budget today. The slow local-vLLM latency need remains unmeasured here because no faithful vLLM target is available.

### #86048 (issue) - Live WSL2/GPU-PV environment check

Summary: This issue is about WSL2 GPU-PV and `llama-server` entering a driver-level lockup that stalls local inference.
Live repro result: direct reproduction is blocked because this requires Windows, WSL2, and an NVIDIA GPU; source/docs inspection did not find an OpenClaw recovery path for a wedged GPU stack.

- Status: direct live reproduction is unavailable in this environment; no macOS or Ollama substitute used.
- Live issue state checked:
  - Issue remains open with no labels.
  - The only comment is a ClawSweeper review-start placeholder; there is no completed maintainer verdict or OpenClaw fix attached yet.
- Required live shape:
  - Windows host with WSL2 GPU-PV.
  - NVIDIA GPU and WSL2-capable NVIDIA driver.
  - `llama-server`/llama.cpp under CUDA load, preferably matching the reported RTX 5090, llama.cpp b9246, Qwen3.6-35B-A3B Q4_K_M, `--cpu-moe -ngl 85`, and kill-during-CUDA-teardown trigger.
  - Observation that `llama-server` enters D state, `nvidia-smi` hangs on WSL and Windows sides, SIGKILL cannot terminate the process, and `wsl --shutdown` is required.
- Local environment check:
  - Current machine is macOS `26.4` on Apple Silicon (`Darwin ... arm64`) with Apple M5 Pro GPU.
  - `wsl` is not available.
  - `system_profiler SPDisplaysDataType` reports Apple M5 Pro graphics, not NVIDIA.
  - Docker/OrbStack is unavailable.
- Crabbox attempts:
  - AWS Windows preflight command: `node scripts/crabbox-wrapper.mjs run --provider aws --target windows --ttl 60m --idle-timeout 30m --no-sync --preflight --timing-json --shell -- "powershell -NoProfile -Command \"$PSVersionTable.PSVersion; wsl -l -v; nvidia-smi\""`.
  - AWS result: Crabbox recorded `run_0b32aa17c1db`, then failed before allocation with `RulesPerSecurityGroupLimitExceeded: The maximum number of rules per security group has been reached`.
  - RunPod preflight command: `node scripts/crabbox-wrapper.mjs run --provider runpod --target linux --ttl 60m --idle-timeout 30m --no-sync --preflight --timing-json --shell -- "nvidia-smi && uname -a"`.
  - RunPod result: Crabbox `0.15.0` refused before allocation with `provider=runpod requires RUNPOD_API_KEY`; even a Linux GPU host would not be WSL2 GPU-PV, but it would at least check NVIDIA availability for adjacent local-model stalls.
- Source/docs check:
  - Repo search found WSL2 setup/docs and local-provider timeout/fallback logic, but no OpenClaw-owned WSL2 GPU-PV health watchdog or automatic `wsl --shutdown` recovery path.
  - Existing OpenClaw local-provider timeout/fallback controls can detect a request-layer stalled inference, but cannot recover a kernel/driver D-state process where `nvidia-smi` itself hangs.
- Finding: I did not reproduce #86048. The available Mac and Crabbox state cannot provide the required Windows + WSL2 + NVIDIA GPU-PV failure mode; current proof is limited to environment checks and source inspection showing OpenClaw has no driver-level recovery path for this class of hang. A faithful repro needs an actual Windows/WSL2 NVIDIA host with the llama.cpp workload and teardown trigger.

### #73801 (issue) - Live Cerebras Active Memory auth-boundary check

Summary: This issue is about Cerebras-backed Active Memory timing out and leaving the gateway CPU-bound.
Live repro result: the isolated OpenClaw config is valid, but the real Cerebras provider call is blocked because this environment has no Cerebras API key.

- Status: direct live Cerebras reproduction is blocked in this environment; no fake provider or local-model substitute used.
- Required live shape:
  - OpenClaw gateway with Active Memory configured for `cerebras/gpt-oss-120b`.
  - Valid Cerebras API credentials with `chat/completions` access to `gpt-oss-120b`.
  - Real direct/channel traffic while measuring recall elapsed time, gateway CPU, `/health`, websocket/admin responsiveness, and cleanup after timeout.
- Live issue state checked:
  - Issue remains open.
  - The 2026-05-26 reporter reproduced the same failure mode on OpenClaw `2026.5.22 (a374c3a)` with Active Memory + `cerebras/gpt-oss-120b`, including timeouts beyond the configured budget, memory pressure, liveness warnings, and `embedded run abort still streaming`.
  - ClawSweeper's acceptance criteria still ask for live or harnessed Active Memory recall against `cerebras/gpt-oss-120b`, with elapsed/CPU/health/websocket/admin proof.
- Local credential check:
  - `CEREBRAS_API_KEY=missing`.
  - `OPENCLAW_CEREBRAS_API_KEY=missing`.
  - I did not inspect or use any production OpenClaw auth profile or personal Cerebras credential state.
- Isolated OpenClaw product-path check:
  - Created isolated profile `live-repro-73801`, config under `~/.openclaw-live-repro-73801`, gateway port `19138`, Active Memory enabled, model `cerebras/gpt-oss-120b`, timeout `5000` ms, memory-core enabled, and explicit Cerebras OpenAI-compatible provider config using `${CEREBRAS_API_KEY}`.
  - Command: `pnpm openclaw --profile live-repro-73801 config validate`.
  - Result: config valid for `~/.openclaw-live-repro-73801/openclaw.json`.
  - Command: `pnpm openclaw --profile live-repro-73801 models status --json`.
  - Result: config warning `missing env var "CEREBRAS_API_KEY" at models.providers.cerebras.apiKey`; JSON reported `defaultModel: "cerebras/gpt-oss-120b"`, `auth.missingProvidersInUse: ["cerebras"]`, and provider `cerebras` effective auth `{ "kind": "missing", "detail": "missing" }`.
- Finding: I did not reproduce #73801 live. The current environment reaches the real OpenClaw Cerebras config/auth path and confirms the repro is blocked by missing Cerebras credentials before any provider stream can run. A faithful repro still needs a valid Cerebras key and a real Active Memory recall run against `cerebras/gpt-oss-120b`; source tests alone do not prove the reported CPU/health recovery behavior.

### #86633 (PR) - Live PR-branch Ollama canary

Summary: This PR adds cooperative yielding during dense Ollama stream processing to reduce event-loop starvation.
Live repro result: the PR branch worked against a real local Ollama model and kept the gateway healthy in a small Mac canary, but it did not prove the original Windows dense-stream stall is fixed.

- Status: live-tested on the PR head with real local Ollama; original dense Windows/gateway starvation symptom not reproduced in this environment.
- PR state checked:
  - PR remains open, not draft.
  - Head: `e40e6a4731003e80b203300b4cefee68a89be79e` from `udaymanish6/openclaw:fix/86599-local-provider-event-loop`.
  - Current maintainer/ClawSweeper review still blocks on real behavior proof and says the PR should be scoped as a narrow native-Ollama mitigation, not the whole #86599 fix.
- Isolated PR worktree:
  - Worktree: `/Users/onur/oc/openclaw-worktrees/86633-repro`.
  - Command: `git fetch origin pull/86633/head:refs/remotes/origin/pr/86633` and `git worktree add --detach /Users/onur/oc/openclaw-worktrees/86633-repro refs/remotes/origin/pr/86633`.
  - Installed dependencies once with `pnpm install --frozen-lockfile` because the fresh worktree had no `node_modules`.
- Focused PR test:
  - Command: `node scripts/run-vitest.mjs extensions/ollama/src/stream.test.ts --reporter=verbose`.
  - Result: 1 test file passed, 9 tests passed.
  - New covered case: `createOllamaStreamFn thinking events > yields to the event loop while processing dense native stream chunks`.
- Live local Ollama setup:
  - Local Ollama models available: `qwen2.5:0.5b` and `smollm2:135m`.
  - Created isolated profile `live-repro-86633`, config under `~/.openclaw-live-repro-86633`, gateway port `19133`, auth disabled for loopback-only repro, Ollama provider enabled, Active Memory and memory-core disabled, default model `ollama/qwen2.5:0.5b`.
  - Command: `pnpm openclaw --profile live-repro-86633 config validate`.
  - Result: config valid.
- Live OpenClaw local transport on PR head:
  - Command: `/usr/bin/time -p env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-86633 infer model run --local --model ollama/qwen2.5:0.5b --prompt "Write 60 short numbered facts about calendar math. Keep each fact under 10 words." --json`.
  - Result: `real 10.37s`; JSON output succeeded with `ok: true`, `transport: "local"`, provider `ollama`, model `qwen2.5:0.5b`. This timing includes one runtime-artifact sync/build in the fresh PR worktree.
- Live OpenClaw gateway transport on PR head:
  - Gateway startup command: `env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-86633 gateway run --force`.
  - Startup result: gateway ready on port `19133`; provider auth prewarm completed in `178ms` with `eventLoopMax=0.0ms`.
  - Command: `/usr/bin/time -p env OLLAMA_API_KEY=ollama-local pnpm openclaw --profile live-repro-86633 infer model run --gateway --model ollama/qwen2.5:0.5b --prompt "Write 120 short numbered facts about calendar math. Keep each fact under 10 words." --json`.
  - Result: `real 5.30s`; JSON output succeeded with `ok: true`, `transport: "gateway"`, provider `ollama`, model `qwen2.5:0.5b`, one text output of `373` bytes.
- Concurrent gateway health probes:
  - Probe command loop: `pnpm openclaw --profile live-repro-86633 health` repeated while and just after the gateway model call.
  - Reported gateway loop samples stayed `ok`, including `max=175ms p99=22ms util=0.11 cpu=0.18`, `max=281ms p99=150ms util=0.255 cpu=0.322`, then steady post-run samples around `max=65-69ms p99=22-23ms util=0.033-0.041`.
  - No liveness warning appeared in the observed gateway output; the gateway shut down cleanly after the canary.
- Finding: this is real PR-branch local-provider proof that #86633 still runs through OpenClaw local and gateway transports against Ollama, and the focused dense-yield test passes. It is not a full live reproduction of the original stall because current main also did not reproduce the Windows/dense-burst symptom with the available small local models, so this run cannot honestly prove a before/after improvement; it only narrows the proof gap.

### #85788 (PR) - PR-branch spawnedByCache eviction harness

Summary: This PR evicts `spawnedByCache` entries after terminal subagent lifecycle events to address one gateway leak path.
Live repro result: the PR-head harness proved the cache entry is removed after completed subagent runs, but no long-running RSS soak was done.

- Status: PR-head harness proof completed; no real long-running gateway/subagent RSS soak performed.
- PR state checked:
  - PR remains open, not draft.
  - Head: `02be8d8bbbf5a2bed842387ea023d046ab761d86` from `georgeboiko/openclaw:fix/spawned-by-cache-leak`.
  - Current ClawSweeper review says the implementation is small and plausible but blocked on stronger real gateway/subagent runtime proof.
- Source comparison:
  - Merge base with current repro worktree: `35969ff4400ae8aea188d340ee5b6b0c4e8545b9`.
  - PR surface at the merge base: source +2, tests +74 across `src/gateway/server-chat.ts` and `src/gateway/server-chat.agent-events.test.ts`.
  - PR code adds `spawnedByCache.delete(sessionKey)` in both terminal `finalizeLifecycleEvent()` paths.
  - PR test drives 500 unique `agent:*:subagent:*` session keys through one handler and checks the closure-internal spawnedBy cache retains zero entries.
- PR worktree/test:
  - Worktree: `/Users/onur/oc/openclaw-worktrees/85788-repro`.
  - Command: `git worktree add --detach /Users/onur/oc/openclaw-worktrees/85788-repro refs/remotes/origin/pr/85788`.
  - Installed dependencies once with `pnpm install --frozen-lockfile` because the fresh worktree had no `node_modules`.
  - Command: `node scripts/run-vitest.mjs src/gateway/server-chat.agent-events.test.ts --reporter=verbose`.
  - Result: 1 test file passed, 69 tests passed.
  - Relevant new covered case: `spawnedByCache memory leak > spawnedByCache size stays at 0 after N runs with unique sessionKeys`.
- Finding: #85788 has direct PR-branch harness proof for the exact add-only cache it changes, and that proof is stronger than source inspection alone. It is still not a live gateway/subagent runtime soak, does not measure RSS, and should not be used to close the broader #54155 gateway memory tracker.

### #78435 (issue) - Slack start-account live blocker and current handoff check

Summary: This issue is about Slack startup/reconnect work blocking the gateway event loop during active runs.
Live repro result: direct Slack Socket Mode reproduction is blocked by missing isolated Slack credentials; current main has test-covered handoff mitigation but still needs real Slack proof.

- Status: direct live Slack reproduction is blocked in this environment; no production Slack credentials inspected or used.
- Live issue state checked:
  - Issue remains open.
  - Latest reporter evidence includes Windows `2026.5.12-beta.1` hot-reload-triggered stalls and Linux `2026.5.12` stalls on every agent run, all attributed to `phase=channels.slack.start-account`.
- Credential/environment check:
  - `SLACK_BOT_TOKEN=missing`.
  - `SLACK_APP_TOKEN=missing`.
  - `OPENCLAW_SLACK_BOT_TOKEN=missing`.
  - `OPENCLAW_SLACK_APP_TOKEN=missing`.
  - Without an isolated Slack app/workspace, a faithful Socket Mode reconnect or hot-reload repro cannot be run safely.
- Current-main source check:
  - `src/gateway/server-channels.ts` now wraps only the startup handoff in `measureStartup("channels.<id>.start-account-handoff", ...)`, stores the returned `startAccountTask`, and awaits the long-lived channel task after the measured phase exits.
  - `extensions/slack/src/channel.ts` still maps Slack `gateway.startAccount` to `monitorSlackProvider(...)`.
  - `extensions/slack/src/monitor/provider.ts` still keeps Socket Mode inside a reconnect loop, so a real Slack runtime can still be long-lived; current source now avoids keeping the startup trace span open for that whole lifetime.
- Focused test:
  - Command: `node scripts/run-vitest.mjs src/gateway/server-channels.test.ts extensions/slack/src/monitor/provider.reconnect.test.ts extensions/slack/src/monitor/provider.allowlist.test.ts src/logging/diagnostic.test.ts --reporter=verbose`.
  - Result: 4 test files passed, 106 tests passed.
  - Relevant covered cases: `ends startup trace spans before long-lived channel account tasks settle`, `emits startup trace spans for channel preflight and handoff`, Slack Socket Mode reconnect helper behavior, Slack startup user allowlist resolution, and diagnostic phase/work labels in liveness warnings.
- Finding: I did not reproduce #78435 live. Current main has a source/test mitigation for the old coarse `channels.slack.start-account` diagnostic span by narrowing it to `start-account-handoff`, but this does not prove the reported Windows/Linux Slack event-loop stalls are gone; a faithful check still needs an isolated Slack Socket Mode app, current main, hot reload or active agent traffic, and liveness/CPU proof.

### #77443 (issue) - WhatsApp Windows first-inbound live blocker and current mitigation checks

Summary: This issue is about WhatsApp on Windows blocking the event loop after the first inbound message.
Live repro result: direct reproduction is blocked because it needs Windows 11 and a linked WhatsApp account; current tests cover retry mitigation but do not prove the first-inbound stall is gone.

- Status: direct live WhatsApp/Windows reproduction is blocked in this environment; no production WhatsApp credentials or linked sessions inspected or used.
- Live issue state checked:
  - Issue remains open with `bug` and `regression` labels.
  - Reporter says they can reproduce on demand on Windows 11 with a linked WhatsApp account and are available to test instrumentation or PRs.
- Local environment check:
  - Current host is macOS `26.4` on Apple Silicon, not Windows 11.
  - No isolated `live-repro-77443` profile exists.
  - `WHATSAPP_SESSION=missing`.
  - `OPENCLAW_WHATSAPP_SESSION=missing`.
- Current-main source check:
  - Current code has renamed the old `src/agents/pi-embedded-runner` path to `src/agents/embedded-agent-runner`.
  - `src/agents/embedded-agent-runner/resource-loader.ts` creates the embedded resource loader with filesystem discovery skip options for extensions, skills, prompt templates, themes, and context files.
  - `src/agents/embedded-agent-runner/run/attempt.ts` still awaits `resourceLoader.reload()` and marks the `session-resource-loader` prep stage, so the reporter's implicated startup boundary still exists.
  - `extensions/whatsapp/src/auto-reply/monitor.ts` keeps Baileys 428 / `Connection Terminated` on the reconnect path for opening-phase and post-open closes.
- Focused tests:
  - Command: `node scripts/run-vitest.mjs src/agents/embedded-agent-runner/resource-loader.test.ts extensions/whatsapp/src/auto-reply.web-auto-reply.connection-and-logging.e2e.test.ts --reporter=verbose`.
  - Result: only the embedded-agent resource-loader test was selected by the default wrapper: 2 project test files passed, 2 tests passed.
  - Correct WhatsApp e2e lane command: `OPENCLAW_E2E_VERBOSE=1 node scripts/run-vitest.mjs --config test/vitest/vitest.e2e.config.ts extensions/whatsapp/src/auto-reply.web-auto-reply.connection-and-logging.e2e.test.ts --reporter=verbose -t "428"`.
  - Result: 1 test file passed, 2 tests passed, 22 skipped.
  - Relevant covered cases: `retries opening-phase Boom 428 through the reconnect policy` and `keeps post-open Baileys 428 on the reconnect path`.
- Finding: I did not reproduce #77443 live. Current main has useful embedded-loader discovery-skip and WhatsApp 428 reconnect mitigation coverage, but the faithful reproduction still requires Windows 11, a linked WhatsApp account, the first inbound message path, and event-loop/model-call timing proof.

### #86599 (issue) - Local model provider calls block gateway event loop

Summary: This issue is about local Ollama/native model streams causing repeated gateway-side work that can block the event loop.
Live repro result: the Mac/Ollama canary stayed responsive and did not reproduce the Windows stall, while source and synthetic probes still support the dense-stream risk.

- Status: source-confirmed.
- Target environment: Windows beta with local Ollama/Qwen or equivalent dense native stream; local macOS worktree can only cover source/test-level reproduction unless Windows/real local model infrastructure is available.
- Live issue state checked: open P1 issue with current discussion saying the symptom is not fully proven fixed on main and likely has two contributors: full-partial repeated streaming work and dense local stream loops.
- Source evidence:
  - `extensions/ollama/src/stream.ts` still parses all NDJSON lines from one read in a tight `for` loop before returning to the event loop.
  - `extensions/ollama/src/stream.ts` rebuilds and emits a full `partial` assistant message on each `text_delta`.
  - `src/agents/pi-embedded-runner/run/attempt.model-diagnostic-events.ts` still measures stream bytes by `JSON.stringify(chunk)`, so a growing full-partial payload creates repeated cumulative work.
  - `src/agents/pi-embedded-subscribe.handlers.messages.ts` still extracts visible text from the full partial and can reprocess accumulated text.
- Local probe:
  - Command: local `node` synthetic stream-work probe in the worktree.
  - Result: delta-only accounting for a 320 KB final answer measured about 0.64 MB and took about 3 ms; full-partial JSON accounting measured about 1.6 GB and took about 941 ms.
  - Result: parsing 50,000 dense JSON records without yielding delayed a timer by about 6.9 ms; yielding every 64 records reduced timer delay to about 0.9 ms on this Mac.
- Focused test:
  - Initial `node scripts/run-vitest.mjs extensions/ollama/src/stream.test.ts --reporter=verbose` failed because the new worktree had no `node_modules`.
  - Ran `pnpm install --frozen-lockfile` once in the worktree; lockfile policy passed and dependencies installed.
  - Reran `node scripts/run-vitest.mjs extensions/ollama/src/stream.test.ts --reporter=verbose`; result: 1 test file passed, 8 tests passed.
- Direct repro gap: did not reproduce the Windows beta gateway symptom end-to-end because this run has no Windows local Ollama/llama.cpp setup attached.
- Finding: current main still contains the repeated full-partial work and the dense Ollama parser shape implicated by #86599, while the existing focused Ollama tests pass and do not cover the dense-stream event-loop-yield regression proposed in #86633.

### #85826 (issue) - Agent stall detector kills legitimate long local vLLM calls

Summary: This issue is about legitimate long local vLLM calls being classified as stalled when they stay silent too long.
Live repro result: no real vLLM target was available, so direct live proof is blocked; source/tests still confirm the stall classification and abort path.

- Status: source-confirmed.
- Target environment: local vLLM serving a large Qwen model on ARM64/DGX Spark with long model calls above 120 seconds; unavailable in this local macOS worktree.
- Live issue state checked: open P1 issue; ClawSweeper review says the exact live vLLM timing was not reproduced but the source behavior is reproducible.
- Source evidence:
  - `src/config/zod-schema.ts` exposes `diagnostics.stuckSessionWarnMs` and `diagnostics.stuckSessionAbortMs`, so the issue's original "no configuration knob" premise is outdated on current main and was reportedly already contradicted by v2026.5.20 source.
  - `src/logging/diagnostic.ts` defaults warning classification to `120_000` ms and computes the default abort threshold as at least 5 minutes and 3x the warning threshold.
  - `src/logging/diagnostic-session-attention.ts` classifies any active work, including `model_call`, as `session.stalled` / `stalled_agent_run` when `lastProgressAgeMs > staleMs`.
  - `src/logging/diagnostic.ts` makes stalled active `model_call` work with an active embedded run eligible for active-abort recovery once `lastProgressAgeMs >= diagnostics.stuckSessionAbortMs`.
- Focused test:
  - Command: `node scripts/run-vitest.mjs src/logging/diagnostic-session-attention.test.ts src/logging/diagnostic.test.ts --reporter=verbose`.
  - Result: 2 test files passed, 63 tests passed.
  - Relevant covered cases include configurable `diagnostics.stuckSessionWarnMs`, active sessions reported as stalled when active work stops progressing, recovery of stale model calls through the active embedded-run abort path, no abort for model calls with recent stream progress, active abort of silent local model calls after the stuck timeout, and use of `diagnostics.stuckSessionAbortMs` for stalled active-work recovery.
- Direct repro gap: did not run a live vLLM call long enough to cross the thresholds, because this worktree has no local vLLM/DGX setup.
- Finding: the current behavior is not hard-coded in the sense originally claimed, but current source and tests do confirm the core risk: a long silent local model call can be classified as stalled and later active-aborted unless the operator raises the diagnostics thresholds or the provider emits progress.

### #84569 (issue) - WhatsApp long model call ends with payloads=0 and no reply

Summary: This issue is about long vLLM-backed WhatsApp turns ending with no delivered payload after an error/fallback path.
Live repro result: the live WhatsApp plus vLLM repro is blocked by missing isolated WhatsApp and vLLM environments; source/tests confirm the WhatsApp error-payload suppression path.

- Status: source-confirmed.
- Target environment: live WhatsApp session plus long vLLM-backed model call; unavailable in this local worktree because it requires WhatsApp credentials/session state and a slow local model backend.
- Live issue state checked: open P1 issue with an open linked PR, #84578, targeting the WhatsApp final error delivery path.
- Source evidence:
  - `src/agents/pi-embedded-runner/run.ts` returns a final fallback payload with `text: "⚠️ Agent couldn't generate a response. Please try again."` and `isError: true` for reasoning-only exhausted / incomplete visible-output paths.
  - `extensions/whatsapp/src/auto-reply/monitor/inbound-dispatch.ts` drops every `payload.isError === true` before delivery, regardless of lifecycle kind.
  - `extensions/whatsapp/src/outbound-base.ts` also returns an empty WhatsApp message id for any routed `ctx.payload.isError === true`.
  - Current WhatsApp tests encode the suppression behavior with tests named `suppresses error payload text` and `suppresses routed error payloads`.
- Focused test:
  - Command: `node scripts/run-vitest.mjs extensions/whatsapp/src/auto-reply/monitor/inbound-dispatch.test.ts extensions/whatsapp/src/outbound-adapter.sendpayload.test.ts --reporter=verbose`.
  - Result: 2 test files passed, 55 tests passed.
  - Relevant covered behavior: current main expects final WhatsApp error payload text not to call `deliverReply`, and routed WhatsApp error payloads not to call `sendWhatsApp`.
- Direct repro gap: did not run a live WhatsApp stalled-session reproduction.
- Finding: the delivery-loss path is directly reproducible from source and tests on current main. The broader long-model-call trigger is shared with #85826, but the WhatsApp-specific user-visible silence is caused by final `isError` payload suppression in two WhatsApp delivery boundaries.

### #75657 (issue) - Local GGUF embedding warmup blocks the Node event loop

Summary: This issue is about local GGUF embedding warmup blocking the Node event loop during gateway startup.
Live repro result: current main no longer shows the old in-process warmup path and reaches a worker boundary, but actual ARM64/Pi native GGUF behavior was not tested.

- Status: not-reproduced on current main; source changed since the issue's ClawSweeper review.
- Target environment: Raspberry Pi/ARM64 with `memorySearch.provider: "local"` and a large GGUF embedding model; unavailable in this local macOS worktree.
- Live issue state checked: open issue. The issue's review comment says the older source path loaded `node-llama-cpp` in the Gateway process, but that comment was against older source and is no longer accurate for the current worktree base.
- Current source evidence:
  - `packages/memory-host-sdk/src/host/embeddings.ts` now makes the public `createLocalEmbeddingProvider()` call `createLocalEmbeddingWorkerProvider()`.
  - `packages/memory-host-sdk/src/host/embeddings-worker.ts` forks a file-backed worker child with IPC and sends `initialize`, `embedQuery`, `embedBatch`, and `close` requests to that child.
  - `packages/memory-host-sdk/src/host/embeddings-worker-child.ts` is the only path that calls `createLocalEmbeddingProviderInProcess()`, so `importNodeLlamaCpp()`, `resolveModelFile()`, `loadModel()`, and `createEmbeddingContext()` run inside the child process instead of the Gateway process for the public provider.
  - `src/gateway/server-startup-memory.ts` also avoids eager multi-agent QMD startup by default unless startup refresh is opted in, the default agent is involved, defaults explicitly enable memory search, or an agent has explicit memory search config.
- Focused test:
  - Command: `node scripts/run-vitest.mjs packages/memory-host-sdk/src/host/embeddings.test.ts src/gateway/server-startup-memory.test.ts src/gateway/server-startup-post-attach.test.ts --reporter=verbose`.
  - Result: 3 test files passed, 65 tests passed.
  - Relevant covered behavior: `uses a worker process for the public local provider`, worker termination and failure handling, `keeps qmd managers lazy when startup refresh is not opted in`, and `keeps the qmd memory backend lazy by default`.
- Direct repro gap: did not run the reporter's Raspberry Pi/systemd/GGUF setup, so I did not prove the six-minute ARM64 startup stall is gone in that environment.
- Finding: the original in-process local GGUF warmup path is not reproduced on current main from source or focused tests because the public local embedding provider now isolates GGUF work behind a child process. Remaining risk is packaging/runtime proof on real ARM64/Pi, not the old absence of a worker/process boundary.

### #72015 (issue) - Active Memory blocks replies and QMD boot overloads gateways

Summary: This issue is about Active Memory and QMD work delaying or blocking user-visible replies.
Live repro result: the local gateway canary confirmed Active Memory still runs in the reply path, but it only produced a short delay with the available small Ollama setup.

- Status: source-confirmed with partial mitigations; see the live addendum above for the current macOS/Ollama/QMD-boundary canary.
- Target environment: live multi-agent gateway with Active Memory enabled, QMD onBoot work, and a slow/heavy active model; the local live canary used small Ollama models and could not cover a real QMD binary/corpus load.
- Live issue state checked: open P1 issue with `clawsweeper:source-repro`, `clawsweeper:needs-product-decision`, and linked open PRs #73667 and #80255. #73667 is still open draft; #80255 is open and targets active-memory main-lane deadlock.
- Current source evidence:
  - `extensions/active-memory/index.ts` still registers a `before_prompt_build` hook and awaits `maybeResolveActiveRecall()` before prompt construction can proceed.
  - `extensions/active-memory/index.ts` still resolves the recall model from `config.model`, then the current run model, then the agent default model, so unset Active Memory config can inherit the heavy interactive model.
  - `extensions/active-memory/index.ts` calls `runEmbeddedPiAgent()` for recall without passing a dedicated `lane`.
  - `src/agents/pi-embedded-runner/lanes.ts` resolves an omitted global lane to `main`, and `src/process/command-queue.ts` creates command lanes with `maxConcurrent: 1`.
  - `src/gateway/server-startup-memory.ts` has current QMD startup mitigations: it skips non-QMD backends, requires startup boot sync to be enabled, eagerly starts only single-agent/default/explicitly configured/defaults-enabled agents, and logs deferred agents.
- Focused test:
  - Command: `node scripts/run-vitest.mjs extensions/active-memory/index.test.ts src/gateway/server-startup-memory.test.ts src/agents/pi-embedded-runner/lanes.test.ts --reporter=verbose`.
  - Result: 3 test files passed, 139 tests passed.
  - Relevant covered behavior: `before_prompt_build` registration and timeout configuration, fallback to the current session model when no plugin model is configured, framing the blocking memory subagent as another model call, timeout/deadline handling, `defaults to main lane when no lane is provided`, and current QMD lazy/deferred startup behavior.
- Direct repro gap: did not reproduce the historical multi-minute overload with a slow/heavy active model or a real QMD indexed corpus; local live testing covered the Active Memory hook with Ollama `qwen2.5:0.5b` and QMD startup only up to missing `qmd` binary fallback.
- Finding: current main has useful hard-deadline and QMD-startup mitigations, but the reply-critical architecture remains: Active Memory recall is still awaited inside `before_prompt_build`, can inherit the active chat model, and still omits a dedicated embedded-runner lane. The live canary shows this blocking hook path runs in a real gateway turn and can briefly degrade the gateway event loop, but the available Mac/small-model environment does not reproduce the original multi-minute overload.

### #63229 (issue) - Healthy local vLLM endpoints falsely timed out or overloaded

Summary: This issue is about healthy local vLLM endpoints being timed out or sent through fallback cascades.
Live repro result: the remaining vLLM timeout case could not be run without a real vLLM server; source/tests show one misclassification is fixed but several timeout budgets still exist.

- Status: partially source-confirmed; remaining false-timeout symptom not directly reproduced; see live addendum above for the current vLLM infrastructure attempts.
- Target environment: live gateway with local vLLM endpoints, multiple agents/cron jobs, and local provider traces; unavailable in this worktree and blocked by current local/Crabbox infrastructure.
- Live issue state checked: open P1 issue. Maintainer comment says commit `3da4b28d1b` partially fixed the `LiveSessionModelSwitchError` -> `overloaded` misclassification, while direct timeout and `sessions_spawn` latency symptoms remain open.
- Current source evidence:
  - `src/agents/model-fallback.ts` now treats `LiveSessionModelSwitchError` as failover with `reason: "unknown"` unless it can redirect to a later matching live-session candidate; it no longer applies overloaded cooldown semantics to that internal switch error.
  - `src/agents/model-fallback.test.ts` covers last-candidate live-session switch errors, continuing fallback past them, direct jump to a later live-session candidate, and not redirecting stale switch errors back to the current candidate.
  - `src/agents/pi-embedded-runner/run/llm-idle-timeout.ts` detects loopback, private IPv4, CGNAT, unique-local/link-local IPv6, and `.local` base URLs and disables the default cloud idle watchdog for local providers unless an explicit timeout is configured.
  - The same timeout resolver still honors explicit `models.providers.<id>.timeoutSeconds`, explicit run timeouts, and shorter `agents.defaults.timeoutSeconds`, so misconfiguration or caller timeouts can still produce local-provider aborts even when the default local watchdog is disabled.
  - `docs/providers/vllm.md` documents `models.providers.vllm.timeoutSeconds` as the vLLM HTTP request budget and separates it from `agents.defaults.timeoutSeconds`, which controls the whole agent run.
- Focused test:
  - Command: `node scripts/run-vitest.mjs src/agents/model-fallback.test.ts src/agents/pi-embedded-runner/run/llm-idle-timeout.test.ts src/agents/model-fallback.run-embedded.e2e.test.ts --reporter=verbose`.
  - Result: 4 project test files passed, 288 tests passed.
  - Relevant covered behavior: live-session switch errors are not overloaded, command-lane watchdog timeouts are not treated as model fallback failures, local/private/.local provider URLs disable the default idle watchdog, explicit provider request timeouts are honored, and shorter agent/run timeouts still bound local providers.
- Direct repro gap: did not run a live local vLLM endpoint or capture current-main fallback/RPC timing traces, so the remaining healthy-vLLM false-timeout cascade is not directly reproduced; local and Crabbox attempts could not provision a real vLLM target.
- Finding: the `overloaded` misclassification part is fixed on current main and covered by tests. The issue remains credible but only partially source-confirmed here: current code shows multiple timeout budgets that can still abort local providers, while the specific reported false timeout and `sessions_spawn` backpressure path need live current-main traces from a real vLLM endpoint.

### #54155 (issue) - Gateway memory growth with session accumulation

Summary: This issue is about long-lived gateway memory growth from accumulated session and runtime state.
Live repro result: the short live gateway canary did not reproduce RSS growth, but persistent session artifacts still grew linearly with turns.

- Status: source-confirmed with partial mitigations; see the live addendum above for the bounded current-main gateway/session accumulation canary.
- Target environment: multi-day gateway soak with channel traffic, cron, subagents, local model traffic, local embeddings/memory search, large transcripts, and failed embedding/provider paths; the local canary covered only short-lived gateway turns with one local Ollama model.
- Live issue state checked: open P1 issue with `clawsweeper:source-repro`, `impact:session-state`, and `impact:crash-loop`. Maintainer comment says #73737 fixed one concrete session-store clone contributor but explicitly keeps this as the broader RSS/session-accumulation tracker.
- Related live PRs checked:
  - #85788 is open and targets `spawnedByCache` eviction on lifecycle end.
  - #75089 is open and targets stale gateway raw/projected/delta chat buffer cleanup.
- Current source evidence:
  - `src/gateway/server-chat.ts` still creates a per-handler `spawnedByCache` map and caches subagent/ACP session keys; current main tests cover lookup caching but not eviction to zero after many distinct session keys.
  - `src/gateway/server-chat.ts` now clears `rawBuffers`, projected buffers, delta metadata, and agent text throttle state in `clearBufferedChatState()` on normal terminal lifecycle cleanup, so one raw-buffer path has been mitigated.
  - `src/gateway/server-maintenance.ts` receives `abortedRuns`, `deltaLastBroadcastText`, `agentDeltaSentAt`, and `bufferedAgentEvents`, plus separate projected chat buffers/delta maps, but not `rawBuffers`; #75089 targets this stale raw-buffer maintenance gap.
  - `src/config/sessions/store-cache.ts` clones session stores through JSON-shaped clones and interns large strings, so the old session-store `structuredClone` contributor is mitigated.
  - `src/agents/auth-profiles/runtime-snapshots.ts` still clones auth-profile runtime snapshots through `cloneAuthProfileStore()`, which remains part of the broader clone/retention concern called out in related review context.
- Focused test:
  - Command: `node scripts/run-vitest.mjs src/gateway/server-chat.agent-events.test.ts src/gateway/server-maintenance.test.ts src/gateway/chat-abort.test.ts src/infra/agent-events.test.ts src/config/sessions.cache.test.ts --reporter=verbose`.
  - Result: 7 project test files passed, 147 tests passed.
  - Relevant covered behavior: session-store cache isolation without `structuredClone`, stale run context/sequence cleanup, chat abort buffer handling, lifecycle cleanup of run sequence tracking, spawnedBy lookup caching, and current maintenance cleanup for projected/orphaned stale buffers and agent throttle state.
- Direct repro gap: did not run a long-lived gateway soak/profile and did not measure RSS/native heap over days; the short live canary did not reproduce RSS growth.
- Finding: current main has several partial mitigations, but #54155 remains source-confirmed as a broad retention tracker because at least one current-main add-only cache path is still open in #85788, stale raw-buffer cleanup is still open in #75089, and no current-main representative soak evidence proves RSS plateaus under the reported workload. The bounded live canary showed session artifacts accumulating linearly while leaf gateway RSS stayed flat at this small scale.

### #86065 (issue) - Active Memory timeout cap is too low for slow local recall models

Summary: This issue is about the Active Memory timeout ceiling preventing operators from allowing slower local recall models to finish.
Live repro result: the real config/gateway path rejects values above 120 seconds today, while the reported slow vLLM recall workload was not available to measure.

- Status: source-confirmed and live-reproduced at the config/gateway boundary; see the live addendum above.
- Target environment: live Active Memory recall against a slow local vLLM model on ARM64/DGX Spark; the latency workload was not run here.
- Live issue state checked: open P2 issue with `clawsweeper:source-repro`, `clawsweeper:needs-maintainer-review`, and `clawsweeper:needs-product-decision`.
- Current source evidence:
  - `extensions/active-memory/openclaw.plugin.json` sets `timeoutMs` maximum to `120000`, so manifest validation rejects larger configured values.
  - `extensions/active-memory/index.ts` also clamps runtime `config.timeoutMs` to `120_000` in `normalizePluginConfig()`.
  - `extensions/active-memory/index.ts` separately allows `setupGraceTimeoutMs` only up to `30_000` and computes the outer `before_prompt_build` watchdog as `timeoutMs + setupGraceTimeoutMs`.
  - `docs/concepts/active-memory.md` documents the same 120000 ms cap for `config.timeoutMs`.
- Focused test:
  - Command: `node scripts/run-vitest.mjs extensions/active-memory/config.test.ts extensions/active-memory/index.test.ts --reporter=verbose`.
  - Result: 2 test files passed, 135 tests passed.
  - Relevant covered behavior: manifest accepts `timeoutMs: 120_000`, rejects values above the runtime ceiling, runtime honors values above the former 60s ceiling, and runtime clamps `timeoutMs: 200_000` down to `120_000`.
- Direct repro gap: did not run the reported 27B/FP8 local vLLM recall workload, so I did not measure whether 120s is insufficient on that hardware; local live proof covers the enforced config ceiling.
- Finding: the issue is directly reproduced: current main intentionally enforces the 120s Active Memory runtime and manifest ceiling, and the real CLI/gateway config path rejects `timeoutMs: 120001`. The live latency claim is not reproduced, but operators cannot configure `timeoutMs` above 120s today.

### #86048 (issue) - WSL2 GPU-PV / llama-server D-state lockup

Summary: This issue is about a WSL2/NVIDIA `llama-server` driver hang that presents to OpenClaw as a local inference stall.
Live repro result: direct reproduction is blocked without Windows/WSL2/GPU-PV hardware; current source inspection found detection-level controls but no recovery for the wedged driver state.

- Status: blocked for direct reproduction; see the live addendum above for current local and Crabbox environment checks.
- Target environment: Windows host with WSL2 GPU-PV, NVIDIA RTX 5090-class GPU, llama.cpp/llama-server under CUDA load, and a driver-level D-state failure; not available from this macOS worktree or current Crabbox allocation state.
- Live issue state checked: open issue with no labels and only a ClawSweeper review-start placeholder comment; no completed maintainer review or OpenClaw fix is attached yet.
- Source/docs evidence:
  - Repository search found general WSL2/local-model documentation and local-provider watchdog logic, but no OpenClaw-owned WSL2 GPU-PV `nvidia-smi` health watchdog or automatic `wsl --shutdown` recovery path.
  - The reported failure is below OpenClaw's process boundary: `llama-server` enters uninterruptible sleep, `nvidia-smi` hangs on both WSL and Windows, and SIGKILL cannot terminate the process.
  - Existing OpenClaw local-model timeout and fallback controls can detect stalled inference at the request/session layer, but cannot recover a wedged WSL2 NVIDIA kernel/driver stack.
- Focused test: none run; no local unit test can exercise a WSL2 GPU-PV driver D-state lockup.
- Direct repro gap: no Windows/WSL2 GPU host with the reporter's NVIDIA driver, llama.cpp build, model, and kill-during-CUDA-teardown setup is available in this run; AWS Windows Crabbox allocation is blocked by security-group exhaustion and RunPod requires credentials.
- Finding: this remains an external-platform live-repro item, not source-confirmed as an OpenClaw bug. The current OpenClaw repo does not appear to contain an automatic mitigation for a wedged WSL2 GPU-PV stack, so the practical reproduction path would need a real Windows/WSL2 GPU host or Crabbox/static Windows target with GPU-PV access.

### #73801 (issue) - Active Memory with Cerebras gpt-oss-120b times out and can pin gateway CPU

Summary: This issue is about Cerebras `gpt-oss-120b` Active Memory timing out and affecting gateway liveness.
Live repro result: the live provider call is blocked by missing Cerebras credentials, but current source still contains the documented Cerebras Active Memory path and generic timeout mitigations.

- Status: source-confirmed for the current path; direct live Cerebras CPU/health symptom blocked by missing credentials. See the live addendum above for the isolated config/auth-boundary check.
- Target environment: live gateway with Cerebras API access, Active Memory configured to `cerebras/gpt-oss-120b`, and real channel traffic; not available in this worktree because `CEREBRAS_API_KEY` / `OPENCLAW_CEREBRAS_API_KEY` are unset and no usable isolated auth profile exists.
- Live issue state checked: open issue. The original report was for 2026.4.26, and a later reporter reproduced the same pattern on 2026.5.22 with Active Memory + `cerebras/gpt-oss-120b`, including timeout, memory pressure, event-loop/cpu liveness warnings, and `embedded run abort still streaming`.
- Current source evidence:
  - `docs/concepts/active-memory.md` still recommends `cerebras/gpt-oss-120b` as a fast dedicated Active Memory recall model.
  - `extensions/cerebras/openclaw.plugin.json` still declares `gpt-oss-120b` as a Cerebras `openai-completions` model with `reasoning: true`.
  - `extensions/active-memory/index.ts` still runs foreground recall from `before_prompt_build`, passes `provider`, `model`, `timeoutMs`, `reasoningLevel: "off"`, `toolsAllow`, and an abort signal into `runEmbeddedPiAgent()`, then races the subagent against a plugin watchdog.
  - The same code now has mitigations: a hard deadline even if the subagent does not cooperate, late-payload ignore behavior, timeout circuit breaker, and memory-search-manager cleanup after timeout.
- Focused test:
  - Command: `node scripts/run-vitest.mjs extensions/active-memory/index.test.ts src/agents/openai-transport-stream.test.ts --reporter=verbose -t "returns timeout within a hard deadline|ignores late subagent payloads|yields to aborts during bursty OpenAI-compatible streams|gpt-oss"`.
  - Result: 3 project test files passed, 4 tests passed, 518 skipped.
  - Relevant covered behavior: Active Memory returns within a hard deadline even when a subagent ignores abort, ignores late subagent payloads after timeout, and OpenAI-compatible streams yield to aborts during bursty stream processing.
- Direct repro gap: did not call live Cerebras and did not measure current-main gateway CPU, `/health`, or websocket/admin responsiveness during and after a Cerebras Active Memory timeout; the isolated product-path check stops at missing provider auth.
- Finding: current main still contains the documented Cerebras Active Memory path and has reporter evidence as recent as 2026.5.22. Generic abort/deadline tests pass and the isolated profile validates, but they do not prove Cerebras stream cleanup or gateway health recovery under the live provider, so the issue remains credible and not closed by local source tests.

### #86633 (PR) - Cooperative yields for dense Ollama stream processing

Summary: This PR adds cooperative yields while dense Ollama stream chunks are processed.
Live repro result: the PR-head local Ollama canary passed on Mac, but it did not reproduce or prove the original Windows dense-stream stall before and after the patch.

- Status: source-confirmed as a narrow mitigation; PR head live-tested with a small local Ollama canary, but the original dense Windows/gateway stall was not reproduced. See the live addendum above.
- Target environment: live Ollama/native local stream or Windows beta gateway scenario from #86599; local PR proof used macOS + Ollama `qwen2.5:0.5b`, which was not heavy/dense enough to reproduce the original #86599 symptom.
- Live PR state checked: open, not draft. ClawSweeper review says patch quality is plausible but merge is blocked on real behavior proof; the PR body only includes mocked Vitest proof.
- PR diff evidence:
  - `extensions/ollama/src/stream.ts` adds a cooperative scheduler with a 64-event / 12 ms threshold and uses `setImmediate()` to yield during dense native stream processing.
  - The PR also adds abort checks before/after scheduled yields and inside the stream loop.
  - `extensions/ollama/src/stream.test.ts` adds a mocked dense NDJSON test that checks a timer can fire before the stream completes.
- Current-main repro evidence from #86599:
  - Current main still parses dense Ollama NDJSON chunks without a macrotask yield in the loop body.
  - Local synthetic probe showed 50,000 dense JSON records without yielding delayed a timer by about 6.9 ms, while yielding every 64 records reduced timer delay to about 0.9 ms on this Mac.
  - Current main's focused Ollama test still passes with 8 tests; it lacks the PR's dense-yield regression test.
- Focused test:
  - Command on current main: `node scripts/run-vitest.mjs extensions/ollama/src/stream.test.ts --reporter=verbose`.
  - Result: 1 test file passed, 8 tests passed.
  - PR-head proof from the live addendum above: `node scripts/run-vitest.mjs extensions/ollama/src/stream.test.ts --reporter=verbose` passed with 9 tests on `e40e6a4731003e80b203300b4cefee68a89be79e`.
- Direct repro gap: did not run the reporter's Windows gateway scenario or a dense local model stream that reproduced the pre-patch stall; the PR-head live canary only proves real Ollama local/gateway success and responsive health in this available environment.
- Finding: the PR targets a real source-level dense-stream starvation path and matches the synthetic yield probe. The PR-head local Ollama canary narrows the proof gap, but it is only a narrow native-Ollama mitigation, does not address the broader repeated full-partial stream work from #86599, and still lacks a faithful before/after repro of the reported Windows/dense-stream stall.

### #85788 (PR) - Evict spawnedByCache on terminal gateway lifecycle

Summary: This PR removes one gateway `spawnedByCache` entry when a subagent session finishes.
Live repro result: the PR-head harness proved the cache is evicted, but no live long-running gateway RSS soak was performed.

- Status: source-confirmed as a narrow current-main leak fix; PR-head harness proof completed, but live gateway soak proof missing. See the live addendum above.
- Target environment: long-lived gateway processing many distinct subagent/ACP sessions; not run as a multi-day soak here.
- Live PR state checked: open, not draft. The PR is labeled P1/gateway and ClawSweeper says implementation is plausible but still needs real runtime proof before merge.
- PR diff evidence:
  - `src/gateway/server-chat.ts` adds `spawnedByCache.delete(sessionKey)` in both terminal `finalizeLifecycleEvent()` paths.
  - `src/gateway/server-chat.agent-events.test.ts` adds a regression test that drives 500 unique subagent session keys through one handler and checks the closure-internal cache does not retain entries.
- Current source evidence:
  - Current main still creates `spawnedByCache` inside `createAgentEventHandler()` and caches eligible subagent/ACP session keys.
  - Current main terminal lifecycle cleanup clears buffers, run context, and sequence state, but does not delete from `spawnedByCache`.
  - Subagent session keys use random UUID-derived keys, so repeated one-shot subagent runs can produce an unbounded key set in one long-lived handler.
  - The current test suite only checks lookup caching and null caching; it does not prove eviction after terminal lifecycle events.
- Focused test:
  - Command: `node scripts/run-vitest.mjs src/gateway/server-chat.agent-events.test.ts extensions/slack/src/monitor/provider.reconnect.test.ts extensions/slack/src/monitor/provider.allowlist.test.ts src/gateway/server-channels.test.ts src/gateway/server-reload-handlers.test.ts src/gateway/channel-health-monitor.test.ts src/logging/diagnostic.test.ts src/agents/pi-embedded-runner/resource-loader.test.ts extensions/whatsapp/src/auto-reply.web-auto-reply.connection-and-logging.e2e.test.ts --reporter=verbose`.
  - Result: 11 test files passed, 296 tests passed.
  - Relevant covered behavior: current spawnedBy lookup caching still works, but current main lacks the PR's eviction regression test.
  - PR-head focused test from the live addendum above: `node scripts/run-vitest.mjs src/gateway/server-chat.agent-events.test.ts --reporter=verbose` passed with 69 tests on `02be8d8bbbf5a2bed842387ea023d046ab761d86`, including the new 500-unique-session eviction regression.
- Direct repro gap: did not run a real gateway/subagent soak/profile after applying the patch, and did not measure RSS/native heap over time.
- Finding: #85788 targets a real current-main add-only cache and is a credible narrow fix for part of #54155. The PR-head harness test proves the changed handler path empties the cache after terminal lifecycle events, but the PR should not close the broader gateway RSS tracker without separate soak evidence.

### #78435 (issue) - Slack start-account phase stalls event loop during active runs

Summary: This issue is about Slack `start-account` startup/reconnect work stalling the gateway event loop during active runs.
Live repro result: direct Slack reproduction is blocked by missing isolated Slack credentials; current main has handoff mitigation covered by tests but still needs live profiling.

- Status: current main has a handoff-phase mitigation covered by tests; direct live Slack reproduction blocked by missing isolated Slack credentials. See the live addendum above.
- Target environment: Slack Socket Mode, channel hot reload or health-monitor restart, and active agent/model work on Windows or Linux; not available in this worktree.
- Live issue state checked: open. Reporter evidence includes Windows 2026.5.4, 2026.5.7, 2026.5.12-beta.1, and Linux 2026.5.12 logs with repeated `phase=channels.slack.start-account` warnings during active agent work.
- Current source evidence:
  - `src/gateway/server-channels.ts` now measures `channels.<id>.start-account-handoff`, captures the returned `startAccountTask`, exits the measured span, and then awaits the long-lived account task.
  - `extensions/slack/src/channel.ts` maps Slack `gateway.startAccount` directly to `monitorSlackProvider()`.
  - `extensions/slack/src/monitor/provider.ts` keeps Socket Mode inside a reconnect loop, awaiting `startSlackSocketAndWaitForDisconnect()` until abort.
  - `extensions/slack/src/monitor/provider-support.ts` awaits `app.start()` and then waits for socket disconnect; source inspection did not show sub-step phase attribution or a hard upper bound for the whole monitor loop.
  - Current diagnostics report the currently active phase, so the old `channels.slack.start-account` evidence from released builds may not map exactly to current-main phase naming after the handoff mitigation.
- Focused test:
  - Command: `node scripts/run-vitest.mjs src/gateway/server-channels.test.ts extensions/slack/src/monitor/provider.reconnect.test.ts extensions/slack/src/monitor/provider.allowlist.test.ts src/logging/diagnostic.test.ts --reporter=verbose`.
  - Result: 4 test files passed, 106 tests passed.
  - Relevant covered behavior: the startup trace span ends before long-lived channel account tasks settle, Slack reconnect helper/status behavior, Slack startup user allowlist resolution, and diagnostic liveness phase/work labels.
- Direct repro gap: did not run live Slack Socket Mode, Windows, Linux, hot reload, or active model-call overlap.
- Finding: #78435 is adjacent to the local-runtime stall cluster because it blocks the same gateway event loop while agent/model work is active, but it is channel-startup centered rather than local/open-weight-model centered. Current main has a handoff mitigation for the coarse phase span, but a safe close/fix decision still needs live Slack profiling or narrower sub-step instrumentation on a real affected setup.

### #77443 (issue) - WhatsApp first inbound blocks event loop on Windows

Summary: This issue is about WhatsApp on Windows blocking the event loop around the first inbound message and embedded-agent startup.
Live repro result: direct Windows linked-WhatsApp reproduction is blocked; current main has reconnect and resource-loader mitigations but still needs a live Windows retest.

- Status: source-confirmed for remaining implicated paths; direct live Windows linked-WhatsApp repro blocked. See the live addendum above.
- Target environment: Windows 11, linked WhatsApp account, first inbound message after gateway start, and active embedded agent startup; not available in this worktree.
- Live issue state checked: open bug/regression. Reporter says they can reproduce on demand on Windows 11 with a linked WhatsApp account; related PR #75773 merged recovery mitigations but did not include full Windows live proof.
- Current source evidence:
  - `extensions/whatsapp/src/auto-reply/monitor.ts` now treats Baileys 428 as retryable, keeping both opening-phase and post-open 428 closes on the reconnect path instead of fail-closing the monitor.
  - `src/agents/embedded-agent-runner/resource-loader.ts` wraps `DefaultResourceLoader` with discovery skip options for extensions, skills, prompt templates, themes, and context files.
  - `src/agents/embedded-agent-runner/run/attempt.ts` still constructs the embedded resource loader and awaits `resourceLoader.reload()` before marking `session-resource-loader`, so the reporter's implicated prep-stage boundary still exists.
  - The embedded loader still owns the actual `DefaultResourceLoader.reload()` implementation; this run did not prove the Windows event-loop behavior of that dependency boundary.
- Focused test:
  - Command: `node scripts/run-vitest.mjs src/agents/embedded-agent-runner/resource-loader.test.ts --reporter=verbose`.
  - Result: 2 project test files passed, 2 tests passed.
  - Command: `OPENCLAW_E2E_VERBOSE=1 node scripts/run-vitest.mjs --config test/vitest/vitest.e2e.config.ts extensions/whatsapp/src/auto-reply.web-auto-reply.connection-and-logging.e2e.test.ts --reporter=verbose -t "428"`.
  - Result: 1 test file passed, 2 tests passed, 22 skipped.
  - Relevant covered behavior: embedded loader skip flags, WhatsApp opening-phase 428 retry, and post-open 428 reconnect behavior pass locally.
- Direct repro gap: no Windows 11 live WhatsApp account, no Baileys socket, and no first-inbound model-call trace were run.
- Finding: current main contains useful recovery and discovery-skip mitigations, but it still reaches the embedded resource-loader reload boundary and lacks post-merge Windows linked-WhatsApp proof. Keep open until a live first-inbound retest shows event-loop delay and subsequent model calls recover.
