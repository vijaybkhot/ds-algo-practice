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
        curr = head
        list_len = 0
        while curr:
            list_len += 1
            curr = curr.next
        
        curr_len = 0
        prev, curr = None, head

        dummy = ListNode()
        tail = dummy
        tail.next = head
        while tail:
            if curr_len == list_len - n:
                tmp = tail.next.next
                node_to_delete = tail.next
                tail.next = tmp
                node_to_delete.next = None
                tail = tail.next
                curr_len += 1
            else:
                tail = tail.next
                curr_len += 1

        return dummy.next
