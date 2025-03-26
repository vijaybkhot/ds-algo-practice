# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def preorder(root, output):
            if root:
                output.append(root.val)
                preorder(root.left, output)
                preorder(root.right, output)
            return output
        
        return preorder(root, [])
        