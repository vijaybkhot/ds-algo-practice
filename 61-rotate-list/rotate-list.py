# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Return the head if head is none or head is the only node in the list
        if not head or not head.next:
            return head

        #  Calculate the length of list
        list_len = 0
        curr = head
        while curr:
            list_len += 1
            curr = curr.next
        # Calculate the rotations if rotations exceed the length of the list
        k = k%list_len
        # If no rotations, return list
        if k == 0:
            return head
        
        # Get the pointer to the new head after rotation. It would be k nodes away from the end
        fast = head
        for _ in range(k):
            fast = fast.next if fast else None
            
    
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        # Get a dummy node to return
        dummy = ListNode()
        # Attach the slow.next which would be the start of the new LL to dummy
        dummy.next = slow.next
        curr= slow.next
        slow.next = None

        while curr and curr.next:
            curr = curr.next
    
        curr.next = head
        return dummy.next
