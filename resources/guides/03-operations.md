# ⚡ Error-Safe Operations - Building Bulletproof Math

> **Learning Goal**: Implement arithmetic operations with comprehensive error handling, postcondition validation, and contract programming principles.

## 🎯 What You'll Learn

- **Design by Contract** - Preconditions, postconditions, and invariants
- **Error Boundary Patterns** - Where and how to handle errors
- **Mathematical Edge Cases** - Division by zero, overflow, underflow
- **Defensive Assertions** - Using assert statements safely

## 📋 Your Task

Implement the four arithmetic functions in [`src/operations/__init__.py`](../../src/operations/__init__.py):
- `add(a, b)` - Addition with overflow checking
- `subtract(a, b)` - Subtraction with overflow checking
- `multiply(a, b)` - Multiplication with special case optimization
- `divide(a, b)` - Division with comprehensive zero checking

## 🔍 Design by Contract Pattern

Each operation follows this pattern:
```python
def operation(a: Number, b: Number) -> Number:
    """Operation with contracts."""

    # 1. PRECONDITIONS (validate inputs)
    _validate_input(a, "a")
    _validate_input(b, "b")

    # 2. OPERATION-SPECIFIC CHECKS
    if operation == "divide" and b == 0:
        raise DivisionByZeroError(...)

    # 3. PERFORM OPERATION (with EAFP error handling)
    try:
        result = a + b  # or -, *, /
    except Exception as e:
        raise InvalidInputError(f"Operation failed: {e}")

    # 4. POSTCONDITIONS (validate result)
    _check_overflow(result, "addition", a, b)

    # 5. ASSERTIONS (invariants that should always hold)
    assert isinstance(result, (int, float))

    return result
```

## 💡 Key Patterns

### Special Case Handling
```python
def multiply(a: Number, b: Number) -> Number:
    # Preconditions
    _validate_input(a, "a")
    _validate_input(b, "b")

    # Early returns for special cases (optimization + clarity)
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a

    # General case
    result = a * b
    _check_overflow(result, "multiplication", a, b)
    return result
```

### Division Special Handling
```python
def divide(a: Number, b: Number) -> float:
    # Preconditions
    _validate_input(a, "a")
    _validate_input(b, "b")

    # Division-specific validation
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")

    if abs(b) < EPSILON:  # Very small number
        raise DivisionByZeroError("Cannot divide by number too close to zero")

    # Special case: 0 divided by anything is 0
    if a == 0:
        return 0.0

    result = a / b
    _check_overflow(result, "division", a, b)

    # Division always returns float
    return float(result)
```

## 🛠️ Implementation Guide

### Step 1: Add Function (10 minutes)
```python
def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    # TODO: Implement using the contract pattern above
    # Remember to:
    # 1. Validate inputs
    # 2. Perform operation with try/catch
    # 3. Check for overflow
    # 4. Maintain int type when both inputs are int
    pass
```

### Step 2: Subtract Function (5 minutes)
Similar to add, but with `a - b`.

### Step 3: Multiply Function (10 minutes)
Include the special case optimizations shown above.

### Step 4: Divide Function (15 minutes)
Most complex - needs zero checking and always returns float.

### Step 5: Test Each Function (10 minutes)
```bash
# Test specific operations
pytest tests/test_operations.py::TestAddition -v
pytest tests/test_operations.py::TestDivision -v

# Try manual testing
python3 -c "
from src.operations import add, divide
print(add(2, 3))      # Should work
print(divide(6, 3))   # Should work
divide(1, 0)          # Should raise DivisionByZeroError
"
```

## 🧪 Edge Cases to Handle

### Mathematical Edge Cases
```python
# Overflow cases
add(1e308, 1e308)         # May overflow
multiply(1e200, 1e200)    # Definitely overflows

# Division edge cases
divide(1, 0)              # Zero division
divide(1, 1e-16)          # Very small divisor
divide(0, 5)              # Zero dividend (should return 0.0)

# Type consistency
add(2, 3)                 # Should return int(5)
add(2.0, 3)               # Should return float(5.0)
divide(6, 3)              # Should return float(2.0) - division always float
```

### Error Context Examples
```python
# Good error context
try:
    result = a / b
except Exception as e:
    raise InvalidInputError(
        f"Division failed: {e}",
        {"a": a, "b": b, "operation": "division"}
    )
```

## 🔍 Testing Your Implementation

### Quick Verification
```python
from src.operations import add, subtract, multiply, divide

# Basic functionality
assert add(2, 3) == 5
assert subtract(5, 3) == 2
assert multiply(2, 3) == 6
assert divide(6, 3) == 2.0

# Type consistency
assert isinstance(add(2, 3), int)        # int + int = int
assert isinstance(add(2.0, 3), float)    # float involved = float
assert isinstance(divide(6, 3), float)   # division always float

# Error handling
try:
    divide(1, 0)
    assert False, "Should have raised DivisionByZeroError"
except DivisionByZeroError:
    pass  # Expected
```

## 🔗 External Resources

- **[IEEE 754 Arithmetic](https://en.wikipedia.org/wiki/IEEE_754)** - Understanding floating-point behavior
- **[Python Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)** - Official documentation
- **[Design by Contract](https://en.wikipedia.org/wiki/Design_by_contract)** - Programming methodology

## ✅ Success Criteria

- [ ] All four operations implemented with full contracts
- [ ] Precondition validation using `_validate_input()`
- [ ] Postcondition checking with `_check_overflow()`
- [ ] Special cases handled (zero, identity elements)
- [ ] Error context provided in exceptions
- [ ] Type consistency maintained (int+int→int, division→float)
- [ ] All operation tests pass

## 🚀 Next Step

With rock-solid operations, move to **[CLI with Error Handling →](04-cli.md)** where you'll build a command-line interface that properly handles and reports errors.

---

💡 **Debug Tip:** Use `python3 -c "from src.operations import *; help(add)"` to test your docstrings and imports!
