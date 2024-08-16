class Solution(object):
    def missingNumber(self, nums):
        l = len(nums)
        s = sorted(nums)
        n = 0
        for i in s:
            if n == i:
                n += 1
        return n   


                    
        
     
                    
         