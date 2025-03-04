# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        doubles = ones =  0
        while target > 1:
            if target % 2 == 1:
                target -= 1
                ones += 1
            else:
                if maxDoubles > 0:
                    target /= 2
                    doubles += 1
                    maxDoubles -= 1
                else:
                    ones += target-1
                    target = 0

        return int(doubles + ones)

