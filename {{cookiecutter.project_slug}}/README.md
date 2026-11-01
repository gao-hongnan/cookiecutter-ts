# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Installation

```bash
pnpm add {{ cookiecutter.project_slug }}
```

## Usage

```typescript
import { hello } from '{{ cookiecutter.project_slug }}';

console.log(hello('World')); // Hello, World!
```
{%- if cookiecutter.use_cli %}

### CLI

```bash
pnpm dlx {{ cookiecutter.project_slug }} hello World
```
{%- endif %}

## Development

```bash
make install    # Install deps + set up git hooks
make test       # Run tests
make test-cov   # Run tests with coverage
make audit      # Audit dependencies for vulnerabilities
make ci         # Full CI pipeline
make build      # Build to dist/
```

Run `make help` to list every target.

## License

{{ cookiecutter.license }} © {{ cookiecutter.author_name }}
