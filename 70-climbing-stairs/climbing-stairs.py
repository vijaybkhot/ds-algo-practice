class Solution:
    def climbStairs(self, n: int) -> int:

        # # Recursion:
        # def dfs(i):
        #     if i >=n:
        #         return i == n
            
        #     return dfs(i+1) + dfs(i+2)

        ## Memoization
        # memo = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     if memo[i] != -1:
        #         return memo[i]
        #     memo[i] = dfs(i + 1) + dfs(i + 2)
        #     return memo[i]
        # return dfs(0)

        # Dynamic Programming:
        if n <= 2:
            return n
            
        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
            