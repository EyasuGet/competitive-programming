# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for col in range(len(matrix[0])):
            new_row = []
            for row in range(len(matrix)):
                new_row.append(matrix[row][col])
            ans.append(new_row)
        return ans

                               