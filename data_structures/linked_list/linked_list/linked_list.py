from abc import ABC


class Node:
    '''

A Class that takes in one argument(value) and creates a node

    '''
    def __init__(self,value):
        self.value = value
        self.next = None


class Linked_list:
    

    '''

A Linked list Class that has the following methods:

insert: add a node at the beginning 
append: add a node at the end 
includes: searches if the value exists in the linkned list or not and returns a boolean
to string: calls a __str__ method to represent the objects
__Str__: returns a string representation of the objects


    '''

    def __init__(self):
        self.head = None


    def insert(self, new_node):
        if new_node == '':
            raise TypeError('Node must not be empty')
        else:
            new_node.next = self.head
            self.head = new_node


    def append(self,added_node):
        if added_node == '':
            raise TypeError('Node must not be empty')
        else:
            
            if self.head is None:
                self.head = added_node
            
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = added_node


    def includes(self,value):
        if value is None:
            raise TypeError('value must not be None')
        else:    
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False


    def to_string(self):
        return self.__str__()

        
    def __str__(self):
        values = ""
        if self.head is None:
            values = "Linked list is empty"
        else:
            current = self.head
            while (current):
                values += f'{current.value} ->'
                current = current.next
            values += "NULL"
            
        return values
            

    

if __name__ == "__main__":

    pass
    ll = Linked_list()
    one = Node("1")
    zaid = Node("Zaid")
    Jarrar = Node("Jarrar")
    ll.append(one)
    ll.insert(zaid)
    ll.insert(Node('zaid'))
   
    ll.append(Jarrar)
    print(ll)

    # linked = Linked_list()
    # linked.head = (Node('Jarrar'))
    # linked.insert('Zaid')
    # print(linked)

    # list1.append(Node('adasd'))

    # list1.append('asdasd')

    # list1.append('apend')

  
    # list1.insert('here')
    # list1.insert('now')
    # list1.insert('5')
    # list1.append('end')

    # list1 = Linked_list()
    
    # list1.head.next = Node('jarrar')
    # list1.to_string()



    # print(list1.includes('zaid'))
    # print(list1.includes('dsdasdasd'))
    # print(list1.includes('asdasd'))


# def to_string(self): 
    #     node = self.head 
    #     while (node): 
    #         print (node.value, " -> ", end = '') 
    #         node = node.next
    #     print("")
   
    # def insert(self,value):
    #     if value == '':
    #         raise TypeError('value must not be empty')
    #     else:    
    #         node = Node(value)
    #         if self.head is not None:
    #             current = self.head
    #             while current.next is not None:
    #                 current = current.next
    #             current.next = node
    #         else:
    #             self.head = node