class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, src, 0)]
        prices = dict()

        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k:
                continue
            for nei, nei_price in graph[node]:
                if (nei, stops) not in prices or prices[(nei, stops)] > cost + nei_price:
                    prices[(nei, stops)] = cost + nei_price
                    heapq.heappush(heap, (cost + nei_price, nei, stops+1))
        
        return -1

