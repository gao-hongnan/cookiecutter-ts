import { Command } from 'commander';
import { VERSION, hello } from './index.js';

export function createProgram(): Command {
  const program = new Command();

  program
    .name('{{ cookiecutter.project_slug }}')
    .description('{{ cookiecutter.project_description }}')
    .version(VERSION);

  program
    .command('hello <name>')
    .description('Say hello to someone')
    .action((name: string) => {
      console.log(hello(name));
    });

  return program;
}
