# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        n = set(nums)
        while curr:
            if curr.val not in n:
                prev.next = curr
                curr = curr.next
                prev = prev.next
            else:
                curr = curr.next
        prev.next = None
        return dummy.next
        