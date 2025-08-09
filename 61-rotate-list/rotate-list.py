# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        num_nodes = 0

        curr = head
        while curr:
            num_nodes += 1
            curr = curr.next
        
        k = k % num_nodes
        
        if k == 0:
            return head

        dummy = ListNode()
        dummy.next = head

        curr = head
        for _ in range(k):
            curr = curr.next
        
        prev = head

        while curr and curr.next:
            prev = prev.next
            curr = curr.next
        dummy.next = prev.next
        prev.next = None
        curr.next = head
        return dummy.next

       