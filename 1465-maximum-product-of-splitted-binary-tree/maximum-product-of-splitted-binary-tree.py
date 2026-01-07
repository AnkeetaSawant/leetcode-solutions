# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10 ** 9 + 7
        self.max_product = 0

        #to find total sum
        def totalSumTree(node):
            if not node:
                return 0
            return node.val + totalSumTree(node.left) + totalSumTree(node.right)

        #Post-order Traversal : left, right, root
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            subtree_sum = node.val + left + right   
            
            self.max_product = max(
                self.max_product, 
                subtree_sum * (total_sum - subtree_sum)
                )
            
            return subtree_sum

        total_sum = totalSumTree(root)
        dfs(root)
        return self.max_product % MOD

       

