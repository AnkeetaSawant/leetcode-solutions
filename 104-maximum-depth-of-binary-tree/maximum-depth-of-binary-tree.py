# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0
            
            right = dfs(node.right)
            left = dfs(node.left)
            print(node.val,right, left, max(left, right))
            return 1 + max(left, right)

        return dfs(root)
    