import copy
from tree.trees import BinaryTree,Node

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        node = Node(value)
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
        '''
    A method to print the queue
    Input: nothing
    Output: string
        '''
        output = ''
        if self.is_empty():
            return 'The queue is empty'
        else:
            current = self.front
            while current is not None:
                output += '{ ' f'{current.value}' ' } -> '
                current = current.next
            output += 'Null'
        return  output


class KNode:
    """
    Create a node that takes value as argument and can have many children for the k-arytree

    """
    def __init__(self,value):
        self.value = value
        self.children = []

class KTree():
    def __init__(self):
        self.root = None

    def breadthFirst(self):
            '''
            A method to traverse the k-ary-tree elements (breadthFirst)
            input: None
            output: print a list of the value of each node
            '''
            current = self.root
            if current is None: 
                return 'The tree is empty'
            values = []
            queue = Queue()
            queue.enqueue(current)
            while not queue.is_empty():
                current = queue.dequeue()
                values.append(current.value)
                for child in current.children:
                    queue.enqueue(child)
            print(values)
            return values
    def add_child(self,value,parent):
        '''
        A method to add a child to a parent node
        input: value, parent
        output: None
        '''
        if type(parent) != KNode:
            raise Exception('Parent is not a KNode')

        node = KNode(value)
        parent.children.append(node)

        return node





def tree_fizz_buzz(k_arytree):

    """
    a function that takes in a k-ary tree and returns a new k-ary tree with the following rules:
    1. if the value of the node is divisible by 3, replace the value with "Fizz"
    2. if the value of the node is divisible by 5, replace the value with "Buzz"
    3. if the value of the node is divisible by 3 and 5, replace the value with "FizzBuzz"
    4. otherwise, leave the value as is but as a string

    input: k-ary tree
    return: new k-ary tree

    """
    # result = []
    modified_k_arytree = KTree()
    
    if k_arytree.root is None:
        return 'The tree is empty'
    
    def _walk(current,parent =None):
        if type(current.value) is not int:
            raise Exception('Current nodes values must be integers') 

        if current.value % 3 == 0 and current.value % 5 == 0:
            output = 'FizzBuzz'

        elif current.value % 3 == 0:
            output = 'Fizz'
        elif current.value % 5 == 0:
            output = 'Buzz'
        else:
            output = str(current.value)
        
            
        node = KNode(output)
        if parent is not None:
            parent.children.append(node)

        if current.children:
            for child in current.children:
                _walk(child,node)     
        
        if parent is None:
            return node

    modified_k_arytree.root= _walk(k_arytree.root)

    print(modified_k_arytree.root.children[0].value)
    # just for viewing purposes
    # queue = Queue()
    # queue.enqueue(modified_k_arytree.root)
    # while not queue.is_empty():
    #     current = queue.dequeue()
    #     result.append(current.value)
    #     for child in current.children:
    #         queue.enqueue(child)
    # print(result)
    # #-----------------------------
    return modified_k_arytree

    

if __name__ == '__main__':
    node1,node2,node3,node4,node5,node6 = [KNode(i) for i in [3,5,6,9,15,2]]
    # node1,node2,node3,node4,node5,node6 = [KNode(i) for i in ['3','5','6','9','15','2']]

    node1.children = [node2,node3]
    node2.children = [node4,node5]
    node3.children = [node6]
    tree = KTree()
    tree.root = node1
    tree.breadthFirst()
    tree_fizz_buzz(tree)



    # ktree = KTree()
    # ktree.add_child(node1)
    # # ktree.root.children.append = Node(1), Node(2)
    # lvl1 = Node(1)
    # lvl2 = Node(2)
    # ktree.add_child(2)
    # ktree.add_child(3)
    # print(ktree.queue)
    

    # --------------------------------------------------------
    # def __str__(self):
    #     '''
    #     A method to print the k-ary-tree
    #     input: None
    #     output: string
    #     '''
    #     output = ''
    #     if self.root is None:
    #         return 'The tree is empty'
    #     else:
    #         current = self.root
    #         while current is not None:
    #             output += '{ ' f'{current.value}' ' } -> '
    #             for child in current.children:
    #                 output += '{ ' f'{child.value}' ' } -> '
    #                 print(current.children[0].value)
    #             current = current.children[0]
    #         output += 'Null'
    #     return output


    # def add_child(self,value):
    #     if self.root is None:
    #         self.root = Node(value)
    #         self.queue.enqueue(self.root)        
    #     else:
    #         self.queue.enqueue(self.root)
    #     while not self.queue.is_empty():
    #         current = self.queue.dequeue()
    #         if current.children is not None:
    #             current.children.append(Node(value))
    #             self.queue.enqueue(current.children[-1])
    #             print(self.queue)
    #             # self.queue.enqueue(current.children[-1])
# def tree_fizz_buzz(k_arytree):

#     if k_arytree.root is None:
#         raise Exception ("Tree is empty")

#     # modified_k_arytree =  k_arytree.breadthFirst()
#     modified_k_arytree = KTree()
#     modified_k_arytree.root = copy.deepcopy(k_arytree.root)
#     output = []
#     queue = Queue()
#     queue.enqueue(modified_k_arytree.root)
#     # queue.enqueue(k_arytree.root)
#     while not queue.is_empty():
#         current = queue.dequeue()

#         if current.value % 3 == 0 and current.value % 5 == 0:
            
            

#             current.value = "FizzBuzz"

#         elif current.value % 3 == 0:
#             current.value = "Fizz"
#         elif current.value % 5 == 0:
#             current.value = "Buzz"
#         else:
#             current.value = str(current.value)
#         output.append(current.value)
#         for child in current.children:
#             queue.enqueue(child)
#     print(output)

#     k_arytree.breadthFirst()
#     modified_k_arytree.breadthFirst()
    

#     return modified_k_arytree
