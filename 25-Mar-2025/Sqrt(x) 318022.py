# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        sq_r = 0

        while left <= right:
            mid = (left+right) // 2
            if mid**2 <= x:
                sq_r = mid
                left = mid + 1
            else:
                right = mid -1
        return sq_r