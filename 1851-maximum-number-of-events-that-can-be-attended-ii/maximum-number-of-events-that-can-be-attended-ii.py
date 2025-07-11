class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        # start_day = min(start for start, _, _ in events)
        # end_day = max(end for _, end, _ in events)
        # k_heap = []
        # eligible_events = []
        # curr_end = 0
        
        # i = 0
        # for day in range(start_day, end_day+1):
        #     while i < len(events) and events[i][0] <= day:
        #         start, end, val = events[i]
        #         heapq.heappush(eligible_events, (end, -val))
            
        #     while eligible_events and eligible_events[0][0] < day:
        #         heapq.heappop(eligible_events)
        #     if k_heap and 
        #     heapq.heappush()

        # def find_next_event(idx, start):
        #     left, right = idx, len(events)
            
        #     while left < right:
        #         mid = (left + right) // 2
        #         if events[mid][0] < start:
        #             left = mid + 1
        #         else:
        #             right = mid

        #     # Now, left == right
        #     # Check if within bounds and meets condition
        #     if left < len(events) and events[left][0] >= start:
        #         return left
        #     else:
        #         return -1

        # dp = {}
        # # Assume events is sorted by start time
        # start_times = [event[0] for event in events]
        # def dfs(i, count):
        #     if (i, count) in dp:
        #         return dp[(i, count)]
        #     if i == len(events) or count == k:
        #         return 0
            
        #     # include and find next event idx
        #     # next_idx = find_next_event(i+1, events[i][1]+1)
        #     next_idx = bisect_right(start_times, events[i][1])
        #     if next_idx > -1:
        #         include = events[i][2] + dfs(next_idx, count+1)
        #     else:
        #         include = events[i][2]

        #     # exclude and move to next idx
        #     exclude = dfs(i+1, count)

        #     dp[(i, count)] = max(include, exclude)
        #     return dp[(i, count)]

        # return dfs(0, 0)

        events.sort()
        n = len(events)
        starts = [start for start, end, value in events]
        next_indices = [bisect_right(starts, events[cur_index][1]) for cur_index in range(n)]
        dp = [[-1] * n for _ in range(k)]
        
        def dfs(cur_index, count):
            if count == k or cur_index == n:
                return 0
            if dp[count][cur_index] != -1:
                return dp[count][cur_index]
            next_index = next_indices[cur_index]
            dp[count][cur_index] = max(dfs(cur_index + 1, count), events[cur_index][2] + dfs(next_index, count + 1))
            return dp[count][cur_index]
        
        return dfs(0, 0)