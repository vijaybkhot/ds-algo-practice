# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Find the insert position
        if not root:
            root = TreeNode(val)
            return root
            
        curr = root
        parent = None
        while curr:
            if val < curr.val:
                parent = curr
                curr = curr.left
            elif val > curr.val:
                parent = curr
                curr = curr.right

        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root