import pytest

from lib.graph import Graph


@pytest.fixture
def graph():
    return Graph()


def test_add_edge_undirected(graph):
    graph.add_edge_undirected(1, 2)

    assert graph.graph[1] == {2}
    assert graph.graph[2] == {1}
    assert len(graph.graph.keys()) == 2


def test_add_edge_directed(graph):
    graph.add_edge_directed(1, 2)

    assert graph.graph[1] == {2}
    assert not graph.graph[2]
    assert len(graph.graph.keys()) == 2


def test_connected_components(graph):
    # Component 1
    _add_edges(
        graph=graph,
        edges_list=[
            (1, 2),
            (2, 3),
            (3, 4),
            (1, 5),
        ],
    )
    # Component 2
    graph.add_edge_undirected(6, 7)

    components = graph.connected_components()
    assert len(components) == 2
    components = list(map(sorted, components))
    assert [1, 2, 3, 4, 5] in components
    assert [6, 7] in components


@pytest.mark.parametrize(
    "edges, is_cycle",
    [([(1, 2), (2, 3), (3, 4)], False), ([(1, 2), (2, 3), (3, 1)], True)],
)
def test_is_cycle(graph, edges, is_cycle):
    _add_edges(graph, edges, is_directed=True)
    assert graph.is_cycle() == is_cycle


def test_topological_sort(graph):
    """
    3 -> 6
    ^
    |
    1 -> 2 -> 5
    |
    v
    4
    """
    _add_edges(
        graph=graph,
        edges_list=[
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 5),
            (3, 6),
        ],
        is_directed=True,
    )
    topo = graph.topological_sort()
    assert topo.index(1) < topo.index(2)
    assert topo.index(1) < topo.index(3)
    assert topo.index(1) < topo.index(4)
    assert topo.index(1) < topo.index(5)
    assert topo.index(2) < topo.index(5)
    assert topo.index(1) < topo.index(6)
    assert topo.index(3) < topo.index(5)


def _add_edges(graph, edges_list, is_directed=False):
    for u, v in edges_list:
        if is_directed:
            graph.add_edge_directed(u, v)
        else:
            graph.add_edge_undirected(u, v)
