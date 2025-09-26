.PHONY: fmt lint typecheck security qa ci

fmt:
	. .venv/bin/activate && black . && isort .

lint:
	. .venv/bin/activate && flake8 $(shell git ls-files '*.py' | tr '\n' ' ') && pylint -j 0 $(shell git ls-files '*.py' | tr '\n' ' ')

typecheck:
	. .venv/bin/activate && mypy answers/src practice/src

qa: fmt lint typecheck

security:
	. .venv/bin/activate && bandit -q -r answers/src practice/src -x tests
	. .venv/bin/activate && pip-audit -r requirements.txt || true

ci:
	. .venv/bin/activate && black --check . && isort --check-only . && flake8 $(shell git ls-files '*.py' | tr '\n' ' ') && pylint -j 0 $(shell git ls-files '*.py' | tr '\n' ' ') && mypy answers/src practice/src && bandit -q -r answers/src practice/src -x tests
