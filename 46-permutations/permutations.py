class Solution(object):
    def permute(self, nums):
        ans , sol = [] , []
        n = len(nums)
        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])  
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()
        backtrack()
        return ans
