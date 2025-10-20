"""Example: EAFP (Easier to Ask for Forgiveness than Permission) vs LBYL (Look Before You Leap)."""

import math
import os


def read_file_lbyl(filename):
    """LBYL approach - check conditions before acting."""
    if not isinstance(filename, str):
        raise TypeError("Filename must be a string")

    if not filename.strip():
        raise ValueError("Filename cannot be empty")

    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' does not exist")

    if not os.access(filename, os.R_OK):
        raise PermissionError(f"Cannot read file '{filename}'")

    # Now we can safely read
    with open(filename, "r") as f:
        return f.read()


def read_file_eafp(filename):
    """EAFP approach - try the operation and handle exceptions."""
    if not isinstance(filename, str):
        raise TypeError("Filename must be a string")

    if not filename.strip():
        raise ValueError("Filename cannot be empty")

    # Just try it - let Python tell us what's wrong
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' does not exist")
    except PermissionError:
        raise PermissionError(f"Cannot read file '{filename}'")
    except Exception as e:
        raise RuntimeError(f"Unexpected error reading '{filename}': {e}")


def safe_sqrt_lbyl(value):
    """LBYL for mathematical validation."""
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")

    if math.isnan(value):
        raise ValueError("Value cannot be NaN")

    if math.isinf(value):
        raise ValueError("Value cannot be infinite")

    if value < 0:
        raise ValueError("Cannot take square root of negative number")

    return math.sqrt(value)


def safe_sqrt_eafp(value):
    """EAFP for mathematical operations."""
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")

    try:
        result = math.sqrt(value)
        if math.isnan(result) or math.isinf(result):
            raise ValueError("Invalid mathematical result")
        return result
    except ValueError as e:
        # Re-raise with more context
        raise ValueError(f"Cannot calculate square root of {value}: {e}")


if __name__ == "__main__":
    # Test mathematical operations
    test_values = [4, -1, float("nan"), float("inf"), "not_a_number"]

    for value in test_values:
        try:
            result = safe_sqrt_lbyl(value)
            print(f"LBYL sqrt({value}) = {result}")
        except Exception as e:
            print(f"LBYL sqrt({value}) failed: {e}")

    print()

    for value in test_values:
        try:
            result = safe_sqrt_eafp(value)
            print(f"EAFP sqrt({value}) = {result}")
        except Exception as e:
            print(f"EAFP sqrt({value}) failed: {e}")
