from src.greeter import greet, greet_formal


def test_greet_with_name():
    assert greet("Phil") == "Hello, Phil!"


def test_greet_empty():
    assert greet("") == "Hello, stranger!"


def test_greet_formal():
    assert greet_formal("Smith") == "Good day, Mr. Smith."


def test_greet_formal_custom_title():
    assert greet_formal("Smith", title="Dr.") == "Good day, Dr. Smith."


def test_greet_formal_empty():
    assert greet_formal("") == "Good day."
