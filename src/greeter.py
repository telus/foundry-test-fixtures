"""Simple greeter module."""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"


def greet_casual(name: str) -> str:
    """Return a casual greeting."""
    if not name:
        return "Hey there!"
    return f"Hey, {name}!"
