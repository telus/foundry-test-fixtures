from src.string_utils import reverse_string


def test_reverse_string_empty():
    assert reverse_string("") == ""


def test_reverse_string_single_char():
    assert reverse_string("a") == "a"


def test_reverse_string_multi_char():
    assert reverse_string("hello") == "olleh"


def test_reverse_string_unicode():
    assert reverse_string("héllo") == "olléh"
