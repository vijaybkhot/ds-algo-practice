# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # # Iterative solution
        # if not root:
        #     return None
        
        # curr = root
        # stack = []
        # res = float('inf')
        # prev = None

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left

        #     curr = stack.pop()
        #     if prev is not None:
        #         res = min(res, abs(curr.val - prev.val))

        #     prev = curr
        #     curr = curr.right
        
        # return res

        # Recursive solution
        self.prev = None
        self.res = float('inf')

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            if self.prev is not None:
                self.res = min(self.res, abs(node.val - self.prev))
            
            self.prev = node.val  
            
            inorder(node.right)

        inorder(root)
        return self.res
        
            

        