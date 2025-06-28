class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        if rows == cols:
            for r in range(rows):
                for c in range(r):
                    matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]
            return matrix

        trans_rows, trans_cols = cols, rows

        transpose = [[0]*trans_cols for _ in range(trans_rows)]
        
        for r in range(rows):
            for c in range(cols):
                transpose[c][r] = matrix[r][c]
        
        return transpose
        