class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs_helper(row, col):
            
            def dfs(r, c):
                nonlocal count
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = -1
                        count += 1
                        dfs(nr, nc)

            grid[row][col] = -1
            count = 1
            dfs(row, col)
            return count
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs_helper(r, c))
        
        return res

