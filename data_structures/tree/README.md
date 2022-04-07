# Trees
<!-- Short summary or background information -->

A Tree is a Data structure in which data items are connected using references in a hierarchical manner. Each Tree consists of a root node from which we can access each element of the tree. Starting from the root node, each node contains zero or more nodes connected to it as children.

## Challenge
<!-- Description of the challenge -->
- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
- Create a Binary Tree class
Define a method for each of the depth first traversals:
- pre_order
- in_order
- post_order which returns an array of the values, ordered appropriately.

- Create a Binary Search Tree class this class should be a sub-class of the Binary Tree Class with the following additional methods:
- **Add**:Adds a new node with that value in the correct location in the binary search tree
- **Contains** :boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Add -- Big O(n) time and O(1) space using a while loop
- Contains-- Big O(n) time and O(1) space by calling on of the order methods and search in the return if value is found or not 
- pre order, in_order post_order -- Big O(n) time and O(n) space using recursion

## API
<!-- Description of each method publicly available in each of your trees -->

Node:
```
    
    class that has properties for the value stored in the node,
    the left child node, and the right child node.
```    
   
BinaryTree:
```     
    Parent class for binary trees which has 3 methods to order the data 
    Pre-order: root >> left >> right
    In-order: left >> root >> right
    Post-order: left >> right >> root
    Input: None
    doing: traverse a tree
    output: returns an array of the values, ordered appropriately.
```    

BinarySearchTree:
```
    A subclass of BinaryTree used to add values to the tree and search for them
Add:
    Arguments: value
    Return: nothing
    Adds a new node with that value in the correct location in the binary search tree.
contains:     
    Argument: value
    Returns: boolean indicating whether or not the value is in the tree at least once.
    
```

- [x] Create Node class
- [x] Create BinaryTree class.
- [x] Create BinarySearchTree class.
- [x] Upon instantiation, an empty BinaryTree should be created.
- [x] pre_order
- [x] in_order
- [x] post_order
- [x] Add
- [x] Contains
 