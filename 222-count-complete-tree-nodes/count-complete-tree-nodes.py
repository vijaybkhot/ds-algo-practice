# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # # Using BFS approach - O(n)
        # if not root:
        #     return 0

        # q = deque([root])
        # level = 0
        # count = 0
        # while q:
        #     level_nodes = len(q)
        #     count += level_nodes
        #     expected_level_nodes = 2**level
        #     if level_nodes < expected_level_nodes:
        #         return count
        #     for _ in range(level_nodes):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        
        # return count

        if not root:
            return 0
        
        # Get left and right subtree heights
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if left_height == right_height:
            # Left subtree is perfect: 2^h - 1 nodes + 1 (root) + right subtree count
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is perfect: 2^h - 1 nodes + 1 (root) + left subtree count
            return (1 << right_height) + self.countNodes(root.left)

    def getHeight(self, node: Optional[TreeNode]) -> int:
        """Returns the height of the leftmost path (tree height)."""
        height = 0
        while node:
            height += 1
            node = node.left
        return height
        