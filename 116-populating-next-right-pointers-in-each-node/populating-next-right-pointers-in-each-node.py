"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        q = deque()

        q.append(root)
        while q:
            curr_q = deque()
            for _ in range(len(q)):
                node = q.popleft()
                if q:
                    node.next = q[0]
                if node.left:
                    curr_q.append(node.left)
                if node.right:
                    curr_q.append(node.right)
            if curr_q:
                q = curr_q.copy()
        return root
