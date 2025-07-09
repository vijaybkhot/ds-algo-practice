class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        q = deque()
        visited = set()
        q.append((0, 0, 1))
        visited.add((0, 0))

        while q:
            row, col, num_cells = q.popleft()
            if (row, col) == (n-1, n-1):
                return num_cells
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if 0 <= r < n and 0 <= c < n and (r, c) not in visited and grid[r][c] == 0:
                    q.append((r, c, num_cells+1))
                    visited.add((r,c))
        
        return -1
        
        