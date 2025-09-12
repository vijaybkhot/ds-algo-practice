class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def dfs(r, c, visited):
            isPossible = False

            total = 0
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0 and (nr, nc) not in visited:
                    isPossible = True
                    visited.add((nr, nc))
                    total = max(total, grid[r][c]+dfs(nr, nc, visited))
                    visited.remove((nr, nc))
            
            return total if isPossible else grid[r][c]
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    res = max(res, dfs(r, c, {(r, c)}))
        
        return res


