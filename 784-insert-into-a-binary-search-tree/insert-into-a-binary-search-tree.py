# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        parent, curr = None, root
        while curr:
            parent = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        
        return root
        










#         # Find the insert position
#         # if not root:
#         #     return TreeNode(val)
            
#         # curr = root
#         # parent = None
#         # while curr:
#         #     if val < curr.val:
#         #         parent = curr
#         #         curr = curr.left
#         #     elif val > curr.val:
#         #         parent = curr
#         #         curr = curr.right

#         # if val < parent.val:
#         #     parent.left = TreeNode(val)
#         # else:
#         #     parent.right = TreeNode(val)
#         # return root

#         # More readable approach
#         if not root:
#             return TreeNode(val)
#         curr = root
#         while True:
#             if val < curr.val:
#                 if not curr.left:
#                     curr.left = TreeNode(val)
#                     break
#                 curr = curr.left
#             else:
#                 if not curr.right:
#                     curr.right = TreeNode(val)
#                     break
#                 curr = curr.right
#         return root