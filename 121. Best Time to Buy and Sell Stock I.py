class Solution(object):
    def maxProfit(self, prices):
        #bruteforce
        # best_sell = 0
        # for i in range(len(prices)):
        #     max_diff = 0
        #     for j in range(i+1,len(prices)):
        #         if prices[i] < prices[j]:
        #             max_diff = max(max_diff, (prices[j] - prices[i]))
                
        #     best_sell = max(max_diff,best_sell)
        # return best_sell

        #optimised

        cheapest = prices[0]
        profit = 0

        for i in range(1,len(prices)):
            c_pro = prices[i] - cheapest
            if c_pro > profit:
                profit = c_pro
            if prices[i] < cheapest:
                cheapest = prices[i]
        return profit   
