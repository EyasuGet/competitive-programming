# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cycle = False
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                cycle = True
                break
        if not cycle:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

        
        