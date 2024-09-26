class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        s = set()
        l = 0
        r = n - 1
        while l <= r:
            av = (nums[l] + nums[r]) / 2.0
            s.add(av)
            l += 1
            r -= 1
        return len(s)