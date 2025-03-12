# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def findpower(self,x,n):
        if n == 0:
            return 1
        if n == 1 or n == -1:
            return x
        ans = self.findpower(x,n//2)
        if n % 2 == 0:
            
            return ans * ans
        else:
            return ans *ans * x

    def myPow(self, x: float, n: int) -> float:
        ans = self.findpower(x,abs(n))
        if n < 0 and ans != 0:
            return 1 / ans
        else:
            return ans