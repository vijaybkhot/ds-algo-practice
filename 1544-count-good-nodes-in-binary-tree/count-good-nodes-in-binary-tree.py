# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # # DFS:
        # def countGoodNodes(node, val):
        #     if not node:
        #         return 0
        #     if not node.left and not node.right and node.val >= val:
        #         return 1
        #     root_count = 1 if node.val >= val else 0
        #     left_count = countGoodNodes(node.left, max(node.val, val))
        #     right_count = countGoodNodes(node.right, max(node.val, val))
        #     return root_count + left_count + right_count

        # return countGoodNodes(root, root.val)

        # BFS:
        q = deque([(root, root.val)])
        count = 0

        while q:
            for _ in range(len(q)):
                node, val = q.popleft()
                if node.val >= val:
                    count += 1
                if node.left:
                    q.append((node.left, max(val, node.val)))
                if node.right:
                    q.append((node.right, max(val, node.val)))
        return count












#         # if root is None:
#         #     return 0
#         # self.good_nodes = 0

#         # def dfs(root, max_val):
#         #     if root:
#         #         if root.val >= max_val:
#         #             self.good_nodes += 1
#         #         max_val = max(max_val, root.val)
#         #         dfs(root.left, max_val)
#         #         dfs(root.right, max_val)
        
#         # dfs(root, root.val)
#         # return self.good_nodes
        
#         # # Optimized solution - without using class variable
#         # def dfs(node, max_val):
#         #     if not node:
#         #         return 0
#         #     good = 1 if node.val >= max_val else 0
#         #     max_val = max(max_val, node.val)
#         #     return good + dfs(node.left, max_val) + dfs(node.right, max_val)

#         # return dfs(root, root.val)

#         # Using iterative dfs
#         if not root:
#             return 0
        
#         stack = [(root, root.val)]
#         good_nodes = 0
#         while stack:
#             node, max_val = stack.pop()

#             if node.val >= max_val:
#                 good_nodes += 1
#             new_max = max(max_val, node.val)
#             if node.left:
#                 stack.append((node.left, new_max))
#             if node.right:
#                 stack.append((node.right, new_max))
        
#         return good_nodes