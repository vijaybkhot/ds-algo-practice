class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left = 0
        num_row = len(matrix)
        num_col = len(matrix[0])
        right = (num_row * num_col) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // num_col
            mid_col = mid % num_col
            if matrix[mid_row][mid_col] < target:
                left = mid + 1
            elif matrix[mid_row][mid_col] > target:
                right = mid - 1
            else:
                return True
        
        return False
        