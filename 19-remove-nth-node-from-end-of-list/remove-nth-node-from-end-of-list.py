# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # if not head:
        #     return []
        # if not head.next and n == 1:
        #     return None

        # tail = ListNode()
        # tail.next = head
        # count = 0
        # curr = head
        # while curr:
        #     count += 1
        #     curr = curr.next
        # first_half = count - n
        # curr, prev = head, tail
        # for _ in range(first_half):
        #     prev = curr
        #     curr = curr.next

        # prev.next = curr.next
        # curr.next = None
        # return tail.next

        if not head:
            return []
        if not head.next and n == 1:
            return None
        
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        deleted_node = slow.next
        slow.next = slow.next.next
        deleted_node.next = None
        return head

        
        