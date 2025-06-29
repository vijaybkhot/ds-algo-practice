class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # l, r = 0, len(matrix)-1
        # while l < r:
        #     for i in range(r-l):
        #         top, bottom = l, r

        #         # save topLeft
        #         topLeft = matrix[top][l+i]

        #         # Move bottomLeft into topLeft
        #         matrix[top][l+i] = matrix[bottom-i][l]

        #         # Move bottomRight into bottomLeft
        #         matrix[bottom-i][l] = matrix[bottom][r-i]

        #         # Move topRight in to bottomRight
        #         matrix[bottom][r-i] = matrix[top+i][r]

        #         # Place topLeft into topRight
        #         matrix[top+i][r] = topLeft

        #     l += 1
        #     r -= 1

        # Solution II: Transpose matrix and reverse each row
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):  # Only go above the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
        




       

        