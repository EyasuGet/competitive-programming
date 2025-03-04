# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        ans = sorted(s, key=lambda i:int(i), reverse=True)

        for i in range(len(ans)):
            if ans[i] == "0":
                ans[i-1], ans[-1] = ans[-1], ans[i-1]
                break

        return "".join(ans)