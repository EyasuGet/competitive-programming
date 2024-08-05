class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left <= right:
            mid = (left+right)//2
            if isBadVersion(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        