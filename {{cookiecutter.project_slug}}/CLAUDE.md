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
make ci         # Full CI pipeline
make build      # Build to dist/
make clean      # Remove build artifacts
```

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
