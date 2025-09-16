class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # q = deque()
        # res = [[-1]*cols for m in range(rows)]

        # for r in range(rows):
        #     for c in range(cols):
        #         if mat[r][c] == 0:
        #             q.append((r, c, 0))
        #             res[r][c] = 0


        # while q:
        #         r, c, dist = q.popleft()
        #         for dr, dc in directions:
        #             nr, nc = r+dr, c+dc
        #             if 0 <= nr < rows and 0 <= nc < cols and res[nr][nc] == -1:
        #                 q.append((nr, nc, dist+1))
        #                 res[nr][nc] = dist+1
                       
            
        # return res

        INF = float('inf')

        dp = [[INF] * cols for _ in range(rows)]

        # Initialize dp with 0s where mat[r][c] == 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dp[r][c] = 0

        # First pass: top-left → bottom-right
        for r in range(rows):
            for c in range(cols):
                if dp[r][c] != 0:  # skip 0s
                    if r > 0:
                        dp[r][c] = min(dp[r][c], dp[r-1][c] + 1)
                    if c > 0:
                        dp[r][c] = min(dp[r][c], dp[r][c-1] + 1)

        # Second pass: bottom-right → top-left
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if dp[r][c] != 0:
                    if r < rows-1:
                        dp[r][c] = min(dp[r][c], dp[r+1][c] + 1)
                    if c < cols-1:
                        dp[r][c] = min(dp[r][c], dp[r][c+1] + 1)

        return dp


            