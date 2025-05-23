# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return []
        if not head.next and n == 1:
            return None
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        first_half = count - n
        curr, prev = head, None
        for _ in range(first_half):
            prev = curr
            curr = curr.next
        if not prev:
            return curr.next
        prev.next = curr.next if curr else None
        curr.next = None
        return head
        
        