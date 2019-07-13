# https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current = head
        count = 0
        while (current != None):
            count = count + 1
            current = current.next
        if k == 0 :
          return head
        if (count == 0 or count == 1) :
          return head

        if k % count == 0:
            return head
        new_tail_position = count - (k % count)

        current = head
        for i in range(1,new_tail_position):
            current = current.next

        new_head = current.next
        current.next = None

        current = new_head
        while (current.next!=None):
            current = current.next

        current.next = head
        head = new_head

        return head

