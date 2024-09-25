class Solution(object):
    def removeTrailingZeros(self, num):
        l = 0
        r = len(num) - 1

        while l < r:
            if num[l] == "0":
                l += 1
            elif num[r] == "0":
                r -= 1
            else:
                return num[l:r+1]
        return num[l:r+1]

        return num.rstrip('0')
        
        
