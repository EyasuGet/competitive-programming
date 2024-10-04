class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        le = len(skill)
        skill.sort()

        summ = sum(skill)
        teams_sum = summ / (le / 2)

        l = 0
        r = le - 1
        chem = 0
        while l < r:
            s = skill[l] + skill[r]
            if s == teams_sum:
                chem +=(skill[l] * skill[r])
                l += 1
                r -= 1
            elif s > teams_sum:
                return -1
            else:
                l += 1
        return chem