# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = defaultdict(list)


        def dfs(root, depth):
            if not root:
                return 
        
            
            level[depth].append(root.val)
            
            l = dfs(root.left, depth + 1)
            r = dfs(root.right, depth + 1)
        
        dfs(root,1)
        return list(level.values())