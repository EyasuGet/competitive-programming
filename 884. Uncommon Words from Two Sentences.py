from collections import Counter
def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        ans = []
        s = s1 + " "+ s2
        s = list(s.split())
        s = dict(Counter(s))
        for key,value in s.items():
            if value == 1:
                ans.append(key)
        return ans


        