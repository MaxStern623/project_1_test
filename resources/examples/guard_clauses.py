"""Example: Guard clauses for early validation and cleaner code."""

def calculate_area_bad(length, width):
    """Bad example: nested validation creates complex code."""
    if isinstance(length, (int, float)):
        if isinstance(width, (int, float)):
            if length > 0:
                if width > 0:
                    return length * width
                else:
                    raise ValueError("Width must be positive")
            else:
                raise ValueError("Length must be positive")
        else:
            raise TypeError("Width must be a number")
    else:
        raise TypeError("Length must be a number")


def calculate_area_good(length, width):
    """Good example: guard clauses for early validation."""
    # Guard clauses - validate early and return/raise early
    if not isinstance(length, (int, float)):
        raise TypeError("Length must be a number")
    
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a number")
    
    if length <= 0:
        raise ValueError("Length must be positive")
    
    if width <= 0:
        raise ValueError("Width must be positive")
    
    # Main business logic - clean and focused
    return length * width


# Example usage
if __name__ == "__main__":
    try:
        area = calculate_area_good(5, 3)
        print(f"Area: {area}")
        
        # This will raise an error
        calculate_area_good(-1, 3)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")