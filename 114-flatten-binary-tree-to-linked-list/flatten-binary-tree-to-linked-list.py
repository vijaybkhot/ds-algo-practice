# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if node is None:
                return None

            if node.left:
                left_tree = node.left
                right_tree = node.right
                node.left = None
                node.right = dfs(left_tree)
                if node.right:
                    curr = node.right
                    while curr.right:
                        curr = curr.right
                    curr.right = dfs(right_tree)
            elif node.right:
                node.right = dfs(node.right)
            return node
                    
        dfs(root)
        