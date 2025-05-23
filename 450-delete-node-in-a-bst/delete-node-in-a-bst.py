# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Recursive
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                return None
            elif (root.left and not root.right) or (root.right and not root.left):
                return root.left if root.left else root.right
            # node to delete has both children:
            # Find successor
            succ = root.right
            while succ.left:
                succ = succ.left
    
            root.right = self.deleteNode(root.right, succ.val)
            root.val = succ.val
        return root












#         # Iterative approach
#         # Search the node
#         curr, parent = root, None
#         while curr and curr.val != key:
#             parent = curr
#             if curr.val > key:
#                 curr = curr.left
#             elif curr.val < key:
#                 curr = curr.right

#         if not curr:
#             return root
        
#         if not curr.right and not curr.left:
#             if not parent:
#                 return None
#             if key < parent.val:
#                 parent.left = None
#             elif key > parent.val:
#                 parent.right = None
#             return root
#         elif not curr.right:
#             if not parent:
#                 return curr.left
#             if key < parent.val:
#                 parent.left = curr.left
#             elif key > parent.val:
#                 parent.right = curr.left
#             return root
#         elif not curr.left:
#             if not parent:
#                 return curr.right
#             if key < parent.val:
#                 parent.left = curr.right
#             elif key > parent.val:
#                 parent.right = curr.right
#             return root
#         else:
#             node_to_delete = curr
#             successor, successor_parent = curr.right, curr
#             while successor.left:
#                 successor_parent = successor
#                 successor = successor.left
#             node_to_delete.val = successor.val

#             if successor_parent.left == successor:
#                 successor_parent.left = successor.right
#             else:
#                 successor_parent.right = successor.right
        
#         return root


        








# #         # # Iterative Solution
# #         # def search(root, key):
# #         #     curr, parent = root, None
# #         #     while curr:
# #         #         if key < curr.val:
# #         #             parent = curr
# #         #             curr = curr.left
# #         #         elif key > curr.val:
# #         #             parent = curr
# #         #             curr = curr.right
# #         #         else:
# #         #             return curr, parent
# #         #     return None, None

# #         # curr, parent = search(root, key)
        
# #         # # Key not found in BST
# #         # if curr is None:
# #         #     return root
        
        
# #         # # Key found in BST: Delete the key node i.e. curr
# #         # # Case 1: If curr has no children (leaf node)
# #         # if curr.left is None and curr.right is None:
# #         #     if parent is None:
# #         #         return None
# #         #     if parent.left == curr:
# #         #         parent.left = None
# #         #     else:
# #         #         parent.right = None
# #         #     return root
# #         # # Case 2: If curr has only one child
# #         # if curr.left is None or curr.right is None:
# #         #     child = curr.left if curr.left else curr.right
# #         #     if parent is None:  # If the root is being deleted and has one child
# #         #         return child
# #         #     if parent.left == curr:
# #         #         parent.left = child
# #         #     else:
# #         #         parent.right = child
# #         #     return root

# #         # # Case 3: If curr has both children, find inorder successor
# #         # node_to_delete = curr
# #         # successor, successor_parent = curr.right, curr
# #         # while successor.left:
# #         #     successor_parent = successor
# #         #     successor = successor.left

# #         # # Replace value of node_to_delete with inorder successor's value
# #         # node_to_delete.val = successor.val

# #         # # Remove successor node

# #         # if successor_parent.left == successor:
# #         #     successor_parent.left = successor.right
# #         # else:
# #         #     successor_parent.right = successor.right
        
# #         # return root

# #         # Recursive solution
# #         if not root:
# #             return None
# #         if key < root.val:
# #             root.left = self.deleteNode(root.left, key)
# #         elif key > root.val:
# #             root.right = self.deleteNode(root.right, key)
# #         else:
# #             # Case 1 & 2: Node has one or no children
# #             if not root.left:
# #                 return root.right  # If left child is None, return right child
# #             elif not root.right:
# #                 return root.left  # If right child is None, return left child

# #             # Case 3: Node has two children
# #             successor = root.right
# #             while successor.left:
# #                 successor = successor.left  # Find inorder successor

# #             root.val = successor.val  # Replace node's value with successor's value
# #             root.right = self.deleteNode(root.right, successor.val)  # Delete successor

# #         return root  # Return the updated root