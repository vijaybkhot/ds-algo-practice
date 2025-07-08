class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]
        n = len(jobs)
        next_indices = [bisect_left(starts, jobs[curr_index][1]) for curr_index in range(n)]

        dp = {}
        def dfs(i):
            if i == n:
                return 0
            if i in dp:
                return dp[i]
            next_idx = next_indices[i]
            include = jobs[i][2] + dfs(next_idx)
            exclude = dfs(i + 1)
            dp[i] = max(include, exclude)
            return dp[i]
        
        return dfs(0)