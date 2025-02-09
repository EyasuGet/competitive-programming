# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        


        #we need to store the diagonal elemments that have pattern same sum of row and col
        crossdiag = defaultdict(list)

        for row in range(n):
            for col in range(m):
                crossdiag[row+col].append((mat[row][col]))
        
        #reverse the diagonals that have even sum of row and col to get main

        for rcsum in crossdiag:
            if rcsum % 2 == 0:
                crossdiag[rcsum].reverse()
                
        ans = []
        for num in crossdiag.values():
            for i in num:
                ans.append(i)

        return ans
