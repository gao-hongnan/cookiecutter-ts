import Fastify, { type FastifyInstance, type FastifyServerOptions } from 'fastify';
import { VERSION } from './index.js';

export function buildApp(options: FastifyServerOptions = {}): FastifyInstance {
  const app = Fastify(options);

  app.get('/', async () => ({ name: '{{ cookiecutter.project_slug }}', version: VERSION }));

  app.get('/health', async () => ({ status: 'ok' }));

  return app;
}
