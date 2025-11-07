class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # Variables to check bound and traverse in 4 directions
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])

        # A set to track visited cells
        visited = set()

        # BFS function to traverse the grid for one iteration
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
                            # return true if cycle is found and the current path contains atleast 4 cells
                            return True
                        visited.add((nr, nc))
                        curr_visited.add((nr, nc))
                        q.append((nr, nc, row, col))
            # No cycle found, return False
            return False
        
        # Traverse through all cells to find cycle
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    # Return True if Cycle found
                    if bfs(r, c, grid[r][c]):
                        return True
        # Return False, cycle not found.
        return False