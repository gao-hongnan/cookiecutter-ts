import json
import shutil
import subprocess
from pathlib import Path


def remove(path: str) -> None:
    p = Path(path)
    if p.is_dir():
        shutil.rmtree(p)
    elif p.exists():
        p.unlink()


def run(cmd: list[str], description: str) -> bool:
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"✓ {description}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"⚠ {description} failed (non-fatal): {e}")
        return False


def update_package_json() -> None:
    use_zod = "{{ cookiecutter.use_zod }}" == "true"
    use_server = "{{ cookiecutter.use_server }}" == "true"
    use_cli = "{{ cookiecutter.use_cli }}" == "true"
    use_prisma = "{{ cookiecutter.use_prisma }}" == "true"
    use_typedoc = "{{ cookiecutter.use_typedoc }}" == "true"

    pkg_path = Path("package.json")
    pkg: dict = json.loads(pkg_path.read_text())

    deps: dict = pkg.setdefault("dependencies", {})
    dev_deps: dict = pkg.setdefault("devDependencies", {})
    scripts: dict = pkg.setdefault("scripts", {})

    if not use_zod:
        deps.pop("zod", None)

    if use_server:
        deps["fastify"] = "^5.0.0"
        dev_deps["tsx"] = "^4.0.0"
        scripts["dev:server"] = "tsx watch src/server.ts"
        scripts["start"] = "node dist/server.js"

    if use_cli:
        deps["commander"] = "^13.0.0"

    if use_prisma:
        deps["@prisma/client"] = "^6.0.0"
        dev_deps["prisma"] = "^6.0.0"
        scripts["db:push"] = "prisma db push"
        scripts["db:migrate"] = "prisma migrate dev"
        scripts["db:studio"] = "prisma studio"
        scripts["db:generate"] = "prisma generate"

    if use_typedoc:
        dev_deps["typedoc"] = "^0.28.0"
        scripts["docs:build"] = "typedoc src/index.ts --out docs"
        scripts["docs:serve"] = "npx serve docs"

    # Remove empty dependencies block if no runtime deps
    if not deps:
        pkg.pop("dependencies", None)

    pkg_path.write_text(json.dumps(pkg, indent=2) + "\n")


def remove_conditional_files() -> None:
    use_docker = "{{ cookiecutter.use_docker }}" == "true"
    use_prisma = "{{ cookiecutter.use_prisma }}" == "true"
    use_server = "{{ cookiecutter.use_server }}" == "true"
    use_cli = "{{ cookiecutter.use_cli }}" == "true"
    use_typedoc = "{{ cookiecutter.use_typedoc }}" == "true"

    if not use_docker:
        remove("environments")
        remove(".dockerignore")
        remove(".hadolint.yaml")

    if not use_prisma:
        remove("prisma")

    if not use_server:
        remove("src/server.ts")
        remove("tests/server.test.ts")

    if not use_cli:
        remove("src/cli.ts")

    if not use_typedoc:
        remove("typedoc.json")


def init_project() -> None:
    run(["git", "init"], "git init")

    pnpm_ok = run(["pnpm", "install"], "pnpm install")
    if pnpm_ok:
        run(["pnpm", "run", "prepare"], "husky setup")
        run(["pnpm", "run", "fix"], "format code")

    run(["git", "add", "-A"], "git add")
    run(
        ["git", "commit", "--no-verify", "-m", "chore: initial commit from cookiecutter-ts"],
        "initial commit",
    )


def print_next_steps() -> None:
    slug = "{{ cookiecutter.project_slug }}"
    print(f"\n{'=' * 60}")
    print(f"  Project '{slug}' created successfully!")
    print(f"{'=' * 60}")
    print("\nNext steps:")
    print("  1. cp .env.sample .env        # Configure environment variables")
    print("  2. make ci                    # Verify everything works")
    print("  3. git remote add origin ...  # Push to GitHub")
    print()


if __name__ == "__main__":
    update_package_json()
    remove_conditional_files()
    init_project()
    print_next_steps()
