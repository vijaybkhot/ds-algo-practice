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
        dummy = ListNode()
        curr = dummy

        def countListLen(head):
            node = head
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        listsLen = list(map(lambda lst: countListLen(lst), lists))
        max_len = sum(listsLen) if listsLen else 0
        for i in range(max_len):
            min_val = float('infinity')
            min_node = None
            # Get the minimum value node from all heads
            for j in range(len(lists)):
                if lists[j] and lists[j].val < min_val:
                    min_val = lists[j].val
                    min_node = j
            curr.next = lists[min_node]
            curr = curr.next
            lists[min_node] = lists[min_node].next
        
        curr.next = None
        return dummy.next
            
                


                


        