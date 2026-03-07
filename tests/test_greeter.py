from src.greeter import greet


def test_greet_with_name():
    assert greet("Phil") == "Hello, Phil!"


def test_greet_empty():
    assert greet("") == "Hello, stranger!"
