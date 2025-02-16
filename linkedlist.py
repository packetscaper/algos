

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
    
    def __init__(self,array=None,head=None):
        self.head = head
        if array != None:
            for i in array:
                self.insert_end(i)


    def insert_beginning(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_end(self,data):
        new_node = Node(data) 
        current = self.head
        if self.head == None :
          self.head = new_node
        
        else :
         while (current.get_next() != None ):
            current = current.get_next()
         current.set_next(new_node)

    def print_list(self):
       current = self.head
       list = 'head--->' 
       while (current != None):
           list = list+ str(current.get_data()) + '--->'
           current = current.get_next()
      
       print list + 'null'
   
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

           
    def get_count(self):
        current = self.head
        count = 0
        while (current != None):
          count = count + 1
          current = current.get_next()
        return count 



    def get_nth_from_last(self,n):
        slow = self.head
        fast = self.head
        for i in range(1,n):
            fast = fast.get_next()
        while (fast.get_next()!=None):
            fast = fast.get_next()
            slow = slow.get_next()

        return slow.get_data()
        
