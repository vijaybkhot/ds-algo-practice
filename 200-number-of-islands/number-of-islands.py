class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(row, col):
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr, nc))
        
        num_components = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_components += 1
                    grid[r][c] == "0"
                    bfs(r, c)
        
        return num_components
                
