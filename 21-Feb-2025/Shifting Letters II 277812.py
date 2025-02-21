# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        ans = [0] * (len(s) + 1)

        for l, r, d in shifts:
            if d == 0:
                ans[l] -= 1
                ans[r+1] += 1
            elif d == 1:
                ans[l] += 1
                ans[r+1] -= 1
        
        for i in range(1,len(ans)):
            ans[i] += ans[i-1]
        
        str1 = []

        for i in range(len(s)):
            shift = ans[i] % 26
            new = shift + ord(s[i])

            if new > 122:
                new -=  26
            elif new < 97:
                new += 26
            
            str1.append(chr(new))
        return "".join(str1)



