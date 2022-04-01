from stack_and_queue.stack_queue import Stack, Node,Queue,PseudoQueue, AnimalShelter,Dog,Cat
import pytest


def test_stack_new_nodes(stack):
    assert stack.pop() == '3'
    assert stack.top.value == '2'
    assert stack.top.next.value == '1'


def test_stack_init():
    stack = Stack()
    assert stack.top == None

def test_stack_push_one(stack):
    stack = Stack()
    stack.push('1')
    actual = stack.top.value
    expected = "1"
    assert actual == expected

def test_stack_push_multi(stack):
    
    actual = stack.top.value
    expected = "3"
    assert actual == expected



def test_stack_pop(stack):
    actual = stack.pop()
    expected = "3"
    assert actual == expected
    
def test_stack_empty_stack_pops(stack):
    with pytest.raises(Exception):
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()

def test_stack_empty():
    with pytest.raises(Exception):
        stack = Stack()
        stack.pop()



def test_stack_peek_next(stack):
    actual = stack.peek()
    expected = "2"
    assert actual == expected
    
 

def test_stack_is_empty():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

#-------------------------------------------------

def test_enqueue(queue):
    queue = Queue()
    queue.enqueue('1')
    actual = queue.rear.value
    expected = '1'
    assert actual == expected

def test_enqueue_multi(queue):

    actual = queue.rear.value
    expected = '3'
    assert actual == expected

def test_dequeue(queue):

    actual = queue.dequeue()
    expected = '1'
    assert actual == expected

def test_dequeue_multi(queue):
    with pytest.raises(Exception):
# will empty the queue until it reaches none and raise an exception
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()

def test_queue():
    queue = Queue()

def test_dequeue_empty():
    with pytest.raises(Exception):
        queue = Queue()
        queue.dequeue()

def test_queue_peek(queue):
    actual = queue.peek()
    expected = '1'
    assert actual == expected
    
def test_queue_empty(queue):
    actual = queue.is_empty()
    expected = False
    assert actual == expected

    
#--------------------------------------------------------------

    
def test_pesudo_enqueue():
    pseudo = PseudoQueue()
    pseudo.enqueue('1')
    pseudo.enqueue('2')
    pseudo.enqueue('3')
    assert pseudo.peek() == '1'
    
   
def test_pesudo_dequeue():
    pseudo = PseudoQueue()
    [pseudo.enqueue(name) for name in ["1", "2", "3"]]    
    pseudo.dequeue() 
    assert pseudo.peek() == '2'

def test_pesudo_dequeue_empty():
    with pytest.raises(Exception):
        pseudo=PseudoQueue()  
        pseudo.dequeue()






# -------------------------------
#Animal Shelter Queue FIFO

def test_shelter_enqueue():
    animal = AnimalShelter()
    [animal.enqueue(i) for i in [Dog(),Cat(),Cat()]]
    assert str(animal.shelter.peek()) == 'dog'


def test_shelter_happy_path_dequeue():
    animal = AnimalShelter()
    [animal.enqueue(i) for i in [Dog(),Cat(),Cat()]]
    assert str(animal.dequeue('cat')) == 'cat'
    assert str(animal.shelter.peek()) == 'dog'


def test_shelter_fail_dequeue_empty():
    with pytest.raises(Exception):
        animal = AnimalShelter()
        assert animal.dequeue()

def test_shelter_stretch_dequeue():
    animal = AnimalShelter()
    [animal.enqueue(i) for i in [Dog(),Cat(),Cat()]]
    assert str(animal.dequeue('dog')) == 'dog'
    assert str(animal.dequeue('lizard')) == 'cat'






@pytest.fixture
def stack():
    stack = Stack()
    stack.push('1')
    stack.push('2')
    stack.push('3') 

    return stack


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue('1')
    queue.enqueue('2')
    queue.enqueue('3')  

    return queue











