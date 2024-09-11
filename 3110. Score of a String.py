class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        summ = 0
        l = 0
        for i in range(1,len(s)):
            summ += abs(ord(s[l]) - ord(s[i]))
            l += 1
        return summ
            
        