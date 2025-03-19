# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        comb = []
        start = 1
        def bt(start, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return 

            for i in range(start, n+1):

                comb.append(i)
                bt(i+1, comb)
                comb.pop()
        bt(start, comb)
        return ans

        
