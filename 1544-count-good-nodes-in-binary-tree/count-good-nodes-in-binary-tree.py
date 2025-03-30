# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if root is None:
        #     return 0
        # self.good_nodes = 0

        # def dfs(root, max_val):
        #     if root:
        #         if root.val >= max_val:
        #             self.good_nodes += 1
        #         max_val = max(max_val, root.val)
        #         dfs(root.left, max_val)
        #         dfs(root.right, max_val)
        
        # dfs(root, root.val)
        # return self.good_nodes
        
        # Optimized solution - without using class variable
        def dfs(node, max_val):
            if not node:
                return 0
            good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return good + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, root.val)