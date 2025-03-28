# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root,curr_max,curr_min):
            if not root:
                return curr_max - curr_min
                               
            curr_max = max(curr_max, root.val)
            curr_min = min(curr_min, root.val)

            l = dfs(root.left, curr_max, curr_min)
            r = dfs(root.right, curr_max,curr_min)

            return max(l,r)

        return dfs(root,root.val, root.val)
