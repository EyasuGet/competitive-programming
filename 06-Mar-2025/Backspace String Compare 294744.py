# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def next_valid(string, index):
            skip = 0
            while index >= 0:
                if string[index] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return index
                index -= 1
            return -1

        i, j = len(s) - 1, len(t) - 1
        
        while i >= 0 or j >= 0:
            i = next_valid(s, i)
            j = next_valid(t, j)
            
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            
            i -= 1
            j -= 1

        return True
