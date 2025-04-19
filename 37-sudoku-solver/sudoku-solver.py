class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # # First Attempt: Correct answer!
        # self.complete = False
        # row_sets = [set() for _ in range(9)]
        # col_sets = [set() for _ in range(9)]
        # grid_sets = [set() for _ in range(9)]

        # for row in range(len(board)):
        #     for col in range(len(board[0])):
        #         if board[row][col] != ".":
        #             num = int(board[row][col])
        #             grid = ((row // 3) * 3) + (col // 3)
        #             row_sets[row].add(num)
        #             col_sets[col].add(num)
        #             grid_sets[grid].add(num)
        
        # def dfs(row, col):
        #     if self.complete:
        #         return
        #     if row == 9:
        #         self.complete = True
        #         return
            
        #     if board[row][col] != ".":
        #         if col == 8:
        #             dfs(row+1, 0)
        #         else:
        #             dfs(row, col+1)
        #         return
            
        #     for i in range(1, 10):
        #         grid = ((row // 3) * 3) + (col // 3)
        #         if i not in row_sets[row] and i not in col_sets[col] and i not in grid_sets[grid]:
        #             board[row][col] = str(i)
        #             row_sets[row].add(i)
        #             col_sets[col].add(i)
        #             grid_sets[grid].add(i)

        #             if col == 8:
        #                 dfs(row+1, 0)
        #             else:
        #                 dfs(row, col+1)
        #             if not self.complete:
        #                 board[row][col] = "."
        #                 row_sets[row].remove(i)
        #                 col_sets[col].remove(i)
        #                 grid_sets[grid].remove(i)
        
        # dfs(0, 0)

        # Optimized solution: Using a separate empty cell array to traverse only the cells which are empty
        self.complete = False
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        grid_sets = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    grid = ((row // 3) * 3) + (col // 3)
                    row_sets[row].add(board[row][col])
                    col_sets[col].add(board[row][col])
                    grid_sets[grid].add(board[row][col])
        
        empty_cells = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    empty_cells.append((row, col))
        
        def dfs(index):
            if self.complete:
                return
            if index == len(empty_cells):
                self.complete = True
                return
            
            row, col = empty_cells[index]
            grid = ((row // 3) * 3) + (col // 3)
            
            for i in range(1, 10):
                str_num = str(i)
                grid = ((row // 3) * 3) + (col // 3)
                if str_num not in row_sets[row] and str_num not in col_sets[col] and str_num not in grid_sets[grid]:
                    board[row][col] = str_num
                    row_sets[row].add(str_num)
                    col_sets[col].add(str_num)
                    grid_sets[grid].add(str_num)

                    dfs(index+1)

                    if not self.complete:
                        board[row][col] = "."
                        row_sets[row].remove(str_num)
                        col_sets[col].remove(str_num)
                        grid_sets[grid].remove(str_num)
        
        dfs(0)
                                
        

                




