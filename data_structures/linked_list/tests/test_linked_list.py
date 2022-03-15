from linked_list.linked_list import Linked_list, Node
import pytest




def test_Linked_list_is_empty(): 
    list1 = Linked_list()
    expected = None
    actual = list1.head
    assert actual == expected   


def test_insert():
  
  add_at_beginning = Linked_list()
  add_at_beginning.insert(Node('Jarrar'))
  add_at_beginning.insert(Node('Zaid'))

  expected = 'Zaid ->Jarrar ->NULL'
  actual = add_at_beginning.to_string()
  assert expected == actual


def test_to_string():
  log = Linked_list()
  log.append(Node(100))
  log.insert(Node('PASS'))
  
  actual = log.to_string()
  expected = 'PASS ->100 ->NULL'
  assert actual == expected



def test_for_includes():
  fav_list = Linked_list()
  fav_list.append(Node(True))
  fav_list.append(Node('ASAC'))
  fav_list.insert(Node('TA'))
  fav_list.insert(Node('YB'))


  assert fav_list.includes(True) == True
  assert fav_list.includes('ASAC') == True
  assert fav_list.includes('TA') == True
  assert fav_list.includes('BY') == False


def test_list_None():
  actual = Linked_list()
  assert actual.head == None



def test_insert_After_middle():
  add = Linked_list()
  add.insert(Node('Cool'))
  add.insert(Node('Is'))
  add.insert(Node('Zaid'))
  add.insert_after('Is', 'Jarrar')

  expected = 'Zaid ->Is ->Jarrar ->Cool ->NULL'
  actual = add.to_string()
  assert expected == actual


def test_insert_After_last():
  add = Linked_list()
  add.insert(Node('Cool'))
  add.insert(Node('Is'))
  add.insert(Node('Zaid'))
  add.insert_after('Cool', 'Jarrar')

  expected = 'Zaid ->Is ->Cool ->Jarrar ->NULL'
  actual = add.to_string()
  assert expected == actual

def test_insert_before_middle():
  add_at_beginning = Linked_list()
  add_at_beginning.insert(Node('Zaid'))
  add_at_beginning.insert(Node('Am'))
  add_at_beginning.insert_before('Zaid', 'I')

  expected = 'Am ->I ->Zaid ->NULL'
  actual = add_at_beginning.to_string()
  assert expected == actual  



def test_insert_before_first():
  add_at_beginning = Linked_list()
  add_at_beginning.insert(Node('Zaid'))
  add_at_beginning.insert(Node('Am'))
  add_at_beginning.insert_before('Am', 'I')

  expected = 'I ->Am ->Zaid ->NULL'
  actual = add_at_beginning.to_string()
  assert expected == actual  


def test_append_node():
  fav_list = Linked_list()
  fav_list.append(Node(True))
  actual = fav_list.to_string()

  assert   'True ->NULL' == actual

def test_append_nodes():
  fav_list = Linked_list()
  fav_list.append(Node(True))
  fav_list.append(Node('ASAC'))
  actual = fav_list.to_string()

  assert   'True ->ASAC ->NULL' == actual


# -----------------------------------------------
# get kth value from a linked list

def test_k_greater_than_length():
  with pytest.raises(Exception):
    add = Linked_list()
    add.insert(Node('Cool'))
    add.insert(Node('Is'))
    add.insert(Node('Zaid'))
    add.kth_from_end(4)  


def test_k_equals_the_length():
  with pytest.raises(Exception):
    add = Linked_list()
    add.insert(Node('Cool'))
    add.insert(Node('Is'))
    add.insert(Node('Zaid'))
    add.kth_from_end(3) 


def test_k_is_not_Positive():
  with pytest.raises(Exception):
    add = Linked_list()
    add.insert(Node('Cool'))
    add.insert(Node('Is'))
    add.insert(Node('Zaid'))
    add.kth_from_end(-1)

def test_linked_list_is_one():
  add = Linked_list()
  add.insert(Node('Zaid'))
  add.kth_from_end(0)
  assert 'Zaid' == add.kth_from_end(0)

def test_k__in_middle():

  add = Linked_list()
  add.insert(Node('Cool'))
  add.insert(Node('Is'))
  add.insert(Node('Zaid'))
  assert add.kth_from_end(1) == 'Is' 


# @pytest.fixture
# def link():
#   add_at_beginning = Linked_list()
#   add_at_beginning.insert(Node('Jarrar'))
#   add_at_beginning.insert(Node('Zaid'))
#   print(add_at_beginning.__str__)
#   return add_at_beginning



 



