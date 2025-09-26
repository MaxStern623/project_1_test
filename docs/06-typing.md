# 6) Static typing with mypy

Static typing catches bugs early and documents intent.

## Learning goals
- Add and refine type hints on functions
- Understand common mypy flags and errors
- Use `typing.Union`/`Literal`/`TypedDict` when appropriate

- Config: `[tool.mypy]` in `pyproject.toml` (targets Python 3.11, excludes tests)
- Key flags: `disallow_untyped_defs = true`, `no_implicit_optional = true`

## Run type checks
```zsh
mypy src
```

Tip: Add types to function signatures and return values. Prefer `float` math in CLI.

## Try it

1. Tighten a function signature in `src/operations/__init__.py` and rerun `mypy src`.
2. Introduce a deliberate type mismatch (e.g., pass a string) in a small local experiment and see mypy’s error.

## Check yourself

- What’s the benefit of `disallow_untyped_defs = true`?
- When would you prefer `float` over `Number`?

## Background
Static analysis predates modern languages; optional typing in Python brings many of those benefits without giving up dynamism.

## Across languages
TypeScript for JS, Kotlin/Java, Rust, and Go use strong typing to prevent whole classes of bugs.

## Career connection
Comfortable type design signals maturity—especially when building public APIs and libraries.

---

Next: [CLI and packaging](./07-cli.md)
