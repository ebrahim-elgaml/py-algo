import pytest

from lib.union_find import UnionFind


@pytest.fixture
def regions():
    return [
        "Europe",
        "Africa",
        "South America",
        "Germany",
        "Austria",
        "Poland",
        "Egypt",
        "Tunisia",
        "Brazil",
        "Argentina",
    ]


@pytest.fixture
def uf(regions):
    return UnionFind(regions)


def test_find_init(uf, regions):
    for region in regions:
        assert uf.get_item(uf.find(region)) == region


def test_flat_union(uf):
    uf.union("Tunisia", "Africa")
    uf.union("Egypt", "Africa")
    assert uf.find("Tunisia") == uf.find("Egypt")


def test_union_noop(uf):
    before = uf.find("Europe")
    uf.union("Europe", "Europe")
    assert uf.find("Europe") == before


def test_nested_union(uf):
    uf.union("Germany", "Austria")
    uf.union("Austria", "Poland")
    uf.union("Germany", "Europe")
    assert (
        uf.find("Germany") == uf.find("Europe")
        and uf.find("Poland") == uf.find("Europe")
        and uf.find("Austria") == uf.find("Europe")
        and uf.find("Europe") == uf.find("Europe")
    )
