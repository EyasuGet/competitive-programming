# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if sum(costs) <= coins:
            return len(costs)
        
        count_sort = [0] * (max(costs)+1)
        for i in costs:
            count_sort[i] += 1
        
        target = 0
        for idx,val in enumerate(count_sort):
            
            for i in range(val):
                costs[target] = idx
                target += 1

        bought = 0
        i = 0

        while coins > 0 and i < len(costs):
            if costs[i] <= coins:
                coins -= costs[i]
                i += 1
            else:
                break

        return i