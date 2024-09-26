class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i-j) >= indexDifference and abs(nums[i]-nums[j]) >= valueDifference:
                    ans.append(i)
                    ans.append(j)
                    return ans
        return [-1,-1]