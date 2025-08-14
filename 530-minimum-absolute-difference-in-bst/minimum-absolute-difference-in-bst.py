# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        stack = []
        def inorder(node):
            if node:
                inorder(node.left)
                stack.append(node.val)
                inorder(node.right)
        
        inorder(root)
        for i in range(1, len(stack)):
            min_diff = min(min_diff, abs(stack[i]-stack[i-1]))
        return min_diff