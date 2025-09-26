# 9) VS Code configuration and tasks

## Learning goals
- Select the correct interpreter and run tasks
- Use Coverage Gutters to visualize untested lines
- Debug both the CLI and tests with breakpoints
## Settings
- File: `.vscode/settings.json`
- Select interpreter: `.venv/bin/python`
- Pytest enabled; format on save via Black; organize imports; Coverage Gutters reads `coverage.xml`.

## Tasks (Command Palette → Run Task)
- venv: create
- venv: pip upgrade
- install: dev tools
- fmt (Black + isort)
- lint (Flake8 + Pylint on Git‑tracked files)
- coverage (pytest with coverage)
- typecheck (mypy)
- security (make security)
- pre‑commit: all‑files
- quality: all (runs fmt → lint → typecheck → coverage → security)

## Debugging
- File: `.vscode/launch.json` (debugpy)
- Examples:
  - Debug calc CLI (add)
  - Debug calc CLI (divide‑by‑zero)
  - Pytest: Debug tests (prompts for -k filter)

## Try it

1. Select interpreter `.venv/bin/python` (bottom-right) and run “quality: all”.
2. Run “coverage”, open a file in `src/`, and toggle Coverage Gutters to see green/red lines.
3. Set a breakpoint in `src/main.py` and start “Debug calc CLI (add)”; inspect variables.

## Check yourself

- Where are tasks defined and how do you add a new one?
- How do you pass arguments to a debug configuration?

## Background
Editor automation (tasks, code actions, debuggers) shortens feedback loops and reduces manual toil.

## Across languages
Every stack benefits from good editor integration—launch configs, linters on save, and test runners.

## Career connection
Proficiency with your tools multiplies impact; teams value engineers who speed up common workflows.

---

Next: [Security and dependency health](./10-security.md)
