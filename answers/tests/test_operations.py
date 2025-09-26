"""Comprehensive tests for calculator operations with defensive programming.

Tests cover:
- Normal operation paths
- Error conditions and edge cases
- Contract validation (pre/post conditions)
- Custom exception handling
- Input validation
"""

import math

import pytest

from answers.src.exceptions import (
    DivisionByZeroError,
    InvalidInputError,
    OverflowError,
    UnderflowError,
)
from answers.src.operations import add, divide, multiply, subtract


class TestInputValidation:
    """Test input validation across all operations."""

    @pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
    @pytest.mark.parametrize(
        "invalid_input",
        [
            "string",
            None,
            [],
            {},
            complex(1, 2),
        ],
    )
    def test_invalid_type_first_arg(self, operation, invalid_input):
        """Test that invalid types for first argument raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="must be a number"):
            operation(invalid_input, 1)

    @pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
    @pytest.mark.parametrize(
        "invalid_input",
        [
            "string",
            None,
            [],
            {},
            complex(1, 2),
        ],
    )
    def test_invalid_type_second_arg(self, operation, invalid_input):
        """Test that invalid types for second argument raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="must be a number"):
            operation(1, invalid_input)

    @pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
    def test_nan_input_first_arg(self, operation):
        """Test that NaN inputs raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="cannot be NaN"):
            operation(float("nan"), 1)

    @pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
    def test_nan_input_second_arg(self, operation):
        """Test that NaN inputs raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="cannot be NaN"):
            operation(1, float("nan"))

    @pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
    def test_infinity_input_first_arg(self, operation):
        """Test that infinite inputs raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="cannot be infinite"):
            operation(float("inf"), 1)

    @pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
    def test_infinity_input_second_arg(self, operation):
        """Test that infinite inputs raise InvalidInputError."""
        with pytest.raises(InvalidInputError, match="cannot be infinite"):
            operation(1, float("inf"))


class TestAddOperation:
    """Test addition with comprehensive coverage."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (0, 0, 0),
            (2, 3, 5),
            (-2, 3, 1),
            (2.5, 0.5, 3.0),
            (-5, -3, -8),
            (1000000, 2000000, 3000000),
        ],
    )
    def test_add_valid_inputs(self, a, b, expected):
        """Test addition with valid inputs."""
        result = add(a, b)
        assert result == expected
        assert isinstance(result, (int, float))

    def test_add_integer_preservation(self):
        """Test that integer inputs return integer when possible."""
        result = add(2, 3)
        assert result == 5
        assert isinstance(result, int)

    def test_add_float_result(self):
        """Test that float inputs return float."""
        result = add(2.5, 3.5)
        assert result == 6.0
        assert isinstance(result, float)

    def test_add_mixed_types(self):
        """Test addition with mixed int/float types."""
        result = add(2, 3.5)
        assert result == 5.5
        assert isinstance(result, float)


class TestSubtractOperation:
    """Test subtraction with comprehensive coverage."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (0, 0, 0),
            (5, 3, 2),
            (-2, -3, 1),
            (2.5, 0.5, 2.0),
            (3, 5, -2),
        ],
    )
    def test_subtract_valid_inputs(self, a, b, expected):
        """Test subtraction with valid inputs."""
        result = subtract(a, b)
        assert result == expected

    def test_subtract_integer_preservation(self):
        """Test that integer inputs return integer when possible."""
        result = subtract(5, 3)
        assert result == 2
        assert isinstance(result, int)


class TestMultiplyOperation:
    """Test multiplication with comprehensive coverage."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (0, 0, 0),
            (2, 3, 6),
            (-2, 3, -6),
            (2.5, 2, 5.0),
            (1, 5, 5),
            (5, 1, 5),
        ],
    )
    def test_multiply_valid_inputs(self, a, b, expected):
        """Test multiplication with valid inputs."""
        result = multiply(a, b)
        assert result == expected

    def test_multiply_by_zero(self):
        """Test multiplication by zero returns zero."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0

    def test_multiply_by_one(self):
        """Test multiplication by one returns original value."""
        assert multiply(1, 5) == 5
        assert multiply(5, 1) == 5
        assert multiply(1, 1) == 1

    def test_multiply_integer_preservation(self):
        """Test that integer inputs return integer when possible."""
        result = multiply(2, 3)
        assert result == 6
        assert isinstance(result, int)


class TestDivideOperation:
    """Test division with comprehensive coverage."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (6, 3, 2.0),
            (2.5, 0.5, 5.0),
            (-6, 3, -2.0),
            (0, 5, 0.0),
            (7, 2, 3.5),
        ],
    )
    def test_divide_valid_inputs(self, a, b, expected):
        """Test division with valid inputs."""
        result = divide(a, b)
        assert math.isclose(result, expected)
        assert isinstance(result, float)

    def test_divide_by_zero_exact(self):
        """Test division by exact zero raises DivisionByZeroError."""
        with pytest.raises(DivisionByZeroError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_divide_by_very_small_number(self):
        """Test division by very small number raises DivisionByZeroError."""
        with pytest.raises(DivisionByZeroError, match="too close to zero"):
            divide(5, 1e-16)

    def test_divide_zero_by_number(self):
        """Test that zero divided by any non-zero number returns 0.0."""
        result = divide(0, 5)
        assert result == 0.0
        assert isinstance(result, float)

    def test_divide_by_one(self):
        """Test division by one returns original value as float."""
        result = divide(5, 1)
        assert result == 5.0
        assert isinstance(result, float)

    def test_divide_always_returns_float(self):
        """Test that division always returns float, even for integer inputs."""
        result = divide(6, 3)
        assert result == 2.0
        assert isinstance(result, float)


class TestErrorContexts:
    """Test that errors provide useful context information."""

    def test_invalid_input_error_context(self):
        """Test that InvalidInputError includes helpful context."""
        with pytest.raises(InvalidInputError) as exc_info:
            add("invalid", 5)

        error = exc_info.value
        assert hasattr(error, "context")
        assert "value" in error.context
        assert "type" in error.context

    def test_division_by_zero_context(self):
        """Test that DivisionByZeroError includes context."""
        with pytest.raises(DivisionByZeroError) as exc_info:
            divide(5, 0)

        error = exc_info.value
        assert hasattr(error, "context")
        assert "dividend" in error.context
        assert "divisor" in error.context
        assert error.context["dividend"] == 5
        assert error.context["divisor"] == 0


class TestContractValidation:
    """Test design by contract assertions and invariants."""

    def test_multiplication_zero_contract(self):
        """Test that multiply(a, 0) == 0 contract holds."""
        for a in [0, 1, -1, 5, -5, 3.14, -2.718]:
            assert multiply(a, 0) == 0
            assert multiply(0, a) == 0

    def test_multiplication_one_contract(self):
        """Test that multiply(a, 1) == a contract holds."""
        for a in [0, 1, -1, 5, -5, 3.14, -2.718]:
            assert multiply(a, 1) == a
            assert multiply(1, a) == a

    def test_division_one_contract(self):
        """Test that divide(a, 1) == a contract holds."""
        for a in [0, 1, -1, 5, -5, 3.14, -2.718]:
            result = divide(a, 1)
            assert abs(result - a) < 1e-15  # Account for float precision

    def test_division_zero_contract(self):
        """Test that divide(0, b) == 0 for non-zero b."""
        for b in [1, -1, 5, -5, 3.14, -2.718, 0.1, -0.1]:
            result = divide(0, b)
            assert result == 0.0


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_very_large_numbers(self):
        """Test operations with very large numbers."""
        large_num = 1e100

        # Should work for addition
        result = add(large_num, 1)
        assert result > large_num

        # Should work for multiplication
        result = multiply(large_num, 2)
        assert result == 2 * large_num

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        small_num = 1e-100

        # Should work for addition
        result = add(small_num, small_num)
        assert result == 2 * small_num

        # Should work for division
        result = divide(small_num, 2)
        assert result == small_num / 2

    def test_precision_edge_cases(self):
        """Test floating point precision edge cases."""
        # Classic floating point issue
        a, b = 0.1, 0.2
        result = add(a, b)
        # Should be close to 0.3, but might not be exact due to float precision
        assert abs(result - 0.3) < 1e-15

        # Division that should yield clean result
        result = divide(1, 3)
        expected = 1.0 / 3.0
        assert abs(result - expected) < 1e-15


class TestLoggingIntegration:
    """Test that operations integrate properly with logging."""

    def test_operations_dont_crash_without_logging_setup(self):
        """Test that operations work even without explicit logging setup."""
        # This should not raise any exceptions
        result = add(2, 3)
        assert result == 5

        result = divide(6, 3)
        assert result == 2.0

    def test_error_paths_work_with_logging(self):
        """Test that error paths don't break due to logging."""
        with pytest.raises(DivisionByZeroError):
            divide(5, 0)

        with pytest.raises(InvalidInputError):
            add("invalid", 5)
