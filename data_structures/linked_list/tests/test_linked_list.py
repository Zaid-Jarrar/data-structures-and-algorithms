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




# @pytest.fixture
# def link():
#   add_at_beginning = Linked_list()
#   add_at_beginning.insert(Node('Jarrar'))
#   add_at_beginning.insert(Node('Zaid'))
#   print(add_at_beginning.__str__)
#   return add_at_beginning



 



