# Contributing to {{ cookiecutter.project_name }}

## Getting Started

1. Fork the repository
2. Clone your fork
3. Run `make install` to install dependencies and set up git hooks

## Development Workflow

```bash
make fix        # Fix lint/format issues
make typecheck  # Check types
make test       # Run tests
make ci         # Full CI check (run before opening a PR)
```

## Commit Messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/). Examples:

- `feat: add new export`
- `fix: handle edge case in hello()`
- `docs: update README`
- `chore: bump dependencies`

The `commit-msg` hook enforces this automatically.

## Pull Requests

1. Create a branch: `git checkout -b feat/your-feature`
2. Make changes, add tests
3. Run `make ci` and ensure it passes
4. Open a PR with a clear description

## Code Style

Enforced automatically by `ultracite` (oxlint + oxfmt). Run `make fix` to auto-fix.
