# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # BFS approach -> Not correct
        if not root or (not root.left and not root.right):
            return 0
        self.max_dia = 0
        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            self.max_dia = max(self.max_dia, left+right)
            return 1 + max(left, right)
        height(root)
        return self.max_dia
        


        



        # # q = deque([root])
        # # dia = 0
        # # level = 0
        # # while q:
        # #     if level > 0:
        # #         if len(q) > 2 ** (level-1):
        # #             dia += 2
        # #         else:
        # #             dia += 1
        # #     for i in range(len(q)):
        # #         node = q.popleft()
        # #         if node.left:
        # #             q.append(node.left)
        # #         if node.right:
        # #             q.append(node.right)
        # #     level += 1
        
        # # return dia

        # # # DFS - Recursive Approach
        # # self.maxDia = 0

        # # def height(node):
        # #     if not node:
        # #         return 0
            
        # #     left_height = height(node.left)
        # #     right_height = height(node.right)
        # #     self.maxDia = max(self.maxDia, left_height+right_height)

        # #     return 1 + max(left_height, right_height)
        
        # # height(root)
        # # return self.maxDia
        
        # self.maxDia = 0
        # def height(node):
        #     if not node:
        #         return 0
        #     left = height(node.left)
        #     right = height(node.right)
        #     self.maxDia = max(self.maxDia, left+right)
        #     return 1 + max(left, right)
    
        
        # height(root)
        # return self.maxDia











