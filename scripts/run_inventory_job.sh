#!/usr/bin/env bash
set -euo pipefail

exec "${OPENCLAW_ONUR_WORKSPACE:-/workspace}/scripts/finalize_inventory_job.sh" "$@"
