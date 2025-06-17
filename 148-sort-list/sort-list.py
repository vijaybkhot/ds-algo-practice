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
        # # Using a heap - O(n logn) time and O(n) space complexity
        # heap = []
        # curr = head
        # while curr:
        #     heapq.heappush(heap, (curr.val, id(curr),curr))
        #     curr = curr.next
        
        # while heap:
        #     _, _, node = heapq.heappop(heap)
        #     tail.next = node
        #     tail = tail.next

        # tail.next = None

        # return dummy.next

        # Using merge sort
        def merge_sort_list(l):
            # Base case
            if not l or not l.next:
                return l
            # divide the list in half
            slow, fast = l, l
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            # Cut the list
            prev.next = None
            # # We have ou
            # l1 = merge_sort_list(l)
            # l2 = merge_sort_list(slow)
            # dummy = ListNode()
            # dummy.next = merge(merge_sort_list(l), merge_sort_list(slow))
            # return dummy.next

            return merge(merge_sort_list(l), merge_sort_list(slow))


        def merge(l1, l2):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 or l2
            return dummy.next
        
        return merge_sort_list(head)
        

