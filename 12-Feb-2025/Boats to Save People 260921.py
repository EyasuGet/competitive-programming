# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people) -1 
        l = 0
        r = n
        count = 0
        while l <= r:

            if people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                r -= 1
                count += 1
        return count
