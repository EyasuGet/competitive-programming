# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        freq = Counter(answers)
        ans = 0
        for key,val in freq.items():
    
            if key == 0:
                ans += val
            else:
                max_size = key + 1
                group = (val + max_size - 1) // max_size
                ans += group * max_size
        return ans
