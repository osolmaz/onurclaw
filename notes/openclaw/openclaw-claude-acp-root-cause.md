# OpenClaw Claude ACP Root Cause

Date: 2026-04-06

## Summary

The `claude-1` Discord bound ACP channel was not failing because of Discord, channel config, or persisted session metadata.

The real root cause was that the live Claude ACP child process was being launched under Node `18.19.1`, even though the OpenClaw gateway itself was running under Node `22.22.0`.

`@agentclientprotocol/claude-agent-acp@0.25.0` uses modern ESM syntax that Node 18 cannot parse, so the child crashed during ACP startup before the handshake completed.

## Exact Failure

Live gateway tracing showed the Claude path reached ACP client startup and then died during initialize:

- OpenClaw reached `ensureSession()`
- ACPX created the Claude client
- the Claude child was spawned
- the child exited with code `1` during ACP initialize

Captured stderr from the live Claude ACP child:

```text
file:///home/bob/.npm/_npx/c8a5d52d0f75a7d1/node_modules/@agentclientprotocol/claude-agent-acp/dist/acp-agent.js:7
import packageJson from "../package.json" with { type: "json" };
                                          ^^^^
SyntaxError: Unexpected token 'with'
Node.js v18.19.1
```

## Why Codex Still Worked

Codex was using a different launcher path:

- Claude default command: `npm exec @agentclientprotocol/claude-agent-acp@^0.25.0`
- Codex default command: `npx @zed-industries/codex-acp@^0.11.1`

On this machine, the Codex path did not hit the same Node-18 failure, so Codex continued to work while Claude failed.

## Why It Looked Like a Hang

The Claude child did not fail before spawn. It failed after spawn, during ACP initialize.

So the visible behavior in OpenClaw was:

- channel message entered `reply_dispatch`
- `ensureSession()` started
- Claude child spawned
- handshake never completed
- channel appeared stuck

This was not a real infinite hang in Claude itself. It was a subprocess startup crash that was not being surfaced clearly enough by the ACP runtime path.

## What Was Ruled Out

The following were explicitly ruled out during debugging:

- Discord ingress problems
- bad `claude-1` channel config
- bad ACP binding metadata alone
- ACPX generally being broken
- Claude ACP generally being broken
- the specific session key being inherently bad

Direct ACPX and direct Claude ACP usage worked outside the live gateway path.

## Practical Conclusion

The broken behavior came from subprocess Node resolution in the live OpenClaw gateway environment.

The fix direction is:

1. make sure the Claude ACP launcher uses the intended Node 22 runtime
2. avoid launcher paths that silently fall back to older system Node binaries
3. fail fast and surface a clear error when the ACP child exits during initialize
