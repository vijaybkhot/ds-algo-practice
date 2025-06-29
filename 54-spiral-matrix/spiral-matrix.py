class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        res = []
        while top <= bottom and left <= right:
            # move from left to right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            # Move from top to bottom
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            # Move from right to left
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # Move from bottom to top
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
