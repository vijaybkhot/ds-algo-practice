class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #     [1,1,1,1],
            # [1,1,1,1],
            # [1,1,1,1]
            # [1,1,1,1]
                
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if matrix[r][c] == 0:
                    continue
                right = matrix[r][c+1] if (0 <= r < rows and 0 <= c+1 < cols) else 0
                bottom = matrix[r+1][c] if (0 <= r+1 < rows and 0 <= c < cols) else 0
                diag = matrix[r+1][c+1] if (0 <= r+1 < rows and 0 <= c+1 < cols) else 0

                if right and bottom and diag:
                    if right == bottom == diag:
                        matrix[r][c] = right+1
                    else:
                        matrix[r][c] = min(right, bottom, diag) + 1
        
        total = 0

        for r in range(rows):
            for c in range(cols):
                total += matrix[r][c]
        print(matrix)
        return total
                