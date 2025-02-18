# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        find = defaultdict(int)
        find[0] = 1
        run_sum = 0
        count = 0

        for i in nums:
            run_sum += i
            count += find[run_sum - k]
            find[run_sum] += 1
            
        return count