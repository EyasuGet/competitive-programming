# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sub_sum = defaultdict(int)
        sub_sum[0] = 1
        totalsum = 0
        count = 0
        for i in nums:
            totalsum += i
            count += sub_sum[totalsum-goal]
            sub_sum[totalsum] += 1
        return count