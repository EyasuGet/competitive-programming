# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        l = 0
        r = t - 1

        while l <= r:
            m = (l + r) // 2
            i = m // n
            j = m % n
            mid_num = matrix[i][j]
            #let i be the number of rows i = m // 2
            #let j be the number of columns j = m % 2

            if target == mid_num:
                return True
            elif target < mid_num:
                r = m - 1
            else:
                l = m + 1

        return False       
        