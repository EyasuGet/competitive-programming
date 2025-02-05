# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans  = []
        for i in range(n):
            idx = abs(nums[i]) - 1 #find the index to be flipped
            if nums[idx] < 0:   #already flipped this mean the number pointing is duplicat
                ans.append(abs(nums[i]))
            else:
                nums[idx] *= (-1) #marking that it is flipped
        return ans

            

        
