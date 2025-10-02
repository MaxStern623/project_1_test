"""Custom exception classes for the calculator with defensive programming."""

from __future__ import annotations

from typing import Any


class CalculatorError(Exception):
    """Base exception for all calculator-related errors."""

    def __init__(self, message: str, context: dict[str, Any] | None = None):
        super().__init__(message)
        self.context = context or {}


class InvalidInputError(CalculatorError):
    """Raised when input parameters are invalid."""

    pass


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

    pass


class OverflowError(CalculatorError):
    """Raised when calculation results in overflow."""

    pass


class UnderflowError(CalculatorError):
    """Raised when calculation results in underflow."""

    pass
