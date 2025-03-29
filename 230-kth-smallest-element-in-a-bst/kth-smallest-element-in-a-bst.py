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

        # Optimized solution for follow up question. Using iterative inorder traversal

        stack = []
        smallest = 0
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            # Process leftmost node
            curr = stack.pop()
            smallest += 1
            if smallest == k:
                return curr.val
            curr = curr.right
            
            

        