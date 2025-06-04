class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # Dynamic Programming bottom-up solution
        # dp = [[0]*n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == m-1 or j == n-1:
        #             dp[i][j] = 1
        
        # for i in range(m-2, -1, -1):
        #     for j in range(n-2, -1, -1):
        #         dp[i][j] = dp[i+1][j]+dp[i][j+1]
        
        # return dp[0][0]

        # # Recursive solution
        # def dfs(i, j):
        #     if i == m-1 or j == n-1:
        #         return 1
        #     curr_total = dfs(i+1, j) + dfs(i, j+1)
        #     return curr_total
        
        # return dfs(0, 0)

        # DP top down solution
        dp = {}
        def dfs(i, j):
            if i == m-1 or j == n-1:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            curr_total = dfs(i+1, j) + dfs(i, j+1)
            dp[(i, j)] = curr_total
            return curr_total
        
        
        return dfs(0, 0)
            
