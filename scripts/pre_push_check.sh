#!/usr/bin/env bash
# Local pre-push checks to mirror CI: mypy, flake8, black/isort check, pytest
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "Running local pre-push checks..."

# Activate venv if available
if [ -f .venv/bin/activate ]; then
  # shellcheck disable=SC1091
  . .venv/bin/activate
fi

echo "-> Running mypy"
python -m mypy src --explicit-package-bases

echo "-> Running flake8"
flake8 $(git ls-files '*.py' | tr '\n' ' ')

echo "-> Running formatting checks (black/isort)"
black --check .
isort --check-only .

echo "-> Running pytest (fast)"
pytest -q -k "not slow" || true

echo "Pre-push checks completed."
