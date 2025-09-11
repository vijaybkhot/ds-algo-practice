class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = -1
            closed_island = True
            while q:
                row, col = q.popleft()
                if row == rows-1 or row == 0 or col == cols-1 or col == 0:
                    closed_island = False
                
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        q.append((nr, nc))
                        grid[nr][nc] = -1

            return 1 if closed_island else 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    res += bfs(r, c)
        
        return res
