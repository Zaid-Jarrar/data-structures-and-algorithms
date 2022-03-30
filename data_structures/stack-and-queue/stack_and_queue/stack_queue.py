

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

    def __str__(self):
        output = ''
        if not self.front:
            return 'The queue is empty'
        else:
            current = self.front
            while current:
                output += f'{current.value} --> '
                current = current.next
            output += 'Null'
            return output


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
        self.front = None
        self.rear = None


    def enqueue(self,value):
        """ 
        Inserts value into the PseudoQueue, using a first-in, first-out approach.
        """
        self.top = Node(value)
        self.stack1.push(value)
        

        # self.stack1.push(value)
        # while not self.stack1.is_empty():
        #     self.stack2.push(self.stack1.pop())
        # return self.stack2



    def dequeue(self):
        """
        Extracts a value from the PseudoQueue, using a first-in first-out approach.
        """
        if not self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
            val = self.stack2.pop()
            elt = None
            while not self.stack2.is_empty():    
                elt = self.stack2.pop()
                self.stack1.push(elt)
                self.top = elt
            return val

        # if not self.stack1.is_empty():
        #     return self.stack1.pop()
        # else:
        #     raise(Exception("Pseudo queue is empty !"))


    def __str__(self):
        output = ''
        if not self.top:
            return 'The stack is empty'
        else:
            current = self.top
            while current:
                output += f'{current.value} -->'
                current = current.next
            output += 'Null'
            return output
                
                    
#--------------------------------------------------------------------



class Dog():
    def __init__(self):
        self.animal_type = 'dog'
           
    
    def __str__(self):
        return f'{self.animal_type}'


class Cat():
    def __init__(self):
        self.animal_type = 'cat'
            

    def __str__(self):
        return f'{self.animal_type}'

   

          

class AnimalShelter:
    """
        AnimalShelter which holds only dogs and cats.
        The shelter operates using a first-in, first-out approach.
        Implementing the following methods

        enqueue method takes in one argument that inserts an animal object into the queue 
        dequeue method takes in one optional argument that retrieves  the animal the user inputs if it exists.
        if it doesnt it will return the longest stayed animal

    """


    def __init__(self):
        self.shelter = Queue()
        self.dog = Dog()
        self.cat = Cat()
        

    def __str__(self):
        return f'{self.shelter}'

    def enqueue(self,animal):
        """
        enqueue method takes in one argument that inserts an animal object into the queue 
        """
        if not isinstance(animal,Dog) and not isinstance(animal,Cat):
            raise Exception ('animal must be either a Cat or a Dog object')
        else:
            self.shelter.enqueue(animal)




    def dequeue(self,pref='lizard'):
        """
        dequeue method takes in one optional argument that retrieves  the animal the user inputs if it exists.
        if it doesnt it will return the longest stayed animal
        """

        if pref != 'cat' and pref != 'dog':

            if not self.shelter.is_empty():
                return self.shelter.dequeue()
            else:
                raise Exception ('Animal Shelter is empty')

         
        # while is used to loop over the queue if the counter is less than the length of the queue
        #checks if the string of the peek is equal to the preferred animal string
        counter = 0   
        while (counter < (self.shelter).__sizeof__()):

            if str(self.shelter.peek()) == pref:

                return self.shelter.dequeue()

            else:
                self.shelter.enqueue(self.shelter.dequeue())
            counter +=1

        if self.shelter.is_empty():
            raise Exception ('Animal Shelter is empty') 
       
        else:
            raise Exception (f'Animal Shelter does not have {pref}') 



if __name__ == '__main__':


    animal = AnimalShelter()
    # [animal.enqueue(i) for i in [Dog(),Cat(),Cat()]]
    animal.enqueue(Dog())

    animal.enqueue(Cat())
    animal.enqueue(Cat())
    animal.enqueue(Dog())
    animal.enqueue(Cat())

    print(animal)
    
    # print(animal.shelter.peek())
  
    print(animal.dequeue('dog'))
    # print(animal.dequeue('dog'))
    print(animal)
    # stack = Stack()
    # stack.push('zaid')
    # stack.push('Jarrar')
    # stack.peek()

    # queue = PseudoQueue()
    # queue.enqueue('1')
    # queue.enqueue('2')
    # queue.enqueue('3')
    # queue.enqueue('4')

    # print(queue)


    



    # print(animal.dequeue('cat'))


    # null<-1<- 2 <-3 <- top
    # empty stack1 3 - 2 - 1
    # insert into a second stack null 3<-  2 <- 1 top 
    # pop second stack 1 2 3 --- returned


    # print(queue.enqueue('Jarrar'))

    # queue.enqueue('Jarrar')
   
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