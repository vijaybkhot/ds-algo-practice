class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.complete = False
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        grid_sets = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    num = int(board[row][col])
                    grid = ((row // 3) * 3) + (col // 3)
                    row_sets[row].add(num)
                    col_sets[col].add(num)
                    grid_sets[grid].add(num)
        
        def dfs(row, col):
            if self.complete:
                return
            if row == 9:
                self.complete = True
                return
            
            if board[row][col] != ".":
                if col == 8:
                    dfs(row+1, 0)
                else:
                    dfs(row, col+1)
                return
            
            for i in range(1, 10):
                grid = ((row // 3) * 3) + (col // 3)
                if i not in row_sets[row] and i not in col_sets[col] and i not in grid_sets[grid]:
                    board[row][col] = str(i)
                    row_sets[row].add(i)
                    col_sets[col].add(i)
                    grid_sets[grid].add(i)

                    if col == 8:
                        dfs(row+1, 0)
                    else:
                        dfs(row, col+1)
                    if not self.complete:
                        board[row][col] = "."
                        row_sets[row].remove(i)
                        col_sets[col].remove(i)
                        grid_sets[grid].remove(i)
        
        dfs(0, 0)
                                
        

                




