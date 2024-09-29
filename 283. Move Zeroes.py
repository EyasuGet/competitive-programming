class Solution(object):
    def moveZeroes(self, nums):

        l = 0
        n = len(nums)
        for i in range(n):
            if nums[i]:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1