# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # dummy = ListNode(0, )
        prev = head
        curr = None

        while prev:
            temp = prev.next
            prev.next = curr
            curr = prev
            prev = temp
        return curr