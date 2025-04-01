# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack = [(root, float('-inf'), float('inf'))]
        max_difference = 0

        while stack:
            node, max_ancestor, min_ancestor = stack.pop()
            if max_ancestor != float('-inf'):
                max_difference = max(max_difference, abs(node.val - max_ancestor), abs(node.val - min_ancestor))
            new_max_ancestor = max(max_ancestor, node.val)
            new_min_ancestor = min(min_ancestor, node.val)
            if node.left:
                stack.append((node.left, new_max_ancestor, new_min_ancestor))
            if node.right:
                stack.append((node.right, new_max_ancestor, new_min_ancestor))
            

        
        return max_difference
