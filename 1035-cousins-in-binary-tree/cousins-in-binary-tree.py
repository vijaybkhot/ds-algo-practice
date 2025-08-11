# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        level = 1
        q = deque([root])
        level_x = 0
        parent_x = None
        level_y = 0
        parent_y = None

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    if node.left.val == x:
                        level_x = level + 1
                        parent_x = node
                    
                    if node.left.val == y:
                        level_y = level + 1
                        parent_y = node

                    q.append(node.left)
                if node.right:
                    if node.right.val == x:
                        level_x = level + 1
                        parent_x = node
                    
                    if node.right.val == y:
                        level_y = level + 1
                        parent_y = node

                    q.append(node.right)
            
            if level_x != 0 and level_y != 0:
                break
            level += 1

        return level_x == level_y and parent_x.val != parent_y.val               
