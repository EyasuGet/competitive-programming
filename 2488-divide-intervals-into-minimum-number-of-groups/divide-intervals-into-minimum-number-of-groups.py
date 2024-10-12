class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = []
        end = []

        for l, r in intervals:
            start.append(l)
            end.append(r)

        start.sort()
        end.sort()

        i , j = 0, 0
        group  = 0
        res = 0

        while i < len(intervals):
            if start[i] <= end[j]:
                group += 1
                i += 1
            else:
                group -= 1
                j += 1
            res = max(res,group) #max(res, i - j)
        return res