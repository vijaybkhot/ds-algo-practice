# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # # Inefficient O(n) Time approach
    # def __init__(self, root: Optional[TreeNode]):
    #     self.root = root
    #     self.pointer = -1
    #     self.inorder_arr = []
    #     def inorder(node):
    #         if node:
    #             inorder(node.left)
    #             self.inorder_arr.append(node.val)
    #             inorder(node.right)
    #     inorder(root)
    #     self.size = len(self.inorder_arr)

    # def next(self) -> int:
    #     self.pointer += 1
    #     return self.inorder_arr[self.pointer]        

    # def hasNext(self) -> bool:
    #     return self.pointer < self.size - 1

    # Optimized O(h) approach
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left
            
    def next(self) -> int:
        top_node = self.stack.pop()
        if top_node.right:
            self._leftmost_inorder(top_node.right)
        return top_node.val      

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()