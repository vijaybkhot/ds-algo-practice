# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        # def serialize(root):
        #     if root == None:
        #         return "$#"

        #     return ("$" + str(root.val) + serialize(root.left) + serialize(root.right))  

        # res= []
        # subtree_map = {}
        # res_set = set()
        # q = deque([root])
        # while q:
        #     level_length = len(q)
        #     for _ in range(level_length):
        #         node = q.popleft()
        #         curr_tree = serialize(node)
        #         if curr_tree not in subtree_map:
        #             subtree_map[curr_tree] = 1
        #         else:
        #             subtree_map[curr_tree] += 1
        #             if curr_tree not in res_set:
        #                 res.append(node)
        #                 res_set.add(curr_tree)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        
        # return res

        # Optimized approach:

        subtree_map = defaultdict(int)  # Stores serialized subtree -> count
        res = []

        def serialize(node):
            if not node:
                return "#"
            
            serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            subtree_map[serial] += 1
            
            # If we have seen this serialized subtree exactly twice, add it to results
            if subtree_map[serial] == 2:
                res.append(node)
            
            return serial
        
        serialize(root)
        return res
        