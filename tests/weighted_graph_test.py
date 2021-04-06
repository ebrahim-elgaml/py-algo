from functools import reduce

import pytest

from lib.weighted_graph import WeightedGraph


@pytest.fixture
def graph():
    return WeightedGraph()


@pytest.fixture
def mst_graph(graph):
    _add_edges(
        graph=graph,
        edges_list=[
            (1, 2, 4),
            (1, 3, 4),
            (2, 3, 2),
            (3, 4, 3),
            (3, 5, 2),
            (3, 5, 4),
            (4, 6, 3),
            (5, 6, 3),
        ],
    )
    return graph


def test_add_edge_undirected(graph):
    graph.add_edge_undirected(v=1, u=2, w=3)

    assert graph.graph[1] == [(2, 3)]
    assert graph.graph[2] == [(1, 3)]
    assert len(graph.graph.keys()) == 2


def test_add_edge_directed(graph):
    graph.add_edge_directed(v=1, u=2, w=3)

    assert graph.graph[1] == [(2, 3)]
    assert graph.graph[2] == []
    assert len(graph.graph.keys()) == 2


def test_dijkstra(graph):
    """
    2 <---100---
    ^          |
    |          |
    500        |
    |          |
    0 --100--> 1
    """
    _add_edges(
        graph,
        [(0, 1, 100), (1, 2, 100), (0, 2, 500)],
        is_directed=True,
    )
    distances = graph.dijkstra(0)
    assert distances[2] == 200
    assert distances[1] == 100


def test_mst(mst_graph):
    prim, p_cost = mst_graph.mst_prim(1)
    kruskal, k_cost = mst_graph.mst_kruskal()

    assert p_cost == k_cost

    def flatted(lis):
        return set(reduce(lambda a, b: a + b, lis))

    # Assert all graph is connected
    all_vertices = set(mst_graph.graph.keys())
    assert flatted([v] + edges for v, edges in prim.items()) == all_vertices
    assert flatted([v] + edges for v, edges in kruskal.items()) == all_vertices


def _add_edges(graph, edges_list, is_directed=False):
    for u, v, w in edges_list:
        if is_directed:
            graph.add_edge_directed(u, v, w)
        else:
            graph.add_edge_undirected(u, v, w)
