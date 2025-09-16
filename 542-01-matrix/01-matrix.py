class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()
        visited = set()
        res = [[0]*cols for m in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))


        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()
                res[r][c] = dist
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] != 0 and (nr, nc) not in visited:
                        q.append((nr, nc, dist+1))
                        visited.add((nr, nc))
                       
            
        return res
            