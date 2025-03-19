# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        prev = tail
        tail = tail.next
        while tail:
            if tail.next and tail.val == tail.next.val:
                duplicate_val = tail.val
                while tail and tail.val == duplicate_val:
                    tail = tail.next
    
                prev.next = tail
            else:
                prev = tail
                tail = tail.next
        
        return dummy.next

        