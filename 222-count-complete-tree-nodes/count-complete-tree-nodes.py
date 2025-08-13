# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 0
        next_level = True
        q = deque([root])

        while q and next_level:
            count += len(q)
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if not node.left or not node.right:
                    next_level = False
            
            if not next_level:
                count += len(q)
                break
        
        return count
                
