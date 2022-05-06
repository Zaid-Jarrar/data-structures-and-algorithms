    
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
    def __init__(self,value):
        self.value = value
        self.children = []

class KTree():
    def __init__(self):
        self.root = None
    # def breadth_first(self):
    #     if self.root is None:
    #         raise Exception('Tree is empty')
    #     current = self.root
    #     output = []
    #     queue = Queue()       
    #     queue.enqueue(current)
    #     while not queue.is_empty():
    #         print(queue.front.value.value + '    BEFORE DEQ')
    #         current = queue.dequeue()
    #         if queue.__sizeof__  :
    #             print(queue.__sizeof__())
    #             print('it is bigger')
    #         print(f'{current.value}     CURRENT VALUE')
    #         # print(queue.front.value.value + ' AFTER DEQ')
    #         output.append(current.value)
    #         for child in current.children:
    #             queue.enqueue(child)
    #     print(queue)
    #     print(output)
    #     return output
    def breadthFirst(self):
            '''
            A method to traverse the k-ary-tree elements (breadthFirst)
            input: None
            output: print a list of the value of each node
            '''
            current = self.root
            if current is None: return 'The tree is empty'
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

            

            


if __name__ == '__main__':

    node1,node2,node3,node4,node5,node6 = [KNode(i) for i in ['A','B','C','D','E','F']]
    node1.children = [node2,node3]
    node2.children = [node4,node5]
    node3.children = [node6]
    tree = KTree()
    tree.root = node1
    tree.breadthFirst()

    tree.add_child('G',node1)
    tree.breadthFirst()


    # ktree = KTree()
    # ktree.add_child(node1)
    # # ktree.root.children.append = Node(1), Node(2)
    # lvl1 = Node(1)
    # lvl2 = Node(2)
    # ktree.add_child(2)
    # ktree.add_child(3)
    # print(ktree.queue)
    
    