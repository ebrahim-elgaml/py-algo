import pytest

from lib.dp import coin_change, knapsack


@pytest.mark.parametrize(
    "amount, coins, result",
    [
        (25, [2, 5, 10, 20], 2),
        (21, [5, 10, 20], -1),
        (23, [1, 2, 5, 10], 4),
        (0, [1], 0),
    ],
)
def test_coin_change(amount, coins, result):
    assert coin_change(amount, coins) == result


def test_knapsack():
    assert knapsack([10, 40, 30, 50], [5, 4, 6, 3], 10) == 90
