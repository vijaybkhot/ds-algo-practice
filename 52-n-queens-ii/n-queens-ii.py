class Solution:
    def totalNQueens(self, n: int) -> int:
        # board = [['.']*n for row in range(n)]
        # cols = set()
        # pos_diagonals = set() # row + col
        # neg_diagonals = set() # row - col
        # self.count = 0 

        # def dfs(row, board):
        #     if row == n:
        #         self.count += 1
        #         return
            
        #     for col in range(n):
        #         if col not in cols and row+col not in pos_diagonals and row-col not in neg_diagonals:
        #             board[row][col] = 'Q'
        #             cols.add(col)
        #             pos_diagonals.add(row+col)
        #             neg_diagonals.add(row-col)

        #             dfs(row+1, board)

        #             board[row][col] = '.'
        #             cols.remove(col)
        #             pos_diagonals.remove(row + col)
        #             neg_diagonals.remove(row - col)
        
        # dfs(0, board)
        # return self.count

        board = [['.']*n for row in range(n)]
        cols = set()
        pos_dias = set()
        neg_dias = set()
        self.count = 0

        def dfs(row):
            if row == n:
                self.count += 1
                return
            
            for col in range(n):
                if col not in cols and (row+col) not in pos_dias and (row-col) not in neg_dias:
                    cols.add(col)
                    pos_dias.add(row+col)
                    neg_dias.add(row-col)
                    
                    dfs(row+1)

                    cols.remove(col)
                    pos_dias.remove(row+col)
                    neg_dias.remove(row-col)
        
        dfs(0)

        return self.count




                
                    