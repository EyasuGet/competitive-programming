class Solution(object):
    def findClosestNumber(self, nums):
        min_diff = 100000
        for i in nums:
            if abs(i) < min_diff:
                min_diff = abs(i)
            # if abs(i) == min_diff:
        if min_diff in nums:     
            return min_diff
        else:
            return min_diff * -1
        # min_diff_index = 0
        # for i in range(1,len(nums)):
        #     if abs(nums[i]) == abs(nums[min_diff_index]):
        #         min_diff_index = max(nums[i],nums[min_diff_index])

        #     if abs(nums[i]) < abs(nums[min_diff_index]):
        #         min_diff_index = i
            
        # return nums[min_diff_index]   
