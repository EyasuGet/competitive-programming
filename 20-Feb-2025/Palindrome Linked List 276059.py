# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head
        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
        #reverse the remaining list starting from slow
        
        curr = slow
        prev = None
        middle = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        p = head
        while p and prev:
            if p.val != prev.val:
                return False
            p = p.next
            prev = prev.next
        

        return True

