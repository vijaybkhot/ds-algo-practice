class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


        def dfs(row, col):
            board[row][col] = "M"
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                    # board[r][c] = "O"
                    dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows-1) or c in (0, cols-1)) and board[r][c] == "O":
                    dfs(r, c)
        
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                     board[i][j] = "X"
                elif board[i][j] == "M":
                     board[i][j] = "O"
        