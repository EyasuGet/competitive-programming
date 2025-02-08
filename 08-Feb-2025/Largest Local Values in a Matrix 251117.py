# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []
        dirs = [(0,1),(0,-1), (1,0), (-1,0), (-1,-1), (1,-1), (-1,1), (1,1)]
        for i in range(1, n-1):
            new_row = []

            for j in range(1,n-1):
                maxx = grid[i][j]
                for dx,dy in dirs:
                    newi, newj = i + dx, j+dy
                    maxx = max(maxx, grid[newi][newj])
                    
                new_row.append(maxx)
            ans.append(new_row) 
        return ans 

