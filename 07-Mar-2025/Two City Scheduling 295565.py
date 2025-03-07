# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #lets take the difference of b - a
        #so that we can get the cost of sending person b relative to a
        #if we sort the diff array we get the mininized costs of sending a person to city b
        n = len(costs)

        diff = []
        for a,b in costs:
            d = b-a
            diff.append([d,a])
            #we can also save both a and b [d, a, b]
        
        diff.sort()
        # diff = sorted(diff, key= lambda i: i[0])

        min_cost = 0
        for i in range(n):
             #add the minimum cost of b that is half
            if i < (n // 2):
                min_cost += (diff[i][0] + diff[i][1])
            else:
                #add the minimum cost of a that is the remaining
                min_cost += diff[i][1]
        
        return min_cost