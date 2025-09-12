class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_row_col(num):
            row = n - (((num-1) // n)+1)
            col = 0
            if (n-1)%2 == 0:
                if row % 2 == 0:
                    col = (num-1)%n
                else:
                    col = n - 1 - (num-1)%n
            else:
                if row % 2 != 0:
                    col = (num-1)%n
                else:
                    col = n - 1 - (num-1)%n
            return (row, col)

                    
        

        q = deque()
        q.append((1, 0))
        dest = n*n
        visited = set([1])
        while q:
            curr, moves = q.popleft()
            if curr == dest:
                return moves
            
            for i in range(1, 7):
                nxt = curr+i
                if nxt > n*n:
                    continue
                # get row, col for the number
                row, col = get_row_col(nxt)
                target = nxt if board[row][col] == -1 else board[row][col]
                if target not in visited:
                   visited.add(target)
                   q.append((target, moves+1))
                
        return -1
            
        