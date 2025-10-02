# 🐍 EAFP vs LBYL - Python's Approach to Error Handling

> **EAFP**: "Easier to Ask for Forgiveness than Permission"
> **LBYL**: "Look Before You Leap"

## 🎯 Quick Decision Guide

| Scenario | Use | Why |
|----------|-----|-----|
| Type checking | **LBYL** | Must verify before using type-specific methods |
| File operations | **EAFP** | File state can change between check and use |
| Division by zero | **LBYL** | Zero check is faster than exception handling |
| Dictionary access | **EAFP** | Pythonic; exceptions are cheap in Python |
| Network requests | **EAFP** | Many things can fail; exceptions expected |
| Range validation | **LBYL** | Simple comparison is more readable |

## 💡 EAFP (Easier to Ask for Forgiveness than Permission)

**Philosophy**: Try the operation first, handle exceptions if it fails.

### ✅ Good EAFP Examples

```python
# Dictionary access
try:
    value = my_dict[key]
except KeyError:
    value = default_value

# File operations
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError:
    handle_missing_file()

# Type conversion
try:
    number = float(user_input)
except ValueError:
    raise InvalidInputError("Input must be a number")

# Complex operations that might fail
try:
    result = complex_calculation(data)
    processed = process_result(result)
    return finalize(processed)
except CalculationError as e:
    logger.error(f"Calculation pipeline failed: {e}")
    return fallback_result()
```

### 🚀 When to Use EAFP

- **Operations that commonly succeed** but might fail
- **Multiple failure modes** (network, file system, parsing)
- **Race conditions possible** (file might be deleted between check and use)
- **Pythonic code** (following Python conventions)
- **Performance critical** (when success is the common case)

## 🔍 LBYL (Look Before You Leap)

**Philosophy**: Check conditions first, then perform the operation.

### ✅ Good LBYL Examples

```python
# Type checking (must do first)
if not isinstance(value, (int, float)):
    raise TypeError("Value must be numeric")

# Division by zero (faster than exception)
if divisor == 0:
    raise DivisionByZeroError("Cannot divide by zero")

# Range validation (clear intent)
if age < 0 or age > 150:
    raise ValueError("Age must be between 0 and 150")

# Resource availability
if not has_sufficient_memory(required_bytes):
    raise ResourceError("Insufficient memory")

# Precondition validation
if len(data) == 0:
    raise ValueError("Data cannot be empty")
```

### 🛡️ When to Use LBYL

- **Safety-critical conditions** (division by zero, null pointers)
- **Simple, fast checks** (type checking, basic comparisons)
- **Precondition validation** (guard clauses)
- **Resource constraints** (memory, disk space)
- **User input validation** (clear error messages needed)

## ⚖️ Comparison Examples

### Dictionary Access

```python
# ❌ LBYL - Race condition possible
if key in my_dict:
    value = my_dict[key]  # Key might be deleted here!
else:
    value = default

# ✅ EAFP - Atomic and safe
try:
    value = my_dict[key]
except KeyError:
    value = default

# ✅ Or use built-in EAFP method
value = my_dict.get(key, default)
```

### File Operations

```python
# ❌ LBYL - File state can change
if os.path.exists(filename):
    with open(filename) as f:  # File might be deleted here!
        content = f.read()

# ✅ EAFP - Handles all failure modes
try:
    with open(filename) as f:
        content = f.read()
except (FileNotFoundError, PermissionError, IOError) as e:
    handle_file_error(e)
```

### Division

```python
# ✅ LBYL - Simple check, clear intent
if b == 0:
    raise DivisionByZeroError("Cannot divide by zero")
return a / b

# ❌ EAFP - Exception overhead not worth it
try:
    return a / b
except ZeroDivisionError:
    raise DivisionByZeroError("Cannot divide by zero")
```

## 🎯 Best Practices

### Combine Both Approaches

```python
def safe_divide(a: float, b: float) -> float:
    # LBYL for preconditions
    if not isinstance(a, (int, float)):
        raise TypeError("a must be numeric")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be numeric")
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")

    # EAFP for the operation (handles unexpected math errors)
    try:
        result = a / b
        return result
    except (OverflowError, ArithmeticError) as e:
        raise CalculationError(f"Division failed: {e}")
```

### Validation Strategy

```python
def process_user_data(data: dict) -> ProcessedData:
    # LBYL for structure validation (clear error messages)
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")
    if 'id' not in data:
        raise ValueError("Missing required field: id")
    if 'name' not in data:
        raise ValueError("Missing required field: name")

    # EAFP for processing (complex operations)
    try:
        validated = validate_data(data)
        normalized = normalize_data(validated)
        return ProcessedData(normalized)
    except (ValidationError, NormalizationError) as e:
        raise ProcessingError(f"Data processing failed: {e}")
```

## 📊 Performance Considerations

### Exception Overhead

```python
# EAFP is faster when success is common (>90%)
def eafp_approach(items):
    for item in items:
        try:
            process(item)  # Usually succeeds
        except ProcessingError:
            handle_error(item)

# LBYL is faster when failure is common (>10%)
def lbyl_approach(items):
    for item in items:
        if can_process(item):  # Quick check
            process(item)
        else:
            handle_error(item)
```

## 🔗 External Resources

- **[Python Glossary: EAFP](https://docs.python.org/3/glossary.html#term-eafp)**
- **[PEP 463: Exception-catching expressions](https://www.python.org/dev/peps/pep-0463/)**
- **[Effective Python: Item 14](https://effectivepython.com/)** - "Prefer Exceptions to Returning None"

## ✅ Quick Rules

1. **Use LBYL for**: Type checks, simple preconditions, safety checks
2. **Use EAFP for**: File/network operations, dictionary access, complex operations
3. **Combine both**: LBYL for validation, EAFP for execution
4. **Consider performance**: EAFP when success is common, LBYL when failure is common
5. **Follow Python idioms**: When in doubt, prefer EAFP (it's more Pythonic)
