class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        @lru_cache(None)
        def dfs(r, c, direction, turns, target):
            nr, nc = r+directions[direction][0],c+directions[direction][1]
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != target:
                return 0
            
            max_step = dfs(nr, nc, direction, turns, 2-target)

            if turns:
                max_step = max(max_step, dfs(nr, nc, (direction+1)%4, False, 2-target))
            
            return 1+ max_step


        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for direction in range(4):
                        res = max(res, 1 + dfs(r, c, direction, True, 2))
        
        return res




