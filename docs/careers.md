# Careers in and around code quality

Modern teams rely on these practices; here’s where they show up on the job.

## Roles and day-to-day
- Software Engineer (backend/frontend/full-stack): implement features, write tests, keep CI green, own services.
- Developer Productivity/Platform Engineer: build templates/tooling, improve CI speed/reliability, maintain linters and test frameworks.
- QA/Software Engineer in Test: design automated test suites, build harnesses, add property/fuzz and integration tests.
- Security Engineer: set policy (Bandit, SAST), manage dependency scanning and response, educate teams.
- Data/ML Engineer: test pipelines, notebooks-to-packages workflows, docstring/type discipline for reproducibility.

## Skills map (from this repo)
- Testing: pytest, parametrization, coverage
- Code health: Black/isort, Flake8, Pylint, pre-commit
- Static typing: mypy and type design
- Automation: VS Code tasks, CI workflows
- Security: Bandit, pip-audit, Dependabot

## Across languages
- JS/TS: Jest/Vitest, Prettier, ESLint, TypeScript, renovate
- Go: `go test`, `gofmt`, golangci-lint, `go vet`
- Java/Kotlin: JUnit, Spotless/Checkstyle, ErrorProne, Maven/Gradle, Dependabot
- C#/.NET: xUnit/NUnit, dotnet-format, Sonar/StyleCop, GitHub Actions/Azure Pipelines

## How to signal readiness on resumes
- Link to a repo with tests, CI badge, and clear README/docs
- Show small PRs with good commit messages and green builds
- Mention ownership: “Raised coverage from 70%→95%, added CI step for static analysis, reduced pipeline time by 30%”

## Next steps
- Learn property-based testing (Hypothesis), mutation testing (mutmut)
- Explore typed APIs and public packages (packaging, semver)
- Contribute small improvements to OSS repos adopting similar tooling
