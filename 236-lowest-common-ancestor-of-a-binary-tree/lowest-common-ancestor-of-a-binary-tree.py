# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# p=5, q=4
#                       3
#               5               1
#           6       2       0       8
#               7       4

class Solution:

    def find(self, node, value):
        if not node:
            return False
        if node.val == value:
            return True
        else:
            return self.find(node.left, value) or self.find(node.right, value)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # if p.val == root.val or q.val == root.val:
        #     return root
        # if self.find(root.left, p.val) and self.find(root.left, q.val):
        #     return self.lowestCommonAncestor(root.left, p, q)
        
        # if self.find(root.right, p.val) and self.find(root.right, q.val):
        #     return self.lowestCommonAncestor(root.right, p, q)
        
        # if (self.find(root.left, p.val) and self.find(root.right, q.val)) or (self.find(root.right, p.val) and self.find(root.left, q.val)):
        #     return root 

        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root  # p in one side, q in the other
        
        return left if left else right