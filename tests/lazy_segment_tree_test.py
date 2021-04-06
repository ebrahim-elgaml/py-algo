from functools import reduce
from operator import mul

import pytest

from lib.lazy_segment_tree import LazySegmentTree


@pytest.fixture
def nums():
    return [1, 6, 5, 2, 4, 2]


@pytest.fixture
def sum_st(nums):
    return LazySegmentTree(nums)


@pytest.fixture
def mul_st(nums):
    return LazySegmentTree(
        nums,
        operation=mul,
        initialize=1,
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


def test_single_update_sum(sum_st, nums):
    sum_st.update(
        val=5,
        update_left=2,
        update_right=4,
        curr_left=0,
        curr_right=len(nums) - 1,
    )
    assert (
        sum_st.query(
            q_left=1,
            q_right=3,
            curr_left=0,
            curr_right=len(nums) - 1,
        )
        == sum(nums[1:4]) + (5 * 2)
    )


def test_update_sum(sum_st, nums):
    sum_st.update(
        val=5,
        update_left=0,
        update_right=5,
        curr_left=0,
        curr_right=len(nums) - 1,
    )
    assert (
        sum_st.query(
            q_left=0,
            q_right=5,
            curr_left=0,
            curr_right=len(nums) - 1,
        )
        == sum(nums) + (5 * 6)
    )

    sum_st.update(
        val=1,
        update_left=3,
        update_right=5,
        curr_left=0,
        curr_right=len(nums) - 1,
    )
    assert (
        sum_st.query(
            q_left=3,
            q_right=5,
            curr_left=0,
            curr_right=len(nums) - 1,
        )
        == sum(nums[3:6]) + (5 * 3) + (1 * 3)
    )


def test_query_mul(mul_st, nums):
    assert (
        mul_st.query(
            q_left=1,
            q_right=4,
            curr_left=0,
            curr_right=len(nums) - 1,
        )
        == reduce(mul, nums[1:5])
    )


def test_update_mul(mul_st, nums):
    mul_st.update(
        val=2,
        update_left=2,
        update_right=3,
        curr_left=0,
        curr_right=len(nums) - 1,
    )
    assert (
        mul_st.query(
            q_left=1,
            q_right=4,
            curr_left=0,
            curr_right=len(nums) - 1,
        )
        == reduce(mul, nums[1:5]) * 4
    )
