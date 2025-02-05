# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        n = len(nums)                                
        result = []
        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(nums[i])
            # elif nums[i] > 0:
            #     idx = (i + nums[i]) % n
            #     result.append(nums[idx])
            else:
                idx = (nums[i] + i) % len(nums)
                result.append(nums[idx])

        return result
        