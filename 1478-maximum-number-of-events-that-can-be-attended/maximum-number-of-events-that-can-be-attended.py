class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[0]))
        count = 0
        start = min(e[0] for e in events)
        end = max(e[1] for e in events)
        heap = []
        i = 0
        for day in range(start, end+1):
            
            while i < len(events) and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1
            
            while heap and heap[0]< day:
                heapq.heappop(heap)
            
            if heap:
                heapq.heappop(heap)
                count += 1
        
        return count

