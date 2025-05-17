# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def remove_leaf(node, target):
            # if not node.right and not node.left:
            #     if node.val == target:
            #         return None
            #     else:
            #         return root
            if node.left:
                node.left = remove_leaf(node.left, target)
            if node.right:
                node.right = remove_leaf(node.right, target)
            if not node.left and not node.right and node.val == target:
                return None
            else:
                return node
        
        return remove_leaf(root, target)
            




        






#         # # This method only delete the leaf nodes at first instance. Not the subsequent possible target leaf nodes
#         # def deleteNode(root, key):
#         #     if root.left is None and root.right is None and root.val == key:
#         #         return None
#         #     else:
#         #         if root.left:
#         #             root.left = deleteNode(root.left, key)
#         #         if root.right:
#         #             root.right = deleteNode(root.right, key)
#         #     return root
        
#         # return deleteNode(root, target)

#         # Using post order traversal
#         def dfs(root, key):
#             if root:
#                 dfs(root.left, key)
#                 dfs(root.right, key)
#                 if root.left and root.left.left is None and root.left.right is None and root.left.val == key:
#                     root.left = None
#                 if root.right and root.right.left is None and root.right.right is None and root.right.val == key:
#                     root.right = None
#             return root
        
#         new_tree = dfs(root, target)
#         if new_tree.left is None and new_tree.right is None and new_tree.val == target:
#             return None
#         return new_tree