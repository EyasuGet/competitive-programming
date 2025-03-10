# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        s = 0
        n = len(happiness)-1

        happiness.sort()
        subtracts = 0
        
        while k > 0:
            happy = (happiness[n] - subtracts)
            if happy > 0:
                s += happy
                subtracts +=1
            k -= 1
            n -= 1
        return s
