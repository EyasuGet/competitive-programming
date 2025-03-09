# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #slow = middle element

        #lets start reversing starting from middle
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        start = head
        max_sum = 0
        while start != slow:
            max_sum = max(max_sum, start.val + prev.val)
            start = start.next
            prev = prev.next
        return max_sum
