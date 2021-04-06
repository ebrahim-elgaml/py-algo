from typing import Dict, Generic, List, TypeVar

T = TypeVar("T", int, str)


class UnionFind(Generic[T]):
    def __init__(self, items: List[T]) -> None:
        self.items: List[T] = items
        self.item_to_id: Dict[T, int] = {e: i for i, e in enumerate(items)}
        self.parents = [n for n in range(len(items))]
        self.sizes = [1] * len(items)

    def find(self, item: T) -> int:
        """Returns the parent of the group that
        item belongs to
        """
        root = self.item_to_id[item]

        while root != self.parents[root]:
            root = self.parents[root]

        # Compress
        curr = self.item_to_id[item]
        while curr != root:
            curr, self.parents[curr] = self.parents[curr], root

        return root

    def union(self, item1: T, item2: T) -> None:
        x, y = self.find(item1), self.find(item2)

        if x == y:
            return

        if self.sizes[y] < self.sizes[x]:
            x, y = y, x

        self.sizes[x] += self.sizes[y]
        self.parents[y] = x

    def get_item(self, i: int) -> T:
        return self.items[i]
