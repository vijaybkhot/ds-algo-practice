# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []
        node_count = 0
        curr = head
        while curr:
            node_count += 1
            curr = curr.next
        
        res = [0]*node_count

        stack = []
        curr = head
        for i in range(node_count):
            curr_num = curr.val
            while stack and stack[-1][0] < curr_num:
                num, idx = stack.pop()
                res[idx] = curr_num
            stack.append((curr_num, i))
            curr = curr.next
        
        return res
