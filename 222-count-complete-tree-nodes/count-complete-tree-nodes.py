# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Using BFS approach
        if not root:
            return 0
            
        q = deque([root])
        level = 0
        count = 0
        while q:
            level_nodes = len(q)
            count += level_nodes
            expected_level_nodes = 2**level
            if level_nodes < expected_level_nodes:
                return count
            for _ in range(level_nodes):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return count
        