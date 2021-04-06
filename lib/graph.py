from collections import defaultdict
from typing import Dict, List, Set


class Graph:
    def __init__(self):
        self.graph: Dict[int, Set[int]] = defaultdict(set)

    def add_edge_undirected(self, v: int, u: int):
        self.graph[v].add(u)
        self.graph[u].add(v)

    def add_edge_directed(self, v: int, u: int):
        self.graph[v].add(u)
        self.graph[u]

    def connected_components(self) -> List[List[int]]:
        visited = set()
        connected = []

        def connected_helper(v: int, tmp: List[int]) -> List[int]:
            visited.add(v)
            tmp.append(v)
            for u in self.graph[v]:
                if u not in visited:
                    tmp = connected_helper(u, tmp)
            return tmp

        for v in self.graph:
            if v not in visited:
                connected.append(connected_helper(v, []))

        return connected

    def is_cycle(self) -> bool:
        colors = defaultdict(lambda: 0)

        def dfs_cycle(v: int) -> bool:
            colors[v] = 1
            for u in self.graph[v]:
                if colors[u] == 1 or (colors[u] == 0 and dfs_cycle(u)):
                    return True

            colors[v] = 2
            return False

        for v in self.graph.keys():
            if colors[v] == 0 and dfs_cycle(v):
                return True
        return False

    def topological_sort(self) -> List[int]:
        visited = set()
        st = []

        def dfs_topo(v: int):
            visited.add(v)
            for u in self.graph[v]:
                if u not in visited:
                    dfs_topo(u)
            st.append(v)

        for v in self.graph.keys():
            if v not in visited:
                dfs_topo(v)
        return list(reversed(st))
