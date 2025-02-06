# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        
        pillow = 0
        dirc = 1
        ct = 0
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        while ct < time:
            pillow += dirc
            if pillow == n-1:
                dirc = -1
            elif pillow == 0:
                dirc = 1

            ct += 1
        return pillow + 1
            
