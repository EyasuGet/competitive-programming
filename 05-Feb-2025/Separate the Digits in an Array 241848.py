# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:
            l = []
            place = 0
            while num > 0:
                r = (num % 10)
                l.append(r)
                num //= 10

            for i in range(len(l)-1,-1,-1):
                ans.append(l[i])
        return ans