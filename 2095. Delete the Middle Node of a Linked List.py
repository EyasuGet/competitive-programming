# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        dummy = ListNode()
        prev = dummy
        curr = head
        while curr:
            if curr != slow:
                prev.next =  curr
                prev = prev.next
                curr = curr.next
            else:
                curr = curr.next
        prev.next = None
        return dummy.next

