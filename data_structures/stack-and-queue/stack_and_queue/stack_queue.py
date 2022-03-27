
class Node:
    """  
     Node class takes in an argument value and creates a new node 
    """
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack():
    """ 

    Stack class has the following methods:

    push: takes in an argument value and pushes a node of that value into the stack which makes the top equal to that node
    pop: takes no arguments and returns the value of the removed node from the top, if stack is empty an exception will be raised
    peek: takes no arguments and returns the value of the top node or the next of the top if exists, if stack is empty an exception will be raised
    is_empty: takes no arguments and returns True if stack is empty, False otherwise

    """
    def __init__(self,node = None):
        self.top = node


    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node
        

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")

        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None 
            return temp.value

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        elif self.top.next:
            return self.top.next.value
        else:   
            return self.top.value     



    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def __str__(self):
        output = ''
        if self.is_empty():
            return 'The stack is empty'
        else:
            current = self.top
            while current is not None:
                if current.next is None:
                    output += '{ ' f'{current.value}' ' }'
                    break
                else:
                    output += '{ ' f'{current.value}' ' } -> '
                    current = current.next
        return  output 


class Queue:
    """ 

    Queue class has the following methods:

    enqueue: takes in an argument value and pushes a node of that value into the queue which makes the rear equal to that node or if empty rear and front will equal to that node
    dequeue: takes no arguments and returns the value of the removed node from the front, if queue is empty an exception will be raised
    peek: takes no arguments and returns the value of the front node, if queue is empty an exception will be raised
    is_empty: takes no arguments and returns True if queue is empty, False otherwise
    """
    def __init__(self,node = None):
        self.front = node
        self.rear = node

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
            raise Exception('queue is empty')
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.is_empty == True:
            raise Exception ('queue is empty')
        else:
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False


class PseudoQueue:

    """  
    This PseudoQueue class will implement our standard queue interface (the two methods listed below),
    Internally, utilize 2 Stack instances to create and manage the queue

    enqueue method:  Inserts value into the PseudoQueue, using a first-in, first-out approach.
    dequeue method:  Extracts a value from the PseudoQueue, using a first-in first-out approach.

    """

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()


    def enqueue(self,value):
        """ 
        Inserts value into the PseudoQueue, using a first-in, first-out approach.
        """
        
        self.stack1.push(value)

    def dequeue(self):
        """
        Extracts a value from the PseudoQueue, using a first-in first-out approach.
        """
        
        if not self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        if not self.stack1.is_empty():
            return self.stack1.pop()
        else:
            raise(Exception("Pseudo queue is empty !"))



if __name__ == '__main__':
    stack = Stack()
    stack.push('zaid')
    stack.push('Jarrar')

    stack.peek()

    queue = PseudoQueue()
    queue.enqueue('Zaid')
    queue.enqueue('Jarrar')

    # queue.enqueue('Jarrar')
    print(queue)
    # print(stack)
#    def enqueue(self,value):
        
 
    # self.stack1.push(value)

    # if self.front is None:
    #     self.stack1.push(value)
    #     self.front = self.stack1.top
    #     self.rear = self.stack1.top
    # else:
    #     node = self.stack1.push(value)
    #     self.rear.next = node
    #     self.rear = node
    # return self.stack1.peek(

    # def __str__(self):
    #     output = ''
    #     if not self.front:
    #         return 'The stack is empty'
    #     else:
    #         current = self.front
    #         while current:
    #             if current.next is None:
    #                 output += f'{current.value}'
    #                 return output
    #             else:
    #                 output += f'{current.value} -> '
    #                 current = current.next
    #     return  output 