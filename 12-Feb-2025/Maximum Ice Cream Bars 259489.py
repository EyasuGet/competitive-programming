# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if sum(costs) <= coins:
            return len(costs)
        
        costs.sort()

        bought = 0

        i = 0

        while coins > 0 and i < len(costs):
            if costs[i] <= coins:
                coins -= costs[i]
                i += 1
            else:
                break

        return i