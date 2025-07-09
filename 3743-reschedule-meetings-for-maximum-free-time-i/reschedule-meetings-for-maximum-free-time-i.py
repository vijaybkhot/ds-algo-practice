class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        # n = len(startTime)
        # durations = [endTime[i] - startTime[i] for i in range(n)]

        # @lru_cache(None)
        # def dfs(i, prev_end, k_left):
        #     if i == n:
        #         # Free time after last meeting
        #         return eventTime - prev_end

        #     max_gap = 0

        #     # Option 1: Don't move the meeting
        #     start = max(prev_end, startTime[i])
        #     end = start + durations[i]
        #     if end <= eventTime:
        #         gap = start - prev_end
        #         max_gap = max(max_gap, gap)
        #         max_gap = max(max_gap, dfs(i+1, end, k_left))

        #     # Option 2: Move the meeting left (if k_left > 0)
        #     if k_left > 0:
        #         earliest_start = prev_end
        #         end = earliest_start + durations[i]
        #         if end <= eventTime:
        #             gap = earliest_start - prev_end
        #             max_gap = max(max_gap, gap)
        #             max_gap = max(max_gap, dfs(i+1, end, k_left - 1))

        #     return max_gap

        # return dfs(0, 0, k)

        n = len(startTime)
        res = 0
        t = 0
        for i in range(n):
            t += endTime[i] - startTime[i]
            left = 0 if i <= k - 1 else endTime[i - k]
            right = eventTime if i == n - 1 else startTime[i + 1]
            res = max(res, right - left - t)
            if i >= k - 1:
                t -= endTime[i - k + 1] - startTime[i - k + 1]
        return res