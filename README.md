# 🛡️ A1 Defensive Programming Calculator

> **Learn defensive programming principles through hands-on implementation** of a calculator with comprehensive error handling, input validation, and robust design patterns.

This project demonstrates defensive programming principles following the A1-defensive-programming.md requirements. It provides both a complete reference implementation and a guided learning experience.

## 🎯 What This Project Teaches

- **Defensive Programming Principles** - EAFP vs LBYL, guard clauses, assertions
- **Custom Exception Hierarchy** - Structured error handling with context
- **Design by Contract** - Pre/post-conditions and invariants
- **Input Validation** - Comprehensive type and value checking
- **Error Boundary Logging** - Structured logging at appropriate levels
- **Test-Driven Error Handling** - Comprehensive error path coverage

## � Project Structure

```
Project_test/
├── answers/                    # ✅ Complete implementation
│   ├── src/                   # Defensive programming implementation
│   └── tests/                 # Comprehensive test suite
├── practice/                   # 📚 Learning version
│   ├── src/                   # Skeleton with TODOs and hints
│   └── tests/                 # Same tests for validation
├── demo_differences.py         # 🎯 Side-by-side comparison
├── DEFENSIVE_PROGRAMMING_README.md  # 📖 Detailed guide
└── A1_IMPLEMENTATION_SUMMARY.md     # 📝 Project summary
```

## 🚀 Quick Start

**Prerequisites**: Python 3.10+ and Git installed

### Try the Complete Implementation (answers/)

```bash
# Basic operations
python3 -m answers.src.main add 2 3
python3 -m answers.src.main divide 6 3

# With verbose logging
python3 -m answers.src.main --verbose multiply 4 5

# See error handling
python3 -m answers.src.main divide 5 0     # Exit code 2 (math error)
python3 -m answers.src.main add invalid 5  # Exit code 1 (input error)

### Learn Through Practice (practice/)

```bash
# See the current incomplete state
python3 -m practice.src.main add 2 3  # Returns: 0 (placeholder)

# Run tests to see what needs implementation
pytest practice/tests/ -v

# Follow the TODOs in practice/src/ to implement defensive programming
# See DEFENSIVE_PROGRAMMING_README.md for detailed guidance
```

### Compare Implementations

```bash
# Run side-by-side comparison
python3 demo_differences.py
```

## 🛡️ Defensive Programming Features Demonstrated

### ✅ Complete Implementation (answers/)

- **🔒 Input Validation**: Rejects invalid types, NaN, infinity with custom exceptions
- **� Custom Exception Hierarchy**: `CalculatorError` → `InvalidInputError`, `DivisionByZeroError`, etc.
- **📝 Design by Contract**: Pre/post-condition validation with assertions
- **🚨 Error Context**: All exceptions include debugging context without data leakage
- **📊 Comprehensive Logging**: Configurable logging at error boundaries
- **🔀 EAFP vs LBYL**: Appropriate strategy selection with justification
- **🛠️ Guard Clauses**: Early validation to reduce nesting
- **⚡ Exit Code Standards**: Different codes for different error types

### 📚 Learning Implementation (practice/)

- **TODO-driven learning** with comprehensive hints
- **Same test suite** validates your progress
- **Step-by-step guidance** for each defensive programming principle
- **Reference to complete implementation** for comparison

## 🧪 Testing & Validation

```bash
# Test the complete implementation
pytest answers/tests/ -v

# Test your practice implementation
pytest practice/tests/ -v

# Run quality checks
make qa
```

## � Documentation

- **[DEFENSIVE_PROGRAMMING_README.md](DEFENSIVE_PROGRAMMING_README.md)** - Complete implementation guide
- **[A1_IMPLEMENTATION_SUMMARY.md](A1_IMPLEMENTATION_SUMMARY.md)** - Project overview and results
- **[A1-defensive-programming.md](A1-defensive-programming.md)** - Original assignment requirements

## 🎯 Key Learning Objectives

### **Defensive Programming Mastery**
- ✅ **EAFP vs LBYL**: When to use each approach with real examples
- ✅ **Input Validation**: Comprehensive type and value checking
- ✅ **Custom Exceptions**: Hierarchical error handling with context
- ✅ **Guard Clauses**: Simplifying complex conditional logic
- ✅ **Contract Programming**: Pre/post-conditions and invariants
- ✅ **Error Boundaries**: Strategic logging placement

### **Professional Error Handling**
- ✅ **Structured Exception Hierarchy**: `CalculatorError` base class system
- ✅ **Context Preservation**: Error debugging without data leakage
- ✅ **Exit Code Standards**: Appropriate CLI error signaling
- ✅ **Logging Best Practices**: Configurable, actionable logging
- ✅ **Test-Driven Error Paths**: Comprehensive error scenario coverage

### 🛠️ **Tools & Technologies**
- **Testing**: pytest with comprehensive error path coverage
- **Code Quality**: Black, isort, Flake8, Pylint integration
- **Type Safety**: mypy static type checking for robustness
- **Logging**: Python logging module with structured output
- **CLI Design**: argparse with defensive argument validation

## 🎓 Defensive Programming Principles in Action

### **EAFP (Easier to Ask for Forgiveness than Permission)**
```python
# Used for arithmetic operations where exceptions are expected
try:
    result = a / b
except Exception as e:
    raise InvalidInputError(f"Division failed: {e}")
```

### **LBYL (Look Before You Leap)**
```python
# Used for type safety and precondition validation
if not isinstance(value, (int, float)):
    raise InvalidInputError(f"Parameter must be a number")
if math.isnan(value):
    raise InvalidInputError(f"Parameter cannot be NaN")
```

### **Guard Clauses for Clean Code**
```python
def divide(a, b):
    _validate_input(a, "a")    # Guard clause
    _validate_input(b, "b")    # Guard clause
    if b == 0:                 # Guard clause
        raise DivisionByZeroError("Cannot divide by zero")
    # Main logic here...
```

## 🆘 Quick Troubleshooting

```bash
# Module import issues
cd /path/to/Project_test
python3 -m answers.src.main add 2 3    # Use full module path

# Run specific tests
pytest answers/tests/test_operations.py::TestAddOperation -v

# Check error handling
python3 -m answers.src.main divide 5 0  # Should exit with code 2
echo $?  # Shows exit code

# Compare implementations
python3 demo_differences.py
```

## 🔗 Related Resources

- **A1 Assignment**: [A1-defensive-programming.md](A1-defensive-programming.md)
- **Implementation Guide**: [DEFENSIVE_PROGRAMMING_README.md](DEFENSIVE_PROGRAMMING_README.md)
- **Project Summary**: [A1_IMPLEMENTATION_SUMMARY.md](A1_IMPLEMENTATION_SUMMARY.md)
- **Python Exception Docs**: [docs.python.org/exceptions](https://docs.python.org/3/tutorial/errors.html)

## 🌟 Why Defensive Programming Matters

### **Production Reliability**
Defensive programming prevents the "it works on my machine" problem by anticipating and handling edge cases before they cause system failures.

### **Debugging Efficiency**
Custom exceptions with context make debugging 10x faster by providing actionable error information instead of cryptic stack traces.

### **Code Maintainability**
Guard clauses and input validation make code self-documenting and easier to modify safely.

### **Professional Development**
These patterns are essential for any Python developer working on production systems where reliability and maintainability matter.

---

**🚀 Ready to master defensive programming? Start with the [complete guide](DEFENSIVE_PROGRAMMING_README.md) or jump into the [practice version](practice/)!**

---

## 📈 Next Steps

1. **Start Learning**: Open [`docs/index.md`](docs/index.md) for the complete guide
2. **Try Exercises**: Each chapter includes hands-on activities
3. **Build Your Version**: Fork this repo and customize it
4. **Join the Community**: Share your progress and get help

**Ready to build professional-grade Python software?** [Start your journey here →](docs/index.md)

# Basic Calculator — Professional Python Project Template

This repo is a tiny calculator used to teach professional Python practices: clean structure, tests with coverage, linting/formatting, typing, security checks, CI, and VS Code workflows.

Looking for the full student guide? Read the textbook in [docs](docs/index.md):

- Start here: docs/index.md
- Or jump to: Setup (docs/02-setup.md), Testing (docs/05-testing.md), VS Code (docs/09-vscode.md), CI (docs/08-ci.md)

## Quickstart (macOS + zsh)

```zsh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Run the quality suite:

```zsh
pytest --cov=src --cov-report=term-missing -q
flake8 $(git ls-files '*.py' | tr '\n' ' ')
pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
mypy src
make security
```

## CLI usage

Install in editable mode to use the `calc` command:

```zsh
. .venv/bin/activate
pip install -e .
calc add 2 3
```

Or run without installing:

```zsh
python -m src.main add 2 3
```

## What’s inside

- `src/` — calculator code and CLI
- `tests/` — pytest suite with 100% coverage on `src/`
- `pyproject.toml` — tool configs (Black, isort, Flake8, Pylint, mypy) and console script
- `.vscode/` — tasks, settings, and debug configs
- `.github/workflows/quality.yml` — CI for format/lint/typecheck/security
- `docs/` — the full student textbook for this project

For details, see the textbook: `docs/index.md`.
