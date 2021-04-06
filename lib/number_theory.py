import math
from typing import List, Set, Tuple


def fast_pow(n, p) -> int:
    # n** p
    if n == 0:
        return 1 if p == 0 else 0
    if n == 1:
        return n

    half = n ** (p // 2)
    result = half * half
    return result if p % 2 == 0 else result * n


def sieve(n) -> Set[int]:
    s = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if not s[i]:
            continue

        for j in range(i ** 2, n + 1, i):
            s[j] = False

    return {i for i in range(n + 1) if s[i]}


def ecludian_gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    return ecludian_gcd(y, x % y)


def powmod(x: int, y: int, m: int) -> int:
    if y == 0:
        return 1

    p = powmod(x, y // 2, m) % m
    p = (p * p) % m
    return p if y % 2 == 0 else (x * p) % m


def modinv(x: int, m: int) -> int:
    return powmod(x, m - 2, m)


def chinese_remainder(n: List[int], a: List[int]) -> Tuple[int, int]:
    """
    x = a1 mod n1
    x = a2 mod n2
    https://www.youtube.com/watch?v=0dbXaSkZ-vc
    """
    x = 0

    prod = 1
    for n_i in n:
        prod *= n_i

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        x += a_i * modinv(p, n_i) * p

    return int(x % prod), prod
