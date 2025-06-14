class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # # Top-down DP solution
        # dp = {}
        # def dfs(i, j):
        #     if i == len(triangle):
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]
        #     path_sum = 0

        #     path_sum = (triangle[i][j] + dfs(i+1, j))
        #     if j+1 < len(triangle[i]):
        #         path_sum = min(path_sum, (triangle[i][j+1] + dfs(i+1, j+1)))

        #     dp[(i, j)] = path_sum
        #     return path_sum
        
        # return dfs(0, 0)

        # Bottom-up DP
        n = len(triangle)
        dp = triangle[n-1]

        for i in range(n-2, -1, -1):
            new_dp = dp[::]
            for j in range(i+1):
                new_dp[j] = min((triangle[i][j] + dp[j]), (triangle[i][j]+dp[j+1]))
            dp = new_dp

        return dp[0]        