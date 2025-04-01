# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()
        for i in range(1,n+1):
            q.append(i)
        

        while len(q) > 1:
            i = k
            while i > 0:
                q.append(q.popleft())
                i -= 1
            q.pop()
        return q[0]