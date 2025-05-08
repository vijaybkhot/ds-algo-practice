# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # Recursive
        # def dfs(node, arr):
        #     if node:
        #         arr.append(node.val)
        #         dfs(node.left, arr)
        #         dfs(node.right, arr)
        #     return arr
        
        # return dfs(root, [])

        # # Iterative
        # if not root:
        #     return []
            
        # stack = [root]
        # res = []
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        
        # return res

        # Recursive approach:

        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        res = []
        dfs(root)
        return res











        