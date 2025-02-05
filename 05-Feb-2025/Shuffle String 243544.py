# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        

        ans = [1]*len(s)

        for i in range(len(s)):
            ans[indices[i]] = s[i]
        return "".join(ans)
