# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        #DFS implementation    
        max_dep = [-1]
        def dfs(root, depth):
            max_dep[0] = max(max_dep[0],depth)
            if not root:
                return depth
            if not root.children:
                return depth
            for child in root.children:

                child_depth = dfs(child, depth+1)
                if child_depth:
                    max_dep[0] = max(max_dep[0], child_depth)
    
        dfs(root, 1)
        return max_dep[0]


        #BFS imp

        q = deque([root])
        count = 0
        while q:
            n = len(q)
            count += 1
            for _ in range(n):
                node = q.popleft()  
                
                if node.children:
                    for child in node.children:
                        q.append(child) 

        return count