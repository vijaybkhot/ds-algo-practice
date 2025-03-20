# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # Find the middle node
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        
        # Get the last part reversed
        right = slow
        prev = None
        while right:
            tmp = right.next
            right.next = prev
            prev = right
            right = tmp
        
        left, right = head, prev
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        
        return True

        

