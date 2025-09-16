class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()
        res = [[-1]*cols for m in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    q.append((r, c))
                    res[r][c] = 0
                



        while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and res[nr][nc] == -1:
                        q.append((nr, nc))
                        res[nr][nc] = res[r][c] + 1
                       
            
        return res