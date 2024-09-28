class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        n = len(people)
        l = 0
        r = n - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1
        return boats