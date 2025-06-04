# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy

        def count_nodes(list_head: Optional[ListNode]):
            curr = list_head
            count = 0
            while curr:
                count += 1
                curr = curr.next
            return count

        def reverse_k(list_head: Optional[ListNode], prev: Optional[ListNode], num_nodes: int):
            curr = list_head
            tail = ListNode()
            tail.next = curr
            new_prev = None
            while curr and num_nodes:
                num_nodes -= 1
                nxt = curr.next
                curr.next = new_prev
                new_prev = curr
                curr = nxt
            tail.next.next = curr
            prev.next = new_prev
            return tail.next

        while curr:
            if count_nodes(curr) < k:
                break
            prev = reverse_k(curr, prev, k)
            curr = prev.next
        
        return dummy.next




                