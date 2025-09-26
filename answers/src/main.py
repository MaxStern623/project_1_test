"""Enhanced CLI entry point with defensive programming practices.

Usage examples:
  python -m src.main add 2 3
  python -m src.main divide 6 3
  python -m src.main --verbose multiply 4 5
"""

from __future__ import annotations

import argparse
import logging
import sys
from typing import Callable

from .exceptions import CalculatorError, DivisionByZeroError, InvalidInputError
from .operations import add, divide, multiply, subtract

# Configure logging
logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    """Configure logging with appropriate level and format.

    Args:
        verbose: If True, set DEBUG level; otherwise INFO level
    """
    level = logging.DEBUG if verbose else logging.INFO
    format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logging.basicConfig(
        level=level,
        format=format_str,
        handlers=[logging.StreamHandler(sys.stderr)],
    )


def validate_operation_args(a: str, b: str) -> tuple[float, float]:
    """Validate and convert string arguments to floats.

    Args:
        a: First operand as string
        b: Second operand as string

    Returns:
        Tuple of validated float values

    Raises:
        InvalidInputError: If arguments cannot be converted to valid numbers
    """
    try:
        val_a = float(a)
        val_b = float(b)
    except ValueError as e:
        logger.error(f"Invalid number format: {e}")
        raise InvalidInputError(
            f"Arguments must be valid numbers: '{a}', '{b}'",
            {"raw_args": [a, b], "error": str(e)},
        ) from e

    # Check for special values that operations module will validate
    import math
    if math.isnan(val_a) or math.isinf(val_a):
        logger.error(f"Invalid special value for 'a': {val_a}")
        raise InvalidInputError(
            f"Argument 'a' cannot be {a} (NaN or infinite)",
            {"raw_args": [a, b], "parsed_a": val_a},
        )
    
    if math.isnan(val_b) or math.isinf(val_b):
        logger.error(f"Invalid special value for 'b': {val_b}")
        raise InvalidInputError(
            f"Argument 'b' cannot be {b} (NaN or infinite)",
            {"raw_args": [a, b], "parsed_b": val_b},
        )

    return val_a, val_b


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argument parser with defensive validation."""
    parser = argparse.ArgumentParser(
        prog="calc",
        description="Basic calculator with defensive programming",
        epilog="Use --verbose for detailed logging output",
        allow_abbrev=False,
    )

    # Global options
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging output",
    )

    # Subcommands
    subparsers = parser.add_subparsers(dest="cmd", required=True, help="Available operations")

    def create_operation_parser(name: str, help_text: str) -> argparse.ArgumentParser:
        """Create a parser for an arithmetic operation.

        Args:
            name: Operation name
            help_text: Help description

        Returns:
            Configured parser for the operation
        """
        op_parser = subparsers.add_parser(name, help=help_text, allow_abbrev=False)
        op_parser.add_argument("a", help="First operand (number)")
        op_parser.add_argument("b", help="Second operand (number)")
        return op_parser

    # Define operations with help text
    create_operation_parser("add", "Add two numbers")
    create_operation_parser("subtract", "Subtract second number from first")
    create_operation_parser("multiply", "Multiply two numbers")
    create_operation_parser("divide", "Divide first number by second")

    return parser


def execute_operation(operation_name: str, a: float, b: float) -> float:
    """Execute the specified operation with error handling.

    Args:
        operation_name: Name of the operation to perform
        a: First operand
        b: Second operand

    Returns:
        Result of the operation

    Raises:
        InvalidInputError: If operation name is invalid
        CalculatorError: If operation fails
    """
    # Operation mapping with type hints
    operations: dict[str, Callable[[float, float], float]] = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    # Guard clause for operation existence
    if operation_name not in operations:
        raise InvalidInputError(
            f"Unknown operation: {operation_name}",
            {"operation": operation_name, "available": list(operations.keys())},
        )

    operation_func = operations[operation_name]
    logger.info(f"Executing {operation_name}({a}, {b})")

    try:
        result = operation_func(a, b)
        logger.info(f"Operation successful: {result}")
        return result
    except CalculatorError:
        # Re-raise calculator-specific errors as-is
        raise
    except Exception as e:
        # Wrap unexpected errors
        logger.error(f"Unexpected error in {operation_name}: {e}")
        raise InvalidInputError(
            f"Operation {operation_name} failed unexpectedly",
            {"operation": operation_name, "operands": [a, b], "error": str(e)},
        ) from e


def main(argv: list[str] | None = None) -> int:
    """Main entry point with comprehensive error handling.

    Args:
        argv: Command line arguments (uses sys.argv if None)

    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    parser = build_parser()

    try:
        args = parser.parse_args(argv)

        # Setup logging based on verbosity
        setup_logging(args.verbose)
        logger.debug(f"Parsed arguments: {args}")

        # Validate and convert arguments (guard clauses)
        try:
            operand_a, operand_b = validate_operation_args(args.a, args.b)
        except InvalidInputError as e:
            print(f"Input Error: {e}", file=sys.stderr)
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"Input validation context: {e.context}")
            return 1

        # Execute operation
        try:
            logger.debug(f"Executing {args.cmd} with operands: {operand_a}, {operand_b}")
            result = execute_operation(args.cmd, operand_a, operand_b)
            logger.debug(f"Operation result: {result}")
            
            # Format output to match test expectations
            if isinstance(result, float):
                if result.is_integer() and abs(result) < 1e15:
                    # Show as int only for small whole numbers  
                    print(int(result))
                else:
                    # Show as float for large numbers or decimals
                    print(result)
            else:
                print(result)
            return 0

        except DivisionByZeroError as e:
            error_msg = f"Math Error: {e}"
            if logger.isEnabledFor(logging.DEBUG) and hasattr(e, 'context'):
                error_msg += f" (Context: {e.context})"
            print(error_msg, file=sys.stderr)
            logger.debug(f"Division error context: {getattr(e, 'context', {})}")
            return 2

        except InvalidInputError as e:
            print(f"Input Error: {e}", file=sys.stderr)
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"Input error context: {e.context}")
            return 1

        except CalculatorError as e:
            print(f"Calculator Error: {e}", file=sys.stderr)
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"Calculator error context: {e.context}")
            return 3

    except SystemExit as e:
        # argparse calls sys.exit() on --help or invalid args
        # Exit code 0 for help, non-zero for errors
        return e.code if e.code is not None else 0
    except Exception as e:
        # Catch-all for unexpected errors
        logger.error(f"Unexpected error in main: {e}", exc_info=True)
        print(f"Internal Error: {e}", file=sys.stderr)
        return 4


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
