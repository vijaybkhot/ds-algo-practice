# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # # Appraoch - I: Using a function to merge two lists and iteratively merging two lists in the lists array
        # def mergeTwoLists(l1, l2):
        #     dummy = ListNode()
        #     tail = dummy
        #     while l1 and l2:
        #         if l1.val < l2.val:
        #             tail.next = l1
        #             l1 = l1.next
        #             tail = tail.next
        #         else:
        #             tail.next = l2
        #             l2 = l2.next
        #             tail = tail.next
        #     if l1:
        #         tail.next = l1
        #     if l2:
        #         tail.next = l2
            
        #     return dummy.next
            
        # dummy = ListNode()
        # tail = dummy

        # while len(lists) > 1:
        #     merged_list = []
        #     for i in range(0, len(lists), 2):
        #         list1 = lists[i]
        #         list2 = lists[i+1] if i+1 < len(lists) else None
        #         merged_list.append(mergeTwoLists(list1, list2))
        #     lists = merged_list
        
        # return lists[0]

        # # Approach II: Counting the maximum length of a list and iterating that many number of times to merge all lists together
        # dummy = ListNode()
        # tail = dummy

        # while any(lists):
        #     # Get node with smallest value
        #     holder = ListNode()
        #     min_value = float('inf')
        #     min_val_idx = len(lists)+1
        #     for j in range(len(lists)):
        #         if lists[j] and lists[j].val < min_value:
        #             min_value = lists[j].val
        #             min_val_idx = j
        #     if min_val_idx < len(lists):
        #         tail.next = lists[min_val_idx]
        #         tail = tail.next
        #         lists[min_val_idx] = lists[min_val_idx].next
        #     else:
        #         break
        # return dummy.next

        # Approach III: Using Priority Queue
        pq = []

        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(pq, (l.val, idx))

        dummy = ListNode()
        tail = dummy
        while pq:
            val, idx = heapq.heappop(pq)
            node = lists[idx]
            if node:
                tail.next = node
                tail = tail.next
                node = node.next
                if node is not None:
                    heapq.heappush(pq, (node.val, idx))
                lists[idx] = node
        
        return dummy.next
