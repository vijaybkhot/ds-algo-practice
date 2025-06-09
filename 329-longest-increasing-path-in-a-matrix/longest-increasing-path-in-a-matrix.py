class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # Bottom-up DP: First attempt - Correct solution - 1.5hours
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        dp = [[0]*cols for _ in range(rows)]
        
        def dfs(i, j):
            max_from_4 = 0
            for dr, dc in directions:
                r, c = i+dr, j+dc
                if 0 <= r < rows and 0 <= c < cols and matrix[r][c] > matrix[i][j]:
                    max_from_rc = dp[r][c] if dp[r][c] != 0 else dfs(r, c)
                    max_from_4 = max(max_from_4, max_from_rc)
            dp[i][j] = 1+max_from_4
            return dp[i][j]

        res = 1
        for i in range(rows):
            for j in range(cols):
                if dp[i][j] == 0:
                    dfs(i, j)
                res = max(res, dp[i][j])
        return res
