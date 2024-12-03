class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


        sum_rem = defaultdict(int)
        count = 0
        total_sum = 0
        sum_rem[0] = 1

        for i in nums:
            total_sum += i
            count += sum_rem[total_sum - k]
            sum_rem[total_sum] += 1
        return count

        