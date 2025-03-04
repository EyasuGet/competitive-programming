# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        substring = 0
        for i in s:
            if i == "R":
                count += 1
            elif i == "L":
                count -= 1
            
            if count == 0:
                substring += 1
                count = 0
        return substring
