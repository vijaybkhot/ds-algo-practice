class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
        min = 0
        first_node = True
        while q:
            if first_node:
                first_node = False
                min -= 1

            min += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r, c = row+dr, col+dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        
        return min


        