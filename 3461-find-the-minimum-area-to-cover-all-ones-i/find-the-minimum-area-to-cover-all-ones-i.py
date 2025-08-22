class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
        def dfs(grid):
            if len(grid) == 1 and len(grid[0]) == 1:
                return grid[0][0]
            
            rows, cols = len(grid), len(grid[0])

            row_0_has_1 = False
            row_last_has_1 = False
            col_0_has_1 = False
            col_last_has_1 = False
            for c in range(cols):
                if row_0_has_1 and row_last_has_1:
                    break
                if grid[0][c] == 1:
                    row_0_has_1 = True
                if grid[rows-1][c] == 1:
                    row_last_has_1 = True
            
            for r in range(rows):
                if col_0_has_1 and col_last_has_1:
                    break
                if grid[r][0] == 1:
                    col_0_has_1 = True
                if grid[r][cols-1] == 1:
                    col_last_has_1 = True
            if row_0_has_1 and row_last_has_1 and col_0_has_1 and col_last_has_1:
                return rows*cols
            else:
                new_grid = []
                for r in range(rows):
                    if (not row_0_has_1 and r == 0) or (not row_last_has_1 and r == rows-1):
                        continue
                    curr_row = grid[r][::]
                    if not col_0_has_1:
                        curr_row = curr_row[1:]
                    if not col_last_has_1:
                        curr_row = curr_row[:-1]
                    
                    new_grid.append(curr_row)
                
                return dfs(new_grid)
        
        return dfs(grid)



            
            