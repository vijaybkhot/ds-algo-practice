class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check 3 X 3 Matrices
        for i in range(9):
            row_lower = 3 * (i // 3)
            row_upper = row_lower + 3
            col_lower = (i % 3) * 3
            col_upper = col_lower + 3
            count_array = [0] * 10
            for row in range(row_lower, row_upper):
                for col in range(col_lower, col_upper):
                    if board[row][col] == '.':
                        continue
                    count_array[int(board[row][col])] += 1
            if max(count_array) > 1:
                return False
        # Check rows:
        for i in range(9):
            row = i
            count_array = [0] * 10
            for col in range(9):
                if board[row][col] == '.':
                    continue
                count_array[int(board[row][col])] += 1
            if max(count_array) > 1:
                return False

        # Check columns:
        for i in range(9):
            col = i
            count_array = [0] * 10
            for row in range(9):
                if board[row][col] == '.':
                    continue
                count_array[int(board[row][col])] += 1
            if max(count_array) > 1:
                return False

        return True





