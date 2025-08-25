class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        clockwise = True
        res = []
        curr = (0, 0)
       

        while True:
            row, col = curr
            res.append(mat[row][col])
            if row == rows-1 and col == cols-1:
                return res
            if clockwise:
                if 0 <= row-1 < rows and 0 <= col+1 < cols:
                    curr = (row-1, col+1)
                else:
                    if 0 <= col+1 < cols:
                        curr = (row, col+1)
                    else:
                        curr = (row+1, col)
                    clockwise = False
            else:
                if 0 <= row+1 < rows and 0 <= col-1 < cols:
                    curr = (row+1, col-1)
                else:
                    if 0 <= row+1 < rows:
                        curr = (row+1, col)
                    else:
                        curr = (row, col+1)
                    clockwise = True

        return res

                    
                        
                
            
