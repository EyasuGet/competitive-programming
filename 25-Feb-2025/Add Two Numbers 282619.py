# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = l1
        arr1 = ""

        while curr:
            arr1 += str(curr.val)
            curr = curr.next
        
        curr2 = l2
        arr2 = ""
        while curr2:
            arr2 += str(curr2.val)
            curr2 = curr2.next
        
        ans = int("".join(list(reversed(arr1)))) + int("".join(list(reversed(arr2))))
        dummy = ListNode(0)
        if ans == 0:
            return dummy
        c = dummy
        place = 0

        while ans>0:
            d = ans % 10
            dummy.next = ListNode(d,None)
            dummy = dummy.next
            ans //= 10
        return c.next
            
        

