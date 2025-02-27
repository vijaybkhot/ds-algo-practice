class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Came up with this solution without any external help!
        # Used a set instead of a count array
        # Check 3 X 3 Matrices
        for i in range(9):
            row_lower = 3 * (i // 3)
            row_upper = row_lower + 3
            col_lower = (i % 3) * 3
            col_upper = col_lower + 3
            num_set = set()
            for row in range(row_lower, row_upper):
                for col in range(col_lower, col_upper):
                    num = board[row][col]
                    if num == '.':
                        continue
                    if num in num_set:
                        return False
                    num_set.add(num)
        # Check rows:
        for i in range(9):
            row = i
            num_set = set()
            for col in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                if num in num_set:
                    return False
                num_set.add(num) 

        # Check columns:
        for i in range(9):
            col = i
            num_set = set()
            for row in range(9):
                num = board[row][col]
                if num == '.':
                    continue
                if num in num_set:
                    return False
                num_set.add(num) 

        return True





