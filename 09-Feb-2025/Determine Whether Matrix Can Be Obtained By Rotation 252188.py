# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat ==  target:
            return True
        n = len(mat)
        for _ in range(3):
            """find the transpose and 
            reverse the rows that gives as the 90deg rotation and 
            check with the target after each rotation"""
            for i in range(n):
                for j in range(i+1 , n):
                    mat[i][j], mat[j][i] = mat[j][i] , mat[i][j]
                mat[i].reverse()
            if mat == target:
                return True
        return False
        

        