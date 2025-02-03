# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ra_nge = set()
        for r in ranges:
            for i in range(r[0],r[1]+1):
                ra_nge.add(i)
        
        
        for i in range(left,right+1):
            if i not in ra_nge:
                return False
        return True