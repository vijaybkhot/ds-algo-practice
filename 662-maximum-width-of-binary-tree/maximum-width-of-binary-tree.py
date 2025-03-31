# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0
        index = -1

        q = deque([[root, 0]])
        while q:
            level_length = len(q)
            _, first_index = q[0]
            _, last_index = q[-1]
            max_width = max(max_width, last_index - first_index + 1)
            for i in range(level_length):
                node, index = q.popleft()
                if node.left:
                    q.append([node.left, 2*index])
                if node.right:
                    q.append([node.right, (2*index) + 1])
        
        return max_width
