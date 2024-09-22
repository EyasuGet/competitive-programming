class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        c = 0
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if i < j and nums[i] + nums[j] < target:
                    c += 1
        return c
        #o(n^2)
        #o(1)


        nums.sort()
        l = 0
        r = n - 1
        ans = 0
        while l < r:
            if nums[l] + nums[r] < target:
                ans += r - l
                l += 1
            else:
                r -= 1
        return ans
