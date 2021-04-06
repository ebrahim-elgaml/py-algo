import math
import random
from functools import reduce
from operator import mul

import pytest

from lib.number_theory import chinese_remainder, ecludian_gcd, fast_pow, sieve


@pytest.mark.parametrize(
    "n, p",
    [
        (random.randint(0, 1000), random.randint(0, 1000)),
        (0, 1),
        (0, 0),
        (2, 0),
        (2, 1),
        (1, 9),
    ],
)
def test_fast_pow(n, p):
    # n = random.randint(0, 1000)
    # p = random.randint(0, 1000)
    assert n ** p == fast_pow(n, p)


def test_sieve():
    assert sieve(20) == {
        0,
        1,
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
    }


def test_gcd():
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    assert math.gcd(a, b) == ecludian_gcd(a, b)


def test_chineese_remainder():
    n = [3, 5, 7]
    a = [2, 3, 2]
    x, p = chinese_remainder(n, a)
    assert x == 23
    assert p == reduce(mul, n)
