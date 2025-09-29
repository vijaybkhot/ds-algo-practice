class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        self.visited = set()

        def dfs(r, c, prev_r, prev_c, curr_char, curr_set):  
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == curr_char and (nr, nc) != (prev_r, prev_c):
                    if (nr, nc) in curr_set and len(curr_set) >= 4:
                        return True
                    else:
                        curr_set.add((nr, nc))
                        self.visited.add((nr,nc))
                        if dfs(nr, nc, r, c, curr_char, curr_set):
                            return True
            
            return False
        
        for r in range(m):
            for c in range(n):
                if (r, c) not in self.visited:
                    self.visited.add((r,c))
                    if dfs(r, c, -1, -1, grid[r][c], set()):
                        return True
        
        return False