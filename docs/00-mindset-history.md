# 0) Developer mindset and a brief history of the craft

Software engineering isn’t just writing code—it’s designing feedback loops so we can change code safely. The tools in this textbook exist to shorten the loop between “I think this works” and “I know this works”.

## Why these practices emerged
- Testing: From the early days of Smalltalk and S-unit to JUnit and pytest—small, fast tests make change cheap. TDD popularized writing tests first to lock in behavior.
- Linting and formatting: Unix lint in the 1970s, then language-specific linters (Pylint, Flake8) and auto-formatters (Black, gofmt, Prettier) to reduce bikeshedding and catch bugs early.
- Static typing: From strongly typed languages to optional typing in Python/TypeScript—types communicate intent and let tools reason about code before it runs.
- CI/CD: From nightly builds to every-commit pipelines—automate verification so no one “forgets” the checklist.
- Editor automation: From vi/emacs macros to modern IDEs—tasks, refactors, and debuggers speed up the loop.

## The professional loop
1) Plan a tiny change
2) Write/adjust a test (red)
3) Implement minimally (green)
4) Refactor with safety nets
5) Automate checks locally and in CI

## Across languages: same ideas, different names
- Python: pytest, Black/isort, Flake8/Pylint, mypy, Bandit
- JavaScript/TypeScript: Jest/Vitest, Prettier, ESLint, TypeScript, npm audit
- Go: `go test`, `gofmt`, `golangci-lint`, static analysis, `go vet`
- Java/Kotlin: JUnit, Spotless/Checkstyle, ErrorProne, SpotBugs, Maven/Gradle builds

## Career connections
- Software Engineer: deliver features safely—tests, CI, code reviews
- Developer Productivity/Platform: build the tooling (CI, templates, linters)
- QA/SET: design automated test systems, property/fuzz testing
- Security Engineer: SAST/DAST, dependency scanning, secure defaults

Mindset: Treat feedback as a teammate. Faster feedback beats guessing.

---

Next: [Project overview](./01-overview.md)
