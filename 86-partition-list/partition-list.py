# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head

        more = ListNode()
        tail = more
        prev, curr = dummy, head

        while curr:
            if curr.val >= x:
                more.next = curr
                more = more.next
                prev.next = curr.next
                
            else:
                prev = curr

            curr = curr.next
        
        prev.next = tail.next
        more.next = None
        return dummy.next
        
        # more -> 4 -> 3 -> 5
        #                   more
        # dummy -> 1  ->  2  ->     2
        #                           prev            curr 
