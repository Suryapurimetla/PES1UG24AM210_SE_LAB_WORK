"""Hypothesis fuzz tests and explicit regression checks."""
import math
import pytest
from hypothesis import given, settings, strategies as st
from airline_baggage import parse_booking, total_weight, tag_label

@settings(max_examples=500)
@given(st.text() | st.none())
def test_parse_booking_no_crash(s):
    result = parse_booking(s)
    assert result is None or (isinstance(result, tuple) and len(result) == 3 and result[1] > 0 and result[2] in 'ABCDEF')

@settings(max_examples=500)
@given(st.text() | st.none())
def test_total_weight_no_crash(s):
    result = total_weight(s)
    assert result is None or (math.isfinite(result) and result >= 0)

@settings(max_examples=500)
@given(st.text() | st.none())
def test_tag_label_no_crash(s):
    result = tag_label(s)
    assert result is None or (isinstance(result, str) and '. ' in result)

@given(st.sampled_from(['AI', '6E', 'UK']), st.integers(1, 9999), st.integers(1, 999), st.sampled_from(list('ABCDEF')))
def test_valid_booking(airline, flight, row, seat):
    assert parse_booking(f'{airline.lower()}-{flight}-{row}{seat.lower()}') == (airline, flight, seat)

@given(st.lists(st.integers(0, 100000), min_size=1, max_size=40))
def test_valid_weight_sum(weights):
    assert total_weight(','.join(map(str, weights))) == sum(weights)

@pytest.mark.parametrize('value', [None, '', 'AI-1-', 'AI-0-1A', 'AI-1-0A', 'AI-x-1A', 'AI-1-1Z', 'AI-1-1A-extra', 42, [], {}])
def test_invalid_booking(value):
    assert parse_booking(value) is None

@pytest.mark.parametrize('value', [None, '', ',', '1,,2', 'abc', '-1', 'NaN', 'inf', '1e309', '1e308,1e308', 42, [], {}])
def test_invalid_weights(value):
    assert total_weight(value) is None

@pytest.mark.parametrize('value', [None, '', '   ', 'Alice', 'Alice 123', 'A! Smith', 42, [], {}])
def test_invalid_name(value):
    assert tag_label(value) is None

@pytest.mark.parametrize('name, expected', [('Alice Smith', 'A. SMITH'), ('  alice   smith ', 'A. SMITH'), ('Mary Jane Watson', 'M. WATSON'), ("Anne-Marie O'Neil", "A. O'NEIL"), ('Éva Müller', 'É. MÜLLER')])
def test_valid_names(name, expected):
    assert tag_label(name) == expected
