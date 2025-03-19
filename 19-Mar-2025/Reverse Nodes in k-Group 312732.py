# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        #find the length
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        dummy = ListNode(0,head)
        prev_end = dummy

        curr = head

        for i in range(length // k):
            p = None
            new_head = curr
            #reverse
            for _ in range(k):
                temp = curr.next
                curr.next = p
                p = curr
                curr = temp

            prev_end.next = p
            new_head.next = curr
            prev_end = new_head

        return dummy.next