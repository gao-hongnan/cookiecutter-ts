import { buildApp } from './app.js';

const app = buildApp({ logger: true });

const start = async () => {
  try {
    const port = Number(process.env['PORT'] ?? 3000);
    await app.listen({ port, host: '0.0.0.0' });
  } catch (err) {
    app.log.error(err);
    process.exit(1);
  }
};

const shutdown = async (signal: NodeJS.Signals) => {
  app.log.info({ signal }, 'shutting down');
  await app.close();
  process.exit(0);
};

process.once('SIGTERM', signal => void shutdown(signal));
process.once('SIGINT', signal => void shutdown(signal));

void start();
