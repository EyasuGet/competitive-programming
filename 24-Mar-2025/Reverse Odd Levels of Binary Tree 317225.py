# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root


        def dfs(l, r, depth):
            if not l and not r:
                return

            if depth % 2 == 1:
                l.val, r.val = r.val, l.val

            dfs(l.right, r.left, depth+1)
            dfs(l.left, r.right, depth+1)
        
        dfs(root.left,root.right,1)
        return root
                    

                
