import Fastify from 'fastify';

const fastify = Fastify({ logger: true });

fastify.get('/', async () => {
  return { name: '{{ cookiecutter.project_slug }}', version: '0.1.0' };
});

fastify.get('/health', async () => {
  return { status: 'ok' };
});

const start = async () => {
  try {
    const port = Number(process.env['PORT'] ?? 3000);
    await fastify.listen({ port, host: '0.0.0.0' });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

const shutdown = async () => {
  await fastify.close();
  process.exit(0);
};

process.on('SIGTERM', () => void shutdown());
process.on('SIGINT', () => void shutdown());

void start();
