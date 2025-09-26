# Appendix: Configuration files explained

- `pyproject.toml`
  - `[build-system]`: setuptools backend
  - `[project]`: metadata and `calc` console entry
  - `[tool.setuptools]`: explicitly include `src` packages
  - `[tool.black]`, `[tool.isort]`, `[tool.flake8]`, `[tool.pylint]`, `[tool.mypy]`: tool configs
- `pytest.ini`: discovery, coverage, and pytest‑pylint integration
- `requirements-dev.txt`: dev tool versions
- `Makefile`: common targets (fmt, lint, typecheck, security, ci)
- `.pre-commit-config.yaml`: fast pre‑commit hooks
- `.editorconfig`: universal editor rules
- `.vscode/tasks.json`: tasks for venv, fmt, lint, tests, typecheck, coverage, security
- `.vscode/settings.json`: pytest enabled, format on save, Coverage Gutters
- `.vscode/launch.json`: debug configs (debugpy)
- `.github/workflows/quality.yml`: CI pipeline
- `.github/dependabot.yml`: automated dependency update PRs

---

Next: [Glossary](./glossary.md)
