"""Example: Logging at error boundaries for better debugging."""

import logging
from typing import Any


# Configure logging for the example
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def process_data_with_logging(data: Any) -> dict:
    """Demonstrate proper logging at error boundaries."""
    logger.info(f"Starting data processing for: {type(data).__name__}")
    
    try:
        # Input validation with debug logging
        if not isinstance(data, (list, tuple)):
            logger.error(f"Invalid data type: expected list/tuple, got {type(data).__name__}")
            raise TypeError("Data must be a list or tuple")
        
        if len(data) == 0:
            logger.warning("Empty data provided")
            return {"count": 0, "sum": 0, "average": 0}
        
        logger.debug(f"Processing {len(data)} items")
        
        # Process with error boundary logging
        numbers = []
        for i, item in enumerate(data):
            try:
                num = float(item)
                if not isinstance(item, (int, float)):
                    logger.debug(f"Converted item {i} from {type(item).__name__} to float")
                numbers.append(num)
            except (ValueError, TypeError) as e:
                logger.error(f"Cannot convert item {i} ('{item}') to number: {e}")
                raise ValueError(f"All items must be convertible to numbers. Item {i}: '{item}'")
        
        # Calculate results
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        
        result = {"count": count, "sum": total, "average": average}
        logger.info(f"Processing completed successfully: {result}")
        return result
        
    except Exception as e:
        # Log the error at the boundary before re-raising
        logger.error(f"Data processing failed: {e}", exc_info=True)
        raise


def divide_with_context_logging(a: float, b: float) -> float:
    """Demonstrate logging with context but no sensitive data."""
    logger.debug("Division operation requested")
    
    try:
        if b == 0:
            logger.error("Division by zero attempted")
            raise ZeroDivisionError("Cannot divide by zero")
        
        result = a / b
        logger.info("Division completed successfully")
        logger.debug(f"Operation result magnitude: {abs(result):.2e}")  # Log magnitude, not actual values
        
        return result
        
    except ZeroDivisionError:
        logger.error("Division operation failed due to zero divisor")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in division: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    print("=== Logging Examples ===\n")
    
    # Test successful processing
    print("1. Successful data processing:")
    try:
        result = process_data_with_logging([1, 2, 3, 4, 5])
        print(f"Result: {result}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    
    # Test error cases
    print("2. Error case - invalid data:")
    try:
        result = process_data_with_logging([1, 2, "invalid", 4])
        print(f"Result: {result}\n")
    except Exception as e:
        print(f"Error: {e}\n")
    
    print("3. Division operations:")
    try:
        result = divide_with_context_logging(10, 2)
        print(f"10 / 2 = {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        result = divide_with_context_logging(10, 0)
        print(f"10 / 0 = {result}")
    except Exception as e:
        print(f"Error: {e}")