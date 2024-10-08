class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        imbalance = 0
        max_im = float("-inf")
        for i in s:
            if i == "[":
                imbalance -= 1
            else:
                imbalance += 1
            max_im = max(imbalance,max_im)
        return (max_im + 1)/2
            