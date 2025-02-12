# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        teamskill = skill[0] + skill[n-1]

        l = 0
        r = n -1
        total_skill = 0
        while l < r:
            if skill[l] + skill[r] != teamskill:
                return -1
            else:
                total_skill += (skill[l] * skill[r])
            l += 1
            r -= 1
        return total_skill
