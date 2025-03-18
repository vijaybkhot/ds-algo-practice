# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # # Two-pass approach
        # curr = head
        # list_len = 0
        # while curr:
        #     list_len += 1
        #     curr = curr.next
        
        # curr_len = 0
        # prev, curr = None, head

        # dummy = ListNode()
        # tail = dummy
        # tail.next = head
        # while tail:
        #     if curr_len == list_len - n:
        #         tmp = tail.next.next
        #         node_to_delete = tail.next
        #         tail.next = tmp
        #         node_to_delete.next = None
        #         tail = tail.next
        #         curr_len += 1
        #     else:
        #         tail = tail.next
        #         curr_len += 1

        # return dummy.next

        # One-pass approach
        # Edge case: if the list only has one element
        if not head:
            return None
        
        fast, slow = head, head
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Edge case: if we need to remove the head node
        if not fast:
            return head.next
        
        # Move both pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        return head