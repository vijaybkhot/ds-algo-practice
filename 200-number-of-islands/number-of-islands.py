class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
        
        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands