# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # # Recursive solution
        # def preorder(root, output):
        #     if root:
        #         output.append(root.val)
        #         preorder(root.left, output)
        #         preorder(root.right, output)
        #     return output
        
        # return preorder(root, [])

        # Iterative solution
        stack = []
        output = []
        curr = root
        while curr or stack:
            if curr:
                output.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return output
        