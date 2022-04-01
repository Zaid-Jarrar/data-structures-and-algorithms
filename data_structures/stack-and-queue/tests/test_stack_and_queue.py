from stack_and_queue.stack_queue import Stack, Node,Queue,PseudoQueue
import pytest


def test_stack_():
    stack = Stack()

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











