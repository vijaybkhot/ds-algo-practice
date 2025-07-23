class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [float('inf')]*n
        # dp[-1] = 0
        # for i in range(n-2, -1, -1):
        #     furthest = min(i + nums[i], n - 1)
        #     for j in range(i + 1, furthest + 1):
        #         dp[i] = min(dp[i], 1 + dp[j])
        
        # return dp[0]

        # dp = {}
        # def dfs(i):
        #     if i == n-1:
        #         return 0
        #     if i in dp:
        #         return dp[i]

        #     min_jump = float('inf')
        #     max_jump = min(n-1, i+nums[i])
        #     for j in range(i+1, max_jump+1):
        #         min_jump = min(min_jump, 1+dfs(j))
            
        #     dp[i] = min_jump
        #     return min_jump
        
        # return dfs(0)

        jumps = 0
        farthest = 0
        curr_end = 0
        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest
        
        return jumps

           


