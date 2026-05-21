# cookiecutter-ts

A modern, opinionated TypeScript project template built with the same philosophy as [cookiecutter-python](https://github.com/{{ cookiecutter.github_username }}/cookiecutter-python): strict quality standards, feature flags, and CI/CD ready out of the box.

## Features

- **pnpm** — fast, disk-efficient package manager
- **TypeScript 5.x** — strict mode with all safety flags enabled
- **ultracite** — unified Rust-based linter (oxlint) + formatter (oxfmt) — same stack as [Vercel AI SDK](https://github.com/vercel/ai)
- **vitest** — fast test runner with coverage
- **tsup** — zero-config dual ESM/CJS build
- **husky** + **lint-staged** — pre-commit hooks
- **commitlint** — conventional commits enforced
- **GitHub Actions** — CI pipeline + npm publish workflow

## Feature Flags

| Flag | Default | Description |
|------|---------|-------------|
| `use_server` | `false` | Fastify web server with `/health` endpoint |
| `use_zod` | `true` | Zod runtime validation |
| `use_docker` | `false` | Multi-stage Dockerfile |
| `use_prisma` | `false` | Prisma ORM + migrations |
| `use_cli` | `false` | Commander CLI app |
| `use_typedoc` | `false` | TypeDoc documentation |

## Usage

```bash
# Install cookiecutter
pip install cookiecutter

# Generate a project
cookiecutter gh:YOUR_GITHUB_USERNAME/cookiecutter-ts

# Or use the bootstrap script (works inside existing repos too)
bash bootstrap.sh
```

## Generated Project Commands

```bash
make install      # Install deps (frozen) + set up husky hooks
make sync         # Install deps (relaxed, for local iteration)
make build        # Build library (tsup → dist/)
make typecheck    # TypeScript type check (tsc --noEmit)
make fix          # Auto-fix lint + format (ultracite fix)
make check        # Check lint + format without writing (ultracite check)
make test         # Run tests (vitest)
make test-cov     # Run tests with coverage (80% threshold)
make ci           # Full pipeline: check + typecheck + test:cov + audit
make clean        # Remove dist/, coverage/, caches
```
