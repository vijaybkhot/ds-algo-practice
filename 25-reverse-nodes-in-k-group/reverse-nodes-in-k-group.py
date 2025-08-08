# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode()
        dummy.next = head
        left_prev, curr = dummy, head

        while curr:    
            # make sure if k nodes are present in the remaining list
            count = 0
            temp = curr
            for _ in range(k):
                if not temp:
                    break
                count += 1
                temp = temp.next
            if count < k:
                break
            tail = curr
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            tail.next = curr
            left_prev.next = prev
            left_prev = tail
        
        return dummy.next
