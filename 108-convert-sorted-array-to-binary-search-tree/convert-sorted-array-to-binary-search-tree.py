# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # n = len(nums)
        # root_val = nums[n//2]
        # root = TreeNode(root_val)

        # def buildTree(root, leftTree, rightTree):
        #     if not leftTree and not rightTree:
        #         return root
        #     if leftTree:
        #         n = len(leftTree)
        #         left_root_index = n//2
        #         left_root_node = TreeNode(leftTree[left_root_index])
        #         root.left = left_root_node
        #         newLeftTree = leftTree[:left_root_index]
        #         newRightTree = leftTree[left_root_index+1:] if left_root_index+1 < n else []
        #         buildTree(left_root_node, newLeftTree, newRightTree)
        #     if rightTree:
        #         n = len(rightTree)
        #         right_root_index = n // 2
        #         right_root_node = TreeNode(rightTree[right_root_index])
        #         root.right = right_root_node
        #         newLeftTree = rightTree[:right_root_index]
        #         newRightTree = rightTree[right_root_index+1:] if right_root_index+1 < n else []
        #         buildTree(right_root_node, newLeftTree, newRightTree)
        #     return root
        
        # return buildTree(root, nums[:n//2], nums[(n//2)+1:])
        # More optimal approach
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
            
        