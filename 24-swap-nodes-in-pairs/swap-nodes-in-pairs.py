# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        tail = dummy
        prev = tail
        tail = dummy.next
        

        while tail:
            curr_node = tail
            next_node = tail.next if tail.next else None
            temp = next_node.next if next_node else None
            if next_node:
                next_node.next = curr_node
                curr_node.next = temp
                prev.next = next_node
                prev = curr_node
                
            tail = tail.next
        
        return dummy.next