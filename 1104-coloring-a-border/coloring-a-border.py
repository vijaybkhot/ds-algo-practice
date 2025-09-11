class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        # Get connected component of the given cell
        connected = set()
        border = set()
        connected.add((row, col))
        orig_color = grid[row][col]

        q = deque([(row, col)])
        while q:
            r, c = q.popleft()
            has_neighbor = False
            for dr, dc in directions:
                nr, nc = r+dr,  c+ dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] != orig_color:
                        has_neighbor = True
                    elif (nr, nc) not in connected:
                        connected.add((nr, nc))
                        q.append((nr, nc))
            
            if (r == 0 or r == rows-1 or c == 0 or c == cols-1) or has_neighbor:
                border.add((r, c))
        
        for r, c in border:
            grid[r][c] = color
        
        return grid
                        
