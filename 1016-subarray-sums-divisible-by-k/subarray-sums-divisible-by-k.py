class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum_rem = defaultdict(int)
        sum_rem[0] = 1
        total_sum = 0

        for i in nums:
            total_sum += i
            count += sum_rem[total_sum % k]
            sum_rem[total_sum%k] += 1
        return count
                