# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def dfs(node):
        #     if node is not None:
        #         dfs(node.left)
        #         res.append(node.val)
        #         dfs(node.right)
        
        # dfs(root)
        # return res

        # # Iterative approach
        # curr, stack, res = root, [], []
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left

        #     curr = stack.pop()
        #     res.append(curr.val)
        #     curr = curr.right
        
        # return res
            
        curr, stack, res = root, [], []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res
            
            

        