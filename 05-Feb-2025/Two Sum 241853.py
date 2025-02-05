# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = {}

        for i in range(len(nums)):
            find = target - nums[i]
            if find in found:
                return [i,found[find]]
            found[nums[i]] = i
    

