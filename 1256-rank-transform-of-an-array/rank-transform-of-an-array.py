class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        s = sorted(set(arr))
        h = {}
        ans = []
        for index,num in enumerate(s):
            if num not in h:
                h[num] = index + 1
        for i in arr:
            ans.append(h[i])
        return ans
       

        