# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # # Brute Force approach - O(N*k) time complexity 
        # dummy = ListNode()
        # curr = dummy

        # def countListLen(head):
        #     node = head
        #     count = 0
        #     while node:
        #         count += 1
        #         node = node.next
        #     return count
        
        # listsLen = list(map(lambda lst: countListLen(lst), lists))
        # sum_len = sum(listsLen) if listsLen else 0
        # for i in range(sum_len):
        #     min_val = float('infinity')
        #     min_node = None
        #     # Get the minimum value node from all heads
        #     for j in range(len(lists)):
        #         if lists[j] and lists[j].val < min_val:
        #             min_val = lists[j].val
        #             min_node = j
        #     curr.next = lists[min_node]
        #     curr = curr.next
        #     lists[min_node] = lists[min_node].next
        
        # curr.next = None
        # return dummy.next

        # Optimized approach
        # Edge cases
        if len(lists) == 0 or not lists:
            return None

        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            
            if list1:
                tail.next = list1
    
            if list2:
                tail.next = list2
            
            return dummy.next
        
        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merged_list.append(mergeTwoLists(list1, list2))
            lists = merged_list
        
        return lists[0]


            
                


                


        