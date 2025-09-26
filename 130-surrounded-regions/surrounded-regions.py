class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, mark):
            board[r][c] = mark
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    dfs(nr, nc, mark)



        # Get uncaptured border regions
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows-1 or c == cols-1:
                    if board[r][c] == "O":
                        dfs(r, c, "N")
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"
        

