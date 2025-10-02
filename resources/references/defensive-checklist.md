# 🛡️ Defensive Programming Checklist

Use this checklist to ensure your code follows defensive programming principles.

## 📋 Input Validation

- [ ] **Type Checking**: All inputs validated for correct type
- [ ] **Range Checking**: Numeric inputs checked for valid ranges  
- [ ] **Null/None Checking**: Handle null/None values appropriately
- [ ] **Special Values**: Check for NaN, infinity, empty strings
- [ ] **Early Validation**: Use guard clauses for immediate validation

```python
# ✅ Good example
def divide(a: float, b: float) -> float:
    if not isinstance(a, (int, float)):
        raise InvalidInputError("a must be a number")
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return a / b
```

## 🚨 Error Handling

- [ ] **Custom Exceptions**: Use specific exception types, not generic Exception
- [ ] **Error Context**: Include debugging information in exceptions
- [ ] **Error Boundaries**: Handle errors at appropriate levels
- [ ] **Graceful Degradation**: System continues working when possible
- [ ] **No Silent Failures**: All errors are logged or reported

```python
# ✅ Good exception with context
raise InvalidInputError(
    "Invalid number format", 
    {"input": user_input, "expected": "float", "error": str(e)}
)
```

## 🔍 EAFP vs LBYL

- [ ] **LBYL for Preconditions**: Check dangerous conditions first
- [ ] **EAFP for Operations**: Try operations, handle exceptions
- [ ] **Consistent Strategy**: Don't mix approaches randomly

```python
# ✅ LBYL for safety checks
if b == 0:  # Must check this first
    raise DivisionByZeroError("Cannot divide by zero")

# ✅ EAFP for operations  
try:
    result = complex_calculation(a, b)
except CalculationError as e:
    raise InvalidInputError(f"Calculation failed: {e}")
```

## 📏 Design by Contract

- [ ] **Preconditions**: Validate all inputs before processing
- [ ] **Postconditions**: Validate results before returning
- [ ] **Invariants**: Assert conditions that should always be true
- [ ] **Documentation**: Document what functions expect and guarantee

```python
def add(a: Number, b: Number) -> Number:
    # Preconditions
    _validate_input(a, "a")  
    _validate_input(b, "b")
    
    result = a + b
    
    # Postconditions
    _check_overflow(result, "addition", a, b)
    assert isinstance(result, (int, float))
    
    return result
```

## 🔐 Security & Privacy

- [ ] **No Data Leakage**: Error messages don't expose sensitive data
- [ ] **Input Sanitization**: Clean untrusted input
- [ ] **Resource Limits**: Prevent resource exhaustion attacks
- [ ] **Safe Defaults**: Choose secure default values

```python
# ❌ Bad - exposes sensitive info
raise DatabaseError(f"Connection failed: username={username}, password={password}")

# ✅ Good - safe error message  
raise DatabaseError("Database connection failed", {"attempt": attempt_count})
```

## 📊 Logging & Observability

- [ ] **Error Boundary Logging**: Log at appropriate levels
- [ ] **Structured Logging**: Use consistent log formats
- [ ] **No PII in Logs**: Keep personally identifiable information out
- [ ] **Debug Information**: Provide context for troubleshooting

```python
logger.debug(f"Processing operation: {operation_name}")
logger.error(f"Operation failed", extra={"operation": op, "inputs": sanitized_inputs})
```

## 🧪 Testing

- [ ] **Error Path Testing**: Test all error conditions
- [ ] **Edge Case Testing**: Test boundary conditions
- [ ] **Integration Testing**: Test error handling across modules
- [ ] **Recovery Testing**: Test system recovery from failures

## 🔄 Code Structure  

- [ ] **Single Responsibility**: Each function has one clear purpose
- [ ] **Fail Fast**: Detect problems early and clearly
- [ ] **Guard Clauses**: Use early returns to reduce nesting
- [ ] **Readable Error Messages**: Clear, actionable error descriptions

## 📈 Performance Considerations

- [ ] **Efficient Validation**: Don't over-validate in hot paths
- [ ] **Resource Cleanup**: Always clean up resources (files, connections)
- [ ] **Timeout Handling**: Set reasonable timeouts for operations
- [ ] **Circuit Breakers**: Fail fast when downstream services are down

## 🎯 Quality Gates

Before considering code complete, ensure:

- [ ] All unit tests pass (including error cases)
- [ ] Code coverage includes error paths
- [ ] Linting and type checking pass
- [ ] Security scanning passes  
- [ ] Manual testing of error scenarios completed

---

## 🔗 Quick References

- **[Exception Patterns](exception-patterns.md)** - Common exception handling patterns
- **[EAFP vs LBYL Guide](eafp-vs-lbyl.md)** - When to use each approach
- **[Error Message Guidelines](error-messages.md)** - Writing good error messages