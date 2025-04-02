# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        arr = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                if node.left and node.left.val in to_delete:
                    node.left = None
                if node.right and node.right.val in to_delete:
                    node.right = None
                
                if node.val in to_delete:
                    if node.left:
                        arr.append(node.left)
                    if node.right:
                        arr.append(node.right)

        
        dfs(root)
        if root.val not in to_delete:
            arr.append(root)
        return arr           
            
            

        