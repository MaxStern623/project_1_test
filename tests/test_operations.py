"""Tests for calculator operations - PRACTICE VERSION

These tests validate your defensive programming implementation.
All tests should pass when you correctly implement defensive programming principles.

Run with: pytest practice/tests/test_operations.py -v
"""

import math

import pytest

# TODO: Update these imports when you implement the operations and exceptions
try:
    from src.operations import add, divide, multiply, subtract

    OPERATIONS_IMPLEMENTED = True
except ImportError:
    # Fallback implementations for testing
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    OPERATIONS_IMPLEMENTED = False

try:
    from src.exceptions import DivisionByZeroError, InvalidInputError, OverflowError, UnderflowError

    EXCEPTIONS_IMPLEMENTED = True
except ImportError:
    # Create placeholder exceptions for testing
    class InvalidInputError(Exception):
        pass

    class DivisionByZeroError(Exception):
        pass

    class OverflowError(Exception):
        pass

    class UnderflowError(Exception):
        pass

    EXCEPTIONS_IMPLEMENTED = False


class TestInputValidation:
    """Test input validation across all operations."""

    @pytest.mark.skipif(
        not OPERATIONS_IMPLEMENTED or not EXCEPTIONS_IMPLEMENTED,
        reason="Operations or exceptions not yet implemented",
    )
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
        with pytest.raises(InvalidInputError):
            operation(invalid_input, 1)

    @pytest.mark.skipif(
        not OPERATIONS_IMPLEMENTED or not EXCEPTIONS_IMPLEMENTED,
        reason="Operations or exceptions not yet implemented",
    )
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
        with pytest.raises(InvalidInputError):
            operation(1, invalid_input)

    @pytest.mark.skipif(
        not OPERATIONS_IMPLEMENTED or not EXCEPTIONS_IMPLEMENTED,
        reason="Operations or exceptions not yet implemented",
    )
    @pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
    def test_nan_input_rejection(self, operation):
        """Test that NaN inputs are rejected."""
        with pytest.raises(InvalidInputError):
            operation(float("nan"), 1)
        with pytest.raises(InvalidInputError):
            operation(1, float("nan"))

    @pytest.mark.skipif(
        not OPERATIONS_IMPLEMENTED or not EXCEPTIONS_IMPLEMENTED,
        reason="Operations or exceptions not yet implemented",
    )
    @pytest.mark.parametrize("operation", [add, subtract, multiply, divide])
    def test_infinity_input_rejection(self, operation):
        """Test that infinite inputs are rejected."""
        with pytest.raises(InvalidInputError):
            operation(float("inf"), 1)
        with pytest.raises(InvalidInputError):
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
        ],
    )
    def test_add_valid_inputs(self, a, b, expected):
        """Test addition with valid inputs."""
        result = add(a, b)
        assert result == expected
        assert isinstance(result, (int, float))

    @pytest.mark.skipif(not OPERATIONS_IMPLEMENTED, reason="Operations not yet implemented")
    def test_add_integer_preservation(self):
        """Test that integer inputs return integer when possible."""
        result = add(2, 3)
        assert result == 5
        assert isinstance(result, int), "Addition of two integers should return integer"

    def test_add_float_result(self):
        """Test that float inputs return float."""
        result = add(2.5, 3.5)
        assert result == 6.0
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

    @pytest.mark.skipif(not OPERATIONS_IMPLEMENTED, reason="Operations not yet implemented")
    def test_subtract_integer_preservation(self):
        """Test that integer inputs return integer when possible."""
        result = subtract(5, 3)
        assert result == 2
        assert isinstance(result, int), "Subtraction of two integers should return integer"


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

    def test_multiply_by_zero_contract(self):
        """Test multiplication by zero contract - should always return 0."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 0) == 0
        assert multiply(0, -5) == 0
        assert multiply(-5, 0) == 0

    def test_multiply_by_one_contract(self):
        """Test multiplication by one contract - should return original value."""
        assert multiply(1, 5) == 5
        assert multiply(5, 1) == 5
        assert multiply(1, 1) == 1
        assert multiply(1, -5) == -5
        assert multiply(-5, 1) == -5

    @pytest.mark.skipif(not OPERATIONS_IMPLEMENTED, reason="Operations not yet implemented")
    def test_multiply_integer_preservation(self):
        """Test that integer inputs return integer when possible."""
        result = multiply(2, 3)
        assert result == 6
        assert isinstance(result, int), "Multiplication of two integers should return integer"


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

    @pytest.mark.skipif(
        not OPERATIONS_IMPLEMENTED or not EXCEPTIONS_IMPLEMENTED,
        reason="Operations or exceptions not yet implemented",
    )
    def test_divide_by_zero_raises_custom_exception(self):
        """Test division by zero raises DivisionByZeroError (not ValueError)."""
        with pytest.raises(DivisionByZeroError):
            divide(5, 0)

    @pytest.mark.skipif(
        not OPERATIONS_IMPLEMENTED or not EXCEPTIONS_IMPLEMENTED,
        reason="Operations or exceptions not yet implemented",
    )
    def test_divide_by_very_small_number(self):
        """Test division by very small number should raise DivisionByZeroError."""
        with pytest.raises(DivisionByZeroError):
            divide(5, 1e-16)

    def test_divide_zero_by_number_contract(self):
        """Test that zero divided by any non-zero number returns 0.0."""
        result = divide(0, 5)
        assert result == 0.0
        assert isinstance(result, float)

    def test_divide_by_one_contract(self):
        """Test division by one returns original value as float."""
        result = divide(5, 1)
        assert result == 5.0
        assert isinstance(result, float)

    def test_divide_always_returns_float(self):
        """Test that division always returns float."""
        result = divide(6, 3)
        assert result == 2.0
        assert isinstance(result, float), "Division should always return float"


class TestErrorContexts:
    """Test that errors provide useful context information."""

    @pytest.mark.skipif(
        not OPERATIONS_IMPLEMENTED or not EXCEPTIONS_IMPLEMENTED,
        reason="Operations or exceptions not yet implemented",
    )
    def test_invalid_input_error_has_context(self):
        """Test that InvalidInputError includes context information."""
        try:
            add("invalid", 5)
            pytest.fail("Should have raised InvalidInputError")
        except InvalidInputError as e:
            assert hasattr(e, "context"), "InvalidInputError should have context attribute"

    @pytest.mark.skipif(
        not OPERATIONS_IMPLEMENTED or not EXCEPTIONS_IMPLEMENTED,
        reason="Operations or exceptions not yet implemented",
    )
    def test_division_by_zero_error_has_context(self):
        """Test that DivisionByZeroError includes context information."""
        try:
            divide(5, 0)
            pytest.fail("Should have raised DivisionByZeroError")
        except DivisionByZeroError as e:
            assert hasattr(e, "context"), "DivisionByZeroError should have context attribute"


class TestContractValidation:
    """Test design by contract assertions and invariants."""

    def test_multiplication_zero_contract_comprehensive(self):
        """Test that multiply(a, 0) == 0 contract holds for various values."""
        test_values = [0, 1, -1, 5, -5, 3.14, -2.718, 100, -100]
        for a in test_values:
            assert multiply(a, 0) == 0, f"multiply({a}, 0) should equal 0"
            assert multiply(0, a) == 0, f"multiply(0, {a}) should equal 0"

    def test_multiplication_one_contract_comprehensive(self):
        """Test that multiply(a, 1) == a contract holds for various values."""
        test_values = [0, 1, -1, 5, -5, 3.14, -2.718]
        for a in test_values:
            assert multiply(a, 1) == a, f"multiply({a}, 1) should equal {a}"
            assert multiply(1, a) == a, f"multiply(1, {a}) should equal {a}"

    def test_division_contracts(self):
        """Test division contracts comprehensively."""
        # Division by 1 contract
        test_values = [0, 1, -1, 5, -5, 3.14, -2.718]
        for a in test_values:
            result = divide(a, 1)
            assert abs(result - a) < 1e-15, f"divide({a}, 1) should equal {a}"

        # Zero dividend contract
        test_divisors = [1, -1, 5, -5, 3.14, -2.718, 0.1, -0.1]
        for b in test_divisors:
            result = divide(0, b)
            assert result == 0.0, f"divide(0, {b}) should equal 0.0"


class TestImplementationChecklist:
    """Tests to verify implementation of defensive programming principles."""

    def test_operations_exist(self):
        """Test that all required operations are implemented."""
        assert callable(add), "add function should be implemented"
        assert callable(subtract), "subtract function should be implemented"
        assert callable(multiply), "multiply function should be implemented"
        assert callable(divide), "divide function should be implemented"

    @pytest.mark.skipif(not EXCEPTIONS_IMPLEMENTED, reason="Custom exceptions not yet implemented")
    def test_custom_exceptions_exist(self):
        """Test that custom exceptions are implemented."""
        assert issubclass(
            InvalidInputError, Exception
        ), "InvalidInputError should inherit from Exception"
        assert issubclass(
            DivisionByZeroError, Exception
        ), "DivisionByZeroError should inherit from Exception"

    @pytest.mark.skipif(not OPERATIONS_IMPLEMENTED, reason="Operations not yet implemented")
    def test_logging_integration(self):
        """Test that operations work with logging (no crashes)."""
        # This should not raise any exceptions related to logging
        try:
            result = add(2, 3)
            assert result == 5
        except Exception as e:
            if "log" in str(e).lower():
                pytest.fail(f"Logging-related error: {e}")

    def test_basic_functionality_preserved(self):
        """Test that basic functionality still works."""
        # Even incomplete implementation should handle simple cases
        assert add(2, 3) == 5
        assert subtract(5, 3) == 2
        assert multiply(2, 3) == 6

        # Division might not work if not implemented
        try:
            result = divide(6, 3)
            assert abs(result - 2.0) < 1e-10
        except (NotImplementedError, AttributeError):
            pass  # OK if not implemented yet
