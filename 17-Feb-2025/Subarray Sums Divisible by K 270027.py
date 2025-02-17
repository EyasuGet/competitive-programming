# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        summ = defaultdict(int)
        summ[0] = 1
        total_sum = 0
        count = 0

        for i in nums:
            total_sum += i
            count += summ[total_sum % k] 
            summ[total_sum % k ] += 1
            
        return count
        
