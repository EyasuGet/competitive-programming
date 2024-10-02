class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # k = len(nums)
        # for i in range(len(nums)):
        #     c = 0
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             c += 1
        #             if c > 1:
        #                 nums[i] = "_"
        #                 k -= 1
        #                 break
        #         else:
        #             break
        # nums.sort()
        # return k

        if len(nums) <= 2:
            return len(nums)

        i = 1  
        for j in range(2, len(nums)):  
            if nums[j] != nums[i-1]:
                i += 1   
                nums[i] = nums[j]  

        return i + 1