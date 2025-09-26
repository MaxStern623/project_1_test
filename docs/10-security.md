# 10) Security and dependency health

## Bandit (static security analysis)
- Run: `bandit -q -r src -x tests`
- In Makefile target `security` and CI job.

## pip‑audit (dependency vulnerabilities)
- Run: `pip-audit -r requirements.txt || true`
- Included in `make security` and CI.

## Dependabot (automated updates)
- Config: `.github/dependabot.yml`
- Opens weekly PRs for pip and GitHub Actions updates (minor/patch grouped).

---

Next: [Everyday workflows](./11-workflows.md)

## Learning goals
- Run security scans on code and dependencies
- Interpret Bandit findings and pip-audit advisories
- Keep dependencies up to date via Dependabot PRs

## Try it

1. Run `make security` locally and inspect the output.
2. (Lab) Add an old version of a common lib to `requirements.txt` (e.g., `requests==2.19.0`), run `pip-audit -r requirements.txt`, then revert the change.
3. Open a Dependabot PR (or simulate) and practice reviewing the change log.

## Check yourself

- What’s the difference between code-level and dependency-level security checks?
- How would you suppress a false positive responsibly?
