# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            if (p and not q) or (q and not p):
                return False
            if not p and not q:
                return True
            
            if p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
                return True
            
            return False


        if (not root and subRoot) or (root and not subRoot):
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
        