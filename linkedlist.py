

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




        
