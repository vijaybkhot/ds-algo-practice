class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0]))
        
        heap = []
        heapq.heappush(heap, intervals[0][1])

        for start, end in intervals[1:]:
            if start > heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        
        return len(heap)