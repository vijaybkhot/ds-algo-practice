class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Shortest path using Djikstras algorithm
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # (price, node, stops)
        heap = [(0, src, 0)]

        # Best price to reach a node with <= stops
        prices = dict()

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost

            if stops > k:
                continue

            for nei, price in graph[node]:
                if (nei, stops) not in prices or cost + price < prices[(nei, stops)]:
                    prices[(nei, stops)] = cost + price
                    heapq.heappush(heap, (cost + price, nei, stops + 1))

        return -1
            
            