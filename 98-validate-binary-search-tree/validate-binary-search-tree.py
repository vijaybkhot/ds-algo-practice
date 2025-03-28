# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        
        # if root.left and root.left.val >= root.val:
        #     return False

        # if root.right and root.right.val <= root.val:
        #     return False        

        # return self.isValidBST(root.left) and self.isValidBST(root.right)

        # Using in order traversal to create an array 
        def inorder(root, arr):
            if root:
                inorder(root.left, arr)
                arr.append(root.val)
                inorder(root.right, arr)
            return arr
        
        inorder_arr = inorder(root, [])
        for i in range(1, len(inorder_arr)):
            if inorder_arr[i] <= inorder_arr[i-1]:
                return False
        
        return True