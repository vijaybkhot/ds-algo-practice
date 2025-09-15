class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1
        q = deque()
        q.append((0, 0, 1)) # (row, col, visited_cells)
        grid[0][0] = -1


        while q:
            row, col, visited_cells = q.popleft()
            if row == rows-1 and col == cols-1:
                return visited_cells
            
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    grid[nr][nc] = -1
                    q.append((nr, nc, visited_cells+1))
        
        return -1
            