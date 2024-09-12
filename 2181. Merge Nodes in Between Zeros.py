# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy  = ListNode()
        summ = dummy

        curr = head.next

        while curr:
      
            if curr.val != 0:
                s = 0
                while curr.val != 0:
                    s += curr.val
                    curr = curr.next
                summ.next = ListNode(s)
                summ = summ.next
                curr = curr.next
            else:
                curr = curr.next
        return dummy.next


            
        