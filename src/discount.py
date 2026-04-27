"""Discount calculation."""


def calculate_discount(price: float, customer_type: str, has_coupon: bool) -> float:
    """Return the price after applying customer-tier and coupon discounts.

    VIP gets 30 percent off, member gets 15 percent off, regular gets none.
    A coupon stacks an additional 10 percent off, but only for member and
    regular tiers (VIP cannot stack).
    """
    if price < 0:
        return 0.0

    if customer_type == "vip":
        discounted = price * 0.70
    elif customer_type == "member":
        discounted = price * 0.85
    else:
        discounted = price

    if has_coupon and customer_type != "vip":
        discounted = discounted * 0.90

    return round(discounted, 2)
