# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        n = num // 3
        if 3*n == num:
            return [n-1,n,n+1]
        else:
            return []
























        n = num//3
        for i in range(n):
            if (i*3 + 3) == num:
                return [i,i+1,i+2]
        return []



        