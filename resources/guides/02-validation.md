# 🛡️ Input Validation - Defending Against Bad Data

> **Learning Goal**: Implement robust input validation using guard clauses, LBYL vs EAFP strategies, and comprehensive error handling.

## 🎯 What You'll Learn

- **Guard Clauses** - Early validation to reduce complexity
- **LBYL vs EAFP** - When to "Look Before You Leap" vs "Easier to Ask Forgiveness than Permission"
- **Type Safety** - Validating data types and ranges
- **Edge Case Handling** - NaN, infinity, and special values

## 📋 Your Task

You'll implement validation functions in [`src/operations/__init__.py`](../../src/operations/__init__.py). Look for the `_validate_input()` function and related TODOs.

## 🔍 Understanding Validation Strategies

### Guard Clauses (LBYL - Look Before You Leap)
```python
def _validate_input(value: Number, param_name: str) -> None:
    # Guard clause - check type first
    if not isinstance(value, (int, float)):
        raise InvalidInputError(f"Parameter '{param_name}' must be a number")

    # Guard clause - check for NaN
    if math.isnan(value):
        raise InvalidInputError(f"Parameter '{param_name}' cannot be NaN")
```

**When to use LBYL:** For conditions that MUST be checked (like division by zero, type validation).

### EAFP (Easier to Ask Forgiveness than Permission)
```python
def safe_operation(a, b):
    try:
        result = a / b  # Just try it
        return result
    except ZeroDivisionError:
        raise DivisionByZeroError("Cannot divide by zero")
```

**When to use EAFP:** For operations that might fail but are expected to succeed most of the time.

## 💡 Key Concepts

### Input Validation Pyramid
```
1. Type Check     ← Guard clause (LBYL)
2. Range Check    ← Guard clause (LBYL)
3. Special Values ← Guard clause (LBYL)
4. Business Logic ← EAFP for operations
```

### Comprehensive Validation
```python
def _validate_input(value: Number, param_name: str) -> None:
    """Validate a single input parameter."""

    # Type validation (LBYL - must check this)
    if not isinstance(value, (int, float)):
        raise InvalidInputError(
            f"Parameter '{param_name}' must be a number",
            {"value": value, "type": type(value).__name__}
        )

    # Special value validation (LBYL - dangerous values)
    if math.isnan(value):
        raise InvalidInputError(
            f"Parameter '{param_name}' cannot be NaN",
            {"value": value, "param": param_name}
        )

    if math.isinf(value):
        raise InvalidInputError(
            f"Parameter '{param_name}' cannot be infinite",
            {"value": value, "param": param_name}
        )
```

## 🛠️ Implementation Steps

### Step 1: Import Dependencies (2 minutes)
Make sure you have the right imports:
```python
import math
from typing import Union
from ..exceptions import InvalidInputError, OverflowError, UnderflowError
```

### Step 2: Implement `_validate_input()` (15 minutes)
This function should:
- Check if the value is a number (int or float)
- Reject NaN values
- Reject infinite values
- Provide clear error messages with context

### Step 3: Implement `_check_overflow()` (10 minutes)
This function should:
- Check if result is infinite (overflow)
- Check if result is unreasonably small (underflow)
- Only flag underflow when inputs aren't already tiny

### Step 4: Test Your Validation (5 minutes)
```bash
# Test specific validation
pytest tests/test_operations.py::TestInputValidation -v

# Try some edge cases
python3 -c "
from src.operations import add
try:
    add('not a number', 5)
except Exception as e:
    print('Caught:', e)
"
```

## 🧪 Testing Edge Cases

Try these scenarios:
```python
from src.operations import add
import math

# These should raise InvalidInputError
add("string", 5)           # Wrong type
add(math.nan, 5)          # NaN value
add(math.inf, 5)          # Infinite value
add(None, 5)              # None type

# These should work
add(0, 5)                 # Zero is valid
add(-5, 10)               # Negative numbers
add(1e-100, 2e-100)       # Very small numbers
add(1e100, 1e100)         # Large numbers (if no overflow)
```

## 🔍 Debugging Tips

### Common Issues
```python
# ❌ Problem: Catching too broadly
except Exception:
    # This hides bugs!

# ✅ Solution: Be specific
except (TypeError, ValueError) as e:
    raise InvalidInputError(f"Conversion failed: {e}")
```

### Validation Order Matters
```python
# ✅ Right order
if not isinstance(value, (int, float)):  # Type first
    raise InvalidInputError(...)
if math.isnan(value):                    # Then special values
    raise InvalidInputError(...)

# ❌ Wrong order
if math.isnan(value):                    # This crashes on strings!
    raise InvalidInputError(...)
if not isinstance(value, (int, float)):
    raise InvalidInputError(...)
```

## 🔗 External Resources

- **[Guard Clauses Pattern](https://refactoring.guru/replace-nested-conditional-with-guard-clauses)** - Refactoring technique
- **[EAFP vs LBYL](https://docs.python.org/3/glossary.html#term-eafp)** - Python's philosophy
- **[IEEE 754 Special Values](https://en.wikipedia.org/wiki/IEEE_754#Special_values)** - Understanding NaN/Infinity

## ✅ Success Criteria

- [ ] `_validate_input()` checks type, NaN, and infinity
- [ ] `_check_overflow()` detects mathematical overflows
- [ ] All validation tests pass
- [ ] Error messages include helpful context
- [ ] Code uses appropriate LBYL vs EAFP strategies

## 🚀 Next Step

With solid validation in place, move to **[Error-Safe Operations →](03-operations.md)** where you'll implement the arithmetic functions using these validation patterns.

---

💡 **Pro Tip:** Run `pytest tests/test_operations.py::TestInputValidation -v` frequently to see your progress!
