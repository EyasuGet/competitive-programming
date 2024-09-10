# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math
class Solution(object):
    def insertGreatestCommonDivisors(self, head):

        def gc(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        nex = head.next
        while curr and nex:
            d = ListNode()
            d.val = gc(curr.val, nex.val)
            
            curr.next = d
            d.next = nex

            curr = curr.next.next
            nex = nex.next
        return head
        