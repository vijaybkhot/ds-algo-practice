# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        # BFS Approach
        res = []
        q = deque([(root, str(root.val))])

        while q:
            level_length = len(q)
            for _ in range(level_length):
                node, curr_path = q.popleft()
                if node.left:
                    q.append((node.left, curr_path + "->" + str(node.left.val)))
                if node.right:
                    q.append((node.right, curr_path + "->" + str(node.right.val)))
                if node.left is None and node.right is None:
                    res.append(curr_path)
        return res


        
        