class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        # graph = defaultdict(set)
        # for u, v, time in edges:
        #     graph[u].add((v, time))
        #     graph[v].add((u, time))
        
        # n = len(passingFees)
        # costs = [float('inf')]*n
        # costs[0] = passingFees[0]
        # times = [float('inf')]*n
        # times[0] = 0
    
        # heap = []
        # heapq.heappush(heap, (0, passingFees[0], 0)) # (time, node)
        # min_cost = float('inf')

        # while heap:
        #     curr_time, curr_cost, curr_node = heapq.heappop(heap)

        #     if curr_time > maxTime:
        #         continue
            
        #     if curr_node == n-1:
        #         min_cost = min(min_cost, curr_cost)
            
        #     for nxt_node, time in graph[curr_node]:
        #         nxt_time = curr_time + time
        #         nxt_cost = curr_cost + passingFees[nxt_node]
        #         if nxt_time <= maxTime and nxt_cost < costs[nxt_node]:
        #             heapq.heappush(heap, (nxt_time, nxt_cost, nxt_node))
        #             times[nxt_node] = nxt_time
        #             costs[nxt_node] = nxt_cost
        
        # return min_cost if min_cost != float('inf') else -1


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

                    
                    
                        

                