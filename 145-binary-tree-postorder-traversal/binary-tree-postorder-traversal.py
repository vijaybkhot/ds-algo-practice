# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       
        # res = []
        # def postorder(node):
        #     if node:
        #         postorder(node.left)
        #         postorder(node.right)
        #         res.append(node.val)

        # postorder(root)
        # return res

        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return res[::-1]

