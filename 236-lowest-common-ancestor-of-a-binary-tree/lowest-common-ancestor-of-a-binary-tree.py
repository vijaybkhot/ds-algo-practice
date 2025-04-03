# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # # Approach using set - Inefficient
        # self.res = None
        # def dfs(node):
        #     if not node or self.res:  # Stop recursion if LCA is found
        #         return set()

        #     left_set = dfs(node.left)
        #     right_set = dfs(node.right)

        #     # If either left_set or right_set is None, treat it as an empty set
        #     if left_set is None: left_set = set()
        #     if right_set is None: right_set = set()

        #     merged_set = left_set | {node.val} | right_set

        #     if p.val in merged_set and q.val in merged_set and self.res is None:
        #         self.res = node
        #         return None  # Signal to stop further recursion

        #     return merged_set


        # dfs(root)
        # return self.res

        # Optimized approach

        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left or right
        