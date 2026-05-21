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

## Development

```bash
make install    # Install deps + set up git hooks
make test       # Run tests
make test-cov   # Run tests with coverage
make ci         # Full CI pipeline
make build      # Build to dist/
```

## License

{{ cookiecutter.license }} © {{ cookiecutter.author_name }}
