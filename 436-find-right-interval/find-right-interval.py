class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # if len(intervals) == 1:
        #     return [-1]
        # # Using a heap - Partial correct solution
        # indexed_intervals = [(interval, idx) for idx, interval in enumerate(intervals)]
        # indexed_intervals.sort()
        # heap = []
        # heapq.heappush(heap, (indexed_intervals[0][0][1], indexed_intervals[0][1]))
        # # left_q.append(indexed_intervals[0])
        # res = [0]*len(intervals)
        # for interval, idx in (indexed_intervals[1:]):
        #     start, end = interval
        #     while heap and heap[0][0]<= start:
        #         end, q_idx = heapq.heappop(heap)
        #         res[q_idx] = idx
        #     heapq.heappush(heap, (end, idx))
        #     # left_q.append((interval, idx))
        
        # while heap:
        #     _, q_idx = heapq.heappop(heap)
        #     res[q_idx] = -1
        
        # return res

        # Using binary search to find earliest interval startin after the end of current interval
        n = len(intervals)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        res = [-1]*n
        for idx, interval in enumerate(intervals):
            end = interval[1]
            left, right = 0, len(starts)-1
            while left <= right:
                mid = (left+right) // 2
                if starts[mid][0] >= end:
                    right = mid - 1
                else:
                    left = mid + 1
            
            res[idx] = starts[left][1] if left < len(starts) else -1
        
        return res



        