# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def preorder(node):
        #     if node:
        #         res.append(node.val)
        #         preorder(node.left)
        #         preorder(node.right)
        
        # preorder(root)
        # return res
        if not root:
            return []
        stack = [root]
        res = []

        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        
        return res
            