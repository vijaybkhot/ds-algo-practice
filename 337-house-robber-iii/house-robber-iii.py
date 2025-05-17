# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        def max_rob(node):
            if not node:
                return [0, 0]
            left_money = max_rob(node.left) # [with left, without left]
            right_money = max_rob(node.right) # [with right, without right]

            with_root = node.val + left_money[1] + right_money[1]
            without_root = max(left_money) + max(right_money)

            return with_root, without_root
        
        return max(max_rob(root))









        
#         def max_rob(node):
#             if not node:
#                 return [0, 0]
            
#             leftPair = max_rob(node.left)   # [withLeft, withoutLeft]
#             rightPair = max_rob(node.right) # [withRight, withoutRight]

#             withRoot = node.val + leftPair[1] + rightPair[1]
#             withoutRoot = max(leftPair) + max(rightPair)

#             return [withRoot, withoutRoot]
        
#         return max(max_rob(root))