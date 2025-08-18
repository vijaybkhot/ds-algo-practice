class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)
        for u, v, w in times:
            graph[u].add((v, w))

        time = [float('inf')]*n
        heap = [(0, k)] # curr_time, node
        while heap:
            curr_time, node = heapq.heappop(heap)
            if curr_time >= time[node-1]:
                continue
            time[node-1] = curr_time
            
            for v, w in graph[node]:
                new_time = curr_time + w
                heapq.heappush(heap, (new_time, v))
        
        max_time = max(time)
        return -1 if max_time == float('inf') else max_time            
