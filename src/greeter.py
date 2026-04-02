"""Simple greeter module."""

from src.templates import load_greeting_template


def greet(name: str, template: str | None = None) -> str:
    """Return a greeting for the given name, optionally using a template."""
    if template:
        tmpl = load_greeting_template(template)
        return tmpl.format(name=name or "stranger")
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"
