"""Simple greeter module."""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"


def greet_formal(name: str, title: str = "Mr.") -> str:
    """Return a formal greeting."""
    if not name:
        return "Good day."
    return f"Good day, {title} {name}."
