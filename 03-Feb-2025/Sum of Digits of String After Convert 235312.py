# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        str1 = ""
        for i in s:
            str1 += str(ord(i)- 96)

        ans = 0
        while k > 0:
            ans = 0
            for i in str1:
                ans += int(i)

            str1 = str(ans)
            k -= 1
        return ans
        