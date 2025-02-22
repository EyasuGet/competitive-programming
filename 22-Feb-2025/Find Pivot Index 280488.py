# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        running_sum = 0
        total = sum(nums)

        for i in range(len(nums)):
            total -= nums[i]
            if total == running_sum:
                return i
            running_sum += nums[i]
        return -1