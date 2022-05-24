class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    '''
    Parent class for binary trees which has 3 methods to order the data 
    pre_order
    in_order
    post_order
    '''
    def __init__(self):
        self.root = None
        self.counter = 0

    def pre_order(self):
        """
    Input: None
    doing: traverse a tree root >> left >> right
    output: returns an array of the values, ordered appropriately.
    """
        if self.root is None:
            raise Exception ("Tree is empty")
        node_array = []
        def _walk(node):
            node_array.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)

        print(node_array)
        return node_array

    def in_order(self):
        """
    Input: None
    doing: traverse a tree left >> root >> right
    output: returns an array of the values, ordered appropriately.
    """
        if self.root is None:
            raise Exception ("Tree is empty")    
        node_array = []
        def _walk(node):

            if node.left:
                _walk(node.left)

            node_array.append(node.value)

            if node.right:
                _walk(node.right)

        _walk(self.root)
        print(node_array)
        return node_array 

    def post_order(self):
        """
    Input: None
    doing: traverse a tree left >> right >> root
    output: returns an array of the values, ordered appropriately.
    """
        if self.root is None:
            raise Exception ("Tree is empty")
        node_array = []

        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            node_array.append(node.value)

        _walk(self.root)
        print(node_array)
        return node_array