class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        # r//3 + c/3

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    curr_num = board[r][c]
                    box_idx = ((r//3)*3) + int(c/3)
                    print(r//3, int(c/3), box_idx)
                    if curr_num in row_set[r] or curr_num in col_set[c] or curr_num in box_set[box_idx]:
                        return False
                    
                    row_set[r].add(curr_num)
                    col_set[c].add(curr_num)
                    box_set[box_idx].add(curr_num)
        
        return True
