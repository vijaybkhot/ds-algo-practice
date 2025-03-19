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
        # Edge case: If left and right are the same, no need to reverse
        if left == right:
            return head

        # Dummy node to handle edge cases where head might change
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy

        # Step 1: Traverse to the node just before the 'left' position
        left_node = head
        for _ in range(left - 1):
            tail = tail.next
            left_node = left_node.next
        
        # Step 2: Reverse the sublist from left to right
        right_node, prev = left_node, None
        for _ in range(right - left + 1):
            temp = right_node.next  # Store next node
            right_node.next = prev  # Reverse link
            prev = right_node  # Move prev forward
            right_node = temp  # Move current forward
        
        # Step 3: Reconnect the reversed sublist with the remaining list
        left_node.next = right_node  # Connect end of reversed list to the remaining part
        tail.next = prev  # Connect the previous part to the reversed sublist

        # Return the updated list
        return dummy.next
            




        
        