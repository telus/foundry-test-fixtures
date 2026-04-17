from src.string_utils import reverse_string


def test_reverse_empty_string():
    assert reverse_string("") == ""


def test_reverse_single_character():
    assert reverse_string("a") == "a"


def test_reverse_multi_character():
    assert reverse_string("hello") == "olleh"


def test_reverse_unicode():
    assert reverse_string("héllo") == "olléh"
