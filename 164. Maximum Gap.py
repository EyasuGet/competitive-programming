class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        l, r = 0, 1
        m = 0
        while r < len(nums):
            m = max(m,nums[r]-nums[l])
            l += 1
            r += 1
        return m        