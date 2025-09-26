# A1 Defensive Programming, Errors, and Contracts [Core]

Duration: 3–4h
P: Testing foundations

## Goal
Write resilient code that fails fast, communicates intent, and recovers gracefully.

## Topics
- EAFP vs LBYL and when to use each
- Invariants, assertions, guard clauses
- Python exceptions hierarchy, custom exceptions, error boundaries
- Design by contract (pre-/post-conditions)
- Sentinel values vs exceptions; logging basics

## Before you start (preflight)
- Repo cloned; tests run locally (pytest -q)
- Python >= 3.10; venv active
- CI has pytest + coverage set up

## Outcomes
- Choose EAFP or LBYL appropriately, with justification
- Implement clear error handling with actionable messages
- Add targeted tests for error paths and contracts

## Build (hands-on)
- Harden an existing module (e.g., calculator ops or config loader):
  - Add explicit pre-/post-condition checks and assertions where helpful
  - Replace ambiguous return codes with custom exceptions
  - Introduce guard clauses to simplify branching
  - Add logging at error boundaries with actionable context
- Update tests to cover error scenarios and contracts

## Acceptance (CI-verifiable)
- Tests pass and include error-path coverage (>= 2 new tests)
- No bare except; custom exceptions used where appropriate
- Logs include context (inputs or IDs) without leaking secrets

## Quick win
Convert a nested conditional into guard clauses; tests become easier to read.

## Common pitfalls
- Overusing exceptions for control flow
- Leaking sensitive data in error messages or logs

## Reflection
Which contract assertion prevented a bug you might have missed?

## References
- Python docs: Errors and Exceptions
- “Design by Contract” primers
