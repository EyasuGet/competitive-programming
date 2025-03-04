# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change5 = change10 = change20 = 0

        for i in bills:
            if i == 5:
                change5 += 1
            elif i == 10:
                change10 += 1
                if change5 == 0:
                    return False
                change5 -= 1
            elif i == 20:
                change20 += 1
                if change5 == 0:
                    return False    
                elif change10 > 0:
                    change10 -= 1
                    change5 -= 1
                elif change5 > 2:
                    change5 -= 3
                else:
                    return False
        return True