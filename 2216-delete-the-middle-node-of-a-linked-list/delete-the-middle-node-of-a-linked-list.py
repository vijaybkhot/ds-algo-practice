# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, slow, fast = None, head, head.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next if fast.next else None
        node_to_delete = ListNode()
        if prev and prev.next:
            node_to_delete = prev.next
            prev.next = prev.next.next
        else:
            return head.next
        
        return head
