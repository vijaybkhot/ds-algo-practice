class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
               

        # # Bottom-up DP
        # for i in range(m - 1 if m > 1 else 0, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if i == m-1 and j == n-1:
        #             obstacleGrid[i][j] = 1
        #         else:
        #             right = obstacleGrid[i][j + 1] if (j + 1 < n and obstacleGrid[i][j + 1] != -1) else 0
        #             bottom = obstacleGrid[i + 1][j] if (i + 1 < m and obstacleGrid[i + 1][j] != -1) else 0
        #             obstacleGrid[i][j] = right + bottom if obstacleGrid[i][j] != -1 else 0
        # return obstacleGrid[0][0]

        # Top-down DP - Recursion with caching
        dp = {}
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]

            if obstacleGrid[i][j] == -1:
                obstacleGrid[i][j] = 0
            else:
                right = dfs(i, j+1) if (j+1 < n) else 0
                bottom = dfs(i+1, j) if (i+1 < m) else 0
                obstacleGrid[i][j] = right + bottom
            dp[(i, j)] = obstacleGrid[i][j]
            return obstacleGrid[i][j]

        return dfs(0, 0)
