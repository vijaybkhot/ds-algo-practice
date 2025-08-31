class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    box_idx = ((r//3)*3) + c // 3
                    num = board[r][c]
                    row_set[r].add(num)
                    col_set[c].add(num)
                    box_set[box_idx].add(num)
    

        def dfs(r, c):
            if r == 9:
                return True  # solved entire board

            if c == 9:
                return dfs(r + 1, 0)  # move to next row

            if board[r][c] == '.':
                for i in range(1, 10):
                    num = str(i)
                    box_idx = (r // 3) * 3 + (c // 3)
                    if num not in row_set[r] and num not in col_set[c] and num not in box_set[box_idx]:
                        # place number
                        board[r][c] = num
                        row_set[r].add(num)
                        col_set[c].add(num)
                        box_set[box_idx].add(num)

                        if dfs(r, c + 1):  # move to next cell
                            return True

                        # backtrack
                        board[r][c] = '.'
                        row_set[r].remove(num)
                        col_set[c].remove(num)
                        box_set[box_idx].remove(num)

                return False
            else:
                return dfs(r, c + 1)  # move to next cell if prefilled

        dfs(0, 0)
