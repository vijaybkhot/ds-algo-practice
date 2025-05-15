# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return True
        
        def get_max_in_tree(node):
            if not node.left and not node.right:
                return node.val
            if node.left or node.right:
                return max(node.val, get_max_in_tree(node.left)) if node.left else max(node.val, get_max_in_tree(node.right))
                
            return max(node.val, get_max_in_tree(node.left), get_max_in_tree(node.right))
        
        def get_min_in_tree(node):
            if not node.left and not node.right:
                return node.val
            if node.left or node.right:
                return min(node.val, get_min_in_tree(node.left)) if node.left else min(node.val, get_min_in_tree(node.right))
                
            return min(node.val, get_min_in_tree(node.left), get_min_in_tree(node.right))
        
        # if root.left and get_max_in_tree(root.left) >= root.val:
        #     return False
        
        # if root.right and get_min_in_tree(root.right) <= root.val:
        #     return False
        
        def inorder(node, max_val, min_val):
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False

            return (inorder(node.left, node.val, min_val) and
                    inorder(node.right, max_val, node.val))

        # Call with initial full range
        return inorder(root, float('inf'), float('-inf'))
        



        # def inorder(node):
        #     curr = node
        #     stack = []
        #     while curr or stack:
        #         while curr:
        #             stack.append(curr)
        #             curr = curr.left
        #         curr = stack.pop()
        #         arr.append(curr.val)
        #         curr = curr.right
        
                    

        inorder(root)
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        
        return True













#         # if not root:
#         #     return True
        
#         # if root.left and root.left.val >= root.val:
#         #     return False

#         # if root.right and root.right.val <= root.val:
#         #     return False        

#         # return self.isValidBST(root.left) and self.isValidBST(root.right)

#         # # Using in order traversal to create an array 
#         # def inorder(root, arr):
#         #     if root:
#         #         inorder(root.left, arr)
#         #         arr.append(root.val)
#         #         inorder(root.right, arr)
#         #     return arr
        
#         # inorder_arr = inorder(root, [])
#         # # Checking if the array is in sorted order.
#         # for i in range(1, len(inorder_arr)):
#         #     if inorder_arr[i] <= inorder_arr[i-1]:
#         #         return False
        
#         # return True

#         # # Modified inorder traversal method without the extra array. We store the previous element in a variable and check every element in the inorder path is greater than this previous element.
#         # prev = None

#         # def inorder(node):
#         #     nonlocal prev

#         #     if not node:
#         #         return True
            
#         #     # Check left subtree
#         #     if not inorder(node.left):
#         #         return False

#         #     # Check the current node val
#         #     if prev is not None and node.val <= prev:
#         #         return False
#         #     prev = node.val

#         #     # Check the right subtree
#         #     return inorder(node.right)
        
#         # return inorder(root)
            
#         # # DFS Solution
#         # def valid(node, left, right):
#         #     if not node:
#         #         return True
#         #     if not left < node.val < right:
#         #         return False
#         #     return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
#         # return valid(root, float('-inf'), float('inf'))

#         # BFS SOlution
        
#         q = deque([(root, float('-inf'), float('inf'))])

#         while q:
#             node, left, right = q.popleft()
#             if not (left < node.val < right):
#                 return False
#             if node.left:
#                 q.append((node.left, left, node.val))
            
#             if node.right:
#                 q.append((node.right, node.val, right))
        
#         return True