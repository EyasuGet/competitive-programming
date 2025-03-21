# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        bt_l = root.val

        while q:
            n = len(q)
            bt_l = q[0].val

            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return bt_l


        #DFS implementation
        max_depth = [float("inf")]
        ans = [0]
        def dfs(root, depth):
            if not root:
                return 
            
            if max_depth[0] == float("inf"):
                max_depth[0] = depth
                ans[0] = root.val
            else:
                if max_depth[0] < depth:
                    max_depth[0] = depth
                    ans[0] = root.val

            l = dfs(root.left, depth+1)
            r = dfs(root.right, depth + 1)
        dfs(root, 1)
        return ans[0]