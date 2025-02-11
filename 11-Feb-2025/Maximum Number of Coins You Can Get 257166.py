# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()
        i = len(piles)
        ans = 0
        while n > 0:
            ans += piles[i-2]
            i -= 2
            n -= 1
        return ans


