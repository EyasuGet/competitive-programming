# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        max_depth = [True]
        def dfs(root, depth):
            if not root:
                return depth

            l = dfs(root.left, depth+1)
            r = dfs(root.right , depth+1)
            max_depth[0] = max_depth[0] and abs(l-r) < 2
            return max(l,r)
        dfs(root, 0)
        return max_depth[0]




        return 



        # return abs(right , depth+1 - left, depth+1)  < 2 and 