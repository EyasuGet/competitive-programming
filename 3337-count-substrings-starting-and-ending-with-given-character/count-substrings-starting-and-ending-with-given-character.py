class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        h = Counter(s)
        m = h[c]
        return (m*(m+1))/2