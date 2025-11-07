class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])

        visited = set()

        def bfs(r, c, char):
            curr_visited = set()
            nonlocal visited
            curr_visited.add((r, c))
            
            q = deque([(r, c, None, None)])

            while q:
                row, col, p_r, p_c = q.popleft()
                
                
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) != (p_r, p_c) and grid[nr][nc] == char:
                        if (nr, nc) in curr_visited and len(curr_visited) >= 4:
                            return True
                        visited.add((nr, nc))
                        curr_visited.add((nr, nc))
                        q.append((nr, nc, row, col))
            
            return False
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    if bfs(r, c, grid[r][c]):
                        return True
        
        return False