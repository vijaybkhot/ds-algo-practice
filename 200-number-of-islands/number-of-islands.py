class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()
        def dfs(row, col):
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == '1':
                    visited.add((r, c))
                    dfs(r, c)
        
        num_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1'  and (r, c) not in visited:
                    visited.add((r, c))
                    dfs(r, c)
                    num_islands += 1
        
        return num_islands