class Solution(object):
    def removeDuplicates(self, nums):
        leftP = 1
        for right in range(1,len(nums)):
            if nums[right] != nums[right-1]:
                nums[leftP] = nums[right]
                leftP += 1
        return leftP