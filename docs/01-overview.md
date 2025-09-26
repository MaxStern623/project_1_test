# 1) Project overview

This repository is a tiny calculator written in Python, designed to teach you professional software practices: clean structure, tests, formatting, linting, typing, security, CI, and editor automation. The code is simple so you can focus on the process.

## Learning goals

You will learn to:
- Create and use a virtual environment (isolated dependencies)
- Format and lint code (Black, isort, Flake8, Pylint)
- Test with pytest and enforce 100% coverage for `src/`
- Add static typing with mypy
- Package and run a CLI (`calc`)
- Scan code and dependencies (Bandit, pip-audit, Dependabot)
- Use VS Code tasks and debug configurations effectively
- Run Continuous Integration (GitHub Actions)

By the end, you’ll be able to bootstrap and maintain a high‑quality Python repo.

## Try it (5 minutes)

1. Open a terminal in the repo root and create a venv:
	```zsh
	python3 -m venv .venv && . .venv/bin/activate && python -m pip install --upgrade pip
	```
2. Install the dev tools and run the tests:
	```zsh
	pip install -r requirements-dev.txt
	pytest -q
	```
3. Peek at the CLI without installing the package yet:
	```zsh
	python -m src.main add 2 3
	```

## Check yourself

- Can you explain why keeping code under `src/` is helpful?
- Which tools here check formatting vs. code quality vs. types?
- What does “100% coverage for src” mean in practice?

---

Next: [Setup and first run](./02-setup.md)
