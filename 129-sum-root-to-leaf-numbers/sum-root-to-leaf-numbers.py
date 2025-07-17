# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0

        q = deque()
        q.append((root, root.val))

        while q:
            node, curr_sum = q.popleft()
            if not node.right and not node.left:
                res += curr_sum
            if node.left:
                q.append((node.left, (curr_sum*10)+node.left.val))
            
            if node.right:
                q.append((node.right, (curr_sum*10)+node.right.val))
        return res