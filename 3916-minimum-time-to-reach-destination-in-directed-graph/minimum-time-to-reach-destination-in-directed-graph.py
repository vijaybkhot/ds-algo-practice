class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(set)
        
        heap = []

        for u, v, s, e in edges:
            graph[u].add((v, s, e))
        
        
        distance = [float('inf')]*n
        distance[0] = 0

        heapq.heappush(heap, (0, 0))    # arrive_time, node

        while heap:
            curr_time, node = heapq.heappop(heap)
            if node == n-1:
                return curr_time
            
            if curr_time > distance[node]:
                continue

            for v, s, e in graph[node]:
                if curr_time > e:
                    continue
                # Wait if we're too early
                arrive_time = curr_time + 1 if s <= curr_time else s + 1

                if arrive_time < distance[v]:
                    distance[v] = arrive_time
                    heapq.heappush(heap, (arrive_time, v))
        
        return -1


        
        

       