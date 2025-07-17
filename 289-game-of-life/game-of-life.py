class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp = [row[:] for row in board]

        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

        for row in range(rows):
            for col in range(cols):
                live, dead = 0, 0
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if 0 <= r < rows and 0 <= c < cols:
                        if temp[r][c] == 1:
                            live += 1
                        if temp[r][c] == 0:
                            dead += 1
                if temp[row][col]:
                    if live < 2 or live > 3:
                        board[row][col] = 0
                else:
                    if live == 3:
                        board[row][col] = 1
