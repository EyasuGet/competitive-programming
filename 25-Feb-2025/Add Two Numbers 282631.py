# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        c = dummy
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 and curr2:
            summ = curr1.val + curr2.val + carry
            carry = summ // 10
            dummy.next = ListNode(summ%10,None)
            dummy = dummy.next
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1:
            summ = curr1.val + carry
            carry = summ // 10
            dummy.next = ListNode(summ%10,None)
            dummy = dummy.next
            curr1 = curr1.next

        while curr2:
            summ = curr2.val + carry
            carry = summ // 10
            dummy.next = ListNode(summ%10,None)
            dummy = dummy.next
            curr2 = curr2.next
            
        if carry !=  0:
            dummy.next = ListNode(carry,None)
        return c.next

            