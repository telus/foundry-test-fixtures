"""Simple calculator module with arithmetic operations."""

from typing import Union

Numeric = Union[int, float]


def _validate_inputs(a: object, b: object) -> None:
    """Raise TypeError if either argument is not an int or float (bools excluded)."""
    for val in (a, b):
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(
                f"Expected numeric (int or float) arguments, got {type(val).__name__}"
            )


def add(a: Numeric, b: Numeric) -> Numeric:
    """Return the sum of a and b."""
    _validate_inputs(a, b)
    return a + b


def subtract(a: Numeric, b: Numeric) -> Numeric:
    """Return the difference of a and b."""
    _validate_inputs(a, b)
    return a - b


def multiply(a: Numeric, b: Numeric) -> Numeric:
    """Return the product of a and b."""
    _validate_inputs(a, b)
    return a * b


def divide(a: Numeric, b: Numeric) -> float:
    """Return a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    _validate_inputs(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
