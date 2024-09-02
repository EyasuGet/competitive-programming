class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dup = set()
        l = 0
        r = 0
        long_s = 0
        while  r <len(s):
            if s[r] not in dup:
                dup.add(s[r])
                r+=1
            else:
                dup.remove(s[l])
                l+=1
            long_s = max(long_s,r-l+1)

        return long_s-1

        