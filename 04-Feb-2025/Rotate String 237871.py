# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(goal) != len(s):
            return False
        
        return goal in (s+s)




        