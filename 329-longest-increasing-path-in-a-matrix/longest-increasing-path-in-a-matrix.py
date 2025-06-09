class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # # Top-down DP: First attempt - Correct solution - 1.5hours
        # rows, cols = len(matrix), len(matrix[0])
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # dp = [[0]*cols for _ in range(rows)]
        
        # def dfs(i, j):
        #     max_from_4 = 0
        #     for dr, dc in directions:
        #         r, c = i+dr, j+dc
        #         if 0 <= r < rows and 0 <= c < cols and matrix[r][c] > matrix[i][j]:
        #             max_from_rc = dp[r][c] if dp[r][c] != 0 else dfs(r, c)
        #             max_from_4 = max(max_from_4, max_from_rc)
        #     dp[i][j] = 1+max_from_4
        #     return dp[i][j]

        # res = 1
        # for i in range(rows):
        #     for j in range(cols):
        #         if dp[i][j] == 0:
        #             dfs(i, j)
        #         res = max(res, dp[i][j])
        # return res

        # Bottom-up DP - Using Kahns Topological sorting algo
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        indegree = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                for dr, dc in directions:
                    r, c = i+dr, j+dc
                    if 0 <= r < rows and 0 <= c < cols and matrix[i][j] > matrix[r][c]:
                        indegree[i][j] += 1

        # Start with zero indegree cells
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if indegree[i][j] == 0:
                    q.append((i, j))
        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for dr, dc in directions:
                    r, c = i+dr, j+dc
                    if 0 <= r < rows and 0 <= c < cols and matrix[i][j] < matrix[r][c]:
                        indegree[r][c] -= 1
                        if indegree[r][c] == 0:
                            q.append((r, c))
        
        return level
                

