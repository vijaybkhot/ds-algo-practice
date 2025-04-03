    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
class Solution:
        def flatten(self, root: Optional[TreeNode]) -> None:
            """
            Do not return anything, modify root in-place instead.
            """
            # # Recursive DFS Approach:
            # def dfs(node):
            #     if node is None:
            #         return None
            #     if node.left:
            #         left_tree = node.left
            #         right_tree = node.right
            #         node.left = None
            #         node.right = dfs(left_tree)
            #         if node.right:
            #             curr = node.right
            #             while curr.right:
            #                 curr = curr.right
            #             curr.right = dfs(right_tree)
            #     elif node.right:
            #         node.right = dfs(node.right)
            #     return node
                        
            # dfs(root)

            if root is None:
                return None
            if root.left:
                left_tree = root.left
                right_tree = root.right
                root.left = None
                root.right = self.flatten(left_tree)
                if root.right:
                    curr = root.right
                    while curr.right:
                        curr = curr.right
                    curr.right = self.flatten(right_tree)
            elif root.right:
                root.right = self.flatten(root.right)
            
            return root



            # # Iterative approach - More space optimal because no stack calls
            # curr = root
            # while curr:
            #     if curr.left:
            #         pre = curr.left
            #         while pre.right:
            #             pre = pre.right
            #         pre.right = curr.right
            #         curr.right = curr.left
            #         curr.left = None
            #     curr = curr.right
            