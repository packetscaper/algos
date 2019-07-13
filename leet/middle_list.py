'''
https://leetcode.com/problems/middle-of-the-linked-list/

Use Cases
 count = 1
 count = 2
 count = even
 count = odd

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        
        while (1):
            
            if (fast.next == None):
              return slow
        
            if (fast.next.next == None):
                return slow.next
            
            slow = slow.next
            fast = fast.next.next
