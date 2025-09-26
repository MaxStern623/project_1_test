"""Core arithmetic operations - PRACTICE VERSION for defensive programming

TODO: Implement defensive programming principles in arithmetic operations.

DEFENSIVE PROGRAMMING PRINCIPLES TO IMPLEMENT:
1. Input validation (guard clauses) - LBYL approach for type safety
2. Pre-condition and post-condition checks
3. Custom exceptions with context information
4. Logging at error boundaries
5. Design by Contract assertions
6. EAFP vs LBYL - choose appropriate strategy for each case

HINTS:
- Use _validate_input() helper for input validation
- Add logging for operations and errors
- Use custom exceptions instead of generic ones
- Add assertions for contract validation
- Handle edge cases (zero, one, very large/small numbers)
- Always validate that inputs are numbers and not NaN/infinite
"""

from __future__ import annotations

import logging
from typing import Union

# TODO: Import your custom exceptions
# HINT: from src.exceptions import ...

# Set up logging
logger = logging.getLogger(__name__)

Number = Union[int, float]

# Constants for validation
MAX_SAFE_NUMBER = 1e308  # Close to float max
MIN_SAFE_NUMBER = -1e308
EPSILON = 1e-15  # For floating point comparison


# TODO: Implement _validate_input helper function
# HINT: This should check if value is a number, not NaN, not infinite
# HINT: Raise InvalidInputError with appropriate context if invalid
def _validate_input(value: Number, param_name: str) -> None:
    """Guard clause for input validation.

    Args:
        value: The number to validate
        param_name: Name of the parameter for error context

    Raises:
        InvalidInputError: If input is invalid
    """
    # TODO: Check if it's a number (isinstance)
    # TODO: Check for NaN using math.isnan()
    # TODO: Check for infinity using math.isinf()
    # TODO: Raise InvalidInputError with context if any validation fails
    pass


# TODO: Implement _check_overflow helper function
# HINT: Check if result is infinite or extremely small
# HINT: Raise OverflowError or UnderflowError with context
def _check_overflow(result: float, operation: str, a: Number, b: Number) -> None:
    """Check for overflow conditions.

    Args:
        result: The calculation result
        operation: Name of the operation for context
        a, b: Original operands for context

    Raises:
        OverflowError: If result is too large
        UnderflowError: If result is too small
    """
    # TODO: Check if result is infinite using math.isinf()
    # TODO: Check if result is very small (potential underflow)
    # TODO: Use logger.error() for overflow conditions
    # TODO: Use logger.warning() for underflow conditions
    # TODO: Raise appropriate exceptions with context
    pass


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b.

    TODO: Implement defensive programming principles:
    1. Input validation using guard clauses
    2. Logging for operation start/end
    3. Overflow checking
    4. Type consistency (preserve int when possible)
    5. Postcondition assertions

    HINTS:
    - Call _validate_input() for both parameters
    - Use logger.debug() for operation logging
    - Use try/catch for the actual arithmetic (EAFP)
    - Call _check_overflow() after calculation
    - Add assertions for postconditions
    """
    # TODO: Add input validation (guard clauses)

    # TODO: Add debug logging

    # TODO: Perform addition with error handling

    # TODO: Check for overflow

    # TODO: Handle type consistency (int preservation)

    # TODO: Add postcondition assertions

    return a + b  # TODO: Replace with proper implementation


def subtract(a: Number, b: Number) -> Number:
    """Return the result of a minus b.

    TODO: Follow same defensive programming pattern as add()
    """
    # TODO: Implement defensive programming for subtraction
    # HINT: Follow the same pattern as add() function
    return a - b  # TODO: Replace with proper implementation


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b.

    TODO: Implement defensive programming with special attention to:
    1. Multiplication by zero contract (should always return 0)
    2. Multiplication by one contract (should return original value)
    3. Early return optimizations for special cases

    HINT: Add contract assertions for special cases
    """
    # TODO: Add input validation

    # TODO: Add logging

    # TODO: Handle special cases (0 and 1) with early returns
    # HINT: if a == 0 or b == 0: return 0
    # HINT: if a == 1: return b, if b == 1: return a

    # TODO: Perform multiplication with error handling

    # TODO: Add contract assertions
    # HINT: assert conditions for multiply by 0 and 1 contracts

    return a * b  # TODO: Replace with proper implementation


def divide(a: Number, b: Number) -> float:
    """Return the result of a divided by b.

    TODO: Implement most comprehensive defensive programming:
    1. Check for exact zero division
    2. Check for very small divisors (near zero)
    3. Special case for zero dividend
    4. Always return float
    5. Contract assertions for division by 1 and zero dividend

    CRITICAL: Use LBYL approach for division by zero check (must check before attempting)
    """
    # TODO: Add input validation

    # TODO: Check for division by zero (exact)
    # HINT: if b == 0: raise DivisionByZeroError

    # TODO: Check for very small divisors
    # HINT: if abs(b) < EPSILON: raise DivisionByZeroError

    # TODO: Add logging

    # TODO: Handle special case: zero dividend
    # HINT: if a == 0: return 0.0

    # TODO: Perform division with error handling

    # TODO: Check for overflow

    # TODO: Ensure result is float

    # TODO: Add contract assertions
    # HINT: Check division by 1 and zero dividend contracts

    return a / b  # TODO: Replace with proper implementation
