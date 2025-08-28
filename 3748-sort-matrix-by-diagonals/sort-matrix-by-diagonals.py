class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        diags = defaultdict(list)

        # group by diagonal key r-c
        for r in range(m):
            for c in range(n):
                diags[r - c].append(grid[r][c])

        # sort descending so pop() returns smallest -> fills diagonals ascending
        for k in diags:
            if k >= 0:
                diags[k].sort()            # ascending -> pop() gives largest first
            else:
                diags[k].sort(reverse=True)

        for r in range(m):
            for c in range(n):
                grid[r][c] = diags[r - c].pop()

        return grid
