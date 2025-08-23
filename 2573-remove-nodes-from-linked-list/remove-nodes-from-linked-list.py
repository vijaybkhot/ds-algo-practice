# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        if not head:
            return head
        stack = []
        curr = head
        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            curr_node = curr
            stack.append(curr_node)
            curr = curr.next
            curr_node.next = None
        
        dummy.next = stack[0]
        for i in range(len(stack)-1):
            curr_node = stack[i]
            nxt_node = stack[i+1]
            curr_node.next = nxt_node
        
        return dummy.next