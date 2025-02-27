# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = min_sum = max_sum = 0
        for num in nums:
            prefix += num
            if min_sum > prefix:
                min_sum = prefix
            if max_sum < prefix:
                max_sum = prefix
        if min_sum == max_sum:
            return abs(min_sum)
        return abs(min_sum - max_sum)