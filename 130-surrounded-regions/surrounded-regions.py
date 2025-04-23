class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def is_surrounded(i, j):
            visited = set()
            surrounded = True
            def dfs(row,col):
                nonlocal surrounded
                visited.add((row, col))
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = row+dr, col+dc
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        surrounded = False
                        break
                    if (r, c) not in visited and board[r][c] == "O":
                        dfs(r, c)
                    
            dfs(i, j)
            return surrounded
        
        def capture(i, j):
            visited = set()
            def dfs(row,col):
                visited.add((row, col))
                board[row][col] = "X"
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = row+dr, col+dc
                    if 0<= r < rows and 0 <= c < cols and board[r][c] not in visited and board[r][c] == "O":
                        dfs(r, c)
            dfs(i, j)
        
        for r in range(rows):
            for c in range(cols):
                if is_surrounded(r, c):
                    capture(r, c)
            

            