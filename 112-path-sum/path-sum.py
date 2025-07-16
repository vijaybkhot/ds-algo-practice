# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q = deque()
        q.append((root, root.val))
        
        while q:
            curr, val = q.popleft()

            if not curr.left and not curr.right and val == targetSum:
                return True
            if curr.left:
                q.append((curr.left, curr.left.val+val))
            if curr.right:
                q.append((curr.right, curr.right.val+val))
        
        return False