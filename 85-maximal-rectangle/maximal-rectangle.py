class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_area = 0
        n = cols

        # convert to ints
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = int(matrix[r][c])

        # build histogram heights
        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c]:
                    matrix[r][c] += matrix[r-1][c]
        
        # process each histogram row
        for row in matrix:
            stack = []
            prev_small = [0]*cols
            next_small = [0]*cols

            # prev smaller (distance)
            for idx, num in enumerate(row):
                while stack and stack[-1][0] >= num:
                    stack.pop()
                last_idx = stack[-1][1] if stack else -1
                prev_small[idx] = idx - last_idx
                stack.append((num, idx))
            
            # next smaller (distance)
            stack = []
            for idx in range(cols-1, -1, -1):
                num = row[idx]
                while stack and row[stack[-1]] >= num:
                    stack.pop()
                if stack:
                    next_small[idx] = stack[-1] - idx
                else:
                    next_small[idx] = cols - idx
                stack.append(idx)
            
            # compute max area
            for i in range(n):
                width = prev_small[i] + next_small[i] - 1
                max_area = max(max_area, width * row[i])

        return max_area
