class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        
        top, left = 0, 0
        bottom, right = n-1, n-1
        start = 0

        while left <= right and top <= bottom:
            x = top
            for y in range(left, right+1):
                start += 1
                matrix[x][y] = start
            
            top += 1

            y = right
            for x in range(top, bottom+1):
                start += 1
                matrix[x][y] = start
            right -= 1

            if right >= left and bottom >= top:
                x = bottom
                for y in range(right, left-1, -1):
                    start += 1
                    matrix[x][y] = start
                bottom -= 1

            if right >= left and bottom >= top:
                y = left
                for x in range(bottom, top-1, -1):
                    start += 1
                    matrix[x][y] = start
                left += 1
        
        return matrix



