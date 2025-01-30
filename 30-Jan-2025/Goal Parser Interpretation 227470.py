# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans = ""
        i = 0
        while i <= (len(command) - 1):
        # for i in range(len(command)-2):
            if command[i] == "G":
                ans += command[i]
                i += 1
            elif command[i] == "(" and command[i+1] == ")":
                ans += "o"
                i += 2
            else:
                ans += "al"
                i += 4
        return ans