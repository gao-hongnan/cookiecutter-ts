#!/usr/bin/env bash
set -euo pipefail

TEMPLATE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPLAY_CACHE="$HOME/.cookiecutter_replay/cookiecutter-ts.json"

# Clear stale replay cache for fresh prompts
if [[ -f "$REPLAY_CACHE" ]]; then
    rm -f "$REPLAY_CACHE"
fi

# Detect if we're inside an existing git repo
if git rev-parse --is-inside-work-tree &>/dev/null 2>&1; then
    REPO_ROOT="$(git rev-parse --show-toplevel)"
    TMP_DIR="$(mktemp -d)"
    trap 'rm -rf "$TMP_DIR"' EXIT

    echo "Detected existing git repo at $REPO_ROOT"
    echo "Generating template to temp directory, then syncing files..."

    cookiecutter "$TEMPLATE_DIR" -o "$TMP_DIR"

    # Find the generated project directory (first subdirectory)
    GENERATED="$(find "$TMP_DIR" -maxdepth 1 -mindepth 1 -type d | head -1)"

    rsync -av --exclude='.git' --exclude='.venv' --exclude='node_modules' \
        "$GENERATED/" "$REPO_ROOT/"

    cd "$REPO_ROOT"
    pnpm install || true
    pnpm run prepare || true

    echo ""
    echo "Files synced into $REPO_ROOT"
    echo "Run 'make ci' to verify everything works."
else
    echo "Generating new project..."
    cookiecutter "$TEMPLATE_DIR"
fi
