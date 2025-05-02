class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}


        def dfs(src, curr_time):
            if curr_time >= dist[src]:
                return
            dist[src] = curr_time
            for nei, nei_time in graph[src]:
                dfs(nei, curr_time+nei_time)
                    
        
        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1
            
