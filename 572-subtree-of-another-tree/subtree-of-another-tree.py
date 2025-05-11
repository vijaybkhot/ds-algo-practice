# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # def isSameTree(p, q):
        #     if not p and not q:
        #         return True
        #     if p and not q or q and not p:
        #         return False
        #     if p.val != q.val:
        #         return False
        #     return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        # if not root and subRoot:
        #     return False

        # if not subRoot:
        #     return False
        
        # if isSameTree(root, subRoot):
        #     return True

        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        # Serialize
        def serialize(root):
            if root == None:
                return "$#"

            return ("$" + str(root.val) + serialize(root.left) + serialize(root.right))  

        return serialize(subRoot) in serialize(root)

        












#         # # Recursively checking with helper function isSameTree: O(N*M) time complexity
#         # def isSameTree(p, q):
#         #     if (p and not q) or (q and not p):
#         #         return False
#         #     if not p and not q:
#         #         return True
            
#         #     if p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
#         #         return True
            
#         #     return False


#         # if (not root and subRoot):
#         #     return False

#         # if not subRoot:
#         #     return True
        
#         # if isSameTree(root, subRoot):
#         #     return True
        
        
#         # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

#         # Optimized approach using serialization of Tree: O(N+M) time complexity

#         def serialize(root):
#             if root == None:
#                 return "$#"

#             return ("$" + str(root.val) + serialize(root.left) + serialize(root.right))  

        
#         root_str = serialize(root)
#         sub_root_str = serialize(subRoot)

#         return sub_root_str in root_str
        
    
        