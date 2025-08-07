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
        
        node_map = dict()

        curr = head
        while curr:
            node_map[curr] = ListNode(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            node_map[curr].next = node_map[curr.next] if curr.next in node_map else None
            node_map[curr].random = node_map[curr.random] if curr.random in node_map else None
            curr = curr.next
        
        return node_map[head]
