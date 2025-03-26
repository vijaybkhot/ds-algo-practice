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
        def invert(root):
            if root:
                left = root.left
                root.left = root.right
                root.right = left
                if root.left:
                    invert(root.left)
                if root.right:
                    invert(root.right)
            return root
        
        rev_tree = invert(root)
        return rev_tree
        