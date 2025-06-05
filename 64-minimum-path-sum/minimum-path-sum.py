class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Bottom-up Dynamic programming:
        m, n = len(grid), len(grid[0])

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                bottom = float('inf') if i == m-1 else grid[i+1][j]
                right = float('inf') if j+1 >= n else grid[i][j+1]
                grid[i][j] = grid[i][j] + min(bottom, right)
                
        return grid[0][0]