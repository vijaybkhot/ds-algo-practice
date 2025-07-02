# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        list_len = 0
        curr = head
        while curr:
            list_len += 1
            curr = curr.next
        
        k = k%list_len
        if k == 0:
            return head
        
        fast = head
        for _ in range(k):
            fast = fast.next if fast else None
            
        
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        dummy = ListNode()
        dummy.next = slow.next
        curr= slow.next
        slow.next = None

        while curr and curr.next:
            curr = curr.next
        if curr:
            curr.next = head
        return dummy.next
