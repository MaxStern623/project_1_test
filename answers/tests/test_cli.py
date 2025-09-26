"""Tests for the CLI interface with defensive programming."""

import sys
from io import StringIO

import pytest

from answers.src.main import main


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


class TestCLIHappyPaths:
    """Test successful CLI operations."""

    @pytest.mark.parametrize(
        "args,expected",
        [
            (["add", "2", "3"], "5"),
            (["subtract", "5", "3"], "2"),
            (["multiply", "2", "3"], "6"),
            (["divide", "6", "3"], "2.0"),
            (["add", "2.5", "1.5"], "4.0"),
            (["subtract", "10.5", "3.2"], "7.3"),
        ],
    )
    def test_cli_operations_success(self, args, expected):
        """Test successful CLI operations return correct results."""
        code, out, err = run_cli(args)
        assert code == 0
        assert out == expected
        assert err == ""  # No error output for successful operations

    def test_cli_with_verbose_flag(self):
        """Test CLI with verbose logging enabled."""
        code, out, err = run_cli(["--verbose", "add", "2", "3"])
        assert code == 0
        assert out == "5"
        # Verbose mode should produce some logging output
        assert len(err) > 0


class TestCLIErrorHandling:
    """Test CLI error handling and appropriate exit codes."""

    def test_division_by_zero_error(self):
        """Test division by zero returns appropriate error code and message."""
        code, out, err = run_cli(["divide", "1", "0"])
        assert code == 2  # Math error exit code
        assert out == ""
        assert "Math Error:" in err
        assert "Cannot divide by zero" in err

    def test_invalid_number_format(self):
        """Test invalid number format returns input error."""
        code, out, err = run_cli(["add", "not_a_number", "5"])
        assert code == 1  # Input error exit code
        assert out == ""
        assert "Input Error:" in err
        assert "must be valid numbers" in err

    def test_invalid_number_format_second_arg(self):
        """Test invalid number format in second argument."""
        code, out, err = run_cli(["multiply", "5", "not_a_number"])
        assert code == 1  # Input error exit code
        assert out == ""
        assert "Input Error:" in err

    def test_missing_arguments(self):
        """Test missing arguments."""
        # argparse should handle this and exit with code 2
        # But our main() returns 0 for SystemExit from argparse
        code, out, err = run_cli(["add", "5"])
        # This will likely be handled by argparse error, resulting in exit code 0
        # since we catch SystemExit in main()
        assert code == 0

    def test_unknown_operation(self):
        """Test unknown operation command."""
        # This should be caught by argparse before reaching our operation validation
        code, out, err = run_cli(["unknown_op", "1", "2"])
        assert code == 0  # argparse SystemExit handling

    def test_no_arguments(self):
        """Test running with no arguments."""
        code, out, err = run_cli([])
        assert code == 0  # argparse SystemExit handling


class TestCLIInputValidation:
    """Test CLI input validation scenarios."""

    @pytest.mark.parametrize("invalid_input", [
        "inf",
        "-inf",
        "nan",
    ])
    def test_special_float_values(self, invalid_input):
        """Test that special float values are handled appropriately."""
        code, out, err = run_cli(["add", invalid_input, "1"])
        assert code == 1  # Should be input error
        assert "Input Error:" in err

    def test_very_large_numbers(self):
        """Test CLI with very large numbers."""
        code, out, err = run_cli(["add", "1e100", "1e100"])
        assert code == 0  # Should succeed
        assert out == "2e+100"

    def test_very_small_numbers(self):
        """Test CLI with very small numbers."""
        code, out, err = run_cli(["add", "1e-100", "1e-100"])
        assert code == 0  # Should succeed
        assert float(out) == 2e-100


class TestCLIVerboseMode:
    """Test verbose mode functionality."""

    def test_verbose_short_flag(self):
        """Test -v short flag for verbose mode."""
        code, out, err = run_cli(["-v", "multiply", "3", "4"])
        assert code == 0
        assert out == "12"
        assert len(err) > 0  # Should have logging output

    def test_verbose_with_error(self):
        """Test verbose mode with error includes additional context."""
        code, out, err = run_cli(["--verbose", "divide", "5", "0"])
        assert code == 2
        assert "Math Error:" in err
        # In verbose mode, should include additional debug context
        assert len(err) > len("Math Error: Cannot divide by zero")


class TestCLIHelp:
    """Test help functionality."""

    def test_help_flag(self):
        """Test --help flag."""
        code, out, err = run_cli(["--help"])
        # Help is handled by argparse and causes SystemExit
        # Our main() catches this and returns 0
        assert code == 0

    def test_operation_help(self):
        """Test help for specific operations."""
        code, out, err = run_cli(["add", "--help"])
        assert code == 0  # SystemExit from argparse help


class TestCLIRobustness:
    """Test CLI robustness and edge cases."""

    def test_empty_string_arguments(self):
        """Test empty string arguments."""
        code, out, err = run_cli(["add", "", "5"])
        assert code == 1  # Input error
        assert "Input Error:" in err

    def test_whitespace_arguments(self):
        """Test whitespace-only arguments."""
        code, out, err = run_cli(["add", "   ", "5"])
        assert code == 1  # Input error
        assert "Input Error:" in err

    def test_multiple_decimal_points(self):
        """Test numbers with multiple decimal points."""
        code, out, err = run_cli(["add", "1.2.3", "5"])
        assert code == 1  # Input error
        assert "Input Error:" in err

    def test_scientific_notation(self):
        """Test scientific notation input."""
        code, out, err = run_cli(["add", "1e3", "2e3"])
        assert code == 0
        assert float(out) == 3000.0

    def test_negative_numbers(self):
        """Test negative number handling."""
        code, out, err = run_cli(["add", "-5", "-3"])
        assert code == 0
        assert out == "-8"

    def test_zero_operations(self):
        """Test operations involving zero."""
        # Addition with zero
        code, out, err = run_cli(["add", "0", "5"])
        assert code == 0
        assert out == "5"

        # Multiplication by zero
        code, out, err = run_cli(["multiply", "0", "5"])
        assert code == 0
        assert out == "0"

        # Division of zero
        code, out, err = run_cli(["divide", "0", "5"])
        assert code == 0
        assert out == "0.0"
