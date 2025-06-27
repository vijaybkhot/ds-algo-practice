class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        indexed_queries = [(query, idx)for idx, query in enumerate(queries)]
        indexed_queries.sort()
        heap = []
        res = [0]*len(queries)
        i = 0
        for query, idx in indexed_queries:
            while i < len(items) and items[i][0] <= query:
                price, beauty = items[i]
                heapq.heappush(heap, (-beauty))
                i += 1
            
            max_beauty = -heap[0] if heap else 0
            res[idx] = max_beauty
        
        return res

        