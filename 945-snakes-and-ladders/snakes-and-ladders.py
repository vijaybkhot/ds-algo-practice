class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

       
        n = len(board)

        def get_coordinates(pos):
            row = n - 1 - (pos - 1) // n
            col_offset = (pos - 1) % n

            if (n - 1 - row) % 2 == 0:  # even row index from bottom → left to right
                col = col_offset
            else:  # odd row index from bottom → right to left
                col = n - 1 - col_offset

            return (row, col)

        # Edge case: if starting cell has a ladder/snake
        if board[n - 1][0] != -1:
            return -1

        q = deque()
        q.append((1, 0))  # (square_number, num_rolls)
        visited = set()
        visited.add(1)

        while q:
            pos, num_rolls = q.popleft()
            if pos == n * n:
                return num_rolls
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > n * n:
                    continue
                row, col = get_coordinates(next_pos)
                dest = board[row][col] if board[row][col] != -1 else next_pos
                if dest not in visited:
                    visited.add(dest)
                    q.append((dest, num_rolls + 1))

        return -1
        
            
                
                
            
