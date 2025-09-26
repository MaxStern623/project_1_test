#!/usr/bin/env python3
"""
Demonstration script showing the differences between the answers and practice versions.

This script shows how defensive programming principles are implemented in the answers
version and what needs to be implemented in the practice version.
"""


def test_answers_version():
    """Test the complete answers version."""
    print("=" * 60)
    print("TESTING ANSWERS VERSION (Complete Implementation)")
    print("=" * 60)

    try:
        from answers.src.exceptions import DivisionByZeroError, InvalidInputError
        from answers.src.operations import add, divide, multiply

        # Test successful operations
        print("\n1. Successful Operations:")
        print(f"   add(2, 3) = {add(2, 3)} (type: {type(add(2, 3)).__name__})")
        print(f"   multiply(0, 5) = {multiply(0, 5)} (contract: multiply by zero)")
        print(f"   divide(6, 3) = {divide(6, 3)} (always returns float)")

        # Test defensive programming features
        print("\n2. Defensive Programming Features:")

        # Custom exception for division by zero
        try:
            divide(5, 0)
        except DivisionByZeroError as e:
            print(f"   ✓ Custom DivisionByZeroError: {e}")
            print(f"   ✓ Error context available: {hasattr(e, 'context')}")

        # Input validation with custom exception
        try:
            add("invalid", 5)
        except InvalidInputError as e:
            print(f"   ✓ Input validation with InvalidInputError: {e}")
            print(f"   ✓ Error context: {e.context if hasattr(e, 'context') else 'Not available'}")

        # NaN rejection
        try:
            multiply(float("nan"), 5)
        except InvalidInputError as e:
            print(f"   ✓ NaN rejection: {e}")

        print("\n   ✓ Comprehensive logging (visible in CLI verbose mode)")
        print("   ✓ Type preservation (int operations return int when possible)")
        print("   ✓ Contract assertions (multiply by 0/1, divide by 1)")
        print("   ✓ Overflow detection")

    except ImportError as e:
        print(f"Could not import answers version: {e}")


def test_practice_version():
    """Test the incomplete practice version."""
    print("\n" + "=" * 60)
    print("TESTING PRACTICE VERSION (Incomplete - Needs Implementation)")
    print("=" * 60)

    try:
        from practice.src.operations import add, divide, multiply

        # Test basic functionality (should work)
        print("\n1. Basic Operations (Currently Working):")
        print(f"   add(2, 3) = {add(2, 3)}")
        print(f"   multiply(2, 3) = {multiply(2, 3)}")

        # Test what needs to be implemented
        print("\n2. Missing Defensive Programming Features:")

        # No custom exceptions - uses built-in ZeroDivisionError
        try:
            divide(5, 0)
        except ZeroDivisionError as e:
            print(f"   ✗ Uses built-in ZeroDivisionError: {e}")
            print("   → Should use custom DivisionByZeroError with context")
        except Exception as e:
            print(f"   ? Unexpected exception type: {type(e).__name__}: {e}")

        # No input validation
        try:
            result = add("invalid", 5)
            print(f"   ✗ No input validation - accepted invalid input: {result}")
        except TypeError as e:
            print(f"   ✗ Uses built-in TypeError for invalid input: {e}")
            print("   → Should use custom InvalidInputError with context")
        except Exception as e:
            print(f"   ? Unexpected exception for invalid input: {type(e).__name__}: {e}")

        # No NaN/infinity checking
        try:
            result = multiply(float("nan"), 5)
            print(f"   ✗ No NaN validation - result: {result}")
            print("   → Should reject NaN inputs with InvalidInputError")
        except Exception as e:
            print(f"   ? NaN handling: {type(e).__name__}: {e}")

        print("\n   TODO: Implement input validation (_validate_input function)")
        print("   TODO: Implement custom exceptions with context")
        print("   TODO: Add logging at error boundaries")
        print("   TODO: Add contract assertions")
        print("   TODO: Add overflow/underflow checking")

    except ImportError as e:
        print(f"Could not import practice version: {e}")


def demo_cli_differences():
    """Demonstrate CLI differences between versions."""
    print("\n" + "=" * 60)
    print("CLI COMPARISON")
    print("=" * 60)

    print("\nAnswers Version CLI Features:")
    print("  ✓ Structured error messages with appropriate exit codes")
    print("  ✓ Verbose logging mode (--verbose/-v flag)")
    print("  ✓ Input validation with clear error messages")
    print("  ✓ Different exit codes for different error types:")
    print("    - 0: Success")
    print("    - 1: Input errors")
    print("    - 2: Math errors (division by zero)")
    print("    - 3: Other calculator errors")
    print("    - 4: Unexpected errors")

    print("\nPractice Version CLI (Incomplete):")
    print("  ✗ Returns placeholder exit code 0")
    print("  ✗ No structured error handling")
    print("  ✗ Missing verbose mode implementation")
    print("  ✗ No input validation")

    print("\nTry these commands to see the differences:")
    print("  # Answers version:")
    print("  python3 -m answers.src.main add 2 3")
    print("  python3 -m answers.src.main --verbose divide 6 3")
    print("  python3 -m answers.src.main divide 5 0  # Exit code 2")
    print("  python3 -m answers.src.main add invalid 5  # Exit code 1")
    print("\n  # Practice version:")
    print("  python3 -m practice.src.main add 2 3  # Returns 0 (placeholder)")


if __name__ == "__main__":
    test_answers_version()
    test_practice_version()
    demo_cli_differences()

    print("\n" + "=" * 60)
    print("LEARNING PATH")
    print("=" * 60)
    print("1. Implement custom exceptions in practice/src/exceptions.py")
    print("2. Add defensive programming to practice/src/operations/__init__.py")
    print("3. Enhance CLI in practice/src/main.py")
    print("4. Run tests: pytest practice/tests/ -v")
    print("5. Compare with answers version for reference")
    print("\nSee DEFENSIVE_PROGRAMMING_README.md for detailed instructions!")
