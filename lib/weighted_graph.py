import heapq
import sys
from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple

from lib.union_find import UnionFind


class WeightedGraph:
    def __init__(self) -> None:
        self.graph: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)

    def add_edge_directed(self, v: int, u: int, w: int):
        self.graph[v].append((u, w))
        self.graph[u]

    def add_edge_undirected(self, v: int, u: int, w: int):
        self.graph[v].append((u, w))
        self.graph[u].append((v, w))

    def dijkstra(self, src: int) -> Dict[int, int]:
        distances = {v: sys.maxsize for v in self.graph}
        distances[src] = 0

        q = [(0, src)]

        while q:
            curr_w, curr_v = heapq.heappop(q)

            if curr_w > distances[curr_v]:
                continue

            for u, w in self.graph[curr_v]:
                new_dist = curr_w + w
                if new_dist < distances[u]:
                    distances[u] = new_dist
                    heapq.heappush(q, (new_dist, u))
        return distances

    def mst_prim(self, start: int) -> Tuple[Dict[int, List[int]], int]:
        # Prim O(VlogV + E)
        cost = 0
        mst = defaultdict(list)
        visited = {start}
        pq = [(w, start, to) for to, w in self.graph[start]]
        heapq.heapify(pq)
        while pq:
            w, fro, to = heapq.heappop(pq)
            if to not in visited:
                mst[fro].append(to)
                cost += w
                visited.add(to)
                for u, uw in self.graph[to]:
                    if u not in visited:
                        heapq.heappush(pq, (uw, to, u))
        return mst, cost

    def mst_kruskal(self) -> Tuple[DefaultDict[int, List[int]], int]:
        # Kruskal --> O(ElogE)
        cost = 0
        mst = defaultdict(list)
        pq = [(w, v, u) for v, items in self.graph.items() for u, w in items]
        heapq.heapify(pq)
        uf = UnionFind(list(self.graph.keys()))
        while pq:
            w, v, u = heapq.heappop(pq)
            if uf.find(v) != uf.find(u):
                uf.union(v, u)
                mst[v].append(u)
                cost += w
        return mst, cost
