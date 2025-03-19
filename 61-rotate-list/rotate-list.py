# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or head.next is None:
            return head

        dummy = ListNode()
        dummy.next = head
        tail = dummy
        list_len = 0
        while tail.next:
            list_len += 1
            tail = tail.next
        
        if k > list_len and list_len > 0:
            k = k % list_len
        
        left_section = head
        # Get last k nodes:
        start_len = list_len - k
        tail = dummy
        for _ in range(start_len):
            tail = tail.next
        left_section = dummy.next
        dummy.next = tail.next
        tail = dummy
        for _ in range(k):
            tail = tail.next
        tail.next = left_section
        for _ in range(start_len):
            tail = tail.next
        tail.next = None
        return dummy.next



        