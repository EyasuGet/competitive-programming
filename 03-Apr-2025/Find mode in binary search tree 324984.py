# Problem: Find mode in binary search tree - https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        freq = defaultdict(int)
        def dfs(root):
            if not root:
                return 
            freq[root.val] += 1
            l = dfs(root.left)
            r = dfs(root.right)
        dfs(root)
        ans = []
        max_freq = max(list(freq.values()))
        for key,val in freq.items():
            if val == max_freq:
                ans.append(key)
        return ans

            