# 5) Testing and coverage

We use pytest with coverage and enforce 100% for `src/`.

## Learning goals
- Run and filter tests
- Measure and interpret coverage
- Write parametrized tests and exception tests

- Config: `pytest.ini`
  - `addopts = --cov=src --pylint --cov-report=term-missing --cov-fail-under=100 -q -ra`
  - `testpaths = tests`

## Run tests
```zsh
pytest -q
```

## Coverage report
```zsh
pytest --cov=src --cov-report=term-missing --cov-report=xml
```
- Writes `coverage.xml` for the Coverage Gutters VS Code extension.

## Writing tests
- Name files `test_*.py`, functions `test_*`.
- Use `pytest.raises` for exceptions.
- Parametrize with `@pytest.mark.parametrize`.

## Try it

1. Add a parametrized test for `add` with positive and negative numbers.
2. Add a test that ensures `divide(x, 0)` raises `ValueError`.
3. Run `pytest --cov=src --cov-report=term-missing` and identify any missing lines.

## Check yourself

- What is the difference between xfail and skip?
- Where is the coverage threshold enforced?

## Background
Unit testing grew alongside iterative development to reduce the cost of change. Pytest focuses on readability and minimal boilerplate, making tests faster to write and run.

## Across languages
JS/TS has Jest/Vitest; Go has `go test`; Java has JUnit. All aim for fast feedback with assertions and fixtures.

## Career connection
Being able to write clear, fast tests and read coverage reports is table stakes for most software roles and a differentiator in interviews.

---

Next: [Static typing with mypy](./06-typing.md)
