# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        q = deque([root])
        level = 0
        ans = [[root.val]]

        while q:
            n = len(q)
            level += 1
            lev = []
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    lev.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    lev.append(node.right.val)
                    q.append(node.right)

            if lev:
                if level % 2 == 0:
                    ans.append(lev)
                else:
                    ans.append(list(reversed(lev)))
        return ans