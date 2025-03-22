# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        q = deque([root])
        av = [root.val]

        while q:
            n = len(q)  
            
            summ = count =  0
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    summ += node.left.val
                    count += 1
                    q.append(node.left)
                if node.right:
                    summ += node.right.val
                    count += 1
                    q.append(node.right)

            if count:
                av.append(summ/count)

        return av