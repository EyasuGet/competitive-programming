class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        small = []
        eq = []
        high = []

        for i in nums:
            if i < pivot:
                small.append(i)
            elif i > pivot:
                high.append(i)
            else:
                eq.append(i)
                

        return small+ eq + high 
        