#!/usr/bin/env bash
set -euo pipefail

plugin_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
openclaw_root=${OPENCLAW_CHECKOUT:-${1:-}}

if [[ -z "$openclaw_root" || ! -f "$openclaw_root/package.json" ]]; then
  echo "usage: OPENCLAW_CHECKOUT=/path/to/openclaw $0" >&2
  exit 2
fi
if [[ ! -x "$openclaw_root/node_modules/.bin/vitest" || ! -x "$openclaw_root/node_modules/.bin/tsc" ]]; then
  echo "OpenClaw dependencies are not installed in $openclaw_root" >&2
  exit 2
fi

mkdir -p "$plugin_root/node_modules"
ln -sfn "$openclaw_root" "$plugin_root/node_modules/openclaw"
ln -sfn "$openclaw_root/node_modules/vitest" "$plugin_root/node_modules/vitest"

"$openclaw_root/node_modules/.bin/vitest" run --config "$plugin_root/vitest.config.ts"
"$openclaw_root/node_modules/.bin/tsc" -p "$plugin_root/tsconfig.json"
"$openclaw_root/node_modules/.bin/tsc" -p "$plugin_root/tsconfig.build.json"
