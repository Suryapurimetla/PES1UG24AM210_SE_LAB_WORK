
import pytest
from airline_baggage import (
    baggage_fee,
    carry_on_ok,
    check_in_status,
)


def test_baggage_invalid_cabin():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 20, "domestic", False)


def test_baggage_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -1, "domestic", False)


def test_baggage_within_allowance():
    assert baggage_fee("economy", 15, "domestic", False) == 0


def test_baggage_member_allowance():
    assert baggage_fee("economy", 20, "domestic", True) == 0


def test_baggage_business_allowance():
    assert baggage_fee("business", 40, "domestic", True) == 0


def test_baggage_domestic_fee():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_baggage_international_fee():
    assert baggage_fee("premium", 30, "international", False) == 225


def test_baggage_high_excess_domestic():
    assert baggage_fee("economy", 36, "domestic", False) == 840


def test_baggage_high_excess_international():
    assert baggage_fee("economy", 36, "international", False) == 2100


def test_carry_on_infant_allowed():
    assert carry_on_ok(10, 2, True) is True


def test_carry_on_infant_too_many_items():
    assert carry_on_ok(10, 3, True) is False


def test_carry_on_overweight():
    assert carry_on_ok(8, 1, False) is False


def test_carry_on_one_item():
    assert carry_on_ok(7, 1, False) is True


def test_carry_on_too_many_items():
    assert carry_on_ok(7, 2, False) is False


def test_checkin_open_domestic_with_baggage():
    assert check_in_status(60, True, False) == "open"


def test_checkin_late_domestic_with_baggage():
    assert check_in_status(50, True, False) == "late"


def test_checkin_closed_domestic_with_baggage():
    assert check_in_status(44, True, False) == "closed"


def test_checkin_open_without_baggage():
    assert check_in_status(45, False, False) == "open"


def test_checkin_international_with_baggage():
    assert check_in_status(120, True, True) == "open"


def test_checkin_international_late():
    assert check_in_status(110, True, True) == "late"


def test_checkin_international_closed():
    assert check_in_status(90, True, True) == "closed"
