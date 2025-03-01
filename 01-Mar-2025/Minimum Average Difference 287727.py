# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        runn = 0
        tot = sum(nums)
        min_aver = float("inf")
        min_idx = 0
        for i in range(n-1):
            runn += nums[i]
            tot -= nums[i]
            average = abs((runn//(i+1)) - tot//(n-i-1)) 
            print(average)
            if average < min_aver:
                min_aver = average
                min_idx = i
        #for the last idx we just need to find the total average
        average = sum(nums) / n
        if average < min_aver:
            return n-1
        return min_idx
            