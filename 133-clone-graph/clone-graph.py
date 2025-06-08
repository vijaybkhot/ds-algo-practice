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
        visited = set()
        graph_dict = {}

        def dfs(vertex):
            new_node = Node(val=vertex.val)
            graph_dict[vertex] = new_node
            for nei in vertex.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
                new_node.neighbors.append(graph_dict[nei])

        visited.add(node)
        dfs(node)
        return graph_dict[node]







        # # # DFS Solution
        # # old_to_new = {}
        # # def dfs(curr_node):
        # #     if curr_node in old_to_new:
        # #         return old_to_new[curr_node]
            
        # #     # Clone current Node
        # #     clone = Node(curr_node.val)
        # #     old_to_new[curr_node] = clone

        # #     # Recursively clone neighbors
        # #     for neighbor in curr_node.neighbors:
        # #         clone.neighbors.append(dfs(neighbor))
            
        # #     return clone
        
        # # return dfs(node)

        # # BFS Solution
        # old_to_new = {}
        # old_to_new[node] = Node(node.val)
        # queue = deque()
        # queue.append(node)

        # while queue:
        #     curr_node = queue.popleft()

        #     for neighbor in curr_node.neighbors:
        #         if neighbor not in old_to_new:
        #             old_to_new[neighbor] = Node(neighbor.val)
        #             queue.append(neighbor)
        #         # Append the clone neighbor to the neighbors list of the clone of the current node
        #         old_to_new[curr_node].neighbors.append(old_to_new[neighbor])
        
        # return old_to_new[node]