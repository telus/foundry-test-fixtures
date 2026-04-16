"""Calculator module providing basic arithmetic operations with input validation."""

from typing import Union

Number = Union[int, float]


def _validate_inputs(a: object, b: object) -> None:
    """Raise TypeError if either argument is not a numeric type (int or float).

    Booleans are explicitly rejected even though bool is a subclass of int.
    """
    for val in (a, b):
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(
                f"Arguments must be numeric (int or float), got {type(val).__name__!r}"
            )


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The arithmetic sum of a and b.

    Raises:
        TypeError: If either argument is not int or float.
    """
    _validate_inputs(a, b)
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of a and b.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The arithmetic difference a - b.

    Raises:
        TypeError: If either argument is not int or float.
    """
    _validate_inputs(a, b)
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The arithmetic product of a and b.

    Raises:
        TypeError: If either argument is not int or float.
    """
    _validate_inputs(a, b)
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return the quotient of a divided by b.

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        The float result of a / b.

    Raises:
        TypeError: If either argument is not int or float.
        ValueError: If b is zero.
    """
    _validate_inputs(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
