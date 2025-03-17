# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # # Using a set to identify unique nodes. O(n) time and O(n) space complexity
        # node_set = set()
        # curr = head
        # while curr:
        #     if curr in node_set:
        #         return True
        #     else:
        #         node_set.add(curr)
        #         curr = curr.next
        
        # return False

        # Floyd’s Cycle Detection Algorithm (Tortoise and Hare). Fast and slow pointer
        tortoise, hare = head, head
        while True:
            tortoise = tortoise.next if tortoise else None
            hare = hare.next.next if hare and hare.next else None
            if not hare or not tortoise:
                return False
            if tortoise == hare:
                return True
        