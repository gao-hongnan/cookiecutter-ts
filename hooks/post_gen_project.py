import json
import shutil
import subprocess
from pathlib import Path


def flag(value: str) -> bool:
    # Cookiecutter renders boolean variables as "True"/"False", while values
    # passed on the command line or from a replay file may be lowercase.
    return value.strip().lower() in {"true", "yes", "y", "1"}


USE_ZOD = flag("{{ cookiecutter.use_zod }}")
USE_SERVER = flag("{{ cookiecutter.use_server }}")
USE_DOCKER = flag("{{ cookiecutter.use_docker }}")
USE_PRISMA = flag("{{ cookiecutter.use_prisma }}")
USE_CLI = flag("{{ cookiecutter.use_cli }}")
USE_TYPEDOC = flag("{{ cookiecutter.use_typedoc }}")


def remove(path: str) -> None:
    p = Path(path)
    if p.is_dir():
        shutil.rmtree(p)
    elif p.exists():
        p.unlink()


def run(cmd: list[str], description: str) -> bool:
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ {description}")
        return True
    except FileNotFoundError as e:
        print(f"⚠ {description} failed (non-fatal): {e}")
        return False
    except subprocess.CalledProcessError as e:
        print(f"⚠ {description} failed (non-fatal): exit code {e.returncode}")
        output = (e.stderr or e.stdout or "").strip()
        if output:
            print("\n".join(f"    {line}" for line in output.splitlines()[-15:]))
        return False


def update_package_json() -> None:
    pkg_path = Path("package.json")
    pkg: dict = json.loads(pkg_path.read_text())

    deps: dict = pkg.setdefault("dependencies", {})
    dev_deps: dict = pkg.setdefault("devDependencies", {})
    scripts: dict = pkg.setdefault("scripts", {})

    if not USE_ZOD:
        deps.pop("zod", None)

    if USE_SERVER:
        deps["fastify"] = "^5.12.7"
        dev_deps["tsx"] = "^4.23.15"
        scripts["dev:server"] = "tsx watch src/server.ts"
        scripts["start"] = "node dist/server.js"

    if USE_CLI:
        deps["commander"] = "^15.0.0"
        pkg["bin"] = {"{{ cookiecutter.project_slug }}": "./dist/cli.js"}

    if USE_PRISMA:
        deps["@prisma/client"] = "^7.10.1"
        dev_deps["prisma"] = "^7.10.1"
        dev_deps["dotenv"] = "^18.0.9"
        scripts["db:push"] = "prisma db push"
        scripts["db:migrate"] = "prisma migrate dev"
        scripts["db:studio"] = "prisma studio"
        scripts["db:generate"] = "prisma generate"
        # The generated client lives in src/generated/ and is gitignored, so
        # typecheck and build need it regenerated after every fresh install.
        scripts["postinstall"] = "prisma generate"

    if USE_TYPEDOC:
        dev_deps["typedoc"] = "^0.28.20"
        scripts["docs:build"] = "typedoc"
        scripts["docs:serve"] = "pnpm dlx serve docs"

    # Keep dependency blocks sorted, as pnpm does, and drop an empty one
    pkg["dependencies"] = dict(sorted(deps.items()))
    pkg["devDependencies"] = dict(sorted(dev_deps.items()))
    if not deps:
        pkg.pop("dependencies")

    pkg_path.write_text(json.dumps(pkg, indent=2) + "\n")


def remove_conditional_files() -> None:
    if not USE_DOCKER:
        remove("environments")
        remove(".dockerignore")
        remove(".hadolint.yaml")

    if not USE_PRISMA:
        remove("prisma")
        remove("prisma.config.ts")

    if not USE_SERVER:
        remove("src/app.ts")
        remove("src/server.ts")
        remove("tests/server.test.ts")

    if not USE_CLI:
        remove("src/program.ts")
        remove("src/cli.ts")
        remove("tests/program.test.ts")

    if not USE_TYPEDOC:
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
