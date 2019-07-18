# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''

Use Case 


Null
1 item

even items
odd items

1-->2--->3---->4

after first iteration

2---1--->4<-------3 
temp = 3


'''


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None :
            return head
        current = head 
        head = head.next
        temp = ListNode(0)
        while (1):
            temp = current.next.next
            current.next.next = current
            if (temp == None or temp.next == None):
                current.next = temp 
                break
            current.next = temp.next 
            current = temp 
            
        return head
