class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        valid_moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (-2, -1), (2, -1)]
        if grid[0][0] != 0:
            return False

        q = deque([(0, 0)])
        curr_move = 1
        while q:
            r, c = q.popleft()
            for dr, dc in valid_moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == curr_move:
                    q.append((nr, nc))
                    curr_move += 1
                    if curr_move == n*n:
                        return True
        
        return False
