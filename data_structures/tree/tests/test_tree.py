from tree.trees import BinaryTree,BinarySearchTree,Node
import pytest
        
def test_tree_init():
    tree = BinaryTree()
    assert tree.root == None

def test_tree_one_node():
    tree = BinaryTree()
    tree.root = Node(1)
    assert tree.root.value == 1

def test_tree_error():
    with pytest.raises(Exception):
        tree = BinaryTree()
        assert tree.in_order()

def test_tree_children_nodes(tree):
    assert tree.root.value == 5
    assert tree.root.left.value == 2
    assert tree.root.right.value == 10


def test_tree_preorder(tree2):
    assert tree2.pre_order() == [23, 8, 4, 16, 42, 27]

def test_tree_inorder(tree2):
    assert tree2.in_order() == [4, 8, 16, 23, 27, 42]

def test_tree_postorder(tree2):
    assert tree2.post_order() == [4, 16, 8, 27, 42, 23]

def test_tree_contains_true(tree2):
    assert tree2.Contains(4) == True

def test_tree_contains_false(tree2):
    assert tree2.Contains(100) == False

@pytest.fixture
def tree():
    tree = BinarySearchTree()
    tree.Add(5)
    tree.Add(2)
    tree.Add(10)

    return tree

@pytest.fixture
def tree2():
    tree2 = BinarySearchTree()
    [tree2.Add(i) for i in [23,8,42,4,16,27]]
    return tree2