class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # First attempt - O(m*n*(m+n)) time and O(1) space
        # rows, cols = len(matrix), len(matrix[0])
        # for r in range(rows):
        #     for c in range(cols):
        #         if matrix[r][c] == 0:
        #             # Move top:
        #             row, col = r-1, c
        #             while row >= 0:
        #                 if matrix[row][col] != 0:
        #                     matrix[row][col] = 'T'
        #                 row -= 1
                    
        #             # Move bottom:
        #             row, col = r+1, c
        #             while row < rows:
        #                 if matrix[row][col] != 0:
        #                     matrix[row][col] = 'T'
        #                 row += 1
                    
        #             # Move left:
        #             row, col = r, c-1
        #             while col >= 0:
        #                 if matrix[row][col] != 0:
        #                     matrix[row][col] = 'T'
        #                 col -= 1
                    
        #             # Move right:
        #             row, col = r, c+1
        #             while col < cols:
        #                 if matrix[row][col] != 0:
        #                     matrix[row][col] = 'T'
        #                 col += 1

        # for r in range(rows):
        #     for c in range(cols):
        #         if matrix[r][c] == "T":
        #             matrix[r][c] = 0
        
        # Mark the corresponding top row or left col with 0 if any cell is zero
        rows, cols = len(matrix), len(matrix[0])

        row0 = any(matrix[0][c] == 0 for c in range(cols))
        col0 = any(matrix[r][0] == 0 for r in range(rows))

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0

        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0

        if row0:
            for c in range(cols):
                matrix[0][c] = 0

        if col0:
            for r in range(rows):
                matrix[r][0] = 0