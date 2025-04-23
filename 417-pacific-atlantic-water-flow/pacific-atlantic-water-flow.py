class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        res = []
        
        # # Inefficient approach:
        # def dfs_pacific(pos):
        #     row, col = pos
        #     isPacific = False
        #     for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        #         r, c = row + dr, col + dc
        #         if r == -1 or c == -1:
        #             return True
        #         if r == len(heights) or c == len(heights[0]):
        #             return False
        #         if heights[r][c] <= heights[row][col]:
        #             isPacific = dfs_pacific((r, c))
        #             if isPacific:
        #                 return True
        #     return isPacific

        # def dfs_atlantic(pos):
        #     row, col = pos
        #     isAtlantic = False
        #     for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        #         r, c = row + dr, col + dc
        #         if r == len(heights) or c == len(heights[0]):
        #             return True
        #         if r == -1 or c == -1:
        #             return False
        #         if heights[r][c] <= heights[row][col]:
        #             isAtlantic = dfs_atlantic((r, c))
        #             if isAtlantic:
        #                 return True
        #     return isAtlantic
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if dfs_pacific((r, c)) and dfs_atlantic((r, c)):
        #             res.append([r, c])
        
        # return res

        # Second attempt - Working - O(m*n) Time and O(m*n) Space complexity
        pacific = set()
        atlantic = set()

        def rev_dfs_pacific(row, col, val):
            if (row, col) in pacific:
                return
            pacific.add((row, col))
            for dr, dc in[(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = row+dr, col+dc
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in pacific and heights[r][c] >= val:
                    rev_dfs_pacific(r, c, heights[r][c])
        
        def rev_dfs_atlantic(row, col, val):
            if (row, col) in atlantic:
                return
            atlantic.add((row, col))
            for dr, dc in[(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = row+dr, col+dc
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in atlantic and heights[r][c] >= val:
                    rev_dfs_atlantic(r, c, heights[r][c])



        # for r in range(rows):
        #     for c in range(cols):
        #         if (r == 0 or c == 0) and (r, c) not in pacific:
        #             rev_dfs_pacific(r, c, heights[r][c])
        #         if (r == rows-1 or c == cols-1) and (r, c) not in atlantic:
        #             rev_dfs_atlantic(r, c, heights[r][c])

        # Cleaner approach:
        for r in range(rows):
            rev_dfs_pacific(r, 0, heights[r][0])           # Left edge
            rev_dfs_atlantic(r, cols - 1, heights[r][cols - 1])  # Right edge

        for c in range(cols):
            rev_dfs_pacific(0, c, heights[0][c])           # Top edge
            rev_dfs_atlantic(rows - 1, c, heights[rows - 1][c])  # Bottom edge
        
        return [[r, c] for (r, c) in pacific if (r, c) in atlantic]
                

