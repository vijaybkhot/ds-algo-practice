class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]     # [{8, 0, 7}, {6,1}, {}, {}, {}, {}, {}, {}, {}]
        col_set = [set() for _ in range(9)]     # [{8, 6}, {0}, {}, {1}, {7}, {}, {}, {}, {}]
        box_set = [set() for _ in range(9)]     # [{8, 0, 6}, {7, 1}, {}, {}, {}, {}, {}, {}, {}]


        for r in range(9):
            for c in range(9):
                #r: 1, c: 4
                curr_num = board[r][c]  # "1"
                if curr_num == '.':
                    continue
                box_index = ((r//3)*3) + (c//3) # 1

                if curr_num in row_set[r] or curr_num in col_set[c] or curr_num in box_set[box_index]:
                    return False
                row_set[r].add(curr_num)
                col_set[c].add(curr_num)
                box_set[box_index].add(curr_num)

        return True

