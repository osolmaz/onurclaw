# OpenClaw llama-server provider

Connect OpenClaw to an existing llama.cpp `llama-server` process over HTTP.

The plugin uses OpenClaw's shared OpenAI completions transport. It owns endpoint normalization, passive model discovery, runtime context and chat-template capability mapping, optional API-key setup, router status, and llama.cpp-safe tool schemas. It does not download, build, launch, stop, or reconfigure `llama-server`.

## Development install

This source currently targets OpenClaw `2026.7.2` and its matching Plugin SDK.

```bash
openclaw plugins install /path/to/onurclaw/extensions/llama-server
```

Restart the gateway, run `openclaw onboard`, and choose `llama-server`. The default endpoint is `http://127.0.0.1:8080/v1`.

For an existing checkout, you can also add this directory to `plugins.load.paths` and enable the `llama-server` plugin.

Run the unit tests and type check against a compatible OpenClaw source checkout:

```bash
OPENCLAW_CHECKOUT=/path/to/openclaw ./scripts/test.sh
```

See [PROVIDER.md](PROVIDER.md) for setup, configuration, router behavior, authentication, and troubleshooting.
