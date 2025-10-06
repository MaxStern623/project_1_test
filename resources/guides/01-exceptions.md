# 🚨 Custom Exceptions - Building Your Error Foundation

> **Learning Goal**: Create a robust exception hierarchy that provides clear, contextual error information while following Python best practices.

## 🎯 What You'll Learn

- **Exception Hierarchy Design** - When to inherit vs create new classes
- **Context-Rich Error Messages** - Providing debugging info without data leakage
- **Python Exception Conventions** - Following community standards
- **Defensive Error Design** - Preventing information disclosure

## 📋 Your Task

You'll implement a custom exception hierarchy in [`src/exceptions.py`](../../src/exceptions.py). Currently it's mostly empty with TODOs - your job is to fill it in!

## 🔍 Understanding the Requirements

### Base Exception Class
```python
class CalculatorError(Exception):
    """Base exception for all calculator-related errors."""
```

**Why?** Having a base class lets users catch all calculator errors with one except block, while still allowing specific error handling.

### Specific Exception Types

1. **`InvalidInputError`** - For bad user input (wrong types, NaN, infinity)
2. **`DivisionByZeroError`** - For mathematical impossibilities
3. **`OverflowError`** - For results too large to represent
4. **`UnderflowError`** - For results too small (near zero when shouldn't be)

## 💡 Key Concepts

### Context Without Disclosure
```python
# ✅ Good - provides context for debugging
raise InvalidInputError(
    "Arguments must be valid numbers: 'not_a_number', '5'",
    {"raw_args": ["not_a_number", "5"], "error": "could not convert string to float: not_a_number"}
)

# ❌ Bad - exposes internal details
raise InvalidInputError(f"Database connection failed: {db_password}")
```

### Exception Inheritance
```python
# ✅ Good - clear hierarchy
class CalculatorError(Exception): pass
class InvalidInputError(CalculatorError): pass

# ❌ Bad - flat structure
class InvalidInputError(Exception): pass  # No relationship to other calculator errors
```

## 🛠️ Implementation Steps

### Step 1: Base Exception (5 minutes)
```python
class CalculatorError(Exception):
    """Base exception for all calculator-related errors."""

    def __init__(self, message: str, context: dict[str, Any] | None = None):
        super().__init__(message)
        self.context = context or {}
```

**🤔 Why context?** It lets you attach debugging information without cluttering the main error message.

### Step 2: Specific Exceptions (10 minutes)
Create each specific exception class. They can be simple:

```python
class InvalidInputError(CalculatorError):
    """Raised when input parameters are invalid."""
    pass
```

### Step 3: Test Your Work (5 minutes)
```bash
# Run exception tests
pytest tests/test_exceptions.py -v

# Should see tests starting to pass!
```

## 🧪 Testing Your Understanding

Try these in a Python REPL:
```python
from src.exceptions import *

# Create an exception with context
try:
    raise InvalidInputError("Bad input", {"value": "abc", "expected": "number"})
except InvalidInputError as e:
    print(e)           # The message
    print(e.context)   # The debugging context

# Test inheritance
try:
    raise DivisionByZeroError("Can't divide by zero")
except CalculatorError as e:  # Should catch it!
    print("Caught as CalculatorError:", e)
```

## 🔗 External Resources

- **[Python Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)** - See how Python organizes exceptions
- **[PEP 3134: Exception Chaining](https://www.python.org/dev/peps/pep-3134/)** - Advanced: chaining exceptions with `from`
- **[Real Python: Exceptions](https://realpython.com/python-exceptions/)** - Comprehensive guide

## ✅ Success Criteria

- [ ] All exception classes inherit from `CalculatorError`
- [ ] Base class accepts both message and context
- [ ] Context is stored as a dictionary
- [ ] Tests in `test_exceptions.py` pass
- [ ] You can import exceptions without errors

## 🚀 Next Step

Once your exceptions are working, move to **[Input Validation →](02-validation.md)** where you'll use these exceptions to validate user input safely.

---

💡 **Stuck?** Check the [complete implementation](../../complete_solutions/exceptions.py) for reference, but try implementing it yourself first!
