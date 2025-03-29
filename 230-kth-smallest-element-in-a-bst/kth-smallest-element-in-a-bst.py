# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # # Solution using inorder traversal. Uses O(n) extra space
        # def inorder(root, arr):
        #     if root:
        #         inorder(root.left, arr)
        #         arr.append(root.val)
        #         inorder(root.right, arr)
        #     return arr
        
        # sorted_bst_arr = inorder(root, [])

        # return sorted_bst_arr[k-1]

        # # Optimized solution for follow up question. Using iterative inorder traversal
        # stack = []
        # curr = root

        # while True:
        #     # Go left as much as possible
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     # Process the leftmost node
        #     curr = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return curr.val  # Found kth smallest
            
        #     # Move to the right subtree
        #     curr = curr.right

        # Recursive inorder traversal
        self.count = 0
        self.result = None

        def inorder(node):
            if node and self.result is None:
                inorder(node.left)
                self.count += 1
                if self.count == k:
                    self.result = node.val
                    return
                inorder(node.right)
            
        inorder(root)
        return self.result

        