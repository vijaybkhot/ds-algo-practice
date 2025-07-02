# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        temp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(temp)
        return root







        # # if not root:
        # #     return None
        # # rootLeft = root.left        
        # # root.left = self.invertTree(root.right)
        # # root.right = self.invertTree(rootLeft)
        # # return root

        # # if not root:
        # #     return None
        
        # # rootLeft = root.left
        # # root.left = self.invertTree(root.right)
        # # root.right = self.invertTree(rootLeft)
        
        
        # # return root

        # curr = root
        # def dfs(node):
        #     if not node:
        #         return None
        #     dfs(node.left)
        #     dfs(node.right)
        #     node.left, node.right = node.right, node.left
        
        # dfs(curr)
        # return curr















        