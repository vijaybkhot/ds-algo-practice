"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = defaultdict(list)
        visited = set()
        # {1,  2, 3, 4}
        # { 4: 4, 3: 3, 2: 2, 1:1}
        # ^
        # 1 <-> 2 <-> 3 <-> 4 <- >1
        # 1  <->   2  <->  3 <-> 4     <-> 1

        if not node:
            return None

        def dfs(node):
            new_node = Node(val=node.val)
            node_map[node] = new_node
            for nei in node.neighbors:
                if nei.val not in visited:
                    visited.add(nei.val)
                    dfs(nei)
                new_node.neighbors.append(node_map[nei])
            

        visited.add(node.val)
        dfs(node)
        return node_map[node]

