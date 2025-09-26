# 11) Everyday workflows

## Learning goals
- Practice a tight red→green→refactor loop
- Keep a branch green locally and on CI
- Communicate changes clearly via commits and PRs

## Local development loop
- Activate venv, install dev tools
- Write a test → implement code → run tests
- Run “quality: all” in VS Code or:
  ```zsh
  black . && isort .
  flake8 $(git ls-files '*.py' | tr '\n' ' ')
  pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
  mypy src
  pytest --cov=src --cov-report=term-missing
  make security
  ```

## Git hygiene
- Small commits with clear messages
- Open a PR early; CI must pass before merge
- Use branches per feature/fix

### Commit message mini‑guide
- Format: `<type>: <short summary>` (e.g., `feat: add power subcommand`)
- Body: why the change, any tradeoffs
- Footer: references (issue/PR), breaking changes

## Try it

1. Create a feature branch, implement a tiny change (e.g., improve an error message), commit, and open a PR.
2. Request a peer review; respond to feedback and keep CI green.

### Lab: TDD a small feature
1. Write a failing test (e.g., `power(2, 3) == 8.0`).
2. Implement the minimal code to pass.
3. Refactor for clarity; ensure `quality: all` passes.
4. Add a CLI subcommand and a test capturing its output.

### Optional: PR checklist (paste into PR description)
- [ ] Tests added/updated
- [ ] `quality: all` passes locally
- [ ] Coverage unchanged or improved
- [ ] Docs (README/docs) updated if behavior changed

## Check yourself

- How small should a commit be? What makes a good message?
- What’s your fastest path to detect a break (tests, lint, or typecheck)?
- Can you keep the branch green while iterating quickly?

---

Next: [Troubleshooting](./12-troubleshooting.md)
