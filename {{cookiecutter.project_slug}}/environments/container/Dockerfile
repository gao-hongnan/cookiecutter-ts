# syntax=docker/dockerfile:1

# ── deps stage ────────────────────────────────────────────────────────────────
FROM node:{{ cookiecutter.node_version }}-alpine AS deps
WORKDIR /app
RUN corepack enable pnpm
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile --prod

# ── build stage ───────────────────────────────────────────────────────────────
FROM node:{{ cookiecutter.node_version }}-alpine AS build
WORKDIR /app
RUN corepack enable pnpm
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile
COPY . .
RUN pnpm run build

# ── runner stage ──────────────────────────────────────────────────────────────
FROM node:{{ cookiecutter.node_version }}-alpine AS runner
WORKDIR /app

RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 appuser

COPY --from=deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
COPY package.json ./

USER appuser

EXPOSE 3000
ENV NODE_ENV=production PORT=3000

CMD ["node", "dist/server.js"]
