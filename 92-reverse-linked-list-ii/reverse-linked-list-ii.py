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

        # while curr and count != left:
        #     prev = curr
        #     curr = curr.next
        #     count += 1
        
        # tail1 = prev
        # head2 = curr
        # prev = None

        # while curr and count != right:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        #     count += 1

        # if curr:
        #     head3 = curr.next
        #     curr.next = prev
        # if tail1:
        #     tail1.next = curr
        # if head2:
        #     head2.next = head3

        # return dummy.next

        # More readable solution
        for _ in range(left-1):
            prev = prev.next
        
        # `start` is the first node to reverse
        start = prev.next
        then = start.next

        for _ in range(right-left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next
        
        
