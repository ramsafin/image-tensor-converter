# Python Project Template

> One-sentence description of what this project does and why it exists.

---

## Features

- Modern Python packaging with [`pyproject.toml`](pyproject.toml)
- [`src/`](src/) layout (safe imports, scalable structure)
- Conda-based reproducible environment
- Testing with `pytest`
- Linting & formatting with `ruff`
- Pre-commit hooks for consistent code quality

---

## Getting Started

### 1. Clone the repository

```shell
git clone <repo-url>
cd <repo-name>
```

### 2. Create and activate the Conda environment

> Modify the environment name in [`environment.yml`](environment.yml).

```shell
conda env create -f environment.yml
conda activate <env-name>
```

### 3. Install the project (editable mode)

```shell
pip install -e ".[dev]"
```

This installs:
- the project itself
- development dependencies (`pytest`, `ruff`, `pre-commit`, etc.)

### 4. Enable pre-commit hooks

```shell
pre-commit install
```

Optional, but recommended for existing files:

```shell
pre-commit run --all-files
```

## Running Tests

```shell
pytest
```

## Linting and Formatting

```shell
pyright

ruff check .
ruff format .
```

## Package Name

The Python package lives in [`src/package_name`](src/package_name/).

If you cloned this from a template, remember to:
- rename the package directory
- update imports
- update the project name in [`pyproject.toml`](pyproject.toml)

## Developer Notes

- Dependencies are declared in [`pyproject.toml`](pyproject.toml)
- The Conda environment manages Python and system libraries
- Do not duplicate dependencies in [`environment.yml`](environment.yml)

## License

This project is licensed under the [MIT License](LICENSE).
