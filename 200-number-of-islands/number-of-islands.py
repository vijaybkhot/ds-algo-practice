class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])

        self.parent = {}
        self.rank = {}
        self.count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    idx = r*n + c
                    self.parent[idx] = idx
                    self.rank[idx] = 0
                    self.count += 1
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False
        
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx]  += 1
        
        self.count -= 1
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1)]

        uf = UnionFind(grid)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    curr = r*(cols) + c
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            uf.union(curr, nr*cols + nc)
        
        return uf.count

        # def bfs(r, c):
        #     q = deque([(r, c)])
        #     grid[r][c] = 0

        #     while q:
        #         row, col = q.popleft()

        #         for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        #             nr, nc = row+dr, col+dc
        #             if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
        #                 grid[nr][nc] = "0"
        #                 q.append((nr, nc))
        
        # num_islands = 0
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             bfs(r, c)
        #             num_islands += 1
        
        # return num_islands