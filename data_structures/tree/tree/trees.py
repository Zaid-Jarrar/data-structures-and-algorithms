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
    
    # def compare_directory_structures(self,tree1,tree2):
    #     # each folder must have either one or two files/folders as children 
    #     # only files dont have children so they are leaf nodes
    #     if tree1.root and tree2.root is None:
    #         raise Exception('Trees are empty')
    #     tree1_files_num = 0
    #     tree2_files_num = 0
    #     for structure in tree1.post_order():

    #         if structure.lower() != 'folder':
    #             tree1_files_num += 1
    #     for structure in tree2.post_order():
    #         if structure.lower() != 'folder':
    #             tree2_files_num += 1
    #     if tree1_files_num == tree2_files_num:
    #         print(True)
    #         return True
    #     print(False)
    #     return False
    # make this as a function as well 
    def compare_directory_structures(self,tree1,tree2):
        """
        a method that compares between two directory structures and returns True if the number of files match for both
        input: directory structure, directory structure
        output: Boolean value
    
        """
        if tree1.root and tree2.root is None:
            raise Exception('Trees are empty')
        # output = []
        
        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            if not node.right and not node.left:              
                # output.append(1)
                self.counter += 1
                
        _walk(tree1.root)
        tree1_file_num = self.counter
        self.counter = 0
        print(tree1_file_num)
        # num1 = len(output)
        # print(output)
        output = []
        _walk(tree2.root)
        # num2 = len(output) 
        tree2_file_num = self.counter 
        print(tree2_file_num)  
        # print(output)
        if tree2_file_num == tree1_file_num:
            print(True)
            return True
        print(False)
        return False




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
    def Get_max(self):
        """  
        Input: Takes 0 arguments 
        Output: Return the maximum value in the tree """
        if self.root is None:
            raise Exception ("Tree is empty")
        current = self.root
        queue = Queue()
        queue.enqueue(current)
        max_value = 0
        while not queue.is_empty():

            current = queue.front
            if current.value.value > max_value:
                max_value = current.value.value
            if current.value.left:
                queue.enqueue(current.value.left)
            if current.value.right:
                queue.enqueue(current.value.right)
            queue.dequeue() 
        print(max_value)
        return max_value
        
        # max_value = 0
        # for max in self.in_order():
        #     if max > max_value:
        #         max_value = max
        # print(max_value)
        # return max_value

     
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
            
    # def odd_number_sum(self):
    #     '''
    #     Input: None
    #     Output: Returns the sum of all the odd numbers in the tree
    #     '''
    #     if self.root is None:
    #         raise Exception ("Tree is empty")
    #     sum = 0
    #     for value in self.pre_order():
    #         if value % 2 == 1:
    #             sum += int(value)
    #     print(sum)
    #     return sum

    def odd_number_sum(self):
        if self.root is None:
            raise Exception('Tree is empty')
        sum = 0
        output = []
        def _walk(node):
            output.append(node.value)
            # you can do this instead of the for but you need to make the sum an attribute of the class and not the function
            # if node.value % 2 != 0:
            #     sum += node.value
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        print(output)
        for value in output:
            if value % 2 == 1:
                sum += value
        print(sum)
        return sum

        


        # OR
        # if value in self.in_order():
        #     print(True)
        #     return True
        # print(False)        
        # return False


class QNode():
    def __init__(self,value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        node = QNode(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def dequeue(self):
        if self.front is None:
            raise Exception('Queue is empty')
        temp = self.front
        # print(self.front.value.value)
        self.front = self.front.next
       
        temp.next = None
        # print(temp.value.value)
        return temp.value

    def is_empty(self):
        if self.front is None:
            return True
        return False
    def __str__(self):
        output = ''
        if not self.front:
            return 'The queue is empty'
        else:
            current = self.front
            while current:
                output += f'{current.value.value} --> '
                current = current.next
            output += 'Null'
            return 


def breadth_first(tree):
    '''
    Input: Tree as an arugment 
    Output: Returns a list of the values in the tree in the order they were encountered. ''' 
    if tree.root is None:
        raise Exception ("Tree is empty")
    queue = Queue()
    current = tree.root
    queue.enqueue(current)
    output = []
    while not queue.is_empty():
        current = queue.front

        # print(f'---->  {current.value.value}')
        if current.value.left:

            queue.enqueue(current.value.left)

        if current.value.right:
            queue.enqueue(current.value.right)
        output.append(current.value.value)
        queue.dequeue()

    print(output)
    return output   


       
if __name__ == "__main__":

    node1 = Node(23)
    node2 = Node(8)
    node3 = Node(42)
    node4 = Node(4)
    node5 = Node(16)
    node6 = Node(27)
    node7 = Node(50)
    node1.left = node2
    node1.right = node3

    node3.left = node6
    node3.right = node7
    node2.left = node4
    node2.right = node5

    # binary_tree = BinaryTree()
    # node11= Node(5)
    # binary_tree.root = node11
    # node11.left = node1

    # breadth_first(binary_tree)
    # binary_tree.root.display()

    sum = BinarySearchTree()
    sum.root = node1
    sum.root.display()
    sum.odd_number_sum()


    # node1 = Node('A')
    # node2 = Node('B')
    # node3 = Node('C')
    # node4 = Node('D')
    # # node5 = Node('E')
    # node6 = Node('F')
    node1,node2,node3,node5 = [Node(i) for i in ['Folder','Folder','.py','.txt']]
    node7,node8,node9,node10,node11,node12 = [Node(i) for i in ['Folder','Folder','Folder','.js','.txt','.txt']]
    # node1.left,node1.right,node3.left,node2.left,node2.right = node2,node3,node6,node4,node5
    tree1 = BinaryTree()
    tree1.root = node1
    node1.left = node2
    node1.right = node3
    
    node2.right = node5
    # node3.left = node6

    tree2 = BinaryTree()
    tree2.root = node7
    node7.left = node8
    node7.right = node9
    node8.left = node10
    node8.right = node11
    node9.left = node12

    tree1.compare_directory_structures(tree1,tree2)


    # tree = BinaryTree()
    # tree.root = node1
    # tree.root.display()
    # tree.Get_max()
    # breadth_first(tree)
    
    

    # tree2 = BinarySearchTree()
    # [tree2.Add(i) for i in [23,8,42,4,16,27]]
    # tree2.in_order()
    
    # search = BinarySearchTree()
    # search.root = node1
    # search.Add(24)
    # search.root.display()

    # search.Contains(23)

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


