class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
        #another soln
        # if len(nums) == 1 and nums[0] == val:
        #     return 0
        # l = 0
        # k = 0
        # r = len(nums) - 1
        # while l <= r:
        #     if nums[r] == val:
        #         k += 1
        #         nums[r] = "_"
        #         r -= 1
        #     elif nums[l] == val:
        #         k += 1
        #         nums[l] = "_"
        #         nums[l],nums[r] = nums[r],nums[l]
        #         l += 1
        #         r -= 1
        #     else: 
        #         l += 1
    
        # return len(nums) - k
        
        