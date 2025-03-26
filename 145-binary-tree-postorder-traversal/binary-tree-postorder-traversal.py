# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # # Recursive solution
        # return self.postorder(root, [])
        
        # Iterative solution
        # [Left -> Right -> Root]
        if not root:
            return []
        res = []
        stack = [root]

        # Add vals to res in the order, root -> Right -> Left
        while stack:
            # Adding root to res
            node = stack.pop()
            res.append(node.val)
            # Adding Left then Right to stack. So when we pop, the vals to res will be added in order Right -> Left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        # The final res will be in Root -> Right -> Left Order, which is exactly reverse of post order
            
        return res[::-1]
    

    # Recursive function
    def postorder(self, root, res):
        if root:
            self.postorder(root.left, res)
            self.postorder(root.right, res)
            res.append(root.val)
        
        return res
    