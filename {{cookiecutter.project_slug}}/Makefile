.DEFAULT_GOAL := help

.PHONY: help install sync build typecheck fix check lint format test test-unit test-cov ci clean tree

# ── Help ──────────────────────────────────────────────────────────────────────

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Setup"
	@echo "  install        Install dependencies (frozen) and set up git hooks"
	@echo "  sync           Install dependencies (relaxed, for local iteration)"
	@echo ""
	@echo "Quality"
	@echo "  fix            Auto-fix lint and formatting (ultracite fix)"
	@echo "  check          Check lint and formatting without writing (ultracite check)"
	@echo "  typecheck      TypeScript type checking (tsc --noEmit)"
	@echo ""
	@echo "Testing"
	@echo "  test           Run tests"
	@echo "  test-cov       Run tests with coverage (80% threshold)"
	@echo ""
	@echo "CI"
	@echo "  ci             Full pipeline: check + typecheck + test:cov + audit"
	@echo ""
	@echo "Utility"
	@echo "  build          Build library (tsup → dist/)"
	@echo "  clean          Remove dist/, coverage/, caches"
	@echo "  tree           Print directory tree (DEPTH=3)"

# ── Setup ─────────────────────────────────────────────────────────────────────

install:
	pnpm install --frozen-lockfile
	pnpm run prepare

sync:
	pnpm install

# ── Build ─────────────────────────────────────────────────────────────────────

build:
	pnpm run build

# ── Quality ───────────────────────────────────────────────────────────────────

typecheck:
	pnpm run typecheck

fix:
	pnpm run fix

check:
	pnpm run check

lint: fix
format: fix

# ── Testing ───────────────────────────────────────────────────────────────────

test:
	pnpm run test $(TEST_ARGS)

test-cov:
	pnpm run test:cov

# ── CI ────────────────────────────────────────────────────────────────────────

ci:
	pnpm run ci

# ── Utility ───────────────────────────────────────────────────────────────────

clean:
	@bash scripts/clean.sh

DEPTH ?= 3
tree:
	@node scripts/tree.mjs $(DEPTH)

# ── Server (use_server) ───────────────────────────────────────────────────────

dev:
	pnpm run dev:server

serve:
	pnpm run start

# ── Docker (use_docker) ───────────────────────────────────────────────────────

TAG ?= latest
build-image:
	docker build -t {{ cookiecutter.project_slug }}:$(TAG) .

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

ps:
	docker compose ps

# ── Database / Prisma (use_prisma) ────────────────────────────────────────────

db-push:
	pnpm run db:push

db-migrate:
	pnpm run db:migrate

db-studio:
	pnpm run db:studio

db-generate:
	pnpm run db:generate

# ── Docs / TypeDoc (use_typedoc) ──────────────────────────────────────────────

docs-build:
	pnpm run docs:build

docs-serve:
	pnpm run docs:serve

docs-clean:
	rm -rf docs/
