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
        if not node:
            return None
        
        old_to_new = {}
        def dfs(curr_node):
            if curr_node in old_to_new:
                return old_to_new[curr_node]
            
            # Clone current Node
            clone = Node(curr_node.val)
            old_to_new[curr_node] = clone

            # Recursively clone neighbors
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)