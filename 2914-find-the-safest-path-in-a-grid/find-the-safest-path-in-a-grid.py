class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c, 0))
                    grid[r][c] = -1
        
        while q:
            row, col, dist = q.popleft()

            for dr, dc in directions:
                nr, nc = row+dr, col+dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    grid[nr][nc] = dist+1
                    q.append((nr, nc, dist+1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -1:
                    grid[r][c] = 0
        if grid[0][0] == 0 or grid[rows-1][cols-1] == 0:
            return 0
        
        max_heap = [(-grid[0][0], 0, 0)]
        grid[0][0] = -1

        while max_heap:
            curr, row, col = heapq.heappop(max_heap)
            curr *= -1
            if row == rows-1 and col == cols-1:
                return curr
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                    heapq.heappush(max_heap, (-1*(min(curr,grid[nr][nc])), nr, nc))
                    grid[nr][nc] = -1


       