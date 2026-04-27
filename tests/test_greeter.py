from src.greeter import greet


def test_greet_with_name():
    result = greet("Phil")
    assert isinstance(result, str)
    assert "Phil" in result


def test_greet_empty():
    assert greet("") is not None
