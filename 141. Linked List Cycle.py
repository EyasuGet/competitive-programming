# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        curr = head
        #if we ever get the pointer at the end it means there is no cycle
        #if the reference is in the set we will return true
        # s = set()

        # while curr:
        #     if curr.next in s:
        #         return True
        #     else:
        #         s.add(curr.next)
        #     curr = curr.next
        # return False

        #tc o(n)
        #sc o(n)

        #we can use slow and fast pointers to minimizze the space complexity

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True
        return False