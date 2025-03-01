# Problem: Removing Minimum Number of Magic Beans - https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        tot = sum(beans)
       
        min_remove = float("inf")
        for i in range(n):
            cur = tot - beans[i] * (n - i)
            if  min_remove > cur:
                min_remove = cur
        return min_remove