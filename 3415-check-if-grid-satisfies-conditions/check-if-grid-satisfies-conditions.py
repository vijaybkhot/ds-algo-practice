class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, -1), (-1, 0)]

        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                for i in range(2):
                    r, c = (row + directions[i][0]), (col + directions[i][1])
                    if 0 <= r < rows and 0 <= c < cols:
                        if i == 0 and grid[r][c] == grid[row][col]:
                            return False
                        elif i == 1 and grid[r][c] != grid[row][col]:
                            return False

        return True



        