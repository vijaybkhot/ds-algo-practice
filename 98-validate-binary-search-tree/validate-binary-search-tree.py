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

        # # Using in order traversal to create an array 
        # def inorder(root, arr):
        #     if root:
        #         inorder(root.left, arr)
        #         arr.append(root.val)
        #         inorder(root.right, arr)
        #     return arr
        
        # inorder_arr = inorder(root, [])
        # # Checking if the array is in sorted order.
        # for i in range(1, len(inorder_arr)):
        #     if inorder_arr[i] <= inorder_arr[i-1]:
        #         return False
        
        # return True

        # # Modified inorder traversal method without the extra array. We store the previous element in a variable and check every element in the inorder path is greater than this previous element.
        # prev = None

        # def inorder(node):
        #     nonlocal prev

        #     if not node:
        #         return True
            
        #     # Check left subtree
        #     if not inorder(node.left):
        #         return False

        #     # Check the current node val
        #     if prev is not None and node.val <= prev:
        #         return False
        #     prev = node.val

        #     # Check the right subtree
        #     return inorder(node.right)
        
        # return inorder(root)
            
        # # DFS Solution
        # def valid(node, left, right):
        #     if not node:
        #         return True
        #     if not left < node.val < right:
        #         return False
        #     return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        # return valid(root, float('-inf'), float('inf'))

        # BFS SOlution
        
        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            
            if node.right:
                q.append((node.right, node.val, right))
        
        return True