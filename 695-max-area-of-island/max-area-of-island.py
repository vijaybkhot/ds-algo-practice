class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        visited = set()

        def dfs(pos):
            i, j = pos
            if grid[i][j] == 0:
                return 0

            visited.add((i, j))
            area = 1
            
            top = (i-1, j) if i-1 > -1 else None
            bottom = (i+1, j) if i+1 < len(grid) else None
            left = (i, j-1) if j-1 > -1 else None
            right = (i, j+1) if j+1 < len(grid[0]) else None

            top_area, bottom_area, left_area, right_area = 0, 0, 0, 0
            
            if top and top not in visited:
                top_area = dfs(top)
            if bottom and bottom not in visited:
                bottom_area = dfs(bottom)
            if left and left not in visited:
                left_area = dfs(left)
            if right and right not in visited:
                right_area = dfs(right)
            
            return area + top_area + bottom_area + left_area + right_area


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs((r, c))
                    max_area = max(max_area, area)
        
        return max_area