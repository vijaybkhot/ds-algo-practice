class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        # # Brute Force approach:
        # min_interval_map = {}
        # for start, end in intervals:
        #     interval_len = end-start+1
        #     for i in range(start, end+1):
        #         if i not in min_interval_map:
        #             min_interval_map[i] = interval_len
        #         else:
        #             min_interval_map[i] = min(interval_len, min_interval_map[i])
        # return [-1 if query not in min_interval_map else min_interval_map[query] for query in queries]

        # Using min heap to store end time and the size of interval and process queries in ascending order
        intervals.sort()
        indexed_queries = [(query, idx)for idx, query in enumerate(queries)]
        indexed_queries.sort()
        heap = []
        res = [0]*len(queries)
        i = 0
        for query, idx in indexed_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(heap, (end-start+1, end))
                i += 1
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            query_min_interval = heap[0][0] if heap else -1
            res[idx] = query_min_interval
        
        return res
            

            
        