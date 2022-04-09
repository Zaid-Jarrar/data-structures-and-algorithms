class Node:

    '''
    class that has properties for the value stored in the node,
    the left child node, and the right child node.
    
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)


    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root. this is 
           a utility function that gets used by the <display()> method for building pretty standdout 
           visualization of the binary tree. """

        # No child exists.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child exists.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child exists.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children exist.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '

        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
            
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinaryTree:
    '''
    Parent class for binary trees which has 3 methods to order the data 
    pre_order
    in_order
    post_order
    '''
    def __init__(self):
        self.root = None

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

    # def breathfirst(self): 
    #     if self.root is None:
    #         raise Exception ("Tree is empty")
    #     queue = Queue()
    #     current = self.root
    #     queue.enqueue(current)
    #     my_list = []
    #     while not queue.is_empty():
    #         current = queue.front

    #         print(f'---->  {current.value.value}')
    #         if current.value.left:
               
    #             queue.enqueue(current.value.left)
                
    #         if current.value.right:
    #             queue.enqueue(current.value.right)
    #         my_list.append(current.value.value)
    #         queue.dequeue()

    #     print(my_list)
        
class BinarySearchTree(BinaryTree):
    '''
    A subclass of BinaryTree used to add values to the tree and search for them
    - Add
    - contains
    '''
    def Add(self,value):
        '''
    Arguments: value
    Return: nothing
    Adds a new node with that value in the correct location in the binary search tree.
        '''
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if node.value < current.value:
                if not current.left:
                    current.left = node                   
                    break                
                current = current.left
            elif node.value > current.value:
                if not current.right:
                    current.right = node
                    break               
                current = current.right
            else:
                raise Exception("Value already exists in the Tree")
       
    def Contains(self,value):
        '''        
    Argument: value
    Returns: boolean indicating whether or not the value is in the tree at least once.
        '''
        if self.root is None:
            return False
        current = self.root

        while current:
            if current.value == value:
                # print(True)
                return True
            elif value < current.value:
                if current.left:
                    current = current.left
                else:
                    # print(False)
                    return False
            
            else:
                if current.right:
                    current = current.right
                else:
                    # print(False)
                    return False
            
        # OR
        # if value in self.in_order():
        #     print(True)
        #     return True
        # print(False)        
        # return False


# class QNode():
#     def __init__(self,value):
#         self.value = value
#         self.next = None
    
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
    
#     def enqueue(self,value):
#         node = QNode(value)
#         if self.front is None:
#             self.front = node
#             self.rear = node
#         self.rear.next = node
#         self.rear = node
    
#     def dequeue(self):
#         if self.front is None:
#             raise Exception('Queue is empty')
#         temp = self.front
#         self.front = self.front.next
#         temp.next = None
#         print(temp.value.value)
#         return temp.value

#     def is_empty(self):
#         if self.front is None:
#             return True
#         return False


       
if __name__ == "__main__":

    node1 = Node(23)
    node2 = Node(8)
    node3 = Node(42)
    node4 = Node(4)
    node5 = Node(16)
    node6 = Node(27)
    node1.left = node2
    node1.right = node3
    node3.left = node6
    node2.left = node4
    node2.right = node5


    # node1 = Node('A')
    # node2 = Node('B')
    # node3 = Node('C')
    # node4 = Node('D')
    # # node5 = Node('E')
    # node6 = Node('F')
    # node1,node2,node3,node4,node5,node6 = [Node(i) for i in ['A','B','C','D','E','F']]

    # node1.left,node1.right,node3.left,node2.left,node2.right = node2,node3,node6,node4,node5




    tree = BinaryTree()
    tree.root = node1
    tree.root.display()

    # tree.breathfirst()
    

    # tree2 = BinarySearchTree()
    # [tree2.Add(i) for i in [23,8,42,4,16,27]]
    # tree2.in_order()
    
    search = BinarySearchTree()
    search.root = node1
    search.Add(24)
    search.root.display()

    search.Contains(23)

    # tree.pre_order_itiration()
    # tree.pre_order()
    # tree.in_order()
    # tree.post_order()


 # INSERT USING RECURSION
        # def _walk(current):                
        #     # if node.value < current.value or node.value > current.value:
        #     if not current.left and node.value < current.value:
        #         current.left = node
        #         return
        #     if not current.right and node.value > current.value:
        #         current.right = node
        #         return
        #     if current.left and node.value < current.value :
        #         # if value < current.value:
        #         _walk(current.left)
        #     if current.right and node.value > current.value:
        #         # if value > current.value:
        #         _walk(current.right)

        # _walk(self.root)


        #         class Node:
        #     def __init__(self, value):
        #         self.value = value  ## Node
        #         self.next = None

        # class Stack:
        #     def __init__(self):
        #         self.top = None

        #     def push(self, value):
        #         """
        #     push will add a new Node to the stack

        #     input: value
        #     output: None

        #     """
        #         node = Node(value)
        #         node.next = self.top
        #         self.top = node

        #     def pop(self):
        #         """
        #     input: none
        #     doing: pop the top node from the stack 
        #     output: popped node's value
        #     """

        #         if self.is_empty():
        #             raise Exception("Stack is empty !")

        #         temp = self.top
        #         self.top = self.top.next
        #         temp.next = None

        #         return temp.value

        #     def is_empty(self):
        #         """
        #     input: None
        #     doing: Check if the top is none or not
        #     output: return a boolean
        #     """
        #         if self.top is None:
        #             return True
        #         return False

    # def pre_order_itiration(self):
    #     """
    # A method to traverse the tree elements
    # input: nothing
    # output: print the value of each node
    #     """
    #     stack = Stack()
    #     current = self.root

    #     stack.push(current)

    #     while not stack.is_empty():
    #         current = stack.pop()
    #         print(current.value)

    #         if current.right:
    #             stack.push(current.right)

    #         if current.left:
    #             stack.push(current.left)


