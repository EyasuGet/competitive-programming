# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans  = numBottles
        rem  = 0

        while numBottles > 0:
            ans += numBottles // numExchange
            rem  += numBottles % numExchange
            numBottles = numBottles // numExchange

            if rem >= numExchange:
                ans += rem // numExchange
                rem = rem // numExchange
  
        return ans
