import pytest

from lib.binary_search import BinarySearch


@pytest.fixture
def bs():
    return BinarySearch([1, 5, 6, 6, 6, 7, 9, 16])


def test_found(bs):
    for n in bs.nums:
        pos = bs.find(n)
        assert bs.nums[pos] == n


def test_not_found(bs):
    assert bs.find(0) == -1


@pytest.mark.parametrize(
    "num, result_position",
    [
        (0, 0),  # First position
        (2, 1),  # Position in the middle
        (6, 5),  # Repeated number
        (17, 8),  # Last posotion
    ],
)
def test_find_insertion_right(bs, num, result_position):
    assert bs.find_insertion_right(num) == result_position
