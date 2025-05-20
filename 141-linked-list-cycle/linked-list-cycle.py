# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using fast and slow pointer algo
        if not head or not head.next:
            return False
        fast, slow = head.next, head
        while fast and slow :
            fast = fast.next.next if fast.next else None
            slow = slow.next
            if fast == slow:
                return True
        
        return False