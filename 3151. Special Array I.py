class Solution(object):
    def isArraySpecial(self, nums):
        l = 0
        r = 1
        if len(nums)==1:
            return True

        while r<len(nums):
            if (nums[l] % 2 ==0)and(nums[r]%2==0):
                return False
            elif (nums[l] % 2 ==1)and(nums[r]%2==1):
                return False
            else:
                l += 1
                r += 1
        return True
            