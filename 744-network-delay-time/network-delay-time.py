class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # # Use DFS with pruning and shortest-time tracking to simulate Dijkstra’s behavior for finding the minimum signal delay to all nodes.
        # graph = defaultdict(list)
        # for u, v, w in times:
        #     graph[u].append((v, w))
        
        # for u in graph:
        #     graph[u].sort(key=lambda x: x[1])  # Sort by weight

        # dist = {node: float("inf") for node in range(1, n + 1)}


        # def dfs(src, curr_time):
        #     if curr_time >= dist[src]:
        #         return
        #     dist[src] = curr_time
        #     for nei, nei_time in graph[src]:
        #         dfs(nei, curr_time+nei_time)
                    
        
        # dfs(k, 0)
        # res = max(dist.values())
        # return res if res < float('inf') else -1

        # # Using Djikstras algorithm
        # graph = defaultdict(list)
        # for u, v, w in times:
        #     graph[u].append((v, w))
        
        # time = {node: float("inf") for node in range(1, n + 1)}
        # time[k] = 0
        # heap = [(0, k)]

        # while heap:
        #     curr_time, node = heapq.heappop(heap)
        #     for nei, nei_time in graph[node]:
        #         new_time = curr_time + nei_time
        #         if time[nei] > new_time:
        #             time[nei] = new_time
        #             heapq.heappush(heap, (new_time, nei))
        
        # res = max(time.values())
        # return res if res < float('inf') else -1
        
        # # Using Bellman-Ford algorithm - Not as efficient as Djikstra's
        # time = {node: float('inf') for node in range(1, n+1)}
        # time[k] = 0
        
        # for i in range(n-1):
        #     for u, v, w in times:
        #         new_time = time[u] + w
        #         if new_time < time[v]:
        #             time[v] = new_time
        
        # res = max(time.values())
        # return res if res < float('inf') else -1

        # Using Floyd-Warshall algorithm
        INF = float('inf')
        dist = [[INF]*(n+1) for i in range(n+1)]

        for i in range(1, n+1):
            dist[i][i] = 0
        for u, v, w in times:
            dist[u][v] = w
        
        for mid in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if dist[i][j] > dist[i][mid]+dist[mid][j]:
                        dist[i][j] = dist[i][mid]+dist[mid][j]
        
        max_dist = max(dist[k][1:])
        return max_dist if max_dist < float('inf') else -1
                
            
