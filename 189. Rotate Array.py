class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #to handle cases where k is larger than the length
        k = k % len(nums)
        
        nums.reverse()
        l = 0
        r = k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        second_l = k
        last = len(nums)-1
        while second_l < last:
            nums[second_l], nums[last] = nums[last], nums[second_l]
            second_l += 1
            last -= 1
        # although we can easily solve it by 
        # k = k % len(nums)
        # nums[:k] = reversed(nums[:k])
        # nums[k:] = reversed(nums[k:])
        
        #or 
        # n = len(nums)
        # if k <= n:
        #     k = k
        # else:
        #     k = k%n
        # nums[k:],nums[:k] = nums[:n-k],nums[n-k:]  
            
        # if len(nums) == 2:
        #     if k % 2 == 1:
        #         return nums.reverse()
        #     else:
        #         return nums
        # if len(nums) < k:
        #     return nums