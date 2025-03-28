# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # if p is child of q then q is the lowest ancestor
        # if they have same parent then the parent is the LCA
        # if they are in left and right of the root then the root is the LCA
        
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p , q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p , q)
        else:
            return root