# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        if left == right:
            return head

        dummy = ListNode()
        dummy.next = head

        count = 1
        curr, prev = head, dummy
        while curr and count != left:
            prev = curr
            curr = curr.next
            count += 1
        
        if not curr:
            return dummy.next
        
        tail1 = prev
        head2 = curr
        prev = None

        while curr and count != right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1

        if curr:
            head3 = curr.next
            curr.next = prev
        if tail1:
            tail1.next = curr
        if head2:
            head2.next = head3

        return dummy.next
        
        
