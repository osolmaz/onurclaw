#!/usr/bin/env bash
set -euo pipefail

workspace="${OPENCLAW_ONUR_WORKSPACE:-/workspace}"
inventory="${OPENCLAW_ONUR_INVENTORY_PATH:-${workspace}/OPENCLAW_ONUR_INVENTORY.md}"
inventory_json="${OPENCLAW_ONUR_INVENTORY_JSON_PATH:-${workspace}/OPENCLAW_ONUR_INVENTORY.json}"
gitcrawl_db="${OPENCLAW_ONUR_GITCRAWL_DB:-/gitcrawl/gitcrawl.db}"
notifier_db="${OPENCLAW_ONUR_NOTIFIER_DB:-/gitcrawl/notifier.sqlite}"
state_file="${OPENCLAW_ONUR_COMPARE_STATE:-/state/inventory-notifier-compare-state.json}"
limit="${OPENCLAW_ONUR_COMPARE_LIMIT:-8}"

fail() {
  printf 'inventory job failed: %s\n' "$1" >&2
  exit 1
}

case "$workspace" in
  /workspace) ;;
  *) fail "workspace must be /workspace" ;;
esac

cd "$workspace"

test -f "$inventory" || fail "missing inventory file"
test -r "$gitcrawl_db" || fail "missing readable gitcrawl database"
test -r "$notifier_db" || fail "missing readable notifier database"
mkdir -p "$(dirname "$state_file")"
test -w "$(dirname "$state_file")" || fail "state directory is not writable"

python3 scripts/inventory_source.py "$gitcrawl_db" >/dev/null

top_level="$(git rev-parse --show-toplevel 2>/dev/null || true)"
test "$top_level" = "$workspace" || fail "workspace is not the repository root"

remote_url="$(git remote get-url origin 2>/dev/null || true)"
case "$remote_url" in
  *osolmaz/onurclaw* | *osolmaz/onurclaw.git*) ;;
  *) fail "unexpected repository remote" ;;
esac

OPENCLAW_ONUR_INVENTORY_SKIP_ACTIVITY=1 \
  python3 scripts/sort_openclaw_onur_inventory.py --no-activity "$inventory" >/dev/null

python3 scripts/export_inventory_json.py "$inventory" "$inventory_json" >/dev/null
python3 scripts/validate_inventory_json.py "$inventory_json" >/dev/null

report="$(
  python3 scripts/inventory_notifier_compare.py \
    --inventory "$inventory" \
    --inventory-json "$inventory_json" \
    --notifier-db "$notifier_db" \
    --state-file "$state_file" \
    --limit "$limit"
)"

if ! git diff --quiet -- OPENCLAW_ONUR_INVENTORY.md OPENCLAW_ONUR_INVENTORY.json; then
  git add -- OPENCLAW_ONUR_INVENTORY.md OPENCLAW_ONUR_INVENTORY.json
  git \
    -c user.name="${ONURCLAW_GIT_AUTHOR_NAME:-Onur Inventory Job}" \
    -c user.email="${ONURCLAW_GIT_AUTHOR_EMAIL:-onur-inventory-job@example.invalid}" \
    commit -m "docs: refresh OpenClaw Onur inventory" >/dev/null
fi

if [ "$report" = "NO_REPLY" ]; then
  report="NO_CHANGES"
fi

printf '%s\n' "$report"
