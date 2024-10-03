class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total_sum = sum(nums)
        remainder = total_sum % p
        
        if remainder == 0:
            return 0

        prefix_mod = {0: -1}
        current_sum = 0
        min_length = float('inf')
        
        for i, num in enumerate(nums):
            current_sum += num
            current_mod = current_sum % p
            
            target_mod = (current_mod - remainder) % p
            
            if target_mod in prefix_mod:
                min_length = min(min_length, i - prefix_mod[target_mod])
            
            prefix_mod[current_mod] = i
        if len(nums) == min_length:
            return -1
        return min_length if min_length != float('inf') else -1