# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(r1, r2):
            if not r1 and r2 or not r2 and r1:
                return False
            if not r1 and not r2:
                return True
            
            return r1.val == r2.val and isMirror(r1.right, r2.left) and isMirror(r1.left, r2.right)

        return isMirror(root.left, root.right) if root else True