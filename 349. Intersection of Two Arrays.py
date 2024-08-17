class Solution(object):
    def intersection(self, nums1, nums2):
        num=[]
        for x in nums1:
            if x in nums2:
                num.append(x)
        return set(num)