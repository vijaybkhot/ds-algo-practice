# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy
        while l1 or l2:
            val = 0
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            remainder = 0
            if val > 9:
                remainder = 1
                val = val % 10
            if l1 and l1.next:
                l1.next.val += remainder
            elif l2 and l2.next:
                l2.next.val += remainder
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            new_node = ListNode(val)
            tail.next = new_node
            tail = tail.next
            if l1 is None and l2 is None and remainder:
                new_node = ListNode(remainder)
                tail.next = new_node
                tail = tail.next
        
        return dummy.next

        