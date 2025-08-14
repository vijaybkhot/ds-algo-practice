# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        stack = []
        res = []

        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            # heapq.heappush(heap, -curr.val)
            # if len(heap) > k:
            #     heapq.heappop(heap)
            res.append(curr.val)
            curr = curr.right
        
        # return -heap[0]
        return res[k-1]