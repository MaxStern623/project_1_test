# 4) Formatting, linting, and style

Quality tools help you keep a consistent, readable codebase.

## Learning goals
- Format code with Black and organize imports with isort
- Catch style issues with Flake8 and code smells with Pylint
- Understand how pre-commit speeds up local feedback

## Black (formatter)
- Config: `[tool.black]` in `pyproject.toml` (line length 100)
- Run: VS Code task “fmt” or `black .`

## isort (imports)
- Config: `[tool.isort]` profile "black"
- Run: `isort .` (included in “fmt” task)

## Flake8 (style linter)
- Config: `[tool.flake8]` in `pyproject.toml`
- Excludes `.venv`, `build`, etc.
- Run only on project files via Git: `flake8 $(git ls-files '*.py' | tr '\n' ' ')`

## Pylint (code linter)
- Config: `[tool.pylint]` in `pyproject.toml`
- Run: `pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')`

## Pre‑commit (fast local checks)
- Config: `.pre-commit-config.yaml`
- Install hooks: `pre-commit install`
- Run all: `pre-commit run --all-files`

## Try it

1. Introduce an unused import in `src/main.py` and run the “lint” task to see Pylint/Flake8 complaints. Remove it and rerun.
2. Mess up formatting (e.g., extra spaces, wrong quote styles) and run “fmt”; inspect the diff.
3. Install and run pre-commit:
	```zsh
	pre-commit install
	pre-commit run --all-files
	```

## Check yourself

- Which tool auto-fixes vs. which only reports?
- Why do we use `git ls-files` when running linters?

## Background
Linters originated to find likely bugs before runtime; formatters remove style debates from code review.

## Across languages
Prettier/ESLint (JS/TS), gofmt/golangci-lint (Go), Spotless/Checkstyle (Java) play similar roles.

## Career connection
Clean diffs and consistent style speed up reviews, making you more effective on any team.

---

Next: [Testing and coverage](./05-testing.md)
