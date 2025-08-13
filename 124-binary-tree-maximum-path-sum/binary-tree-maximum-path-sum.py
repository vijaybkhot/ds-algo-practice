# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_sum = float('-inf')
        @lru_cache(maxsize=None)
        def dfs(node):
            if node:
                center = node.val
                left, right, left_and_right = float('-inf'), float('-inf'), float('-inf')
                
                if node.left:
                    left = node.val+dfs(node.left)
                
                if node.right:
                    right = node.val+dfs(node.right)
                
                if node.left and node.right:
                    left_and_right = node.val+dfs(node.right)+dfs(node.left)
                
                self.max_sum = max(self.max_sum, left, right, left_and_right, center)
                
                return max(center, left, right)
            else:
                return float('-inf')
        
        dfs(root)

        return self.max_sum