# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        #DFS implementation

        if not root:
            return []
        ans = [root.val]
        rows = defaultdict(list)

        def dfs(root,depth):
            if not root:
                return depth
            if root.left:
                rows[depth].append(root.left.val)
            if root.right:
                rows[depth].append(root.right.val)
            l = dfs(root.left, depth+1)
            r = dfs(root.right, depth+1)
        dfs(root,1)
        for row in rows.values():
            ans.append(max(row))
        return ans



        #DFS impl

        q = deque([root])
        ans = []
        while q:
            n = len(q)
            max_num = float("-inf")
            for _ in range(n):
                node = q.popleft()
                max_num = max(node.val, max_num)
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            if max_num != float("-inf"):
                ans.append(max_num)
        return ans