# {{ cookiecutter.project_name }}

## Project Overview

{{ cookiecutter.project_description }}

## Tech Stack

- **Runtime**: Node.js {{ cookiecutter.node_version }}+
- **Language**: TypeScript (strict mode)
- **Package Manager**: pnpm
- **Linter**: oxlint (via ultracite)
- **Formatter**: oxfmt (via ultracite)
- **Tests**: vitest
- **Build**: tsup

## Common Commands

```bash
make install    # Install deps + set up git hooks
make fix        # Auto-fix lint + format
make typecheck  # Type check
make test       # Run tests
make test-cov   # Run tests with coverage
make audit      # Audit dependencies for known vulnerabilities
make ci         # Full CI pipeline
make build      # Build to dist/
make clean      # Remove build artifacts
```

Run `make help` for feature-specific targets.

## Code Style

- Single quotes for strings
- Semicolons required
- 80 character line width
- 2-space indentation, LF line endings
- Trailing commas in multi-line expressions
- `import type` for type-only imports

## Commit Convention

Uses [Conventional Commits](https://www.conventionalcommits.org/):
`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`, `ci:`

## Testing

Tests live in `tests/`. Run with `make test`. Coverage threshold: 80%.
Process entry points (`src/server.ts`, `src/cli.ts`) stay thin and are
excluded from coverage; put logic in modules the tests can import.

## Security

`make audit` runs `pnpm audit --audit-level=high`, failing on high or critical
advisories in the dependency tree. It is part of `make ci`, so it also runs on
every push and pull request.
