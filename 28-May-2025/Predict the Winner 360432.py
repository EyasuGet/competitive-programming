# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution(object):
    def predictTheWinner(self, nums):
        def helper(left, right):
            if left == right:
                return nums[left]
            return max(nums[left] - helper(left + 1, right), nums[right] - helper(left, right - 1))
        return helper(0, len(nums) - 1) >= 0