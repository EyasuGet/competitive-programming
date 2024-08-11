class Solution(object):
    def majorityElement(self, nums):
        n = sorted(nums)
        l = len(nums)
            
        if n[0] == n[l//2]:
            return n[0]
        else:
            return n[l//2]
        