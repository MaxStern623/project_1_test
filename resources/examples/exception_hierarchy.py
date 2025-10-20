"""Example: Exception hierarchy with context for better error handling."""


class CalculationError(Exception):
    """Base exception for calculation errors."""

    def __init__(self, message, context=None):
        super().__init__(message)
        self.context = context or {}


class InvalidInputError(CalculationError):
    """Raised when input is invalid."""

    pass


class MathError(CalculationError):
    """Raised when mathematical operation fails."""

    pass


def safe_divide(a, b):
    """Demonstrate exception hierarchy and context."""
    # Input validation
    if not isinstance(a, (int, float)):
        raise InvalidInputError(
            f"First argument must be a number, got {type(a).__name__}",
            {"value": a, "expected_type": "number"},
        )

    if not isinstance(b, (int, float)):
        raise InvalidInputError(
            f"Second argument must be a number, got {type(b).__name__}",
            {"value": b, "expected_type": "number"},
        )

    # Mathematical validation
    if b == 0:
        raise MathError("Cannot divide by zero", {"dividend": a, "divisor": b})

    return a / b


# Example usage
if __name__ == "__main__":
    test_cases = [
        (10, 2),  # Valid
        (5, 0),  # Division by zero
        ("10", 2),  # Invalid type
    ]

    for a, b in test_cases:
        try:
            result = safe_divide(a, b)
            print(f"{a} / {b} = {result}")
        except CalculationError as e:
            print(f"Error: {e}")
            if hasattr(e, "context"):
                print(f"Context: {e.context}")
        print()  # Empty line for readability
