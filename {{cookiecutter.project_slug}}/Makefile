.DEFAULT_GOAL := help

.PHONY: help install sync build typecheck fix check lint format test test-cov audit ci clean tree

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
	@echo "  audit          Audit dependencies for vulnerabilities (pnpm audit)"
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
{%- if cookiecutter.use_server %}
	@echo ""
	@echo "Server"
	@echo "  dev            Run the server with reload (tsx watch)"
	@echo "  serve          Build and run the compiled server"
{%- endif %}
{%- if cookiecutter.use_docker %}
	@echo ""
	@echo "Docker"
	@echo "  build-image    Build the container image (TAG=latest)"
	@echo "  run-image      Run the container image on port 3000"
{%- endif %}
{%- if cookiecutter.use_prisma %}
	@echo ""
	@echo "Database"
	@echo "  db-push        Push the Prisma schema to the database"
	@echo "  db-migrate     Create and apply a migration"
	@echo "  db-studio      Open Prisma Studio"
	@echo "  db-generate    Regenerate the Prisma client"
{%- endif %}
{%- if cookiecutter.use_typedoc %}
	@echo ""
	@echo "Docs"
	@echo "  docs-build     Build API docs (TypeDoc → docs/)"
	@echo "  docs-serve     Serve docs/ locally"
	@echo "  docs-clean     Remove docs/"
{%- endif %}

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

audit:
	pnpm run audit

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
{%- if cookiecutter.use_server %}

# ── Server ────────────────────────────────────────────────────────────────────

.PHONY: dev serve

dev:
	pnpm run dev:server

serve: build
	pnpm run start
{%- endif %}
{%- if cookiecutter.use_docker %}

# ── Docker ────────────────────────────────────────────────────────────────────

.PHONY: build-image run-image

TAG ?= latest
build-image:
	docker build -f environments/container/Dockerfile -t {{ cookiecutter.project_slug }}:$(TAG) .

run-image:
	docker run --rm -p 3000:3000 {{ cookiecutter.project_slug }}:$(TAG)
{%- endif %}
{%- if cookiecutter.use_prisma %}

# ── Database / Prisma ─────────────────────────────────────────────────────────

.PHONY: db-push db-migrate db-studio db-generate

db-push:
	pnpm run db:push

db-migrate:
	pnpm run db:migrate

db-studio:
	pnpm run db:studio

db-generate:
	pnpm run db:generate
{%- endif %}
{%- if cookiecutter.use_typedoc %}

# ── Docs / TypeDoc ────────────────────────────────────────────────────────────

.PHONY: docs-build docs-serve docs-clean

docs-build:
	pnpm run docs:build

docs-serve:
	pnpm run docs:serve

docs-clean:
	rm -rf docs/
{%- endif %}
