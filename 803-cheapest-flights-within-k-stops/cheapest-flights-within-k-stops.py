class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # # Using modified Djikstras algorithm
        # graph = defaultdict(list)
        # for u, v, w in flights:
        #     graph[u].append((v, w))

        # heap = [(0, src, 0)]
        # prices = dict()

        # while heap:
        #     cost, node, stops = heapq.heappop(heap)
        #     if node == dst:
        #         return cost
        #     if stops > k:
        #         continue
        #     for nei, nei_price in graph[node]:
        #         if (nei, stops) not in prices or prices[(nei, stops)] > cost + nei_price:
        #             prices[(nei, stops)] = cost + nei_price
        #             heapq.heappush(heap, (cost + nei_price, nei, stops+1))
        
        # return -1

        # # Using Bellman-Ford algorithm
        # prices = [float('inf')] * n
        # prices[src] = 0

        # for i in range(k+1):
        #     temp = prices[:]
        #     for u, v, w in flights:
        #         if prices[u] == float('inf'):
        #             continue
        #         if temp[v] > (prices[u] + w):
        #             temp[v] = prices[u] + w
        
        #     prices = temp
        
        # return prices[dst] if prices[dst] != float('inf') else -1
        


        graph = defaultdict(set)
        for u, v, w in flights:
            graph[u].add((v, w))
        
        heap = []
        heapq.heappush(heap, (0, src, 0)) # arrival_price, source, stops
        prices = dict() #(node, stops) : price
       

        while heap:
            price, node, stops = heapq.heappop(heap)
        
            if node == dst:
                return price
            if stops > k:
                continue

            for nei, cost in graph[node]:
                next_state = (nei, stops+1)
                next_price = price+cost
                if next_state not in prices or next_price < prices[next_state]:
                    heapq.heappush(heap, (price + cost, nei, stops + 1))
                    prices[next_state] = next_price
            
        return -1