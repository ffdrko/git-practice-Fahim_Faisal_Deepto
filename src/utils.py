"""Utility module for calculator operations."""


def _validate_numbers(a, b):
    """Ensure both inputs are int or float, otherwise raise TypeError."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers (int or float).")


def add(a, b):
    """Return the sum of a and b."""
    _validate_numbers(a, b)
    return a + b


def subtract(a, b):
    """Return the result of a minus b."""
    _validate_numbers(a, b)
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    _validate_numbers(a, b)
    return a * b


def divide(a, b):
    """Return the result of a divided by b.

    Raises:
        TypeError: If inputs are not numbers.
        ZeroDivisionError: If b is zero.
    """
    _validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
