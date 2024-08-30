class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new = re.sub(r"[^a-zA-Z0-9]","",s)
        lowCase = new.lower()
        
        l = 0
        r = len(new) - 1
        while l <= r:
            if lowCase[l] == lowCase[r]:
                l += 1
                r -= 1
            else:
                return False
        return True