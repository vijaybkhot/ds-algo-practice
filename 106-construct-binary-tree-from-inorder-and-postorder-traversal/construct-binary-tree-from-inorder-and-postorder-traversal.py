# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return []
        
        self.post_idx = len(postorder)-1
        inorder_map = {val:idx for idx, val in enumerate(inorder)}

        def dfs(left, right):
            if left > right or self.post_idx < 0:
                return None
            
            root_val = postorder[self.post_idx]
            root = TreeNode(val=root_val)
            self.post_idx -= 1

            inorder_idx = inorder_map[root_val]

            root.right = dfs(inorder_idx+1, right)
            root.left = dfs(left, inorder_idx-1)
            return root
        
        return dfs(0, len(postorder)-1)
