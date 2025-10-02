.PHONY: fmt lint typecheck security qa ci

fmt:
	. .venv/bin/activate && black . && isort .

lint:
	. .venv/bin/activate && flake8 $(shell git ls-files '*.py' | tr '\n' ' ') && pylint -j 0 $(shell git ls-files '*.py' | tr '\n' ' ')

typecheck:
	. .venv/bin/activate && mypy src --explicit-package-bases

qa: fmt lint typecheck

security:
	. .venv/bin/activate && bandit -q -r src -x tests -s B101
	. .venv/bin/activate && pip-audit -r requirements.txt || true

ci:
	. .venv/bin/activate && black --check . && isort --check-only . && flake8 $(shell git ls-files '*.py' | tr '\n' ' ') && pylint -j 0 $(shell git ls-files '*.py' | tr '\n' ' ') && mypy src --explicit-package-bases && bandit -q -r src -x tests -s B101
