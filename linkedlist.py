

class Node():

    def __init__(self,data=None,next_node=None):

        self.data = data
        self.next_node = next_node

    
    def get_data(self):
        return self.data



    def get_next(self):
        return self.next_node


    def set_next(self,new_next):
        self.next_node = new_next



class LinkedList():
    
    def __init__(self,head=None):
        self.head = head


    def insert_beginning(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_end(self,data):
        current = self.head
        while current.next_node != None:
            current = current.next_node

        new_node = Node(data)
        current.next_node = new_node


    def print_list(self):
       current = self.head
       while (current != None):
           print current.get_data()
           current = current.get_next()

   
    def reverse_list(self):
       new_head = self.head
       old_head = self.head.get_next()
       new_head.set_next(None) 
       current = old_head
       while current!= None :
           current = current.get_next() 
           old_head.set_next(new_head)
           new_head = old_head
           old_head = current

       self.head = new_head

           

        
