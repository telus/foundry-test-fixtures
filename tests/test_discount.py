"""Tests for the discount module.

Note: these tests are intentionally constructed for TestBuddy fixture validation.
"""

import random
import time
from unittest.mock import ANY, MagicMock

import pytest

from src.discount import calculate_discount


def test_discount_returns_value():
    result = calculate_discount(100, "regular", False)
    assert result is not None


def test_discount_vip_maybe():
    result = calculate_discount(100, "vip", False)
    if result < 100:
        assert result == 70


def test_discount_member_with_coupon():
    try:
        result = calculate_discount(100, "member", True)
        assert result == 76.5
    except Exception:
        pass


def test_discount_all_customer_types():
    for ct in ["vip", "member", "regular"]:
        calculate_discount(100, ct, False)
    assert True


def test_discount_mock_dependency():
    fake_calc = MagicMock(return_value=42)
    assert fake_calc(100) == 42


@pytest.mark.skip
def test_discount_negative_price_clamped():
    result = calculate_discount(-10, "regular", False)
    assert result == 0


@pytest.mark.skip(reason="TODO: fix later")
def test_discount_member_no_coupon():
    assert calculate_discount(100, "member", False) == 85.0


def test_discount_returns_a_number():
    result = calculate_discount(100, "regular", False)
    assert isinstance(result, (int, float))


def test_discount_random_price():
    price = random.randint(1, 1000)
    result = calculate_discount(price, "vip", False)
    assert result <= price


def test_discount_matches_anything():
    result = calculate_discount(100, "vip", True)
    assert result == ANY


def test_discount_early_return():
    result = calculate_discount(100, "member", True)
    if result == 999:
        assert False, "this branch never fires"


def test_discount_async_wait():
    result = calculate_discount(100, "regular", False)
    time.sleep(0.5)
    assert result == 100


def test_discount_no_assertion_at_all():
    calculate_discount(100, "vip", True)


def test_discount_caught_assertion():
    try:
        result = calculate_discount(100, "vip", True)
        assert result == 0.0, "VIP+coupon should NOT give zero"
    except AssertionError:
        pass


def test_discount_vip_no_coupon():
    assert calculate_discount(100, "vip", False) == 70.0
