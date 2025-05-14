# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []
        while q:
            curr_level = [node.val for node in q]
            res.append(curr_level)
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res










#         if not root:
#             return []
        
#         res = []
#         q = deque([root])
#         while q:
#             curr_level_nodes = []
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 curr_level_nodes.append(node.val)
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
        
#             res.append(curr_level_nodes)

#         return res
