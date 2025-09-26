# 12) Troubleshooting

- ModuleNotFoundError: Ensure you run from repo root and venv is active. For CLI, `pip install -e .` then run `calc ...`.
- Flake8 errors from site‑packages: Our configs run Flake8 only on Git‑tracked files; use the provided task/commands.
- Coverage not 100%: Run `pytest --cov=src --cov-report=term-missing`; add tests for uncovered lines.
- Pylint import errors: Ensure venv active; run from repo root; install dev tools.
- VS Code uses wrong interpreter: Select `.venv/bin/python` (bottom right status bar).

If stuck, run the “quality: all” task and read the first failing step’s output.

---

Next: [Appendix: Configuration files explained](./appendix-configs.md)

## Try it

- Intentionally cause a `ModuleNotFoundError` by running from the wrong directory; fix it by switching to repo root and activating the venv.
- Trigger a coverage failure by skipping a branch; write a test to cover it and re-run.

## Check yourself

- Can you locate the exact step that failed using the CI logs?
