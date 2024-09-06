class Solution(object):
    def sortArrayByParity(self, nums):
        l = 0
        r = len(nums)-1
        while l < r:
            if nums[r] % 2 == 1:
                r -= 1
            elif nums[l] % 2 == 1:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            else:
                l += 1
        return nums
