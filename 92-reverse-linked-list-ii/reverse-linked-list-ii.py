# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next
        
        rev_prev = None
        curr = prev.next
        tail = curr

        for _ in range(right-left+1):
            next_node = curr.next
            curr.next = rev_prev
            rev_prev = curr
            curr = next_node
        
        tail.next = curr
        prev.next = rev_prev

        return dummy.next
