#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:-}"

if [[ -z "$VERSION" ]]; then
    echo "Usage: bash scripts/release.sh <version>"
    echo "Example: bash scripts/release.sh 1.2.3"
    exit 1
fi

# Validate semver (x.y.z or x.y.z-pre)
if ! echo "$VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+(-[a-zA-Z0-9.]+)?$'; then
    echo "ERROR: '$VERSION' is not a valid semver (e.g. 1.2.3 or 1.2.3-alpha.1)"
    exit 1
fi

# Ensure working tree is clean
if ! git diff --quiet || ! git diff --staged --quiet; then
    echo "ERROR: Working tree is not clean. Commit or stash changes first."
    exit 1
fi

echo "Releasing v$VERSION..."

# Bump version in package.json
npm pkg set version="$VERSION"

git add package.json
git commit -m "chore: release v$VERSION"
git tag -a "v$VERSION" -m "Release v$VERSION"

echo ""
echo "Release v$VERSION ready. Push with:"
echo "  git push && git push --tags"
