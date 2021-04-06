import math
from operator import add
from typing import Callable, List


class SegmentTree:
    def __init__(
        self, a: List[int], initialize: int = 0, operation: Callable = add
    ) -> None:
        super().__init__()
        self.original_list = a
        self.tree: List[int] = [initialize] * self.__get_tree_size()
        self.operation = operation
        self.build(0, len(a) - 1)
        self.initialize = initialize

    def __get_tree_size(self):
        return 2 * (2 ** math.ceil(math.log2(len(self.original_list)))) + 1

    def build(
        self,
        left: int,
        right: int,
        tree_index: int = 0,
    ) -> int:
        if left == right:
            self.tree[tree_index] = self.original_list[left]
            return self.original_list[left]
        middle = (left + right) // 2

        self.tree[tree_index] = self.operation(
            self.build(left, middle, 2 * tree_index + 1),
            self.build(middle + 1, right, 2 * tree_index + 2),
        )
        return self.tree[tree_index]

    def query(
        self,
        q_left: int,
        q_right: int,
        curr_left: int,
        curr_right: int,
        tree_index: int = 0,
    ) -> int:
        if q_right < curr_left or curr_right < q_left:
            # Query outside range
            return self.initialize
        if q_left <= curr_left and curr_right <= q_right:
            # Range included inside query
            return self.tree[tree_index]
        middle = (curr_left + curr_right) // 2
        return self.operation(
            self.query(
                q_left,
                q_right,
                curr_left,
                middle,
                2 * tree_index + 1,
            ),
            self.query(
                q_left,
                q_right,
                middle + 1,
                curr_right,
                2 * tree_index + 2,
            ),
        )

    def update(
        self,
        val: int,
        index: int,
        curr_left: int,
        curr_right: int,
        tree_index: int = 0,
    ) -> None:
        if index < curr_left or index > curr_right:
            # Query outside range
            return
        self.tree[tree_index] = self.operation(
            self.tree[tree_index],
            val,
        )
        if curr_left != curr_right:
            middle = (curr_left + curr_right) // 2
            self.update(val, index, curr_left, middle, 2 * tree_index + 1)
            self.update(val, index, middle + 1, curr_right, 2 * tree_index + 2)
