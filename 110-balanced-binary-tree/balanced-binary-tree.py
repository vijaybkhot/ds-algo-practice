# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            
            if abs(left-right) <= 1:
                return 1 + max(left, right)
            else:
                return float('inf')
        
        if not root:
            return True
        
        left_height = height(root.left)
        right_height = height(root.right)
        return abs(left_height-right_height) <= 1












    #     self.isBalanced = True
    #     if not root:
    #         return True
    #     left = self.height(root.left)
    #     right = self.height(root.right)

    #     return abs(left - right) <= 1 if self.isBalanced else self.isBalanced
    
    
    # def height(self, node):
    #     if not node:
    #         return 0
    #     left = self.height(node.left)
    #     right = self.height(node.right)
    #     if abs(left - right) > 1:
    #         self.isBalanced = False
    #     return 1 + max(left, right)















    # #     if not root:
    # #         return True
        
    # #     # if root.left:    
    # #     #     return self.isBalanced(root.left)
    #     # if root.right:
    #     #     return self.isBalanced(root.right)

    #     return self.height(root) != -1

    # def height(self, node: Optional[TreeNode])-> int:
    #         if not node:
    #             return 0
    #         leftHeight = self.height(node.left)
    #         rightHeight = self.height(node.right)

    #         if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
    #             return -1

    #         return 1 + max(leftHeight, rightHeight)


















