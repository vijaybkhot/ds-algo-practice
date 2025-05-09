class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        one_sec = False
        visited = set()
        visited.add((0, 0, one_sec))
        heap = [(0, 0, 0, one_sec)]

        while heap:
            curr_cell_time, row, col, one_sec = heapq.heappop(heap)
            if row == rows-1 and col == cols-1:
                return curr_cell_time
            
            additional_move_time = 1 if not one_sec else 2
            one_sec = not one_sec
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if 0 <= r < rows and 0 <= c < cols and (r, c, one_sec) not in visited:
                    move_diff = moveTime[r][c] - curr_cell_time
                    new_cell_time = (curr_cell_time + move_diff + additional_move_time) if move_diff > 0 else additional_move_time + curr_cell_time
                    heapq.heappush(heap, (new_cell_time, r, c, one_sec))
                    visited.add((r, c, one_sec))

            
           



