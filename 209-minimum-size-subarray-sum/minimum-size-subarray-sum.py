class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if target in nums:
            return 1
        if sum(nums) < target:
            return 0
        l = 0
        r = 0
        min_size = float("inf")
        summ = 0
        while r < len(nums):
            summ = summ + nums[r]
            if summ < target:
                r += 1
            else:
                min_size = min(min_size,r - l + 1)
                summ -= nums[l]
                summ -= nums[r]
                if l == r:
                    r += 1
                else:
                    l += 1
                    
        return min_size

        