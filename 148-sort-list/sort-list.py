# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        

        dummy = ListNode()
        dummy.next = head
        tail = dummy
        # Using a heap
        heap = []
        curr = head
        while curr:
            heapq.heappush(heap, (curr.val, id(curr),curr))
            curr = curr.next
        
        while heap:
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

        tail.next = None

        return dummy.next