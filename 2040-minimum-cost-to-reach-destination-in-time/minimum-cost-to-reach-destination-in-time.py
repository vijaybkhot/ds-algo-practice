class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph = defaultdict(set)
        for u, v, time in edges:
            graph[u].add((v, time))
            graph[v].add((u, time))
        
        n = len(passingFees)
        
        # min_time[node] = smallest time at which we visited node
        min_time = [float('inf')] * n
    
        heap = []
        heapq.heappush(heap, (passingFees[0], 0, 0)) # (time, node)

        while heap:
            curr_cost, curr_time, curr_node = heapq.heappop(heap)

            if curr_time > maxTime:
                continue
            
            if curr_node == n-1:
                return curr_cost
            
            if curr_time >= min_time[curr_node]:
                continue
            min_time[curr_node] = curr_time
            
            
            for nxt_node, time in graph[curr_node]:
                nxt_time = curr_time + time
                nxt_cost = curr_cost + passingFees[nxt_node]
                if nxt_time <= maxTime:
                    heapq.heappush(heap, (nxt_cost, nxt_time, nxt_node))
        
        return -1


        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        n = len(passingFees)
        # min_time[node] = smallest time at which we visited node
        min_time = [float('inf')] * n

        # Priority Queue: (total_cost_so_far, time_so_far, node)
        heap = [(passingFees[0], 0, 0)]

        while heap:
            cost, time, node = heapq.heappop(heap)

            if time > maxTime:
                continue

            if node == n - 1:
                return cost

            if time >= min_time[node]:
                continue

            min_time[node] = time

            for nei, t in graph[node]:
                new_time = time + t
                new_cost = cost + passingFees[nei]
                if new_time <= maxTime:
                    heapq.heappush(heap, (new_cost, new_time, nei))

        return -1

                    
                    
                        

                