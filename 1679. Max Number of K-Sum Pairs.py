class Solution(object):
    def maxOperations(self, nums, k):
        n = len(nums)
        l = 0
        r = n - 1
        max_op = 0

        num = sorted(nums)

        while l < r:
            tot = num[l] + num[r]
            if tot == k:
                max_op += 1
                l += 1
                r -= 1
            elif tot < k:
                l += 1
            else:
                r -= 1
        return max_op 
        