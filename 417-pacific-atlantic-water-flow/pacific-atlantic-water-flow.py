class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        pacific = set()
        atlantic = set()

        def dfs(row, col, curr_set):
            if (row, col) in curr_set:
                return 
            curr_set.add((row, col))

            for dr, dc in directions:
                nr, nc = dr+row, dc+col
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in curr_set and heights[nr][nc] >= heights[row][col]:
                    dfs(nr, nc, curr_set)


        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0) and (r, c) not in pacific:
                    dfs(r, c, pacific)
                
                if (r == rows-1 or c == cols-1) and (r, c) not in atlantic:
                    dfs(r, c, atlantic)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res

                