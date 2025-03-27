# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # if root.left:    
        #     return self.isBalanced(root.left)
        # if root.right:
        #     return self.isBalanced(root.right)

        return self.height(root) != -1

    def height(self, node: Optional[TreeNode])-> int:
            if not node:
                return 0
            leftHeight = self.height(node.left)
            rightHeight = self.height(node.right)

            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)
