# 🖥️ CLI with Error Handling - Professional Command-Line Interface

> **Learning Goal**: Build a robust command-line interface with proper argument parsing, error handling, exit codes, and user-friendly error messages.

## 🎯 What You'll Learn

- **Argument Parsing** - Using argparse for professional CLI design
- **Exit Code Standards** - Proper Unix exit codes for different error types
- **Error Message Design** - User-friendly vs developer-friendly messages
- **Logging Integration** - Conditional logging for debugging vs production

## 📋 Your Task

Complete the CLI implementation in [`src/main.py`](../../src/main.py). The file has TODOs guiding you through:
- Argument parsing and validation
- Operation execution with error handling
- Proper exit codes for different error types
- Logging setup for debugging

## 🔍 CLI Architecture

### Professional CLI Structure
```
CLI Request → Argument Parsing → Input Validation → Operation → Output
     ↓              ↓                 ↓             ↓         ↓
Error Handling → Exit Codes → User Messages → Logging → Clean Exit
```

### Exit Code Standards
```python
# Standard Unix exit codes
0 - Success
1 - General input/usage errors
2 - Misuse of shell command (argparse errors)
3 - Calculator-specific errors (custom)
4 - Unexpected/internal errors
```

## 💡 Key Patterns

### Argument Parsing Setup
```python
def build_parser() -> argparse.ArgumentParser:
    """Build CLI parser with subcommands."""
    parser = argparse.ArgumentParser(
        prog="calc",
        description="Defensive calculator with error handling"
    )

    # Global options
    parser.add_argument("--verbose", "-v", action="store_true")

    # Subcommands for operations
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # Each operation gets its own subcommand
    add_parser = subparsers.add_parser("add", help="Add two numbers")
    add_parser.add_argument("a", help="First number")
    add_parser.add_argument("b", help="Second number")

    # ... repeat for subtract, multiply, divide
    return parser
```

### Error Handling with Exit Codes
```python
def main(argv: list[str] | None = None) -> int:
    """Main entry with proper error handling."""
    try:
        args = parser.parse_args(argv)

        # Validate and convert arguments
        try:
            a, b = validate_operation_args(args.a, args.b)
        except InvalidInputError as e:
            print(f"Input Error: {e}", file=sys.stderr)
            return 1  # Input error exit code

        # Execute operation
        try:
            result = execute_operation(args.cmd, a, b)
            print(result)
            return 0  # Success

        except DivisionByZeroError as e:
            print(f"Math Error: {e}", file=sys.stderr)
            return 2  # Math error exit code

        except CalculatorError as e:
            print(f"Calculator Error: {e}", file=sys.stderr)
            return 3  # Calculator error exit code

    except SystemExit as e:
        # argparse calls sys.exit() for --help or invalid syntax
        return e.code if e.code is not None else 0

    except Exception as e:
        print(f"Internal Error: {e}", file=sys.stderr)
        return 4  # Unexpected error exit code
```

### Input Validation for CLI
```python
def validate_operation_args(a: str, b: str) -> tuple[float, float]:
    """Convert and validate string arguments."""
    try:
        val_a = float(a)
        val_b = float(b)
    except ValueError as e:
        raise InvalidInputError(
            f"Arguments must be valid numbers: '{a}', '{b}'",
            {"raw_args": [a, b], "error": str(e)}
        )

    # Additional validation for special values
    import math
    if math.isnan(val_a) or math.isinf(val_a):
        raise InvalidInputError(f"Argument 'a' cannot be {a}")
    if math.isnan(val_b) or math.isinf(val_b):
        raise InvalidInputError(f"Argument 'b' cannot be {b}")

    return val_a, val_b
```

## 🛠️ Implementation Steps

### Step 1: Logging Setup (10 minutes)
```python
def setup_logging(verbose: bool = False) -> None:
    """Configure logging based on verbosity."""
    if verbose:
        level = logging.DEBUG
        format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=level, format=format_str, handlers=[logging.StreamHandler(sys.stderr)])
    else:
        # Disable logging in normal mode to avoid test interference
        logging.basicConfig(level=logging.CRITICAL + 1, handlers=[])
```

### Step 2: Argument Parser (15 minutes)
Build the `build_parser()` function with subcommands for each operation.

### Step 3: Input Validation (10 minutes)
Implement `validate_operation_args()` to convert strings to numbers safely.

### Step 4: Operation Executor (10 minutes)
```python
def execute_operation(operation_name: str, a: float, b: float) -> float:
    """Execute operation with error handling."""
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    if operation_name not in operations:
        raise InvalidInputError(f"Unknown operation: {operation_name}")

    return operations[operation_name](a, b)
```

### Step 5: Main Function (20 minutes)
Complete the main function with all error handling and exit codes.

## 🧪 Testing Your CLI

### Basic Functionality
```bash
# Success cases (exit code 0)
python3 -m src.main add 2 3           # Should print: 5
python3 -m src.main divide 6 3        # Should print: 2.0
python3 -m src.main --verbose add 2 3 # Should show debug info

# Input errors (exit code 1)
python3 -m src.main add invalid 5     # Should show input error
echo $?                               # Should print: 1

# Math errors (exit code 2)
python3 -m src.main divide 1 0        # Should show math error
echo $?                               # Should print: 2

# Help (exit code 0)
python3 -m src.main --help            # Should show help
python3 -m src.main add --help        # Should show add help
```

### Error Message Quality
```bash
# Good error messages are:
# - Clear about what went wrong
# - Don't expose internal details
# - Suggest what the user should do

# Example good messages:
Input Error: Arguments must be valid numbers: 'abc', '5'
Math Error: Cannot divide by zero
Calculator Error: Result overflow in multiplication
```

## 🔍 Advanced Features

### Verbose Mode Implementation
```python
# In main(), after setup_logging():
logger.debug(f"Parsed arguments: {args}")
logger.debug(f"Executing {args.cmd} with operands: {a}, {b}")

# In operations, add debug logging:
logger.debug(f"Adding {a} + {b}")
logger.debug(f"Result: {result}")
```

### Output Formatting
```python
# Handle different number types appropriately
if isinstance(result, float) and result.is_integer():
    print(int(result))  # Print "5" instead of "5.0" when appropriate
else:
    print(result)
```

## 🔗 External Resources

- **[argparse Tutorial](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)** - Official Python tutorial
- **[Exit Status Codes](https://tldp.org/LDP/abs/html/exitcodes.html)** - Unix/Linux standards
- **[CLI Design Principles](https://clig.dev/)** - Modern CLI design guide
- **[Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)** - Logging best practices

## ✅ Success Criteria

- [ ] CLI accepts all four operations with proper arguments
- [ ] `--verbose` flag enables debug logging
- [ ] Proper exit codes for different error types (0, 1, 2, 3, 4)
- [ ] User-friendly error messages to stderr
- [ ] Help system works (`--help` for main and subcommands)
- [ ] All CLI tests pass
- [ ] Numbers are formatted appropriately in output

## 🎯 Testing Commands

```bash
# Run CLI tests specifically
pytest tests/test_cli.py -v

# Test exit codes manually
python3 -m src.main add 2 3; echo "Exit code: $?"
python3 -m src.main divide 1 0; echo "Exit code: $?"
python3 -m src.main add invalid 5; echo "Exit code: $?"

# Test verbose mode
python3 -m src.main --verbose add 2 3 2>&1 | grep DEBUG
```

## 🏆 Completion

Once your CLI is working, you've built a professional-grade command-line tool! You should be able to:

- ✅ Perform calculations: `calc add 2 3`
- ✅ Handle errors gracefully with clear messages
- ✅ Return proper exit codes for automation
- ✅ Debug with `--verbose` flag
- ✅ Get help with `--help`

## 🚀 Next Steps

Your defensive programming calculator is now complete! Consider exploring:

- **[Testing Strategies](../../../docs/05-testing.md)** - Learn about comprehensive testing
- **[Code Quality Tools](../../../docs/04-tooling.md)** - Formatting, linting, and type checking
- **[Advanced Exercises](../advanced/)** - More challenging defensive programming scenarios

---

💡 **Pro Tip:** Test your CLI like a user would - try to break it with weird inputs and see how gracefully it fails!
