from tree.trees import BinaryTree,BinarySearchTree,Node,breadth_first
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

#----------------------------------------- BinarySearchTree Tests -----------------------------------------
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

#----------------------------------------- BinaryTree Tests -----------------------------------------
def test_tree_bi_preorder(tree_bi):
    assert tree_bi.pre_order() == [23, 8, 4, 16, 42]

def test_tree_bi_inorder(tree_bi):
    assert tree_bi.in_order() == [4, 8, 16, 23, 42]

def test_tree_bi_postorder(tree_bi):
    assert tree_bi.post_order() == [4, 16, 8, 42, 23]

#-------------------------------------------------Get Max Tests-------------------------------------------------

def test_tree_get_max_50(tree_bi):
    assert tree_bi.Get_max() == 42

def test_tree_get_max2_5(binary_tree):
    assert binary_tree.Get_max() == 5

def test_tree_root_fail(binary_tree_root):
    with pytest.raises(Exception):
        assert binary_tree_root.root


#--------------------------------breadth_first_traversal Tests--------------------------------

def test_breadth_first_traversal(tree_bi):
    assert breadth_first(tree_bi) == [23, 8, 42, 4, 16]

def test_breadth_first_traversal_error(binary_tree_root):
    with pytest.raises (Exception):
        assert breadth_first(binary_tree_root)

def test_breadth_first_traversal_left(binary_tree_left):
    assert breadth_first(binary_tree_left) == [5, 3]

def test_breadth_first_traversal_right(binary_tree_right):
    assert breadth_first(binary_tree_right) == [5, 3, 4, 9]


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


@pytest.fixture
def tree_bi():
    tree2 = BinaryTree()
    node1 = Node(23)
    node2 = Node(8)
    node3 = Node(42)
    node4 = Node(4)
    node5 = Node(16)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    tree2.root = node1
    return tree2


@pytest.fixture
def binary_tree():
    binary_tree = BinaryTree()
    binary_tree.root = Node(5)
    return binary_tree


@pytest.fixture
def binary_tree_root():
    binary_tree_none = BinaryTree()
    return binary_tree_none

@pytest.fixture
def binary_tree_left():
    binary_tree_left = BinaryTree()
    binary_tree_left.root = Node(5)
    binary_tree_left.root.left = Node(3)
    return binary_tree_left

@pytest.fixture
def binary_tree_right():
    binary_tree_right = BinaryTree()
    binary_tree_right.root = Node(5)
    binary_tree_right.root.left = Node(3)
    binary_tree_right.root.right = Node(4)
    binary_tree_right.root.left.right = Node(9)


    return binary_tree_right