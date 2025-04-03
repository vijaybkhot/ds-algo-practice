# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        val_set = set([p.val, q.val])
        def dfs(node):
            if not node:
                return set()
            left_set = dfs(node.left)
            right_set = dfs(node.right)
            
            merged_set = left_set | {node.val} | right_set

            if p.val in merged_set and q.val in merged_set and self.res is None:
                self.res =  node
            return merged_set

        dfs(root)
        return self.res