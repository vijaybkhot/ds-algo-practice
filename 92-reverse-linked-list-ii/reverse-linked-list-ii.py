# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # # Multiple pass approach
        # if left == right:
        #     return head
        # prev_count, left_node = 0, head
        # for _ in range(left-1):
        #     prev_count += 1
        #     left_node = left_node.next

        # remainder, right_node = None, left_node
        # for _ in range(right-left):
        #     right_node = right_node.next
        #     remainder = right_node.next
        
        # prev, curr = None, left_node
        # for _ in range(right - left +1):
        #     tmp = curr.next
        #     curr.next = prev
        #     if _ == 0:
        #         curr.next = remainder
        #     prev = curr
        #     curr = tmp
        
        # dummy = ListNode()
        # tail = dummy
        # tail.next = head
        
        # for _ in range(prev_count):
        #     tail = tail.next
        
        # tail.next = None
        # tail.next = prev
        # return dummy.next

        # One pass approach
        if left == right:
            return head
        
        dummy = ListNode()
        tail = dummy

        tail.next = head
        left_node = head        
        for _ in range(left-1):
            tail = tail.next
            left_node = left_node.next
        
        right_node, prev, tmp = left_node, None, None
        for _ in range(right - left + 1):
            tmp = right_node.next
            right_node.next = prev
            prev = right_node
            right_node = tmp
        left_node.next = tmp
        tail.next = prev
        return dummy.next
            
            




        
        