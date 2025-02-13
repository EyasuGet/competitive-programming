# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        if c == 2 or c == 0:
            return True
        
        num = int(math.sqrt(c))

        arr = [i for i in range(0,num+1)]

        l = 0
        r = len(arr) -1
        while l < r:
            if (arr[r] ** 2) * 2 == c:
                return True
            prod = arr[r]**2 + arr[l]**2
            if prod < c:
                l += 1
            elif prod > c:
                r -= 1
            else:
                return True
        return False

        