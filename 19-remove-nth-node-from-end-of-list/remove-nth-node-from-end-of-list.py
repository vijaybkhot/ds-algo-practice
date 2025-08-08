# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head
        
        dummy = ListNode()
        dummy.next = head
        
        curr = dummy
        for _ in range(n):
            curr = curr.next
        
        tail = dummy

        while curr and curr.next:
            tail = tail.next
            curr = curr.next
        
        if tail and tail.next:
            if not tail.next.next:
                tail.next = None
            else:
                tail.next = tail.next.next
        
        return dummy.next
        

        