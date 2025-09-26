#!/usr/bin/env bash
# Bootstrap VS Code + Python quality toolchain for a repo (macOS/Linux).
# Creates .vscode configs, pyproject.toml (Black/isort/Flake8/Pylint),
# pre-commit hooks, Makefile, GitHub Actions workflow, venv, and first pass.
# Safe defaults; no brittle env vars; consistent versions; zero known config footguns.

set -euo pipefail

# -------- Settings (tweak as needed) ------------------------------------------
PY_VERSION="3.11"              # Target Python for tooling/configs
LINE_LENGTH="100"              # Shared line length for Black/Flake8/Pylint/isort
PKG_UNDER_TEST="src"           # Used by coverage tasks; set to your top-level package/module
TEST_DIR="tests"               # Pytest discovery dir
USE_BLACK_PREVIEW=true         # Black 'preview' flag; boolean TOML literal

# -------- Helpers --------------------------------------------------------------
say()  { printf "\033[1;32m%s\033[0m\n" "$*"; }
warn() { printf "\033[1;33m%s\033[0m\n" "$*"; }
err()  { printf "\033[1;31m%s\033[0m\n" "$*" >&2; }

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || { err "Missing required command: $1"; exit 1; }
}

# -------- Pre-flight -----------------------------------------------------------
require_cmd python3
require_cmd git

if [[ ! -d .git ]]; then
  warn "No .git repo found. Initializing a new one."
  git init
else
  say "Git repo detected."
fi

mkdir -p .vscode .github/workflows scripts

# -------- Virtualenv -----------------------------------------------------------
if [[ ! -d .venv ]]; then
  say "Creating virtualenv (.venv)..."
  python3 -m venv .venv
else
  say "Using existing .venv"
fi

# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip wheel

# -------- Dev tools (pinned where appropriate) --------------------------------
TOOLS=(black isort flake8 pylint pytest pytest-cov debugpy pre-commit)
say "Installing dev tools: ${TOOLS[*]}"
pip install "${TOOLS[@]}"

# -------- requirements-dev.txt ------------------------------------------------
say "Writing requirements-dev.txt"
cat > requirements-dev.txt <<'TXT'
black==24.8.0
isort==5.13.2
flake8==7.1.1
pylint==3.2.6
pytest>=8.2
pytest-cov>=5.0
pytest-pylint>=0.21
debugpy>=1.8
pre-commit>=3.7
# Flake8 plugins (installed to match config behavior)
flake8-bugbear>=24.2
flake8-comprehensions>=3.14
TXT

# -------- pyproject.toml ------------------------------------------------------
# Notes:
# - Pylint reads [tool.pylint] from pyproject.toml (modern, correct).
# - We avoid brittle 'select' overrides for Flake8 to prevent code mismatch.
# - 'preview' is a real Black key; boolean value inserted from $USE_BLACK_PREVIEW.
PY_COMPACT="py${PY_VERSION/./}"
say "Writing pyproject.toml"
cat > pyproject.toml <<TOML
[tool.black]
line-length = ${LINE_LENGTH}
target-version = ["${PY_COMPACT}"]
preview = ${USE_BLACK_PREVIEW}

[tool.isort]
profile = "black"
line_length = ${LINE_LENGTH}
combine_as_imports = true

[tool.flake8]
max-line-length = ${LINE_LENGTH}
extend-ignore = [
  "E203",  # Black compatibility (whitespace before :)
  "W503"   # Line-break before binary operator (Black-compatible style)
]
per-file-ignores = [
  "__init__.py:F401",  # allow package re-exports
]
# Plugins installed (bugbear/comprehensions) will contribute additional checks automatically.

[tool.pylint]
py-version = "${PY_VERSION}"
ignore-paths = ["tests/"]               # treat tests as leafs; adjust if needed
max-line-length = ${LINE_LENGTH}
good-names = ["i","j","k","x","y","z","df","id"]
min-similarity-lines = 6
# Gradual tuning example:
# disable = ["missing-module-docstring","missing-class-docstring","missing-function-docstring"]
TOML

# -------- .env ----------------------------------------------------------------
# Do NOT include editor vars like ${workspaceFolder} here; they won't expand.
say "Writing .env"
cat > .env <<'ENV'
# Keep minimal. Add app-specific env here if needed.
ENV=dev
# FLASK_APP=app.py
# DJANGO_SETTINGS_MODULE=project.settings
ENV

# -------- VS Code: settings.json ----------------------------------------------
say "Writing .vscode/settings.json"
cat > .vscode/settings.json <<JSON
{
  // Python env & analysis
  "python.defaultInterpreterPath": "\${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "python.analysis.typeCheckingMode": "basic",
  "python.envFile": "\${workspaceFolder}/.env",

  // Testing
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["-q", "${TEST_DIR}"],

  // Formatting & imports
  "editor.formatOnSave": true,
  "python.formatting.provider": "black",
  "editor.codeActionsOnSave": { "source.organizeImports": "explicit" },

  // Debugger ergonomics
  "debug.inlineValues": true,
  "debug.showBreakpointsInOverviewRuler": true,
  "debug.openDebug": "openOnSessionStart",
  "python.logging.level": "warning",

  // Lint integration (non-blocking in editor)
  "flake8.args": ["--max-line-length=${LINE_LENGTH}"],
  "pylint.args": ["--output-format=colorized"],

  // Coverage Gutters (install the extension)
  "coverage-gutters.showLineCoverage": true,
  "coverage-gutters.highlight": true,

  // File hygiene
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true
}
JSON

# -------- VS Code: launch.json ------------------------------------------------
say "Writing .vscode/launch.json"
cat > .vscode/launch.json <<'JSON'
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: Module",
      "type": "python",
      "request": "launch",
      "module": "mypkg.cli",
      "args": [],
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Pytest: Debug tests",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": ["-q", "tests", "-k", "${input:testFilter}"],
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Flask: Debug",
      "type": "python",
      "request": "launch",
      "module": "flask",
      "envFile": "${workspaceFolder}/.env",
      "env": { "FLASK_ENV": "development", "FLASK_APP": "app.py" },
      "args": ["run", "--no-debugger", "--reload"],
      "jinja": true,
      "justMyCode": true
    },
    {
      "name": "FastAPI (uvicorn)",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["app:app", "--reload"],
      "envFile": "${workspaceFolder}/.env",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver", "0.0.0.0:8000"],
      "django": true,
      "envFile": "${workspaceFolder}/.env",
      "justMyCode": true
    },
    {
      "name": "Attach: debugpy 5678",
      "type": "python",
      "request": "attach",
      "connect": { "host": "localhost", "port": 5678 },
      "justMyCode": false
    }
  ],
  "inputs": [
    {
      "id": "testFilter",
      "type": "promptString",
      "description": "Pytest -k expression (optional)",
      "default": ""
    }
  ]
}
JSON

# -------- VS Code: tasks.json -------------------------------------------------
say "Writing .vscode/tasks.json"
cat > .vscode/tasks.json <<JSON
{
  "version": "2.0.0",
  "tasks": [
    { "label": "venv: create", "type": "shell", "command": "python3 -m venv .venv" },
    { "label": "venv: pip upgrade", "type": "shell", "command": ". .venv/bin/activate && pip install --upgrade pip" },
    { "label": "install: dev tools", "type": "shell", "command": ". .venv/bin/activate && pip install -r requirements-dev.txt" },
    { "label": "fmt", "type": "shell", "command": ". .venv/bin/activate && black . && isort ." },
    { "label": "lint", "type": "shell", "command": ". .venv/bin/activate && flake8 . && pylint -j 0 $(git ls-files '*.py' | tr '\\n' ' ')" },
    { "label": "test", "type": "shell", "command": ". .venv/bin/activate && pytest -q" },
    {
      "label": "coverage",
      "type": "shell",
      "command": ". .venv/bin/activate && pytest --cov=${PKG_UNDER_TEST} --cov-report=xml --cov-report=term",
      "problemMatcher": []
    },
    {
      "label": "coverage: gutters refresh",
      "type": "shell",
      "command": "echo 'Reload coverage.xml in Coverage Gutters'",
      "problemMatcher": []
    }
  ]
}
JSON

# -------- pre-commit: format+lint (fast, consistent) --------------------------
# Note: We include Flake8 + plugins here. Pylint is intentionally left to CI and 'make lint'
# for speed and to avoid import/env issues in pre-commit isolated environments.
say "Writing .pre-commit-config.yaml"
cat > .pre-commit-config.yaml <<'YAML'
repos:
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 7.1.1
    hooks:
      - id: flake8
        additional_dependencies:
          - flake8-bugbear>=24.2
          - flake8-comprehensions>=3.14
YAML

# -------- Makefile ------------------------------------------------------------
say "Writing Makefile"
cat > Makefile <<'MAKE'
.PHONY: fmt lint qa ci

fmt:
	. .venv/bin/activate && black . && isort .

lint:
	. .venv/bin/activate && flake8 . && pylint -j 0 $(shell git ls-files '*.py' | tr '\n' ' ')

qa: fmt lint

ci:
	. .venv/bin/activate && black --check . && isort --check-only . && flake8 . && pylint -j 0 $(shell git ls-files '*.py' | tr '\n' ' ')
MAKE

# -------- GitHub Actions (enforce on PRs) -------------------------------------
say "Writing .github/workflows/quality.yml"
cat > .github/workflows/quality.yml <<'YAML'
name: Quality
on:
  pull_request:
  push:
    branches: [ main, master ]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Cache pip
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: pip-${{ runner.os }}-${{ hashFiles('**/requirements-dev.txt', '**/pyproject.toml') }}

      - name: Install tooling
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-dev.txt

      - name: Verify format (Black/isort) + Lint (Flake8/Pylint)
        run: |
          black --check .
          isort --check-only .
          flake8 .
          pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
YAML

# -------- First pass & hooks ---------------------------------------------------
say "Running first format (Black/isort)..."
black .
isort .

say "Installing pre-commit hooks..."
pre-commit install

say "Running initial pre-commit on all files..."
# Don't fail the whole script on first run (lets you inspect), but surface output.
pre-commit run --all-files || true

# -------- Final notes ----------------------------------------------------------
say "Done."
say "Open in VS Code and select the interpreter: .venv/bin/python"
say "Update PKG_UNDER_TEST in this script (and re-run) or adjust .vscode/tasks.json for coverage."
warn "If you need Windows support, use WSL or adapt activate path (.venv\\Scripts\\activate)."
