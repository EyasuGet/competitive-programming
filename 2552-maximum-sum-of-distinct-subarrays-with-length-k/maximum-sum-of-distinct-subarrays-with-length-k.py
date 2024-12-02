class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        num = defaultdict(int)
        max_sum = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            num[nums[i]] += 1

            if i - l + 1 > k:
                num[nums[l]] -= 1

                if num[nums[l]] == 0:
                    num.pop(nums[l])
                cur_sum -= nums[l]
                l += 1
            if len(num) == k == i - l +1:
                max_sum = max(cur_sum,max_sum)
        return max_sum