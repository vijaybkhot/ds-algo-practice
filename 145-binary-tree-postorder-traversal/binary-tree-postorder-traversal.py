# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # self.res = []
        # def postorder(node):
        #     if node:
        #         postorder(node.left)
        #         postorder(node.right)
        #         self.res.append(node.val)
        # postorder(root)
        # return self.res

        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res[::-1]

















        
        # # Recursive
        # def dfs(node):
        #     if node:
        #         dfs(node.left)
        #         dfs(node.right)
        #         res.append(node.val)
        # res = []
        # dfs(root)
        # return res

        # # Iterative:
        # if not root:
        #     return []
        # res, stack = [], [root]

        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        
        # return res[::-1]



