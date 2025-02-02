# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        for i in digits:
            s += str(i)
        num = int(s) + 1

        ans = []
        while num > 0:
            r = num % 10
            num //= 10
            ans.append(r)
        ans.reverse()
        return ans