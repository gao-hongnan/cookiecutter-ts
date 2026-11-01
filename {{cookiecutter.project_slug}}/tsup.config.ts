import { defineConfig } from 'tsup';

export default defineConfig([
  {
    entry: ['src/index.ts'],
    format: ['esm', 'cjs'],
    dts: true,
    sourcemap: true,
    clean: true,
    splitting: false,
    treeshake: true,
  },
{%- if cookiecutter.use_server or cookiecutter.use_cli %}
  {
    // Executables: ESM only, no type declarations.
    entry: [
{%- if cookiecutter.use_server %}
      'src/server.ts',
{%- endif %}
{%- if cookiecutter.use_cli %}
      'src/cli.ts',
{%- endif %}
    ],
    format: ['esm'],
    sourcemap: true,
    splitting: false,
    treeshake: true,
  },
{%- endif %}
]);
