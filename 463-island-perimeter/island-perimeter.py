class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # def dfs(r, c):
        #     total = 0
        #     for dr, dc in directions:
        #         nr, nc = r+dr, c+dc
        #         if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        #             total += 1   # touches boundary
        #         elif grid[nr][nc] == 0:
        #             total += 1   # touches water
        #         elif grid[nr][nc] == 1:
        #             grid[nr][nc] = -1   # mark visited
        #             total += dfs(nr, nc)
        #     return total
        
        def bfs(r, c):
            q = deque()
            total = 0
            q.append((r, c))
            visited = set()
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                        total += 1 
                    elif grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            
            return total



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
