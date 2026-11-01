import { afterEach, describe, expect, it, vi } from 'vitest';
import { createProgram } from '../src/program.js';

afterEach(() => {
  vi.restoreAllMocks();
});

describe('hello command', () => {
  it('prints a greeting', async () => {
    const log = vi.spyOn(console, 'log').mockImplementation(() => {});
    await createProgram().parseAsync(['hello', 'World'], { from: 'user' });
    expect(log).toHaveBeenCalledWith('Hello, World!');
  });
});
