class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [['.']*n for row in range(n)]
        # res = []

        # cols = set()
        # pos_diagonals = set()  # row + col
        # neg_diagonals = set()   # row - col

        # def dfs(row, board):
        #     if row == n:
        #         res.append([''.join(row) for row in board])
        #         return

        #     for col in range(n):
        #         # Find queen position
        #         if col not in cols and row + col not in  pos_diagonals and row - col not in neg_diagonals:
        #             board[row][col] = 'Q'
        #             cols.add(col)
        #             pos_diagonals.add(row + col)
        #             neg_diagonals.add(row - col)

        #             # Find queen position for the next row
        #             dfs(row+1, board)
                    
        #             # Backtrack
        #             board[row][col] = '.'
        #             cols.remove(col)
        #             pos_diagonals.remove(row + col)
        #             neg_diagonals.remove(row - col)
                    

        # dfs(0, board)
        # return res

        board = [['.']*n for _ in range(n)]
        cols = set()
        pos_dias = set()
        neg_dias = set()
        res = []
        def dfs(row, board):
            if row == n:
                res.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if col not in cols and (row + col) not in pos_dias and (row-col) not in neg_dias:
                    board[row][col] = 'Q'
                    cols.add(col)
                    pos_dias.add(row+col)
                    neg_dias.add(row-col)
                    dfs(row+1, board)
                    board[row][col] = '.'
                    cols.remove(col)
                    pos_dias.remove(row+col)
                    neg_dias.remove(row-col)
            
        dfs(0, board)
        return res 
