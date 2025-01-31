# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type modified: str
        :rtype: int
        """
        if len(s.strip())==1:
            return 1
        modified = s.strip()
        i = len(modified) -1 

        while modified[i] != " ":
            i -= 1
            if i == -1:
                return len(modified)
        return len(modified[i:-1])
