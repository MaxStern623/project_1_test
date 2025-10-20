# Recreate this Defensive-Programming Project

This document describes the architecture of the project and gives step-by-step instructions so you (or someone else) can recreate the repository from scratch. Each section explains what to create, why it's needed, what should happen, and concrete steps or commands to complete it.

Keep this guide next to the code (for example in `docs/RECREATE_PROJECT.md`) so maintainers and students can rebuild or fork the project reliably.

## High-level overview

- Purpose: a small Python teaching project that demonstrates defensive programming: custom exceptions, guarded arithmetic operations, a CLI, examples, reference solutions, tests, linting, type checking, and CI.
- Audience: instructors, students, maintainers who want a runnable student-skeleton (`src/`) plus a runnable reference implementation (`complete_solutions/`) and educational snippets (`resources/examples/`).

## Desired repository layout

```
README.md
pyproject.toml
requirements.txt
requirements-dev.txt
.pre-commit-config.yaml
.flake8
.pylintrc
docs/
  RECREATE_PROJECT.md
  INDEX.md
src/
  __init__.py
  main.py          # student CLI skeleton
  exceptions.py    # student exceptions skeleton
  operations/
    __init__.py    # student operations skeleton
tests/
  test_cli.py
  test_operations.py
  test_exceptions.py
complete_solutions/
  main.py          # runnable reference implementation
  exceptions.py
  operations/
    __init__.py
resources/
  examples/        # small, focused examples
tools/
  grade_from_junit.py
scripts/
  install_hooks.sh
  pre_push_check.sh
```

## Contract / design goals (quick)

- Inputs/outputs: CLI receives two operands (strings) and an operation; operations accept numeric operands and return numeric results or raise typed exceptions.
- Error modes: invalid input (exit code 1), math errors like division-by-zero (exit code 2), other calculator-level errors (exit code 3), unexpected internal errors (exit code 4).
- Quality gates: format (black/isort), lint (flake8, pylint), types (mypy), tests (pytest), pre-commit hooks and GitHub Actions.

## 1. Initialize the repo

What to do
- Create a new git repository and an initial commit.

Why
- Version control and CI require a git repo.

How

```bash
git init project_name
cd project_name
git remote add origin <your-remote-url>
```

Add a small README and commit.

## 2. Create the Python project files

What to do
- Create `pyproject.toml` for build tool + black/isort config, `requirements.txt` and `requirements-dev.txt` (dev tools: pytest, black, isort, flake8, pylint, mypy, pre-commit, pytest-cov), and an initial `src/` package with skeleton files.

Why
- Centralized configuration and reproducible dev environment.

How

1. `pyproject.toml` minimal example (black/isort):

```toml
[tool.black]
line-length = 100

[tool.isort]
profile = "black"
```

2. `requirements-dev.txt` should list dev dependencies. Example:

```
pytest
black
isort
flake8
pylint
mypy
pre-commit
pytest-cov
```

3. Create `src/__init__.py`, `src/main.py` (skeleton), `src/exceptions.py` (skeleton), and `src/operations/__init__.py` (skeleton). Keep TODO markers in student files.

## 3. Implement the reference solution (`complete_solutions/`)

What to do
- Create a runnable reference implementation that fully implements behavior expected by tests.

Why
- Instructors/maintainers can run a working implementation. Students use `src/` as practice; CI and graders can run `complete_solutions/` when comparing behavior.

How (files & responsibilities)

- `complete_solutions/exceptions.py` — implement:
  - `CalculatorError(Exception)` base class storing `message` and optional `context` dict.
  - `InvalidInputError`, `DivisionByZeroError`, `OverflowError`, `UnderflowError` each inheriting from `CalculatorError`.

- `complete_solutions/operations/__init__.py` — implement:
  - `_validate_input(value, param_name)` that ensures operands are int/float, not NaN or infinite; raises `InvalidInputError` with context on failure.
  - `_check_overflow(result, operation, a, b)` that checks for infinite results and suspicious underflow; raises `OverflowError` or `UnderflowError`.
  - `add(a,b)`, `subtract(a,b)`, `multiply(a,b)`, `divide(a,b)` implementing guard clauses, EAFP around arithmetics, postcondition checks, maintaining type consistency (return int when both inputs int and result integral), and specific division-by-zero handling raising `DivisionByZeroError`.

- `complete_solutions/main.py` — implement the CLI:
  - `build_parser()` to create argparse subcommands for `add`, `subtract`, `multiply`, `divide` and a global `--verbose` flag.
  - `validate_operation_args(a, b)` to parse strings into floats and reject NaN/inf.
  - `execute_operation(cmd, a, b)` that maps command names to functions and wraps unexpected errors into `InvalidInputError`.
  - `main(argv=None)` that wires parsing, logging, execution, prints outputs in formats expected by tests (integers vs floats, `2.0` for division results when integral), and returns correct exit codes.

Tip: Keep `complete_solutions` importable as a package (use package-qualified imports inside it) so linters and local runs don't produce import errors.

## 4. Create small, focused examples (`resources/examples/`)

What to do
- Add short scripts (10–50 lines) demonstrating a concept: guard clauses, EAFP vs LBYL, logging patterns, exception hierarchy, input validation.

Why
- Provide learning artifacts without shipping full solutions in the `src` folder.

How
- Keep these small and idempotent. Run `black` on them; add short README in `resources/examples/` describing each example's purpose.

## 5. Tests and TDD

What to do
- Add `tests/` with pytest tests that describe the expected behavior for `src/` implementations (these form the student spec).

Why
- Tests drive what students must implement; the reference solution must pass them.

How
- `tests/test_operations.py` — unit tests for `add`, `subtract`, `multiply`, `divide` covering normal cases and edge cases (zero, one, NaN/inf, overflow/underflow, negative numbers, scientific notation).
- `tests/test_exceptions.py` — ensure exceptions have correct types and context attributes.
- `tests/test_cli.py` — run `main()` with argument lists using a helper that captures stdout/stderr and asserts exit codes and output formats.

TDD suggestion: implement a failing test in `tests/` first, then implement minimal change in `complete_solutions/` or `src/` (depending on instructor intention) to pass it.

## 6. Development tools & quality gates

What to do
- Configure and enable pre-commit hooks, black, isort, flake8, pylint, mypy, pytest, and coverage.

Why
- Ensure consistent style, early detection of errors, and enforceable quality for students and CI.

How

1. Add `.pre-commit-config.yaml` with hooks for black, isort, flake8 and run `pre-commit install` or provide `scripts/install_hooks.sh`:

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
```

2. Create `.flake8` to explicitly set `max-line-length = 100` and ignores required for your environment.

3. Create `.pylintrc` tuned for the teaching repo (you may suppress certain warnings or exclude `complete_solutions/` and `resources/examples/` so pylint focuses on `src/`).

4. Configure `mypy` via `pyproject.toml` or a `mypy.ini` and ensure `src` is type-checked with `--explicit-package-bases` if using namespace packages. Try to keep type hints minimal in student skeletons but complete in `complete_solutions`.

5. Add `pytest.ini` and use `pytest -q --junitxml=reports/junit.xml --cov=src --cov-report=xml:reports/coverage.xml` in CI to generate coverage/junit artifacts.

## 7. CI (GitHub Actions) configuration

What to do
- Add `.github/workflows/ci.yml` that runs the quality gates on push/PR across a matrix of Python versions (choose at least 3.11 and 3.12 if you want newer coverage).

Why
- Automate checks and ensure reproducible verification on pull requests and merges.

How (steps inside the workflow)

- checkout
- set up python
- install dependencies from `requirements-dev.txt`
- run `pre-commit run --all-files` or run black/isort/flake8 separately (fast path)
- run `mypy` (optional strictness depending on teaching goals)
- run `pytest` with junit/coverage outputs
- optional: run `tools/grade_from_junit.py` to produce grading summaries
- upload artifacts (junit/coverage) and fail on test/lint failures

Example matrix snippet in workflow:

```yaml
matrix:
  python-version: [3.11, 3.12]
```

## 8. Grading tool and automation

What to do
- Add a `tools/grade_from_junit.py` script that reads `reports/junit.xml` and produces a small JSON summary `reports/grade_summary.json`.

Why
- Instructors often want to aggregate test results and give a simple grade or pass/fail summary.

How
- Use Python's `xml.etree.ElementTree` to parse `junit.xml`, count failures/skips/errors, and produce a minimal JSON with fields: tests, failures, errors, skipped, passed.

## 9. Scripts and developer convenience

What to do
- Provide `scripts/install_hooks.sh`, `scripts/pre_push_check.sh` that run pre-commit or the full quality pipeline locally.

Why
- Makes it easy for students to check locally before pushing.

How

`install_hooks.sh`:
```bash
#!/usr/bin/env bash
python -m venv .venv || true
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
pre-commit install
```

`pre_push_check.sh`:
```bash
. .venv/bin/activate
pre-commit run --all-files
pytest -q
```

## 10. Documentation and onboarding (docs/)

What to do
- Include `docs/INDEX.md`, `docs/RECREATE_PROJECT.md` (this file), a short `LEARNING_GUIDE.md`, and a `COMPLETE_SOLUTIONS.md` pointing to the reference.

Why
- Onboarding new students or maintainers is faster when everything is documented.

How
- Keep `docs/INDEX.md` as the landing page linking to the learning guide, example list, and the recreate instructions.

## 11. Release & packaging (optional)

What to do
- If you want to package for pip or internal distribution, create a `setup.cfg`/`pyproject.toml` with metadata and a simple `setup.py` or rely on PEP 517.

Why
- Makes the project easy to install into an environment for automated graders or CI caching.

How
- Keep packaging minimal; prefer editable installs in CI with `pip install -e .` if needed.

## 12. Checklist to verify everything works

1. Create venv and install dev dependencies.
2. Run `pre-commit run --all-files` and fix formatting issues.
3. Run `flake8` and address warnings (or tune `.flake8`).
4. Run `pylint` for targeted folders (or tune `.pylintrc`).
5. Run `mypy src --explicit-package-bases`.
6. Run `pytest -q` and ensure tests behave as expected.
7. Run `pytest --junitxml=reports/junit.xml --cov=src --cov-report=xml:reports/coverage.xml` and verify artifacts.
8. Push to remote and ensure GitHub Actions completes successfully.

## Edge cases & gotchas

- flake8 sometimes uses a different config source than black/isort; adding a top-level `.flake8` ensures deterministic behavior in CI and pre-commit.
- Pylint is very noisy for educational repos; it's common to configure `.pylintrc` to ignore `complete_solutions` or to selectively disable categories (e.g., TODO warnings, unused-argument in tests).
- Be careful with argparse and operands that look like options (for example `-inf`). If you accept raw argv lists in tests, preprocess and insert `--` when needed or design tests to pass `argv` in a way argparse expects.

## Minimal reproduction commands

These commands assume a Unix-like shell and Python 3.11+ installed.

```bash
# create project and venv
git clone <repo>
cd project_1_test
python3 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt

# run formatting and tests
pre-commit run --all-files
pytest -q
```

## Final notes & recommended workflow

- Keep `src/` as the student-facing skeleton. Keep `complete_solutions/` as a runnable reference but consider excluding it from some linters so students see only relevant lint errors.
- Use `resources/examples/` for short teaching snippets — they are not full solutions.
- Automate quality gates in CI so PRs fail fast when tests or linters complain.

If you want, I can also:
- produce the initial `pyproject.toml`, `.pre-commit-config.yaml`, `.flake8`, and `.pylintrc` templates for you to drop into a fresh repository;
- generate a starter `complete_solutions` implementation (fully working) or a skeleton `src/` for students.

Good luck — tell me which artifact you want created next and I will generate it.
