# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])

        start_row = start_col = 0
        end_row = n - 1
        end_col = m - 1

        while start_row <= end_row and start_col <= end_col:

            for j in range(start_col,end_col+1):
                ans.append(matrix[start_row][j])
                
            if len(ans) == n * m:
                break

            for i in range(start_row+1, end_row + 1):
                ans.append(matrix[i][end_col])

            if len(ans) == n * m:
                break

            for j in range(end_col-1, start_col - 1, -1):
                ans.append(matrix[end_row][j])

            if len(ans) == n * m:
                break

            for i in range(end_row-1, start_row,-1):
                ans.append(matrix[i][start_col])

            if len(ans) == n * m:
                break

            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1

        return ans      
