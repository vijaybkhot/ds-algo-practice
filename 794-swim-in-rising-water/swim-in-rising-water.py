class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # # Using Binary Search to find the minimum time - First Attemtp
        # max_grid, min_grid = float('-inf'), float('inf')
        # # Find max and min
        # for r in range(rows):
        #     for c in range(cols):
        #         max_grid = max(max_grid, grid[r][c])
        #         min_grid = min(min_grid, grid[r][c])
            
        # def dfs(pos, val):
        #     row, col = pos
        #     if grid[row][col] > val:
        #         return False
        #     if (row, col) in visited:
        #         return False
        #     visited.add((row, col))
        #     if row == rows-1 and col == cols - 1:
        #         return True
        #     isPath = False
        #     for dr, dc in directions:
        #         r, c = row + dr, col + dc
        #         if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] <= val:
        #             isPath = dfs((r, c), val)
        #             if isPath:
        #                 return True
        #     return isPath
        
        # left, right = min_grid, max_grid
        # while left <= right:
        #     mid = (left + right) // 2
        #     visited = set()
        #     if dfs((0, 0), mid):
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # return left

        # Using Djikstras algorithm
        heap = [(grid[0][0], 0, 0)]
        max_time = grid[0][0]
        visited = set()

        while heap:
            curr_time, row, col = heapq.heappop(heap)
            max_time = max(max_time, curr_time)
            if row == rows-1 and col == cols-1:
                return max_time
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    heapq.heappush(heap, (grid[r][c], r, c))
                    visited.add((r, c))




        