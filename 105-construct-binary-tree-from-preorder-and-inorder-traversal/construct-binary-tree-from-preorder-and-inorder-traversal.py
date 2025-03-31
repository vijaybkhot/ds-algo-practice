# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_idx = 0
        inorder_map = {num:index for index, num in enumerate(inorder)}
        
        def dfs(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            inorder_index = inorder_map[root_val]
            root.left = dfs(left, inorder_index - 1)
            root.right = dfs(inorder_index + 1, right)

            return root
        return dfs(0, len(preorder)-1)


        


        