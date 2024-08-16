class Solution(object):
    def increasingTriplet(self, nums):
        # first_smallest = nums[0]
        # second_smallest = nums[1]
        # if first_smallest > second_smallest:
        #     first_smallest, second_smallest= second_smallest,first_smallest
        # for i in range(2,n):
            
        #     if nums[i] > first_smallest and nums[i] > second_smallest:
        #         return True
        #     elif nums[i] < second_smallest:
        #         second_smallest = nums[i]
        #     else:
        #         first_smallest= nums[i]
        # return False
        # for i in range(n):
        #     count = 0
        #     second_small = -1
        #     for j in range(i+1,n):
        #         if (nums[j] > nums[i]) and (nums[j] > second_small):
        #             count += 1
        #             second_small = nums[j]
        #     if count >= 2:
        #         return True
        # return False
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # Update the smallest number
            elif num <= second:
                second = num  
            else:
                # If we find a number greater than both `first` and `second`,
                return True
        
        return False