# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        curr = root
        stack = []
        res = float('inf')
        prev = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if prev is not None:
                res = min(res, abs(curr.val - prev.val))

            prev = curr
            curr = curr.right
        
        return res
        
            

        