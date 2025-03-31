# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # def dfs_left(node, arr):
        #     if node:
        #         arr.append(node.val)
        #         if node.left and not node.right:
        #             node.right = TreeNode(float('inf'))
        #         if node.right and not node.left:
        #             node.left = TreeNode(float('inf'))

        #         dfs_left(node.left, arr)
        #         dfs_left(node.right, arr)
        #     return arr
        
        # def dfs_right(node, arr):
        #     if node:
        #         arr.append(node.val)
        #         if node.left and not node.right:
        #             node.right = TreeNode(float('inf'))
        #         if node.right and not node.left:
        #             node.left = TreeNode(float('inf'))
        #         dfs_right(node.right, arr)
        #         dfs_right(node.left, arr)
        #     return arr

        # if not root or (root.left is None and root.right is None):
        #     return True
        
        # left_subtree = dfs_left(root.left, [])
        # right_subtree = dfs_right(root.right, [])

        # return left_subtree == right_subtree

        # More optimal approach
        def isMirror(t1, t2):
            if (not t1 and t2) or (not t2 and t1):
                return False
            if not t1 and not t2:
                return True
            
            return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t2.left, t1.right)
        
        return isMirror(root.left, root.right) if root else True


