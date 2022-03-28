# Stacks and Queues
<!-- Short summary or background information -->
A Stack is a data structure that follows the LIFO(Last In First Out) principle or FILO (First In Last Out)
which has a top pointer

A Queue follows the First-in-First-Out (FIFO) principle, or the LILO (Last in Last Out) principle
and has two pointers one is for the front of the queue ie the dequeue and one for the rear of the queue
ie the enqueue

## Challenge
<!-- Description of the challenge -->
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
The class should contain the following methods:
- push
- pop
- peek
- is empty

- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
The class should contain the following methods:
- enqueue
- dequeue
- peek
- is empty

- Create PseudoQueue class that will implement our standard queue interface (the two methods listed below),
Internally, utilize 2 Stack instances to create and manage the queue
- enqueue method
- dequeue method


## whiteboards
![PseudoQueue](assets/PseudoQueue.jpg)
  


## Approach & Efficiency
Big O here is O(1) for both time and space since it is only done on one node at a time hence the O(1) of time. 
and for the space there is no loops or anythong to increase it, so it is a linear relationship so O(1)


## API
<!-- Description of each method publicly available to your Stack and Queue-->

    Node class takes in an argument value and creates a new node 

    Stack class has the following methods:
    push: takes in an argument value and pushes a node of that value into the stack which makes the top equal to that node
    pop: takes no arguments and returns the value of the removed node from the top, if stack is empty an exception will be raised
    peek: takes no arguments and returns the value of the top node or the next of the top if exists, if stack is empty an exception will be raised
    is_empty: takes no arguments and returns True if stack is empty, False otherwise

    Queue class has the following methods:
    enqueue: takes in an argument value and pushes a node of that value into the queue which makes the rear equal to that node or if empty rear and front will equal to that node
    dequeue: takes no arguments and returns the value of the removed node from the front, if queue is empty an exception will be raised
    peek: takes no arguments and returns the value of the front node, if queue is empty an exception will be raised
    is_empty: takes no arguments and returns True if queue is empty, False otherwise

    PseudoQueue class will implement our standard queue interface (the two methods listed below),
    Internally, utilize 2 Stack instances to create and manage the queue
    enqueue method:  Inserts value into the PseudoQueue, using a first-in, first-out approach.
    dequeue method:  Extracts a value from the PseudoQueue, using a first-in first-out approach.