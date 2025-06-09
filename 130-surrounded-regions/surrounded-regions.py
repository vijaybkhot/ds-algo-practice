class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        q = deque()

        def dfs(r, c):
            board[r][c] = "N"
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if 0 <= row < rows and 0 <= col < cols and board[row][col] == "O":
                    dfs(row, col)

        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    if i == 0 or j == 0 or i == (rows-1) or j == (cols-1):
                        dfs(i, j)
        
        while q:
            r, c = q.popleft()
            board[r][c] = "N"
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if 0 <= row < rows and 0 <= col < cols and board[row][col] == "O":
                    q.append((row, col))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                     board[i][j] = "X"
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "N":
                     board[i][j] = "O"

                
     
















        # # First attempt - Working but inefficient:
        # # For each ‘O’, use DFS to check if it’s fully surrounded by ‘X’, and if so, capture the region by flipping all connected ‘O’s to ‘X’.
        # rows, cols = len(board), len(board[0])

        # def is_surrounded(i, j):
        #     visited = set()
        #     surrounded = True
        #     def dfs(row,col):
        #         nonlocal surrounded
        #         visited.add((row, col))
        #         for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        #             r, c = row+dr, col+dc
        #             if r < 0 or r >= rows or c < 0 or c >= cols:
        #                 surrounded = False
        #                 break
        #             if (r, c) not in visited and board[r][c] == "O":
        #                 dfs(r, c)
                    
        #     dfs(i, j)
        #     return surrounded
        
        # def capture(i, j):
        #     visited = set()
        #     def dfs(row,col):
        #         visited.add((row, col))
        #         board[row][col] = "X"
        #         for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        #             r, c = row+dr, col+dc
        #             if 0<= r < rows and 0 <= c < cols and board[r][c] not in visited and board[r][c] == "O":
        #                 dfs(r, c)
        #     dfs(i, j)
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] == "O" and is_surrounded(r, c):
        #             capture(r, c)

        # # Using reverse dfs approach:
        # rows, cols = len(board), len(board[0])
        
        # def rev_dfs_identify_non_region(row, col):
        #     if board[row][col] == "X" or board[row][col] == "T":
        #         return
        #     # visited.add((row, col))
        #     board[row][col] = "T"
        #     for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        #         r, c = row+dr, col+dc
        #         if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
        #             rev_dfs_identify_non_region(r, c)
        
        # for r in range(rows):
        #     rev_dfs_identify_non_region(r, 0)
        #     rev_dfs_identify_non_region(r, cols-1)
        
        # for c in range(cols):
        #     rev_dfs_identify_non_region(0, c)
        #     rev_dfs_identify_non_region(rows-1, c)
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] == "O":
        #             board[r][c] = "X"
        #         elif board[r][c] == "T":
        #             board[r][c] = "O"





            

            