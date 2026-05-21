#!/usr/bin/env node
import { readdirSync, statSync } from 'fs';
import { join } from 'path';

const IGNORE = new Set([
  'node_modules',
  '.git',
  'dist',
  'coverage',
  '.turbo',
  '.next',
  'out',
  '.husky',
  '__pycache__',
]);

const depth = parseInt(process.argv[2] ?? '3', 10);

function tree(dir, prefix = '', level = 0) {
  if (level >= depth) return;
  const entries = readdirSync(dir)
    .filter(e => (!IGNORE.has(e) && !e.startsWith('.')) || e === '.env.sample')
    .sort();
  entries.forEach((entry, i) => {
    const isLast = i === entries.length - 1;
    const connector = isLast ? '└── ' : '├── ';
    console.log(prefix + connector + entry);
    const full = join(dir, entry);
    if (statSync(full).isDirectory()) {
      const newPrefix = prefix + (isLast ? '    ' : '│   ');
      tree(full, newPrefix, level + 1);
    }
  });
}

console.log('.');
tree('.');
