# 🛡️ Defensive Programming Calculator - Learning Project

> **Master defensive programming principles through hands-on implementation** of a calculator with comprehensive error handling, input validation, and robust design patterns.

This project teaches defensive programming principles through guided implementation. Start with the skeleton code and build your understanding step-by-step using provided resources and examples.

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
├── src/                       # 🧱 Your implementation (start here!)
│   ├── main.py               # CLI entry point with TODOs
│   ├── exceptions.py         # Custom exception classes to build
│   └── operations/           # Arithmetic operations to implement
├── complete_solutions/        # 🏆 Reference implementation (runnable)
├── tests/                     # 🧪 Test suite (validates your progress)
├── resources/                 # 📚 Learning materials and references
│   ├── examples/             # 📚 Focused defensive programming snippets
│   ├── guides/               # Step-by-step tutorials
│   └── references/           # Quick reference materials
├── docs/                      # 📖 Complete learning guide
├── COMPLETE_SOLUTIONS.md      # 📖 Code reference documentation
└── LEARNING_GUIDE.md          # 🎯 Start your journey here
```

## 🚀 Quick Start

**Prerequisites**: Python 3.10+ and Git installed

### 1. Set Up Your Development Environment

```bash
# Clone and enter the project
git clone <your-repo-url>
cd Project_test

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development tools
pip install -r requirements-dev.txt
```

### 2. Start Learning

```bash
# Read the learning guide first
cat LEARNING_GUIDE.md

# Try your implementation (will fail initially - that's expected!)
python3 -m src.main add 2 3

# Run tests to see what needs implementing
pytest tests/ -v
```

### 3. Build Your Implementation

```bash
# See the current incomplete state
python3 -m src.main add 2 3  # Returns: 0 (placeholder)

# Run tests to see what needs implementation
pytest tests/ -v

# Follow the TODOs in src/ to implement defensive programming
# Use resources/guides/ for step-by-step instructions
```

## ⚠️ Why tests may fail for you (expected behavior)

This repository is designed as a learning exercise. The `src/` package intentionally contains skeleton code with TODOs for you to implement. Because of that, running the full test-suite against `src/` will produce failing tests until you implement the missing pieces.

If you want a fully working reference, check `complete_solutions/` which contains a complete, runnable implementation you can inspect or run directly.

Copyable commands to run local checks and compare implementations:

```bash
# Run tests (will fail until you implement src/)
pytest tests/ -v

# Type checking (mypy)
mypy src --explicit-package-bases

# Lint and format checks (pre-commit will run black/isort/flake8)
. .venv/bin/activate && pre-commit run --all-files

# Run the reference implementation
python3 -m complete_solutions.main add 2 3
```


### Reference Implementation

```bash
# See complete runnable implementation
cd complete_solutions/
python3 main.py add 2 3

# Compare with your implementation
# Run side-by-side comparison
python3 demo_differences.py
```

## 🛡️ Defensive Programming Features Demonstrated

### ✅ Complete Implementation

- **🔒 Input Validation**: Rejects invalid types, NaN, infinity with custom exceptions
- **� Custom Exception Hierarchy**: `CalculatorError` → `InvalidInputError`, `DivisionByZeroError`, etc.
- **📝 Design by Contract**: Pre/post-condition validation with assertions
- **🚨 Error Context**: All exceptions include debugging context without data leakage
- **📊 Comprehensive Logging**: Configurable logging at error boundaries
- **🔀 EAFP vs LBYL**: Appropriate strategy selection with justification
- **🛠️ Guard Clauses**: Early validation to reduce nesting
- **⚡ Exit Code Standards**: Different codes for different error types

```

Your implementation lives in [`src/`](src/) - it's mostly skeleton code with TODOs and hints. The [`tests/`](tests/) directory contains a comprehensive test suite that will guide your implementation and validate your progress.

## 📚 Learning Resources

### 📖 Comprehensive Guides
- **[LEARNING_GUIDE.md](LEARNING_GUIDE.md)** - Your roadmap to success
- **[Exception Design](resources/guides/01-exceptions.md)** - Building robust error handling
- **[Input Validation](resources/guides/02-validation.md)** - Defending against bad data
- **[Error-Safe Operations](resources/guides/03-operations.md)** - Bulletproof arithmetic
- **[CLI Design](resources/guides/04-cli.md)** - Professional command-line interfaces

### 🔧 Quick References
- **[Complete Solutions](COMPLETE_SOLUTIONS.md)** - 🏆 Full working implementations
- **[Code Examples](resources/examples/)** - 📚 Focused defensive programming snippets
- **[Defensive Programming Checklist](resources/references/defensive-checklist.md)**
- **[EAFP vs LBYL Guide](resources/references/eafp-vs-lbyl.md)**

### 📘 Complete Learning Path
The [`docs/`](docs/) directory contains a full textbook on professional Python development:
- **[Getting Started](docs/01-overview.md)** - Project overview and setup
- **[Testing & Coverage](docs/05-testing.md)** - Comprehensive testing strategies
- **[Code Quality](docs/04-tooling.md)** - Linting, formatting, and type checking
- **[VS Code Setup](docs/09-vscode.md)** - Professional development environment

## 🎯 Learning Objectives

By completing this project, you'll master:

### 🛡️ **Defensive Programming**
- **Input Validation** - Type checking, range validation, special value handling
- **Error Boundaries** - Where and how to handle errors appropriately
- **Guard Clauses** - Early validation to reduce complexity
- **Contract Programming** - Preconditions, postconditions, and invariants

### 🚨 **Error Handling Excellence**
- **Custom Exception Hierarchies** - Structured error types with rich context
- **EAFP vs LBYL** - Choosing the right strategy for each situation
- **Error Message Design** - User-friendly messages that aid debugging
- **Graceful Degradation** - Failing safely without crashing

### 🔧 **Professional Development Skills**
- **Test-Driven Development** - Writing tests that guide implementation
- **Code Quality Tools** - Linting, formatting, type checking, security scanning
- **CLI Design** - Argument parsing, exit codes, help systems
- **Documentation** - Clear docstrings and user guides

## 🧪 Quality Assurance

This project includes a full professional development toolkit:

```bash
# Run all quality checks
make qa

# Individual tools
pytest tests/              # Test suite with coverage
mypy src/                  # Static type checking
flake8 src/                # Code style linting
black src/                 # Automatic formatting
bandit src/                # Security vulnerability scanning
```

### Success Metrics
- ✅ **All Tests Pass** - Your implementation satisfies the requirements
- ✅ **Type Safety** - mypy finds no type errors
- ✅ **Code Quality** - Passes linting and formatting checks
- ✅ **Security** - No vulnerabilities detected
- ✅ **Coverage** - Tests exercise all code paths

## 🆘 Getting Help

### When You're Stuck
1. **Check the guides** in [`resources/guides/`](resources/guides/)
2. **Look at examples** in [`resources/examples/`](resources/examples/)
3. **Read the tests** - they show exactly what's expected
4. **Use the debugger** - VS Code debug configurations are included

### Common Issues
- **Import errors**: Make sure you're in the project root directory
- **Test failures**: Expected initially! They guide what to implement
- **Type errors**: Check the [typing guide](resources/references/typing-guide.md)
- **Module not found**: Activate your virtual environment

### External Resources
- **[Python Exception Documentation](https://docs.python.org/3/tutorial/errors.html)**
- **[Real Python: Exception Handling](https://realpython.com/python-exceptions/)**
- **[Clean Code Principles](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29)**
- **[PEP 8: Style Guide](https://www.python.org/dev/peps/pep-0008/)**

## 🏆 Next Steps

After mastering defensive programming here:

1. **Apply to Real Projects** - Use these patterns in your own code
2. **Explore Advanced Topics** - Concurrency, async/await, design patterns
3. **Build Your Portfolio** - Showcase your defensive programming skills
4. **Join the Community** - Contribute to open-source projects
5. **Keep Learning** - Check out [`docs/careers.md`](docs/careers.md) for career paths

---

**Ready to become a defensive programming expert?** Start with **[LEARNING_GUIDE.md](LEARNING_GUIDE.md)** and begin your journey! 🚀

## 🧪 Testing & Validation

```bash
# Test the complete implementation
pytest tests/ -v

# Test your practice implementation
pytest tests/ -v

# Run quality checks
make qa
```

## 🔁 Continuous Integration and Local Checks

This repository includes a GitHub Actions workflow that runs on pushes and pull requests to `main`. The CI performs:

- Type checking with `mypy`
- Linting with `flake8`
- Formatting checks with `black` and `isort`
- Test execution with `pytest` (JUnit + coverage reports)
- Grading summary generation (simple JSON) from pytest results

To enable local checks before pushing, install the provided git hook:

```bash
# From project root
./scripts/install_hooks.sh

# This will install a pre-push hook that runs a subset of CI checks locally
# (mypy, flake8, black/isort checks, and a fast pytest run).
```

Note: GitHub branch protection rules can be enabled in your repository settings to require the CI to pass before merging to the `main` branch. Actions cannot prevent a force-push; use branch protection to enforce checks.

If you want Codecov integration, add a `CODECOV_TOKEN` secret to your repository settings and the workflow will upload coverage reports automatically.


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
pytest tests/test_operations.py::TestAddOperation -v

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

**🚀 Ready to master defensive programming? Start with the [Learning Guide](LEARNING_GUIDE.md) and build your implementation in [`src/`](src/)!**

---

## 📈 Next Steps

1. **Start Learning**: Open [`docs/INDEX.md`](docs/INDEX.md) for the complete guide
2. **Try Exercises**: Each chapter includes hands-on activities
3. **Build Your Version**: Fork this repo and customize it
4. **Join the Community**: Share your progress and get help

**Ready to build professional-grade Python software?** [Start your journey here →](docs/INDEX.md)

---

# 📖 Professional Python Development Template

*This project serves as both a defensive programming tutorial and a template for professional Python projects.*

This project demonstrates professional Python development practices through a focused example: a defensive calculator. It shows how small projects can be engineered like professional ones.

**For educators and learners**: Use this as a complete learning curriculum for defensive programming and professional Python development.

**For developers**: Fork this as a template for new Python projects with professional tooling already configured.

### 📚 Complete Learning Materials

- **[Complete Textbook](docs/INDEX.md)** - Professional Python development from setup to CI
- **[Quick Start](docs/02-setup.md)** - Get running in 5 minutes
- **[Testing Guide](docs/05-testing.md)** - Comprehensive testing strategies
- **[VS Code Setup](docs/09-vscode.md)** - Professional development environment
- **[CI/CD Guide](docs/08-ci.md)** - Automated quality checks

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
