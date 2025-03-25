# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # # Recursive solution
        # output = []
        # def inOrder(root, output):
        #     if root is not None:
        #         inOrder(root.left, output)
        #         output.append(root.val)
        #         inOrder(root.right, output)
        #     return output

        # return inOrder(root, output)

        # Iterative solution
        stack = []
        output = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        
        return output
               


        