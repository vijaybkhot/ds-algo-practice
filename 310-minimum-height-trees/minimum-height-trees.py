class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # # Brute Force appraoch:
        # graph = defaultdict(set)
        # for u, v in edges:
        #     graph[u].add(v)
        #     graph[v].add(u)
        
        # def bfs(node):
        #     q = deque()
        #     visited = set()
        #     visited.add(node)
        #     q.append(node)
        #     level = 0
        #     while q:
        #         for _ in range(len(q)):
        #             curr = q.popleft()
        #             for nei in graph[curr]:
        #                 if nei not in visited:
        #                     visited.add(nei)
        #                     q.append(nei)
        #         level += 1
        #     return level
        
        # height_map = {node: bfs(node) for node in graph}
        # min_height = min(height_map.values())
        # res = [node for node in height_map if height_map[node] == min_height]
        # return res
        
        # Kahn's algorithm by peeling off leaves
        indegree = [0]*n
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque([idx for idx, indegree in enumerate(indegree) if indegree == 1])
        remaining_nodes = n
        while remaining_nodes > 2:
            level_len = len(q)
            remaining_nodes -= level_len
            for _ in range(len(q)):
                curr = q.popleft()
                for nei in graph[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)
        
        return list(q)
        
        
        
        
        
#         # Brute Force approach - Use BFS to count height and count height for every node
#         graph = defaultdict(set)
#         indegree = [0] * n
        
#         for u, v in edges:
#             graph[u].add(v)
#             graph[v].add(u)
#             indegree[u] += 1
#             indegree[v] += 1

#         # def bfs(root):
#         #     visited = set()
#         #     q = deque()
#         #     visited.add(root)
#         #     q.append(root)
#         #     height = -1
#         #     while q:
#         #         for _ in range(len(q)):
#         #             node = q.popleft()
#         #             for nei in graph[node]:
#         #                 if nei not in visited:
#         #                     visited.add(nei)
#         #                     q.append(nei)
#         #         height += 1
#         #     return max(height, 0)
#         # height_map = defaultdict(list)
#         # min_height = 0
#         # for i in range(n):
#         #     height = bfs(i)
#         #     height_map[height].append(i)
#         #     min_height = height if min_height == 0 else min(min_height, height)
        
#         # return height_map[min_height]

#         # Using Kahn's algorithm by peeling of leaves 
#         q = deque()

#         for i in range(n):
#             if indegree[i] == 1:
#                 q.append(i)
        
#         # while max(indegree) > 1:
#         #     level_len = len(q)
#         #     for _ in range(level_len):
#         #         node = q.popleft()
#         #         for nei in graph[node]:
#         #             indegree[nei] -= 1
#         #             if indegree[nei] == 1:
#         #                 q.append(nei)

#         remaining_nodes = n
#         while remaining_nodes > 2:
#             level_len = len(q)
#             remaining_nodes -= level_len
#             for _ in range(level_len):
#                 node = q.popleft()
#                 for nei in graph[node]:
#                     indegree[nei] -= 1
#                     if indegree[nei] == 1:
#                         q.append(nei)
        
#         return (list(q) or [0])


        