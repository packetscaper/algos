# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''

The idea is to traverse the even nodes and keep splitting the list
Stich the lists towards the end.

Use Cases

1. Null
2. Even
3. Odd

'''

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        
        if head == None:
            return head
       
        even = even_head = head.next 
        while (even != None and even.next != None):
         
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = even_head 
       
        return head
          
