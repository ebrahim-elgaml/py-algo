import sys

import pytest

from lib.segment_tree import SegmentTree


@pytest.fixture
def nums():
    return [1, 6, 5, 2, 4, 2]


@pytest.fixture
def sum_st(nums):
    return SegmentTree(nums)


@pytest.fixture
def min_st(nums):
    return SegmentTree(
        nums,
        operation=min,
        initialize=sys.maxsize,
    )


def test_query_sum(sum_st, nums):
    assert (
        sum_st.query(
            q_left=1,
            q_right=4,
            curr_left=0,
            curr_right=len(nums) - 1,
        )
        == sum(nums[1:5])
    )


def test_update_sum(sum_st, nums):
    sum_st.update(
        val=5,
        index=3,
        curr_left=0,
        curr_right=len(nums) - 1,
    )
    assert (
        sum_st.query(
            q_left=1,
            q_right=4,
            curr_left=0,
            curr_right=len(nums) - 1,
        )
        == sum(nums[1:5]) + 5
    )


def test_query_min(min_st, nums):
    assert (
        min_st.query(
            q_left=1,
            q_right=4,
            curr_left=0,
            curr_right=len(nums) - 1,
        )
        == min(nums[1:5])
    )
