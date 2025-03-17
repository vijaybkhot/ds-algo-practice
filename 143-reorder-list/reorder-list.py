# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Find the mid point of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Connect both halves of the list alternatingly
        l1 = head
        l2 = prev
        while l1 and l2:
            tmp = l1.next
            l1.next = l2
            l2 = l2.next
            l1 = l1.next
            l1.next = tmp
            l1 = l1.next
