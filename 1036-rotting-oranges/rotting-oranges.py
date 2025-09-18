class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()

        fresh_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
    
        mins = -1
        print(fresh_oranges)
        while q:
            level = len(q)
            for _ in range(level):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh_oranges -= 1
                        q.append((nr, nc))
                        grid[nr][nc] = 2
            mins += 1
        
        print(fresh_oranges)

        return -1 if fresh_oranges > 0 else max(mins, 0)

