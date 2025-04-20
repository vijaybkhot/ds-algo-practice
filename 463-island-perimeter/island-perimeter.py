class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # # Brute force solution
        # res = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             isLeft = grid[i][j-1] if j-1 > -1 else 0
        #             isRight = grid[i][j+1] if j+1 < len(grid[0]) else 0
        #             isTop = grid[i-1][j] if i-1 > -1 else 0
        #             isBottom = grid[i+1][j] if i+1 < len(grid) else 0
        #             isLeft = 1 if not isLeft else 0
        #             isRight = 1 if not isRight else 0
        #             isTop = 1 if not isTop else 0
        #             isBottom = 1 if not isBottom else 0
        #             res += (isLeft + isRight + isTop + isBottom)

        # return res
        
        # DFS Solution
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
        
            visited.add((i, j))
            
            return dfs(i, j-1) + dfs(i, j+1) + dfs(i-1, j) + dfs(i+1, j)
        
        i, j = 0, 0
        for r in range(len(grid)):
            if i and j:
                break
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    i = r
                    j = c
                    break
        
        return dfs(i, j)
        
        