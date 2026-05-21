import { describe, expect, it, vi } from 'vitest';
import { VERSION, hello } from '../src/index.js';

describe('hello', () => {
  it('returns greeting with name', () => {
    expect(hello('World')).toBe('Hello, World!');
  });

  it('returns greeting with empty string', () => {
    expect(hello('')).toBe('Hello, !');
  });

  it.each([
    ['Alice', 'Hello, Alice!'],
    ['Bob', 'Hello, Bob!'],
    ['TypeScript', 'Hello, TypeScript!'],
  ])('hello(%s) === %s', (name, expected) => {
    expect(hello(name)).toBe(expected);
  });
});

describe('VERSION', () => {
  it('is a semver string', () => {
    expect(VERSION).toMatch(/^\d+\.\d+\.\d+/);
  });
});

describe('async example', () => {
  it('resolves a promise', async () => {
    const result = await Promise.resolve(hello('async'));
    expect(result).toBe('Hello, async!');
  });
});

describe('mock example', () => {
  it('can spy on a function', () => {
    const spy = vi.fn(hello);
    spy('spy');
    expect(spy).toHaveBeenCalledWith('spy');
    expect(spy).toHaveReturnedWith('Hello, spy!');
  });
});
