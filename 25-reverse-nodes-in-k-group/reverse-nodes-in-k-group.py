# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def countNodes(list_head):
            curr = list_head
            count = 0
            while list_head:
                count += 1
                list_head = list_head.next
            return count

        dummy = ListNode()
        dummy.next = head
        tail, curr = dummy, dummy.next
        node_count = countNodes(head)
        while curr:
            prev = None
            if node_count < k:
                tail.next = curr
                break
            for _ in range(k):
                if curr:
                    tmp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = tmp
                else:
                    break
        
            tail.next.next = curr
            tail.next = prev
            for _ in range(k):
                tail = tail.next
            node_count -= k

        return dummy.next
            






        



        