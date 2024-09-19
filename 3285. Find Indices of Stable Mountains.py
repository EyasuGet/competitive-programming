class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        ans = []
        l = 0
        r = 1
        while r < len(height):
            if height[l] > threshold and height[l] != 0:
                ans.append(r)
                r += 1
                l += 1
            else:
                r += 1
                l += 1
        return ans


        # k = []
        # for i in range(1, len(height)):
        #     if height[i-1] > threshold:
        #         k.append(i)
        # return k
        