# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        
        def dfs(node, q):
            if not node:
                return None

            q.append(node.val)            
            
            curr_sum = 0
            for j in range(len(q)-1, -1, -1):
                curr_sum += q[j]
                if curr_sum == targetSum:
                    self.count += 1

            dfs(node.left, q)
            dfs(node.right, q)
            if q:
                q.pop()
        
        dfs(root, deque([]))
        return self.count

            

