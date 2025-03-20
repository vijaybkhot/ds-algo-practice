# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # # Set approach. O(n+m) time and O(n) or O(m) extra space
        # node_set = set()
        # while headA or headB:
        #     if headA is not None and headA in node_set:
        #         return headA
        #     if headA is not None:
        #         node_set.add(headA)
        #     if headB is not None and headB in node_set:
        #         return headB
        #     if headB is not None:
        #         node_set.add(headB)
        #     headA = headA.next if headA else None
        #     headB = headB.next if headB else None
        
        # return None

        # Two pointer approach. O(n+m) time and O(1) extra space
        if not headA or not headB:
            return None

        ptrA, ptrB = headA, headB

        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        
        return ptrA
        