# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # # Recursive solution
        # def invert(root):
        #     if root:
        #         root.left, root.right = root.right, root.left
        #         if root.left:
        #             invert(root.left)
        #         if root.right:
        #             invert(root.right)
        #     return root
        
        # return invert(root)

        # Iterative solution:
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root

        