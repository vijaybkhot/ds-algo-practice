class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        

        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
        
        if len(q) == 0 or len(q) == n*n:
            return -1
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dist = -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1  # mark as visited (land now)
                        q.append((nr, nc))
            dist += 1
        
        return dist
