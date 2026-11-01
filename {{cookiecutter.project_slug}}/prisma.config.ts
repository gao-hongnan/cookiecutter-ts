import 'dotenv/config';
import { defineConfig } from 'prisma/config';

export default defineConfig({
  schema: 'prisma/schema.prisma',
  migrations: {
    path: 'prisma/migrations',
  },
  datasource: {
    // `prisma generate` never connects, so fresh clones and CI can install
    // without a .env; migrate/push use DATABASE_URL when it is set.
    url: process.env['DATABASE_URL'] ?? 'file:./dev.db',
  },
});
