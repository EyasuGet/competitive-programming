# Problem: Concatenation of Array - https://leetcode.com/problems/concatenation-of-array/description/

class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     nums.append(nums[i])
        # return nums
        return nums + nums
        
