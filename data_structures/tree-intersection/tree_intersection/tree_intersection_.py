from tree_intersection.hashtable import HashTable
from tree_intersection.binary_tree import BinaryTree,Node


def tree_intersection(bt1, bt2):
    """
    Input: two binary trees
    doing: traverse the first tree and store the values in a hashtable
    output: returns an array of the values, ordered appropriately.
    """
    if bt1.root is None or bt2.root is None:
        raise Exception ("Tree is empty")

    # intersections = []
    hashtable = HashTable()

    def tree_traversal(root,root2):
        if root.value == root2.value:
            # intersections.append(root.value)
            hashtable.set(str(root.value), True)
        if root.left and root2.left:
            tree_traversal(root.left,root2.left)
        if root.right and root2.right:
            tree_traversal(root.right,root2.right)
    tree_traversal(bt1.root,bt2.root)
    return set(hashtable.keys())


if __name__ == '__main__':
    pass
    # Bt1 = BinaryTree()
    # Bt1.root = Node(12)
    # Bt1.root.right = Node(9)
    # Bt1.root.left = Node(2)
    # Bt1.root.left.left = Node(0)
    # Bt1.root.right.left = Node(10)

    # Bt2 = BinaryTree()
    # Bt2.root = Node(12)
    # Bt2.root.right = Node(2)
    # Bt2.root.left = Node(2)
    # Bt2.root.left.left = Node(18)

    # Bt3 = BinaryTree()
    # Bt3.root = Node(150)
    # node2 =  Node(100)
    # node3 =  Node(250)
    # node4 =  Node(75)
    # node5 =  Node(175)
    # node6 =  Node(125)

    # Bt3.root.left = node2
    # Bt3.root.right = node3
    # node2.left = node4
    # # node2.right = node7
    # # node3.left = node11
    # # node3.right = node9
    # # node7.left = node6
    # # node7.right = node5

    # Bt4 = BinaryTree()
    # Bt4.root = Node(150)
  

    # Bt4.root.left = node2
    # Bt4.root.right = node3
    # node2.left = node4
    # node2.right = node7
    # node3.left = node11
    # node3.right = node9
    # node7.left = node6
    # node7.right = node5
    

    # print(tree_intersection(Bt1, Bt2))
    # print(tree_intersection(Bt1, Bt2))
# def tree_intersection(bt1, bt2):

#     """
#     Input: two binary trees
#     doing: traverse the first tree and store the values in a hashtable
#     output: returns an array of the values, ordered appropriately.
#     """
#     if bt1.root is None or bt2.root is None:
#         raise Exception ("Tree is empty")
#     intersections = []
#     hashtable = HashTable()

#     def tree_traversal(root):
#         if hashtable.contains(str(root.value)) == True:
#             intersections.append(root.value)
#         else:
#             hashtable.set(str(root.value), True)
#         if root.left:
#             tree_traversal(root.left)
#         if root.right:
#             tree_traversal(root.right)  
        
#     tree_traversal(bt1.root)
#     tree_traversal(bt2.root)
    
#     return intersections