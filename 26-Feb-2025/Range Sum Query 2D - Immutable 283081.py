# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows =  len(self.matrix)
        cols = len(self.matrix[0])
        # add 0 arr in the matrix to prevent index outof range
        self.prefix = [[0] * (cols + 1) for i in range(rows + 1)]

        #find the 2d prefix sum 
        #add horizontally
        for row in range(rows):
            for col in range(1,cols+1):
                self.prefix[row+1][col] =self.prefix[row+1][col-1] + self.matrix[row][col-1]

        #add vertically
        for row in range(1,rows+1):
            for col in range(cols):
                self.prefix[row][col+1] = self.prefix[row-1][col+1] + self.prefix[row][col+1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        ans += self.prefix[row2+1][col2+1]
        ans -= self.prefix[row2+1][col1]
        ans -= self.prefix[row1][col2+1]
        ans += self.prefix[row1][col1]
        return ans





# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)