"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        list_map = {}

        while curr:
            list_map[curr] = ListNode(val=curr.val)
            curr = curr.next
        curr = head
        while curr:
            node = list_map[curr]
            node.next = list_map[curr.next] if curr.next else None
            node.random = list_map[curr.random] if curr.random else None
            curr = curr.next
        
        return list_map[head]

        