class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Counting number of connected components
        visited = set()
        def dfs(i, j):
            if grid[i][j] == "0":
                return
            visited.add((i, j))
            top = (i-1, j) if i-1 > -1 else None
            bottom = (i+1, j) if i+1 < len(grid) else None
            left = (i, j+1) if j+1 < len(grid[0]) else None
            right = (i, j-1) if j-1 > -1 else None

            if top and top not in visited:
                dfs(top[0], top[1])
            if bottom and bottom not in visited:
                dfs(bottom[0], bottom[1])
            if left and left not in visited:
                dfs(left[0], left[1])
            if right and right not in visited:
                dfs(right[0], right[1])

        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands

        