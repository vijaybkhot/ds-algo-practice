# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # h = 0
        # q = deque([root])

        # while q:
        #     missing = False
        #     count = 0
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         count += 1
        #         if node.right and not node.left:
        #             return False
        #         if not node.left:
        #             missing = True
        #         if node.left:
        #             if missing:
        #                 return False
        #             q.append(node.left)
        #         if not node.right:
        #             missing = True
        #         if node.right:
        #             if missing:
        #                 return False
        #             q.append(node.right)
        #     if q and count < 2**h:
        #         return False
            
        #     h += 1

    
        # return True
        

        # Clean approach

        q = deque([root])

        found_null = False

        while q:
            node = q.popleft()
            if not node:
                found_null = True
            else:
                if found_null:
                    return False
                q.append(node.left)
                q.append(node.right)
        
        return True