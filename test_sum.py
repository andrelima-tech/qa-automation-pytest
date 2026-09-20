import pytest


def sum_numbers(a, b):
    return a + b


@pytest.fixture
def base_number():
    return 2


def test_sum_two_positive_numbers(base_number):
    assert sum_numbers(base_number, 3) == 5


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_sum_returns_expected_result(a, b, expected):
    assert sum_numbers(a, b) == expected