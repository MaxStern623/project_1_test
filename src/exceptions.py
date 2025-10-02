"""Custom exceptions for the calculator application - PRACTICE VERSION

TODO: Implement custom exceptions following defensive programming principles.

HINTS:
1. Create a base CalculatorError exception that inherits from Exception
2. Add context parameter to store additional error information
3. Create specific exception types for different error conditions:
   - InvalidInputError: For invalid input parameters
   - DivisionByZeroError: For division by zero attempts
   - OverflowError: For calculation overflow
   - UnderflowError: For calculation underflow
4. Make sure all specific exceptions inherit from CalculatorError
5. Add meaningful docstrings explaining when each exception is raised

DEFENSIVE PROGRAMMING PRINCIPLES TO APPLY:
- Clear error communication with actionable messages
- Structured error hierarchy for different handling strategies
- Context information for debugging without leaking sensitive data
"""

from __future__ import annotations


# TODO: Implement CalculatorError base class
# HINT: Should accept message and optional context dict
class CalculatorError(Exception):
    """Base exception for all calculator-related errors."""

    # TODO: Add __init__ method that accepts message and optional context
    pass


# TODO: Implement InvalidInputError
# HINT: This should inherit from CalculatorError
class InvalidInputError:
    """Raised when input parameters are invalid."""

    # TODO: Implement this exception class
    pass


# TODO: Implement DivisionByZeroError
# HINT: This should inherit from CalculatorError
# TODO: Implement this exception class


# TODO: Implement OverflowError
# HINT: This should inherit from CalculatorError
# TODO: Implement this exception class


# TODO: Implement UnderflowError
# HINT: This should inherit from CalculatorError
# TODO: Implement this exception class
