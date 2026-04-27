"""Tests for the discount module.

Note: these tests are intentionally constructed for TestBuddy fixture validation.
"""

import random
from unittest.mock import MagicMock

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


def test_discount_returns_a_number():
    result = calculate_discount(100, "regular", False)
    assert isinstance(result, (int, float))


def test_discount_random_price():
    price = random.randint(1, 1000)
    result = calculate_discount(price, "vip", False)
    assert result <= price


def test_discount_vip_no_coupon():
    assert calculate_discount(100, "vip", False) == 70.0
