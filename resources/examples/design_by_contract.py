"""Example: Design by Contract with preconditions, postconditions, and invariants."""

import math
from typing import Union

Number = Union[int, float]


class BankAccount:
    """Example class demonstrating Design by Contract principles."""
    
    def __init__(self, initial_balance: Number = 0):
        # Precondition
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a number")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self._balance = float(initial_balance)
        
        # Postcondition
        assert self._balance >= 0, "Account balance invariant violated"
    
    @property
    def balance(self) -> float:
        """Get current balance."""
        # Invariant check
        assert self._balance >= 0, "Account balance invariant violated"
        return self._balance
    
    def deposit(self, amount: Number) -> None:
        """Deposit money into account."""
        # Preconditions
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        if math.isnan(amount) or math.isinf(amount):
            raise ValueError("Deposit amount must be a valid number")
        
        # Store old balance for postcondition check
        old_balance = self._balance
        
        # Operation
        self._balance += amount
        
        # Postconditions
        assert self._balance == old_balance + amount, "Deposit calculation error"
        assert self._balance >= 0, "Account balance invariant violated"
    
    def withdraw(self, amount: Number) -> None:
        """Withdraw money from account."""
        # Preconditions
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be a number")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if math.isnan(amount) or math.isinf(amount):
            raise ValueError("Withdrawal amount must be a valid number")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        
        # Store old balance for postcondition check
        old_balance = self._balance
        
        # Operation
        self._balance -= amount
        
        # Postconditions
        assert self._balance == old_balance - amount, "Withdrawal calculation error"
        assert self._balance >= 0, "Account balance invariant violated"


def calculate_compound_interest(principal: Number, rate: Number, time: Number, compounds_per_year: int = 1) -> float:
    """
    Calculate compound interest with Design by Contract.
    
    Preconditions:
    - All inputs must be valid numbers
    - Principal must be positive
    - Rate must be non-negative (0% or higher)
    - Time must be non-negative
    - Compounds per year must be positive integer
    
    Postconditions:
    - Result is always >= principal (assuming rate >= 0)
    - Result is a valid number (not NaN or infinite)
    """
    # Preconditions
    if not isinstance(principal, (int, float)):
        raise TypeError("Principal must be a number")
    if not isinstance(rate, (int, float)):
        raise TypeError("Rate must be a number")
    if not isinstance(time, (int, float)):
        raise TypeError("Time must be a number")
    if not isinstance(compounds_per_year, int):
        raise TypeError("Compounds per year must be an integer")
    
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if time < 0:
        raise ValueError("Time cannot be negative")
    if compounds_per_year <= 0:
        raise ValueError("Compounds per year must be positive")
    
    # Check for special values
    for value, name in [(principal, "principal"), (rate, "rate"), (time, "time")]:
        if math.isnan(value) or math.isinf(value):
            raise ValueError(f"{name} must be a valid number")
    
    # Operation: A = P(1 + r/n)^(nt)
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    
    # Postconditions
    if rate >= 0 and time >= 0:
        assert amount >= principal, "Compound interest result should be >= principal"
    assert not math.isnan(amount), "Result should not be NaN"
    assert not math.isinf(amount), "Result should not be infinite"
    assert amount > 0, "Result should be positive"
    
    return amount


if __name__ == "__main__":
    print("=== Design by Contract Examples ===\n")
    
    # Bank account example
    print("1. Bank Account Operations:")
    account = BankAccount(100)
    print(f"Initial balance: ${account.balance}")
    
    account.deposit(50)
    print(f"After $50 deposit: ${account.balance}")
    
    account.withdraw(30)
    print(f"After $30 withdrawal: ${account.balance}")
    
    # Test contract violations
    try:
        account.withdraw(200)  # Insufficient funds
    except ValueError as e:
        print(f"Contract violation caught: {e}")
    
    print("\n2. Compound Interest Calculations:")
    test_cases = [
        (1000, 0.05, 10, 1),      # Valid case
        (1000, 0.05, 10, 12),     # Monthly compounding
        (-1000, 0.05, 10, 1),     # Invalid principal
        (1000, -0.05, 10, 1),     # Invalid rate
    ]
    
    for principal, rate, time, compounds in test_cases:
        try:
            result = calculate_compound_interest(principal, rate, time, compounds)
            print(f"P=${principal}, r={rate*100}%, t={time}yr, n={compounds} → ${result:.2f}")
        except (TypeError, ValueError) as e:
            print(f"P=${principal}, r={rate*100}%, t={time}yr, n={compounds} → Error: {e}")