# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        idx = 0
        while idx < len(nums):
            pos = nums[idx] - 1
            if nums[idx] != nums[pos]:
                nums[idx], nums[pos] = nums[pos], nums[idx]
            else:
                idx += 1
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
