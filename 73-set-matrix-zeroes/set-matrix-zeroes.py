class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # Move top:
                    row, col = r-1, c
                    while row >= 0:
                        if matrix[row][col] != 0:
                            matrix[row][col] = 'T'
                        row -= 1
                    
                    # Move bottom:
                    row, col = r+1, c
                    while row < rows:
                        if matrix[row][col] != 0:
                            matrix[row][col] = 'T'
                        row += 1
                    
                    # Move left:
                    row, col = r, c-1
                    while col >= 0:
                        if matrix[row][col] != 0:
                            matrix[row][col] = 'T'
                        col -= 1
                    
                    # Move right:
                    row, col = r, c+1
                    while col < cols:
                        if matrix[row][col] != 0:
                            matrix[row][col] = 'T'
                        col += 1

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "T":
                    matrix[r][c] = 0
        