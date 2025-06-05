class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # # Bottom-up Dynamic programming:
        # m, n = len(grid), len(grid[0])
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if i == m-1 and j == n-1:
        #             continue
        #         bottom = float('inf') if i == m-1 else grid[i+1][j]
        #         right = float('inf') if j+1 >= n else grid[i][j+1]
        #         grid[i][j] = grid[i][j] + min(bottom, right)
                
        # return grid[0][0]

        # # Top-down DP: Recursion with caching
        # dp = {}
        # m, n = len(grid), len(grid[0])
        # def dfs(i, j):
        #     if i == m-1 and j == n-1:
        #         return grid[i][j]
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     bottom = float('inf') if i == m-1 else dfs(i+1, j)
        #     right = float('inf') if j+1 >= n else dfs(i, j+1)
        #     total = grid[i][j] + min(bottom, right)
        #     dp[(i, j)] = total
        #     return total
        
        # return dfs(0, 0)

        ROWS, COLS = len(grid), len(grid[0])
        dp = [float("inf")] * (COLS + 1)
        dp[COLS - 1] = 0

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[c] = grid[r][c] + min(dp[c], dp[c + 1])

        return dp[0]
                