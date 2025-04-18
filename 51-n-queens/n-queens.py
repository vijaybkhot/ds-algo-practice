class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for row in range(n)]
        res = []

        cols = set()
        pos_diagonals = set()  # row + col
        neg_diagonals = set()   # row - col

        def dfs(row, board):
            if row == n:
                res.append([''.join(row) for row in board])
                return

            for col in range(n):
                if col not in cols and row + col not in  pos_diagonals and row - col not in neg_diagonals:
                    board[row][col] = 'Q'
                    cols.add(col)
                    pos_diagonals.add(row + col)
                    neg_diagonals.add(row - col)

                    dfs(row+1, board)
                    
                    # Backtrack
                    board[row][col] = '.'
                    cols.remove(col)
                    pos_diagonals.remove(row + col)
                    neg_diagonals.remove(row - col)
                    

        dfs(0, board)
        return res


