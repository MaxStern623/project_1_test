"""Tests for custom exceptions - PRACTICE VERSION

These tests validate your exception implementation.
All tests should pass when you correctly implement the exceptions module.
"""

import pytest

# TODO: Update these imports when you implement the exceptions
try:
    from src.exceptions import (
        CalculatorError,
        DivisionByZeroError,
        InvalidInputError,
        OverflowError,
        UnderflowError,
    )

    EXCEPTIONS_IMPLEMENTED = True
except ImportError:
    # Create placeholder classes for testing
    class CalculatorError(Exception):
        def __init__(self, message, context=None):
            super().__init__(message)
            self.context = context or {}

    class InvalidInputError(CalculatorError):
        pass

    class DivisionByZeroError(CalculatorError):
        pass

    class OverflowError(CalculatorError):
        pass

    class UnderflowError(CalculatorError):
        pass

    EXCEPTIONS_IMPLEMENTED = False


class TestCustomExceptions:
    """Test custom exception hierarchy and functionality."""

    def test_calculator_error_base_class(self):
        """Test that CalculatorError is the base exception."""
        error = CalculatorError("Test error")
        assert isinstance(error, Exception)
        assert str(error) == "Test error"

    def test_calculator_error_with_context(self):
        """Test CalculatorError with context information."""
        context = {"operation": "test", "values": [1, 2]}
        error = CalculatorError("Test error with context", context)

        assert str(error) == "Test error with context"
        assert hasattr(error, "context"), "CalculatorError should have context attribute"
        assert error.context == context
        assert "operation" in error.context
        assert "values" in error.context

    def test_calculator_error_without_context(self):
        """Test CalculatorError without context defaults to empty dict."""
        error = CalculatorError("Test error")
        assert hasattr(error, "context"), "CalculatorError should have context attribute"
        assert error.context == {}

    @pytest.mark.skipif(not EXCEPTIONS_IMPLEMENTED, reason="Exceptions not yet implemented")
    def test_invalid_input_error_inheritance(self):
        """Test that InvalidInputError inherits from CalculatorError."""
        error = InvalidInputError("Invalid input")
        assert isinstance(error, CalculatorError)
        assert isinstance(error, Exception)

    @pytest.mark.skipif(not EXCEPTIONS_IMPLEMENTED, reason="Exceptions not yet implemented")
    def test_division_by_zero_error_inheritance(self):
        """Test that DivisionByZeroError inherits from CalculatorError."""
        error = DivisionByZeroError("Division by zero")
        assert isinstance(error, CalculatorError)
        assert isinstance(error, Exception)

    @pytest.mark.skipif(not EXCEPTIONS_IMPLEMENTED, reason="Exceptions not yet implemented")
    def test_overflow_error_inheritance(self):
        """Test that OverflowError inherits from CalculatorError."""
        error = OverflowError("Overflow occurred")
        assert isinstance(error, CalculatorError)
        assert isinstance(error, Exception)

    @pytest.mark.skipif(not EXCEPTIONS_IMPLEMENTED, reason="Exceptions not yet implemented")
    def test_underflow_error_inheritance(self):
        """Test that UnderflowError inherits from CalculatorError."""
        error = UnderflowError("Underflow occurred")
        assert isinstance(error, CalculatorError)
        assert isinstance(error, Exception)

    def test_specific_errors_with_context(self):
        """Test that specific error types work with context."""
        context = {"dividend": 5, "divisor": 0}
        error = DivisionByZeroError("Cannot divide by zero", context)

        assert str(error) == "Cannot divide by zero"
        if EXCEPTIONS_IMPLEMENTED:
            assert error.context == context
            assert error.context["dividend"] == 5
            assert error.context["divisor"] == 0

    @pytest.mark.skipif(not EXCEPTIONS_IMPLEMENTED, reason="Exceptions not yet implemented")
    def test_exception_can_be_caught_as_calculator_error(self):
        """Test that specific exceptions can be caught as CalculatorError."""
        try:
            raise InvalidInputError("Test invalid input")
        except CalculatorError as e:
            assert isinstance(e, InvalidInputError)
            assert isinstance(e, CalculatorError)

        try:
            raise DivisionByZeroError("Test division by zero")
        except CalculatorError as e:
            assert isinstance(e, DivisionByZeroError)
            assert isinstance(e, CalculatorError)
