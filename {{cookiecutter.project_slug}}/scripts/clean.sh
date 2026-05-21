#!/usr/bin/env bash
set -euo pipefail

echo "Cleaning build artifacts and caches..."

rm -rf dist
rm -rf coverage
rm -rf node_modules/.cache
rm -f tsconfig.tsbuildinfo
rm -f tsconfig.test.tsbuildinfo
rm -rf .turbo
find . -name "*.tsbuildinfo" -not -path "./node_modules/*" -delete

echo "Done."
