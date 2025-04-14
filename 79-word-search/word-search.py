class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])

        def dfs(row, col, str_idx):
            if str_idx >= len(word):
                return True
            if row >= rows or col >= cols or row < 0 or col < 0 or board[row][col] != word[str_idx]:
                return False
            
            # Mark as visited
            temp = board[row][col]
            board[row][col] = '#'
            found = ( dfs(row, col+1, str_idx+1) or dfs(row, col-1, str_idx+1) or dfs(row+1, col, str_idx+1) or dfs(row-1, col, str_idx+1) )

            # Backtrack
            board[row][col] = temp
            return found

        

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False
        