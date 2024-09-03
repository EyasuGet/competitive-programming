class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        max_w = 0
        curr_zero = 0
        for r in range(len(nums)) :
            if nums[r] == 0:
                curr_zero += 1
            while curr_zero > k:
                if nums[l] == 0:
                    curr_zero -= 1
                l += 1
            
            max_w = max(max_w, r - l + 1)
        return max_w