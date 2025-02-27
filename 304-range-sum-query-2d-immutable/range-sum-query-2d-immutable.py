class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # # Brute force solution
        # self.matrix = matrix
        #Optimal solution
        if not matrix or not matrix[0]:
            return
        
        rows, cols = len(matrix), len(matrix[0])
        # Compute prefix sum matrix
        self.prefixSumMatrix = [[0] * (cols+1) for _ in range (rows+1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.prefixSumMatrix[r][c+1]
                self.prefixSumMatrix[r+1][c+1] = prefix + above
         

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # # Brute force solution
        # res = 0
        # for r in range(row1, row2+1):
        #     for c in range(col1, col2+1):
        #         res += self.matrix[r][c]
        # return res
        # Solution using prefix sum matrix
        row1, col1, row2, col2 = row1 + 1, col1+1, row2+1, col2+1
        bottomRight = self.prefixSumMatrix[row2][col2]
        above = self.prefixSumMatrix[row1-1][col2]
        left = self.prefixSumMatrix[row2][col1-1]
        topLeft = self.prefixSumMatrix[row1-1][col1-1]
        return bottomRight - above - left + topLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)