# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find mid-point of the list
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse second half of the list
        curr, prev = slow.next, None
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l1, l2 = head, prev
        while l1 and l2:
            l1_nxt = l1.next
            l2_nxt = l2.next
            l1.next = l2
            l2.next = l1_nxt
            l1 = l1_nxt
            l2 = l2_nxt
        return head


        