# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1

        q = deque([root])
        max_sum = float('-inf')
        max_level = 1

        while q:
            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()

                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = level
            
            level += 1
        
        return max_level

