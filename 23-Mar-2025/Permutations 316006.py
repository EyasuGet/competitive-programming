# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        ans , sol = [] , []
        n = len(nums)
        def bt():
            if len(sol) == n:
                ans.append(sol[:])
            
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    bt()
                    sol.pop()
        bt()
        return ans
        #tc = o(n!) 
        #sc = o(n)