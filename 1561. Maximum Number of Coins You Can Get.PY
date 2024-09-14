class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        piles.reverse()
        n = len(piles)
        s = 1 #bc its the second max
        coin = 0
        for i in range(n/3): #n/3 to control the number of iterations
            coin += piles[s]
            s += 2 #this is not 3 bc the third person picks the least of the numbers always
        return coin