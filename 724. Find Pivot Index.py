class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        # sum = 0
        # # if the pivot is at zero we check if all numbers to the right sum upto 0
        # for i in range(1,n):
        #     sum += nums[i]
        # if sum == 0:
        #     return 0
        # # for pivot greater than 0
        # l_sum = 0
        # r_sum = 0
        # pivot = 1
        # while pivot < n:
        #     l_sum = 0
        #     r_sum = 0
        #     for i in range(0,pivot):
        #         l_sum += nums[i]
        #     for j in range(pivot+1,n):
        #         r_sum += nums[j]
        #     if l_sum == r_sum:
        #         return pivot
        #     pivot += 1
        # return -1

        # l_sum = []
        # r_sum = []
        # def leftSum(pivot):
        #     return sum(nums[:pivot])
        #     # for i in range(0,pivot):
        #     #     sum += nums[i]
        #     # return sum

        # def rightSum(pivot):
        #     return sum(nums[pivot+1:])
        #     # for i in range(pivot+1,n):
        #     #     sum += nums[i]
        # l_sum = 0
        # r_sum = 0
        # for index in range(n):
        #     l_sum = leftSum(index)
        #     r_sum = rightSum(index)
        #     if l_sum == r_sum:
        #         return index
        # return -1
        total_sum = sum(nums)
        left_sum = 0
    
        for index, value in enumerate(nums):
            right_sum = total_sum - left_sum - value
            
            if left_sum == right_sum:
                return index
            
            left_sum += value

        return -1
        
        
