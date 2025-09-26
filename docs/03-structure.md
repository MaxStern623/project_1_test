# 3) Repository structure

```
.
├── pyproject.toml                 # Tooling + packaging metadata
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # (Optional) runtime dependencies
├── requirements-dev.txt           # Developer toolchain
├── Makefile                       # Common quality targets
├── .pre-commit-config.yaml        # Fast local checks before commit
├── .editorconfig                  # Editor‑agnostic formatting rules
├── .github/workflows/quality.yml  # CI pipeline
├── .vscode/                       # Editor tasks, settings, launches
│   ├── tasks.json
│   ├── settings.json
│   └── launch.json
├── src/
│   ├── __init__.py
│   ├── main.py                    # CLI entry
│   └── operations/__init__.py     # Arithmetic functions
├── tests/
│   ├── __init__.py
│   ├── test_operations.py
│   └── test_operations_param.py
└── docs/                          # This textbook
```

## Learning goals

- Navigate a src/tests project layout
- Understand where configs live and what they control
- Know where to add code vs. tests vs. docs

Design choices:
- src/ layout: prevents accidental imports and mirrors installable packages.
- Single source of truth for config in `pyproject.toml` where possible.
- Tests live in `tests/` and target `src/`.
- VS Code tasks encapsulate common commands using the venv.

## Try it

1. Open `src/operations/__init__.py` and locate `add`, `subtract`, `multiply`, `divide`.
2. Add a new stub function `power(a: Number, b: Number) -> float:` that raises `NotImplementedError`.
3. In `tests/`, create a test (e.g., `test_power.py`) that asserts `power(2, 3) == 8.0` and mark it `xfail(strict=True)` for now.
4. Run `pytest -q` and observe the xfail.

## Check yourself

- Why do we keep implementation under `src/` and tests under `tests/`?
- Which config file controls test discovery and coverage behavior?

---

Next: [Formatting, linting, and style](./04-tooling.md)
