class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # rows, cols = len(board), len(board[0])

        # def dfs(row, col, str_idx):
        #     if str_idx >= len(word):
        #         return True
        #     if row >= rows or col >= cols or row < 0 or col < 0 or board[row][col] != word[str_idx]:
        #         return False
            
        #     # Mark as visited
        #     temp = board[row][col]
        #     board[row][col] = '#'
        #     found = ( dfs(row, col+1, str_idx+1) or dfs(row, col-1, str_idx+1) or dfs(row+1, col, str_idx+1) or dfs(row-1, col, str_idx+1) )

        #     # Backtrack
        #     board[row][col] = temp
        #     return found

        

        
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if board[i][j] == word[0] and dfs(i, j, 0):
        #             return True

        # return False
        rows, cols = len(board), len(board[0])

        def dfs(pos, path):
            if len(path) == len(word):
                return True
            if pos is None:
                return False
            row, col = pos
            if board[row][col] != word[len(path)]:
                return False
            
            top = (row-1, col) if row - 1 > -1 else None
            bottom = (row+1, col) if row+1 < rows else None
            left = (row, col-1) if col-1 > -1 else None
            right = (row, col+1) if col+1 < cols else None
            
            temp = board[row][col]
            path += (board[row][col])
            board[row][col] = '#'
            found = dfs(top, path) or dfs(bottom, path) or dfs(left, path) or dfs(right, path)
            board[row][col] = temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs((r, c), ""):
                    return True
        
        return False
