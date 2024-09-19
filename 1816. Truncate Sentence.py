class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l  = list(s.split())
        a = l[:k]
        return " ".join(a)
        