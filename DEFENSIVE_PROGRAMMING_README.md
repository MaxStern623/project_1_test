# A1 Defensive Programming - Calculator Project

This project implements defensive programming principles for a simple calculator application, following the requirements from A1-defensive-programming.md.

## Project Structure

### Two Versions Created:

1. **`answers/`** - Complete implementation with all defensive programming principles
2. **`practice/`** - Incomplete version with TODOs and hints for learning

## Defensive Programming Principles Implemented

### In the Answers Version:

1. **Input Validation (Guard Clauses)**
   - Type checking for all inputs
   - NaN and infinity rejection
   - Parameter validation with meaningful error messages

2. **Custom Exception Hierarchy**
   - `CalculatorError` base class with context support
   - `InvalidInputError` for input validation failures
   - `DivisionByZeroError` for division by zero
   - `OverflowError` and `UnderflowError` for numerical limits

3. **Design by Contract**
   - Pre-condition validation in all operations
   - Post-condition assertions
   - Contract assertions for special cases (multiply by 0/1, divide by 1)

4. **EAFP vs LBYL Strategy**
   - LBYL for type and NaN/infinity checking (must validate before use)
   - EAFP for arithmetic operations (try calculation, handle exceptions)
   - LBYL for division by zero (must check before dividing)

5. **Comprehensive Logging**
   - Debug logging for operation flow
   - Error logging at failure boundaries
   - Warning logging for edge cases
   - Structured logging with context

6. **Error Context and Communication**
   - All exceptions include context dictionaries
   - Clear, actionable error messages
   - Different exit codes for different error types
   - No sensitive data leakage in error messages

### Key Features:

#### Operations Module (`src/operations/__init__.py`)
- **Input validation**: Rejects non-numeric, NaN, and infinite inputs
- **Overflow detection**: Catches arithmetic overflow/underflow
- **Type preservation**: Maintains integer types when possible
- **Contract validation**: Asserts mathematical contracts (e.g., x*0=0, x*1=x)
- **Special case handling**: Early returns for 0 and 1 in multiplication

#### CLI Module (`src/main.py`)
- **Structured error handling**: Different exit codes for different error types
- **Verbose logging**: Optional detailed logging output
- **Input validation**: Validates command-line arguments before processing
- **Graceful error recovery**: Catches and handles all exception types

#### Exception Module (`src/exceptions.py`)
- **Hierarchical exceptions**: Specific exception types for different scenarios
- **Context preservation**: All exceptions carry context information
- **Clear inheritance**: All custom exceptions inherit from CalculatorError

## Running the Code

### Answers Version (Complete Implementation):
```bash
# Navigate to project root
cd /path/to/Project_test

# Run operations (from project root)
python -m answers.src.main add 2 3
python -m answers.src.main --verbose divide 6 3
python -m answers.src.main multiply 4 5

# Run tests
pytest answers/tests/ -v
```

### Practice Version (Learning Exercise):
```bash
# Run current (incomplete) implementation
python -m practice.src.main add 2 3

# Run tests to see what needs to be implemented
pytest practice/tests/ -v

# As you implement features, more tests will pass
```

## Learning Path for Practice Version

### Step 1: Implement Custom Exceptions
Edit `practice/src/exceptions.py`:
1. Complete the `CalculatorError` base class with context support
2. Implement all specific exception classes inheriting from `CalculatorError`
3. Run `pytest practice/tests/test_exceptions.py -v` to validate

### Step 2: Implement Operations with Defensive Programming
Edit `practice/src/operations/__init__.py`:
1. Implement `_validate_input()` helper function
2. Implement `_check_overflow()` helper function
3. Add defensive programming to each operation:
   - Input validation (guard clauses)
   - Logging
   - Error handling with custom exceptions
   - Contract assertions
4. Run `pytest practice/tests/test_operations.py -v` to validate

### Step 3: Enhance CLI with Error Handling
Edit `practice/src/main.py`:
1. Implement `setup_logging()` function
2. Implement `validate_operation_args()` function
3. Complete argument parsing with verbose flag
4. Add structured error handling with appropriate exit codes
5. Run `pytest practice/tests/test_cli.py -v` to validate

### Step 4: Verify Complete Implementation
```bash
# All tests should pass
pytest practice/tests/ -v

# CLI should work like the answers version
python -m practice.src.main --verbose add 2 3
```

## Testing Strategy

The test suite covers:
- **Happy path scenarios**: Normal operations with valid inputs
- **Error conditions**: Invalid inputs, edge cases, boundary conditions
- **Contract validation**: Mathematical contracts and invariants
- **Exception handling**: Proper exception types and context
- **CLI functionality**: Exit codes, error messages, verbose mode
- **Implementation verification**: Checks for required features

## Key Learning Objectives

1. **When to use LBYL vs EAFP**:
   - LBYL: Type checking, NaN/infinity detection, division by zero
   - EAFP: Arithmetic operations, file operations, network operations

2. **Guard Clauses**: Early validation and return to reduce nesting

3. **Custom Exception Design**: Specific, actionable exceptions with context

4. **Contract Programming**: Explicit pre/post-conditions and invariants

5. **Error Boundary Logging**: Logging at the right abstraction level

6. **Graceful Degradation**: Failing fast with useful error messages

## Common Defensive Programming Patterns Demonstrated

1. **Input Validation Pattern**:
   ```python
   def _validate_input(value, param_name):
       if not isinstance(value, (int, float)):
           raise InvalidInputError(f"Parameter '{param_name}' must be a number")
       if math.isnan(value):
           raise InvalidInputError(f"Parameter '{param_name}' cannot be NaN")
   ```

2. **Guard Clause Pattern**:
   ```python
   def divide(a, b):
       _validate_input(a, "a")  # Guard clause
       _validate_input(b, "b")  # Guard clause
       if b == 0:               # Guard clause
           raise DivisionByZeroError("Cannot divide by zero")
       # Main logic here
   ```

3. **Contract Assertion Pattern**:
   ```python
   def multiply(a, b):
       result = a * b
       # Contract assertions
       if a == 0 or b == 0:
           assert result == 0, "Multiplication by zero should yield zero"
       return result
   ```

4. **Error Context Pattern**:
   ```python
   except Exception as e:
       raise InvalidInputError(
           "Operation failed",
           {"operation": "multiply", "operands": [a, b], "error": str(e)}
       ) from e
   ```

This structure provides both a complete reference implementation and a guided learning experience for defensive programming principles.
