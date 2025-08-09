# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
    
        dummy = ListNode()
        dummy.next = head

        curr = head
        prev = dummy
        while curr:
            if curr.next and curr.val == curr.next.val:
                next_node = curr.next
                while next_node and next_node.val == curr.val:
                    next_node = next_node.next
                prev.next = next_node
                curr = next_node
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next
