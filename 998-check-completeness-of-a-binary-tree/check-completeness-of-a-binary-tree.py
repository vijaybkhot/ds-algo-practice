# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        h = 0
        q = deque([root])

        while q:
            missing = False
            count = 0
            for _ in range(len(q)):
                node = q.popleft()
                count += 1
                if node.right and not node.left:
                    print(1)
                    return False
                if not node.left:
                    missing = True
                if node.left:
                    if missing:
                        print(2)
                        return False
                    
                    q.append(node.left)
                if not node.right:
                    missing = True
                if node.right:
                    if missing:
                        print(3)
                        return False
                    
                    q.append(node.right)
            if q and count < 2**h:
                print(4)
                print(q)
                print(2**h)
                print(count)
                return False
            
            h += 1

        


        return True
        
