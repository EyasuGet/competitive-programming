# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        l = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                l = i + 1
                
                while l < len(nums) and nums[l] == 0:
                    l += 1
                if l < len(nums):

                    nums[i], nums[l] = nums[l], nums[i]
               
            i += 1
        return nums