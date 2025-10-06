"""Core arithmetic operations for the calculator with defensive programming.

These functions implement Design by Contract principles with:
- Explicit precondition validation (guard clauses)
- Postcondition assertions
- Comprehensive error handling with context
- Logging at error boundaries
"""

from __future__ import annotations

import logging
import math
from typing import Union

from exceptions import (
    DivisionByZeroError,
    InvalidInputError,
    OverflowError,
    UnderflowError,
)

# Set up logging
logger = logging.getLogger(__name__)

Number = Union[int, float]

# Constants for validation
MAX_SAFE_NUMBER = 1e308  # Close to float max
MIN_SAFE_NUMBER = -1e308
EPSILON = 1e-15  # For floating point comparison and division by zero check


def _validate_input(value: Number, param_name: str) -> None:
    """Guard clause for input validation.

    Args:
        value: The number to validate
        param_name: Name of the parameter for error context

    Raises:
        InvalidInputError: If input is invalid
    """
    # Check if it's a number (LBYL approach for type safety)
    if not isinstance(value, (int, float)):
        raise InvalidInputError(
            f"Parameter '{param_name}' must be a number",
            {"value": value, "type": type(value).__name__},
        )

    # Check for NaN or infinity (EAFP wouldn't work well here)
    if math.isnan(value):
        raise InvalidInputError(
            f"Parameter '{param_name}' cannot be NaN",
            {"value": value, "param": param_name},
        )

    if math.isinf(value):
        raise InvalidInputError(
            f"Parameter '{param_name}' cannot be infinite",
            {"value": value, "param": param_name},
        )


def _check_overflow(result: float, operation: str, a: Number, b: Number) -> None:
    """Check for overflow conditions.

    Args:
        result: The calculation result
        operation: Name of the operation for context
        a, b: Original operands for context

    Raises:
        OverflowError: If result is too large
        UnderflowError: If result is too small (close to zero when shouldn't be)
    """
    if math.isinf(result):
        logger.error(f"Overflow in {operation}: {a} and {b} -> {result}")
        raise OverflowError(
            f"Result overflow in {operation}",
            {"operation": operation, "operands": [a, b], "result": result},
        )

    # Check for underflow only in cases where result is unreasonably small
    # Skip underflow checks for very small input numbers (they're expected to be small)
    min_input = min(abs(a), abs(b)) if a != 0 and b != 0 else 0
    if result != 0 and abs(result) < EPSILON and min_input > EPSILON:
        logger.warning(f"Potential underflow in {operation}: {a} and {b} -> {result}")
        raise UnderflowError(
            f"Result underflow in {operation}",
            {"operation": operation, "operands": [a, b], "result": result},
        )


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b.

    Preconditions:
        - a and b must be valid numbers (not NaN or infinite)

    Postconditions:
        - Result is a valid number
        - If both inputs are integers and result fits in int range, returns int

    Args:
        a: First addend
        b: Second addend

    Returns:
        Sum of a and b

    Raises:
        InvalidInputError: If inputs are invalid
        OverflowError: If result overflows

    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 1.5)
        4.0
    """
    # Precondition validation (guard clauses)
    _validate_input(a, "a")
    _validate_input(b, "b")

    logger.debug(f"Adding {a} + {b}")

    # Perform operation (EAFP for the actual arithmetic)
    try:
        result = a + b
    except Exception as e:
        logger.error(f"Unexpected error in addition: {e}")
        raise InvalidInputError(f"Addition failed: {e}", {"a": a, "b": b})

    # Postcondition validation
    _check_overflow(result, "addition", a, b)

    # Maintain type consistency: if both inputs are integers, try to return integer
    if isinstance(a, int) and isinstance(b, int) and isinstance(result, (int, float)):
        if result == int(result):  # Can be safely converted to int
            result = int(result)

    assert isinstance(result, (int, float)), f"Result should be numeric, got {type(result)}"
    logger.debug(f"Addition result: {result}")

    return result


def subtract(a: Number, b: Number) -> Number:
    """Return the result of a minus b.

    Preconditions:
        - a and b must be valid numbers

    Postconditions:
        - Result is a valid number

    Args:
        a: Minuend
        b: Subtrahend

    Returns:
        Difference of a and b

    Raises:
        InvalidInputError: If inputs are invalid
        OverflowError: If result overflows
    """
    # Guard clauses
    _validate_input(a, "a")
    _validate_input(b, "b")

    logger.debug(f"Subtracting {a} - {b}")

    try:
        result = a - b
    except Exception as e:
        logger.error(f"Unexpected error in subtraction: {e}")
        raise InvalidInputError(f"Subtraction failed: {e}", {"a": a, "b": b})

    _check_overflow(result, "subtraction", a, b)

    # Type consistency
    if isinstance(a, int) and isinstance(b, int) and isinstance(result, (int, float)):
        if result == int(result):
            result = int(result)

    assert isinstance(result, (int, float)), f"Result should be numeric, got {type(result)}"
    logger.debug(f"Subtraction result: {result}")

    return result


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b.

    Preconditions:
        - a and b must be valid numbers

    Postconditions:
        - Result is a valid number
        - multiply(a, 0) == 0 for any valid a
        - multiply(a, 1) == a for any valid a

    Args:
        a: First factor
        b: Second factor

    Returns:
        Product of a and b

    Raises:
        InvalidInputError: If inputs are invalid
        OverflowError: If result overflows
    """
    # Guard clauses
    _validate_input(a, "a")
    _validate_input(b, "b")

    logger.debug(f"Multiplying {a} * {b}")

    # Early return for special cases (optimization + clarity)
    if a == 0 or b == 0:
        logger.debug("Multiplication by zero, returning 0")
        return 0

    if a == 1:
        logger.debug("Multiplication by 1, returning second operand")
        return b

    if b == 1:
        logger.debug("Multiplication by 1, returning first operand")
        return a

    try:
        result = a * b
    except Exception as e:
        logger.error(f"Unexpected error in multiplication: {e}")
        raise InvalidInputError(f"Multiplication failed: {e}", {"a": a, "b": b})

    _check_overflow(result, "multiplication", a, b)

    # Type consistency
    if isinstance(a, int) and isinstance(b, int) and isinstance(result, (int, float)):
        if result == int(result):
            result = int(result)

    # Postcondition assertions
    assert isinstance(result, (int, float)), f"Result should be numeric, got {type(result)}"

    # Contract assertions for special cases
    if a == 0 or b == 0:
        assert result == 0, "Multiplication by zero should yield zero"

    logger.debug(f"Multiplication result: {result}")

    return result


def divide(a: Number, b: Number) -> float:
    """Return the result of a divided by b.

    Preconditions:
        - a and b must be valid numbers
        - b must not be zero

    Postconditions:
        - Result is a valid float
        - divide(a, 1) == a for any valid a
        - divide(0, b) == 0 for any valid non-zero b

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Quotient of a and b as float

    Raises:
        InvalidInputError: If inputs are invalid
        DivisionByZeroError: If divisor is zero
        OverflowError: If result overflows

    Examples:
        >>> divide(6, 3)
        2.0
        >>> divide(1, 3)
        0.3333333333333333
    """
    # Guard clauses for preconditions
    _validate_input(a, "a")
    _validate_input(b, "b")

    # Check for division by zero (LBYL approach - we must check this)
    if b == 0:
        logger.error(f"Division by zero attempted: {a} / {b}")
        raise DivisionByZeroError("Cannot divide by zero", {"dividend": a, "divisor": b})

    # Additional check for very small divisors that might cause overflow
    if abs(b) < EPSILON:
        logger.warning(f"Division by very small number: {a} / {b}")
        raise DivisionByZeroError(
            "Cannot divide by number too close to zero",
            {"dividend": a, "divisor": b, "threshold": EPSILON},
        )

    logger.debug(f"Dividing {a} / {b}")

    # Special case: zero divided by anything (except zero) is zero
    if a == 0:
        logger.debug("Division of zero, returning 0.0")
        return 0.0

    # Perform division (EAFP for the arithmetic operation)
    try:
        result = a / b
    except Exception as e:
        logger.error(f"Unexpected error in division: {e}")
        raise InvalidInputError(f"Division failed: {e}", {"a": a, "b": b})

    # Postcondition validation
    _check_overflow(result, "division", a, b)

    # Always return float for division
    result = float(result)

    # Postcondition assertions
    assert isinstance(result, float), f"Division should return float, got {type(result)}"
    assert not math.isnan(result), "Division result should not be NaN"

    # Contract assertions
    if a == 0:
        assert result == 0.0, "Zero divided by non-zero should be zero"
    if b == 1:
        assert abs(result - a) < EPSILON, "Division by 1 should return original value"

    logger.debug(f"Division result: {result}")

    return result
