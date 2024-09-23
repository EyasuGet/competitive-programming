class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        l = 0
        r = len(nums)-1
        ans = float("inf")
        while l < r:
            av = float(nums[l] + nums[r]) / 2
            ans = min(av,ans)
            l += 1
            r -= 1
        return ans

        