# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum_level = float('-inf')
        queue = deque([root])
        level = 1
        final_level = 1
        
        while queue:
            level_sum = 0
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            if max_sum_level < level_sum:
                max_sum_level, final_level = level_sum, level
            level = level + 1
        return final_level
