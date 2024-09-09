class Solution(object):
    def productExceptSelf(self, nums):
        #brute force 
        # answer = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     answer.append(product)
        # return answer
        

        #o(n) 
        n = len(nums)
        output = [1] * n
        
        # Step 1: Calculate prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output