class Solution(object):
    def numIdenticalPairs(self, nums):

        count = 0
        n = len(nums)
        for i in range(n):
            j = i + 1
            while (j < n):
                if nums[i] == nums[j]:
                    count += 1
                j +=1
        return count     