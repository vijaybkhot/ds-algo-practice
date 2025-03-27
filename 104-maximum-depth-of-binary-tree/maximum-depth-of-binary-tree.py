# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # def depth(root, currDepth):
        #     if root:
        #         new_depth = max(depth(root.left, currDepth+1), depth(root.right, currDepth+1))
        #         return new_depth
        #     return currDepth
        
        # return depth(root, 0)

        # Optimized solution
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        