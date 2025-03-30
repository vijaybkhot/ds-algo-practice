# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def search(root, key):
            curr, parent = root, None
            while curr:
                if key < curr.val:
                    parent = curr
                    curr = curr.left
                elif key > curr.val:
                    parent = curr
                    curr = curr.right
                else:
                    return curr, parent
            return None, None

        curr, parent = search(root, key)
        
        # Key not found in BST
        if curr is None:
            return root
        
        
        # Key found in BST: Delete the key node i.e. curr
        # Case 1: If curr has no children (leaf node)
        if curr.left is None and curr.right is None:
            if parent is None:
                return None
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
            return root
        # Case 2: If curr has only one child
        if curr.left is None or curr.right is None:
            child = curr.left if curr.left else curr.right
            if parent is None:  # If the root is being deleted and has one child
                return child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child
            return root

        # Case 3: If curr has both children, find inorder successor
        node_to_delete = curr
        successor, successor_parent = curr.right, curr
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # Replace value of node_to_delete with inorder successor's value
        node_to_delete.val = successor.val

        # Remove successor node

        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right
        
        return root
            

        

        
        
        