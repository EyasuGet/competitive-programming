# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        dup = []
        for i in nums:
            if i in hashmap:
                dup.append(i)
            else:
                hashmap[i] = 1
        return dup