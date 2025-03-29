# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        while res:
            if res.val == p.val or res.val == q.val:
                return res
            if res.val > p.val and res.val > q.val:
                res = res.left
            elif res.val < p.val and res.val < q.val:
                res = res.right
            elif (res.val < p.val and res.val > q.val) or (res.val > p.val and res.val < q.val):
                return res
            
