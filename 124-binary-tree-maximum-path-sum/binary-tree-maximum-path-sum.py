# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # # First Attempt:
        # self.curr_max = float('-inf')
        # def dfs(node):
        #     if node is None:
        #         return 0
                
        #     left_path_sum = dfs(node.left)
        #     right_path_sum = dfs(node.right)
        #     curr_path_sum = max(node.val, node.val + left_path_sum + right_path_sum, node.val + left_path_sum, node.val + right_path_sum)
        #     self.curr_max = max(self.curr_max, curr_path_sum)
        #     return_path_sum = max(node.val, node.val+left_path_sum, node.val + right_path_sum)
        #     return return_path_sum
        
        # dfs(root)
        # return self.curr_max

        # More readable code:
        self.curr_max = float('-inf')

        def dfs(node):
            if not node:
                return 0
            leftTreeSum = max(0, dfs(node.left))
            rightTreeSum = max(0, dfs(node.right))
            curr_node_sum = node.val + leftTreeSum + rightTreeSum
            self.curr_max = max(self.curr_max, curr_node_sum)

            return node.val + max(leftTreeSum, rightTreeSum)
        
        dfs(root)
        return self.curr_max
            
