# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        third_value = float('-inf')
        stack = []

        for number in reversed(nums):
            if number < third_value:
                return True

            while stack and stack[-1] < number:
 
                third_value = stack.pop()

            stack.append(number)

        return False
        