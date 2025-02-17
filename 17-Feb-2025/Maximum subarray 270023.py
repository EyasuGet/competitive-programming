# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #bruteforce
        # max_sub = float("-inf")
        # for i in range(len(nums)):
        #     curr = 0
        #     for j in range(i, len(nums)):
        #         curr += nums[j]

        #         max_sub = max(curr , max_sub)
        
        # return max_sub

        #kadane algo

        max_sub = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):

            max_sub = max(max_sub + nums[i], nums[i])
            res = max(res, max_sub)

        return res
