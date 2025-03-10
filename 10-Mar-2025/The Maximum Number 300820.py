# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num = list(set(nums))
        num.sort()
        
        if len(num) > 2:
            return num[-3]
        else:
            return num[-1]