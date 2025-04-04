# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # res = root
        # q = deque([root])
        # leaf_nodes = 0
        # leaf_node = None
        # while q:
        #     leaf_nodes = len(q)
        #     if leaf_nodes == 1:
        #         leaf_node = q[-1]
        #     for _ in range(leaf_nodes):
        #         node = q.popleft()
        #         if node.left is not None and node.right is not None:
        #             leaf_node = node
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return leaf_node
        
        self.lca = None

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
            
        def dfs(node):
            left_height = height(node.left)
            right_height = height(node.right)
            if left_height == right_height:
                self.lca = node
            elif left_height > right_height:
                dfs(node.left)
            else:
                dfs(node.right)
        dfs(root)
        return self.lca
        