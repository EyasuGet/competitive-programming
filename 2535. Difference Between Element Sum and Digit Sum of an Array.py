class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum1 = 0
        sum2 = 0
        for i in nums:
            sum1 += i
            temp = i
            while temp > 0:
                sum2 += temp % 10
                temp = temp // 10
        return abs(sum1- sum2)