from typing import List


class BinarySearch:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums

    def find(self, target: int) -> int:
        left, right = 0, len(self.nums)

        while left <= right:
            p = (left + right) // 2
            if self.nums[p] == target:
                return p

            if self.nums[p] < target:
                left = p + 1
            else:
                right = p - 1
        return -1

    def find_insertion_right(self, target: int) -> int:
        left, right = 0, len(self.nums)

        while left <= right and left < len(self.nums):
            p = (left + right) // 2

            if self.nums[p] <= target:
                left = p + 1
            else:
                right = p - 1
        return left
