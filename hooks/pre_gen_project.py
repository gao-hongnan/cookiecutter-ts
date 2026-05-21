import re
import sys


def validate_project_slug() -> None:
    slug = "{{ cookiecutter.project_slug }}"
    pattern = r"^[a-z0-9]+(?:-[a-z0-9]+)*$"
    if not re.match(pattern, slug):
        print(f"ERROR: project_slug '{slug}' is invalid.")
        print("Must be lowercase kebab-case: letters, digits, hyphens only (no leading/trailing hyphens).")
        sys.exit(1)


def validate_node_version() -> None:
    version = "{{ cookiecutter.node_version }}"
    allowed = {"20", "22"}
    if version not in allowed:
        print(f"ERROR: node_version '{version}' is not supported.")
        print(f"Allowed values: {sorted(allowed)}")
        sys.exit(1)


def validate_license() -> None:
    lic = "{{ cookiecutter.license }}"
    allowed = {"MIT", "Apache-2.0"}
    if lic not in allowed:
        print(f"ERROR: license '{lic}' is not supported.")
        print(f"Allowed values: {sorted(allowed)}")
        sys.exit(1)


if __name__ == "__main__":
    validate_project_slug()
    validate_node_version()
    validate_license()
