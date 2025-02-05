# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for i in accounts:
            wealth = sum(i)
            if wealth > richest:
                richest = wealth
        return richest