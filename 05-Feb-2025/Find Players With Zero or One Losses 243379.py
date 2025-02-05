# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winner = []
        loser = defaultdict(int)

        for match in matches:
            winner.append(match[0])
            loser[match[1]] += 1
            
        
        noloss= set()
        for i in winner:
            if i not in loser:
               noloss.add(i)

        oneloss = set()
        for key,value in loser.items():
            if value == 1:
                oneloss.add(key)
        return [sorted(list(noloss)),sorted(list(oneloss))]


