class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s = set(nums2)
        for i in nums1:
            if i in s:
                return i
        return -1
        