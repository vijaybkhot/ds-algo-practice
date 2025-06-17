class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Create a weighted edge graph with adjacency list
        graph = defaultdict(set)
        for idx, edge in enumerate(equations):
            u, v = edge
            val = values[idx]
            graph[u].add((v, val))
            graph[v].add((u, 1/val))
        

        def bfs(node, dest):
            if node not in graph or dest not in graph:
                return -1
            if node == dest:
                return 1
            
            q = deque()
            q.append((node, 1))
            visited = set()
            visited.add(node)
            while q:
                curr, curr_dist = q.popleft()
                if curr == dest:
                    return curr_dist
                
                for nei, dist in graph[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, curr_dist*dist))
            
            return -1
        
        return [bfs(u, v) for u, v in queries]


                
                
                    
                        
                    
                
                

            


















#         adj = defaultdict(list) # Map a -> list of [b, a/b]
#         for i, eq in enumerate(equations):
#             a, b = eq
#             adj[a].append((b, values[i]))
#             adj[b].append((a, 1/values[i]))
        
#         def bfs(src, target):
#             if src not in adj or target not in adj:
#                 return -1
            
#             q = deque()
#             visited = set()
#             q.append((src, 1))
#             visited.add(src)

#             while q:
#                 node, w = q.popleft()
#                 if node == target:
#                     return w
                
#                 for nei, weight in adj[node]:
#                     if nei not in visited:
#                         visited.add(nei)
#                         q.append((nei, w*weight))
            
#             return -1
        
#         return [bfs(a, b) for a, b in queries]


