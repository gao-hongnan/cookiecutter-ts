# cookiecutter-ts

A modern, opinionated TypeScript project template. Same philosophy as
[cookiecutter-python](https://github.com/gao-hongnan/cookiecutter-python):
strict quality standards, feature flags, and CI/CD ready out of the box.

## Features

- **Node.js 24 / 26 / 22** — current LTS lines (24 is the default)
- **pnpm 12** — fast, disk-efficient package manager
- **TypeScript 6.x** — strict mode with all safety flags enabled
- **ultracite** — unified Rust-based linter (oxlint) + formatter (oxfmt) —
  same stack as [Vercel AI SDK](https://github.com/vercel/ai)
- **vitest** — fast test runner with coverage
- **tsup** — zero-config dual ESM/CJS build
- **husky** + **lint-staged** — pre-commit hooks
- **commitlint** — conventional commits enforced
- **GitHub Actions** — CI pipeline + npm publish workflow

## Feature Flags

| Flag          | Default | Description                                |
| ------------- | ------- | ------------------------------------------ |
| `use_server`  | `false` | Fastify web server with `/health` endpoint |
| `use_zod`     | `true`  | Zod runtime validation                     |
| `use_docker`  | `false` | Multi-stage Dockerfile for the server      |
| `use_prisma`  | `false` | Prisma 7 ORM (SQLite) + migrations         |
| `use_cli`     | `false` | Commander CLI app                          |
| `use_typedoc` | `false` | TypeDoc documentation                      |

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
make audit        # Audit dependencies (fails on high/critical)
make ci           # Full pipeline: check + typecheck + test:cov + audit
make clean        # Remove dist/, coverage/, caches
```

Feature flags add their own targets (`make dev`, `make build-image`,
`make db-migrate`, `make docs-build`, and others). Run `make help` in the
generated project to list them.

## Toolchain Notes

- **TypeScript stays on 6.x.** TypeScript 7 (the native port) ships no
  compiler API yet, so tsup's declaration build and TypeDoc 0.28 cannot run
  on it. Move to 7.x once both support it.
- **Prisma 7** reads the connection URL from `prisma.config.ts`, not from
  `schema.prisma`, and generates the client into `src/generated/prisma`
  (gitignored and regenerated on `postinstall`). To query at runtime, add a
  driver adapter such as `@prisma/adapter-better-sqlite3`.
- **pnpm 11+** reads pnpm settings from `pnpm-workspace.yaml`. Packages that
  run install scripts must be listed under `allowBuilds` there.
