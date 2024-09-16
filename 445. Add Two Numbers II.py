# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = ""
        curr = l1
        while curr:
            s1 += str(curr.val)
            curr = curr.next
        s2 = ""

        curr = l2
        while curr:
            s2 += str(curr.val)
            curr = curr.next
        
        s = str(int(s1) + int(s2))
        s = list(s)

        dummy = ListNode()
        curr = dummy
        for i in s:
            d = ListNode(i)
            dummy.next = d
            dummy = dummy.next
        return curr.next