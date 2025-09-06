class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r, c):
            total = 0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    total += 1   # touches boundary
                elif grid[nr][nc] == 0:
                    total += 1   # touches water
                elif grid[nr][nc] == 1:
                    grid[nr][nc] = -1   # mark visited
                    total += dfs(nr, nc)
            return total

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = -1
                    return dfs(r, c)
