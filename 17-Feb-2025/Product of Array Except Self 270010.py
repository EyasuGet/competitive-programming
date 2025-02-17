# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 1 , 2, 2, 6
        # 24 12 4 1
                 

        prod = 1
        prefix_prod = [1] * len(nums)
        for i in range(1,len(nums)):
            prefix_prod[i] = (prod * nums[i-1])
            prod *= nums[i-1]
        
        suffix_prod = [1] * len(nums)
        prod2 = 1
        for i in range(len(nums)-2, -1, -1):
            suffix_prod[i] = nums[i+1] * prod2
            prod2 *= nums[i+1]
        
        for i in range(len(suffix_prod)):
            suffix_prod[i] *= prefix_prod[i]
        
        return suffix_prod

