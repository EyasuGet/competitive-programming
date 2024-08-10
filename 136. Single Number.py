class Solution(object):
    def singleNumber(self, nums):
        n = sorted(nums)
        if len(nums)<2:
            return n[0]
        for i in range(0,len(nums)-1,2): 
            if n[i] != n[i+1]:
                return n[i]
        return n[-1]