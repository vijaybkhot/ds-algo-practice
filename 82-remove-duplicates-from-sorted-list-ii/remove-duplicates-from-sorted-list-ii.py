# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = head
        prev = dummy
        while curr:
            # Check for duplicate group
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with the same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Skip the last duplicate
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next

        return dummy.next


        