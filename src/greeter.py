"""Simple greeter module."""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"
