# 7) CLI and packaging

We provide a console script `calc` and a Python module entry `src.main:main`.

## Learning goals
- Run the CLI both with and without installation
- Understand console script entry points
- Know where packaging metadata lives

- Packaging metadata: `[build-system]` and `[project]` in `pyproject.toml`
- Console entry point:
  ```toml
  [project.scripts]
  calc = "src.main:main"
  ```
- Explicit packages to include:
  ```toml
  [tool.setuptools]
  packages = ["src", "src.operations"]
  ```

## Install and use the CLI
```zsh
. .venv/bin/activate
pip install -e .
calc add 2 3
```

## Run without installing
```zsh
python -m src.main add 2 3
```

## Try it

1. Install editable mode and run `calc multiply 2 3`.
2. Add a new subcommand stub (e.g., `power`) in `src/main.py`, return a hardcoded value, and run it.
3. Add a small test in `tests/` exercising the CLI output with `capsys`.

## Check yourself

- What does `-e` (editable) change in your workflow?
- How does the console script name map to the Python function?

## Background
CLIs are the original UX for developers; packaging and entry points standardize how users discover commands.

## Across languages
Node has `bin` in package.json; Go builds binaries; Java exposes `main` classes via JARs.

## Career connection
Shipping usable tools—even tiny ones—demonstrates craftsmanship and empathy for developer experience.

---

Next: [Continuous Integration](./08-ci.md)
