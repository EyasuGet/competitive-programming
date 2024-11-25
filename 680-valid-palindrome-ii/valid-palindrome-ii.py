class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        l = 0
        r = n - 1
        count = 0
        while l <= r:
            if s[l] != s[r]:
                skipl, skipr = s[l+1 : r+1], s[l : r]
                return (skipl == skipl[::-1] or skipr == skipr[::-1])
            l += 1
            r -= 1
        return True
                
            
        