# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthan = ListNode(0)
        l = lessthan

        greater = ListNode(0)
        g = greater

        curr = head
        while curr:
            if curr.val < x:
                lessthan.next = curr
                lessthan = lessthan.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next 
        greater.next = None
        lessthan.next = g.next
        return l.next