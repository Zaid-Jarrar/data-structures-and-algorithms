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
insert_after: add a node after a given node to the linked list
insert_before: add a node before a given node to the linked list
get_kth_value: takes in an integer as an argument and returns value of that starting from the end of linked list


    '''

    def __init__(self):
        self.head = None


    def insert(self, new_node):
        if new_node == '':
            raise TypeError('Node must not be empty')
        else:
            new_node.next = self.head
            self.head = new_node

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


    def insert_after(self,previous_node,added_data):
        
        if added_data == '':
            raise TypeError('added data must not be empty')
        elif previous_node is None:
            raise TypeError('Previous Node must not be empty')
        else:
            current = self.head
            while current is not None:
                if current.value == previous_node:
                    added_node = Node(added_data)
                    added_node.next = current.next
                    current.next =  added_node
                current = current.next


    # def insert_before(self,next_node, added_data):
    def insert_before(self,value, new_value):
        if self.head is None:
            return "empty linked list"

        if not isinstance(value, Node):
            value= Node(value)
        if not isinstance(new_value, Node):
            new_value= Node(new_value)

        current = self.head

        if current.value == value.value:
            new_value.next = current
            self.head = new_value

        else:
            while current is not None:
                if current.next.value == value.value:
                    new_value.next = current.next
                    current.next = new_value
                    return
                current = current.next


#---------------------------------------------
# get the kth value of the linked list in reverse where 0 will output the last node in the list

    def kth_from_end(self,k):

        length = 0
        if k >= 0:
            current = self.head

            #while to calculate the length of the linked lists
            while current is not None:
                length += 1
                current = current.next
                
            # index less than 0
        elif k < 0:
            raise Exception ("Inputted number must be positive")

        if length > k:
            # bigger 
            current = self.head
            # k+1 so we get the last one before Null
            for __ in range(length - (k+1)):
                current = current.next
            current = current.value
            print(current)
        else:
            raise Exception ('Index is out of range')
        
        return current
        
#--------------------------------------------------------------------------

    # zip (connect) 2 linked lists into one linked list amongst them 
    def zip_linked_lists(self, ll1,ll2):

            ''' 
            zip linked lists takes in 2 linked lists as arguments 
            and zips the two linked lists in one of them 
            and returns the head of the the zipped linked list
            '''
            
            if ll1.head is None and ll2.head is None:
                raise Exception ('inputted linked lists must not be empty')
            
            else:    
                ll1_current = ll1.head
                ll2_current = ll2.head

                # swap their positions until one finishes off
                while ll1_current  and ll2_current:

                    # Save next pointers
                    
                    ll1_next = ll1_current.next
                    ll2_next = ll2_current.next

                    # linking between the 2 lists nodes
                    ll2_current.next = ll1_next
                    ll1_current.next = ll2_current

                    # update current pointers for next iteration

                    ll1_current = ll1_next
                    ll2_current = ll2_next
                    ll2.head = ll2_current

                # Add the ll2.head or the remaining ll2 nodes at the end of ll1 in case ll1 was shorter than ll2 
                ll1.append(ll2_current)
                
            return ll1.head.value


    def is_plindrome(self):
        string = ""
        current = self.head
        while current:
            string += current.value
            current = current.next
        if string == string[::-1]:
            print(True)
            return True
        else:
            print(False)
            return False

    def reversedI(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev



if __name__ == "__main__":


    pass
    ll = Linked_list()
    # one = Node("Zaid")
    # zaid = Node("Am")
    # Jarrar = Node("Jarrar")

    ll.append(Node('R'))
    ll.append(Node('A'))
    ll.append(Node('D'))
    ll.append(Node('A'))
    ll.append(Node('R'))
    ll.is_plindrome()
    print(ll)
    

    # ll.append(one)
    # ll.insert(zaid)
    # # ll.insert(Node('I'))
    # ll.append(Jarrar)
    # ll.insert(Node('three'))
    # ll.insert(Node('two'))
    # ll.insert(Node('one'))

# both empty and either is empty and one has one node and the 

    # ll.kth_from_end(0)
    # print(ll)

    ll2 = Linked_list()
    first = Node("1")  
    second = Node("2")
    third = Node("3")
    forth = Node("4")
    five = Node("5")

    ll2.append(first)
    ll2.append(second)
    ll2.append(third)
    ll2.append(forth)
    ll2.append(five)
    ll2.reversedI()
    print(ll2)

    
    # ll2.append(forth)
    # ll2.append(five)
    

    # print(ll2)

    # ll.merge(ll,ll2)
    # ll.zip_linked_lists(ll,ll2)
    print(ll)
    # print(ll2)

    
    
    # ll.insert_after('Zaid', 'new')
  

 
    
   
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