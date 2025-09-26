# 2) Setup and first run (macOS + zsh)

This project uses a local virtual environment `.venv` and pinned developer tools.

## Learning goals

- Create and activate a virtual environment
- Install developer tooling consistently
- Verify tests, linters, and type checks locally

## Create and activate the environment

```zsh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
```

## Install developer tools

```zsh
pip install -r requirements-dev.txt
```

This installs Black, isort, Flake8, Pylint, pytest (+cov, +pylint plugin), mypy, Bandit, pip‑audit, and pre‑commit.

## Verify everything

- Run tests with coverage: VS Code task “coverage” or:
  ```zsh
  pytest --cov=src --cov-report=term-missing
  ```
- Lint project files:
  ```zsh
  flake8 $(git ls-files '*.py' | tr '\n' ' ')
  pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
  ```
- Type check:
  ```zsh
  mypy src
  ```

If these pass, you’re ready.

## Try it (VS Code one-click)

- Run the task: Command Palette → “Run Task” → “setup: dev”. Then run “quality: all”.

## Check yourself

- Where is the interpreter selected in VS Code?
- Which command writes `coverage.xml` for Coverage Gutters?

---

Next: [Repository structure](./03-structure.md)
