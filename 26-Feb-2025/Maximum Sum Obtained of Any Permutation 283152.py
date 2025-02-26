# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        rangee = [0] * (len(nums)+1)
        ans = 0
        for st, en in requests:
            rangee[st] += 1
            rangee[en+1] -=1
        
        for i in range(1, len(rangee)):
            rangee[i] += rangee[i-1]

        nums.sort()
        rangee.sort(reverse=True)

        l = 0
        for i in range(len(nums)-1,-1,-1):
            ans += nums[i] * rangee[l]
            l += 1
        return ans % (10**9 + 7)


