# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minimum = total = 0
        answer = float("-inf")
        for num in nums:
            total += num
            answer = max(answer, total - minimum)
            minimum = min(minimum, total)
        return answer
