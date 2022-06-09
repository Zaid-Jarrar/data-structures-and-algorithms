import pytest
from graph.graph_ import Graph


def test_graph_init():
    graph = Graph()
    assert graph.adjacency_list == {}

def test_graph_add_node():
    graph = Graph()
    graph.add_node(1)
    actual = graph.get_node()
    expected = [1]
    assert actual == expected

def test_graph_add_edge():
    graph = Graph()
    node1=graph.add_node(1)
    node2=graph.add_node(2)
    graph.add_edge(node1, node2)
    actual = graph.get_neighbors(node1)
    expected = [[2, 0]]
    assert actual == expected


def test_graph_get_node():
    graph = Graph()
    node1=graph.add_node(1)
    node2=graph.add_node(2)
    graph.add_edge(node1, node2)
    assert graph.get_node() == [1, 2]

def test_graph_get_neighbors_1():
    graph = Graph()
    node1=graph.add_node(1)
    node2=graph.add_node(2)
    node3=graph.add_node(3)
    node4=graph.add_node(4)
    graph.add_edge(node1, node2)
    graph.add_edge(node1, node3)
    graph.add_edge(node1, node4)
    assert graph.get_neighbors(node1) == [[2, 0], [3, 0], [4, 0]]


def test_graph_get_neighbors_2():
    graph = Graph()
    node1=graph.add_node(1)
    node2=graph.add_node(2)
    node3=graph.add_node(3)
    node4=graph.add_node(4)
    graph.add_edge(node1, node2,5)
    graph.add_edge(node1, node3,6)
    graph.add_edge(node1, node4,7)
    assert graph.get_neighbors(node1) ==  [[2, 5], [3, 6], [4, 7]]

def test_graph_size():
    graph = Graph()
    node1=graph.add_node(1)
    node2=graph.add_node(2)
    graph.add_edge(node1, node2)
    assert graph.size() == 2


def test_graph_one_node_one_edge():
    graph = Graph()
    node = graph.add_node(1)
    graph.add_edge(node,node,5) 
    actual = graph.get_neighbors(node)
    expected = [[1, 5]]
    assert actual == expected

def test_graph_empty_graph():
    graph = Graph()
    actual = graph.get_node()
    expected = []
    assert actual == expected


def test_graph_error_add_edge_to_graph():
    with pytest.raises(Exception):
        graph = Graph()
        graph.add_edge(1, 2)









