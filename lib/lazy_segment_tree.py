import math
from operator import add
from typing import Callable, List


class LazySegmentTree:
    def __init__(
        self, a: List[int], initialize: int = 0, operation: Callable = add
    ) -> None:
        super().__init__()
        self.original_list = a
        self.tree: List[int] = [initialize] * self.__get_tree_size()
        self.lazy: List[int] = [initialize] * len(self.tree)
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

        if self.lazy[tree_index] != self.initialize:
            self.propagate(curr_left, curr_right, tree_index)

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
        update_left: int,
        update_right: int,
        curr_left: int,
        curr_right: int,
        tree_index: int = 0,
    ) -> None:
        if self.lazy[tree_index] != self.initialize:
            self.propagate(curr_left, curr_right, tree_index)
        if (
            update_right < curr_left
            or curr_right < update_left
            or curr_right < curr_left
        ):
            # Out of range
            return

        if update_left <= curr_left and curr_right <= update_right:
            # fully included
            self.lazy[tree_index] = self.operation(
                self.lazy[tree_index],
                val,
            )
            self.propagate(curr_left, curr_right, tree_index)
            return

        if curr_left != curr_right:
            middle = (curr_left + curr_right) // 2
            self.update(
                val,
                update_left,
                update_right,
                curr_left,
                middle,
                2 * tree_index + 1,
            )
            self.update(
                val,
                update_left,
                update_right,
                middle + 1,
                curr_right,
                2 * tree_index + 2,
            )
            self.tree[tree_index] = self.operation(
                self.tree[2 * tree_index + 1],
                self.tree[2 * tree_index + 2],
            )

    def propagate(
        self,
        curr_left: int,
        curr_right: int,
        tree_index: int,
    ) -> None:
        lazy_val = self.lazy[tree_index] * (curr_right - curr_left + 1)
        self.tree[tree_index] = self.operation(
            self.tree[tree_index],
            lazy_val,
        )
        if curr_left != curr_right:
            # Not a leaf
            self.lazy[2 * tree_index + 1] += self.lazy[tree_index]
            self.lazy[2 * tree_index + 2] += self.lazy[tree_index]
        self.lazy[tree_index] = self.initialize
