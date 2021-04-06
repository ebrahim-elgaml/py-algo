import sys
from typing import List


def coin_change(amount: int, coins: List[int]) -> int:
    if amount == 0:
        return 0
    dp = [sys.maxsize] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != sys.maxsize else -1


def knapsack(values: List[int], weights: List[int], max_capacity: int) -> int:
    dp = [[0] * (max_capacity + 1) for _ in range(len(values) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            if j - weights[i - 1] >= 0:
                dp[i][j] = max(
                    dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1]
                )
    return dp[-1][-1]
