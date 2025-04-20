class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    isLeft = grid[i][j-1] if j-1 > -1 else 0
                    isRight = grid[i][j+1] if j+1 < len(grid[0]) else 0
                    isTop = grid[i-1][j] if i-1 > -1 else 0
                    isBottom = grid[i+1][j] if i+1 < len(grid) else 0
                    isLeft = 1 if not isLeft else 0
                    isRight = 1 if not isRight else 0
                    isTop = 1 if not isTop else 0
                    isBottom = 1 if not isBottom else 0
                    res += (isLeft + isRight + isTop + isBottom)

                    
                    
                # isLeft = grid[i][j-1] if j-1 > -1 else 0
                # isRight = grid[i][j+1] if j+1 < len(grid[0]) else 0
                # isTop = grid[i-1][j] if i-1 > -1 else 0
                # isBottom = grid[i+1][j] if i+1 < len(grid) else 0
                # res += (isLeft + isRight + isTop + isBottom)
        
        return res
        