"""Example: Input validation patterns for defensive programming."""

import math
from typing import Any, Union

Number = Union[int, float]


def validate_number(value: Any, param_name: str) -> Number:
    """Comprehensive number validation with clear error messages."""
    # Type validation
    if not isinstance(value, (int, float)):
        raise TypeError(f"Parameter '{param_name}' must be a number, got {type(value).__name__}")

    # Special value validation
    if math.isnan(value):
        raise ValueError(f"Parameter '{param_name}' cannot be NaN")

    if math.isinf(value):
        raise ValueError(f"Parameter '{param_name}' cannot be infinite")

    return value


def validate_positive_number(value: Any, param_name: str) -> Number:
    """Validate that a value is a positive number."""
    validated = validate_number(value, param_name)

    if validated <= 0:
        raise ValueError(f"Parameter '{param_name}' must be positive, got {validated}")

    return validated


def validate_range(value: Any, param_name: str, min_val: Number, max_val: Number) -> Number:
    """Validate that a number is within a specific range."""
    validated = validate_number(value, param_name)

    if validated < min_val or validated > max_val:
        raise ValueError(
            f"Parameter '{param_name}' must be between {min_val} and {max_val}, " f"got {validated}"
        )

    return validated


def calculate_circle_area(radius: Any) -> float:
    """Calculate circle area with comprehensive input validation."""
    # Validate radius is a positive number
    r = validate_positive_number(radius, "radius")

    # Additional domain-specific validation
    if r > 1000000:  # Arbitrary large value check
        raise ValueError("Radius is unreasonably large")

    return math.pi * r * r


def calculate_percentage(part: Any, total: Any) -> float:
    """Calculate percentage with validation."""
    validated_part = validate_number(part, "part")
    validated_total = validate_positive_number(total, "total")

    if validated_part < 0:
        raise ValueError("Part cannot be negative")

    if validated_part > validated_total:
        raise ValueError("Part cannot be greater than total")

    return (validated_part / validated_total) * 100


if __name__ == "__main__":
    # Test cases
    test_cases = [
        # (function, args, description)
        (calculate_circle_area, (5,), "Valid radius"),
        (calculate_circle_area, (-1,), "Negative radius"),
        (calculate_circle_area, (float("inf"),), "Infinite radius"),
        (calculate_circle_area, ("5",), "String radius"),
        (calculate_percentage, (25, 100), "Valid percentage"),
        (calculate_percentage, (150, 100), "Part > total"),
        (calculate_percentage, (25, 0), "Zero total"),
    ]

    for func, args, description in test_cases:
        try:
            result = func(*args)
            print(f"✓ {description}: {func.__name__}{args} = {result}")
        except (TypeError, ValueError) as e:
            print(f"✗ {description}: {func.__name__}{args} → {e}")
        print()
