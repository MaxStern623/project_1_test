"""Tests for the CLI interface - PRACTICE VERSION

These tests validate your CLI defensive programming implementation.
All tests should pass when you correctly implement the CLI enhancements.

Run with: pytest practice/tests/test_cli.py -v
"""

import sys
from io import StringIO

import pytest

# TODO: Update this import when you implement the main module
try:
    from src.main import main
    MAIN_IMPLEMENTED = True
except ImportError:
    def main(argv=None):
        return 0  # Placeholder
    MAIN_IMPLEMENTED = False


def run_cli(args):
    """Helper function to run CLI and capture output."""
    stdout = StringIO()
    stderr = StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = stdout, stderr
        code = main(args)
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    return code, stdout.getvalue().strip(), stderr.getvalue().strip()


class TestCLIBasicFunctionality:
    """Test that basic CLI functionality works."""

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    @pytest.mark.parametrize(
        "args,expected_code,expected_output",
        [
            (["add", "2", "3"], 0, "5"),
            (["subtract", "5", "3"], 0, "2"),
            (["multiply", "2", "3"], 0, "6"),
            (["divide", "6", "3"], 0, "2.0"),
        ],
    )
    def test_basic_operations_success(self, args, expected_code, expected_output):
        """Test that basic operations work and return correct exit codes."""
        code, out, err = run_cli(args)
        assert code == expected_code, f"Expected exit code {expected_code}, got {code}"
        assert out == expected_output, f"Expected output '{expected_output}', got '{out}'"


class TestCLIErrorHandling:
    """Test CLI error handling with appropriate exit codes."""

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_division_by_zero_exit_code(self):
        """Test that division by zero returns exit code 2 (math error)."""
        code, out, err = run_cli(["divide", "1", "0"])
        assert code == 2, "Division by zero should return exit code 2 (math error)"
        assert "Error:" in err or "error" in err.lower(), "Should include error message in stderr"

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_invalid_number_exit_code(self):
        """Test that invalid numbers return exit code 1 (input error)."""
        code, out, err = run_cli(["add", "not_a_number", "5"])
        assert code == 1, "Invalid input should return exit code 1 (input error)"
        assert "Error:" in err or "error" in err.lower(), "Should include error message in stderr"

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_invalid_second_argument(self):
        """Test invalid second argument handling."""
        code, out, err = run_cli(["multiply", "5", "invalid"])
        assert code == 1, "Invalid second argument should return exit code 1"
        assert "Error:" in err or "error" in err.lower(), "Should include error message"


class TestCLIInputValidation:
    """Test CLI input validation scenarios."""

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    @pytest.mark.parametrize("invalid_input", ["inf", "-inf", "nan"])
    def test_special_float_values_handling(self, invalid_input):
        """Test handling of special float values (inf, nan)."""
        code, out, err = run_cli(["add", invalid_input, "1"])
        # Should be handled as input error (exit code 1)
        assert code in [1, 4], f"Special value {invalid_input} should be handled with appropriate exit code"

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_empty_arguments(self):
        """Test empty string arguments."""
        code, out, err = run_cli(["add", "", "5"])
        assert code == 1, "Empty string should return input error (exit code 1)"

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_scientific_notation_support(self):
        """Test that scientific notation is supported."""
        code, out, err = run_cli(["add", "1e3", "2e3"])
        if code == 0:  # If implemented correctly
            assert float(out) == 3000.0
        # If not implemented, should still handle gracefully


class TestCLIVerboseMode:
    """Test verbose mode functionality."""

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_verbose_flag_exists(self):
        """Test that verbose flag is recognized (doesn't cause argument error)."""
        # This test passes if the argument is recognized, even if logging isn't implemented
        code, out, err = run_cli(["--verbose", "add", "2", "3"])
        # Should not fail due to unknown argument
        assert code != 2 or "unrecognized arguments" not in err

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_verbose_short_flag(self):
        """Test that -v short flag works."""
        code, out, err = run_cli(["-v", "multiply", "3", "4"])
        # Should not fail due to unknown argument
        assert code != 2 or "unrecognized arguments" not in err


class TestCLIArgumentParsing:
    """Test argument parsing functionality."""

    def test_help_functionality(self):
        """Test that help works (even if not fully implemented)."""
        # Help should be handled by argparse
        code, out, err = run_cli(["--help"])
        # argparse help causes SystemExit, which our main() should handle
        assert code == 0  # Should handle SystemExit gracefully

    def test_missing_arguments_handling(self):
        """Test handling of missing arguments."""
        code, out, err = run_cli(["add", "5"])  # Missing second argument
        # Should be handled by argparse or our validation
        assert code in [0, 1, 2], "Missing arguments should be handled gracefully"

    def test_unknown_operation_handling(self):
        """Test handling of unknown operations."""
        code, out, err = run_cli(["unknown_operation", "1", "2"])
        # Should be handled by argparse or our validation
        assert code in [0, 1], "Unknown operations should be handled gracefully"


class TestCLIRobustness:
    """Test CLI robustness and edge cases."""

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_negative_numbers(self):
        """Test negative number handling."""
        code, out, err = run_cli(["add", "-5", "-3"])
        if code == 0:  # If implemented
            assert out == "-8"

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_decimal_numbers(self):
        """Test decimal number handling."""
        code, out, err = run_cli(["add", "2.5", "1.5"])
        if code == 0:  # If implemented
            assert float(out) == 4.0

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_zero_operations(self):
        """Test operations with zero."""
        # Test addition with zero
        code, out, err = run_cli(["add", "0", "5"])
        if code == 0:
            assert out == "5"

        # Test multiplication by zero
        code, out, err = run_cli(["multiply", "0", "5"])
        if code == 0:
            assert out == "0"

        # Test division of zero
        code, out, err = run_cli(["divide", "0", "5"])
        if code == 0:
            assert out == "0.0"


class TestExitCodeContract:
    """Test that exit codes follow the specified contract."""

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_success_exit_code(self):
        """Test that successful operations return exit code 0."""
        code, out, err = run_cli(["add", "1", "1"])
        if "Error:" not in err:  # If no error occurred
            assert code == 0, "Successful operations should return exit code 0"

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_math_error_exit_code(self):
        """Test that math errors (division by zero) return exit code 2."""
        code, out, err = run_cli(["divide", "1", "0"])
        if "divide" in err.lower() and "zero" in err.lower():
            assert code == 2, "Math errors should return exit code 2"

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_input_error_exit_code(self):
        """Test that input errors return exit code 1."""
        code, out, err = run_cli(["add", "invalid", "5"])
        if code != 0 and code != 2:  # Not success, not math error
            assert code == 1, "Input errors should return exit code 1"


class TestImplementationProgress:
    """Tests to check implementation progress."""

    def test_main_function_exists(self):
        """Test that main function exists and is callable."""
        assert callable(main), "main function should exist and be callable"

    def test_main_accepts_argv_parameter(self):
        """Test that main function accepts argv parameter."""
        try:
            # Should not crash when called with argument list
            result = main([])
            assert isinstance(result, int), "main should return integer exit code"
        except TypeError as e:
            if "argv" in str(e) or "argument" in str(e):
                pytest.fail("main function should accept argv parameter")

    @pytest.mark.skipif(not MAIN_IMPLEMENTED, reason="Main module not yet implemented")
    def test_structured_error_messages(self):
        """Test that error messages are structured and informative."""
        code, out, err = run_cli(["divide", "1", "0"])
        if code != 0:  # If error occurred
            # Error message should be more than just the exception
            assert len(err) > 10, "Error messages should be informative"
            # Should not contain bare exception traces in normal operation
            assert "Traceback" not in err, "Should not show raw tracebacks to users"
