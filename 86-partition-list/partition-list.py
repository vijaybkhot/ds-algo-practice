# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        small_dummy = ListNode()
        large_dummy = ListNode()
        small = small_dummy
        large = large_dummy
        curr = head
        
        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next
            curr = curr.next
        
        large.next = None
        small.next = large_dummy.next
        return small_dummy.next
        
        
            

        