import pytest
from tree_intersection.binary_tree import BinaryTree,Node
from tree_intersection.tree_intersection_ import tree_intersection

def test_tree_intersection(tree_1,tree_2):

    actual = tree_intersection(tree_1,tree_2)
    expected = {'0', '10', '2', '6'}
    assert actual == expected


def test_tree_intersection_fail():
    with pytest.raises(Exception):
        tree_intersection(BinaryTree(),BinaryTree())



def test_tree_intersection3(tree_3,tree_4):
    actual = tree_intersection(tree_3,tree_4)
    expected = {'6'}
    assert actual == expected





@pytest.fixture
def tree_1():
    bt1 = BinaryTree()
    bt1.root = Node(6)
    bt1.root.right = Node(9)
    bt1.root.left = Node(2)
    bt1.root.left.left = Node(0)
    bt1.root.right.left = Node(10)
    return bt1

@pytest.fixture    
def tree_2():

    bt2= BinaryTree()
    bt2.root = Node(6)
    bt2.root.right = Node(12)
    bt2.root.left = Node(2)
    bt2.root.left.left = Node(0)
    bt2.root.right.left = Node(10)

    return bt2
        

@pytest.fixture    
def tree_3():

    bt2 = BinaryTree()
    bt2.root = Node(6)

    return bt2


@pytest.fixture
def tree_4():
    bt1 = BinaryTree()
    bt1.root = Node(6)
    return bt1
